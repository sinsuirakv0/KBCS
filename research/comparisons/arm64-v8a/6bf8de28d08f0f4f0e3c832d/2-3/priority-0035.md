# v16.0.2 → v16.0.3 · 最優先の変更候補 (35)

[一覧の目次](README.md)

<a id="compare-4000fb7a0ed0158e2390ba4ed5b35d7d"></a>

### [`006fd974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd974.md) → [`006fdd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fdd24.md) FUN_006fdd24

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fdd38",
      "incomplete_value": false,
      "site": "006fdd3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fd988",
      "incomplete_value": false,
      "site": "006fd98c",
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
            "const:d68:8"
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
      "006fdd3c",
      "DATA",
      [
        "storage",
        "00c76d68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fdd3c",
      "DATA",
      [
        "storage",
        "00c77d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fd980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd974.md#insn-006fd980) · [`006fd984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd974.md#insn-006fd984) · [`006fd988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd974.md#insn-006fd988)
- 新版 [`006fdd30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fdd24.md#insn-006fdd30) · [`006fdd34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fdd24.md#insn-006fdd34) · [`006fdd38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fdd24.md#insn-006fdd38)

~~~diff
- 006fd980 ["INT_ADD", "register:40f0:8", ["const:6fd980:8", "const:4:8"]]
- 006fd980 ["CALL", null, ["callee:00c58f30:8"]]
+ 006fdd30 ["INT_ADD", "register:40f0:8", ["const:6fdd30:8", "const:4:8"]]
+ 006fdd30 ["CALL", null, ["callee:00c58f30:8"]]
- 006fd980 bytes 78691594
+ 006fdd30 bytes 806c1594
- 006fd984 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fdd34 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fd984 bytes c82b00b0
+ 006fdd34 bytes c82b00d0
- 006fd988 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 006fd988 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fd988 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fd988 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fdd38 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 006fdd38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fdd38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fdd38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fd988 bytes 08a13591
+ 006fdd38 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faafee773ae514f4f55ae8e9337fdacf"></a>

### [`006fd9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd9b0.md) → [`006fdd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fdd60.md) FUN_006fdd60

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
      "site": "006fdd7c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd9cc",
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
      "006fdd7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006fdd7c",
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

- 旧版 [`006fd9cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd9b0.md#insn-006fd9cc) · [`006fd9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd9b0.md#insn-006fd9d8)
- 新版 [`006fdd7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fdd60.md#insn-006fdd7c) · [`006fdd88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fdd60.md#insn-006fdd88)

~~~diff
- 006fd9cc ["INT_ADD", "register:40f0:8", ["const:6fd9cc:8", "const:4:8"]]
- 006fd9cc ["CALL", null, ["ram:47ad34:8"]]
+ 006fdd7c ["INT_ADD", "register:40f0:8", ["const:6fdd7c:8", "const:4:8"]]
+ 006fdd7c ["CALL", null, ["ram:47b054:8"]]
- 006fd9cc bytes daf4f597
+ 006fdd7c bytes b6f4f597
- 006fd9d8 ["INT_ADD", "register:40f0:8", ["const:6fd9d8:8", "const:4:8"]]
- 006fd9d8 ["CALL", null, ["callee:0047d134:8"]]
+ 006fdd88 ["INT_ADD", "register:40f0:8", ["const:6fdd88:8", "const:4:8"]]
+ 006fdd88 ["CALL", null, ["callee:0047d134:8"]]
- 006fd9d8 bytes 0ffdf597
+ 006fdd88 bytes ebfcf597
~~~


<a id="compare-a6fabe4cadf91ae834ad7852a8d444e6"></a>

### [`006fda1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fda1c.md) → [`006fddcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fddcc.md) FUN_006fddcc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "006fddf0",
      "incomplete_value": false,
      "site": "006fddf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fda40",
      "incomplete_value": false,
      "site": "006fda44",
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
            "const:de8:8"
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
      "006fddf4",
      "DATA",
      [
        "storage",
        "00c76de8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fddf4",
      "DATA",
      [
        "storage",
        "00c77db8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fda30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fda1c.md#insn-006fda30) · [`006fda3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fda1c.md#insn-006fda3c) · [`006fda40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fda1c.md#insn-006fda40)
- 新版 [`006fdde0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fddcc.md#insn-006fdde0) · [`006fddec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fddcc.md#insn-006fddec) · [`006fddf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fddcc.md#insn-006fddf0)

~~~diff
- 006fda30 ["INT_ADD", "register:40f0:8", ["const:6fda30:8", "const:4:8"]]
- 006fda30 ["CALL", null, ["callee:00c58f30:8"]]
+ 006fdde0 ["INT_ADD", "register:40f0:8", ["const:6fdde0:8", "const:4:8"]]
+ 006fdde0 ["CALL", null, ["callee:00c58f30:8"]]
- 006fda30 bytes 4c691594
+ 006fdde0 bytes 546c1594
- 006fda3c ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fddec ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fda3c bytes c82b00b0
+ 006fddec bytes c82b00d0
- 006fda40 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 006fda40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fda40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fda40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fddf0 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 006fddf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fddf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fddf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fda40 bytes 08a13791
+ 006fddf0 bytes 08e13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2805a34c2b792bf7ebb64c7cf2c8ec8"></a>

### [`006fda84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fda84.md) → [`006fde34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fde34.md) FUN_006fde34

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 21件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044d730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d730.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fdf38",
      "incomplete_value": true,
      "site": "006fdf4c",
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
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:fee:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fdb88",
      "incomplete_value": true,
      "site": "006fdb9c",
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
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fdf8c",
      "incomplete_value": true,
      "site": "006fdf8c",
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
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:d15:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fdbdc",
      "incomplete_value": true,
      "site": "006fdbdc",
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
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:c37:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fdf90",
      "incomplete_value": true,
      "site": "006fdf90",
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
      "definition_site": "006fdbe0",
      "incomplete_value": true,
      "site": "006fdbe0",
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
    "ordinal": 18,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fde80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006fdee0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ede3c"
      ]
    ],
    [
      "006fdef0",
      "DATA",
      [
        "storage",
        "0042ef82",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "006fde80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006fdee0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ee1ec"
      ]
    ],
    [
      "006fdef0",
      "DATA",
      [
        "storage",
        "0042ef82",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fdad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fda84.md#insn-006fdad0) · [`006fdb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fda84.md#insn-006fdb30) · [`006fdb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fda84.md#insn-006fdb54)
- 新版 [`006fde80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fde34.md#insn-006fde80) · [`006fdee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fde34.md#insn-006fdee0) · [`006fdf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fde34.md#insn-006fdf04)

~~~diff
- 006fdad0 ["INT_ADD", "register:40f0:8", ["const:6fdad0:8", "const:4:8"]]
- 006fdad0 ["CALL", null, ["ram:47ad34:8"]]
+ 006fde80 ["INT_ADD", "register:40f0:8", ["const:6fde80:8", "const:4:8"]]
+ 006fde80 ["CALL", null, ["ram:47b054:8"]]
- 006fdad0 bytes 99f4f597
+ 006fde80 bytes 75f4f597
- 006fdb30 ["INT_ADD", "register:40f0:8", ["const:6fdb30:8", "const:4:8"]]
- 006fdb30 ["CALL", null, ["ram:6ede3c:8"]]
+ 006fdee0 ["INT_ADD", "register:40f0:8", ["const:6fdee0:8", "const:4:8"]]
+ 006fdee0 ["CALL", null, ["ram:6ee1ec:8"]]
- 006fdb30 bytes c3c0ff97
+ 006fdee0 bytes c3c0ff97
- 006fdb54 ["INT_ADD", "register:40f0:8", ["const:6fdb54:8", "const:4:8"]]
- 006fdb54 ["CALL", null, ["ram:63c5c8:8"]]
+ 006fdf04 ["INT_ADD", "register:40f0:8", ["const:6fdf04:8", "const:4:8"]]
+ 006fdf04 ["CALL", null, ["ram:63c978:8"]]
- 006fdb54 bytes 9dfafc97
+ 006fdf04 bytes 9dfafc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd9465ea13ac92ecb78b881f601366e2"></a>

### [`006fe190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe190.md) → [`006fe540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe540.md) FUN_006fe540

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
      "definition_site": "006fe560",
      "incomplete_value": false,
      "site": "006fe564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe1b0",
      "incomplete_value": false,
      "site": "006fe1b4",
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
            "const:e58:8"
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
      "006fe564",
      "DATA",
      [
        "storage",
        "00c76e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe564",
      "DATA",
      [
        "storage",
        "00c77e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe190.md#insn-006fe1a4) · [`006fe1ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe190.md#insn-006fe1ac) · [`006fe1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe190.md#insn-006fe1b0)
- 新版 [`006fe554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe540.md#insn-006fe554) · [`006fe55c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe540.md#insn-006fe55c) · [`006fe560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe540.md#insn-006fe560)

~~~diff
- 006fe1a4 ["INT_ADD", "register:40f0:8", ["const:6fe1a4:8", "const:4:8"]]
- 006fe1a4 ["CALL", null, ["callee:00c58f30:8"]]
+ 006fe554 ["INT_ADD", "register:40f0:8", ["const:6fe554:8", "const:4:8"]]
+ 006fe554 ["CALL", null, ["callee:00c58f30:8"]]
- 006fe1a4 bytes 6f671594
+ 006fe554 bytes 776a1594
- 006fe1ac ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fe55c ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fe1ac bytes c82b0090
+ 006fe55c bytes c82b00b0
- 006fe1b0 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 006fe1b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe1b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe1b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe560 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 006fe560 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe560 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe560 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe1b0 bytes 08613991
+ 006fe560 bytes 08a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb8fe080ba3df95daa200cccd5c2247f"></a>

### [`006fe1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe1c8.md) → [`006fe578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe578.md) FUN_006fe578

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
      "definition_site": "006fe57c",
      "incomplete_value": false,
      "site": "006fe580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe1cc",
      "incomplete_value": false,
      "site": "006fe1d0",
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
            "const:e58:8"
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
      "006fe580",
      "DATA",
      [
        "storage",
        "00c76e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe580",
      "DATA",
      [
        "storage",
        "00c77e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe1c8.md#insn-006fe1c8) · [`006fe1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe1c8.md#insn-006fe1cc)
- 新版 [`006fe578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe578.md#insn-006fe578) · [`006fe57c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe578.md#insn-006fe57c)

~~~diff
- 006fe1c8 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fe578 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fe1c8 bytes c82b0090
+ 006fe578 bytes c82b00b0
- 006fe1cc ["COPY", "tmp:0:8", ["const:e58:8"]]
- 006fe1cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe1cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe1cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe57c ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 006fe57c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe57c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe57c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe1cc bytes 08613991
+ 006fe57c bytes 08a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6973f2afbc39a38b79d102aed7c5709"></a>

### [`006fe1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe1e8.md) → [`006fe598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe598.md) FUN_006fe598

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) [`006f0558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f0558.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) [`006f0908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f0/006f0908.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

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
      "site": "006fe5c4",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe214",
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
      "site": "006fe618",
      "value": [
        "leaf",
        "ram:6f0908:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe268",
      "value": [
        "leaf",
        "ram:6f0558:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe5c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006fe618",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f0558"
      ]
    ]
  ],
  "added": [
    [
      "006fe5c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006fe618",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f0908"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe1e8.md#insn-006fe214) · [`006fe268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe1e8.md#insn-006fe268) · [`006fe220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe1e8.md#insn-006fe220)
- 新版 [`006fe5c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe598.md#insn-006fe5c4) · [`006fe618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe598.md#insn-006fe618) · [`006fe5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe598.md#insn-006fe5d0)

~~~diff
- 006fe214 ["INT_ADD", "register:40f0:8", ["const:6fe214:8", "const:4:8"]]
- 006fe214 ["CALL", null, ["ram:47ad34:8"]]
+ 006fe5c4 ["INT_ADD", "register:40f0:8", ["const:6fe5c4:8", "const:4:8"]]
+ 006fe5c4 ["CALL", null, ["ram:47b054:8"]]
- 006fe214 bytes c8f2f597
+ 006fe5c4 bytes a4f2f597
- 006fe268 ["INT_ADD", "register:40f0:8", ["const:6fe268:8", "const:4:8"]]
- 006fe268 ["CALL", null, ["ram:6f0558:8"]]
+ 006fe618 ["INT_ADD", "register:40f0:8", ["const:6fe618:8", "const:4:8"]]
+ 006fe618 ["CALL", null, ["ram:6f0908:8"]]
- 006fe268 bytes bcc8ff97
+ 006fe618 bytes bcc8ff97
- 006fe220 ["INT_ADD", "register:40f0:8", ["const:6fe220:8", "const:4:8"]]
- 006fe220 ["CALL", null, ["callee:0047d134:8"]]
+ 006fe5d0 ["INT_ADD", "register:40f0:8", ["const:6fe5d0:8", "const:4:8"]]
+ 006fe5d0 ["CALL", null, ["callee:0047d134:8"]]
- 006fe220 bytes fdfaf597
+ 006fe5d0 bytes d9faf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fdf56ac326b1584d65e8e6f1d6d50a1"></a>

### [`006fe2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe2c8.md) → [`006fe678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe678.md) FUN_006fe678

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
      "definition_site": "006fe698",
      "incomplete_value": false,
      "site": "006fe69c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe2e8",
      "incomplete_value": false,
      "site": "006fe2ec",
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
            "const:ee8:8"
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
      "006fe69c",
      "DATA",
      [
        "storage",
        "00c76ee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe69c",
      "DATA",
      [
        "storage",
        "00c77eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe2c8.md#insn-006fe2dc) · [`006fe2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe2c8.md#insn-006fe2e4) · [`006fe2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe2c8.md#insn-006fe2e8)
- 新版 [`006fe68c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe678.md#insn-006fe68c) · [`006fe694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe678.md#insn-006fe694) · [`006fe698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe678.md#insn-006fe698)

~~~diff
- 006fe2dc ["INT_ADD", "register:40f0:8", ["const:6fe2dc:8", "const:4:8"]]
- 006fe2dc ["CALL", null, ["callee:00c58f30:8"]]
+ 006fe68c ["INT_ADD", "register:40f0:8", ["const:6fe68c:8", "const:4:8"]]
+ 006fe68c ["CALL", null, ["callee:00c58f30:8"]]
- 006fe2dc bytes 21671594
+ 006fe68c bytes 296a1594
- 006fe2e4 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fe694 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fe2e4 bytes c82b0090
+ 006fe694 bytes c82b00b0
- 006fe2e8 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 006fe2e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe2e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe2e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe698 ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 006fe698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe2e8 bytes 08a13b91
+ 006fe698 bytes 08e13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c67d8b7eae2991dc710cdb26089ee5a6"></a>

### [`006fe4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe4ec.md) → [`006fe89c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe89c.md) FUN_006fe89c

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
      "definition_site": "006fe8bc",
      "incomplete_value": false,
      "site": "006fe8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe50c",
      "incomplete_value": false,
      "site": "006fe510",
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
            "const:f68:8"
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
      "006fe8c0",
      "DATA",
      [
        "storage",
        "00c76f68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe8c0",
      "DATA",
      [
        "storage",
        "00c77f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe4ec.md#insn-006fe500) · [`006fe508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe4ec.md#insn-006fe508) · [`006fe50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe4ec.md#insn-006fe50c)
- 新版 [`006fe8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe89c.md#insn-006fe8b0) · [`006fe8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe89c.md#insn-006fe8b8) · [`006fe8bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe89c.md#insn-006fe8bc)

~~~diff
- 006fe500 ["INT_ADD", "register:40f0:8", ["const:6fe500:8", "const:4:8"]]
- 006fe500 ["CALL", null, ["callee:00c58f30:8"]]
+ 006fe8b0 ["INT_ADD", "register:40f0:8", ["const:6fe8b0:8", "const:4:8"]]
+ 006fe8b0 ["CALL", null, ["callee:00c58f30:8"]]
- 006fe500 bytes 98661594
+ 006fe8b0 bytes a0691594
- 006fe508 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fe8b8 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fe508 bytes c82b0090
+ 006fe8b8 bytes c82b00b0
- 006fe50c ["COPY", "tmp:0:8", ["const:f68:8"]]
- 006fe50c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe50c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe50c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe8bc ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 006fe8bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe8bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe8bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe50c bytes 08a13d91
+ 006fe8bc bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74dddb751d2fff7d7f1ea51a8c75c4fc"></a>

### [`006fe544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe544.md) → [`006fe8f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe8f4.md) FUN_006fe8f4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) [`006f0558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f0558.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) [`006f0908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f0/006f0908.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

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
      "site": "006fe91c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe56c",
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
      "site": "006fe960",
      "value": [
        "leaf",
        "ram:6f0908:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe5b0",
      "value": [
        "leaf",
        "ram:6f0558:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe91c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006fe960",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f0558"
      ]
    ]
  ],
  "added": [
    [
      "006fe91c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006fe960",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f0908"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe544.md#insn-006fe56c) · [`006fe5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe544.md#insn-006fe5b0) · [`006fe578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe544.md#insn-006fe578)
- 新版 [`006fe91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe8f4.md#insn-006fe91c) · [`006fe960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe8f4.md#insn-006fe960) · [`006fe928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe8f4.md#insn-006fe928)

~~~diff
- 006fe56c ["INT_ADD", "register:40f0:8", ["const:6fe56c:8", "const:4:8"]]
- 006fe56c ["CALL", null, ["ram:47ad34:8"]]
+ 006fe91c ["INT_ADD", "register:40f0:8", ["const:6fe91c:8", "const:4:8"]]
+ 006fe91c ["CALL", null, ["ram:47b054:8"]]
- 006fe56c bytes f2f1f597
+ 006fe91c bytes cef1f597
- 006fe5b0 ["INT_ADD", "register:40f0:8", ["const:6fe5b0:8", "const:4:8"]]
- 006fe5b0 ["CALL", null, ["ram:6f0558:8"]]
+ 006fe960 ["INT_ADD", "register:40f0:8", ["const:6fe960:8", "const:4:8"]]
+ 006fe960 ["CALL", null, ["ram:6f0908:8"]]
- 006fe5b0 bytes eac7ff97
+ 006fe960 bytes eac7ff97
- 006fe578 ["INT_ADD", "register:40f0:8", ["const:6fe578:8", "const:4:8"]]
- 006fe578 ["CALL", null, ["callee:0047d134:8"]]
+ 006fe928 ["INT_ADD", "register:40f0:8", ["const:6fe928:8", "const:4:8"]]
+ 006fe928 ["CALL", null, ["callee:0047d134:8"]]
- 006fe578 bytes 27faf597
+ 006fe928 bytes 03faf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62081af89586d317beb6494ea0c05f79"></a>

### [`006fe604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe604.md) → [`006fe9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe9b4.md) FUN_006fe9b4

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
      "definition_site": "006fe9d4",
      "incomplete_value": false,
      "site": "006fe9d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe624",
      "incomplete_value": false,
      "site": "006fe628",
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
            "const:fe8:8"
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
      "006fe9d8",
      "DATA",
      [
        "storage",
        "00c76fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe9d8",
      "DATA",
      [
        "storage",
        "00c77fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe604.md#insn-006fe618) · [`006fe620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe604.md#insn-006fe620) · [`006fe624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe604.md#insn-006fe624)
- 新版 [`006fe9c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe9b4.md#insn-006fe9c8) · [`006fe9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe9b4.md#insn-006fe9d0) · [`006fe9d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fe9b4.md#insn-006fe9d4)

~~~diff
- 006fe618 ["INT_ADD", "register:40f0:8", ["const:6fe618:8", "const:4:8"]]
- 006fe618 ["CALL", null, ["callee:00c58f30:8"]]
+ 006fe9c8 ["INT_ADD", "register:40f0:8", ["const:6fe9c8:8", "const:4:8"]]
+ 006fe9c8 ["CALL", null, ["callee:00c58f30:8"]]
- 006fe618 bytes 52661594
+ 006fe9c8 bytes 5a691594
- 006fe620 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fe9d0 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fe620 bytes c82b0090
+ 006fe9d0 bytes c82b00b0
- 006fe624 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 006fe624 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe624 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe624 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe9d4 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 006fe9d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe9d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe9d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe624 bytes 08a13f91
+ 006fe9d4 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f172f5f9492fdfc79a06f68aea207be"></a>

### [`006fe65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe65c.md) → [`006fea0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fea0c.md) FUN_006fea0c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`006e542c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e542c.md) [`006ef79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ef/006ef79c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`006e57dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e5/006e57dc.md) [`006efb4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ef/006efb4c.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006feb10",
      "incomplete_value": true,
      "site": "006feb20",
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
                "const:7fd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe760",
      "incomplete_value": true,
      "site": "006fe770",
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
                "const:71f:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006feb3c",
      "incomplete_value": false,
      "site": "006feb44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe78c",
      "incomplete_value": false,
      "site": "006fe794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fea48",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe698",
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
      "006fea48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006fea68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006fead4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ef79c"
      ]
    ]
  ],
  "added": [
    [
      "006fea48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006fea68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006fead4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006efb4c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe65c.md#insn-006fe698) · [`006fe6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe65c.md#insn-006fe6b8) · [`006fe6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe65c.md#insn-006fe6e0)
- 新版 [`006fea48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fea0c.md#insn-006fea48) · [`006fea68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fea0c.md#insn-006fea68) · [`006fea90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fea0c.md#insn-006fea90)

~~~diff
- 006fe698 ["INT_ADD", "register:40f0:8", ["const:6fe698:8", "const:4:8"]]
- 006fe698 ["CALL", null, ["ram:47ad34:8"]]
+ 006fea48 ["INT_ADD", "register:40f0:8", ["const:6fea48:8", "const:4:8"]]
+ 006fea48 ["CALL", null, ["ram:47b054:8"]]
- 006fe698 bytes a7f1f597
+ 006fea48 bytes 83f1f597
- 006fe6b8 ["INT_ADD", "register:40f0:8", ["const:6fe6b8:8", "const:4:8"]]
- 006fe6b8 ["CALL", null, ["ram:47ad34:8"]]
+ 006fea68 ["INT_ADD", "register:40f0:8", ["const:6fea68:8", "const:4:8"]]
+ 006fea68 ["CALL", null, ["ram:47b054:8"]]
- 006fe6b8 bytes 9ff1f597
+ 006fea68 bytes 7bf1f597
- 006fe6e0 ["INT_ADD", "register:40f0:8", ["const:6fe6e0:8", "const:4:8"]]
- 006fe6e0 ["CALL", null, ["callee:008524fc:8"]]
+ 006fea90 ["INT_ADD", "register:40f0:8", ["const:6fea90:8", "const:4:8"]]
+ 006fea90 ["CALL", null, ["callee:008524fc:8"]]
- 006fe6e0 bytes 9c4b0594
+ 006fea90 bytes 9b4e0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4d2261c54f2a96f6dd5992bedff79e4"></a>

### [`006fe8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe8ec.md) → [`006fec9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fec9c.md) FUN_006fec9c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fecb0",
      "incomplete_value": false,
      "site": "006fecb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe900",
      "incomplete_value": false,
      "site": "006fe904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "006fecb4",
      "DATA",
      [
        "storage",
        "00c77058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fecb4",
      "DATA",
      [
        "storage",
        "00c78028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe8ec.md#insn-006fe8f8) · [`006fe8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe8ec.md#insn-006fe8fc) · [`006fe900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe8ec.md#insn-006fe900)
- 新版 [`006feca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fec9c.md#insn-006feca8) · [`006fecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fec9c.md#insn-006fecac) · [`006fecb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fec9c.md#insn-006fecb0)

~~~diff
- 006fe8f8 ["INT_ADD", "register:40f0:8", ["const:6fe8f8:8", "const:4:8"]]
- 006fe8f8 ["CALL", null, ["callee:00c58f30:8"]]
+ 006feca8 ["INT_ADD", "register:40f0:8", ["const:6feca8:8", "const:4:8"]]
+ 006feca8 ["CALL", null, ["callee:00c58f30:8"]]
- 006fe8f8 bytes 9a651594
+ 006feca8 bytes a2681594
- 006fe8fc ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 006fecac ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006fe8fc bytes c82b00b0
+ 006fecac bytes c82b00d0
- 006fe900 ["COPY", "tmp:0:8", ["const:58:8"]]
- 006fe900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fecb0 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 006fecb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fecb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fecb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe900 bytes 08610191
+ 006fecb0 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12a1111cf89baa6d26c13c165378b56e"></a>

### [`006fe910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe910.md) → [`006fecc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fecc0.md) FUN_006fecc0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fecc4",
      "incomplete_value": false,
      "site": "006fecc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe914",
      "incomplete_value": false,
      "site": "006fe918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "006fecc8",
      "DATA",
      [
        "storage",
        "00c77058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fecc8",
      "DATA",
      [
        "storage",
        "00c78028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe910.md#insn-006fe910) · [`006fe914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe910.md#insn-006fe914)
- 新版 [`006fecc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fecc0.md#insn-006fecc0) · [`006fecc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fecc0.md#insn-006fecc4)

~~~diff
- 006fe910 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 006fecc0 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006fe910 bytes c82b00b0
+ 006fecc0 bytes c82b00d0
- 006fe914 ["COPY", "tmp:0:8", ["const:58:8"]]
- 006fe914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fecc4 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 006fecc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fecc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fecc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe914 bytes 08610191
+ 006fecc4 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45a9cbeb228f710184379856ac91bd14"></a>

### [`006fe928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe928.md) → [`006fecd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fecd8.md) FUN_006fecd8

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
      "site": "006fecf4",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe944",
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
      "006fecf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006fecf4",
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

- 旧版 [`006fe944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe928.md#insn-006fe944) · [`006fe950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe928.md#insn-006fe950)
- 新版 [`006fecf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fecd8.md#insn-006fecf4) · [`006fed00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fecd8.md#insn-006fed00)

~~~diff
- 006fe944 ["INT_ADD", "register:40f0:8", ["const:6fe944:8", "const:4:8"]]
- 006fe944 ["CALL", null, ["ram:47ad34:8"]]
+ 006fecf4 ["INT_ADD", "register:40f0:8", ["const:6fecf4:8", "const:4:8"]]
+ 006fecf4 ["CALL", null, ["ram:47b054:8"]]
- 006fe944 bytes fcf0f597
+ 006fecf4 bytes d8f0f597
- 006fe950 ["INT_ADD", "register:40f0:8", ["const:6fe950:8", "const:4:8"]]
- 006fe950 ["CALL", null, ["callee:0047d134:8"]]
+ 006fed00 ["INT_ADD", "register:40f0:8", ["const:6fed00:8", "const:4:8"]]
+ 006fed00 ["CALL", null, ["callee:0047d134:8"]]
- 006fe950 bytes 31f9f597
+ 006fed00 bytes 0df9f597
~~~


<a id="compare-7411d56ee66be4825b1bd251395fbe62"></a>

### [`006fe994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe994.md) → [`006fed44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fed44.md) FUN_006fed44

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
      "definition_site": "006fed64",
      "incomplete_value": false,
      "site": "006fed68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe9b4",
      "incomplete_value": false,
      "site": "006fe9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "006fed68",
      "DATA",
      [
        "storage",
        "00c770e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fed68",
      "DATA",
      [
        "storage",
        "00c780b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe994.md#insn-006fe9a8) · [`006fe9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe994.md#insn-006fe9b0) · [`006fe9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe994.md#insn-006fe9b4)
- 新版 [`006fed58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fed44.md#insn-006fed58) · [`006fed60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fed44.md#insn-006fed60) · [`006fed64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fed44.md#insn-006fed64)

~~~diff
- 006fe9a8 ["INT_ADD", "register:40f0:8", ["const:6fe9a8:8", "const:4:8"]]
- 006fe9a8 ["CALL", null, ["callee:00c58f30:8"]]
+ 006fed58 ["INT_ADD", "register:40f0:8", ["const:6fed58:8", "const:4:8"]]
+ 006fed58 ["CALL", null, ["callee:00c58f30:8"]]
- 006fe9a8 bytes 6e651594
+ 006fed58 bytes 76681594
- 006fe9b0 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 006fed60 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006fe9b0 bytes c82b00b0
+ 006fed60 bytes c82b00d0
- 006fe9b4 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 006fe9b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe9b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe9b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fed64 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 006fed64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fed64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fed64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe9b4 bytes 08a10391
+ 006fed64 bytes 08e10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b587261983f5bb07d3651b1502222934"></a>

### [`006fe9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe9ec.md) → [`006fed9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fed9c.md) FUN_006fed9c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0052e060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.21% / 新版 92.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fee3c",
      "incomplete_value": true,
      "site": "006fee54",
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
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:fb7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fea8c",
      "incomplete_value": true,
      "site": "006feaa4",
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
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:ee0:8"
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
      "definition_site": "006feea4",
      "incomplete_value": true,
      "site": "006feea4",
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
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:d15:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006feaf4",
      "incomplete_value": true,
      "site": "006feaf4",
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
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:c37:8"
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
      "definition_site": "006feea8",
      "incomplete_value": true,
      "site": "006feea8",
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
      "definition_site": "006feaf8",
      "incomplete_value": true,
      "site": "006feaf8",
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
      "006fedd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006fedf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006fee3c",
      "READ",
      [
        "storage",
        "002b0ee0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006fedd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006fedf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006fee3c",
      "READ",
      [
        "storage",
        "002b0fb7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fea28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe9ec.md#insn-006fea28) · [`006fea44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe9ec.md#insn-006fea44) · [`006fea7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe9ec.md#insn-006fea7c)
- 新版 [`006fedd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fed9c.md#insn-006fedd8) · [`006fedf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fed9c.md#insn-006fedf4) · [`006fee2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fed9c.md#insn-006fee2c)

~~~diff
- 006fea28 ["INT_ADD", "register:40f0:8", ["const:6fea28:8", "const:4:8"]]
- 006fea28 ["CALL", null, ["ram:47ad34:8"]]
+ 006fedd8 ["INT_ADD", "register:40f0:8", ["const:6fedd8:8", "const:4:8"]]
+ 006fedd8 ["CALL", null, ["ram:47b054:8"]]
- 006fea28 bytes c3f0f597
+ 006fedd8 bytes 9ff0f597
- 006fea44 ["INT_ADD", "register:40f0:8", ["const:6fea44:8", "const:4:8"]]
- 006fea44 ["CALL", null, ["ram:47ad34:8"]]
+ 006fedf4 ["INT_ADD", "register:40f0:8", ["const:6fedf4:8", "const:4:8"]]
+ 006fedf4 ["CALL", null, ["ram:47b054:8"]]
- 006fea44 bytes bcf0f597
+ 006fedf4 bytes 98f0f597
- 006fea7c ["INT_ADD", "register:40f0:8", ["const:6fea7c:8", "const:4:8"]]
- 006fea7c ["CALL", null, ["callee:008524fc:8"]]
+ 006fee2c ["INT_ADD", "register:40f0:8", ["const:6fee2c:8", "const:4:8"]]
+ 006fee2c ["CALL", null, ["callee:008524fc:8"]]
- 006fea7c bytes b54a0594
+ 006fee2c bytes b44d0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3368dd14d170742334c91f3b5f6d8a61"></a>

### [`006fed64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fed64.md) → [`006ff114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff114.md) FUN_006ff114

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
      "definition_site": "006ff138",
      "incomplete_value": false,
      "site": "006ff138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fed88",
      "incomplete_value": false,
      "site": "006fed88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "006ff138",
      "DATA",
      [
        "storage",
        "00c77158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff138",
      "DATA",
      [
        "storage",
        "00c78128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fed78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fed64.md#insn-006fed78) · [`006fed80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fed64.md#insn-006fed80) · [`006fed84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fed64.md#insn-006fed84)
- 新版 [`006ff128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff114.md#insn-006ff128) · [`006ff130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff114.md#insn-006ff130) · [`006ff134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff114.md#insn-006ff134)

~~~diff
- 006fed78 ["INT_ADD", "register:40f0:8", ["const:6fed78:8", "const:4:8"]]
- 006fed78 ["CALL", null, ["callee:00c58f30:8"]]
+ 006ff128 ["INT_ADD", "register:40f0:8", ["const:6ff128:8", "const:4:8"]]
+ 006ff128 ["CALL", null, ["callee:00c58f30:8"]]
- 006fed78 bytes 7a641594
+ 006ff128 bytes 82671594
- 006fed80 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 006ff130 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006fed80 bytes c82b00b0
+ 006ff130 bytes c82b00b0
- 006fed84 ["COPY", "tmp:0:8", ["const:158:8"]]
- 006fed84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fed84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fed84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff134 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 006ff134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fed84 bytes 08610591
+ 006ff134 bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff99bdb239b591fcf1c7cc42f3fe5901"></a>

### [`006fed98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fed98.md) → [`006ff148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff148.md) FUN_006ff148

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
      "definition_site": "006ff154",
      "incomplete_value": false,
      "site": "006ff154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006feda4",
      "incomplete_value": false,
      "site": "006feda4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "006ff154",
      "DATA",
      [
        "storage",
        "00c77158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff154",
      "DATA",
      [
        "storage",
        "00c78128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fed9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fed98.md#insn-006fed9c) · [`006feda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fed98.md#insn-006feda0)
- 新版 [`006ff14c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff148.md#insn-006ff14c) · [`006ff150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff148.md#insn-006ff150)

~~~diff
- 006fed9c ["COPY", "register:4048:8", ["const:c77000:8"]]
+ 006ff14c ["COPY", "register:4048:8", ["const:c78000:8"]]
- 006fed9c bytes c92b00b0
+ 006ff14c bytes c92b00b0
- 006feda0 ["COPY", "tmp:0:8", ["const:158:8"]]
- 006feda0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006feda0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006feda0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006ff150 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 006ff150 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006ff150 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006ff150 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006feda0 bytes 29610591
+ 006ff150 bytes 29a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e85c001fe3f532c7cd9f9138b374ad9"></a>

### [`006fedb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fedb4.md) → [`006ff164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff164.md) FUN_006ff164

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
      "site": "006ff180",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fedd0",
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
      "006ff180",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006ff180",
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

- 旧版 [`006fedd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fedb4.md#insn-006fedd0) · [`006feddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fedb4.md#insn-006feddc)
- 新版 [`006ff180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff164.md#insn-006ff180) · [`006ff18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff164.md#insn-006ff18c)

~~~diff
- 006fedd0 ["INT_ADD", "register:40f0:8", ["const:6fedd0:8", "const:4:8"]]
- 006fedd0 ["CALL", null, ["ram:47ad34:8"]]
+ 006ff180 ["INT_ADD", "register:40f0:8", ["const:6ff180:8", "const:4:8"]]
+ 006ff180 ["CALL", null, ["ram:47b054:8"]]
- 006fedd0 bytes d9eff597
+ 006ff180 bytes b5eff597
- 006feddc ["INT_ADD", "register:40f0:8", ["const:6feddc:8", "const:4:8"]]
- 006feddc ["CALL", null, ["callee:0047d134:8"]]
+ 006ff18c ["INT_ADD", "register:40f0:8", ["const:6ff18c:8", "const:4:8"]]
+ 006ff18c ["CALL", null, ["callee:0047d134:8"]]
- 006feddc bytes 0ef8f597
+ 006ff18c bytes eaf7f597
~~~


<a id="compare-7ec7a0ce244457e892b54133818d1f87"></a>

### [`006fee5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fee5c.md) → [`006ff20c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff20c.md) FUN_006ff20c

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
      "site": "006ff228",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fee78",
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
      "006ff228",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006ff228",
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

- 旧版 [`006fee78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fee5c.md#insn-006fee78) · [`006fee84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fee5c.md#insn-006fee84)
- 新版 [`006ff228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff20c.md#insn-006ff228) · [`006ff234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff20c.md#insn-006ff234)

~~~diff
- 006fee78 ["INT_ADD", "register:40f0:8", ["const:6fee78:8", "const:4:8"]]
- 006fee78 ["CALL", null, ["ram:47ad34:8"]]
+ 006ff228 ["INT_ADD", "register:40f0:8", ["const:6ff228:8", "const:4:8"]]
+ 006ff228 ["CALL", null, ["ram:47b054:8"]]
- 006fee78 bytes afeff597
+ 006ff228 bytes 8beff597
- 006fee84 ["INT_ADD", "register:40f0:8", ["const:6fee84:8", "const:4:8"]]
- 006fee84 ["CALL", null, ["callee:0047d134:8"]]
+ 006ff234 ["INT_ADD", "register:40f0:8", ["const:6ff234:8", "const:4:8"]]
+ 006ff234 ["CALL", null, ["callee:0047d134:8"]]
- 006fee84 bytes e4f7f597
+ 006ff234 bytes c0f7f597
~~~


<a id="compare-b13a01c7f5d86cf9dcc95660d4fdb7ea"></a>

### [`006feec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006feec8.md) → [`006ff278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff278.md) FUN_006ff278

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006ff28c",
      "incomplete_value": false,
      "site": "006ff290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006feedc",
      "incomplete_value": false,
      "site": "006feee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "006ff290",
      "DATA",
      [
        "storage",
        "00c77268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff290",
      "DATA",
      [
        "storage",
        "00c78238",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006feed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006feec8.md#insn-006feed4) · [`006feed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006feec8.md#insn-006feed8) · [`006feedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006feec8.md#insn-006feedc)
- 新版 [`006ff284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff278.md#insn-006ff284) · [`006ff288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff278.md#insn-006ff288) · [`006ff28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff278.md#insn-006ff28c)

~~~diff
- 006feed4 ["INT_ADD", "register:40f0:8", ["const:6feed4:8", "const:4:8"]]
- 006feed4 ["CALL", null, ["callee:00c58f30:8"]]
+ 006ff284 ["INT_ADD", "register:40f0:8", ["const:6ff284:8", "const:4:8"]]
+ 006ff284 ["CALL", null, ["callee:00c58f30:8"]]
- 006feed4 bytes 23641594
+ 006ff284 bytes 2b671594
- 006feed8 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 006ff288 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006feed8 bytes c82b00b0
+ 006ff288 bytes c82b00b0
- 006feedc ["COPY", "tmp:0:8", ["const:268:8"]]
- 006feedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006feedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006feedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff28c ["COPY", "tmp:0:8", ["const:238:8"]]
+ 006ff28c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff28c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff28c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006feedc bytes 08a10991
+ 006ff28c bytes 08e10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3d1693b109b48d7dab2592f4dbb4e7c"></a>

### [`006feff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006feff0.md) → [`006ff3a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff3a0.md) FUN_006ff3a0

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
      "definition_site": "006ff3c4",
      "incomplete_value": false,
      "site": "006ff3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff014",
      "incomplete_value": false,
      "site": "006ff014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
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
      "006ff3c4",
      "DATA",
      [
        "storage",
        "00c772e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff3c4",
      "DATA",
      [
        "storage",
        "00c782b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006feff0.md#insn-006ff004) · [`006ff00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006feff0.md#insn-006ff00c) · [`006ff010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006feff0.md#insn-006ff010)
- 新版 [`006ff3b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff3a0.md#insn-006ff3b4) · [`006ff3bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff3a0.md#insn-006ff3bc) · [`006ff3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff3a0.md#insn-006ff3c0)

~~~diff
- 006ff004 ["INT_ADD", "register:40f0:8", ["const:6ff004:8", "const:4:8"]]
- 006ff004 ["CALL", null, ["callee:00c58f30:8"]]
+ 006ff3b4 ["INT_ADD", "register:40f0:8", ["const:6ff3b4:8", "const:4:8"]]
+ 006ff3b4 ["CALL", null, ["callee:00c58f30:8"]]
- 006ff004 bytes d7631594
+ 006ff3b4 bytes df661594
- 006ff00c ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 006ff3bc ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006ff00c bytes c82b0090
+ 006ff3bc bytes c82b00b0
- 006ff010 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 006ff010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ff010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ff010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff3c0 ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 006ff3c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff3c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff3c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ff010 bytes 08a10b91
+ 006ff3c0 bytes 08e10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2bed174aedc9fd3cbc4d5cbfaeeb45c"></a>

### [`006ff040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff040.md) → [`006ff3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff3f0.md) FUN_006ff3f0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

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
      "site": "006ff420",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff070",
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
      "site": "006ff448",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff098",
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
      "006ff420",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006ff448",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006ff420",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006ff448",
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

- 旧版 [`006ff070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff040.md#insn-006ff070) · [`006ff098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff040.md#insn-006ff098) · [`006ff0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff040.md#insn-006ff0a4)
- 新版 [`006ff420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff3f0.md#insn-006ff420) · [`006ff448`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff3f0.md#insn-006ff448) · [`006ff454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff3f0.md#insn-006ff454)

~~~diff
- 006ff070 ["INT_ADD", "register:40f0:8", ["const:6ff070:8", "const:4:8"]]
- 006ff070 ["CALL", null, ["ram:47ad34:8"]]
+ 006ff420 ["INT_ADD", "register:40f0:8", ["const:6ff420:8", "const:4:8"]]
+ 006ff420 ["CALL", null, ["ram:47b054:8"]]
- 006ff070 bytes 31eff597
+ 006ff420 bytes 0deff597
- 006ff098 ["INT_ADD", "register:40f0:8", ["const:6ff098:8", "const:4:8"]]
- 006ff098 ["CALL", null, ["ram:47ad34:8"]]
+ 006ff448 ["INT_ADD", "register:40f0:8", ["const:6ff448:8", "const:4:8"]]
+ 006ff448 ["CALL", null, ["ram:47b054:8"]]
- 006ff098 bytes 27eff597
+ 006ff448 bytes 03eff597
- 006ff0a4 ["INT_ADD", "register:40f0:8", ["const:6ff0a4:8", "const:4:8"]]
- 006ff0a4 ["CALL", null, ["callee:0047d134:8"]]
+ 006ff454 ["INT_ADD", "register:40f0:8", ["const:6ff454:8", "const:4:8"]]
+ 006ff454 ["CALL", null, ["callee:0047d134:8"]]
- 006ff0a4 bytes 5cf7f597
+ 006ff454 bytes 38f7f597
~~~


<a id="compare-ae75ace0466e3c6af6e882cb48f84523"></a>

### [`006ff0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff0e4.md) → [`006ff494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff494.md) FUN_006ff494

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ff4a8",
      "incomplete_value": true,
      "site": "006ff4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff0f8",
      "incomplete_value": true,
      "site": "006ff0fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
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
      "006ff4ac",
      "DATA",
      [
        "storage",
        "00c77368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff4ac",
      "DATA",
      [
        "storage",
        "00c78338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff0e4.md#insn-006ff0f0) · [`006ff0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff0e4.md#insn-006ff0f4) · [`006ff0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff0e4.md#insn-006ff0f8)
- 新版 [`006ff4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff494.md#insn-006ff4a0) · [`006ff4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff494.md#insn-006ff4a4) · [`006ff4a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff494.md#insn-006ff4a8)

~~~diff
- 006ff0f0 ["INT_ADD", "register:40f0:8", ["const:6ff0f0:8", "const:4:8"]]
- 006ff0f0 ["CALL", null, ["callee:00c58f30:8"]]
+ 006ff4a0 ["INT_ADD", "register:40f0:8", ["const:6ff4a0:8", "const:4:8"]]
+ 006ff4a0 ["CALL", null, ["callee:00c58f30:8"]]
- 006ff0f0 bytes 9c631594
+ 006ff4a0 bytes a4661594
- 006ff0f4 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 006ff4a4 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006ff0f4 bytes c82b0090
+ 006ff4a4 bytes c82b00b0
- 006ff0f8 ["COPY", "tmp:0:8", ["const:368:8"]]
- 006ff0f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ff0f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ff0f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff4a8 ["COPY", "tmp:0:8", ["const:338:8"]]
+ 006ff4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ff0f8 bytes 08a10d91
+ 006ff4a8 bytes 08e10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc9bbc7a69a6cb7f146ace554474ce36"></a>

### [`006ff204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff204.md) → [`006ff5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff5b4.md) FUN_006ff5b4

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
      "definition_site": "006ff5d8",
      "incomplete_value": false,
      "site": "006ff5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff228",
      "incomplete_value": false,
      "site": "006ff228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
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
      "006ff5d8",
      "DATA",
      [
        "storage",
        "00c773e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff5d8",
      "DATA",
      [
        "storage",
        "00c783b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff204.md#insn-006ff218) · [`006ff220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff204.md#insn-006ff220) · [`006ff224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff204.md#insn-006ff224)
- 新版 [`006ff5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff5b4.md#insn-006ff5c8) · [`006ff5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff5b4.md#insn-006ff5d0) · [`006ff5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff5b4.md#insn-006ff5d4)

~~~diff
- 006ff218 ["INT_ADD", "register:40f0:8", ["const:6ff218:8", "const:4:8"]]
- 006ff218 ["CALL", null, ["callee:00c58f30:8"]]
+ 006ff5c8 ["INT_ADD", "register:40f0:8", ["const:6ff5c8:8", "const:4:8"]]
+ 006ff5c8 ["CALL", null, ["callee:00c58f30:8"]]
- 006ff218 bytes 52631594
+ 006ff5c8 bytes 5a661594
- 006ff220 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 006ff5d0 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006ff220 bytes c82b0090
+ 006ff5d0 bytes c82b00b0
- 006ff224 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 006ff224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ff224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ff224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff5d4 ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 006ff5d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff5d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff5d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ff224 bytes 08a10f91
+ 006ff5d4 bytes 08e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3cf5481f245999d46817b63acb0ef8c"></a>

### [`006ff320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff320.md) → [`006ff6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff6d0.md) FUN_006ff6d0

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
      "definition_site": "006ff6f4",
      "incomplete_value": false,
      "site": "006ff6f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff344",
      "incomplete_value": false,
      "site": "006ff344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:468:8"
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
      "006ff6f4",
      "DATA",
      [
        "storage",
        "00c77468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff6f4",
      "DATA",
      [
        "storage",
        "00c78438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff320.md#insn-006ff334) · [`006ff33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff320.md#insn-006ff33c) · [`006ff340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff320.md#insn-006ff340)
- 新版 [`006ff6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff6d0.md#insn-006ff6e4) · [`006ff6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff6d0.md#insn-006ff6ec) · [`006ff6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff6d0.md#insn-006ff6f0)

~~~diff
- 006ff334 ["INT_ADD", "register:40f0:8", ["const:6ff334:8", "const:4:8"]]
- 006ff334 ["CALL", null, ["callee:00c58f30:8"]]
+ 006ff6e4 ["INT_ADD", "register:40f0:8", ["const:6ff6e4:8", "const:4:8"]]
+ 006ff6e4 ["CALL", null, ["callee:00c58f30:8"]]
- 006ff334 bytes 0b631594
+ 006ff6e4 bytes 13661594
- 006ff33c ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 006ff6ec ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006ff33c bytes c82b0090
+ 006ff6ec bytes c82b00b0
- 006ff340 ["COPY", "tmp:0:8", ["const:468:8"]]
- 006ff340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ff340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ff340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff6f0 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 006ff6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ff340 bytes 08a11191
+ 006ff6f0 bytes 08e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dc77e31911bce699f9a8c14a509b9f0"></a>

### [`006ff370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff370.md) → [`006ff720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff720.md) FUN_006ff720

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0047ce68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce68.md) [`006b247c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b247c.md) [`006b2488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2488.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0047d188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d188.md) [`006b282c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b282c.md) [`006b2838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b2838.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.28% / 新版 97.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006ff8b0",
      "incomplete_value": false,
      "site": "006ff8b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff500",
      "incomplete_value": false,
      "site": "006ff508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff764",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff3b4",
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
      "site": "006ff89c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff4ec",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ff764",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006ff89c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006ff8b8",
      "DATA",
      [
        "storage",
        "00c774d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff764",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006ff89c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006ff8b8",
      "DATA",
      [
        "storage",
        "00c784a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff370.md#insn-006ff3b4) · [`006ff4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff370.md#insn-006ff4ec) · [`006ff3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff370.md#insn-006ff3b0)
- 新版 [`006ff764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff720.md#insn-006ff764) · [`006ff89c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff720.md#insn-006ff89c) · [`006ff760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff720.md#insn-006ff760)

~~~diff
- 006ff3b4 ["INT_ADD", "register:40f0:8", ["const:6ff3b4:8", "const:4:8"]]
- 006ff3b4 ["CALL", null, ["ram:47ad34:8"]]
+ 006ff764 ["INT_ADD", "register:40f0:8", ["const:6ff764:8", "const:4:8"]]
+ 006ff764 ["CALL", null, ["ram:47b054:8"]]
- 006ff3b4 bytes 60eef597
+ 006ff764 bytes 3ceef597
- 006ff4ec ["INT_ADD", "register:40f0:8", ["const:6ff4ec:8", "const:4:8"]]
- 006ff4ec ["CALL", null, ["ram:47ad34:8"]]
+ 006ff89c ["INT_ADD", "register:40f0:8", ["const:6ff89c:8", "const:4:8"]]
+ 006ff89c ["CALL", null, ["ram:47b054:8"]]
- 006ff4ec bytes 12eef597
+ 006ff89c bytes eeedf597
- 006ff3b0 ["INT_ADD", "register:40f0:8", ["const:6ff3b0:8", "const:4:8"]]
- 006ff3b0 ["CALL", null, ["callee:008ba17c:8"]]
+ 006ff760 ["INT_ADD", "register:40f0:8", ["const:6ff760:8", "const:4:8"]]
+ 006ff760 ["CALL", null, ["callee:008ba17c:8"]]
- 006ff3b0 bytes 88e70694
+ 006ff760 bytes 87ea0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35dbe46026be1a7cba8d34d7d4aebd45"></a>

### [`006ff65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff65c.md) → [`006ffa0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ffa0c.md) FUN_006ffa0c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006ffa20",
      "incomplete_value": false,
      "site": "006ffa24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff670",
      "incomplete_value": false,
      "site": "006ff674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "006ffa24",
      "DATA",
      [
        "storage",
        "00c774d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ffa24",
      "DATA",
      [
        "storage",
        "00c784a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff65c.md#insn-006ff668) · [`006ff66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff65c.md#insn-006ff66c) · [`006ff670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff65c.md#insn-006ff670)
- 新版 [`006ffa18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ffa0c.md#insn-006ffa18) · [`006ffa1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ffa0c.md#insn-006ffa1c) · [`006ffa20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ffa0c.md#insn-006ffa20)

~~~diff
- 006ff668 ["INT_ADD", "register:40f0:8", ["const:6ff668:8", "const:4:8"]]
- 006ff668 ["CALL", null, ["callee:00c58f30:8"]]
+ 006ffa18 ["INT_ADD", "register:40f0:8", ["const:6ffa18:8", "const:4:8"]]
+ 006ffa18 ["CALL", null, ["callee:00c58f30:8"]]
- 006ff668 bytes 3e621594
+ 006ffa18 bytes 46651594
- 006ff66c ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 006ffa1c ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006ff66c bytes c82b0090
+ 006ffa1c bytes c82b00b0
- 006ff670 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 006ff670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ff670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ff670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ffa20 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 006ffa20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ffa20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ffa20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ff670 bytes 08611391
+ 006ffa20 bytes 08a11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96f74636580e5b1fd4479e6550ae762d"></a>

### [`006ff680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff680.md) → [`006ffa30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ffa30.md) FUN_006ffa30

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006ffa34",
      "incomplete_value": false,
      "site": "006ffa38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff684",
      "incomplete_value": false,
      "site": "006ff688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "006ffa38",
      "DATA",
      [
        "storage",
        "00c774d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ffa38",
      "DATA",
      [
        "storage",
        "00c784a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff680.md#insn-006ff680) · [`006ff684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff680.md#insn-006ff684)
- 新版 [`006ffa30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ffa30.md#insn-006ffa30) · [`006ffa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ffa30.md#insn-006ffa34)

~~~diff
- 006ff680 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 006ffa30 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006ff680 bytes c82b0090
+ 006ffa30 bytes c82b00b0
- 006ff684 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 006ff684 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ff684 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ff684 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ffa34 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 006ffa34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ffa34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ffa34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ff684 bytes 08611391
+ 006ffa34 bytes 08a11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f41c9d049da388e176a803db28f7f53e"></a>

### [`006ff698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff698.md) → [`006ffa48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ffa48.md) FUN_006ffa48

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 26件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047cf48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cf48.md)
- 新版 呼出元 0件  · 呼出先 26件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00442e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442e98.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d268.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ffae0",
      "incomplete_value": true,
      "site": "006ffaf0",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:4da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff730",
      "incomplete_value": true,
      "site": "006ff740",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:40f:8"
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
      "definition_site": "006ffb68",
      "incomplete_value": true,
      "site": "006ffb7c",
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
                "const:18b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff7b8",
      "incomplete_value": true,
      "site": "006ff7cc",
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
                "const:bc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006ffb9c",
      "incomplete_value": false,
      "site": "006ffb9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff7ec",
      "incomplete_value": false,
      "site": "006ff7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ffa94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006ffae0",
      "READ",
      [
        "storage",
        "002a340f",
        null,
        "string"
      ]
    ],
    [
      "006ffb68",
      "READ",
      [
        "storage",
        "002b90bc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006ffa94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006ffae0",
      "READ",
      [
        "storage",
        "002a34da",
        null,
        "string"
      ]
    ],
    [
      "006ffb68",
      "READ",
      [
        "storage",
        "002b918b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff698.md#insn-006ff6e4) · [`006ffaf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff698.md#insn-006ffaf0) · [`006ff6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff698.md#insn-006ff6cc)
- 新版 [`006ffa94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ffa48.md#insn-006ffa94) · [`006ffea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ffa48.md#insn-006ffea0) · [`006ffa7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ffa48.md#insn-006ffa7c)

~~~diff
- 006ff6e4 ["INT_ADD", "register:40f0:8", ["const:6ff6e4:8", "const:4:8"]]
- 006ff6e4 ["CALL", null, ["ram:47ad34:8"]]
+ 006ffa94 ["INT_ADD", "register:40f0:8", ["const:6ffa94:8", "const:4:8"]]
+ 006ffa94 ["CALL", null, ["ram:47b054:8"]]
- 006ff6e4 bytes 94edf597
+ 006ffa94 bytes 70edf597
- 006ffaf0 ["INT_ADD", "register:40f0:8", ["const:6ffaf0:8", "const:4:8"]]
- 006ffaf0 ["CALL", null, ["callee:00c58f50:8"]]
+ 006ffea0 ["INT_ADD", "register:40f0:8", ["const:6ffea0:8", "const:4:8"]]
+ 006ffea0 ["CALL", null, ["callee:00c58f50:8"]]
- 006ffaf0 bytes 24611594
+ 006ffea0 bytes 2c641594
- 006ff6cc ["INT_ADD", "register:40f0:8", ["const:6ff6cc:8", "const:4:8"]]
- 006ff6cc ["CALL", null, ["callee:0059822c:8"]]
+ 006ffa7c ["INT_ADD", "register:40f0:8", ["const:6ffa7c:8", "const:4:8"]]
+ 006ffa7c ["CALL", null, ["callee:0059822c:8"]]
- 006ff6cc bytes 1062fa97
+ 006ffa7c bytes ec61fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee20d89182b034cdffdaad2f503d36a2"></a>

### [`006ffe54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ffe54.md) → [`00700204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700204.md) FUN_00700204

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00700218",
      "incomplete_value": false,
      "site": "0070021c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ffe68",
      "incomplete_value": false,
      "site": "006ffe6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "0070021c",
      "DATA",
      [
        "storage",
        "00c77548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070021c",
      "DATA",
      [
        "storage",
        "00c78518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ffe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ffe54.md#insn-006ffe60) · [`006ffe64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ffe54.md#insn-006ffe64) · [`006ffe68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ffe54.md#insn-006ffe68)
- 新版 [`00700210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700204.md#insn-00700210) · [`00700214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700204.md#insn-00700214) · [`00700218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700204.md#insn-00700218)

~~~diff
- 006ffe60 ["INT_ADD", "register:40f0:8", ["const:6ffe60:8", "const:4:8"]]
- 006ffe60 ["CALL", null, ["callee:00c58f30:8"]]
+ 00700210 ["INT_ADD", "register:40f0:8", ["const:700210:8", "const:4:8"]]
+ 00700210 ["CALL", null, ["callee:00c58f30:8"]]
- 006ffe60 bytes 40601594
+ 00700210 bytes 48631594
- 006ffe64 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 00700214 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006ffe64 bytes c82b0090
+ 00700214 bytes c82b0090
- 006ffe68 ["COPY", "tmp:0:8", ["const:548:8"]]
- 006ffe68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ffe68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ffe68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00700218 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00700218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00700218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00700218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ffe68 bytes 08211591
+ 00700218 bytes 08611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-244239e1fb5f8b52aaaf36c2f2da2c25"></a>

### [`006ffe78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ffe78.md) → [`00700228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700228.md) FUN_00700228

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0070022c",
      "incomplete_value": false,
      "site": "00700230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ffe7c",
      "incomplete_value": false,
      "site": "006ffe80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "00700230",
      "DATA",
      [
        "storage",
        "00c77548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00700230",
      "DATA",
      [
        "storage",
        "00c78518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ffe78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ffe78.md#insn-006ffe78) · [`006ffe7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ffe78.md#insn-006ffe7c)
- 新版 [`00700228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700228.md#insn-00700228) · [`0070022c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700228.md#insn-0070022c)

~~~diff
- 006ffe78 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 00700228 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006ffe78 bytes c82b0090
+ 00700228 bytes c82b0090
- 006ffe7c ["COPY", "tmp:0:8", ["const:548:8"]]
- 006ffe7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ffe7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ffe7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070022c ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0070022c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070022c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070022c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ffe7c bytes 08211591
+ 0070022c bytes 08611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a8b4a41fccb813efbdaa6cfcde3d602"></a>

### [`006ffe90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ffe90.md) → [`00700240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700240.md) FUN_00700240

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "00700264",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ffeb4",
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
      "00700264",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00700264",
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

- 旧版 [`006ffeb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ffe90.md#insn-006ffeb4) · [`006ffec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ffe90.md#insn-006ffec0)
- 新版 [`00700264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700240.md#insn-00700264) · [`00700270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700240.md#insn-00700270)

~~~diff
- 006ffeb4 ["INT_ADD", "register:40f0:8", ["const:6ffeb4:8", "const:4:8"]]
- 006ffeb4 ["CALL", null, ["ram:47ad34:8"]]
+ 00700264 ["INT_ADD", "register:40f0:8", ["const:700264:8", "const:4:8"]]
+ 00700264 ["CALL", null, ["ram:47b054:8"]]
- 006ffeb4 bytes a0ebf597
+ 00700264 bytes 7cebf597
- 006ffec0 ["INT_ADD", "register:40f0:8", ["const:6ffec0:8", "const:4:8"]]
- 006ffec0 ["CALL", null, ["callee:0047d134:8"]]
+ 00700270 ["INT_ADD", "register:40f0:8", ["const:700270:8", "const:4:8"]]
+ 00700270 ["CALL", null, ["callee:0047d134:8"]]
- 006ffec0 bytes d5f3f597
+ 00700270 bytes b1f3f597
~~~


<a id="compare-641fc7cf83fb012aa89c9b636ed10ecb"></a>

### [`006fff04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fff04.md) → [`007002b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007002b4.md) FUN_007002b4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007002c8",
      "incomplete_value": false,
      "site": "007002cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fff18",
      "incomplete_value": false,
      "site": "006fff1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "007002cc",
      "DATA",
      [
        "storage",
        "00c775c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007002cc",
      "DATA",
      [
        "storage",
        "00c78598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fff10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fff04.md#insn-006fff10) · [`006fff14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fff04.md#insn-006fff14) · [`006fff18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fff04.md#insn-006fff18)
- 新版 [`007002c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007002b4.md#insn-007002c0) · [`007002c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007002b4.md#insn-007002c4) · [`007002c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007002b4.md#insn-007002c8)

~~~diff
- 006fff10 ["INT_ADD", "register:40f0:8", ["const:6fff10:8", "const:4:8"]]
- 006fff10 ["CALL", null, ["callee:00c58f30:8"]]
+ 007002c0 ["INT_ADD", "register:40f0:8", ["const:7002c0:8", "const:4:8"]]
+ 007002c0 ["CALL", null, ["callee:00c58f30:8"]]
- 006fff10 bytes 14601594
+ 007002c0 bytes 1c631594
- 006fff14 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 007002c4 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006fff14 bytes c82b0090
+ 007002c4 bytes c82b0090
- 006fff18 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 006fff18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fff18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fff18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007002c8 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 007002c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007002c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007002c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fff18 bytes 08211791
+ 007002c8 bytes 08611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dc986d6fdf4ac2e67031379b85209af"></a>

### [`006fff28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fff28.md) → [`007002d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007002d8.md) FUN_007002d8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007002dc",
      "incomplete_value": false,
      "site": "007002e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fff2c",
      "incomplete_value": false,
      "site": "006fff30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "007002e0",
      "DATA",
      [
        "storage",
        "00c775c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007002e0",
      "DATA",
      [
        "storage",
        "00c78598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fff28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fff28.md#insn-006fff28) · [`006fff2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fff28.md#insn-006fff2c)
- 新版 [`007002d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007002d8.md#insn-007002d8) · [`007002dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007002d8.md#insn-007002dc)

~~~diff
- 006fff28 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 007002d8 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 006fff28 bytes c82b0090
+ 007002d8 bytes c82b0090
- 006fff2c ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 006fff2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fff2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fff2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007002dc ["COPY", "tmp:0:8", ["const:598:8"]]
+ 007002dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007002dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007002dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fff2c bytes 08211791
+ 007002dc bytes 08611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cc14427b09bae9ec5fea053aa0a533c"></a>

### [`006fff40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fff40.md) → [`007002f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007002f0.md) FUN_007002f0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "00700314",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fff64",
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
      "00700314",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00700314",
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

- 旧版 [`006fff64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fff40.md#insn-006fff64) · [`006fff70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fff40.md#insn-006fff70)
- 新版 [`00700314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007002f0.md#insn-00700314) · [`00700320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007002f0.md#insn-00700320)

~~~diff
- 006fff64 ["INT_ADD", "register:40f0:8", ["const:6fff64:8", "const:4:8"]]
- 006fff64 ["CALL", null, ["ram:47ad34:8"]]
+ 00700314 ["INT_ADD", "register:40f0:8", ["const:700314:8", "const:4:8"]]
+ 00700314 ["CALL", null, ["ram:47b054:8"]]
- 006fff64 bytes 74ebf597
+ 00700314 bytes 50ebf597
- 006fff70 ["INT_ADD", "register:40f0:8", ["const:6fff70:8", "const:4:8"]]
- 006fff70 ["CALL", null, ["callee:0047d134:8"]]
+ 00700320 ["INT_ADD", "register:40f0:8", ["const:700320:8", "const:4:8"]]
+ 00700320 ["CALL", null, ["callee:0047d134:8"]]
- 006fff70 bytes a9f3f597
+ 00700320 bytes 85f3f597
~~~


<a id="compare-11c7fca22ba924c86e089471b1064c92"></a>

### [`006fffb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fffb0.md) → [`00700360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700360.md) FUN_00700360

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
      "definition_site": "0070036c",
      "incomplete_value": false,
      "site": "00700370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fffbc",
      "incomplete_value": false,
      "site": "006fffc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "00700370",
      "DATA",
      [
        "storage",
        "00c77668",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00700370",
      "DATA",
      [
        "storage",
        "00c78638",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fffb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fffb0.md#insn-006fffb8) · [`006fffbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fffb0.md#insn-006fffbc)
- 新版 [`00700368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700360.md#insn-00700368) · [`0070036c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700360.md#insn-0070036c)

~~~diff
- 006fffb8 ["COPY", "register:4048:8", ["const:c77000:8"]]
+ 00700368 ["COPY", "register:4048:8", ["const:c78000:8"]]
- 006fffb8 bytes c92b0090
+ 00700368 bytes c92b0090
- 006fffbc ["COPY", "tmp:0:8", ["const:668:8"]]
- 006fffbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fffbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fffbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0070036c ["COPY", "tmp:0:8", ["const:638:8"]]
+ 0070036c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0070036c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0070036c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fffbc bytes 29a11991
+ 0070036c bytes 29e11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d06172cc9700328cce2da769952e33f0"></a>

### [`006fffd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fffd4.md) → [`00700384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700384.md) FUN_00700384

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
      "definition_site": "0070038c",
      "incomplete_value": false,
      "site": "00700390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fffdc",
      "incomplete_value": false,
      "site": "006fffe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "00700390",
      "DATA",
      [
        "storage",
        "00c77668",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00700390",
      "DATA",
      [
        "storage",
        "00c78638",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fffd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fffd4.md#insn-006fffd8) · [`006fffdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fffd4.md#insn-006fffdc) · [`00700000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006fffd4.md#insn-00700000)
- 新版 [`00700388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700384.md#insn-00700388) · [`0070038c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700384.md#insn-0070038c) · [`007003b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700384.md#insn-007003b0)

~~~diff
- 006fffd8 ["COPY", "register:4048:8", ["const:c77000:8"]]
+ 00700388 ["COPY", "register:4048:8", ["const:c78000:8"]]
- 006fffd8 bytes c92b0090
+ 00700388 bytes c92b0090
- 006fffdc ["COPY", "tmp:0:8", ["const:668:8"]]
- 006fffdc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fffdc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fffdc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0070038c ["COPY", "tmp:0:8", ["const:638:8"]]
+ 0070038c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0070038c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0070038c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fffdc bytes 29a11991
+ 0070038c bytes 29e11891
- 00700000 ["INT_ADD", "register:40f0:8", ["const:700000:8", "const:4:8"]]
- 00700000 ["CALL", null, ["callee:00c58f50:8"]]
+ 007003b0 ["INT_ADD", "register:40f0:8", ["const:7003b0:8", "const:4:8"]]
+ 007003b0 ["CALL", null, ["callee:00c58f50:8"]]
- 00700000 bytes e05f1594
+ 007003b0 bytes e8621594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c8d8b57f075ddb63f35c6437116b9bd"></a>

### [`00700014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700014.md) → [`007003c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007003c4.md) FUN_007003c4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007003f4",
      "incomplete_value": false,
      "site": "007003f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00700044",
      "incomplete_value": false,
      "site": "00700044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007003f4",
      "DATA",
      [
        "storage",
        "00c77668",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007003f4",
      "DATA",
      [
        "storage",
        "00c78638",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070002c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700014.md#insn-0070002c) · [`00700034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700014.md#insn-00700034) · [`00700038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700014.md#insn-00700038)
- 新版 [`007003dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007003c4.md#insn-007003dc) · [`007003e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007003c4.md#insn-007003e4) · [`007003e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007003c4.md#insn-007003e8)

~~~diff
- 0070002c ["INT_ADD", "register:40f0:8", ["const:70002c:8", "const:4:8"]]
- 0070002c ["CALL", null, ["callee:00c58f30:8"]]
+ 007003dc ["INT_ADD", "register:40f0:8", ["const:7003dc:8", "const:4:8"]]
+ 007003dc ["CALL", null, ["callee:00c58f30:8"]]
- 0070002c bytes cd5f1594
+ 007003dc bytes d5621594
- 00700034 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 007003e4 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 00700034 bytes a82b00f0
+ 007003e4 bytes c82b0090
- 00700038 ["COPY", "tmp:0:8", ["const:668:8"]]
- 00700038 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00700038 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00700038 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007003e8 ["COPY", "tmp:0:8", ["const:638:8"]]
+ 007003e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007003e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007003e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00700038 bytes 08a11991
+ 007003e8 bytes 08e11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-085f82e2ec0d690c6c4dffa1d77c5934"></a>

### [`007000c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007000c8.md) → [`00700478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700478.md) FUN_00700478

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007004a4",
      "incomplete_value": false,
      "site": "007004a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007000f4",
      "incomplete_value": false,
      "site": "007000f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "007004a4",
      "DATA",
      [
        "storage",
        "00c77668",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007004a4",
      "DATA",
      [
        "storage",
        "00c78638",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007000e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007000c8.md#insn-007000e8) · [`007000ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007000c8.md#insn-007000ec) · [`0070010c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007000c8.md#insn-0070010c)
- 新版 [`00700498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700478.md#insn-00700498) · [`0070049c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700478.md#insn-0070049c) · [`007004bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700478.md#insn-007004bc)

~~~diff
- 007000e8 ["COPY", "register:4050:8", ["const:c77000:8"]]
+ 00700498 ["COPY", "register:4050:8", ["const:c78000:8"]]
- 007000e8 bytes aa2b00f0
+ 00700498 bytes ca2b0090
- 007000ec ["COPY", "tmp:0:8", ["const:668:8"]]
- 007000ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007000ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007000ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0070049c ["COPY", "tmp:0:8", ["const:638:8"]]
+ 0070049c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0070049c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0070049c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007000ec bytes 4aa11991
+ 0070049c bytes 4ae11891
- 0070010c ["INT_ADD", "register:40f0:8", ["const:70010c:8", "const:4:8"]]
- 0070010c ["CALL", null, ["callee:00c58f30:8"]]
+ 007004bc ["INT_ADD", "register:40f0:8", ["const:7004bc:8", "const:4:8"]]
+ 007004bc ["CALL", null, ["callee:00c58f30:8"]]
- 0070010c bytes 955f1594
+ 007004bc bytes 9d621594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f9f1e224e97468f8c2944eb1a788723"></a>

### [`0070039c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/0070039c.md) → [`0070074c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/0070074c.md) FUN_0070074c

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
      "definition_site": "00700758",
      "incomplete_value": false,
      "site": "0070075c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007003a8",
      "incomplete_value": false,
      "site": "007003ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
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
      "0070075c",
      "DATA",
      [
        "storage",
        "00c776e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070075c",
      "DATA",
      [
        "storage",
        "00c786b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007003a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/0070039c.md#insn-007003a4) · [`007003a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/0070039c.md#insn-007003a8)
- 新版 [`00700754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/0070074c.md#insn-00700754) · [`00700758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/0070074c.md#insn-00700758)

~~~diff
- 007003a4 ["COPY", "register:4048:8", ["const:c77000:8"]]
+ 00700754 ["COPY", "register:4048:8", ["const:c78000:8"]]
- 007003a4 bytes a92b00f0
+ 00700754 bytes c92b0090
- 007003a8 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 007003a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007003a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007003a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00700758 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00700758 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00700758 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00700758 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007003a8 bytes 29a11b91
+ 00700758 bytes 29e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-660f6b758d93753ac3951da4147e6e89"></a>

### [`007003c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007003c0.md) → [`00700770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700770.md) FUN_00700770

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
      "definition_site": "00700778",
      "incomplete_value": false,
      "site": "0070077c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007003c8",
      "incomplete_value": false,
      "site": "007003cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
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
      "0070077c",
      "DATA",
      [
        "storage",
        "00c776e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070077c",
      "DATA",
      [
        "storage",
        "00c786b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007003c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007003c0.md#insn-007003c4) · [`007003c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007003c0.md#insn-007003c8) · [`007003ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007003c0.md#insn-007003ec)
- 新版 [`00700774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700770.md#insn-00700774) · [`00700778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700770.md#insn-00700778) · [`0070079c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700770.md#insn-0070079c)

~~~diff
- 007003c4 ["COPY", "register:4048:8", ["const:c77000:8"]]
+ 00700774 ["COPY", "register:4048:8", ["const:c78000:8"]]
- 007003c4 bytes a92b00f0
+ 00700774 bytes c92b0090
- 007003c8 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 007003c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007003c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007003c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00700778 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00700778 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00700778 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00700778 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007003c8 bytes 29a11b91
+ 00700778 bytes 29e11a91
- 007003ec ["INT_ADD", "register:40f0:8", ["const:7003ec:8", "const:4:8"]]
- 007003ec ["CALL", null, ["callee:00c58f50:8"]]
+ 0070079c ["INT_ADD", "register:40f0:8", ["const:70079c:8", "const:4:8"]]
+ 0070079c ["CALL", null, ["callee:00c58f50:8"]]
- 007003ec bytes e55e1594
+ 0070079c bytes ed611594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72f3969b60a006d6e06674bcb0689a92"></a>

### [`00700400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700400.md) → [`007007b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007007b0.md) FUN_007007b0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007007e0",
      "incomplete_value": false,
      "site": "007007e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00700430",
      "incomplete_value": false,
      "site": "00700430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007007e0",
      "DATA",
      [
        "storage",
        "00c776e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007007e0",
      "DATA",
      [
        "storage",
        "00c786b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00700418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700400.md#insn-00700418) · [`00700420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700400.md#insn-00700420) · [`00700424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700400.md#insn-00700424)
- 新版 [`007007c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007007b0.md#insn-007007c8) · [`007007d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007007b0.md#insn-007007d0) · [`007007d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/007007b0.md#insn-007007d4)

~~~diff
- 00700418 ["INT_ADD", "register:40f0:8", ["const:700418:8", "const:4:8"]]
- 00700418 ["CALL", null, ["callee:00c58f30:8"]]
+ 007007c8 ["INT_ADD", "register:40f0:8", ["const:7007c8:8", "const:4:8"]]
+ 007007c8 ["CALL", null, ["callee:00c58f30:8"]]
- 00700418 bytes d25e1594
+ 007007c8 bytes da611594
- 00700420 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 007007d0 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 00700420 bytes a82b00f0
+ 007007d0 bytes c82b0090
- 00700424 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 00700424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00700424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00700424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007007d4 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 007007d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007007d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007007d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00700424 bytes 08a11b91
+ 007007d4 bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c87231446100ccca09a75f381b15bbc"></a>

### [`007004b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007004b4.md) → [`00700864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700864.md) FUN_00700864

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00700890",
      "incomplete_value": false,
      "site": "00700890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007004e0",
      "incomplete_value": false,
      "site": "007004e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
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
      "00700890",
      "DATA",
      [
        "storage",
        "00c776e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00700890",
      "DATA",
      [
        "storage",
        "00c786b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007004d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007004b4.md#insn-007004d4) · [`007004d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007004b4.md#insn-007004d8) · [`007004f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007004b4.md#insn-007004f8)
- 新版 [`00700884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700864.md#insn-00700884) · [`00700888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700864.md#insn-00700888) · [`007008a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700864.md#insn-007008a8)

~~~diff
- 007004d4 ["COPY", "register:4050:8", ["const:c77000:8"]]
+ 00700884 ["COPY", "register:4050:8", ["const:c78000:8"]]
- 007004d4 bytes aa2b00f0
+ 00700884 bytes ca2b0090
- 007004d8 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 007004d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007004d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007004d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00700888 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00700888 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00700888 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00700888 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007004d8 bytes 4aa11b91
+ 00700888 bytes 4ae11a91
- 007004f8 ["INT_ADD", "register:40f0:8", ["const:7004f8:8", "const:4:8"]]
- 007004f8 ["CALL", null, ["callee:00c58f30:8"]]
+ 007008a8 ["INT_ADD", "register:40f0:8", ["const:7008a8:8", "const:4:8"]]
+ 007008a8 ["CALL", null, ["callee:00c58f30:8"]]
- 007004f8 bytes 9a5e1594
+ 007008a8 bytes a2611594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c6ac7b4053737dd1197d06241c96543"></a>

### [`0070059c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/0070059c.md) → [`0070094c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/0070094c.md) FUN_0070094c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 11件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467df4.md) [`0046a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a290.md) [`0055a624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a624.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00468114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468114.md) [`0046a5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046a/0046a5b0.md) [`0055a944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055a/0055a944.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00700a88",
      "incomplete_value": true,
      "site": "00700a90",
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
      "definition_site": "007006d8",
      "incomplete_value": true,
      "site": "007006e0",
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
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007009dc",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007009e0",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007009e8",
      "PARAM",
      [
        "storage",
        "00c738e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007009dc",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007009e0",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "007009e8",
      "PARAM",
      [
        "storage",
        "00c748b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007006e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/0070059c.md#insn-007006e0) · [`007005d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/0070059c.md#insn-007005d0) · [`007005dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/0070059c.md#insn-007005dc)
- 新版 [`00700a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/0070094c.md#insn-00700a90) · [`00700980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/0070094c.md#insn-00700980) · [`0070098c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/0070094c.md#insn-0070098c)

~~~diff
- 007006e0 ["INT_ADD", "register:40f0:8", ["const:7006e0:8", "const:4:8"]]
- 007006e0 ["CALL", null, ["callee:00c596b0:8"]]
+ 00700a90 ["INT_ADD", "register:40f0:8", ["const:700a90:8", "const:4:8"]]
+ 00700a90 ["CALL", null, ["callee:00c596b0:8"]]
- 007006e0 bytes 00601594
+ 00700a90 bytes 08631594
- 007005d0 ["INT_ADD", "register:40f0:8", ["const:7005d0:8", "const:4:8"]]
- 007005d0 ["CALL", null, ["callee:008ba294:8"]]
+ 00700980 ["INT_ADD", "register:40f0:8", ["const:700980:8", "const:4:8"]]
+ 00700980 ["CALL", null, ["callee:008ba294:8"]]
- 007005d0 bytes 46e30694
+ 00700980 bytes 45e60694
- 007005dc ["INT_ADD", "register:40f0:8", ["const:7005dc:8", "const:4:8"]]
- 007005dc ["CALL", null, ["callee:008ba29c:8"]]
+ 0070098c ["INT_ADD", "register:40f0:8", ["const:70098c:8", "const:4:8"]]
+ 0070098c ["CALL", null, ["callee:008ba29c:8"]]
- 007005dc bytes 45e30694
+ 0070098c bytes 44e60694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a51c00bb7298dfad39c1961b0061e261"></a>

### [`007007c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007007c0.md) → [`00700b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700b70.md) _INIT_111

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.31% / 新版 85.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00700bac",
      "incomplete_value": true,
      "site": "00700bc8",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007007fc",
      "incomplete_value": true,
      "site": "00700818",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
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
      "definition_site": "00700bd0",
      "incomplete_value": true,
      "site": "00700bec",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00700820",
      "incomplete_value": true,
      "site": "0070083c",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f79:8"
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
      "definition_site": "00700bf0",
      "incomplete_value": true,
      "site": "00700c0c",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00700840",
      "incomplete_value": true,
      "site": "0070085c",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
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
      "00700bac",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00700bd0",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00700bf0",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00700bac",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00700bd0",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "00700bf0",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007009f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007007c0.md#insn-007009f4) · [`007007e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007007c0.md#insn-007007e8) · [`007007ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007007c0.md#insn-007007ec)
- 新版 [`00700da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700b70.md#insn-00700da4) · [`00700b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700b70.md#insn-00700b98) · [`00700b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700b70.md#insn-00700b9c)

~~~diff
- 007009f4 ["INT_ADD", "register:40f0:8", ["const:7009f4:8", "const:4:8"]]
- 007009f4 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00700da4 ["INT_ADD", "register:40f0:8", ["const:700da4:8", "const:4:8"]]
+ 00700da4 ["CALL", null, ["callee:00c58ed0:8"]]
- 007009f4 bytes 435d1594
+ 00700da4 bytes 4b601594
- 007007e8 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 00700b98 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 007007e8 bytes 332d00f0
+ 00700b98 bytes 532d0090
- 007007ec ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 007007ec ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007007ec ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007007ec ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00700b9c ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 00700b9c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00700b9c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00700b9c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007007ec bytes 73623391
+ 00700b9c bytes 73623291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef41847dbbbde438fc4dc4550e2066c8"></a>

### [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) → [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) FUN_00700f00

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 293件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440b40.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md)
- 新版 呼出元 1件 [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) · 呼出先 293件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00440e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440e60.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 98.32% / 新版 98.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `call_target` 48件, `store_destination` 1件, `store_value` 16件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00700f58",
      "incomplete_value": true,
      "site": "00700f58",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:354:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00700ba8",
      "incomplete_value": true,
      "site": "00700ba8",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:285:8"
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
      "definition_site": "00700f5c",
      "incomplete_value": true,
      "site": "00700f5c",
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
      "definition_site": "00700bac",
      "incomplete_value": true,
      "site": "00700bac",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0070104c",
      "incomplete_value": true,
      "site": "0070104c",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:540:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00700c9c",
      "incomplete_value": true,
      "site": "00700c9c",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00700f38",
      "READ",
      [
        "storage",
        "002b9285",
        null,
        "string"
      ]
    ],
    [
      "00700f50",
      "READ",
      [
        "storage",
        "002b928a",
        null,
        "string"
      ]
    ],
    [
      "00700f98",
      "READ",
      [
        "storage",
        "002b830c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00700f38",
      "READ",
      [
        "storage",
        "002b9354",
        null,
        "string"
      ]
    ],
    [
      "00700f50",
      "READ",
      [
        "storage",
        "002b9359",
        null,
        "string"
      ]
    ],
    [
      "00700f98",
      "READ",
      [
        "storage",
        "002b83db",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00700c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md#insn-00700c60) · [`00700c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md#insn-00700c88) · [`00700e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md#insn-00700e3c)
- 新版 [`00701010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md#insn-00701010) · [`00701038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md#insn-00701038) · [`007011ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md#insn-007011ec)

~~~diff
- 00700c60 ["INT_ADD", "register:40f0:8", ["const:700c60:8", "const:4:8"]]
- 00700c60 ["CALL", null, ["callee:00c596b0:8"]]
+ 00701010 ["INT_ADD", "register:40f0:8", ["const:701010:8", "const:4:8"]]
+ 00701010 ["CALL", null, ["callee:00c596b0:8"]]
- 00700c60 bytes a05e1594
+ 00701010 bytes a8611594
- 00700c88 ["INT_ADD", "register:40f0:8", ["const:700c88:8", "const:4:8"]]
- 00700c88 ["CALL", null, ["callee:0046cfd4:8"]]
+ 00701038 ["INT_ADD", "register:40f0:8", ["const:701038:8", "const:4:8"]]
+ 00701038 ["CALL", null, ["callee:0046cfd4:8"]]
- 00700c88 bytes 0bb0f597
+ 00701038 bytes e7aff597
- 00700e3c ["INT_ADD", "register:40f0:8", ["const:700e3c:8", "const:4:8"]]
- 00700e3c ["CALL", null, ["ram:47ad34:8"]]
+ 007011ec ["INT_ADD", "register:40f0:8", ["const:7011ec:8", "const:4:8"]]
+ 007011ec ["CALL", null, ["ram:47b054:8"]]
- 00700e3c bytes bee7f597
+ 007011ec bytes 9ae7f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5efb2a135bef71a64b8bed04c0a4e7e3"></a>

### [`007075c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/007075c0.md) → [`00707970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00707/00707970.md) FUN_00707970

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`00934924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00934/00934924.md) · 呼出先 14件 [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`005e1b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1b58.md) [`005e1b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1b70.md) [`006648e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/006648e0.md)
- 新版 呼出元 2件 [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) [`009358d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00935/009358d0.md) · 呼出先 14件 [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`005e1f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1f08.md) [`005e1f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1f20.md) [`00664c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664c90.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.93% / 新版 87.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `store_destination` 7件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00707bf4",
      "incomplete_value": false,
      "site": "00707bf4",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:fc0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00707844",
      "incomplete_value": false,
      "site": "00707844",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00707bf8",
      "incomplete_value": false,
      "site": "00707bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00707848",
      "incomplete_value": false,
      "site": "00707848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00707bf4",
      "incomplete_value": false,
      "site": "00707bf8",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:fc0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00707844",
      "incomplete_value": false,
      "site": "00707848",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007079a0",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007079ac",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007079b4",
      "PARAM",
      [
        "storage",
        "00c71a48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007079a0",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "007079ac",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007079b4",
      "PARAM",
      [
        "storage",
        "00c72a18",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00707610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/007075c0.md#insn-00707610) · [`00707658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/007075c0.md#insn-00707658) · [`0070781c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/007075c0.md#insn-0070781c)
- 新版 [`007079c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00707/00707970.md#insn-007079c0) · [`00707a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00707/00707970.md#insn-00707a08) · [`00707bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00707/00707970.md#insn-00707bcc)

~~~diff
- 00707610 ["INT_ADD", "register:40f0:8", ["const:707610:8", "const:4:8"]]
- 00707610 ["CALL", null, ["callee:00c596b0:8"]]
+ 007079c0 ["INT_ADD", "register:40f0:8", ["const:7079c0:8", "const:4:8"]]
+ 007079c0 ["CALL", null, ["callee:00c596b0:8"]]
- 00707610 bytes 34441594
+ 007079c0 bytes 3c471594
- 00707658 ["INT_ADD", "register:40f0:8", ["const:707658:8", "const:4:8"]]
- 00707658 ["CALL", null, ["ram:6648e0:8"]]
+ 00707a08 ["INT_ADD", "register:40f0:8", ["const:707a08:8", "const:4:8"]]
+ 00707a08 ["CALL", null, ["ram:664c90:8"]]
- 00707658 bytes a274fd97
+ 00707a08 bytes a274fd97
- 0070781c ["INT_ADD", "register:40f0:8", ["const:70781c:8", "const:4:8"]]
- 0070781c ["CALL", null, ["callee:00c58ef0:8"]]
+ 00707bcc ["INT_ADD", "register:40f0:8", ["const:707bcc:8", "const:4:8"]]
+ 00707bcc ["CALL", null, ["callee:00c58ef0:8"]]
- 0070781c bytes c1411594
+ 00707bcc bytes c9441594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6053c8ccb6a8dc804da5a3a218bc113"></a>

### [`007078a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/007078a4.md) → [`00707c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00707/00707c54.md) FUN_00707c54

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 3件 [`00936618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00936/00936618.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) · 呼出先 3件 [`009375c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00937/009375c4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00707c88",
      "incomplete_value": true,
      "site": "00707c9c",
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
                "const:385:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007078d8",
      "incomplete_value": true,
      "site": "007078ec",
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
                "const:2b6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00707ca0",
      "incomplete_value": true,
      "site": "00707ca0",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007078f0",
      "incomplete_value": true,
      "site": "007078f0",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00707c88",
      "READ",
      [
        "storage",
        "002b92b6",
        null,
        "string"
      ]
    ],
    [
      "00707c8c",
      "READ",
      [
        "storage",
        "002b92c3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00707c88",
      "READ",
      [
        "storage",
        "002b9385",
        null,
        "string"
      ]
    ],
    [
      "00707c8c",
      "READ",
      [
        "storage",
        "002b9392",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007078d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/007078a4.md#insn-007078d0) · [`00707904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/007078a4.md#insn-00707904) · [`00707924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/007078a4.md#insn-00707924)
- 新版 [`00707c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00707/00707c54.md#insn-00707c80) · [`00707cb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00707/00707c54.md#insn-00707cb4) · [`00707cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00707/00707c54.md#insn-00707cd4)

~~~diff
- 007078d0 ["COPY", "tmp:0:8", ["const:2b6:8"]]
- 007078d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007078d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007078d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00707c80 ["COPY", "tmp:0:8", ["const:385:8"]]
+ 00707c80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00707c80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00707c80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007078d0 bytes 29d90a91
+ 00707c80 bytes 29150e91
- 00707904 ["INT_ADD", "register:40f0:8", ["const:707904:8", "const:4:8"]]
- 00707904 ["CALL", null, ["callee:009375c4:8"]]
+ 00707cb4 ["INT_ADD", "register:40f0:8", ["const:707cb4:8", "const:4:8"]]
+ 00707cb4 ["CALL", null, ["callee:009375c4:8"]]
- 00707904 bytes 45bb0894
+ 00707cb4 bytes 44be0894
- 00707924 ["INT_ADD", "register:40f0:8", ["const:707924:8", "const:4:8"]]
- 00707924 ["CALL", null, ["callee:00c58f50:8"]]
+ 00707cd4 ["INT_ADD", "register:40f0:8", ["const:707cd4:8", "const:4:8"]]
+ 00707cd4 ["CALL", null, ["callee:00c58f50:8"]]
- 00707924 bytes 97411594
+ 00707cd4 bytes 9f441594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c788ffd51cedab1d1b5ea5425fcc8f53"></a>

### [`0070d410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070d/0070d410.md) → [`0070d7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070d/0070d7c0.md) FUN_0070d7c0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) · 呼出先 21件 [`005e4f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4f7c.md) [`00604e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00604/00604e94.md) [`00604fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00604/00604fe4.md) [`00689994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/00689994.md) [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md)
- 新版 呼出元 1件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) · 呼出先 21件 [`005e532c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e5/005e532c.md) [`00605244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00605/00605244.md) [`00605394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00605/00605394.md) [`00689d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00689/00689d44.md) [`0071c868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c868.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.66% / 新版 96.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0070d9ec",
      "incomplete_value": false,
      "site": "0070d9f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:b6f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070d63c",
      "incomplete_value": false,
      "site": "0070d644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0070da14",
      "incomplete_value": true,
      "site": "0070da20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:67d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070d664",
      "incomplete_value": true,
      "site": "0070d670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:5ae:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0070da4c",
      "incomplete_value": false,
      "site": "0070da50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:ec3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070d69c",
      "incomplete_value": false,
      "site": "0070d6a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:e79:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0070d924",
      "DATA",
      [
        "storage",
        "003965a4",
        null,
        "qword"
      ]
    ],
    [
      "0070d9f4",
      "DATA",
      [
        "storage",
        "002aea98",
        null,
        "string"
      ]
    ],
    [
      "0070da20",
      "DATA",
      [
        "storage",
        "002b75ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0070d924",
      "DATA",
      [
        "storage",
        "003965a4",
        "fde_003965a4",
        "dword"
      ]
    ],
    [
      "0070d9f4",
      "DATA",
      [
        "storage",
        "002aeb6f",
        null,
        "string"
      ]
    ],
    [
      "0070da20",
      "DATA",
      [
        "storage",
        "002b767d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070d4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070d/0070d410.md#insn-0070d4b0) · [`0070d50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070d/0070d410.md#insn-0070d50c) · [`0070d594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070d/0070d410.md#insn-0070d594)
- 新版 [`0070d860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070d/0070d7c0.md#insn-0070d860) · [`0070d8bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070d/0070d7c0.md#insn-0070d8bc) · [`0070d944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070d/0070d7c0.md#insn-0070d944)

~~~diff
- 0070d4b0 ["INT_ADD", "register:40f0:8", ["const:70d4b0:8", "const:4:8"]]
- 0070d4b0 ["CALL", null, ["callee:0071d43c:8"]]
+ 0070d860 ["INT_ADD", "register:40f0:8", ["const:70d860:8", "const:4:8"]]
+ 0070d860 ["CALL", null, ["callee:0071d43c:8"]]
- 0070d4b0 bytes f73e0094
+ 0070d860 bytes f73e0094
- 0070d50c ["INT_ADD", "register:40f0:8", ["const:70d50c:8", "const:4:8"]]
- 0070d50c ["CALL", null, ["callee:0071d43c:8"]]
+ 0070d8bc ["INT_ADD", "register:40f0:8", ["const:70d8bc:8", "const:4:8"]]
+ 0070d8bc ["CALL", null, ["callee:0071d43c:8"]]
- 0070d50c bytes e03e0094
+ 0070d8bc bytes e03e0094
- 0070d594 ["INT_ADD", "register:40f0:8", ["const:70d594:8", "const:4:8"]]
- 0070d594 ["CALL", null, ["callee:009e1fc0:8"]]
+ 0070d944 ["INT_ADD", "register:40f0:8", ["const:70d944:8", "const:4:8"]]
+ 0070d944 ["CALL", null, ["callee:009e1fc0:8"]]
- 0070d594 bytes a04e0b94
+ 0070d944 bytes 9f510b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d14f47c7f41eb1e8463e0afd85e993c5"></a>

### [`0070e1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e1e8.md) → [`0070e598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e598.md) FUN_0070e598

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
      "definition_site": "0070e5bc",
      "incomplete_value": false,
      "site": "0070e5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e20c",
      "incomplete_value": false,
      "site": "0070e20c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:768:8"
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
      "0070e5bc",
      "DATA",
      [
        "storage",
        "00c77768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070e5bc",
      "DATA",
      [
        "storage",
        "00c78738",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e1e8.md#insn-0070e1fc) · [`0070e204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e1e8.md#insn-0070e204) · [`0070e208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e1e8.md#insn-0070e208)
- 新版 [`0070e5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e598.md#insn-0070e5ac) · [`0070e5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e598.md#insn-0070e5b4) · [`0070e5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e598.md#insn-0070e5b8)

~~~diff
- 0070e1fc ["INT_ADD", "register:40f0:8", ["const:70e1fc:8", "const:4:8"]]
- 0070e1fc ["CALL", null, ["callee:00c58f30:8"]]
+ 0070e5ac ["INT_ADD", "register:40f0:8", ["const:70e5ac:8", "const:4:8"]]
+ 0070e5ac ["CALL", null, ["callee:00c58f30:8"]]
- 0070e1fc bytes 59271594
+ 0070e5ac bytes 612a1594
- 0070e204 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0070e5b4 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0070e204 bytes 482b00b0
+ 0070e5b4 bytes 482b00d0
- 0070e208 ["COPY", "tmp:0:8", ["const:768:8"]]
- 0070e208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070e208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070e208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070e5b8 ["COPY", "tmp:0:8", ["const:738:8"]]
+ 0070e5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070e208 bytes 08a11d91
+ 0070e5b8 bytes 08e11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a35823998471ea134e17ff65adeb3213"></a>

### [`0070e21c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e21c.md) → [`0070e5cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e5cc.md) FUN_0070e5cc

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
      "definition_site": "0070e5d8",
      "incomplete_value": false,
      "site": "0070e5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e228",
      "incomplete_value": false,
      "site": "0070e228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:768:8"
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
      "0070e5d8",
      "DATA",
      [
        "storage",
        "00c77768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070e5d8",
      "DATA",
      [
        "storage",
        "00c78738",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e21c.md#insn-0070e220) · [`0070e224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e21c.md#insn-0070e224)
- 新版 [`0070e5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e5cc.md#insn-0070e5d0) · [`0070e5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e5cc.md#insn-0070e5d4)

~~~diff
- 0070e220 ["COPY", "register:4048:8", ["const:c77000:8"]]
+ 0070e5d0 ["COPY", "register:4048:8", ["const:c78000:8"]]
- 0070e220 bytes 492b00b0
+ 0070e5d0 bytes 492b00d0
- 0070e224 ["COPY", "tmp:0:8", ["const:768:8"]]
- 0070e224 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0070e224 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0070e224 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0070e5d4 ["COPY", "tmp:0:8", ["const:738:8"]]
+ 0070e5d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0070e5d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0070e5d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0070e224 bytes 29a11d91
+ 0070e5d4 bytes 29e11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7eb7cf172a29b66e9ee4bf0fb9994cf"></a>

### [`0070e238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e238.md) → [`0070e5e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e5e8.md) FUN_0070e5e8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

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
      "site": "0070e610",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0070e260",
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
      "0070e610",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "0070e610",
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

- 旧版 [`0070e260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e238.md#insn-0070e260) · [`0070e26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e238.md#insn-0070e26c)
- 新版 [`0070e610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e5e8.md#insn-0070e610) · [`0070e61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e5e8.md#insn-0070e61c)

~~~diff
- 0070e260 ["INT_ADD", "register:40f0:8", ["const:70e260:8", "const:4:8"]]
- 0070e260 ["CALL", null, ["ram:47ad34:8"]]
+ 0070e610 ["INT_ADD", "register:40f0:8", ["const:70e610:8", "const:4:8"]]
+ 0070e610 ["CALL", null, ["ram:47b054:8"]]
- 0070e260 bytes b5b2f597
+ 0070e610 bytes 91b2f597
- 0070e26c ["INT_ADD", "register:40f0:8", ["const:70e26c:8", "const:4:8"]]
- 0070e26c ["CALL", null, ["callee:0047d134:8"]]
+ 0070e61c ["INT_ADD", "register:40f0:8", ["const:70e61c:8", "const:4:8"]]
+ 0070e61c ["CALL", null, ["callee:0047d134:8"]]
- 0070e26c bytes eabaf597
+ 0070e61c bytes c6baf597
~~~


<a id="compare-b2e536f94b87926c6722dbb42464d16b"></a>

### [`0070e2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e2c4.md) → [`0070e674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e674.md) FUN_0070e674

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
      "definition_site": "0070e698",
      "incomplete_value": false,
      "site": "0070e698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e2e8",
      "incomplete_value": false,
      "site": "0070e2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
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
      "0070e698",
      "DATA",
      [
        "storage",
        "00c777e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070e698",
      "DATA",
      [
        "storage",
        "00c787b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e2c4.md#insn-0070e2d8) · [`0070e2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e2c4.md#insn-0070e2e0) · [`0070e2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e2c4.md#insn-0070e2e4)
- 新版 [`0070e688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e674.md#insn-0070e688) · [`0070e690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e674.md#insn-0070e690) · [`0070e694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e674.md#insn-0070e694)

~~~diff
- 0070e2d8 ["INT_ADD", "register:40f0:8", ["const:70e2d8:8", "const:4:8"]]
- 0070e2d8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0070e688 ["INT_ADD", "register:40f0:8", ["const:70e688:8", "const:4:8"]]
+ 0070e688 ["CALL", null, ["callee:00c58f30:8"]]
- 0070e2d8 bytes 22271594
+ 0070e688 bytes 2a2a1594
- 0070e2e0 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0070e690 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0070e2e0 bytes 482b00b0
+ 0070e690 bytes 482b00d0
- 0070e2e4 ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 0070e2e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070e2e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070e2e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070e694 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 0070e694 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e694 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e694 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070e2e4 bytes 08a11f91
+ 0070e694 bytes 08e11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d1bc9e4c7f6c19c40c201a05036d5cc"></a>

### [`0070e2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e2f8.md) → [`0070e6a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e6a8.md) FUN_0070e6a8

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
      "definition_site": "0070e6b4",
      "incomplete_value": false,
      "site": "0070e6b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e304",
      "incomplete_value": false,
      "site": "0070e304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
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
      "0070e6b4",
      "DATA",
      [
        "storage",
        "00c777e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070e6b4",
      "DATA",
      [
        "storage",
        "00c787b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e2f8.md#insn-0070e2fc) · [`0070e300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e2f8.md#insn-0070e300)
- 新版 [`0070e6ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e6a8.md#insn-0070e6ac) · [`0070e6b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e6a8.md#insn-0070e6b0)

~~~diff
- 0070e2fc ["COPY", "register:4048:8", ["const:c77000:8"]]
+ 0070e6ac ["COPY", "register:4048:8", ["const:c78000:8"]]
- 0070e2fc bytes 492b00b0
+ 0070e6ac bytes 492b00d0
- 0070e300 ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 0070e300 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0070e300 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0070e300 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0070e6b0 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 0070e6b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0070e6b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0070e6b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0070e300 bytes 29a11f91
+ 0070e6b0 bytes 29e11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3cf48c701c79ba717a1691cb077f1c1"></a>

### [`0070e314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e314.md) → [`0070e6c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e6c4.md) FUN_0070e6c4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

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
      "site": "0070e6ec",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0070e33c",
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
      "0070e6ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "0070e6ec",
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

- 旧版 [`0070e33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e314.md#insn-0070e33c) · [`0070e348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e314.md#insn-0070e348)
- 新版 [`0070e6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e6c4.md#insn-0070e6ec) · [`0070e6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e6c4.md#insn-0070e6f8)

~~~diff
- 0070e33c ["INT_ADD", "register:40f0:8", ["const:70e33c:8", "const:4:8"]]
- 0070e33c ["CALL", null, ["ram:47ad34:8"]]
+ 0070e6ec ["INT_ADD", "register:40f0:8", ["const:70e6ec:8", "const:4:8"]]
+ 0070e6ec ["CALL", null, ["ram:47b054:8"]]
- 0070e33c bytes 7eb2f597
+ 0070e6ec bytes 5ab2f597
- 0070e348 ["INT_ADD", "register:40f0:8", ["const:70e348:8", "const:4:8"]]
- 0070e348 ["CALL", null, ["callee:0047d134:8"]]
+ 0070e6f8 ["INT_ADD", "register:40f0:8", ["const:70e6f8:8", "const:4:8"]]
+ 0070e6f8 ["CALL", null, ["callee:0047d134:8"]]
- 0070e348 bytes b3baf597
+ 0070e6f8 bytes 8fbaf597
~~~


<a id="compare-239723eb23c4b86f5e2589e06a0ca2d6"></a>

### [`0070e3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e3ac.md) → [`0070e75c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e75c.md) FUN_0070e75c

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
      "definition_site": "0070e77c",
      "incomplete_value": false,
      "site": "0070e780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e3cc",
      "incomplete_value": false,
      "site": "0070e3d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:868:8"
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
      "0070e780",
      "DATA",
      [
        "storage",
        "00c77868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070e780",
      "DATA",
      [
        "storage",
        "00c78838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e3ac.md#insn-0070e3c0) · [`0070e3c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e3ac.md#insn-0070e3c8) · [`0070e3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e3ac.md#insn-0070e3cc)
- 新版 [`0070e770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e75c.md#insn-0070e770) · [`0070e778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e75c.md#insn-0070e778) · [`0070e77c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e75c.md#insn-0070e77c)

~~~diff
- 0070e3c0 ["INT_ADD", "register:40f0:8", ["const:70e3c0:8", "const:4:8"]]
- 0070e3c0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0070e770 ["INT_ADD", "register:40f0:8", ["const:70e770:8", "const:4:8"]]
+ 0070e770 ["CALL", null, ["callee:00c58f30:8"]]
- 0070e3c0 bytes e8261594
+ 0070e770 bytes f0291594
- 0070e3c8 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0070e778 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0070e3c8 bytes 482b00b0
+ 0070e778 bytes 482b00d0
- 0070e3cc ["COPY", "tmp:0:8", ["const:868:8"]]
- 0070e3cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070e3cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070e3cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070e77c ["COPY", "tmp:0:8", ["const:838:8"]]
+ 0070e77c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e77c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e77c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070e3cc bytes 08a12191
+ 0070e77c bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b9c465c9066ab57945a876b72eba6d4"></a>

### [`0070e3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e3e4.md) → [`0070e794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e794.md) FUN_0070e794

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
      "definition_site": "0070e798",
      "incomplete_value": false,
      "site": "0070e79c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e3e8",
      "incomplete_value": false,
      "site": "0070e3ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:868:8"
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
      "0070e79c",
      "DATA",
      [
        "storage",
        "00c77868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070e79c",
      "DATA",
      [
        "storage",
        "00c78838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e3e4.md#insn-0070e3e4) · [`0070e3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e3e4.md#insn-0070e3e8)
- 新版 [`0070e794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e794.md#insn-0070e794) · [`0070e798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e794.md#insn-0070e798)

~~~diff
- 0070e3e4 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0070e794 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0070e3e4 bytes 482b00b0
+ 0070e794 bytes 482b00d0
- 0070e3e8 ["COPY", "tmp:0:8", ["const:868:8"]]
- 0070e3e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070e3e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070e3e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070e798 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 0070e798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070e3e8 bytes 08a12191
+ 0070e798 bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46933a4fb553294a3f3c2ae6b1eee278"></a>

### [`0070e43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e43c.md) → [`0070e7ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e7ec.md) FUN_0070e7ec

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
      "definition_site": "0070e810",
      "incomplete_value": false,
      "site": "0070e810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e460",
      "incomplete_value": false,
      "site": "0070e460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "0070e810",
      "DATA",
      [
        "storage",
        "00c778e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070e810",
      "DATA",
      [
        "storage",
        "00c788b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e43c.md#insn-0070e450) · [`0070e458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e43c.md#insn-0070e458) · [`0070e45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e43c.md#insn-0070e45c)
- 新版 [`0070e800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e7ec.md#insn-0070e800) · [`0070e808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e7ec.md#insn-0070e808) · [`0070e80c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e7ec.md#insn-0070e80c)

~~~diff
- 0070e450 ["INT_ADD", "register:40f0:8", ["const:70e450:8", "const:4:8"]]
- 0070e450 ["CALL", null, ["callee:00c58f30:8"]]
+ 0070e800 ["INT_ADD", "register:40f0:8", ["const:70e800:8", "const:4:8"]]
+ 0070e800 ["CALL", null, ["callee:00c58f30:8"]]
- 0070e450 bytes c4261594
+ 0070e800 bytes cc291594
- 0070e458 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0070e808 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0070e458 bytes 482b00b0
+ 0070e808 bytes 482b00d0
- 0070e45c ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0070e45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070e45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070e45c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070e80c ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 0070e80c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e80c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e80c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070e45c bytes 08a12391
+ 0070e80c bytes 08e12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea9b6050bc7f1c48c69726ea4ee4d04c"></a>

### [`0070e470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e470.md) → [`0070e820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e820.md) FUN_0070e820

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
      "definition_site": "0070e82c",
      "incomplete_value": false,
      "site": "0070e82c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e47c",
      "incomplete_value": false,
      "site": "0070e47c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
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
      "0070e82c",
      "DATA",
      [
        "storage",
        "00c778e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070e82c",
      "DATA",
      [
        "storage",
        "00c788b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e470.md#insn-0070e474) · [`0070e478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e470.md#insn-0070e478)
- 新版 [`0070e824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e820.md#insn-0070e824) · [`0070e828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e820.md#insn-0070e828)

~~~diff
- 0070e474 ["COPY", "register:4048:8", ["const:c77000:8"]]
+ 0070e824 ["COPY", "register:4048:8", ["const:c78000:8"]]
- 0070e474 bytes 492b00b0
+ 0070e824 bytes 492b00d0
- 0070e478 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0070e478 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0070e478 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0070e478 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0070e828 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 0070e828 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0070e828 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0070e828 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0070e478 bytes 29a12391
+ 0070e828 bytes 29e12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a26cf087cf18dcbd067cc609d775dcd2"></a>

### [`0070e48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e48c.md) → [`0070e83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e83c.md) FUN_0070e83c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

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
      "site": "0070e864",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0070e4b4",
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
      "0070e864",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "0070e864",
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

- 旧版 [`0070e4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e48c.md#insn-0070e4b4) · [`0070e4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e48c.md#insn-0070e4c0)
- 新版 [`0070e864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e83c.md#insn-0070e864) · [`0070e870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e83c.md#insn-0070e870)

~~~diff
- 0070e4b4 ["INT_ADD", "register:40f0:8", ["const:70e4b4:8", "const:4:8"]]
- 0070e4b4 ["CALL", null, ["ram:47ad34:8"]]
+ 0070e864 ["INT_ADD", "register:40f0:8", ["const:70e864:8", "const:4:8"]]
+ 0070e864 ["CALL", null, ["ram:47b054:8"]]
- 0070e4b4 bytes 20b2f597
+ 0070e864 bytes fcb1f597
- 0070e4c0 ["INT_ADD", "register:40f0:8", ["const:70e4c0:8", "const:4:8"]]
- 0070e4c0 ["CALL", null, ["callee:0047d134:8"]]
+ 0070e870 ["INT_ADD", "register:40f0:8", ["const:70e870:8", "const:4:8"]]
+ 0070e870 ["CALL", null, ["callee:0047d134:8"]]
- 0070e4c0 bytes 55baf597
+ 0070e870 bytes 31baf597
~~~


<a id="compare-18f373ebc5b1629efcd4b7c7ac088438"></a>

### [`0070e518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e518.md) → [`0070e8c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e8c8.md) FUN_0070e8c8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0070e8e8",
      "incomplete_value": true,
      "site": "0070e8ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e538",
      "incomplete_value": true,
      "site": "0070e53c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "0070e8ec",
      "DATA",
      [
        "storage",
        "00c77968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070e8ec",
      "DATA",
      [
        "storage",
        "00c78938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e518.md#insn-0070e52c) · [`0070e534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e518.md#insn-0070e534) · [`0070e538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e518.md#insn-0070e538)
- 新版 [`0070e8dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e8c8.md#insn-0070e8dc) · [`0070e8e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e8c8.md#insn-0070e8e4) · [`0070e8e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e8c8.md#insn-0070e8e8)

~~~diff
- 0070e52c ["INT_ADD", "register:40f0:8", ["const:70e52c:8", "const:4:8"]]
- 0070e52c ["CALL", null, ["callee:00c58f30:8"]]
+ 0070e8dc ["INT_ADD", "register:40f0:8", ["const:70e8dc:8", "const:4:8"]]
+ 0070e8dc ["CALL", null, ["callee:00c58f30:8"]]
- 0070e52c bytes 8d261594
+ 0070e8dc bytes 95291594
- 0070e534 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0070e8e4 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0070e534 bytes 482b00b0
+ 0070e8e4 bytes 482b00d0
- 0070e538 ["COPY", "tmp:0:8", ["const:968:8"]]
- 0070e538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070e538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070e538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070e8e8 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 0070e8e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e8e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e8e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070e538 bytes 08a12591
+ 0070e8e8 bytes 08e12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eff4f1fbd9868bc2c4c9cebf8237a85f"></a>

### [`0070e550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e550.md) → [`0070e900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e900.md) FUN_0070e900

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
      "definition_site": "0070e904",
      "incomplete_value": false,
      "site": "0070e908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e554",
      "incomplete_value": false,
      "site": "0070e558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
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
      "0070e908",
      "DATA",
      [
        "storage",
        "00c77968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070e908",
      "DATA",
      [
        "storage",
        "00c78938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e550.md#insn-0070e550) · [`0070e554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e550.md#insn-0070e554)
- 新版 [`0070e900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e900.md#insn-0070e900) · [`0070e904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e900.md#insn-0070e904)

~~~diff
- 0070e550 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0070e900 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0070e550 bytes 482b00b0
+ 0070e900 bytes 482b00d0
- 0070e554 ["COPY", "tmp:0:8", ["const:968:8"]]
- 0070e554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070e554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070e554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070e904 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 0070e904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070e554 bytes 08a12591
+ 0070e904 bytes 08e12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62a2b84ae465065796749e5a3185171a"></a>

### [`0070e5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e5a8.md) → [`0070e958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e958.md) FUN_0070e958

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
      "definition_site": "0070e97c",
      "incomplete_value": false,
      "site": "0070e97c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e5cc",
      "incomplete_value": false,
      "site": "0070e5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "0070e97c",
      "DATA",
      [
        "storage",
        "00c779e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070e97c",
      "DATA",
      [
        "storage",
        "00c789b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e5bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e5a8.md#insn-0070e5bc) · [`0070e5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e5a8.md#insn-0070e5c4) · [`0070e5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e5a8.md#insn-0070e5c8)
- 新版 [`0070e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e958.md#insn-0070e96c) · [`0070e974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e958.md#insn-0070e974) · [`0070e978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e958.md#insn-0070e978)

~~~diff
- 0070e5bc ["INT_ADD", "register:40f0:8", ["const:70e5bc:8", "const:4:8"]]
- 0070e5bc ["CALL", null, ["callee:00c58f30:8"]]
+ 0070e96c ["INT_ADD", "register:40f0:8", ["const:70e96c:8", "const:4:8"]]
+ 0070e96c ["CALL", null, ["callee:00c58f30:8"]]
- 0070e5bc bytes 69261594
+ 0070e96c bytes 71291594
- 0070e5c4 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0070e974 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0070e5c4 bytes 482b00b0
+ 0070e974 bytes 482b00d0
- 0070e5c8 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 0070e5c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070e5c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070e5c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070e978 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 0070e978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070e5c8 bytes 08a12791
+ 0070e978 bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bcf13e460b47fda9bedb5b1b54d74fc"></a>

### [`0070e5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e5dc.md) → [`0070e98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e98c.md) FUN_0070e98c

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
      "definition_site": "0070e998",
      "incomplete_value": false,
      "site": "0070e998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e5e8",
      "incomplete_value": false,
      "site": "0070e5e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
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
      "0070e998",
      "DATA",
      [
        "storage",
        "00c779e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070e998",
      "DATA",
      [
        "storage",
        "00c789b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e5dc.md#insn-0070e5e0) · [`0070e5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e5dc.md#insn-0070e5e4)
- 新版 [`0070e990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e98c.md#insn-0070e990) · [`0070e994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e98c.md#insn-0070e994)

~~~diff
- 0070e5e0 ["COPY", "register:4048:8", ["const:c77000:8"]]
+ 0070e990 ["COPY", "register:4048:8", ["const:c78000:8"]]
- 0070e5e0 bytes 492b00b0
+ 0070e990 bytes 492b00d0
- 0070e5e4 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 0070e5e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0070e5e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0070e5e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0070e994 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 0070e994 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0070e994 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0070e994 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0070e5e4 bytes 29a12791
+ 0070e994 bytes 29e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c571f4c4c21e6a83e602c88340309d5"></a>

### [`0070e5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e5f8.md) → [`0070e9a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e9a8.md) FUN_0070e9a8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

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
      "site": "0070e9d0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0070e620",
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
      "0070e9d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "0070e9d0",
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

- 旧版 [`0070e620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e5f8.md#insn-0070e620) · [`0070e62c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e5f8.md#insn-0070e62c)
- 新版 [`0070e9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e9a8.md#insn-0070e9d0) · [`0070e9dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e9a8.md#insn-0070e9dc)

~~~diff
- 0070e620 ["INT_ADD", "register:40f0:8", ["const:70e620:8", "const:4:8"]]
- 0070e620 ["CALL", null, ["ram:47ad34:8"]]
+ 0070e9d0 ["INT_ADD", "register:40f0:8", ["const:70e9d0:8", "const:4:8"]]
+ 0070e9d0 ["CALL", null, ["ram:47b054:8"]]
- 0070e620 bytes c5b1f597
+ 0070e9d0 bytes a1b1f597
- 0070e62c ["INT_ADD", "register:40f0:8", ["const:70e62c:8", "const:4:8"]]
- 0070e62c ["CALL", null, ["callee:0047d134:8"]]
+ 0070e9dc ["INT_ADD", "register:40f0:8", ["const:70e9dc:8", "const:4:8"]]
+ 0070e9dc ["CALL", null, ["callee:0047d134:8"]]
- 0070e62c bytes fab9f597
+ 0070e9dc bytes d6b9f597
~~~


<a id="compare-fbfea65bdc3c5c75309cf2b84228922e"></a>

### [`0070e684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e684.md) → [`0070ea34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ea34.md) FUN_0070ea34

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
      "definition_site": "0070ea54",
      "incomplete_value": false,
      "site": "0070ea58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e6a4",
      "incomplete_value": false,
      "site": "0070e6a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
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
      "0070ea58",
      "DATA",
      [
        "storage",
        "00c77a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070ea58",
      "DATA",
      [
        "storage",
        "00c78a38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e684.md#insn-0070e698) · [`0070e6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e684.md#insn-0070e6a0) · [`0070e6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e684.md#insn-0070e6a4)
- 新版 [`0070ea48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ea34.md#insn-0070ea48) · [`0070ea50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ea34.md#insn-0070ea50) · [`0070ea54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ea34.md#insn-0070ea54)

~~~diff
- 0070e698 ["INT_ADD", "register:40f0:8", ["const:70e698:8", "const:4:8"]]
- 0070e698 ["CALL", null, ["callee:00c58f30:8"]]
+ 0070ea48 ["INT_ADD", "register:40f0:8", ["const:70ea48:8", "const:4:8"]]
+ 0070ea48 ["CALL", null, ["callee:00c58f30:8"]]
- 0070e698 bytes 32261594
+ 0070ea48 bytes 3a291594
- 0070e6a0 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0070ea50 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0070e6a0 bytes 482b00b0
+ 0070ea50 bytes 482b00d0
- 0070e6a4 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 0070e6a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070e6a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070e6a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070ea54 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 0070ea54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070ea54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070ea54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070e6a4 bytes 08a12991
+ 0070ea54 bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f9ea8b77b5f5166326e2f00ce4a1485"></a>

### [`0070e6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e6bc.md) → [`0070ea6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ea6c.md) FUN_0070ea6c

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
      "definition_site": "0070ea70",
      "incomplete_value": false,
      "site": "0070ea74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e6c0",
      "incomplete_value": false,
      "site": "0070e6c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
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
      "0070ea74",
      "DATA",
      [
        "storage",
        "00c77a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070ea74",
      "DATA",
      [
        "storage",
        "00c78a38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e6bc.md#insn-0070e6bc) · [`0070e6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e6bc.md#insn-0070e6c0)
- 新版 [`0070ea6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ea6c.md#insn-0070ea6c) · [`0070ea70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ea6c.md#insn-0070ea70)

~~~diff
- 0070e6bc ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0070ea6c ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0070e6bc bytes 482b00b0
+ 0070ea6c bytes 482b00d0
- 0070e6c0 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 0070e6c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070e6c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070e6c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070ea70 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 0070ea70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070ea70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070ea70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070e6c0 bytes 08a12991
+ 0070ea70 bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b146c2ed1ffce778a02e77e83a72dd3"></a>

### [`0070e710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e710.md) → [`0070eac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070eac0.md) FUN_0070eac0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0070eacc",
      "incomplete_value": true,
      "site": "0070ead0",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e71c",
      "incomplete_value": true,
      "site": "0070e720",
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
      "0070eacc",
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
      "0070eacc",
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

- 旧版 [`0070e720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e710.md#insn-0070e720) · [`0070e718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e710.md#insn-0070e718) · [`0070e71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e710.md#insn-0070e71c)
- 新版 [`0070ead0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070eac0.md#insn-0070ead0) · [`0070eac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070eac0.md#insn-0070eac8) · [`0070eacc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070eac0.md#insn-0070eacc)

~~~diff
- 0070e720 ["INT_ADD", "register:40f0:8", ["const:70e720:8", "const:4:8"]]
- 0070e720 ["CALL", null, ["callee:0043bad8:8"]]
+ 0070ead0 ["INT_ADD", "register:40f0:8", ["const:70ead0:8", "const:4:8"]]
+ 0070ead0 ["CALL", null, ["callee:0043bad8:8"]]
- 0070e720 bytes 26b4f497
+ 0070ead0 bytes 02b4f497
- 0070e718 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0070eac8 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0070e718 bytes 40ddffb0
+ 0070eac8 bytes 40ddffd0
- 0070e71c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0070e71c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0070e71c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0070e71c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0070eacc ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0070eacc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0070eacc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0070eacc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0070e71c bytes 00303e91
+ 0070eacc bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c101350372645e4e53a29a972c65d92e"></a>

### [`0070e724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e724.md) → [`0070ead4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ead4.md) _INIT_112

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.88% / 新版 85.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0070eb10",
      "incomplete_value": true,
      "site": "0070eb2c",
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
                "live",
                "register:4048:8"
              ],
              [
                "leaf",
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e760",
      "incomplete_value": true,
      "site": "0070e77c",
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
                "live",
                "register:4048:8"
              ],
              [
                "leaf",
                "const:f66:8"
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
      "definition_site": "0070eb34",
      "incomplete_value": true,
      "site": "0070eb50",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e784",
      "incomplete_value": true,
      "site": "0070e7a0",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f79:8"
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
      "definition_site": "0070eb54",
      "incomplete_value": true,
      "site": "0070eb70",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e7a4",
      "incomplete_value": true,
      "site": "0070e7c0",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
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
      "0070eb10",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0070eb34",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0070eb54",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0070eb10",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0070eb34",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0070eb54",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e724.md#insn-0070e958) · [`0070e74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e724.md#insn-0070e74c) · [`0070e750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e724.md#insn-0070e750)
- 新版 [`0070ed08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ead4.md#insn-0070ed08) · [`0070eafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ead4.md#insn-0070eafc) · [`0070eb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ead4.md#insn-0070eb00)

~~~diff
- 0070e958 ["INT_ADD", "register:40f0:8", ["const:70e958:8", "const:4:8"]]
- 0070e958 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0070ed08 ["INT_ADD", "register:40f0:8", ["const:70ed08:8", "const:4:8"]]
+ 0070ed08 ["CALL", null, ["callee:00c58ed0:8"]]
- 0070e958 bytes 6a251594
+ 0070ed08 bytes 72281594
- 0070e74c ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 0070eafc ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 0070e74c bytes d32c00b0
+ 0070eafc bytes d32c00d0
- 0070e750 ["COPY", "tmp:0:8", ["const:cf0:8"]]
- 0070e750 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0070e750 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0070e750 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0070eb00 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 0070eb00 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0070eb00 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0070eb00 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0070e750 bytes 73c23391
+ 0070eb00 bytes 73c23291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15c78865b9974f39903e7473a068919e"></a>

### [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) → [`0070ee64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ee64.md) FUN_0070ee64

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`007133b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/007133b0.md) [`00714c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714c40.md) [`00714fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714fe4.md) [`00715458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00715/00715458.md) · 呼出先 87件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md)
- 新版 呼出元 4件 [`00713760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00713/00713760.md) [`00714ff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/00714ff0.md) [`00715394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/00715394.md) [`00715808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/00715808.md) · 呼出先 87件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.24% / 新版 98.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0070f0a4",
      "incomplete_value": true,
      "site": "0070f0b4",
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
                "const:9b4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070ecf4",
      "incomplete_value": true,
      "site": "0070ed04",
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
                "const:8d6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007100f4",
      "incomplete_value": true,
      "site": "00710104",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070fd44",
      "incomplete_value": true,
      "site": "0070fd54",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 122,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007100f0",
      "incomplete_value": true,
      "site": "00710104",
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
                "const:e19:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070fd40",
      "incomplete_value": true,
      "site": "0070fd54",
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
                "const:d42:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 123,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0070f0a4",
      "READ",
      [
        "storage",
        "002bc8d6",
        null,
        "string"
      ]
    ],
    [
      "0070f3dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00aff6c8"
      ]
    ],
    [
      "0070f400",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00aff6c8"
      ]
    ]
  ],
  "added": [
    [
      "0070f0a4",
      "READ",
      [
        "storage",
        "002bc9b4",
        null,
        "string"
      ]
    ],
    [
      "0070f3dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b006bc"
      ]
    ],
    [
      "0070f400",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b006bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070f02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md#insn-0070f02c) · [`0070f050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md#insn-0070f050) · [`0070f25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md#insn-0070f25c)
- 新版 [`0070f3dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ee64.md#insn-0070f3dc) · [`0070f400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ee64.md#insn-0070f400) · [`0070f60c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ee64.md#insn-0070f60c)

~~~diff
- 0070f02c ["INT_ADD", "register:40f0:8", ["const:70f02c:8", "const:4:8"]]
- 0070f02c ["CALL", null, ["ram:aff6c8:8"]]
+ 0070f3dc ["INT_ADD", "register:40f0:8", ["const:70f3dc:8", "const:4:8"]]
+ 0070f3dc ["CALL", null, ["ram:b006bc:8"]]
- 0070f02c bytes a7c10f94
+ 0070f3dc bytes b8c40f94
- 0070f050 ["INT_ADD", "register:40f0:8", ["const:70f050:8", "const:4:8"]]
- 0070f050 ["CALL", null, ["ram:aff6c8:8"]]
+ 0070f400 ["INT_ADD", "register:40f0:8", ["const:70f400:8", "const:4:8"]]
+ 0070f400 ["CALL", null, ["ram:b006bc:8"]]
- 0070f050 bytes 9ec10f94
+ 0070f400 bytes afc40f94
- 0070f25c ["INT_ADD", "register:40f0:8", ["const:70f25c:8", "const:4:8"]]
- 0070f25c ["CALL", null, ["callee:0043e138:8"]]
+ 0070f60c ["INT_ADD", "register:40f0:8", ["const:70f60c:8", "const:4:8"]]
+ 0070f60c ["CALL", null, ["callee:0043e138:8"]]
- 0070f25c bytes efbaf497
+ 0070f60c bytes cbbaf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bf0a1c144ddaefc476650ac8ce042f3"></a>

### [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) → [`007106e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00710/007106e0.md) FUN_007106e0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`005fb97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fb/005fb97c.md) [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 63件 [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`005e0ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0ee8.md) [`005e0f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0f2c.md) [`005e1b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1b70.md) [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md)
- 新版 呼出元 3件 [`005fbd2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fb/005fbd2c.md) [`0070ee64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ee64.md) [`00711df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00711/00711df8.md) · 呼出先 63件 [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`005e1298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1298.md) [`005e12dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e12dc.md) [`005e1f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1f20.md) [`005e7810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e7/005e7810.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.66% / 新版 93.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 43件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00710860",
      "incomplete_value": true,
      "site": "00710870",
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
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007104b0",
      "incomplete_value": true,
      "site": "007104c0",
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
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00710874",
      "incomplete_value": true,
      "site": "00710884",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:444:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007104c4",
      "incomplete_value": true,
      "site": "007104d4",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:404:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00710874",
      "incomplete_value": true,
      "site": "00710884",
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
      "definition_site": "007104c4",
      "incomplete_value": true,
      "site": "007104d4",
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
      "00710860",
      "READ",
      [
        "storage",
        "002c32e0",
        null,
        null
      ]
    ],
    [
      "00710874",
      "READ",
      [
        "storage",
        "002a0404",
        null,
        "string"
      ]
    ],
    [
      "00710874",
      "READ",
      [
        "storage",
        "002a0414",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00710860",
      "READ",
      [
        "storage",
        "002c3330",
        null,
        null
      ]
    ],
    [
      "00710874",
      "READ",
      [
        "storage",
        "002a0444",
        null,
        "string"
      ]
    ],
    [
      "00710874",
      "READ",
      [
        "storage",
        "002a0454",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007103cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md#insn-007103cc) · [`0071054c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md#insn-0071054c) · [`00710f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md#insn-00710f68)
- 新版 [`0071077c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00710/007106e0.md#insn-0071077c) · [`007108fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00710/007106e0.md#insn-007108fc) · [`00711318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00710/007106e0.md#insn-00711318)

~~~diff
- 007103cc ["INT_ADD", "register:40f0:8", ["const:7103cc:8", "const:4:8"]]
- 007103cc ["CALL", null, ["callee:005e1f20:8"]]
+ 0071077c ["INT_ADD", "register:40f0:8", ["const:71077c:8", "const:4:8"]]
+ 0071077c ["CALL", null, ["callee:005e1f20:8"]]
- 007103cc bytes e945fb97
+ 0071077c bytes e945fb97
- 0071054c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6c0:8"]]
- 0071054c ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
- 0071054c ["COPY", "register:5050:8", ["const:0:8"]]
- 0071054c ["COPY", "register:5058:8", ["const:0:8"]]
+ 007108fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:710:8"]]
+ 007108fc ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
+ 007108fc ["COPY", "register:5050:8", ["const:0:8"]]
+ 007108fc ["COPY", "register:5058:8", ["const:0:8"]]
- 0071054c bytes 22b1c13d
+ 007108fc bytes 22c5c13d
- 00710f68 ["INT_ADD", "register:40f0:8", ["const:710f68:8", "const:4:8"]]
- 00710f68 ["CALL", null, ["callee:00af82a8:8"]]
+ 00711318 ["INT_ADD", "register:40f0:8", ["const:711318:8", "const:4:8"]]
+ 00711318 ["CALL", null, ["callee:00af82a8:8"]]
- 00710f68 bytes d3980f94
+ 00711318 bytes e49b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f9abd8adb7d26c10d099de0ce11a6bf"></a>

### [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) → [`00711df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00711/00711df8.md) FUN_00711df8

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`007142b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/007142b4.md) [`00714e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714e10.md) [`00714fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714fe4.md) [`00715458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00715/00715458.md) · 呼出先 99件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0046dafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046dafc.md) [`005e0ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0ee8.md) [`005e0f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0f2c.md)
- 新版 呼出元 4件 [`00714664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/00714664.md) [`007151c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/007151c0.md) [`00715394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/00715394.md) [`00715808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/00715808.md) · 呼出先 99件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0046de1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de1c.md) [`005e1298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1298.md) [`005e12dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e12dc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00712c14",
      "incomplete_value": true,
      "site": "00712c20",
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
      "definition_site": "00712864",
      "incomplete_value": true,
      "site": "00712870",
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
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0071243c",
      "incomplete_value": false,
      "site": "00712444",
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
            "const:40c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071208c",
      "incomplete_value": false,
      "site": "00712094",
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
            "const:3cc:8"
          ]
        ]
      ]
    },
    "ordinal": 60,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00712cf4",
      "incomplete_value": false,
      "site": "00712cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:8a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00712944",
      "incomplete_value": false,
      "site": "0071294c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:7da:8"
          ]
        ]
      ]
    },
    "ordinal": 139,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00712058",
      "READ",
      [
        "storage",
        "002bc8d6",
        null,
        "string"
      ]
    ],
    [
      "0071243c",
      "PARAM",
      [
        "storage",
        "002a03cc",
        null,
        null
      ]
    ],
    [
      "00712c14",
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
      "00712058",
      "READ",
      [
        "storage",
        "002bc9b4",
        null,
        "string"
      ]
    ],
    [
      "0071243c",
      "PARAM",
      [
        "storage",
        "002a040c",
        null,
        null
      ]
    ],
    [
      "00712c14",
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

- 旧版 [`00712094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md#insn-00712094) · [`0071259c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md#insn-0071259c) · [`0071294c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md#insn-0071294c)
- 新版 [`00712444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00711/00711df8.md#insn-00712444) · [`0071294c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00711/00711df8.md#insn-0071294c) · [`00712cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00711/00711df8.md#insn-00712cfc)

~~~diff
- 00712094 ["INT_ADD", "register:40f0:8", ["const:712094:8", "const:4:8"]]
- 00712094 ["CALL", null, ["callee:0043e138:8"]]
+ 00712444 ["INT_ADD", "register:40f0:8", ["const:712444:8", "const:4:8"]]
+ 00712444 ["CALL", null, ["callee:0043e138:8"]]
- 00712094 bytes 61aff497
+ 00712444 bytes 3daff497
- 0071259c ["INT_ADD", "register:40f0:8", ["const:71259c:8", "const:4:8"]]
- 0071259c ["CALL", null, ["callee:00af7b50:8"]]
+ 0071294c ["INT_ADD", "register:40f0:8", ["const:71294c:8", "const:4:8"]]
+ 0071294c ["CALL", null, ["callee:00af7b50:8"]]
- 0071259c bytes 70910f94
+ 0071294c bytes 81940f94
- 0071294c ["INT_ADD", "register:40f0:8", ["const:71294c:8", "const:4:8"]]
- 0071294c ["CALL", null, ["callee:0043e138:8"]]
+ 00712cfc ["INT_ADD", "register:40f0:8", ["const:712cfc:8", "const:4:8"]]
+ 00712cfc ["CALL", null, ["callee:0043e138:8"]]
- 0071294c bytes 33adf497
+ 00712cfc bytes 0fadf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c44c9fbbfed7db00387f14974ac0623"></a>

### [`007142b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/007142b4.md) → [`00714664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/00714664.md) FUN_00714664

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 28件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0046da88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da88.md) [`005fe288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe288.md)
- 新版 呼出元 1件 [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) · 呼出先 28件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0046dda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046dda8.md) [`005fe638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fe638.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007146d4",
      "incomplete_value": true,
      "site": "007146d4",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:125:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00714324",
      "incomplete_value": true,
      "site": "00714324",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:47:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00714a20",
      "incomplete_value": true,
      "site": "00714a38",
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
                "const:100:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00714670",
      "incomplete_value": true,
      "site": "00714688",
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
                "const:b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 55,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007146ac",
      "value": [
        "leaf",
        "ram:af4aec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007142fc",
      "value": [
        "leaf",
        "ram:af3af8:8"
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
      "007146ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af3af8"
      ]
    ],
    [
      "007146c4",
      "READ",
      [
        "storage",
        "002bf047",
        null,
        "undefined8"
      ]
    ],
    [
      "0071474c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00713d7c"
      ]
    ]
  ],
  "added": [
    [
      "007146ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af4aec"
      ]
    ],
    [
      "007146c4",
      "READ",
      [
        "storage",
        "002bf125",
        null,
        "undefined8"
      ]
    ],
    [
      "0071474c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071412c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007142fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/007142b4.md#insn-007142fc) · [`0071439c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/007142b4.md#insn-0071439c) · [`007144a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/007142b4.md#insn-007144a4)
- 新版 [`007146ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/00714664.md#insn-007146ac) · [`0071474c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/00714664.md#insn-0071474c) · [`00714854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/00714664.md#insn-00714854)

~~~diff
- 007142fc ["INT_ADD", "register:40f0:8", ["const:7142fc:8", "const:4:8"]]
- 007142fc ["CALL", null, ["ram:af3af8:8"]]
+ 007146ac ["INT_ADD", "register:40f0:8", ["const:7146ac:8", "const:4:8"]]
+ 007146ac ["CALL", null, ["ram:af4aec:8"]]
- 007142fc bytes ff7d0f94
+ 007146ac bytes 10810f94
- 0071439c ["INT_ADD", "register:40f0:8", ["const:71439c:8", "const:4:8"]]
- 0071439c ["CALL", null, ["ram:713d7c:8"]]
+ 0071474c ["INT_ADD", "register:40f0:8", ["const:71474c:8", "const:4:8"]]
+ 0071474c ["CALL", null, ["ram:71412c:8"]]
- 0071439c bytes 78feff97
+ 0071474c bytes 78feff97
- 007144a4 ["INT_ADD", "register:40f0:8", ["const:7144a4:8", "const:4:8"]]
- 007144a4 ["CALL", null, ["ram:af3af8:8"]]
+ 00714854 ["INT_ADD", "register:40f0:8", ["const:714854:8", "const:4:8"]]
+ 00714854 ["CALL", null, ["ram:af4aec:8"]]
- 007144a4 bytes 957d0f94
+ 00714854 bytes a6800f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7385347019feda59f3fceb6dac5ea487"></a>

### [`00714c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714c40.md) → [`00714ff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/00714ff0.md) FUN_00714ff0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005f7980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f7/005f7980.md) · 呼出先 5件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00af3af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af3af8.md) [`00afab64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afab64.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`005f7d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005f7/005f7d30.md) · 呼出先 5件 [`0070ee64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ee64.md) [`00af4aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af4/00af4aec.md) [`00afbb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afb/00afbb58.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.10% / 新版 98.10%

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
      "site": "00715048",
      "value": [
        "leaf",
        "ram:af4aec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00714c98",
      "value": [
        "leaf",
        "ram:af3af8:8"
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
      "site": "00715058",
      "value": [
        "leaf",
        "ram:af4aec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00714ca8",
      "value": [
        "leaf",
        "ram:af3af8:8"
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
      "00715048",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af3af8"
      ]
    ],
    [
      "00715058",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af3af8"
      ]
    ],
    [
      "00715114",
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
      "00715048",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af4aec"
      ]
    ],
    [
      "00715058",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af4aec"
      ]
    ],
    [
      "00715114",
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

- 旧版 [`00714c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714c40.md#insn-00714c98) · [`00714ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714c40.md#insn-00714ca8) · [`00714cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714c40.md#insn-00714cb8)
- 新版 [`00715048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/00714ff0.md#insn-00715048) · [`00715058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/00714ff0.md#insn-00715058) · [`00715068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/00714ff0.md#insn-00715068)

~~~diff
- 00714c98 ["INT_ADD", "register:40f0:8", ["const:714c98:8", "const:4:8"]]
- 00714c98 ["CALL", null, ["ram:af3af8:8"]]
+ 00715048 ["INT_ADD", "register:40f0:8", ["const:715048:8", "const:4:8"]]
+ 00715048 ["CALL", null, ["ram:af4aec:8"]]
- 00714c98 bytes 987b0f94
+ 00715048 bytes a97e0f94
- 00714ca8 ["INT_ADD", "register:40f0:8", ["const:714ca8:8", "const:4:8"]]
- 00714ca8 ["CALL", null, ["ram:af3af8:8"]]
+ 00715058 ["INT_ADD", "register:40f0:8", ["const:715058:8", "const:4:8"]]
+ 00715058 ["CALL", null, ["ram:af4aec:8"]]
- 00714ca8 bytes 947b0f94
+ 00715058 bytes a57e0f94
- 00714cb8 ["INT_ADD", "register:40f0:8", ["const:714cb8:8", "const:4:8"]]
- 00714cb8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00715068 ["INT_ADD", "register:40f0:8", ["const:715068:8", "const:4:8"]]
+ 00715068 ["CALL", null, ["callee:00c58f50:8"]]
- 00714cb8 bytes b20c1594
+ 00715068 bytes ba0f1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d37bb7ad815ce7d0d44a4a62a408276"></a>

### [`00714e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714e10.md) → [`007151c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/007151c0.md) FUN_007151c0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005f7980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f7/005f7980.md) · 呼出先 5件 [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) [`00af3af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af3af8.md) [`00afab64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afab64.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`005f7d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005f7/005f7d30.md) · 呼出先 5件 [`00711df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00711/00711df8.md) [`00af4aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af4/00af4aec.md) [`00afbb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afb/00afbb58.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "site": "00715218",
      "value": [
        "leaf",
        "ram:af4aec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00714e68",
      "value": [
        "leaf",
        "ram:af3af8:8"
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
      "site": "00715228",
      "value": [
        "leaf",
        "ram:af4aec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00714e78",
      "value": [
        "leaf",
        "ram:af3af8:8"
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
      "00715218",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af3af8"
      ]
    ],
    [
      "00715228",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af3af8"
      ]
    ],
    [
      "007152e8",
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
      "00715218",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af4aec"
      ]
    ],
    [
      "00715228",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af4aec"
      ]
    ],
    [
      "007152e8",
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

- 旧版 [`00714e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714e10.md#insn-00714e68) · [`00714e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714e10.md#insn-00714e78) · [`00714e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714e10.md#insn-00714e88)
- 新版 [`00715218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/007151c0.md#insn-00715218) · [`00715228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/007151c0.md#insn-00715228) · [`00715238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/007151c0.md#insn-00715238)

~~~diff
- 00714e68 ["INT_ADD", "register:40f0:8", ["const:714e68:8", "const:4:8"]]
- 00714e68 ["CALL", null, ["ram:af3af8:8"]]
+ 00715218 ["INT_ADD", "register:40f0:8", ["const:715218:8", "const:4:8"]]
+ 00715218 ["CALL", null, ["ram:af4aec:8"]]
- 00714e68 bytes 247b0f94
+ 00715218 bytes 357e0f94
- 00714e78 ["INT_ADD", "register:40f0:8", ["const:714e78:8", "const:4:8"]]
- 00714e78 ["CALL", null, ["ram:af3af8:8"]]
+ 00715228 ["INT_ADD", "register:40f0:8", ["const:715228:8", "const:4:8"]]
+ 00715228 ["CALL", null, ["ram:af4aec:8"]]
- 00714e78 bytes 207b0f94
+ 00715228 bytes 317e0f94
- 00714e88 ["INT_ADD", "register:40f0:8", ["const:714e88:8", "const:4:8"]]
- 00714e88 ["CALL", null, ["callee:00c58f50:8"]]
+ 00715238 ["INT_ADD", "register:40f0:8", ["const:715238:8", "const:4:8"]]
+ 00715238 ["CALL", null, ["callee:00c58f50:8"]]
- 00714e88 bytes 3e0c1594
+ 00715238 bytes 460f1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-661972434fdbf5f1c5eefc2db2b37397"></a>

### [`00715558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00715/00715558.md) → [`00715908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/00715908.md) FUN_00715908

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) · 呼出先 81件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0046da88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da88.md) [`0046dafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046dafc.md) [`0046db14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db14.md)
- 新版 呼出元 2件 [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) [`00717198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00717/00717198.md) · 呼出先 81件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0046dda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046dda8.md) [`0046de1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de1c.md) [`0046de34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de34.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.16% / 新版 98.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 9件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00715aa4",
      "incomplete_value": true,
      "site": "00715ab8",
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
                "const:820:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007156f4",
      "incomplete_value": true,
      "site": "00715708",
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
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071607c",
      "incomplete_value": true,
      "site": "0071608c",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00715ccc",
      "incomplete_value": true,
      "site": "00715cdc",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00716088",
      "incomplete_value": true,
      "site": "00716090",
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
                "const:39b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00715cd8",
      "incomplete_value": true,
      "site": "00715ce0",
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
                "const:2cc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00715aa4",
      "READ",
      [
        "storage",
        "002c27d0",
        null,
        null
      ]
    ],
    [
      "00715cf8",
      "READ",
      [
        "storage",
        "00c9b5f8",
        null,
        "pointer"
      ]
    ],
    [
      "00715cfc",
      "DATA",
      [
        "storage",
        "00ca407c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00715aa4",
      "READ",
      [
        "storage",
        "002c2820",
        null,
        null
      ]
    ],
    [
      "00715cf8",
      "READ",
      [
        "storage",
        "00c9c5c8",
        null,
        "pointer"
      ]
    ],
    [
      "00715cfc",
      "DATA",
      [
        "storage",
        "00ca504c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007159a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00715/00715558.md#insn-007159a4) · [`00715dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00715/00715558.md#insn-00715dbc) · [`00715f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00715/00715558.md#insn-00715f54)
- 新版 [`00715d54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/00715908.md#insn-00715d54) · [`0071616c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/00715908.md#insn-0071616c) · [`00716304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/00715908.md#insn-00716304)

~~~diff
- 007159a4 ["INT_ADD", "register:40f0:8", ["const:7159a4:8", "const:4:8"]]
- 007159a4 ["CALL", null, ["ram:47ad34:8"]]
+ 00715d54 ["INT_ADD", "register:40f0:8", ["const:715d54:8", "const:4:8"]]
+ 00715d54 ["CALL", null, ["ram:47b054:8"]]
- 007159a4 bytes e494f597
+ 00715d54 bytes c094f597
- 00715dbc ["INT_ADD", "register:40f0:8", ["const:715dbc:8", "const:4:8"]]
- 00715dbc ["CALL", null, ["ram:713d7c:8"]]
+ 0071616c ["INT_ADD", "register:40f0:8", ["const:71616c:8", "const:4:8"]]
+ 0071616c ["CALL", null, ["ram:71412c:8"]]
- 00715dbc bytes f0f7ff97
+ 0071616c bytes f0f7ff97
- 00715f54 ["INT_ADD", "register:40f0:8", ["const:715f54:8", "const:4:8"]]
- 00715f54 ["CALL", null, ["callee:00682854:8"]]
+ 00716304 ["INT_ADD", "register:40f0:8", ["const:716304:8", "const:4:8"]]
+ 00716304 ["CALL", null, ["callee:00682854:8"]]
- 00715f54 bytes 54b1fd97
+ 00716304 bytes 54b1fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b40fe6ea142a85c74e590d7a8ea4044"></a>

### [`00716bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716bd8.md) → [`00716f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00716/00716f88.md) FUN_00716f88

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00715558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00715/00715558.md) [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) · 呼出先 17件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce1c.md) [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a51c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a51/00a51c48.md)
- 新版 呼出元 2件 [`00715908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/00715908.md) [`00717198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00717/00717198.md) · 呼出先 17件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d13c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d13c.md) [`005e7810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e7/005e7810.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00a52c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a52/00a52c3c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.24% / 新版 99.24%

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
      "site": "007170f8",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00716d48",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007170f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "007170f8",
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

- 旧版 [`00716d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716bd8.md#insn-00716d48) · [`00716c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716bd8.md#insn-00716c04) · [`00716c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716bd8.md#insn-00716c20)
- 新版 [`007170f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00716/00716f88.md#insn-007170f8) · [`00716fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00716/00716f88.md#insn-00716fb4) · [`00716fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00716/00716f88.md#insn-00716fd0)

~~~diff
- 00716d48 ["INT_ADD", "register:40f0:8", ["const:716d48:8", "const:4:8"]]
- 00716d48 ["CALL", null, ["ram:47ad34:8"]]
+ 007170f8 ["INT_ADD", "register:40f0:8", ["const:7170f8:8", "const:4:8"]]
+ 007170f8 ["CALL", null, ["ram:47b054:8"]]
- 00716d48 bytes fb8ff597
+ 007170f8 bytes d78ff597
- 00716c04 ["INT_ADD", "register:40f0:8", ["const:716c04:8", "const:4:8"]]
- 00716c04 ["CALL", null, ["callee:00af4cac:8"]]
+ 00716fb4 ["INT_ADD", "register:40f0:8", ["const:716fb4:8", "const:4:8"]]
+ 00716fb4 ["CALL", null, ["callee:00af4cac:8"]]
- 00716c04 bytes 2d740f94
+ 00716fb4 bytes 3e770f94
- 00716c20 ["INT_ADD", "register:40f0:8", ["const:716c20:8", "const:4:8"]]
- 00716c20 ["CALL", null, ["callee:00a52c3c:8"]]
+ 00716fd0 ["INT_ADD", "register:40f0:8", ["const:716fd0:8", "const:4:8"]]
+ 00716fd0 ["CALL", null, ["callee:00a52c3c:8"]]
- 00716c20 bytes 0aec0c94
+ 00716fd0 bytes 1bef0c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9bf82f3964906408c072dd4e9cbe694"></a>

### [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) → [`00717198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00717/00717198.md) FUN_00717198

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 123件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0046da88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da88.md) [`0046dafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046dafc.md) [`0046db14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db14.md)
- 新版 呼出元 1件 [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) · 呼出先 123件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0046dda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046dda8.md) [`0046de1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de1c.md) [`0046de34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de34.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00717b18",
      "incomplete_value": true,
      "site": "00717b1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:39b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00717768",
      "incomplete_value": true,
      "site": "0071776c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:2cc:8"
          ]
        ]
      ]
    },
    "ordinal": 90,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00717b88",
      "incomplete_value": false,
      "site": "00717b8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:39b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007177d8",
      "incomplete_value": false,
      "site": "007177dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:2cc:8"
          ]
        ]
      ]
    },
    "ordinal": 96,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00717bd0",
      "value": [
        "leaf",
        "ram:71412c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00717820",
      "value": [
        "leaf",
        "ram:713d7c:8"
      ]
    },
    "ordinal": 99,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00717278",
      "READ",
      [
        "storage",
        "002c3f80",
        null,
        "undefined8"
      ]
    ],
    [
      "00717954",
      "READ",
      [
        "storage",
        "00c9b5f8",
        null,
        "pointer"
      ]
    ],
    [
      "00717958",
      "DATA",
      [
        "storage",
        "00ca407c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00717278",
      "READ",
      [
        "storage",
        "002c3fd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00717954",
      "READ",
      [
        "storage",
        "00c9c5c8",
        null,
        "pointer"
      ]
    ],
    [
      "00717958",
      "DATA",
      [
        "storage",
        "00ca504c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00717470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md#insn-00717470) · [`0071776c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md#insn-0071776c) · [`007177dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md#insn-007177dc)
- 新版 [`00717820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00717/00717198.md#insn-00717820) · [`00717b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00717/00717198.md#insn-00717b1c) · [`00717b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00717/00717198.md#insn-00717b8c)

~~~diff
- 00717470 ["INT_ADD", "register:40f0:8", ["const:717470:8", "const:4:8"]]
- 00717470 ["CALL", null, ["callee:00af4e94:8"]]
+ 00717820 ["INT_ADD", "register:40f0:8", ["const:717820:8", "const:4:8"]]
+ 00717820 ["CALL", null, ["callee:00af4e94:8"]]
- 00717470 bytes 8c720f94
+ 00717820 bytes 9d750f94
- 0071776c ["INT_ADD", "register:40f0:8", ["const:71776c:8", "const:4:8"]]
- 0071776c ["CALL", null, ["callee:0043e138:8"]]
+ 00717b1c ["INT_ADD", "register:40f0:8", ["const:717b1c:8", "const:4:8"]]
+ 00717b1c ["CALL", null, ["callee:0043e138:8"]]
- 0071776c bytes ab99f497
+ 00717b1c bytes 8799f497
- 007177dc ["INT_ADD", "register:40f0:8", ["const:7177dc:8", "const:4:8"]]
- 007177dc ["CALL", null, ["callee:0043e138:8"]]
+ 00717b8c ["INT_ADD", "register:40f0:8", ["const:717b8c:8", "const:4:8"]]
+ 00717b8c ["CALL", null, ["callee:0043e138:8"]]
- 007177dc bytes 8f99f497
+ 00717b8c bytes 6b99f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82faab186e7db945fa5bd0105157cc53"></a>

### [`007187cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00718/007187cc.md) → [`00718b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00718/00718b7c.md) FUN_00718b7c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 24件 [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`005e0fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0fd0.md) [`005e1660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1660.md)
- 新版 呼出元 1件 [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) · 呼出先 24件 [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`005e1380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1380.md) [`005e1a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1a10.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.87% / 新版 99.87%

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
      "site": "00719708",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00719358",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 51,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00719708",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00719708",
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

- 旧版 [`00719358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00718/007187cc.md#insn-00719358) · [`00718838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00718/007187cc.md#insn-00718838) · [`0071887c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00718/007187cc.md#insn-0071887c)
- 新版 [`00719708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00718/00718b7c.md#insn-00719708) · [`00718be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00718/00718b7c.md#insn-00718be8) · [`00718c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00718/00718b7c.md#insn-00718c2c)

~~~diff
- 00719358 ["INT_ADD", "register:40f0:8", ["const:719358:8", "const:4:8"]]
- 00719358 ["CALL", null, ["ram:47ad34:8"]]
+ 00719708 ["INT_ADD", "register:40f0:8", ["const:719708:8", "const:4:8"]]
+ 00719708 ["CALL", null, ["ram:47b054:8"]]
- 00719358 bytes 7786f597
+ 00719708 bytes 5386f597
- 00718838 ["INT_ADD", "register:40f0:8", ["const:718838:8", "const:4:8"]]
- 00718838 ["CALL", null, ["callee:00a43938:8"]]
+ 00718be8 ["INT_ADD", "register:40f0:8", ["const:718be8:8", "const:4:8"]]
+ 00718be8 ["CALL", null, ["callee:00a43938:8"]]
- 00718838 bytes 43a80c94
+ 00718be8 bytes 54ab0c94
- 0071887c ["INT_ADD", "register:40f0:8", ["const:71887c:8", "const:4:8"]]
- 0071887c ["CALL", null, ["callee:00af4980:8"]]
+ 00718c2c ["INT_ADD", "register:40f0:8", ["const:718c2c:8", "const:4:8"]]
+ 00718c2c ["CALL", null, ["callee:00af4980:8"]]
- 0071887c bytes 446c0f94
+ 00718c2c bytes 556f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bfd308d1897b5ff54dc86d060d75660"></a>

### [`00719768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719768.md) → [`00719b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719b18.md) FUN_00719b18

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007133b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00713/007133b0.md) [`007142b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/007142b4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`00713760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00713/00713760.md) [`00714664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/00714664.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00719b24",
      "incomplete_value": false,
      "site": "00719b28",
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
      "definition_site": "00719774",
      "incomplete_value": false,
      "site": "00719778",
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
      "00719b24",
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
      "00719b24",
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

- 旧版 [`00719778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719768.md#insn-00719778) · [`00719770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719768.md#insn-00719770) · [`00719774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719768.md#insn-00719774)
- 新版 [`00719b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719b18.md#insn-00719b28) · [`00719b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719b18.md#insn-00719b20) · [`00719b24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719b18.md#insn-00719b24)

~~~diff
- 00719778 ["INT_ADD", "register:40f0:8", ["const:719778:8", "const:4:8"]]
- 00719778 ["CALL", null, ["callee:0043bad8:8"]]
+ 00719b28 ["INT_ADD", "register:40f0:8", ["const:719b28:8", "const:4:8"]]
+ 00719b28 ["CALL", null, ["callee:0043bad8:8"]]
- 00719778 bytes 1088f497
+ 00719b28 bytes ec87f497
- 00719770 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00719b20 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00719770 bytes e0dcffd0
+ 00719b20 bytes e0dcfff0
- 00719774 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00719774 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00719774 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00719774 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00719b24 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00719b24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00719b24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00719b24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00719774 bytes 00303e91
+ 00719b24 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45dd2e34f90a51a832e4624a9c4816c4"></a>

### [`0071986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/0071986c.md) → [`00719c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719c1c.md) _INIT_113

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00719c7c",
      "incomplete_value": true,
      "site": "00719c98",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007198cc",
      "incomplete_value": true,
      "site": "007198e8",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f79:8"
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
      "definition_site": "00719cbc",
      "incomplete_value": true,
      "site": "00719cd4",
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071990c",
      "incomplete_value": true,
      "site": "00719924",
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
                "const:f15:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00719e44",
      "incomplete_value": false,
      "site": "00719e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca8000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00719a94",
      "incomplete_value": false,
      "site": "00719aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca7000:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00719c58",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00719c7c",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00719c9c",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00719c58",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00719c7c",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "00719c9c",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00719aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/0071986c.md#insn-00719aa0) · [`00719894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/0071986c.md#insn-00719894) · [`00719898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/0071986c.md#insn-00719898)
- 新版 [`00719e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719c1c.md#insn-00719e50) · [`00719c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719c1c.md#insn-00719c44) · [`00719c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719c1c.md#insn-00719c48)

~~~diff
- 00719aa0 ["INT_ADD", "register:40f0:8", ["const:719aa0:8", "const:4:8"]]
- 00719aa0 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00719e50 ["INT_ADD", "register:40f0:8", ["const:719e50:8", "const:4:8"]]
+ 00719e50 ["CALL", null, ["callee:00c58ed0:8"]]
- 00719aa0 bytes 18f91494
+ 00719e50 bytes 20fc1494
- 00719894 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 00719c44 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 00719894 bytes 732c00d0
+ 00719c44 bytes 732c00f0
- 00719898 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00719898 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00719898 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00719898 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00719c48 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 00719c48 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00719c48 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00719c48 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00719898 bytes 73223491
+ 00719c48 bytes 73223391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2cd6fcd9fb14cd79fd6a50937bc5555"></a>

### [`00719cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719cc0.md) → [`0071a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a070.md) FUN_0071a070

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009d906c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d9/009d906c.md) · 呼出先 18件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)
- 新版 呼出元 1件 [`009da018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009da/009da018.md) · 呼出先 18件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00487c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c8c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487dc4.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.62% / 新版 94.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071a0b4",
      "incomplete_value": false,
      "site": "0071a0b8",
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
      "definition_site": "00719d04",
      "incomplete_value": false,
      "site": "00719d08",
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
      "definition_site": "0071a0e4",
      "incomplete_value": true,
      "site": "0071a0f4",
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
                "const:d40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00719d34",
      "incomplete_value": true,
      "site": "00719d44",
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
                "const:cf0:8"
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
      "definition_site": "0071a0dc",
      "incomplete_value": true,
      "site": "0071a0f8",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:4ec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00719d2c",
      "incomplete_value": true,
      "site": "00719d48",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:421:8"
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
      "0071a0b8",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "0071a0dc",
      "READ",
      [
        "storage",
        "002a3421",
        null,
        "string"
      ]
    ],
    [
      "0071a0dc",
      "READ",
      [
        "storage",
        "002a3431",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0071a0b8",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "0071a0dc",
      "READ",
      [
        "storage",
        "002a34ec",
        null,
        "string"
      ]
    ],
    [
      "0071a0dc",
      "READ",
      [
        "storage",
        "002a34fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00719d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719cc0.md#insn-00719d00) · [`0071a0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719cc0.md#insn-0071a0b8) · [`00719cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719cc0.md#insn-00719cf8)
- 新版 [`0071a0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a070.md#insn-0071a0b0) · [`0071a468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a070.md#insn-0071a468) · [`0071a0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a070.md#insn-0071a0a8)

~~~diff
- 00719d00 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0071a0b0 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00719d00 bytes 482a00f0
+ 0071a0b0 bytes 482a00f0
- 0071a0b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c90:8"]]
- 0071a0b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0071a468 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c60:8"]]
+ 0071a468 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0071a0b8 bytes 084946f9
+ 0071a468 bytes 083146f9
- 00719cf8 ["INT_ADD", "register:40f0:8", ["const:719cf8:8", "const:4:8"]]
- 00719cf8 ["CALL", null, ["callee:00488180:8"]]
+ 0071a0a8 ["INT_ADD", "register:40f0:8", ["const:71a0a8:8", "const:4:8"]]
+ 0071a0a8 ["CALL", null, ["callee:00488180:8"]]
- 00719cf8 bytes 5ab8f597
+ 0071a0a8 bytes 36b8f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd09160bb5f66de573b2b6fd8071385c"></a>

### [`0071a3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a3e4.md) → [`0071a794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a794.md) FUN_0071a794

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00719cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719cc0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0071a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a070.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0071a7a0",
      "incomplete_value": false,
      "site": "0071a7a4",
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
      "definition_site": "0071a3f0",
      "incomplete_value": false,
      "site": "0071a3f4",
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
      "0071a7a0",
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
      "0071a7a0",
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

- 旧版 [`0071a3f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a3e4.md#insn-0071a3f4) · [`0071a3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a3e4.md#insn-0071a3ec) · [`0071a3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a3e4.md#insn-0071a3f0)
- 新版 [`0071a7a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a794.md#insn-0071a7a4) · [`0071a79c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a794.md#insn-0071a79c) · [`0071a7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a794.md#insn-0071a7a0)

~~~diff
- 0071a3f4 ["INT_ADD", "register:40f0:8", ["const:71a3f4:8", "const:4:8"]]
- 0071a3f4 ["CALL", null, ["callee:0043bad8:8"]]
+ 0071a7a4 ["INT_ADD", "register:40f0:8", ["const:71a7a4:8", "const:4:8"]]
+ 0071a7a4 ["CALL", null, ["callee:0043bad8:8"]]
- 0071a3f4 bytes f184f497
+ 0071a7a4 bytes cd84f497
- 0071a3ec ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0071a79c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0071a3ec bytes e0dcffb0
+ 0071a79c bytes e0dcffd0
- 0071a3f0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0071a3f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0071a3f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0071a3f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0071a7a0 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0071a7a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0071a7a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0071a7a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0071a3f0 bytes 00303e91
+ 0071a7a0 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fceb7e33f9a621b269577cab8f9fd9ec"></a>

### [`0071a3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a3f8.md) → [`0071a7a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a7a8.md) FUN_0071a7a8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00719cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719cc0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0071a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a070.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0071a7b4",
      "incomplete_value": false,
      "site": "0071a7b8",
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
      "definition_site": "0071a404",
      "incomplete_value": false,
      "site": "0071a408",
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
      "0071a7b4",
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
      "0071a7b4",
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

- 旧版 [`0071a408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a3f8.md#insn-0071a408) · [`0071a400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a3f8.md#insn-0071a400) · [`0071a404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a3f8.md#insn-0071a404)
- 新版 [`0071a7b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a7a8.md#insn-0071a7b8) · [`0071a7b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a7a8.md#insn-0071a7b0) · [`0071a7b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a7a8.md#insn-0071a7b4)

~~~diff
- 0071a408 ["INT_ADD", "register:40f0:8", ["const:71a408:8", "const:4:8"]]
- 0071a408 ["CALL", null, ["callee:0043bad8:8"]]
+ 0071a7b8 ["INT_ADD", "register:40f0:8", ["const:71a7b8:8", "const:4:8"]]
+ 0071a7b8 ["CALL", null, ["callee:0043bad8:8"]]
- 0071a408 bytes ec84f497
+ 0071a7b8 bytes c884f497
- 0071a400 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0071a7b0 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0071a400 bytes e0dcffb0
+ 0071a7b0 bytes e0dcffd0
- 0071a404 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0071a404 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0071a404 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0071a404 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0071a7b4 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0071a7b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0071a7b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0071a7b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0071a404 bytes 00303e91
+ 0071a7b4 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ae5b23c8573e1c3f34533caa1b82f65"></a>

### [`0071a40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a40c.md) → [`0071a7bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a7bc.md) _INIT_114

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071a7f8",
      "incomplete_value": true,
      "site": "0071a814",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071a448",
      "incomplete_value": true,
      "site": "0071a464",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
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
      "definition_site": "0071a81c",
      "incomplete_value": true,
      "site": "0071a838",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071a46c",
      "incomplete_value": true,
      "site": "0071a488",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f79:8"
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
      "definition_site": "0071a83c",
      "incomplete_value": true,
      "site": "0071a858",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071a48c",
      "incomplete_value": true,
      "site": "0071a4a8",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
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
      "0071a7f8",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0071a81c",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0071a83c",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0071a7f8",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0071a81c",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0071a83c",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071a56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a40c.md#insn-0071a56c) · [`0071a640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a40c.md#insn-0071a640) · [`0071a434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a40c.md#insn-0071a434)
- 新版 [`0071a91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a7bc.md#insn-0071a91c) · [`0071a9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a7bc.md#insn-0071a9f0) · [`0071a7e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a7bc.md#insn-0071a7e4)

~~~diff
- 0071a56c ["INT_ADD", "register:40f0:8", ["const:71a56c:8", "const:4:8"]]
- 0071a56c ["CALL", null, ["callee:0043bb58:8"]]
+ 0071a91c ["INT_ADD", "register:40f0:8", ["const:71a91c:8", "const:4:8"]]
+ 0071a91c ["CALL", null, ["callee:0043bb58:8"]]
- 0071a56c bytes b384f497
+ 0071a91c bytes 8f84f497
- 0071a640 ["INT_ADD", "register:40f0:8", ["const:71a640:8", "const:4:8"]]
- 0071a640 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0071a9f0 ["INT_ADD", "register:40f0:8", ["const:71a9f0:8", "const:4:8"]]
+ 0071a9f0 ["CALL", null, ["callee:00c58ed0:8"]]
- 0071a640 bytes 30f61494
+ 0071a9f0 bytes 38f91494
- 0071a434 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 0071a7e4 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 0071a434 bytes 732c00b0
+ 0071a7e4 bytes 732c00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a5951283e823ab15adc891a3e43c546"></a>

### [`0071adbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071adbc.md) → [`0071b16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b16c.md) FUN_0071b16c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009d906c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d9/009d906c.md) · 呼出先 23件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)
- 新版 呼出元 1件 [`009da018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009da/009da018.md) · 呼出先 23件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c8c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.43% / 新版 94.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071b1b4",
      "incomplete_value": true,
      "site": "0071b1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071ae04",
      "incomplete_value": true,
      "site": "0071ae0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
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
      "definition_site": "0071b3c4",
      "incomplete_value": true,
      "site": "0071b3dc",
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
                "const:9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071b014",
      "incomplete_value": true,
      "site": "0071b02c",
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071b5d0",
      "incomplete_value": true,
      "site": "0071b5e4",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:931:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071b220",
      "incomplete_value": true,
      "site": "0071b234",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:864:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0071b1bc",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "0071b1d4",
      "READ",
      [
        "storage",
        "002a45f0",
        null,
        "string"
      ]
    ],
    [
      "0071b3c4",
      "READ",
      [
        "storage",
        "002b2050",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0071b1bc",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "0071b1d4",
      "READ",
      [
        "storage",
        "002a46bb",
        null,
        "string"
      ]
    ],
    [
      "0071b3c4",
      "READ",
      [
        "storage",
        "002b209a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071afb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071adbc.md#insn-0071afb4) · [`0071adfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071adbc.md#insn-0071adfc) · [`0071ae00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071adbc.md#insn-0071ae00)
- 新版 [`0071b364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b16c.md#insn-0071b364) · [`0071b1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b16c.md#insn-0071b1ac) · [`0071b1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b16c.md#insn-0071b1b0)

~~~diff
- 0071afb4 ["INT_ADD", "register:40f0:8", ["const:71afb4:8", "const:4:8"]]
- 0071afb4 ["CALL", null, ["callee:00c58f30:8"]]
+ 0071b364 ["INT_ADD", "register:40f0:8", ["const:71b364:8", "const:4:8"]]
+ 0071b364 ["CALL", null, ["callee:00c58f30:8"]]
- 0071afb4 bytes ebf31494
+ 0071b364 bytes f3f61494
- 0071adfc ["INT_ADD", "register:40f0:8", ["const:71adfc:8", "const:4:8"]]
- 0071adfc ["CALL", null, ["callee:00488180:8"]]
+ 0071b1ac ["INT_ADD", "register:40f0:8", ["const:71b1ac:8", "const:4:8"]]
+ 0071b1ac ["CALL", null, ["callee:00488180:8"]]
- 0071adfc bytes 19b4f597
+ 0071b1ac bytes f5b3f597
- 0071ae00 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0071b1b0 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0071ae00 bytes 482a00d0
+ 0071b1b0 bytes 482a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8d311f784614bb86d848249b4333728"></a>

### [`0071b588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071b588.md) → [`0071b938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b938.md) FUN_0071b938

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0071adbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071adbc.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0071b16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b16c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0071b944",
      "incomplete_value": false,
      "site": "0071b948",
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
      "definition_site": "0071b594",
      "incomplete_value": false,
      "site": "0071b598",
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
      "0071b944",
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
      "0071b944",
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

- 旧版 [`0071b598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071b588.md#insn-0071b598) · [`0071b590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071b588.md#insn-0071b590) · [`0071b594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071b588.md#insn-0071b594)
- 新版 [`0071b948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b938.md#insn-0071b948) · [`0071b940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b938.md#insn-0071b940) · [`0071b944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b938.md#insn-0071b944)

~~~diff
- 0071b598 ["INT_ADD", "register:40f0:8", ["const:71b598:8", "const:4:8"]]
- 0071b598 ["CALL", null, ["callee:0043bad8:8"]]
+ 0071b948 ["INT_ADD", "register:40f0:8", ["const:71b948:8", "const:4:8"]]
+ 0071b948 ["CALL", null, ["callee:0043bad8:8"]]
- 0071b598 bytes 8880f497
+ 0071b948 bytes 6480f497
- 0071b590 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0071b940 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0071b590 bytes e0dcff90
+ 0071b940 bytes e0dcffb0
- 0071b594 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0071b594 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0071b594 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0071b594 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0071b944 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0071b944 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0071b944 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0071b944 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0071b594 bytes 00303e91
+ 0071b944 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-241e5e647d62bf67101088bf76ad7b51"></a>

### [`0071b59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071b59c.md) → [`0071b94c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b94c.md) _INIT_115

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071b988",
      "incomplete_value": true,
      "site": "0071b9a4",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071b5d8",
      "incomplete_value": true,
      "site": "0071b5f4",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
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
      "definition_site": "0071b9cc",
      "incomplete_value": true,
      "site": "0071b9e8",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071b61c",
      "incomplete_value": true,
      "site": "0071b638",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0071ba28",
      "incomplete_value": true,
      "site": "0071ba44",
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
                "const:2a0000:8"
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
      "definition_site": "0071b678",
      "incomplete_value": true,
      "site": "0071b694",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0071b988",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0071b9ac",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0071b9cc",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0071b988",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0071b9ac",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0071b9cc",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071b7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071b59c.md#insn-0071b7d0) · [`0071b5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071b59c.md#insn-0071b5c4) · [`0071b5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071b59c.md#insn-0071b5c8)
- 新版 [`0071bb80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b94c.md#insn-0071bb80) · [`0071b974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b94c.md#insn-0071b974) · [`0071b978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b94c.md#insn-0071b978)

~~~diff
- 0071b7d0 ["INT_ADD", "register:40f0:8", ["const:71b7d0:8", "const:4:8"]]
- 0071b7d0 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0071bb80 ["INT_ADD", "register:40f0:8", ["const:71bb80:8", "const:4:8"]]
+ 0071bb80 ["CALL", null, ["callee:00c58ed0:8"]]
- 0071b7d0 bytes ccf11494
+ 0071bb80 bytes d4f41494
- 0071b5c4 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 0071b974 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 0071b5c4 bytes 732c0090
+ 0071b974 bytes 732c00b0
- 0071b5c8 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0071b5c8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0071b5c8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0071b5c8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0071b978 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 0071b978 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0071b978 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0071b978 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0071b5c8 bytes 73e23491
+ 0071b978 bytes 73e23391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85d7130286c2a8dcc9b16707ed11324d"></a>

### [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md) → [`0071c868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c868.md) FUN_0071c868

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 45件 [`005c8800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8800.md) [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`00611ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00611/00611ea0.md) [`00616990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616990.md) · 呼出先 3件 [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md) [`0071d254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d254.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 45件 [`005c8bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c8bb0.md) [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`00605644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00605/00605644.md) [`00612250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00612/00612250.md) [`00616d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00616/00616d40.md) · 呼出先 3件 [`0071c2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c2e0.md) [`0071d604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d604.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 95.16% / 新版 95.16%

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
      "site": "0071c8ac",
      "value": [
        "leaf",
        "ram:71c2e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0071c4fc",
      "value": [
        "leaf",
        "ram:71bf30:8"
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
      "site": "0071c928",
      "value": [
        "leaf",
        "ram:71c2e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0071c578",
      "value": [
        "leaf",
        "ram:71bf30:8"
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
      "0071c89c",
      "DATA",
      [
        "storage",
        "003965ac",
        "fde_003965ac",
        "dword"
      ]
    ],
    [
      "0071c8ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "0071c8c4",
      "DATA",
      [
        "storage",
        "003965ac",
        "fde_003965ac",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "0071c89c",
      "DATA",
      [
        "storage",
        "003965ac",
        null,
        "dword"
      ]
    ],
    [
      "0071c8ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c2e0"
      ]
    ],
    [
      "0071c8c4",
      "DATA",
      [
        "storage",
        "003965ac",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071c4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md#insn-0071c4fc) · [`0071c578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md#insn-0071c578) · [`0071c4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md#insn-0071c4d8)
- 新版 [`0071c8ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c868.md#insn-0071c8ac) · [`0071c928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c868.md#insn-0071c928) · [`0071c888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c868.md#insn-0071c888)

~~~diff
- 0071c4fc ["INT_ADD", "register:40f0:8", ["const:71c4fc:8", "const:4:8"]]
- 0071c4fc ["CALL", null, ["ram:71bf30:8"]]
+ 0071c8ac ["INT_ADD", "register:40f0:8", ["const:71c8ac:8", "const:4:8"]]
+ 0071c8ac ["CALL", null, ["ram:71c2e0:8"]]
- 0071c4fc bytes 8dfeff97
+ 0071c8ac bytes 8dfeff97
- 0071c578 ["INT_ADD", "register:40f0:8", ["const:71c578:8", "const:4:8"]]
- 0071c578 ["CALL", null, ["ram:71bf30:8"]]
+ 0071c928 ["INT_ADD", "register:40f0:8", ["const:71c928:8", "const:4:8"]]
+ 0071c928 ["CALL", null, ["ram:71c2e0:8"]]
- 0071c578 bytes 6efeff97
+ 0071c928 bytes 6efeff97
- 0071c4d8 ["INT_ADD", "register:40f0:8", ["const:71c4d8:8", "const:4:8"]]
- 0071c4d8 ["CALL", null, ["callee:008524fc:8"]]
+ 0071c888 ["INT_ADD", "register:40f0:8", ["const:71c888:8", "const:4:8"]]
+ 0071c888 ["CALL", null, ["callee:008524fc:8"]]
- 0071c4d8 bytes 1ed40494
+ 0071c888 bytes 1dd70494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c387c1cb0ad0d766c68649075cd28428"></a>

### [`0071f128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f128.md) → [`0071f4d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f4d8.md) _INIT_116

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071f558",
      "incomplete_value": true,
      "site": "0071f574",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f1a8",
      "incomplete_value": true,
      "site": "0071f1c4",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0071f5b4",
      "incomplete_value": true,
      "site": "0071f5d0",
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
                "const:2a0000:8"
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
      "definition_site": "0071f204",
      "incomplete_value": true,
      "site": "0071f220",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0071f6f8",
      "incomplete_value": false,
      "site": "0071f70c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43b000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f348",
      "incomplete_value": false,
      "site": "0071f35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "0071f514",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0071f538",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0071f558",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0071f514",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0071f538",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0071f558",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071f35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f128.md#insn-0071f35c) · [`0071f150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f128.md#insn-0071f150) · [`0071f154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f128.md#insn-0071f154)
- 新版 [`0071f70c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f4d8.md#insn-0071f70c) · [`0071f500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f4d8.md#insn-0071f500) · [`0071f504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f4d8.md#insn-0071f504)

~~~diff
- 0071f35c ["INT_ADD", "register:40f0:8", ["const:71f35c:8", "const:4:8"]]
- 0071f35c ["CALL", null, ["callee:00c58ed0:8"]]
+ 0071f70c ["INT_ADD", "register:40f0:8", ["const:71f70c:8", "const:4:8"]]
+ 0071f70c ["CALL", null, ["callee:00c58ed0:8"]]
- 0071f35c bytes e9e21494
+ 0071f70c bytes f1e51494
- 0071f150 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 0071f500 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 0071f150 bytes 532c0090
+ 0071f500 bytes 532c00b0
- 0071f154 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 0071f154 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0071f154 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0071f154 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0071f504 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 0071f504 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0071f504 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0071f504 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0071f154 bytes 73423591
+ 0071f504 bytes 73423491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d3b41f8d9c9a9fb8001c39a5daaa7bf"></a>

### [`0071f638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f638.md) → [`0071f9e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f9e8.md) _INIT_117

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071fa68",
      "incomplete_value": true,
      "site": "0071fa84",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f6b8",
      "incomplete_value": true,
      "site": "0071f6d4",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0071fa88",
      "incomplete_value": true,
      "site": "0071faa0",
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f6d8",
      "incomplete_value": true,
      "site": "0071f6f0",
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
                "const:f15:8"
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
      "definition_site": "0071faa4",
      "incomplete_value": true,
      "site": "0071fac0",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:643:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f6f4",
      "incomplete_value": true,
      "site": "0071f710",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:576:8"
              ]
            ]
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
      "0071fa24",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0071fa48",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0071fa68",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0071fa24",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0071fa48",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0071fa68",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071f86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f638.md#insn-0071f86c) · [`0071f660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f638.md#insn-0071f660) · [`0071f664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f638.md#insn-0071f664)
- 新版 [`0071fc1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f9e8.md#insn-0071fc1c) · [`0071fa10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f9e8.md#insn-0071fa10) · [`0071fa14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f9e8.md#insn-0071fa14)

~~~diff
- 0071f86c ["INT_ADD", "register:40f0:8", ["const:71f86c:8", "const:4:8"]]
- 0071f86c ["CALL", null, ["callee:00c58ed0:8"]]
+ 0071fc1c ["INT_ADD", "register:40f0:8", ["const:71fc1c:8", "const:4:8"]]
+ 0071fc1c ["CALL", null, ["callee:00c58ed0:8"]]
- 0071f86c bytes a5e11494
+ 0071fc1c bytes ade41494
- 0071f660 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 0071fa10 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 0071f660 bytes 532c0090
+ 0071fa10 bytes 532c00b0
- 0071f664 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 0071f664 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0071f664 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0071f664 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0071fa14 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 0071fa14 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0071fa14 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0071fa14 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0071f664 bytes 73a23591
+ 0071fa14 bytes 73a23491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc18bcb48c2919e309f6a9657dc1a1dc"></a>

### [`0071f9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f9c8.md) → [`0071fd78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071fd78.md) _INIT_118

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.88% / 新版 85.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071fdd8",
      "incomplete_value": true,
      "site": "0071fdf4",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071fa28",
      "incomplete_value": true,
      "site": "0071fa44",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f79:8"
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
      "definition_site": "0071fdf8",
      "incomplete_value": true,
      "site": "0071fe14",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071fa48",
      "incomplete_value": true,
      "site": "0071fa64",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0071fe18",
      "incomplete_value": true,
      "site": "0071fe30",
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071fa68",
      "incomplete_value": true,
      "site": "0071fa80",
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
                "const:f15:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0071fdb4",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0071fdd8",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0071fdf8",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0071fdb4",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0071fdd8",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0071fdf8",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071fbfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f9c8.md#insn-0071fbfc) · [`0071f9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f9c8.md#insn-0071f9f0) · [`0071f9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f9c8.md#insn-0071f9f4)
- 新版 [`0071ffac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071fd78.md#insn-0071ffac) · [`0071fda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071fd78.md#insn-0071fda0) · [`0071fda4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071fd78.md#insn-0071fda4)

~~~diff
- 0071fbfc ["INT_ADD", "register:40f0:8", ["const:71fbfc:8", "const:4:8"]]
- 0071fbfc ["CALL", null, ["callee:00c58ed0:8"]]
+ 0071ffac ["INT_ADD", "register:40f0:8", ["const:71ffac:8", "const:4:8"]]
+ 0071ffac ["CALL", null, ["callee:00c58ed0:8"]]
- 0071fbfc bytes c1e01494
+ 0071ffac bytes c9e31494
- 0071f9f0 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 0071fda0 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 0071f9f0 bytes 532c0090
+ 0071fda0 bytes 532c00b0
- 0071f9f4 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 0071f9f4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0071f9f4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0071f9f4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0071fda4 ["COPY", "tmp:0:8", ["const:d40:8"]]
+ 0071fda4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0071fda4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0071fda4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0071f9f4 bytes 73023691
+ 0071fda4 bytes 73023591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c1b108a2a9ce02cd427ec13ae92ebc2"></a>

### [`0071fd58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071fd58.md) → [`00720108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00720/00720108.md) _INIT_119

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00720144",
      "incomplete_value": true,
      "site": "00720160",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071fd94",
      "incomplete_value": true,
      "site": "0071fdb0",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
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
      "definition_site": "007201a8",
      "incomplete_value": true,
      "site": "007201c0",
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071fdf8",
      "incomplete_value": true,
      "site": "0071fe10",
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
                "const:f15:8"
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
      "definition_site": "007201c4",
      "incomplete_value": true,
      "site": "007201e0",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:643:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071fe14",
      "incomplete_value": true,
      "site": "0071fe30",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:576:8"
              ]
            ]
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
      "00720144",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00720168",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00720188",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00720144",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00720168",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "00720188",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071ff8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071fd58.md#insn-0071ff8c) · [`0071fd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071fd58.md#insn-0071fd80) · [`0071fd84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071fd58.md#insn-0071fd84)
- 新版 [`0072033c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00720/00720108.md#insn-0072033c) · [`00720130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00720/00720108.md#insn-00720130) · [`00720134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00720/00720108.md#insn-00720134)

~~~diff
- 0071ff8c ["INT_ADD", "register:40f0:8", ["const:71ff8c:8", "const:4:8"]]
- 0071ff8c ["CALL", null, ["callee:00c58ed0:8"]]
+ 0072033c ["INT_ADD", "register:40f0:8", ["const:72033c:8", "const:4:8"]]
+ 0072033c ["CALL", null, ["callee:00c58ed0:8"]]
- 0071ff8c bytes dddf1494
+ 0072033c bytes e5e21494
- 0071fd80 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 00720130 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 0071fd80 bytes 532c0090
+ 00720130 bytes 532c0090
- 0071fd84 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 0071fd84 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0071fd84 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0071fd84 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00720134 ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 00720134 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00720134 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00720134 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0071fd84 bytes 73623691
+ 00720134 bytes 73623591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-024eb96fd5d0011a51a9a5cfc248654b"></a>

### [`007200e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00720/007200e8.md) → [`00720498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00720/00720498.md) FUN_00720498

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 49件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0046d9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d9b4.md) [`0046e578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e578.md)
- 新版 呼出元 1件 [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) · 呼出先 49件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046cde4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cde4.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0046dcd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046dcd4.md) [`0046e898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046e898.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.10% / 新版 95.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 40件, `call_target` 33件, `store_destination` 9件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00722d70",
      "incomplete_value": false,
      "site": "00722d70",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:fc0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007229c0",
      "incomplete_value": false,
      "site": "007229c0",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 285,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00722d74",
      "incomplete_value": false,
      "site": "00722d74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007229c4",
      "incomplete_value": false,
      "site": "007229c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 286,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00722d70",
      "incomplete_value": false,
      "site": "00722d74",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:fc0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007229c0",
      "incomplete_value": false,
      "site": "007229c4",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 286,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007205a0",
      "READ",
      [
        "storage",
        "002c43a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00720698",
      "READ",
      [
        "storage",
        "00c9ad70",
        null,
        "pointer"
      ]
    ],
    [
      "007206b0",
      "PARAM",
      [
        "storage",
        "00ca50d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "007205a0",
      "READ",
      [
        "storage",
        "002c43f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00720698",
      "READ",
      [
        "storage",
        "00c9bd40",
        null,
        "pointer"
      ]
    ],
    [
      "007206b0",
      "PARAM",
      [
        "storage",
        "00ca6098",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00720304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00720/007200e8.md#insn-00720304) · [`00720460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00720/007200e8.md#insn-00720460) · [`007204b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00720/007200e8.md#insn-007204b0)
- 新版 [`007206b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00720/00720498.md#insn-007206b4) · [`00720810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00720/00720498.md#insn-00720810) · [`00720860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00720/00720498.md#insn-00720860)

~~~diff
- 00720304 ["INT_ADD", "register:40f0:8", ["const:720304:8", "const:4:8"]]
- 00720304 ["CALL", null, ["callee:0047ec3c:8"]]
+ 007206b4 ["INT_ADD", "register:40f0:8", ["const:7206b4:8", "const:4:8"]]
+ 007206b4 ["CALL", null, ["callee:0047ec3c:8"]]
- 00720304 bytes 8679f597
+ 007206b4 bytes 6279f597
- 00720460 ["INT_ADD", "register:40f0:8", ["const:720460:8", "const:4:8"]]
- 00720460 ["CALL", null, ["callee:0047ec3c:8"]]
+ 00720810 ["INT_ADD", "register:40f0:8", ["const:720810:8", "const:4:8"]]
+ 00720810 ["CALL", null, ["callee:0047ec3c:8"]]
- 00720460 bytes 2f79f597
+ 00720810 bytes 0b79f597
- 007204b0 ["INT_ADD", "register:40f0:8", ["const:7204b0:8", "const:4:8"]]
- 007204b0 ["CALL", null, ["callee:00c54d90:8"]]
+ 00720860 ["INT_ADD", "register:40f0:8", ["const:720860:8", "const:4:8"]]
+ 00720860 ["CALL", null, ["callee:00c54d90:8"]]
- 007204b0 bytes 3cce1494
+ 00720860 bytes 4cd11494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e17ff3f30348fe3fa61e9cb0445f9592"></a>

### [`007244b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00724/007244b8.md) → [`00724868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00724/00724868.md) _INIT_120

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007248a4",
      "incomplete_value": true,
      "site": "007248c0",
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
                "live",
                "register:4048:8"
              ],
              [
                "leaf",
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007244f4",
      "incomplete_value": true,
      "site": "00724510",
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
                "live",
                "register:4048:8"
              ],
              [
                "leaf",
                "const:f66:8"
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
      "definition_site": "007248e8",
      "incomplete_value": true,
      "site": "00724904",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00724538",
      "incomplete_value": true,
      "site": "00724554",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00724924",
      "incomplete_value": true,
      "site": "00724940",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:643:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00724574",
      "incomplete_value": true,
      "site": "00724590",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:576:8"
              ]
            ]
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
      "007248a4",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "007248c8",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "007248e8",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007248a4",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "007248c8",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "007248e8",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007244e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00724/007244b8.md#insn-007244e0) · [`007244e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00724/007244b8.md#insn-007244e4) · [`007244ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00724/007244b8.md#insn-007244ec)
- 新版 [`00724890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00724/00724868.md#insn-00724890) · [`00724894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00724/00724868.md#insn-00724894) · [`0072489c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00724/00724868.md#insn-0072489c)

~~~diff
- 007244e0 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 00724890 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 007244e0 bytes 132c00f0
+ 00724890 bytes 332c0090
- 007244e4 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 007244e4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007244e4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007244e4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00724894 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00724894 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00724894 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00724894 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007244e4 bytes 73c23691
+ 00724894 bytes 73c23591
- 007244ec ["COPY", "register:4048:8", ["const:2b7000:8"]]
+ 0072489c ["COPY", "register:4048:8", ["const:2b8000:8"]]
- 007244ec bytes 89dcfff0
+ 0072489c bytes a9dcff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64438cf16e1211a7c37316e9da4de54b"></a>

### [`00724848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00724/00724848.md) → [`00724bf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00724/00724bf8.md) FUN_00724bf8

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 21件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)
- 新版 呼出元 1件 [`00b29fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b29/00b29fe4.md) · 呼出先 21件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.85% / 新版 94.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00724c3c",
      "incomplete_value": false,
      "site": "00724c48",
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
      "definition_site": "0072488c",
      "incomplete_value": false,
      "site": "00724898",
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
      "definition_site": "00724c74",
      "incomplete_value": true,
      "site": "00724c84",
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
                "const:29f000:8"
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
      "definition_site": "007248c4",
      "incomplete_value": true,
      "site": "007248d4",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:34a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00724c78",
      "incomplete_value": true,
      "site": "00724c88",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007248c8",
      "incomplete_value": true,
      "site": "007248d8",
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
                "const:9:8"
              ]
            ]
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
      "00724c48",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "00724c74",
      "READ",
      [
        "storage",
        "0029f34a",
        null,
        "string"
      ]
    ],
    [
      "00724c78",
      "READ",
      [
        "storage",
        "0029f353",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00724c48",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "00724c74",
      "READ",
      [
        "storage",
        "0029f38a",
        null,
        "string"
      ]
    ],
    [
      "00724c78",
      "READ",
      [
        "storage",
        "0029f393",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00724c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00724/00724848.md#insn-00724c48) · [`00724c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00724/00724848.md#insn-00724c8c) · [`00724880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00724/00724848.md#insn-00724880)
- 新版 [`00724ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00724/00724bf8.md#insn-00724ff8) · [`0072503c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00724/00724bf8.md#insn-0072503c) · [`00724c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00724/00724bf8.md#insn-00724c30)

~~~diff
- 00724c48 ["INT_ADD", "register:40f0:8", ["const:724c48:8", "const:4:8"]]
- 00724c48 ["CALL", null, ["callee:00c58f50:8"]]
+ 00724ff8 ["INT_ADD", "register:40f0:8", ["const:724ff8:8", "const:4:8"]]
+ 00724ff8 ["CALL", null, ["callee:00c58f50:8"]]
- 00724c48 bytes cecc1494
+ 00724ff8 bytes d6cf1494
- 00724c8c ["INT_ADD", "register:40f0:8", ["const:724c8c:8", "const:4:8"]]
- 00724c8c ["CALL", null, ["callee:004413ec:8"]]
+ 0072503c ["INT_ADD", "register:40f0:8", ["const:72503c:8", "const:4:8"]]
+ 0072503c ["CALL", null, ["callee:004413ec:8"]]
- 00724c8c bytes 1071f497
+ 0072503c bytes ec70f497
- 00724880 ["INT_ADD", "register:40f0:8", ["const:724880:8", "const:4:8"]]
- 00724880 ["CALL", null, ["callee:00488180:8"]]
+ 00724c30 ["INT_ADD", "register:40f0:8", ["const:724c30:8", "const:4:8"]]
+ 00724c30 ["CALL", null, ["callee:00488180:8"]]
- 00724880 bytes 788df597
+ 00724c30 bytes 548df597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-487d6d3fc2a3ad19917ce321db864007"></a>

### [`007254bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00725/007254bc.md) → [`0072586c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00725/0072586c.md) FUN_0072586c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0075d7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d7b4.md) · 呼出先 19件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md)
- 新版 呼出元 1件 [`0075db64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075db64.md) · 呼出先 19件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`0071c2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c2e0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.82% / 新版 99.82%

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
      "site": "00725c10",
      "value": [
        "leaf",
        "ram:71c2e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00725860",
      "value": [
        "leaf",
        "ram:71bf30:8"
      ]
    },
    "ordinal": 19,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00725c10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ]
  ],
  "added": [
    [
      "00725c10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c2e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00725860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00725/007254bc.md#insn-00725860) · [`00725c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00725/007254bc.md#insn-00725c10) · [`00725514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00725/007254bc.md#insn-00725514)
- 新版 [`00725c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00725/0072586c.md#insn-00725c10) · [`00725fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00725/0072586c.md#insn-00725fc0) · [`007258c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00725/0072586c.md#insn-007258c4)

~~~diff
- 00725860 ["INT_ADD", "register:40f0:8", ["const:725860:8", "const:4:8"]]
- 00725860 ["CALL", null, ["ram:71bf30:8"]]
+ 00725c10 ["INT_ADD", "register:40f0:8", ["const:725c10:8", "const:4:8"]]
+ 00725c10 ["CALL", null, ["ram:71c2e0:8"]]
- 00725860 bytes b4d9ff97
+ 00725c10 bytes b4d9ff97
- 00725c10 ["INT_ADD", "register:40f0:8", ["const:725c10:8", "const:4:8"]]
- 00725c10 ["CALL", null, ["callee:0083a9c8:8"]]
+ 00725fc0 ["INT_ADD", "register:40f0:8", ["const:725fc0:8", "const:4:8"]]
+ 00725fc0 ["CALL", null, ["callee:0083a9c8:8"]]
- 00725c10 bytes 834f0494
+ 00725fc0 bytes 82520494
- 00725514 ["INT_ADD", "register:40f0:8", ["const:725514:8", "const:4:8"]]
- 00725514 ["CALL", null, ["callee:005c1b8c:8"]]
+ 007258c4 ["INT_ADD", "register:40f0:8", ["const:7258c4:8", "const:4:8"]]
+ 007258c4 ["CALL", null, ["callee:005c1b8c:8"]]
- 00725514 bytes b270fa97
+ 007258c4 bytes b270fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fdddc52180e76e55a1c1db4f5e6bd82"></a>

### [`007260e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007260e4.md) → [`00726494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00726/00726494.md) FUN_00726494

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00725f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00725/00725f0c.md) [`0077c1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c1e8.md) [`00a38eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a38eac.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`007262bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00726/007262bc.md) [`0077c5c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077c5c4.md) [`00a39ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a39/00a39ea0.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "007264a0",
      "incomplete_value": true,
      "site": "007264a4",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007260f0",
      "incomplete_value": true,
      "site": "007260f4",
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
      "007264a0",
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
      "007264a0",
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

- 旧版 [`007260f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007260e4.md#insn-007260f4) · [`007260ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007260e4.md#insn-007260ec) · [`007260f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007260e4.md#insn-007260f0)
- 新版 [`007264a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00726/00726494.md#insn-007264a4) · [`0072649c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00726/00726494.md#insn-0072649c) · [`007264a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00726/00726494.md#insn-007264a0)

~~~diff
- 007260f4 ["INT_ADD", "register:40f0:8", ["const:7260f4:8", "const:4:8"]]
- 007260f4 ["CALL", null, ["callee:0043bad8:8"]]
+ 007264a4 ["INT_ADD", "register:40f0:8", ["const:7264a4:8", "const:4:8"]]
+ 007264a4 ["CALL", null, ["callee:0043bad8:8"]]
- 007260f4 bytes b155f497
+ 007264a4 bytes 8d55f497
- 007260ec ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0072649c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 007260ec bytes 80dcffb0
+ 0072649c bytes 80dcffd0
- 007260f0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 007260f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007260f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007260f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007264a0 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 007264a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007264a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007264a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007260f0 bytes 00303e91
+ 007264a0 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

