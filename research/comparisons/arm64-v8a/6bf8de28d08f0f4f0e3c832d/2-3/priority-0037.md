# v16.0.2 → v16.0.3 · 最優先の変更候補 (37)

[一覧の目次](README.md)

<a id="compare-f01a15ea0cd6c08ad70041b4a1ee757a"></a>

### [`00748064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748064.md) → [`00748414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748414.md) FUN_00748414

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
      "definition_site": "0074842c",
      "incomplete_value": false,
      "site": "00748438",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074807c",
      "incomplete_value": false,
      "site": "00748088",
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
            "const:f10:8"
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
      "00748438",
      "DATA",
      [
        "storage",
        "00c77f10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00748438",
      "DATA",
      [
        "storage",
        "00c78ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00748078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748064.md#insn-00748078) · [`0074807c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748064.md#insn-0074807c) · [`007480ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748064.md#insn-007480ac)
- 新版 [`00748428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748414.md#insn-00748428) · [`0074842c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748414.md#insn-0074842c) · [`0074845c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748414.md#insn-0074845c)

~~~diff
- 00748078 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 00748428 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 00748078 bytes 682900f0
+ 00748428 bytes 88290090
- 0074807c ["COPY", "tmp:0:8", ["const:f10:8"]]
- 0074807c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0074807c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0074807c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0074842c ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 0074842c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0074842c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0074842c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0074807c bytes 08413c91
+ 0074842c bytes 08813b91
- 007480ac ["COPY", "register:0:8", ["register:4040:8"]]
- 007480ac ["INT_ADD", "register:40f0:8", ["const:7480ac:8", "const:4:8"]]
- 007480ac ["CALLIND", null, ["register:0:8"]]
+ 0074845c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0074845c ["INT_ADD", "register:40f0:8", ["const:74845c:8", "const:4:8"]]
+ 0074845c ["CALLIND", null, ["register:0:8"]]
- 007480ac bytes 00013fd6
+ 0074845c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d105bba6829233a1ffec202b4a34dae2"></a>

### [`007480c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007480c0.md) → [`00748470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748470.md) FUN_00748470

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00748498",
      "incomplete_value": false,
      "site": "0074849c",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007480e8",
      "incomplete_value": false,
      "site": "007480ec",
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
            "const:f10:8"
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
      "0074849c",
      "DATA",
      [
        "storage",
        "00c77f10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0074849c",
      "DATA",
      [
        "storage",
        "00c78ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007480d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007480c0.md#insn-007480d4) · [`007480e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007480c0.md#insn-007480e4) · [`007480e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007480c0.md#insn-007480e8)
- 新版 [`00748484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748470.md#insn-00748484) · [`00748494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748470.md#insn-00748494) · [`00748498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748470.md#insn-00748498)

~~~diff
- 007480d4 ["INT_ADD", "register:40f0:8", ["const:7480d4:8", "const:4:8"]]
- 007480d4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00748484 ["INT_ADD", "register:40f0:8", ["const:748484:8", "const:4:8"]]
+ 00748484 ["CALL", null, ["callee:00c58f30:8"]]
- 007480d4 bytes a33f1494
+ 00748484 bytes ab421494
- 007480e4 ["COPY", "register:4048:8", ["const:c77000:8"]]
+ 00748494 ["COPY", "register:4048:8", ["const:c78000:8"]]
- 007480e4 bytes 692900f0
+ 00748494 bytes 89290090
- 007480e8 ["COPY", "tmp:0:8", ["const:f10:8"]]
- 007480e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007480e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007480e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00748498 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00748498 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00748498 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00748498 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007480e8 bytes 29413c91
+ 00748498 bytes 29813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0315216021dcc302ef462a0c7906aac7"></a>

### [`00748158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748158.md) → [`00748508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748508.md) FUN_00748508

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00748528",
      "incomplete_value": false,
      "site": "0074852c",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00748178",
      "incomplete_value": false,
      "site": "0074817c",
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
            "const:f10:8"
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
      "0074852c",
      "DATA",
      [
        "storage",
        "00c77f10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0074852c",
      "DATA",
      [
        "storage",
        "00c78ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00748174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748158.md#insn-00748174) · [`00748178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748158.md#insn-00748178) · [`0074819c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748158.md#insn-0074819c)
- 新版 [`00748524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748508.md#insn-00748524) · [`00748528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748508.md#insn-00748528) · [`0074854c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748508.md#insn-0074854c)

~~~diff
- 00748174 ["COPY", "register:4048:8", ["const:c77000:8"]]
+ 00748524 ["COPY", "register:4048:8", ["const:c78000:8"]]
- 00748174 bytes 692900f0
+ 00748524 bytes 89290090
- 00748178 ["COPY", "tmp:0:8", ["const:f10:8"]]
- 00748178 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00748178 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00748178 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00748528 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00748528 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00748528 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00748528 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00748178 bytes 29413c91
+ 00748528 bytes 29813b91
- 0074819c ["COPY", "register:0:8", ["register:4040:8"]]
- 0074819c ["INT_ADD", "register:40f0:8", ["const:74819c:8", "const:4:8"]]
- 0074819c ["CALLIND", null, ["register:0:8"]]
+ 0074854c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0074854c ["INT_ADD", "register:40f0:8", ["const:74854c:8", "const:4:8"]]
+ 0074854c ["CALLIND", null, ["register:0:8"]]
- 0074819c bytes 00013fd6
+ 0074854c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6fe81ea9524b20e0100b89309a0ebf6"></a>

### [`00748264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748264.md) → [`00748614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748614.md) FUN_00748614

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`005aa1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1b0.md) [`0071d18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d18c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`005aa560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005aa/005aa560.md) [`0071d53c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d53c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.33% / 新版 99.33%

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
      "site": "00748704",
      "value": [
        "leaf",
        "ram:71d53c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00748354",
      "value": [
        "leaf",
        "ram:71d18c:8"
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
      "00748704",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d18c"
      ]
    ]
  ],
  "added": [
    [
      "00748704",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d53c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00748354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748264.md#insn-00748354) · [`00748330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748264.md#insn-00748330) · [`00748340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748264.md#insn-00748340)
- 新版 [`00748704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748614.md#insn-00748704) · [`007486e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748614.md#insn-007486e0) · [`007486f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748614.md#insn-007486f0)

~~~diff
- 00748354 ["INT_ADD", "register:40f0:8", ["const:748354:8", "const:4:8"]]
- 00748354 ["CALL", null, ["ram:71d18c:8"]]
+ 00748704 ["INT_ADD", "register:40f0:8", ["const:748704:8", "const:4:8"]]
+ 00748704 ["CALL", null, ["ram:71d53c:8"]]
- 00748354 bytes 8e53ff97
+ 00748704 bytes 8e53ff97
- 00748330 ["INT_ADD", "register:40f0:8", ["const:748330:8", "const:4:8"]]
- 00748330 ["CALL", null, ["callee:00c58f30:8"]]
+ 007486e0 ["INT_ADD", "register:40f0:8", ["const:7486e0:8", "const:4:8"]]
+ 007486e0 ["CALL", null, ["callee:00c58f30:8"]]
- 00748330 bytes 0c3f1494
+ 007486e0 bytes 14421494
- 00748340 ["INT_ADD", "register:40f0:8", ["const:748340:8", "const:4:8"]]
- 00748340 ["CALL", null, ["callee:00c590a0:8"]]
+ 007486f0 ["INT_ADD", "register:40f0:8", ["const:7486f0:8", "const:4:8"]]
+ 007486f0 ["CALL", null, ["callee:00c590a0:8"]]
- 00748340 bytes 643f1494
+ 007486f0 bytes 6c421494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-273a9494296d5a2334c34084b9254549"></a>

### [`007484e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007484e8.md) → [`00748898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748898.md) FUN_00748898

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
      "definition_site": "007488a4",
      "incomplete_value": false,
      "site": "007488b0",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007484f4",
      "incomplete_value": false,
      "site": "00748500",
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
            "const:f90:8"
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
      "007488b0",
      "DATA",
      [
        "storage",
        "00c77f90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007488b0",
      "DATA",
      [
        "storage",
        "00c78f60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007484f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007484e8.md#insn-007484f0) · [`007484f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007484e8.md#insn-007484f4)
- 新版 [`007488a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748898.md#insn-007488a0) · [`007488a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748898.md#insn-007488a4)

~~~diff
- 007484f0 ["COPY", "register:4050:8", ["const:c77000:8"]]
+ 007488a0 ["COPY", "register:4050:8", ["const:c78000:8"]]
- 007484f0 bytes 6a2900f0
+ 007488a0 bytes 8a290090
- 007484f4 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 007484f4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007484f4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007484f4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007488a4 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 007488a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007488a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007488a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007484f4 bytes 4a413e91
+ 007488a4 bytes 4a813d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d88da5002197f97a254cf4bf5cd5e9b3"></a>

### [`0074852c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/0074852c.md) → [`007488dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/007488dc.md) FUN_007488dc

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
      "definition_site": "007488f4",
      "incomplete_value": false,
      "site": "00748900",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00748544",
      "incomplete_value": false,
      "site": "00748550",
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
            "const:f90:8"
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
      "00748900",
      "DATA",
      [
        "storage",
        "00c77f90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00748900",
      "DATA",
      [
        "storage",
        "00c78f60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00748540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/0074852c.md#insn-00748540) · [`00748544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/0074852c.md#insn-00748544) · [`00748574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/0074852c.md#insn-00748574)
- 新版 [`007488f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/007488dc.md#insn-007488f0) · [`007488f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/007488dc.md#insn-007488f4) · [`00748924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/007488dc.md#insn-00748924)

~~~diff
- 00748540 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 007488f0 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 00748540 bytes 682900f0
+ 007488f0 bytes 88290090
- 00748544 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 00748544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00748544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00748544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007488f4 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 007488f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007488f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007488f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00748544 bytes 08413e91
+ 007488f4 bytes 08813d91
- 00748574 ["COPY", "register:0:8", ["register:4040:8"]]
- 00748574 ["INT_ADD", "register:40f0:8", ["const:748574:8", "const:4:8"]]
- 00748574 ["CALLIND", null, ["register:0:8"]]
+ 00748924 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00748924 ["INT_ADD", "register:40f0:8", ["const:748924:8", "const:4:8"]]
+ 00748924 ["CALLIND", null, ["register:0:8"]]
- 00748574 bytes 00013fd6
+ 00748924 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76fa1e2c7a9433657bffb946cac3bd4a"></a>

### [`00748588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748588.md) → [`00748938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748938.md) FUN_00748938

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00748960",
      "incomplete_value": false,
      "site": "00748964",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007485b0",
      "incomplete_value": false,
      "site": "007485b4",
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
            "const:f90:8"
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
      "00748964",
      "DATA",
      [
        "storage",
        "00c77f90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00748964",
      "DATA",
      [
        "storage",
        "00c78f60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0074859c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748588.md#insn-0074859c) · [`007485ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748588.md#insn-007485ac) · [`007485b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748588.md#insn-007485b0)
- 新版 [`0074894c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748938.md#insn-0074894c) · [`0074895c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748938.md#insn-0074895c) · [`00748960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748938.md#insn-00748960)

~~~diff
- 0074859c ["INT_ADD", "register:40f0:8", ["const:74859c:8", "const:4:8"]]
- 0074859c ["CALL", null, ["callee:00c58f30:8"]]
+ 0074894c ["INT_ADD", "register:40f0:8", ["const:74894c:8", "const:4:8"]]
+ 0074894c ["CALL", null, ["callee:00c58f30:8"]]
- 0074859c bytes 713e1494
+ 0074894c bytes 79411494
- 007485ac ["COPY", "register:4048:8", ["const:c77000:8"]]
+ 0074895c ["COPY", "register:4048:8", ["const:c78000:8"]]
- 007485ac bytes 692900f0
+ 0074895c bytes 89290090
- 007485b0 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 007485b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007485b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007485b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00748960 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00748960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00748960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00748960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007485b0 bytes 29413e91
+ 00748960 bytes 29813d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4f998628d45910e4aaccb6b8c7d74c3"></a>

### [`00748618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748618.md) → [`007489c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/007489c8.md) FUN_007489c8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007489e4",
      "incomplete_value": false,
      "site": "007489e8",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00748634",
      "incomplete_value": false,
      "site": "00748638",
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
            "const:f90:8"
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
      "007489e8",
      "DATA",
      [
        "storage",
        "00c77f90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007489e8",
      "DATA",
      [
        "storage",
        "00c78f60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00748630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748618.md#insn-00748630) · [`00748634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748618.md#insn-00748634) · [`0074865c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748618.md#insn-0074865c)
- 新版 [`007489e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/007489c8.md#insn-007489e0) · [`007489e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/007489c8.md#insn-007489e4) · [`00748a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/007489c8.md#insn-00748a0c)

~~~diff
- 00748630 ["COPY", "register:4050:8", ["const:c77000:8"]]
+ 007489e0 ["COPY", "register:4050:8", ["const:c78000:8"]]
- 00748630 bytes 6a2900f0
+ 007489e0 bytes 8a290090
- 00748634 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 00748634 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00748634 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00748634 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007489e4 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 007489e4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007489e4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007489e4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00748634 bytes 4a413e91
+ 007489e4 bytes 4a813d91
- 0074865c ["COPY", "register:0:8", ["register:4048:8"]]
- 0074865c ["INT_ADD", "register:40f0:8", ["const:74865c:8", "const:4:8"]]
- 0074865c ["CALLIND", null, ["register:0:8"]]
+ 00748a0c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00748a0c ["INT_ADD", "register:40f0:8", ["const:748a0c:8", "const:4:8"]]
+ 00748a0c ["CALLIND", null, ["register:0:8"]]
- 0074865c bytes 20013fd6
+ 00748a0c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8ddd4ce5f3443f23e07a8209a913506"></a>

### [`007487c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007487c8.md) → [`00748b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748b78.md) FUN_00748b78

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
      "definition_site": "00748b8c",
      "incomplete_value": false,
      "site": "00748b90",
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
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007487dc",
      "incomplete_value": false,
      "site": "007487e0",
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
            "const:10:8"
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
      "00748b90",
      "DATA",
      [
        "storage",
        "00c78010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00748b90",
      "DATA",
      [
        "storage",
        "00c78fe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007487d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007487c8.md#insn-007487d4) · [`007487dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007487c8.md#insn-007487dc)
- 新版 [`00748b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748b78.md#insn-00748b84) · [`00748b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748b78.md#insn-00748b8c)

~~~diff
- 007487d4 ["INT_ADD", "register:40f0:8", ["const:7487d4:8", "const:4:8"]]
- 007487d4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00748b84 ["INT_ADD", "register:40f0:8", ["const:748b84:8", "const:4:8"]]
+ 00748b84 ["CALL", null, ["callee:00c58f30:8"]]
- 007487d4 bytes e33d1494
+ 00748b84 bytes eb401494
- 007487dc ["COPY", "tmp:0:8", ["const:10:8"]]
- 007487dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007487dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007487dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00748b8c ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 00748b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00748b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00748b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007487dc bytes 08410091
+ 00748b8c bytes 08813f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d94f50daebead6858fbe784190bf9f2a"></a>

### [`007487ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007487ec.md) → [`00748b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748b9c.md) FUN_00748b9c

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
      "definition_site": "00748ba0",
      "incomplete_value": false,
      "site": "00748ba4",
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
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007487f0",
      "incomplete_value": false,
      "site": "007487f4",
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
            "const:10:8"
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
      "00748ba4",
      "DATA",
      [
        "storage",
        "00c78010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00748ba4",
      "DATA",
      [
        "storage",
        "00c78fe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007487f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007487ec.md#insn-007487f0)
- 新版 [`00748ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748b9c.md#insn-00748ba0)

~~~diff
- 007487f0 ["COPY", "tmp:0:8", ["const:10:8"]]
- 007487f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007487f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007487f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00748ba0 ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 00748ba0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00748ba0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00748ba0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007487f0 bytes 08410091
+ 00748ba0 bytes 08813f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-192d6d65d5b94272d03d202330585d3d"></a>

### [`00748834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748834.md) → [`00748be4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748be4.md) FUN_00748be4

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
      "definition_site": "00748bf8",
      "incomplete_value": false,
      "site": "00748bfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00748848",
      "incomplete_value": false,
      "site": "0074884c",
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
            "const:90:8"
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
      "00748bfc",
      "DATA",
      [
        "storage",
        "00c78090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00748bfc",
      "DATA",
      [
        "storage",
        "00c79060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00748840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748834.md#insn-00748840) · [`00748844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748834.md#insn-00748844) · [`00748848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748834.md#insn-00748848)
- 新版 [`00748bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748be4.md#insn-00748bf0) · [`00748bf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748be4.md#insn-00748bf4) · [`00748bf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748be4.md#insn-00748bf8)

~~~diff
- 00748840 ["INT_ADD", "register:40f0:8", ["const:748840:8", "const:4:8"]]
- 00748840 ["CALL", null, ["callee:00c58f30:8"]]
+ 00748bf0 ["INT_ADD", "register:40f0:8", ["const:748bf0:8", "const:4:8"]]
+ 00748bf0 ["CALL", null, ["callee:00c58f30:8"]]
- 00748840 bytes c83d1494
+ 00748bf0 bytes d0401494
- 00748844 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00748bf4 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00748844 bytes 88290090
+ 00748bf4 bytes 882900b0
- 00748848 ["COPY", "tmp:0:8", ["const:90:8"]]
- 00748848 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00748848 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00748848 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00748bf8 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 00748bf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00748bf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00748bf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00748848 bytes 08410291
+ 00748bf8 bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e211046fbc97c6dc4f07b0f57e5bb25"></a>

### [`00748858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748858.md) → [`00748c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748c08.md) FUN_00748c08

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
      "definition_site": "00748c0c",
      "incomplete_value": false,
      "site": "00748c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074885c",
      "incomplete_value": false,
      "site": "00748860",
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
            "const:90:8"
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
      "00748c10",
      "DATA",
      [
        "storage",
        "00c78090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00748c10",
      "DATA",
      [
        "storage",
        "00c79060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00748858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748858.md#insn-00748858) · [`0074885c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748858.md#insn-0074885c)
- 新版 [`00748c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748c08.md#insn-00748c08) · [`00748c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748c08.md#insn-00748c0c)

~~~diff
- 00748858 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00748c08 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00748858 bytes 88290090
+ 00748c08 bytes 882900b0
- 0074885c ["COPY", "tmp:0:8", ["const:90:8"]]
- 0074885c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0074885c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0074885c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00748c0c ["COPY", "tmp:0:8", ["const:60:8"]]
+ 00748c0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00748c0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00748c0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0074885c bytes 08410291
+ 00748c0c bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3af893b8de000bc9c7b2d37c559abc7b"></a>

### [`007488a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007488a4.md) → [`00748c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748c54.md) FUN_00748c54

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
      "definition_site": "00748c78",
      "incomplete_value": false,
      "site": "00748c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007488c8",
      "incomplete_value": false,
      "site": "007488c8",
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
            "const:110:8"
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
      "00748c78",
      "DATA",
      [
        "storage",
        "00c78110",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00748c78",
      "DATA",
      [
        "storage",
        "00c790e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007488b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007488a4.md#insn-007488b8) · [`007488c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007488a4.md#insn-007488c0) · [`007488c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007488a4.md#insn-007488c4)
- 新版 [`00748c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748c54.md#insn-00748c68) · [`00748c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748c54.md#insn-00748c70) · [`00748c74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748c54.md#insn-00748c74)

~~~diff
- 007488b8 ["INT_ADD", "register:40f0:8", ["const:7488b8:8", "const:4:8"]]
- 007488b8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00748c68 ["INT_ADD", "register:40f0:8", ["const:748c68:8", "const:4:8"]]
+ 00748c68 ["CALL", null, ["callee:00c58f30:8"]]
- 007488b8 bytes aa3d1494
+ 00748c68 bytes b2401494
- 007488c0 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00748c70 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 007488c0 bytes 88290090
+ 00748c70 bytes 882900b0
- 007488c4 ["COPY", "tmp:0:8", ["const:110:8"]]
- 007488c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007488c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007488c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00748c74 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00748c74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00748c74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00748c74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007488c4 bytes 08410491
+ 00748c74 bytes 08810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7d27729c9c1e6bbb40a49fa6d50a5e9"></a>

### [`007488d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007488d8.md) → [`00748c88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748c88.md) FUN_00748c88

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
      "definition_site": "00748c94",
      "incomplete_value": false,
      "site": "00748c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007488e4",
      "incomplete_value": false,
      "site": "007488e4",
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
            "const:110:8"
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
      "00748c94",
      "DATA",
      [
        "storage",
        "00c78110",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00748c94",
      "DATA",
      [
        "storage",
        "00c790e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007488dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007488d8.md#insn-007488dc) · [`007488e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007488d8.md#insn-007488e0)
- 新版 [`00748c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748c88.md#insn-00748c8c) · [`00748c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748c88.md#insn-00748c90)

~~~diff
- 007488dc ["COPY", "register:4048:8", ["const:c78000:8"]]
+ 00748c8c ["COPY", "register:4048:8", ["const:c79000:8"]]
- 007488dc bytes 89290090
+ 00748c8c bytes 892900b0
- 007488e0 ["COPY", "tmp:0:8", ["const:110:8"]]
- 007488e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007488e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007488e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00748c90 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00748c90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00748c90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00748c90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007488e0 bytes 29410491
+ 00748c90 bytes 29810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-449ac7ee6f24784495a1835cb8bb89be"></a>

### [`007488f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007488f4.md) → [`00748ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ca4.md) FUN_00748ca4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`005aa1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1b0.md) [`0071d18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d18c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 7件 [`005aa560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005aa/005aa560.md) [`0071d53c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d53c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.33% / 新版 98.33%

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
      "site": "00748da0",
      "value": [
        "leaf",
        "ram:71d53c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007489f0",
      "value": [
        "leaf",
        "ram:71d18c:8"
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
      "site": "00748dc4",
      "value": [
        "leaf",
        "ram:71d53c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00748a14",
      "value": [
        "leaf",
        "ram:71d18c:8"
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
      "00748da0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d18c"
      ]
    ],
    [
      "00748dc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d18c"
      ]
    ]
  ],
  "added": [
    [
      "00748da0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d53c"
      ]
    ],
    [
      "00748dc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d53c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007489f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007488f4.md#insn-007489f0) · [`00748a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007488f4.md#insn-00748a14) · [`0074896c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007488f4.md#insn-0074896c)
- 新版 [`00748da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ca4.md#insn-00748da0) · [`00748dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ca4.md#insn-00748dc4) · [`00748d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ca4.md#insn-00748d1c)

~~~diff
- 007489f0 ["INT_ADD", "register:40f0:8", ["const:7489f0:8", "const:4:8"]]
- 007489f0 ["CALL", null, ["ram:71d18c:8"]]
+ 00748da0 ["INT_ADD", "register:40f0:8", ["const:748da0:8", "const:4:8"]]
+ 00748da0 ["CALL", null, ["ram:71d53c:8"]]
- 007489f0 bytes e751ff97
+ 00748da0 bytes e751ff97
- 00748a14 ["INT_ADD", "register:40f0:8", ["const:748a14:8", "const:4:8"]]
- 00748a14 ["CALL", null, ["ram:71d18c:8"]]
+ 00748dc4 ["INT_ADD", "register:40f0:8", ["const:748dc4:8", "const:4:8"]]
+ 00748dc4 ["CALL", null, ["ram:71d53c:8"]]
- 00748a14 bytes de51ff97
+ 00748dc4 bytes de51ff97
- 0074896c ["INT_ADD", "register:40f0:8", ["const:74896c:8", "const:4:8"]]
- 0074896c ["CALL", null, ["callee:00c58f30:8"]]
+ 00748d1c ["INT_ADD", "register:40f0:8", ["const:748d1c:8", "const:4:8"]]
+ 00748d1c ["CALL", null, ["callee:00c58f30:8"]]
- 0074896c bytes 7d3d1494
+ 00748d1c bytes 85401494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88ebb27052e11421cf4a5e85edfa0b3c"></a>

### [`00748b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b20.md) → [`00748ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ed0.md) FUN_00748ed0

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
      "definition_site": "00748ee4",
      "incomplete_value": false,
      "site": "00748ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00748b34",
      "incomplete_value": false,
      "site": "00748b38",
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
            "const:190:8"
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
      "00748ee8",
      "DATA",
      [
        "storage",
        "00c78190",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00748ee8",
      "DATA",
      [
        "storage",
        "00c79160",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00748b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b20.md#insn-00748b2c) · [`00748b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b20.md#insn-00748b30) · [`00748b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b20.md#insn-00748b34)
- 新版 [`00748edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ed0.md#insn-00748edc) · [`00748ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ed0.md#insn-00748ee0) · [`00748ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ed0.md#insn-00748ee4)

~~~diff
- 00748b2c ["INT_ADD", "register:40f0:8", ["const:748b2c:8", "const:4:8"]]
- 00748b2c ["CALL", null, ["callee:00c58f30:8"]]
+ 00748edc ["INT_ADD", "register:40f0:8", ["const:748edc:8", "const:4:8"]]
+ 00748edc ["CALL", null, ["callee:00c58f30:8"]]
- 00748b2c bytes 0d3d1494
+ 00748edc bytes 15401494
- 00748b30 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00748ee0 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00748b30 bytes 88290090
+ 00748ee0 bytes 882900b0
- 00748b34 ["COPY", "tmp:0:8", ["const:190:8"]]
- 00748b34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00748b34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00748b34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00748ee4 ["COPY", "tmp:0:8", ["const:160:8"]]
+ 00748ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00748ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00748ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00748b34 bytes 08410691
+ 00748ee4 bytes 08810591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c0dad550af8adc0bff12270a82ee781"></a>

### [`00748b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b44.md) → [`00748ef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ef4.md) FUN_00748ef4

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
      "definition_site": "00748ef8",
      "incomplete_value": false,
      "site": "00748efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00748b48",
      "incomplete_value": false,
      "site": "00748b4c",
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
            "const:190:8"
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
      "00748efc",
      "DATA",
      [
        "storage",
        "00c78190",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00748efc",
      "DATA",
      [
        "storage",
        "00c79160",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00748b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b44.md#insn-00748b44) · [`00748b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b44.md#insn-00748b48)
- 新版 [`00748ef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ef4.md#insn-00748ef4) · [`00748ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ef4.md#insn-00748ef8)

~~~diff
- 00748b44 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00748ef4 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00748b44 bytes 88290090
+ 00748ef4 bytes 882900b0
- 00748b48 ["COPY", "tmp:0:8", ["const:190:8"]]
- 00748b48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00748b48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00748b48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00748ef8 ["COPY", "tmp:0:8", ["const:160:8"]]
+ 00748ef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00748ef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00748ef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00748b48 bytes 08410691
+ 00748ef8 bytes 08810591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e3ccc79d9feab2f36b045c4e3707958"></a>

### [`00748fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748fa0.md) → [`00749350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749350.md) FUN_00749350

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007472b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/007472b4.md) [`00748d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748d7c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`00747664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747664.md) [`0074912c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/0074912c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0074935c",
      "incomplete_value": false,
      "site": "00749360",
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
      "definition_site": "00748fac",
      "incomplete_value": false,
      "site": "00748fb0",
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
      "0074935c",
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
      "0074935c",
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

- 旧版 [`00748fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748fa0.md#insn-00748fb0) · [`00748fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748fa0.md#insn-00748fa8) · [`00748fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748fa0.md#insn-00748fac)
- 新版 [`00749360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749350.md#insn-00749360) · [`00749358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749350.md#insn-00749358) · [`0074935c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749350.md#insn-0074935c)

~~~diff
- 00748fb0 ["INT_ADD", "register:40f0:8", ["const:748fb0:8", "const:4:8"]]
- 00748fb0 ["CALL", null, ["callee:0043bad8:8"]]
+ 00749360 ["INT_ADD", "register:40f0:8", ["const:749360:8", "const:4:8"]]
+ 00749360 ["CALL", null, ["callee:0043bad8:8"]]
- 00748fb0 bytes 02caf397
+ 00749360 bytes dec9f397
- 00748fa8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00749358 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00748fa8 bytes 60dbfff0
+ 00749358 bytes 60dbfff0
- 00748fac ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00748fac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00748fac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00748fac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0074935c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0074935c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0074935c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0074935c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00748fac bytes 00303e91
+ 0074935c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a62ebc0ca7be1a2b378a56bf09204b4b"></a>

### [`00749010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749010.md) → [`007493c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/007493c0.md) FUN_007493c0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00749010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749010.md) [`007acb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007acb24.md) [`009a5c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5c58.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 3件 [`007493c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/007493c0.md) [`007acf48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ac/007acf48.md) [`009a6c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a6c04.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00749510",
      "incomplete_value": false,
      "site": "00749518",
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
            "const:62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00749160",
      "incomplete_value": false,
      "site": "00749168",
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
            "const:f93:8"
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
      "definition_site": "00749534",
      "incomplete_value": false,
      "site": "00749540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:f73:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00749184",
      "incomplete_value": false,
      "site": "00749190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:f29:8"
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
      "definition_site": "00749668",
      "incomplete_value": false,
      "site": "00749670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:ef6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007492b8",
      "incomplete_value": false,
      "site": "007492c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:e27:8"
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
      "00749510",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00749534",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "00749668",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00749510",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "00749534",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ],
    [
      "00749668",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00749168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749010.md#insn-00749168) · [`00749190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749010.md#insn-00749190) · [`007492c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749010.md#insn-007492c0)
- 新版 [`00749518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/007493c0.md#insn-00749518) · [`00749540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/007493c0.md#insn-00749540) · [`00749670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/007493c0.md#insn-00749670)

~~~diff
- 00749168 ["INT_ADD", "register:40f0:8", ["const:749168:8", "const:4:8"]]
- 00749168 ["CALL", null, ["callee:004421f4:8"]]
+ 00749518 ["INT_ADD", "register:40f0:8", ["const:749518:8", "const:4:8"]]
+ 00749518 ["CALL", null, ["callee:004421f4:8"]]
- 00749168 bytes 5be3f397
+ 00749518 bytes 37e3f397
- 00749190 ["INT_ADD", "register:40f0:8", ["const:749190:8", "const:4:8"]]
- 00749190 ["CALL", null, ["callee:00442b54:8"]]
+ 00749540 ["INT_ADD", "register:40f0:8", ["const:749540:8", "const:4:8"]]
+ 00749540 ["CALL", null, ["callee:00442b54:8"]]
- 00749190 bytes a9e5f397
+ 00749540 bytes 85e5f397
- 007492c0 ["INT_ADD", "register:40f0:8", ["const:7492c0:8", "const:4:8"]]
- 007492c0 ["CALL", null, ["callee:004421f4:8"]]
+ 00749670 ["INT_ADD", "register:40f0:8", ["const:749670:8", "const:4:8"]]
+ 00749670 ["CALL", null, ["callee:004421f4:8"]]
- 007492c0 bytes 05e3f397
+ 00749670 bytes e1e2f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc5d6112c262bf4a8fc1a966b7314c95"></a>

### [`007497fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/007497fc.md) → [`00749bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749bac.md) FUN_00749bac

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
      "definition_site": "00749bb8",
      "incomplete_value": false,
      "site": "00749bc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00749808",
      "incomplete_value": false,
      "site": "00749814",
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
      "00749bc4",
      "DATA",
      [
        "storage",
        "00c78210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00749bc4",
      "DATA",
      [
        "storage",
        "00c791e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00749804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/007497fc.md#insn-00749804) · [`00749808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/007497fc.md#insn-00749808)
- 新版 [`00749bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749bac.md#insn-00749bb4) · [`00749bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749bac.md#insn-00749bb8)

~~~diff
- 00749804 ["COPY", "register:4050:8", ["const:c78000:8"]]
+ 00749bb4 ["COPY", "register:4050:8", ["const:c79000:8"]]
- 00749804 bytes 6a2900f0
+ 00749bb4 bytes 8a290090
- 00749808 ["COPY", "tmp:0:8", ["const:210:8"]]
- 00749808 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00749808 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00749808 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00749bb8 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 00749bb8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00749bb8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00749bb8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00749808 bytes 4a410891
+ 00749bb8 bytes 4a810791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c8aeb7a4d931c92d4a992dadd26312e"></a>

### [`00749840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749840.md) → [`00749bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749bf0.md) FUN_00749bf0

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
      "definition_site": "00749c08",
      "incomplete_value": false,
      "site": "00749c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00749858",
      "incomplete_value": false,
      "site": "00749864",
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
            "const:210:8"
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
      "00749c14",
      "DATA",
      [
        "storage",
        "00c78210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00749c14",
      "DATA",
      [
        "storage",
        "00c791e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00749854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749840.md#insn-00749854) · [`00749858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749840.md#insn-00749858) · [`00749888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749840.md#insn-00749888)
- 新版 [`00749c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749bf0.md#insn-00749c04) · [`00749c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749bf0.md#insn-00749c08) · [`00749c38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749bf0.md#insn-00749c38)

~~~diff
- 00749854 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00749c04 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00749854 bytes 682900f0
+ 00749c04 bytes 88290090
- 00749858 ["COPY", "tmp:0:8", ["const:210:8"]]
- 00749858 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00749858 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00749858 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00749c08 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 00749c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00749c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00749c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00749858 bytes 08410891
+ 00749c08 bytes 08810791
- 00749888 ["COPY", "register:0:8", ["register:4040:8"]]
- 00749888 ["INT_ADD", "register:40f0:8", ["const:749888:8", "const:4:8"]]
- 00749888 ["CALLIND", null, ["register:0:8"]]
+ 00749c38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00749c38 ["INT_ADD", "register:40f0:8", ["const:749c38:8", "const:4:8"]]
+ 00749c38 ["CALLIND", null, ["register:0:8"]]
- 00749888 bytes 00013fd6
+ 00749c38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8453060a56ac4920bc3670fdac55d62"></a>

### [`0074989c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/0074989c.md) → [`00749c4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749c4c.md) FUN_00749c4c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00749c78",
      "incomplete_value": false,
      "site": "00749c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007498c8",
      "incomplete_value": false,
      "site": "007498c8",
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
            "const:210:8"
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
      "00749c78",
      "DATA",
      [
        "storage",
        "00c78210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00749c78",
      "DATA",
      [
        "storage",
        "00c791e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007498b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/0074989c.md#insn-007498b0) · [`007498bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/0074989c.md#insn-007498bc) · [`007498c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/0074989c.md#insn-007498c0)
- 新版 [`00749c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749c4c.md#insn-00749c60) · [`00749c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749c4c.md#insn-00749c6c) · [`00749c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749c4c.md#insn-00749c70)

~~~diff
- 007498b0 ["INT_ADD", "register:40f0:8", ["const:7498b0:8", "const:4:8"]]
- 007498b0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00749c60 ["INT_ADD", "register:40f0:8", ["const:749c60:8", "const:4:8"]]
+ 00749c60 ["CALL", null, ["callee:00c58f30:8"]]
- 007498b0 bytes ac391494
+ 00749c60 bytes b43c1494
- 007498bc ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00749c6c ["COPY", "register:4040:8", ["const:c79000:8"]]
- 007498bc bytes 682900f0
+ 00749c6c bytes 88290090
- 007498c0 ["COPY", "tmp:0:8", ["const:210:8"]]
- 007498c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007498c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007498c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00749c70 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 00749c70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00749c70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00749c70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007498c0 bytes 08410891
+ 00749c70 bytes 08810791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f659bb61acaf404d5b050696d4d772d"></a>

### [`0074992c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/0074992c.md) → [`00749cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749cdc.md) FUN_00749cdc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00749cfc",
      "incomplete_value": false,
      "site": "00749cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074994c",
      "incomplete_value": false,
      "site": "0074994c",
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
            "const:210:8"
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
      "00749cfc",
      "DATA",
      [
        "storage",
        "00c78210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00749cfc",
      "DATA",
      [
        "storage",
        "00c791e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00749944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/0074992c.md#insn-00749944) · [`00749948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/0074992c.md#insn-00749948) · [`00749968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/0074992c.md#insn-00749968)
- 新版 [`00749cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749cdc.md#insn-00749cf4) · [`00749cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749cdc.md#insn-00749cf8) · [`00749d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749cdc.md#insn-00749d18)

~~~diff
- 00749944 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00749cf4 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00749944 bytes 682900f0
+ 00749cf4 bytes 88290090
- 00749948 ["COPY", "tmp:0:8", ["const:210:8"]]
- 00749948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00749948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00749948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00749cf8 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 00749cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00749cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00749cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00749948 bytes 08410891
+ 00749cf8 bytes 08810791
- 00749968 ["COPY", "register:0:8", ["register:4040:8"]]
- 00749968 ["INT_ADD", "register:40f0:8", ["const:749968:8", "const:4:8"]]
- 00749968 ["CALLIND", null, ["register:0:8"]]
+ 00749d18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00749d18 ["INT_ADD", "register:40f0:8", ["const:749d18:8", "const:4:8"]]
+ 00749d18 ["CALLIND", null, ["register:0:8"]]
- 00749968 bytes 00013fd6
+ 00749d18 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-178cfb8273733630d30e310a7c01fb0b"></a>

### [`0074a400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a400.md) → [`0074a7b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074a7b0.md) FUN_0074a7b0

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
      "definition_site": "0074a7bc",
      "incomplete_value": false,
      "site": "0074a7c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074a40c",
      "incomplete_value": false,
      "site": "0074a418",
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
            "const:290:8"
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
      "0074a7c8",
      "DATA",
      [
        "storage",
        "00c78290",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0074a7c8",
      "DATA",
      [
        "storage",
        "00c79260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0074a408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a400.md#insn-0074a408) · [`0074a40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a400.md#insn-0074a40c)
- 新版 [`0074a7b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074a7b0.md#insn-0074a7b8) · [`0074a7bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074a7b0.md#insn-0074a7bc)

~~~diff
- 0074a408 ["COPY", "register:4050:8", ["const:c78000:8"]]
+ 0074a7b8 ["COPY", "register:4050:8", ["const:c79000:8"]]
- 0074a408 bytes 6a2900d0
+ 0074a7b8 bytes 6a2900f0
- 0074a40c ["COPY", "tmp:0:8", ["const:290:8"]]
- 0074a40c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0074a40c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0074a40c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0074a7bc ["COPY", "tmp:0:8", ["const:260:8"]]
+ 0074a7bc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0074a7bc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0074a7bc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0074a40c bytes 4a410a91
+ 0074a7bc bytes 4a810991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82be24742e5cbe3e991403810076b957"></a>

### [`0074a958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a958.md) → [`0074ad08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074ad08.md) _INIT_130

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
      "definition_site": "0074ad44",
      "incomplete_value": true,
      "site": "0074ad60",
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
      "definition_site": "0074a994",
      "incomplete_value": true,
      "site": "0074a9b0",
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
      "definition_site": "0074ad68",
      "incomplete_value": true,
      "site": "0074ad84",
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
      "definition_site": "0074a9b8",
      "incomplete_value": true,
      "site": "0074a9d4",
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
      "definition_site": "0074ad88",
      "incomplete_value": true,
      "site": "0074ada4",
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
      "definition_site": "0074a9d8",
      "incomplete_value": true,
      "site": "0074a9f4",
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
      "0074ad44",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0074ad68",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0074ad88",
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
      "0074ad44",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0074ad68",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0074ad88",
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

- 旧版 [`0074ab8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a958.md#insn-0074ab8c) · [`0074a980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a958.md#insn-0074a980) · [`0074a984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a958.md#insn-0074a984)
- 新版 [`0074af3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074ad08.md#insn-0074af3c) · [`0074ad30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074ad08.md#insn-0074ad30) · [`0074ad34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074ad08.md#insn-0074ad34)

~~~diff
- 0074ab8c ["INT_ADD", "register:40f0:8", ["const:74ab8c:8", "const:4:8"]]
- 0074ab8c ["CALL", null, ["callee:00c58ed0:8"]]
+ 0074af3c ["INT_ADD", "register:40f0:8", ["const:74af3c:8", "const:4:8"]]
+ 0074af3c ["CALL", null, ["callee:00c58ed0:8"]]
- 0074ab8c bytes dd341494
+ 0074af3c bytes e5371494
- 0074a980 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 0074ad30 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 0074a980 bytes f32a00b0
+ 0074ad30 bytes f32a00d0
- 0074a984 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 0074a984 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0074a984 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0074a984 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0074ad34 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 0074ad34 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0074ad34 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0074ad34 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0074a984 bytes 73a23a91
+ 0074ad34 bytes 73a23991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e63f2a24d395ec1dae51c22c694089a3"></a>

### [`0074b25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074b/0074b25c.md) → [`0074b60c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074b60c.md) FUN_0074b60c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md)
- 新版 呼出元 1件 [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) · 呼出先 21件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.97% / 新版 94.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0074b668",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0074b2b8",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
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
      "site": "0074b728",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0074b378",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0074b740",
      "value": [
        "leaf",
        "ram:71c2e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0074b390",
      "value": [
        "leaf",
        "ram:71bf30:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0074b668",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "0074b69c",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "0074b70c",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0074b668",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "0074b69c",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ],
    [
      "0074b70c",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0074b2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074b/0074b25c.md#insn-0074b2b8) · [`0074b378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074b/0074b25c.md#insn-0074b378) · [`0074b390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074b/0074b25c.md#insn-0074b390)
- 新版 [`0074b668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074b60c.md#insn-0074b668) · [`0074b728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074b60c.md#insn-0074b728) · [`0074b740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074b60c.md#insn-0074b740)

~~~diff
- 0074b2b8 ["INT_ADD", "register:40f0:8", ["const:74b2b8:8", "const:4:8"]]
- 0074b2b8 ["CALL", null, ["ram:6e4b1c:8"]]
+ 0074b668 ["INT_ADD", "register:40f0:8", ["const:74b668:8", "const:4:8"]]
+ 0074b668 ["CALL", null, ["ram:6e4ecc:8"]]
- 0074b2b8 bytes 1966fe97
+ 0074b668 bytes 1966fe97
- 0074b378 ["INT_ADD", "register:40f0:8", ["const:74b378:8", "const:4:8"]]
- 0074b378 ["CALL", null, ["ram:6e4b1c:8"]]
+ 0074b728 ["INT_ADD", "register:40f0:8", ["const:74b728:8", "const:4:8"]]
+ 0074b728 ["CALL", null, ["ram:6e4ecc:8"]]
- 0074b378 bytes e965fe97
+ 0074b728 bytes e965fe97
- 0074b390 ["INT_ADD", "register:40f0:8", ["const:74b390:8", "const:4:8"]]
- 0074b390 ["CALL", null, ["ram:71bf30:8"]]
+ 0074b740 ["INT_ADD", "register:40f0:8", ["const:74b740:8", "const:4:8"]]
+ 0074b740 ["CALL", null, ["ram:71c2e0:8"]]
- 0074b390 bytes e842ff97
+ 0074b740 bytes e842ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e21ade243fb0e40844e985478e9c1e29"></a>

### [`0074baa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074b/0074baa8.md) → [`0074be58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074be58.md) FUN_0074be58

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00651ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00651/00651ae4.md) · 呼出先 5件 [`00615be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615be0.md) [`0063dc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063dc84.md) [`00641ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641ba0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00651e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00651/00651e94.md) · 呼出先 5件 [`00615f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00615/00615f90.md) [`0063e034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063e/0063e034.md) [`00641f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641f50.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

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
      "site": "0074beb8",
      "value": [
        "leaf",
        "ram:63e034:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0074bb08",
      "value": [
        "leaf",
        "ram:63dc84:8"
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
      "site": "0074bee0",
      "value": [
        "leaf",
        "ram:641f50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0074bb30",
      "value": [
        "leaf",
        "ram:641ba0:8"
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
      "0074bea0",
      "DATA",
      [
        "storage",
        "004347d0",
        null,
        "dword"
      ]
    ],
    [
      "0074beb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063dc84"
      ]
    ],
    [
      "0074bed4",
      "DATA",
      [
        "storage",
        "004347d0",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "0074bea0",
      "DATA",
      [
        "storage",
        "004347d0",
        null,
        "byte[35]"
      ]
    ],
    [
      "0074beb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063e034"
      ]
    ],
    [
      "0074bed4",
      "DATA",
      [
        "storage",
        "004347d0",
        null,
        "byte[35]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0074bb08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074b/0074baa8.md#insn-0074bb08) · [`0074bb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074b/0074baa8.md#insn-0074bb30) · [`0074bad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074b/0074baa8.md#insn-0074bad0)
- 新版 [`0074beb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074be58.md#insn-0074beb8) · [`0074bee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074be58.md#insn-0074bee0) · [`0074be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074be58.md#insn-0074be80)

~~~diff
- 0074bb08 ["INT_ADD", "register:40f0:8", ["const:74bb08:8", "const:4:8"]]
- 0074bb08 ["CALL", null, ["ram:63dc84:8"]]
+ 0074beb8 ["INT_ADD", "register:40f0:8", ["const:74beb8:8", "const:4:8"]]
+ 0074beb8 ["CALL", null, ["ram:63e034:8"]]
- 0074bb08 bytes 5fc8fb97
+ 0074beb8 bytes 5fc8fb97
- 0074bb30 ["INT_ADD", "register:40f0:8", ["const:74bb30:8", "const:4:8"]]
- 0074bb30 ["CALL", null, ["ram:641ba0:8"]]
+ 0074bee0 ["INT_ADD", "register:40f0:8", ["const:74bee0:8", "const:4:8"]]
+ 0074bee0 ["CALL", null, ["ram:641f50:8"]]
- 0074bb30 bytes 1cd8fb97
+ 0074bee0 bytes 1cd8fb97
- 0074bad0 ["INT_ADD", "register:40f0:8", ["const:74bad0:8", "const:4:8"]]
- 0074bad0 ["CALL", null, ["callee:008524fc:8"]]
+ 0074be80 ["INT_ADD", "register:40f0:8", ["const:74be80:8", "const:4:8"]]
+ 0074be80 ["CALL", null, ["callee:008524fc:8"]]
- 0074bad0 bytes a0160494
+ 0074be80 bytes 9f190494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00e3652156c503fa8922997935909380"></a>

### [`0074c928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074c/0074c928.md) → [`0074ccd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074c/0074ccd8.md) FUN_0074ccd8

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 13件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00468844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468844.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md)
- 新版 呼出元 1件 [`007e00a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007e0/007e00a4.md) · 呼出先 13件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`00468b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468b64.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.15% / 新版 98.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0074cdc8",
      "incomplete_value": true,
      "site": "0074cdd4",
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074ca18",
      "incomplete_value": true,
      "site": "0074ca24",
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
                "const:c80:8"
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
      "definition_site": "0074cdf8",
      "incomplete_value": true,
      "site": "0074ce08",
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
                "const:178:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074ca48",
      "incomplete_value": true,
      "site": "0074ca58",
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
                "const:128:8"
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
      "definition_site": "0074ceac",
      "incomplete_value": true,
      "site": "0074ceb8",
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074cafc",
      "incomplete_value": true,
      "site": "0074cb08",
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
                "const:c80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0074cd30",
      "READ",
      [
        "storage",
        "00c9b578",
        null,
        "pointer"
      ]
    ],
    [
      "0074cd34",
      "DATA",
      [
        "storage",
        "00ca4554",
        null,
        null
      ]
    ],
    [
      "0074cdc8",
      "READ",
      [
        "storage",
        "002c2c80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0074cd30",
      "READ",
      [
        "storage",
        "00c9c548",
        null,
        "pointer"
      ]
    ],
    [
      "0074cd34",
      "DATA",
      [
        "storage",
        "00ca5524",
        null,
        null
      ]
    ],
    [
      "0074cdc8",
      "READ",
      [
        "storage",
        "002c2cd0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0074d78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074c/0074c928.md#insn-0074d78c) · [`0074c95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074c/0074c928.md#insn-0074c95c) · [`0074c964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074c/0074c928.md#insn-0074c964)
- 新版 [`0074db3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074c/0074ccd8.md#insn-0074db3c) · [`0074cd0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074c/0074ccd8.md#insn-0074cd0c) · [`0074cd14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074c/0074ccd8.md#insn-0074cd14)

~~~diff
- 0074d78c ["INT_ADD", "register:40f0:8", ["const:74d78c:8", "const:4:8"]]
- 0074d78c ["CALL", null, ["callee:00467e8c:8"]]
+ 0074db3c ["INT_ADD", "register:40f0:8", ["const:74db3c:8", "const:4:8"]]
+ 0074db3c ["CALL", null, ["callee:00467e8c:8"]]
- 0074d78c bytes f868f497
+ 0074db3c bytes d468f497
- 0074c95c ["INT_ADD", "register:40f0:8", ["const:74c95c:8", "const:4:8"]]
- 0074c95c ["CALL", null, ["callee:00467bc0:8"]]
+ 0074cd0c ["INT_ADD", "register:40f0:8", ["const:74cd0c:8", "const:4:8"]]
+ 0074cd0c ["CALL", null, ["callee:00467bc0:8"]]
- 0074c95c bytes d16bf497
+ 0074cd0c bytes ad6bf497
- 0074c964 ["INT_ADD", "register:40f0:8", ["const:74c964:8", "const:4:8"]]
- 0074c964 ["CALL", null, ["callee:008524fc:8"]]
+ 0074cd14 ["INT_ADD", "register:40f0:8", ["const:74cd14:8", "const:4:8"]]
+ 0074cd14 ["CALL", null, ["callee:008524fc:8"]]
- 0074c964 bytes fb120494
+ 0074cd14 bytes fa150494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69495ab25d82e240cbd18bd63857978d"></a>

### [`0074dc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074d/0074dc64.md) → [`0074e014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074e/0074e014.md) FUN_0074e014

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 9件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00b11188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11188.md)
- 新版 呼出元 1件 [`0081b818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081b/0081b818.md) · 呼出先 9件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487dc4.md) [`00b1217c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b12/00b1217c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0074e044",
      "incomplete_value": true,
      "site": "0074e05c",
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
                "const:e33:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074dc94",
      "incomplete_value": true,
      "site": "0074dcac",
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
                "const:d5c:8"
              ]
            ]
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
      "0074e044",
      "READ",
      [
        "storage",
        "002afd5c",
        null,
        "string"
      ]
    ],
    [
      "0074e328",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0074e044",
      "READ",
      [
        "storage",
        "002afe33",
        null,
        "string"
      ]
    ],
    [
      "0074e328",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0074dc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074d/0074dc64.md#insn-0074dc8c) · [`0074dcc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074d/0074dc64.md#insn-0074dcc4) · [`0074dcd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074d/0074dc64.md#insn-0074dcd8)
- 新版 [`0074e03c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074e/0074e014.md#insn-0074e03c) · [`0074e074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074e/0074e014.md#insn-0074e074) · [`0074e088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074e/0074e014.md#insn-0074e088)

~~~diff
- 0074dc8c ["COPY", "tmp:0:8", ["const:d5c:8"]]
- 0074dc8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0074dc8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0074dc8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0074e03c ["COPY", "tmp:0:8", ["const:e33:8"]]
+ 0074e03c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0074e03c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0074e03c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0074dc8c bytes 29713591
+ 0074e03c bytes 29cd3891
- 0074dcc4 ["INT_ADD", "register:40f0:8", ["const:74dcc4:8", "const:4:8"]]
- 0074dcc4 ["CALL", null, ["callee:00b1217c:8"]]
+ 0074e074 ["INT_ADD", "register:40f0:8", ["const:74e074:8", "const:4:8"]]
+ 0074e074 ["CALL", null, ["callee:00b1217c:8"]]
- 0074dcc4 bytes 310d0f94
+ 0074e074 bytes 42100f94
- 0074dcd8 ["INT_ADD", "register:40f0:8", ["const:74dcd8:8", "const:4:8"]]
- 0074dcd8 ["CALL", null, ["callee:00c58f50:8"]]
+ 0074e088 ["INT_ADD", "register:40f0:8", ["const:74e088:8", "const:4:8"]]
+ 0074e088 ["CALL", null, ["callee:00c58f50:8"]]
- 0074dcd8 bytes aa281494
+ 0074e088 bytes b22b1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b45168e997315975e0265cf35e3c279"></a>

### [`0074e3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074e/0074e3dc.md) → [`0074e78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074e/0074e78c.md) FUN_0074e78c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00932664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00932/00932664.md) · 呼出先 15件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043e868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e868.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0048cef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cef8.md) [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md)
- 新版 呼出元 1件 [`00933610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00933/00933610.md) · 呼出先 15件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043eb88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043eb88.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0048d218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d218.md) [`00493168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493168.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.75% / 新版 92.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0074e7f8",
      "incomplete_value": true,
      "site": "0074e7f8",
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
                "const:106:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074e448",
      "incomplete_value": true,
      "site": "0074e448",
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
                "const:39:8"
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
      "definition_site": "0074e824",
      "incomplete_value": true,
      "site": "0074e824",
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
      "definition_site": "0074e474",
      "incomplete_value": true,
      "site": "0074e474",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0074e8b8",
      "incomplete_value": true,
      "site": "0074e8d0",
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
                "const:b83:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074e508",
      "incomplete_value": true,
      "site": "0074e520",
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
                "const:ab6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0074e7ec",
      "READ",
      [
        "storage",
        "002a9039",
        null,
        "string"
      ]
    ],
    [
      "0074e814",
      "READ",
      [
        "storage",
        "002a9e83",
        null,
        "string"
      ]
    ],
    [
      "0074e8b8",
      "READ",
      [
        "storage",
        "002acab6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0074e7ec",
      "READ",
      [
        "storage",
        "002a9106",
        null,
        "string"
      ]
    ],
    [
      "0074e814",
      "READ",
      [
        "storage",
        "002a9f50",
        null,
        "string"
      ]
    ],
    [
      "0074e8b8",
      "READ",
      [
        "storage",
        "002acb83",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0074e438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074e/0074e3dc.md#insn-0074e438) · [`0074e454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074e/0074e3dc.md#insn-0074e454) · [`0074e45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074e/0074e3dc.md#insn-0074e45c)
- 新版 [`0074e7e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074e/0074e78c.md#insn-0074e7e8) · [`0074e804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074e/0074e78c.md#insn-0074e804) · [`0074e80c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074e/0074e78c.md#insn-0074e80c)

~~~diff
- 0074e438 ["COPY", "tmp:0:8", ["const:39:8"]]
- 0074e438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0074e438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0074e438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0074e7e8 ["COPY", "tmp:0:8", ["const:106:8"]]
+ 0074e7e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0074e7e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0074e7e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0074e438 bytes 08e50091
+ 0074e7e8 bytes 08190491
- 0074e454 ["INT_ADD", "register:40f0:8", ["const:74e454:8", "const:4:8"]]
- 0074e454 ["CALL", null, ["callee:0048d1b4:8"]]
+ 0074e804 ["INT_ADD", "register:40f0:8", ["const:74e804:8", "const:4:8"]]
+ 0074e804 ["CALL", null, ["callee:0048d1b4:8"]]
- 0074e454 bytes 90faf497
+ 0074e804 bytes 6cfaf497
- 0074e45c ["COPY", "tmp:0:8", ["const:e83:8"]]
- 0074e45c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0074e45c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0074e45c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0074e80c ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 0074e80c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0074e80c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0074e80c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0074e45c bytes 290d3a91
+ 0074e80c bytes 29413d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67e5f25e9ebaa078d1de5c69c82bb148"></a>

### [`0074f3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074f/0074f3e8.md) → [`0074f798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074f/0074f798.md) FUN_0074f798

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) · 呼出先 8件 [`0071d12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d12c.md) [`0071ed58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071ed58.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0094826c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00948/0094826c.md) · 呼出先 8件 [`0071d4dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d4dc.md) [`0071f108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f108.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.33% / 新版 99.33%

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
      "site": "0074f7dc",
      "value": [
        "leaf",
        "ram:71d4dc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0074f42c",
      "value": [
        "leaf",
        "ram:71d12c:8"
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
      "0074f7dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d12c"
      ]
    ]
  ],
  "added": [
    [
      "0074f7dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d4dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0074f42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074f/0074f3e8.md#insn-0074f42c) · [`0074f410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074f/0074f3e8.md#insn-0074f410) · [`0074f434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074f/0074f3e8.md#insn-0074f434)
- 新版 [`0074f7dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074f/0074f798.md#insn-0074f7dc) · [`0074f7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074f/0074f798.md#insn-0074f7c0) · [`0074f7e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074f/0074f798.md#insn-0074f7e4)

~~~diff
- 0074f42c ["INT_ADD", "register:40f0:8", ["const:74f42c:8", "const:4:8"]]
- 0074f42c ["CALL", null, ["ram:71d12c:8"]]
+ 0074f7dc ["INT_ADD", "register:40f0:8", ["const:74f7dc:8", "const:4:8"]]
+ 0074f7dc ["CALL", null, ["ram:71d4dc:8"]]
- 0074f42c bytes 4037ff97
+ 0074f7dc bytes 4037ff97
- 0074f410 ["INT_ADD", "register:40f0:8", ["const:74f410:8", "const:4:8"]]
- 0074f410 ["CALL", null, ["callee:008524fc:8"]]
+ 0074f7c0 ["INT_ADD", "register:40f0:8", ["const:74f7c0:8", "const:4:8"]]
+ 0074f7c0 ["CALL", null, ["callee:008524fc:8"]]
- 0074f410 bytes 50080494
+ 0074f7c0 bytes 4f0b0494
- 0074f434 ["INT_ADD", "register:40f0:8", ["const:74f434:8", "const:4:8"]]
- 0074f434 ["CALL", null, ["callee:0071f108:8"]]
+ 0074f7e4 ["INT_ADD", "register:40f0:8", ["const:74f7e4:8", "const:4:8"]]
+ 0074f7e4 ["CALL", null, ["callee:0071f108:8"]]
- 0074f434 bytes 493eff97
+ 0074f7e4 bytes 493eff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abec7f8f0ce019041b31834bdd6fca74"></a>

### [`007522f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522f0.md) → [`007526a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/007526a0.md) FUN_007526a0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009bf72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009bf/009bf72c.md) · 呼出先 10件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md) [`005ae628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae628.md) [`005da5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005da/005da5c4.md)
- 新版 呼出元 1件 [`009c06d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009c0/009c06d8.md) · 呼出先 10件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00493168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493168.md) [`005ae9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ae/005ae9d8.md) [`005da974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005da/005da974.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.57% / 新版 95.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00752714",
      "incomplete_value": true,
      "site": "00752724",
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
                "const:b96:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00752364",
      "incomplete_value": true,
      "site": "00752374",
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
                "const:ac9:8"
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
      "definition_site": "00752728",
      "incomplete_value": true,
      "site": "00752728",
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
      "definition_site": "00752378",
      "incomplete_value": true,
      "site": "00752378",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0075284c",
      "incomplete_value": false,
      "site": "00752854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:e1c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075249c",
      "incomplete_value": false,
      "site": "007524a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:d3e:8"
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
      "007526e8",
      "DATA",
      [
        "storage",
        "003965a4",
        null,
        "qword"
      ]
    ],
    [
      "00752714",
      "READ",
      [
        "storage",
        "002acac9",
        null,
        "string"
      ]
    ],
    [
      "00752718",
      "READ",
      [
        "storage",
        "002acad6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007526e8",
      "DATA",
      [
        "storage",
        "003965a4",
        "fde_003965a4",
        "dword"
      ]
    ],
    [
      "00752714",
      "READ",
      [
        "storage",
        "002acb96",
        null,
        "string"
      ]
    ],
    [
      "00752718",
      "READ",
      [
        "storage",
        "002acba3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007524a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522f0.md#insn-007524a4) · [`00752508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522f0.md#insn-00752508) · [`00752320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522f0.md#insn-00752320)
- 新版 [`00752854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/007526a0.md#insn-00752854) · [`007528b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/007526a0.md#insn-007528b8) · [`007526d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/007526a0.md#insn-007526d0)

~~~diff
- 007524a4 ["INT_ADD", "register:40f0:8", ["const:7524a4:8", "const:4:8"]]
- 007524a4 ["CALL", null, ["callee:0043e138:8"]]
+ 00752854 ["INT_ADD", "register:40f0:8", ["const:752854:8", "const:4:8"]]
+ 00752854 ["CALL", null, ["callee:0043e138:8"]]
- 007524a4 bytes 5daef397
+ 00752854 bytes 39aef397
- 00752508 ["INT_ADD", "register:40f0:8", ["const:752508:8", "const:4:8"]]
- 00752508 ["CALL", null, ["callee:0043e138:8"]]
+ 007528b8 ["INT_ADD", "register:40f0:8", ["const:7528b8:8", "const:4:8"]]
+ 007528b8 ["CALL", null, ["callee:0043e138:8"]]
- 00752508 bytes 44aef397
+ 007528b8 bytes 20aef397
- 00752320 ["INT_ADD", "register:40f0:8", ["const:752320:8", "const:4:8"]]
- 00752320 ["CALL", null, ["callee:008524fc:8"]]
+ 007526d0 ["INT_ADD", "register:40f0:8", ["const:7526d0:8", "const:4:8"]]
+ 007526d0 ["CALL", null, ["callee:008524fc:8"]]
- 00752320 bytes 8cfc0394
+ 007526d0 bytes 8bff0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-711ec5aa6092646754b4621c1945baf0"></a>

### [`00752644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/00752644.md) → [`007529f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/007529f4.md) FUN_007529f4

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009bf72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009bf/009bf72c.md) · 呼出先 15件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md) [`005da5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005da/005da5c4.md) [`00664a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664a2c.md)
- 新版 呼出元 1件 [`009c06d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009c0/009c06d8.md) · 呼出先 15件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00493168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493168.md) [`005da974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005da/005da974.md) [`00664ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664ddc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.39% / 新版 96.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00752a58",
      "incomplete_value": true,
      "site": "00752a80",
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
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007526a8",
      "incomplete_value": true,
      "site": "007526d0",
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
                "const:2e0:8"
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
      "definition_site": "00752dec",
      "incomplete_value": true,
      "site": "00752df8",
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
                "const:5d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00752a3c",
      "incomplete_value": true,
      "site": "00752a48",
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
                "const:f7f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00752b14",
      "incomplete_value": false,
      "site": "00752b18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00752764",
      "incomplete_value": false,
      "site": "00752768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:76a:8"
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
      "00752a58",
      "READ",
      [
        "storage",
        "002c22e0",
        null,
        null
      ]
    ],
    [
      "00752b14",
      "PARAM",
      [
        "storage",
        "002bc76a",
        null,
        null
      ]
    ],
    [
      "00752b20",
      "READ",
      [
        "storage",
        "002acac9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00752a58",
      "READ",
      [
        "storage",
        "002c2330",
        null,
        null
      ]
    ],
    [
      "00752b14",
      "PARAM",
      [
        "storage",
        "002bc848",
        null,
        null
      ]
    ],
    [
      "00752b20",
      "READ",
      [
        "storage",
        "002acb96",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00752768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/00752644.md#insn-00752768) · [`00752824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/00752644.md#insn-00752824) · [`00752a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/00752644.md#insn-00752a24)
- 新版 [`00752b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/007529f4.md#insn-00752b18) · [`00752bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/007529f4.md#insn-00752bd4) · [`00752dd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/007529f4.md#insn-00752dd4)

~~~diff
- 00752768 ["INT_ADD", "register:40f0:8", ["const:752768:8", "const:4:8"]]
- 00752768 ["CALL", null, ["callee:00c59010:8"]]
+ 00752b18 ["INT_ADD", "register:40f0:8", ["const:752b18:8", "const:4:8"]]
+ 00752b18 ["CALL", null, ["callee:00c59010:8"]]
- 00752768 bytes 36161494
+ 00752b18 bytes 3e191494
- 00752824 ["INT_ADD", "register:40f0:8", ["const:752824:8", "const:4:8"]]
- 00752824 ["CALL", null, ["callee:00c59010:8"]]
+ 00752bd4 ["INT_ADD", "register:40f0:8", ["const:752bd4:8", "const:4:8"]]
+ 00752bd4 ["CALL", null, ["callee:00c59010:8"]]
- 00752824 bytes 07161494
+ 00752bd4 bytes 0f191494
- 00752a24 ["INT_ADD", "register:40f0:8", ["const:752a24:8", "const:4:8"]]
- 00752a24 ["CALL", null, ["callee:00c59010:8"]]
+ 00752dd4 ["INT_ADD", "register:40f0:8", ["const:752dd4:8", "const:4:8"]]
+ 00752dd4 ["CALL", null, ["callee:00c59010:8"]]
- 00752a24 bytes 87151494
+ 00752dd4 bytes 8f181494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-797de859f57d79ae46e84630a1a13dc4"></a>

### [`00752c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/00752c28.md) → [`00752fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/00752fd8.md) FUN_00752fd8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a6dd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6d/00a6dd44.md) · 呼出先 13件 [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 1件 [`00a6ed38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6e/00a6ed38.md) · 呼出先 13件 [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.26% / 新版 88.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "007532a8",
      "incomplete_value": true,
      "site": "007532a8",
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
                "register:4008:8"
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
      "definition_site": "00752ef8",
      "incomplete_value": true,
      "site": "00752ef8",
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
                "register:4008:8"
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
    "ordinal": 27,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "007532ac",
      "incomplete_value": true,
      "site": "007532ac",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00752efc",
      "incomplete_value": true,
      "site": "00752efc",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007532a8",
      "incomplete_value": true,
      "site": "007532ac",
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
                "register:4008:8"
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
      "definition_site": "00752ef8",
      "incomplete_value": true,
      "site": "00752efc",
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
                "register:4008:8"
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00753010",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "0075302c",
      "READ",
      [
        "storage",
        "00c9ad70",
        null,
        "pointer"
      ]
    ],
    [
      "0075302c",
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
      "00753010",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "0075302c",
      "READ",
      [
        "storage",
        "00c9bd40",
        null,
        "pointer"
      ]
    ],
    [
      "0075302c",
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

- 旧版 [`00752ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/00752c28.md#insn-00752ca0) · [`00752de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/00752c28.md#insn-00752de4) · [`00752ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/00752c28.md#insn-00752ed4)
- 新版 [`00753050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/00752fd8.md#insn-00753050) · [`00753194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/00752fd8.md#insn-00753194) · [`00753284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/00752fd8.md#insn-00753284)

~~~diff
- 00752ca0 ["INT_ADD", "register:40f0:8", ["const:752ca0:8", "const:4:8"]]
- 00752ca0 ["CALL", null, ["callee:0047ec3c:8"]]
+ 00753050 ["INT_ADD", "register:40f0:8", ["const:753050:8", "const:4:8"]]
+ 00753050 ["CALL", null, ["callee:0047ec3c:8"]]
- 00752ca0 bytes 1faff497
+ 00753050 bytes fbaef497
- 00752de4 ["INT_ADD", "register:40f0:8", ["const:752de4:8", "const:4:8"]]
- 00752de4 ["CALL", null, ["callee:0047ec3c:8"]]
+ 00753194 ["INT_ADD", "register:40f0:8", ["const:753194:8", "const:4:8"]]
+ 00753194 ["CALL", null, ["callee:0047ec3c:8"]]
- 00752de4 bytes ceaef497
+ 00753194 bytes aaaef497
- 00752ed4 ["INT_ADD", "register:40f0:8", ["const:752ed4:8", "const:4:8"]]
- 00752ed4 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00753284 ["INT_ADD", "register:40f0:8", ["const:753284:8", "const:4:8"]]
+ 00753284 ["CALL", null, ["callee:00c58ef0:8"]]
- 00752ed4 bytes 13141494
+ 00753284 bytes 1b171494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b2a9c2c46901188419e566125914b65"></a>

### [`00753368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753368.md) → [`00753718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753718.md) FUN_00753718

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0074c928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074c/0074c928.md) [`00789e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00789/00789e38.md) [`00b29a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29a84.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`0074ccd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074c/0074ccd8.md) [`0078a214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078a/0078a214.md) [`00b2aa78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2a/00b2aa78.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00753724",
      "incomplete_value": false,
      "site": "00753728",
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
      "definition_site": "00753374",
      "incomplete_value": false,
      "site": "00753378",
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
      "00753724",
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
      "00753724",
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

- 旧版 [`00753378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753368.md#insn-00753378) · [`00753370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753368.md#insn-00753370) · [`00753374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753368.md#insn-00753374)
- 新版 [`00753728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753718.md#insn-00753728) · [`00753720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753718.md#insn-00753720) · [`00753724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753718.md#insn-00753724)

~~~diff
- 00753378 ["INT_ADD", "register:40f0:8", ["const:753378:8", "const:4:8"]]
- 00753378 ["CALL", null, ["callee:0043bad8:8"]]
+ 00753728 ["INT_ADD", "register:40f0:8", ["const:753728:8", "const:4:8"]]
+ 00753728 ["CALL", null, ["callee:0043bad8:8"]]
- 00753378 bytes 10a1f397
+ 00753728 bytes eca0f397
- 00753370 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00753720 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00753370 bytes 20dbff90
+ 00753720 bytes 20dbffb0
- 00753374 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00753374 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00753374 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00753374 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00753724 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00753724 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00753724 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00753724 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00753374 bytes 00303e91
+ 00753724 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6cebdc42228e3398ab95d523f2c989f"></a>

### [`00753380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753380.md) → [`00753730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753730.md) FUN_00753730

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
      "definition_site": "00753744",
      "incomplete_value": false,
      "site": "00753748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00753394",
      "incomplete_value": false,
      "site": "00753398",
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
            "const:310:8"
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
      "00753748",
      "DATA",
      [
        "storage",
        "00c78310",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00753748",
      "DATA",
      [
        "storage",
        "00c792e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075338c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753380.md#insn-0075338c) · [`00753390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753380.md#insn-00753390) · [`00753394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753380.md#insn-00753394)
- 新版 [`0075373c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753730.md#insn-0075373c) · [`00753740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753730.md#insn-00753740) · [`00753744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753730.md#insn-00753744)

~~~diff
- 0075338c ["INT_ADD", "register:40f0:8", ["const:75338c:8", "const:4:8"]]
- 0075338c ["CALL", null, ["callee:00c58f30:8"]]
+ 0075373c ["INT_ADD", "register:40f0:8", ["const:75373c:8", "const:4:8"]]
+ 0075373c ["CALL", null, ["callee:00c58f30:8"]]
- 0075338c bytes f5121494
+ 0075373c bytes fd151494
- 00753390 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00753740 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00753390 bytes 282900b0
+ 00753740 bytes 282900d0
- 00753394 ["COPY", "tmp:0:8", ["const:310:8"]]
- 00753394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00753394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00753394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00753744 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 00753744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00753744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00753744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00753394 bytes 08410c91
+ 00753744 bytes 08810b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d5352ebfff17b1713b26d7ab4cd9bd9"></a>

### [`007533a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/007533a4.md) → [`00753754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753754.md) FUN_00753754

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
      "definition_site": "00753758",
      "incomplete_value": false,
      "site": "0075375c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007533a8",
      "incomplete_value": false,
      "site": "007533ac",
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
            "const:310:8"
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
      "0075375c",
      "DATA",
      [
        "storage",
        "00c78310",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075375c",
      "DATA",
      [
        "storage",
        "00c792e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007533a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/007533a4.md#insn-007533a4) · [`007533a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/007533a4.md#insn-007533a8)
- 新版 [`00753754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753754.md#insn-00753754) · [`00753758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753754.md#insn-00753758)

~~~diff
- 007533a4 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00753754 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 007533a4 bytes 282900b0
+ 00753754 bytes 282900d0
- 007533a8 ["COPY", "tmp:0:8", ["const:310:8"]]
- 007533a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007533a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007533a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00753758 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 00753758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00753758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00753758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007533a8 bytes 08410c91
+ 00753758 bytes 08810b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bcf0c8b3e12c008847a05f9d0589e44"></a>

### [`007533bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/007533bc.md) → [`0075376c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/0075376c.md) FUN_0075376c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0048dca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dca0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0048dfc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048dfc0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.06% / 新版 89.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007537f4",
      "incomplete_value": true,
      "site": "00753808",
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
                "const:dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00753444",
      "incomplete_value": true,
      "site": "00753458",
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
                "const:93:8"
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
      "definition_site": "0075380c",
      "incomplete_value": true,
      "site": "0075380c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075345c",
      "incomplete_value": true,
      "site": "0075345c",
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
                "const:e:8"
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
      "site": "007537a4",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007533f4",
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
      "007537a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007537e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "007537f4",
      "READ",
      [
        "storage",
        "002b2093",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007537a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "007537e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ],
    [
      "007537f4",
      "READ",
      [
        "storage",
        "002b20dd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007533f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/007533bc.md#insn-007533f4) · [`00753434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/007533bc.md#insn-00753434) · [`00753400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/007533bc.md#insn-00753400)
- 新版 [`007537a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/0075376c.md#insn-007537a4) · [`007537e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/0075376c.md#insn-007537e4) · [`007537b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/0075376c.md#insn-007537b0)

~~~diff
- 007533f4 ["INT_ADD", "register:40f0:8", ["const:7533f4:8", "const:4:8"]]
- 007533f4 ["CALL", null, ["ram:47ad34:8"]]
+ 007537a4 ["INT_ADD", "register:40f0:8", ["const:7537a4:8", "const:4:8"]]
+ 007537a4 ["CALL", null, ["ram:47b054:8"]]
- 007533f4 bytes 509ef497
+ 007537a4 bytes 2c9ef497
- 00753434 ["INT_ADD", "register:40f0:8", ["const:753434:8", "const:4:8"]]
- 00753434 ["CALL", null, ["ram:48cd38:8"]]
+ 007537e4 ["INT_ADD", "register:40f0:8", ["const:7537e4:8", "const:4:8"]]
+ 007537e4 ["CALL", null, ["ram:48d058:8"]]
- 00753434 bytes 41e6f497
+ 007537e4 bytes 1de6f497
- 00753400 ["INT_ADD", "register:40f0:8", ["const:753400:8", "const:4:8"]]
- 00753400 ["CALL", null, ["callee:0047d134:8"]]
+ 007537b0 ["INT_ADD", "register:40f0:8", ["const:7537b0:8", "const:4:8"]]
+ 007537b0 ["CALL", null, ["callee:0047d134:8"]]
- 00753400 bytes 85a6f497
+ 007537b0 bytes 61a6f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-718b947cddb767f88ecd80f7380798b2"></a>

### [`00753528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753528.md) → [`007538d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/007538d8.md) FUN_007538d8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0074fc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074f/0074fc38.md) [`00751008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00751/00751008.md) [`0077b364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077b364.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`007ef448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007ef448.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 7件 [`0074ffe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074f/0074ffe8.md) [`00751150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00751/00751150.md) [`0077b740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077b740.md) [`007e00a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007e0/007e00a4.md) [`007f03ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f0/007f03ac.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "007538e4",
      "incomplete_value": false,
      "site": "007538e8",
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
      "definition_site": "00753534",
      "incomplete_value": false,
      "site": "00753538",
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
      "007538e4",
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
      "007538e4",
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

- 旧版 [`00753538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753528.md#insn-00753538) · [`00753530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753528.md#insn-00753530) · [`00753534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753528.md#insn-00753534)
- 新版 [`007538e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/007538d8.md#insn-007538e8) · [`007538e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/007538d8.md#insn-007538e0) · [`007538e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/007538d8.md#insn-007538e4)

~~~diff
- 00753538 ["INT_ADD", "register:40f0:8", ["const:753538:8", "const:4:8"]]
- 00753538 ["CALL", null, ["callee:0043bad8:8"]]
+ 007538e8 ["INT_ADD", "register:40f0:8", ["const:7538e8:8", "const:4:8"]]
+ 007538e8 ["CALL", null, ["callee:0043bad8:8"]]
- 00753538 bytes a0a0f397
+ 007538e8 bytes 7ca0f397
- 00753530 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 007538e0 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00753530 bytes 20dbff90
+ 007538e0 bytes 20dbffb0
- 00753534 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00753534 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00753534 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00753534 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007538e4 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 007538e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007538e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007538e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00753534 bytes 00303e91
+ 007538e4 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-772b1764362cbf3c50f1700a7597292f"></a>

### [`0075353c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/0075353c.md) → [`007538ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/007538ec.md) _INIT_131

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
      "definition_site": "00753928",
      "incomplete_value": true,
      "site": "00753944",
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
      "definition_site": "00753578",
      "incomplete_value": true,
      "site": "00753594",
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
      "definition_site": "0075394c",
      "incomplete_value": true,
      "site": "00753968",
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
      "definition_site": "0075359c",
      "incomplete_value": true,
      "site": "007535b8",
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
      "definition_site": "0075396c",
      "incomplete_value": true,
      "site": "00753988",
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
      "definition_site": "007535bc",
      "incomplete_value": true,
      "site": "007535d8",
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
      "00753928",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0075394c",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0075396c",
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
      "00753928",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0075394c",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0075396c",
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

- 旧版 [`00753770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/0075353c.md#insn-00753770) · [`00753564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/0075353c.md#insn-00753564) · [`00753568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/0075353c.md#insn-00753568)
- 新版 [`00753b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/007538ec.md#insn-00753b20) · [`00753914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/007538ec.md#insn-00753914) · [`00753918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/007538ec.md#insn-00753918)

~~~diff
- 00753770 ["INT_ADD", "register:40f0:8", ["const:753770:8", "const:4:8"]]
- 00753770 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00753b20 ["INT_ADD", "register:40f0:8", ["const:753b20:8", "const:4:8"]]
+ 00753b20 ["CALL", null, ["callee:00c58ed0:8"]]
- 00753770 bytes e4111494
+ 00753b20 bytes ec141494
- 00753564 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 00753914 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 00753564 bytes b32a0090
+ 00753914 bytes b32a00b0
- 00753568 ["COPY", "tmp:0:8", ["const:ec0:8"]]
- 00753568 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00753568 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00753568 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00753918 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00753918 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00753918 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00753918 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00753568 bytes 73023b91
+ 00753918 bytes 73023a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e71199da62d2766e342b8590398494f6"></a>

### [`007538cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/007538cc.md) → [`00753c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753c7c.md) FUN_00753c7c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 16件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048a77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a77c.md) [`00754968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00754/00754968.md)
- 新版 呼出元 1件 [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) · 呼出先 16件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0048aa9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048aa9c.md) [`00754d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00754/00754d18.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 84.03% / 新版 84.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 19件, `call_target` 1件, `store_destination` 25件, `store_value` 9件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00753cc0",
      "incomplete_value": false,
      "site": "00753cc0",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00753910",
      "incomplete_value": false,
      "site": "00753910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00753cb8",
      "incomplete_value": true,
      "site": "00753cc0",
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
      "definition_site": "00753908",
      "incomplete_value": true,
      "site": "00753910",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00753cc4",
      "incomplete_value": false,
      "site": "00753cc4",
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
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00753914",
      "incomplete_value": false,
      "site": "00753914",
      "value": [
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
    },
    "ordinal": 14,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00753cb8",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00753cbc",
      "READ",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00753cc0",
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
      "00753cb8",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "00753cbc",
      "READ",
      [
        "storage",
        "00ca5a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00753cc0",
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

- 旧版 [`00753910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/007538cc.md#insn-00753910) · [`00753914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/007538cc.md#insn-00753914) · [`00753950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/007538cc.md#insn-00753950)
- 新版 [`00753cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753c7c.md#insn-00753cc0) · [`00753cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753c7c.md#insn-00753cc4) · [`00753d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753c7c.md#insn-00753d00)

~~~diff
- 00753910 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 00753910 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00753cc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a28:8"]]
+ 00753cc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00753910 bytes 093505f9
+ 00753cc0 bytes 091505f9
- 00753914 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 00753914 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00753cc4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a38:8"]]
+ 00753cc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00753914 bytes aa3e05f9
+ 00753cc4 bytes aa1e05f9
- 00753950 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 00753950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00753d00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a38:8"]]
+ 00753d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00753950 bytes b43e05f9
+ 00753d00 bytes b41e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aba62f0f29375359b12bd91093c5c1b1"></a>

### [`00754060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00754/00754060.md) → [`00754410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00754/00754410.md) FUN_00754410

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 8件 [`0046edcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046edcc.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00859ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859ba4.md)
- 新版 呼出元 1件 [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) · 呼出先 8件 [`0046f0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f0ec.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`0085ab50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085a/0085ab50.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.64% / 新版 97.64%

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
      "site": "00754468",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007540b8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0075458c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007541dc",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007545d8",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00754228",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 15,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00754468",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "0075458c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007545d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00754468",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "0075458c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "007545d8",
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

- 旧版 [`007540b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00754/00754060.md#insn-007540b8) · [`007541dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00754/00754060.md#insn-007541dc) · [`00754228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00754/00754060.md#insn-00754228)
- 新版 [`00754468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00754/00754410.md#insn-00754468) · [`0075458c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00754/00754410.md#insn-0075458c) · [`007545d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00754/00754410.md#insn-007545d8)

~~~diff
- 007540b8 ["INT_ADD", "register:40f0:8", ["const:7540b8:8", "const:4:8"]]
- 007540b8 ["CALL", null, ["ram:47ad34:8"]]
+ 00754468 ["INT_ADD", "register:40f0:8", ["const:754468:8", "const:4:8"]]
+ 00754468 ["CALL", null, ["ram:47b054:8"]]
- 007540b8 bytes 1f9bf497
+ 00754468 bytes fb9af497
- 007541dc ["INT_ADD", "register:40f0:8", ["const:7541dc:8", "const:4:8"]]
- 007541dc ["CALL", null, ["ram:47ad34:8"]]
+ 0075458c ["INT_ADD", "register:40f0:8", ["const:75458c:8", "const:4:8"]]
+ 0075458c ["CALL", null, ["ram:47b054:8"]]
- 007541dc bytes d69af497
+ 0075458c bytes b29af497
- 00754228 ["INT_ADD", "register:40f0:8", ["const:754228:8", "const:4:8"]]
- 00754228 ["CALL", null, ["ram:47ad34:8"]]
+ 007545d8 ["INT_ADD", "register:40f0:8", ["const:7545d8:8", "const:4:8"]]
+ 007545d8 ["CALL", null, ["ram:47b054:8"]]
- 00754228 bytes c39af497
+ 007545d8 bytes 9f9af497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af0c2997389fb3891171162a539689a6"></a>

### [`00754968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00754/00754968.md) → [`00754d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00754/00754d18.md) FUN_00754d18

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007538cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/007538cc.md) · 呼出先 16件 [`0047c9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c9a8.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md)
- 新版 呼出元 1件 [`00753c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753c7c.md) · 呼出先 16件 [`0047ccc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047c/0047ccc8.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00493168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493168.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.43% / 新版 87.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 36件, `call_target` 1件, `store_destination` 7件, `store_value` 15件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00754d5c",
      "incomplete_value": false,
      "site": "00754d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007549ac",
      "incomplete_value": false,
      "site": "007549b0",
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
            "const:3c0:8"
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
      "definition_site": "00755274",
      "incomplete_value": true,
      "site": "00755274",
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
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:f91:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00754ec4",
      "incomplete_value": true,
      "site": "00754ec4",
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
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:f47:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 66,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00755278",
      "incomplete_value": true,
      "site": "00755278",
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
      "definition_site": "00754ec8",
      "incomplete_value": true,
      "site": "00754ec8",
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
    "ordinal": 67,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00754d60",
      "DATA",
      [
        "storage",
        "00c783c0",
        null,
        "pointer"
      ]
    ],
    [
      "00754d74",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "00754d88",
      "READ",
      [
        "storage",
        "002bb5ce",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00754d60",
      "DATA",
      [
        "storage",
        "00c79390",
        null,
        "pointer"
      ]
    ],
    [
      "00754d74",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "00754d88",
      "READ",
      [
        "storage",
        "002bb6ac",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00754a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00754/00754968.md#insn-00754a88) · [`00754c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00754/00754968.md#insn-00754c38) · [`00754cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00754/00754968.md#insn-00754cd4)
- 新版 [`00754e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00754/00754d18.md#insn-00754e38) · [`00754fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00754/00754d18.md#insn-00754fe8) · [`00755084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00754/00754d18.md#insn-00755084)

~~~diff
- 00754a88 ["INT_ADD", "register:40f0:8", ["const:754a88:8", "const:4:8"]]
- 00754a88 ["CALL", null, ["callee:0047e96c:8"]]
+ 00754e38 ["INT_ADD", "register:40f0:8", ["const:754e38:8", "const:4:8"]]
+ 00754e38 ["CALL", null, ["callee:0047e96c:8"]]
- 00754a88 bytes f1a6f497
+ 00754e38 bytes cda6f497
- 00754c38 ["INT_ADD", "register:40f0:8", ["const:754c38:8", "const:4:8"]]
- 00754c38 ["CALL", null, ["callee:0047e96c:8"]]
+ 00754fe8 ["INT_ADD", "register:40f0:8", ["const:754fe8:8", "const:4:8"]]
+ 00754fe8 ["CALL", null, ["callee:0047e96c:8"]]
- 00754c38 bytes 85a6f497
+ 00754fe8 bytes 61a6f497
- 00754cd4 ["INT_ADD", "register:40f0:8", ["const:754cd4:8", "const:4:8"]]
- 00754cd4 ["CALL", null, ["ram:71d12c:8"]]
+ 00755084 ["INT_ADD", "register:40f0:8", ["const:755084:8", "const:4:8"]]
+ 00755084 ["CALL", null, ["ram:71d4dc:8"]]
- 00754cd4 bytes 1621ff97
+ 00755084 bytes 1621ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b8b43d699e1fbd71acadd616dd45480"></a>

### [`00755ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755ac0.md) → [`00755e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00755/00755e70.md) FUN_00755e70

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00755bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755bb8.md) · 呼出先 3件 [`00682364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00755f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00755/00755f68.md) · 呼出先 3件 [`00682714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00682/00682714.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00755e88",
      "incomplete_value": false,
      "site": "00755e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00755ad8",
      "incomplete_value": false,
      "site": "00755adc",
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
            "const:3c0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00755f24",
      "incomplete_value": false,
      "site": "00755f28",
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
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00755b74",
      "incomplete_value": false,
      "site": "00755b78",
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
            "const:8e0:8"
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
      "00755e8c",
      "DATA",
      [
        "storage",
        "00c783c0",
        null,
        "pointer"
      ]
    ],
    [
      "00755f28",
      "DATA",
      [
        "storage",
        "00c748e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00755e8c",
      "DATA",
      [
        "storage",
        "00c79390",
        null,
        "pointer"
      ]
    ],
    [
      "00755f28",
      "DATA",
      [
        "storage",
        "00c758b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00755ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755ac0.md#insn-00755ad4) · [`00755ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755ac0.md#insn-00755ad8) · [`00755aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755ac0.md#insn-00755aec)
- 新版 [`00755e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00755/00755e70.md#insn-00755e84) · [`00755e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00755/00755e70.md#insn-00755e88) · [`00755e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00755/00755e70.md#insn-00755e9c)

~~~diff
- 00755ad4 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00755e84 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00755ad4 bytes 082900f0
+ 00755e84 bytes 28290090
- 00755ad8 ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 00755ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00755ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00755ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00755e88 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 00755e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00755e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00755e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00755ad8 bytes 08010f91
+ 00755e88 bytes 08410e91
- 00755aec ["INT_ADD", "register:40f0:8", ["const:755aec:8", "const:4:8"]]
- 00755aec ["CALL", null, ["callee:00c54d90:8"]]
+ 00755e9c ["INT_ADD", "register:40f0:8", ["const:755e9c:8", "const:4:8"]]
+ 00755e9c ["CALL", null, ["callee:00c54d90:8"]]
- 00755aec bytes adf81394
+ 00755e9c bytes bdfb1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-048b759ed8f95444d485aecec1a6f929"></a>

### [`00755bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755bdc.md) → [`00755f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00755/00755f8c.md) _INIT_132

採用 · 移動量 `+0x3b0` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00755fc8",
      "incomplete_value": true,
      "site": "00755fe4",
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
      "definition_site": "00755c18",
      "incomplete_value": true,
      "site": "00755c34",
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
      "definition_site": "00755fec",
      "incomplete_value": true,
      "site": "00756008",
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
      "definition_site": "00755c3c",
      "incomplete_value": true,
      "site": "00755c58",
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
      "definition_site": "0075600c",
      "incomplete_value": true,
      "site": "00756028",
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
      "definition_site": "00755c5c",
      "incomplete_value": true,
      "site": "00755c78",
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
      "00755fc8",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00755fec",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0075600c",
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
      "00755fc8",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00755fec",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0075600c",
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

- 旧版 [`00755e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755bdc.md#insn-00755e10) · [`00755c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755bdc.md#insn-00755c04) · [`00755c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755bdc.md#insn-00755c08)
- 新版 [`007561c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00755/00755f8c.md#insn-007561c0) · [`00755fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00755/00755f8c.md#insn-00755fb4) · [`00755fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00755/00755f8c.md#insn-00755fb8)

~~~diff
- 00755e10 ["INT_ADD", "register:40f0:8", ["const:755e10:8", "const:4:8"]]
- 00755e10 ["CALL", null, ["callee:00c58ed0:8"]]
+ 007561c0 ["INT_ADD", "register:40f0:8", ["const:7561c0:8", "const:4:8"]]
+ 007561c0 ["CALL", null, ["callee:00c58ed0:8"]]
- 00755e10 bytes 3c081494
+ 007561c0 bytes 440b1494
- 00755c04 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 00755fb4 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 00755c04 bytes 932a00d0
+ 00755fb4 bytes 932a00f0
- 00755c08 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 00755c08 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00755c08 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00755c08 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00755fb8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00755fb8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00755fb8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00755fb8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00755c08 bytes 73623b91
+ 00755fb8 bytes 73623a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ba12112727b16dbf2ceb53d62d7a768"></a>

### [`00755f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755f6c.md) → [`0075631c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00756/0075631c.md) _INIT_133

採用 · 移動量 `+0x3b0` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0075639c",
      "incomplete_value": true,
      "site": "007563b8",
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
      "definition_site": "00755fec",
      "incomplete_value": true,
      "site": "00756008",
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
      "definition_site": "007563d8",
      "incomplete_value": true,
      "site": "007563f4",
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
      "definition_site": "00756028",
      "incomplete_value": true,
      "site": "00756044",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007563f8",
      "incomplete_value": true,
      "site": "00756414",
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
      "definition_site": "00756048",
      "incomplete_value": true,
      "site": "00756064",
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
      "00756358",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0075637c",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0075639c",
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
      "00756358",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0075637c",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0075639c",
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

- 旧版 [`007561a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755f6c.md#insn-007561a0) · [`00755f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755f6c.md#insn-00755f94) · [`00755f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755f6c.md#insn-00755f98)
- 新版 [`00756550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00756/0075631c.md#insn-00756550) · [`00756344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00756/0075631c.md#insn-00756344) · [`00756348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00756/0075631c.md#insn-00756348)

~~~diff
- 007561a0 ["INT_ADD", "register:40f0:8", ["const:7561a0:8", "const:4:8"]]
- 007561a0 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00756550 ["INT_ADD", "register:40f0:8", ["const:756550:8", "const:4:8"]]
+ 00756550 ["CALL", null, ["callee:00c58ed0:8"]]
- 007561a0 bytes 58071494
+ 00756550 bytes 600a1494
- 00755f94 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 00756344 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 00755f94 bytes 932a00d0
+ 00756344 bytes 932a00d0
- 00755f98 ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 00755f98 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00755f98 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00755f98 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00756348 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 00756348 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00756348 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00756348 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00755f98 bytes 73c23b91
+ 00756348 bytes 73c23a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab797646a12fc577948f27bb8d01bea5"></a>

### [`00758228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758228.md) → [`007585d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/007585d8.md) FUN_007585d8

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`007562fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00756/007562fc.md) [`007b0a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0a70.md) [`008bc920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc920.md) [`008e0c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0c84.md) [`008faedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008faedc.md) · 呼出先 10件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0067e1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e1dc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 7件 [`007566ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00756/007566ac.md) [`007b19d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007b1/007b19d4.md) [`008bd8cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd8cc.md) [`008e1c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1c30.md) [`008fbe88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fb/008fbe88.md) · 呼出先 10件 [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0067e58c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0067e/0067e58c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 74.56% / 新版 74.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00758608",
      "incomplete_value": false,
      "site": "0075860c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758258",
      "incomplete_value": false,
      "site": "0075825c",
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
            "const:400:8"
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
      "definition_site": "0075864c",
      "incomplete_value": true,
      "site": "0075864c",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:475:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075829c",
      "incomplete_value": true,
      "site": "0075829c",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:435:8"
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
      "definition_site": "00758664",
      "incomplete_value": true,
      "site": "00758664",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:368:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007582b4",
      "incomplete_value": true,
      "site": "007582b4",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:31e:8"
              ]
            ]
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
      "0075860c",
      "DATA",
      [
        "storage",
        "00c78400",
        null,
        "pointer"
      ]
    ],
    [
      "0075861c",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "0075863c",
      "READ",
      [
        "storage",
        "002a1435",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0075860c",
      "DATA",
      [
        "storage",
        "00c793d0",
        null,
        "pointer"
      ]
    ],
    [
      "0075861c",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "0075863c",
      "READ",
      [
        "storage",
        "002a1475",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007582d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758228.md#insn-007582d4) · [`0075839c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758228.md#insn-0075839c) · [`007583d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758228.md#insn-007583d8)
- 新版 [`00758684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/007585d8.md#insn-00758684) · [`0075874c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/007585d8.md#insn-0075874c) · [`00758788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/007585d8.md#insn-00758788)

~~~diff
- 007582d4 ["INT_ADD", "register:40f0:8", ["const:7582d4:8", "const:4:8"]]
- 007582d4 ["CALL", null, ["callee:0047e96c:8"]]
+ 00758684 ["INT_ADD", "register:40f0:8", ["const:758684:8", "const:4:8"]]
+ 00758684 ["CALL", null, ["callee:0047e96c:8"]]
- 007582d4 bytes de98f497
+ 00758684 bytes ba98f497
- 0075839c ["INT_ADD", "register:40f0:8", ["const:75839c:8", "const:4:8"]]
- 0075839c ["CALL", null, ["callee:00c58ef0:8"]]
+ 0075874c ["INT_ADD", "register:40f0:8", ["const:75874c:8", "const:4:8"]]
+ 0075874c ["CALL", null, ["callee:00c58ef0:8"]]
- 0075839c bytes e1fe1394
+ 0075874c bytes e9011494
- 007583d8 ["INT_ADD", "register:40f0:8", ["const:7583d8:8", "const:4:8"]]
- 007583d8 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00758788 ["INT_ADD", "register:40f0:8", ["const:758788:8", "const:4:8"]]
+ 00758788 ["CALL", null, ["callee:00c58ed0:8"]]
- 007583d8 bytes cafe1394
+ 00758788 bytes d2011494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f52308df0dd5d3548622352733cb35e"></a>

### [`00758898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758898.md) → [`00758c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/00758c48.md) FUN_00758c48

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`0062e1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062e/0062e1e0.md) [`00677a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00677/00677a80.md) [`0067a3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067a/0067a3e4.md) [`0092491c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00924/0092491c.md) [`009be458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009be/009be458.md) · 呼出先 21件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md) [`0046f724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f724.md)
- 新版 呼出元 7件 [`0062e590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062e/0062e590.md) [`00677e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00677/00677e30.md) [`0067a794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0067a/0067a794.md) [`009258c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00925/009258c8.md) [`009bf404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009bf/009bf404.md) · 呼出先 21件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0046ecd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ecd0.md) [`0046f414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f414.md) [`0046fa44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046fa44.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.74% / 新版 92.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00758f08",
      "incomplete_value": true,
      "site": "00758f18",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:9d6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758b58",
      "incomplete_value": true,
      "site": "00758b68",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:87e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00759004",
      "incomplete_value": true,
      "site": "00759014",
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
                "const:6f1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758c54",
      "incomplete_value": true,
      "site": "00758c64",
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
                "const:626:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0075908c",
      "incomplete_value": true,
      "site": "007590a0",
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
                "const:bac:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758cdc",
      "incomplete_value": true,
      "site": "00758cf0",
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
                "const:adf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 69,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00758ca8",
      "PARAM",
      [
        "storage",
        "002b6490",
        null,
        "string"
      ]
    ],
    [
      "00758cb8",
      "PARAM",
      [
        "storage",
        "002b3fa8",
        null,
        null
      ]
    ],
    [
      "00758dec",
      "READ",
      [
        "storage",
        "002afd81",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00758ca8",
      "PARAM",
      [
        "storage",
        "002b655f",
        null,
        "string"
      ]
    ],
    [
      "00758cb8",
      "PARAM",
      [
        "storage",
        "002b4086",
        null,
        null
      ]
    ],
    [
      "00758dec",
      "READ",
      [
        "storage",
        "002afe58",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758898.md#insn-00758900) · [`00758910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758898.md#insn-00758910) · [`00758bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758898.md#insn-00758bb8)
- 新版 [`00758cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/00758c48.md#insn-00758cb0) · [`00758cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/00758c48.md#insn-00758cc0) · [`00758f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/00758c48.md#insn-00758f68)

~~~diff
- 00758900 ["INT_ADD", "register:40f0:8", ["const:758900:8", "const:4:8"]]
- 00758900 ["CALL", null, ["callee:00c59230:8"]]
+ 00758cb0 ["INT_ADD", "register:40f0:8", ["const:758cb0:8", "const:4:8"]]
+ 00758cb0 ["CALL", null, ["callee:00c59230:8"]]
- 00758900 bytes 58fe1394
+ 00758cb0 bytes 60011494
- 00758910 ["INT_ADD", "register:40f0:8", ["const:758910:8", "const:4:8"]]
- 00758910 ["CALL", null, ["callee:00c59230:8"]]
+ 00758cc0 ["INT_ADD", "register:40f0:8", ["const:758cc0:8", "const:4:8"]]
+ 00758cc0 ["CALL", null, ["callee:00c59230:8"]]
- 00758910 bytes 54fe1394
+ 00758cc0 bytes 5c011494
- 00758bb8 ["INT_ADD", "register:40f0:8", ["const:758bb8:8", "const:4:8"]]
- 00758bb8 ["CALL", null, ["callee:0047e96c:8"]]
+ 00758f68 ["INT_ADD", "register:40f0:8", ["const:758f68:8", "const:4:8"]]
+ 00758f68 ["CALL", null, ["callee:0047e96c:8"]]
- 00758bb8 bytes a596f497
+ 00758f68 bytes 8196f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-265e72cf7bf09c413e2a1423a0002973"></a>

### [`0075ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075ba1c.md) → [`0075bdcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075b/0075bdcc.md) FUN_0075bdcc

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0075d7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d7b4.md) · 呼出先 32件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00604dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00604/00604dd0.md) [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md) [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md)
- 新版 呼出元 1件 [`0075db64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075db64.md) · 呼出先 32件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`00605180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00605/00605180.md) [`0071c2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c2e0.md) [`0071c868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c868.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.61% / 新版 97.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_destination` 2件, `store_value` 13件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075bee4",
      "incomplete_value": false,
      "site": "0075beec",
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
      "definition_site": "0075bb34",
      "incomplete_value": false,
      "site": "0075bb3c",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075bf0c",
      "incomplete_value": false,
      "site": "0075bf18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075bb5c",
      "incomplete_value": false,
      "site": "0075bb68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:f1e:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075bf3c",
      "incomplete_value": false,
      "site": "0075bf44",
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
      "definition_site": "0075bb8c",
      "incomplete_value": false,
      "site": "0075bb94",
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
    "ordinal": 23,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0075be24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d12c"
      ]
    ],
    [
      "0075be4c",
      "DATA",
      [
        "storage",
        "003965b0",
        null,
        "dword"
      ]
    ],
    [
      "0075be54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ]
  ],
  "added": [
    [
      "0075be24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d4dc"
      ]
    ],
    [
      "0075be4c",
      "DATA",
      [
        "storage",
        "003965b0",
        null,
        "qword"
      ]
    ],
    [
      "0075be54",
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

- 旧版 [`0075ba74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075ba1c.md#insn-0075ba74) · [`0075baa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075ba1c.md#insn-0075baa4) · [`0075d20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075ba1c.md#insn-0075d20c)
- 新版 [`0075be24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075b/0075bdcc.md#insn-0075be24) · [`0075be54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075b/0075bdcc.md#insn-0075be54) · [`0075d5bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075b/0075bdcc.md#insn-0075d5bc)

~~~diff
- 0075ba74 ["INT_ADD", "register:40f0:8", ["const:75ba74:8", "const:4:8"]]
- 0075ba74 ["CALL", null, ["ram:71d12c:8"]]
+ 0075be24 ["INT_ADD", "register:40f0:8", ["const:75be24:8", "const:4:8"]]
+ 0075be24 ["CALL", null, ["ram:71d4dc:8"]]
- 0075ba74 bytes ae05ff97
+ 0075be24 bytes ae05ff97
- 0075baa4 ["INT_ADD", "register:40f0:8", ["const:75baa4:8", "const:4:8"]]
- 0075baa4 ["CALL", null, ["ram:71bf30:8"]]
+ 0075be54 ["INT_ADD", "register:40f0:8", ["const:75be54:8", "const:4:8"]]
+ 0075be54 ["CALL", null, ["ram:71c2e0:8"]]
- 0075baa4 bytes 2301ff97
+ 0075be54 bytes 2301ff97
- 0075d20c ["INT_ADD", "register:40f0:8", ["const:75d20c:8", "const:4:8"]]
- 0075d20c ["CALL", null, ["callee:00a388c4:8"]]
+ 0075d5bc ["INT_ADD", "register:40f0:8", ["const:75d5bc:8", "const:4:8"]]
+ 0075d5bc ["CALL", null, ["callee:00a388c4:8"]]
- 0075d20c bytes b1690b94
+ 0075d5bc bytes c26c0b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84aa11c4c221f80c18721b9ac16534d7"></a>

### [`0075e5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075e5e0.md) → [`0075e990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075e990.md) FUN_0075e990

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0075d7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d7b4.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 14件 [`0044eae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044eae0.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`0059769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059769c.md)
- 新版 呼出元 2件 [`0075db64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075db64.md) [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 14件 [`0044ee00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044e/0044ee00.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`005979bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979bc.md)

変更の種類 call, call_target, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 86.01% / 新版 86.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 3件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0075e9dc",
      "incomplete_value": true,
      "site": "0075e9e4",
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
                "const:ae0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075e62c",
      "incomplete_value": true,
      "site": "0075e634",
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
                "const:a90:8"
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
      "definition_site": "0075e9d8",
      "incomplete_value": true,
      "site": "0075e9e8",
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075e628",
      "incomplete_value": true,
      "site": "0075e638",
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
                "const:80:8"
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
      "definition_site": "0075e9d8",
      "incomplete_value": true,
      "site": "0075e9e8",
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
      "definition_site": "0075e628",
      "incomplete_value": true,
      "site": "0075e638",
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
      "0075e9d8",
      "READ",
      [
        "storage",
        "002b402c",
        null,
        "string"
      ]
    ],
    [
      "0075e9d8",
      "READ",
      [
        "storage",
        "002b403c",
        null,
        "string"
      ]
    ],
    [
      "0075e9dc",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0075e9d8",
      "READ",
      [
        "storage",
        "002b410a",
        null,
        "string"
      ]
    ],
    [
      "0075e9d8",
      "READ",
      [
        "storage",
        "002b411a",
        null,
        "string"
      ]
    ],
    [
      "0075e9dc",
      "READ",
      [
        "storage",
        "002c2ae0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075e644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075e5e0.md#insn-0075e644) · [`0075e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075e5e0.md#insn-0075e64c) · [`0075e654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075e5e0.md#insn-0075e654)

~~~diff
- 0075e644 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:9d:8"]]
- 0075e644 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0075e644 bytes 00d0893c
- 0075e64c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:40:8"]]
- 0075e64c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 0075e64c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 0075e64c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 0075e64c bytes 010002ad
- 0075e654 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:60:8"]]
- 0075e654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0075e654 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 0075e654 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5040:16"]]
- 0075e654 bytes 000803ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60b1363c0c8f6c22dff6d92fbe4e9e05"></a>

### [`0075ea9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ea9c.md) → [`0075ee4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ee4c.md) FUN_0075ee4c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 6件 [`00728d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00728/00728d40.md) [`00728e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00728/00728e44.md) [`00729044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00729/00729044.md) [`00729160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00729/00729160.md) [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md)
- 新版 呼出元 1件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 6件 [`007290f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00729/007290f0.md) [`007291f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00729/007291f4.md) [`007293f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00729/007293f4.md) [`00729510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00729/00729510.md) [`00801334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00801/00801334.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.73% / 新版 98.73%

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
      "site": "0075eea8",
      "value": [
        "leaf",
        "ram:7291f4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0075eaf8",
      "value": [
        "leaf",
        "ram:728e44:8"
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
      "0075eea8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00728e44"
      ]
    ]
  ],
  "added": [
    [
      "0075eea8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007291f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075eaf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ea9c.md#insn-0075eaf8) · [`0075eac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ea9c.md#insn-0075eac0) · [`0075eae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ea9c.md#insn-0075eae4)
- 新版 [`0075eea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ee4c.md#insn-0075eea8) · [`0075ee70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ee4c.md#insn-0075ee70) · [`0075ee94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ee4c.md#insn-0075ee94)

~~~diff
- 0075eaf8 ["INT_ADD", "register:40f0:8", ["const:75eaf8:8", "const:4:8"]]
- 0075eaf8 ["CALL", null, ["ram:728e44:8"]]
+ 0075eea8 ["INT_ADD", "register:40f0:8", ["const:75eea8:8", "const:4:8"]]
+ 0075eea8 ["CALL", null, ["ram:7291f4:8"]]
- 0075eaf8 bytes d328ff97
+ 0075eea8 bytes d328ff97
- 0075eac0 ["INT_ADD", "register:40f0:8", ["const:75eac0:8", "const:4:8"]]
- 0075eac0 ["CALL", null, ["callee:0085e4f8:8"]]
+ 0075ee70 ["INT_ADD", "register:40f0:8", ["const:75ee70:8", "const:4:8"]]
+ 0075ee70 ["CALL", null, ["callee:0085e4f8:8"]]
- 0075eac0 bytes a3fa0394
+ 0075ee70 bytes a2fd0394
- 0075eae4 ["INT_ADD", "register:40f0:8", ["const:75eae4:8", "const:4:8"]]
- 0075eae4 ["CALL", null, ["callee:007290f0:8"]]
+ 0075ee94 ["INT_ADD", "register:40f0:8", ["const:75ee94:8", "const:4:8"]]
+ 0075ee94 ["CALL", null, ["callee:007290f0:8"]]
- 0075eae4 bytes 9728ff97
+ 0075ee94 bytes 9728ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dff5d00f6e65bc77e4d0f9b2f60b3ad"></a>

### [`00764148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764148.md) → [`00764524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764524.md) FUN_00764524

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`00793960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00793/00793960.md) · 呼出先 9件 [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0072ad78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072a/0072ad78.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 2件 [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) [`00793d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/00793d3c.md) · 呼出先 9件 [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0072b128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0072b/0072b128.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.09% / 新版 89.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00764754",
      "incomplete_value": false,
      "site": "00764754",
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
      "definition_site": "00764378",
      "incomplete_value": false,
      "site": "00764378",
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
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00764758",
      "incomplete_value": false,
      "site": "00764758",
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
      "definition_site": "0076437c",
      "incomplete_value": false,
      "site": "0076437c",
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
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00764754",
      "incomplete_value": false,
      "site": "00764758",
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
      "definition_site": "00764378",
      "incomplete_value": false,
      "site": "0076437c",
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
      "00764618",
      "READ",
      [
        "storage",
        "00c9ad70",
        null,
        "pointer"
      ]
    ],
    [
      "0076466c",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "00764680",
      "PARAM",
      [
        "storage",
        "00ca5000",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00764618",
      "READ",
      [
        "storage",
        "00c9bd40",
        null,
        "pointer"
      ]
    ],
    [
      "0076466c",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "00764680",
      "PARAM",
      [
        "storage",
        "00ca5fc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007642cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764148.md#insn-007642cc) · [`00764354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764148.md#insn-00764354) · [`00764390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764148.md#insn-00764390)
- 新版 [`007646a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764524.md#insn-007646a8) · [`00764730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764524.md#insn-00764730) · [`0076476c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764524.md#insn-0076476c)

~~~diff
- 007642cc ["INT_ADD", "register:40f0:8", ["const:7642cc:8", "const:4:8"]]
- 007642cc ["CALL", null, ["callee:0047ec3c:8"]]
+ 007646a8 ["INT_ADD", "register:40f0:8", ["const:7646a8:8", "const:4:8"]]
+ 007646a8 ["CALL", null, ["callee:0047ec3c:8"]]
- 007642cc bytes 9469f497
+ 007646a8 bytes 6569f497
- 00764354 ["INT_ADD", "register:40f0:8", ["const:764354:8", "const:4:8"]]
- 00764354 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00764730 ["INT_ADD", "register:40f0:8", ["const:764730:8", "const:4:8"]]
+ 00764730 ["CALL", null, ["callee:00c58ef0:8"]]
- 00764354 bytes f3ce1394
+ 00764730 bytes f0d11394
- 00764390 ["INT_ADD", "register:40f0:8", ["const:764390:8", "const:4:8"]]
- 00764390 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0076476c ["INT_ADD", "register:40f0:8", ["const:76476c:8", "const:4:8"]]
+ 0076476c ["CALL", null, ["callee:00c58ed0:8"]]
- 00764390 bytes dcce1394
+ 0076476c bytes d9d11394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c913313974adf1e3158c4c2e14229ff1"></a>

### [`0076442c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/0076442c.md) → [`00764808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764808.md) FUN_00764808

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 1件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0076487c",
      "incomplete_value": false,
      "site": "00764880",
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
      "definition_site": "007644a0",
      "incomplete_value": false,
      "site": "007644a4",
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
      "0076487c",
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
      "0076487c",
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

- 旧版 [`007644a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/0076442c.md#insn-007644a4) · [`007644a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/0076442c.md#insn-007644a0)
- 新版 [`00764880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764808.md#insn-00764880) · [`0076487c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764808.md#insn-0076487c)

~~~diff
- 007644a4 ["INT_ADD", "register:40f0:8", ["const:7644a4:8", "const:4:8"]]
- 007644a4 ["CALL", null, ["callee:00442c90:8"]]
+ 00764880 ["INT_ADD", "register:40f0:8", ["const:764880:8", "const:4:8"]]
+ 00764880 ["CALL", null, ["callee:00442c90:8"]]
- 007644a4 bytes 3379f397
+ 00764880 bytes 0479f397
- 007644a0 ["COPY", "tmp:0:8", ["const:170:8"]]
- 007644a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007644a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007644a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0076487c ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 0076487c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0076487c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0076487c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007644a0 bytes 00c00591
+ 0076487c bytes 00c00691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f5be959a18ceff08e36304630129350"></a>

### [`007644b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007644b4.md) → [`00764890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764890.md) FUN_00764890

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 1件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00764904",
      "incomplete_value": false,
      "site": "00764908",
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
      "definition_site": "00764528",
      "incomplete_value": false,
      "site": "0076452c",
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
      "00764904",
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
      "00764904",
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

- 旧版 [`0076452c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007644b4.md#insn-0076452c) · [`00764528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007644b4.md#insn-00764528)
- 新版 [`00764908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764890.md#insn-00764908) · [`00764904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764890.md#insn-00764904)

~~~diff
- 0076452c ["INT_ADD", "register:40f0:8", ["const:76452c:8", "const:4:8"]]
- 0076452c ["CALL", null, ["callee:00442c90:8"]]
+ 00764908 ["INT_ADD", "register:40f0:8", ["const:764908:8", "const:4:8"]]
+ 00764908 ["CALL", null, ["callee:00442c90:8"]]
- 0076452c bytes 1179f397
+ 00764908 bytes e278f397
- 00764528 ["COPY", "tmp:0:8", ["const:170:8"]]
- 00764528 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00764528 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00764528 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00764904 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 00764904 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00764904 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00764904 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00764528 bytes 00c00591
+ 00764904 bytes 00c00691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e42b9871ec8dad42f370613c1321e9e"></a>

### [`0076453c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/0076453c.md) → [`00764918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764918.md) FUN_00764918

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`00a8a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) · 呼出先 23件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md) [`009a9354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a9354.md) [`009a97bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a97bc.md) [`009aae10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aae10.md)
- 新版 呼出元 2件 [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) [`00a8b47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a8b/00a8b47c.md) · 呼出先 23件 [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`00801334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00801/00801334.md) [`009aa300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa300.md) [`009aa768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa768.md) [`009abdbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abdbc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 68.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00764700",
      "incomplete_value": true,
      "site": "00764708",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 25,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00764708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/0076453c.md#insn-00764708) · [`00764570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/0076453c.md#insn-00764570) · [`00764578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/0076453c.md#insn-00764578)
- 新版 [`00764ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764918.md#insn-00764ae4) · [`0076494c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764918.md#insn-0076494c) · [`00764954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764918.md#insn-00764954)

~~~diff
- 00764708 ["INT_ADD", "register:40f0:8", ["const:764708:8", "const:4:8"]]
- 00764708 ["CALL", null, ["callee:00c58f50:8"]]
+ 00764ae4 ["INT_ADD", "register:40f0:8", ["const:764ae4:8", "const:4:8"]]
+ 00764ae4 ["CALL", null, ["callee:00c58f50:8"]]
- 00764708 bytes 1ece1394
+ 00764ae4 bytes 1bd11394
- 00764570 ["INT_ADD", "register:40f0:8", ["const:764570:8", "const:4:8"]]
- 00764570 ["CALL", null, ["callee:0048d1e4:8"]]
+ 0076494c ["INT_ADD", "register:40f0:8", ["const:76494c:8", "const:4:8"]]
+ 0076494c ["CALL", null, ["callee:0048d1e4:8"]]
- 00764570 bytes 55a2f497
+ 0076494c bytes 26a2f497
- 00764578 ["INT_ADD", "register:40f0:8", ["const:764578:8", "const:4:8"]]
- 00764578 ["CALL", null, ["callee:00a36be0:8"]]
+ 00764954 ["INT_ADD", "register:40f0:8", ["const:764954:8", "const:4:8"]]
+ 00764954 ["CALL", null, ["callee:00a36be0:8"]]
- 00764578 bytes 9d450b94
+ 00764954 bytes a3480b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f37e4f22bafd2e7c6b8b02531f65e74f"></a>

### [`007647c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007647c8.md) → [`00764ba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764ba4.md) FUN_00764ba4

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00736074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00736/00736074.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) [`0089b2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089b2e4.md) [`008d9c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9c58.md) · 呼出先 16件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00652da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652da0.md) [`00733734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00733/00733734.md)
- 新版 呼出元 5件 [`00736424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00736/00736424.md) [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) [`0089c290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089c290.md) [`008dac04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008dac04.md) · 呼出先 16件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`00653150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653150.md) [`00733ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00733/00733ae4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.41% / 新版 93.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00764cc4",
      "incomplete_value": true,
      "site": "00764ce8",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:b6d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007648e8",
      "incomplete_value": true,
      "site": "0076490c",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:a15:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00764c30",
      "incomplete_value": true,
      "site": "00764c30",
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
      "definition_site": "00764854",
      "incomplete_value": true,
      "site": "00764854",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00764c38",
      "incomplete_value": false,
      "site": "00764c48",
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
      "definition_site": "0076485c",
      "incomplete_value": false,
      "site": "0076486c",
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
      "00764c2c",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00764c38",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00764c40",
      "PARAM",
      [
        "storage",
        "00c77ad8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00764c2c",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "00764c38",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00764c40",
      "PARAM",
      [
        "storage",
        "00c78aa8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076486c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007647c8.md#insn-0076486c) · [`00764a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007647c8.md#insn-00764a88) · [`00764804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007647c8.md#insn-00764804)
- 新版 [`00764c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764ba4.md#insn-00764c48) · [`00764e64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764ba4.md#insn-00764e64) · [`00764be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764ba4.md#insn-00764be0)

~~~diff
- 0076486c ["INT_ADD", "register:40f0:8", ["const:76486c:8", "const:4:8"]]
- 0076486c ["CALL", null, ["callee:00c596b0:8"]]
+ 00764c48 ["INT_ADD", "register:40f0:8", ["const:764c48:8", "const:4:8"]]
+ 00764c48 ["CALL", null, ["callee:00c596b0:8"]]
- 0076486c bytes 9dcf1394
+ 00764c48 bytes 9ad21394
- 00764a88 ["INT_ADD", "register:40f0:8", ["const:764a88:8", "const:4:8"]]
- 00764a88 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00764e64 ["INT_ADD", "register:40f0:8", ["const:764e64:8", "const:4:8"]]
+ 00764e64 ["CALL", null, ["callee:00c58ed0:8"]]
- 00764a88 bytes 1ecd1394
+ 00764e64 bytes 1bd01394
- 00764804 ["INT_ADD", "register:40f0:8", ["const:764804:8", "const:4:8"]]
- 00764804 ["CALL", null, ["callee:0073771c:8"]]
+ 00764be0 ["INT_ADD", "register:40f0:8", ["const:764be0:8", "const:4:8"]]
+ 00764be0 ["CALL", null, ["callee:0073771c:8"]]
- 00764804 bytes da4aff97
+ 00764be0 bytes cf4aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64dede19c9e1c0d5924ded361427e141"></a>

### [`00764c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764c84.md) → [`00765060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765060.md) FUN_00765060

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`007662b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/007662b4.md) [`007671a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/007671a0.md) [`00767dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767dfc.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 2件 [`00b2f88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2f88c.md) [`00b2f91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2f91c.md)
- 新版 呼出元 7件 [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) [`00766690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00766/00766690.md) [`0076757c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00767/0076757c.md) [`007681d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007681d8.md) [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 2件 [`00b30880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30880.md) [`00b30910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30910.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate, store_destination

命令の説明率　旧版 99.42% / 新版 99.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "007650ac",
      "incomplete_value": true,
      "site": "007650ac",
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
            "const:f3c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00764cd0",
      "incomplete_value": true,
      "site": "00764cd0",
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
            "const:f6c:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007652e4",
      "incomplete_value": false,
      "site": "007652e4",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00764f08",
      "incomplete_value": false,
      "site": "00764f08",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0076530c",
      "incomplete_value": true,
      "site": "00765310",
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
    "old": {
      "definition_site": "00764f30",
      "incomplete_value": true,
      "site": "00764f34",
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
      "00765064",
      "READ",
      [
        "storage",
        "00ca3f6c",
        null,
        "undefined1"
      ]
    ],
    [
      "007650ac",
      "WRITE",
      [
        "storage",
        "00ca3f6c",
        null,
        "undefined1"
      ]
    ],
    [
      "007652e4",
      "WRITE",
      [
        "storage",
        "00ca7f20",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00765064",
      "READ",
      [
        "storage",
        "00ca4f3c",
        null,
        "undefined1"
      ]
    ],
    [
      "007650ac",
      "WRITE",
      [
        "storage",
        "00ca4f3c",
        null,
        "undefined1"
      ]
    ],
    [
      "007652e4",
      "WRITE",
      [
        "storage",
        "00ca8ee0",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00764cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764c84.md#insn-00764cd0) · [`00764f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764c84.md#insn-00764f08) · [`00764c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764c84.md#insn-00764c84)
- 新版 [`007650ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765060.md#insn-007650ac) · [`007652e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765060.md#insn-007652e4) · [`00765060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765060.md#insn-00765060)

~~~diff
- 00764cd0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00764cd0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00764cd0 ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:f6c:8"]]
- 00764cd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 007650ac ["COPY", "tmp:0:4", ["const:0:4"]]
+ 007650ac ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 007650ac ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:f3c:8"]]
+ 007650ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00764cd0 bytes 1fb13d39
+ 007650ac bytes 1ff13c39
- 00764f08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
- 00764f08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 007652e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
+ 007652e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 00764f08 bytes 00210fb9
+ 007652e4 bytes 00e10eb9
- 00764c84 ["COPY", "register:4040:8", ["const:ca3000:8"]]
+ 00765060 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00764c84 bytes e82900f0
+ 00765060 bytes e82900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aecbd82c66d2d2a594999c251c43768"></a>

### [`00765180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765180.md) → [`0076555c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/0076555c.md) FUN_0076555c

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`007662b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/007662b4.md) [`007671a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/007671a0.md) · 呼出先 21件 [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md) [`0055ea08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ea08.md)
- 新版 呼出元 2件 [`00766690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00766/00766690.md) [`0076757c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00767/0076757c.md) · 呼出先 21件 [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00451afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451afc.md) [`00451d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451d38.md) [`0055ed28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055e/0055ed28.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.20% / 新版 86.20%

CFGの説明率　旧版 39.47% / 新版 38.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 2件, `store_value` 6件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007651d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007651dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00765680",
      "incomplete_value": true,
      "site": "00765684",
      "value": [
        "INT_ADD",
        "8",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007652a4",
      "incomplete_value": true,
      "site": "007652a8",
      "value": [
        "INT_ADD",
        "8",
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
            "const:40:8"
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
      "unmatched:007651c4",
      "READ",
      [
        "storage",
        "002afd8f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:007651d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x250]",
        null,
        null
      ]
    ],
    [
      "unmatched:007651dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x17f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007655a0",
      "READ",
      [
        "storage",
        "002afe66",
        null,
        "string"
      ]
    ],
    [
      "007655b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x250]",
        null,
        null
      ]
    ],
    [
      "007655b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x17f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007651d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765180.md#insn-007651d8) · [`007651dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765180.md#insn-007651dc) · [`007651f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765180.md#insn-007651f8)

~~~diff
- 007651d8 ["COPY", "tmp:0:8", ["register:8:8"]]
- 007651d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 007651d8 bytes e003803d
- 007651dc ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:1:8"]]
- 007651dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 007651dc bytes 8013803c
- 007651f8 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 007651f8 bytes 40150054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ef26e78c60e6d309a3dc1682dda1b24"></a>

### [`00765780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765780.md) → [`00765b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765b5c.md) FUN_00765b5c

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00765e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765e74.md) · 呼出先 22件 [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md) [`0055ea08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ea08.md) [`00560498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560498.md)
- 新版 呼出元 1件 [`00766250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00766/00766250.md) · 呼出先 22件 [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00451d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451d38.md) [`0055ed28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055e/0055ed28.md) [`005607b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/005607b8.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.50% / 新版 88.50%

CFGの説明率　旧版 81.65% / 新版 83.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 1件, `store_value` 6件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00765780"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00765780"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00765784"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00765780",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00765784",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00765788",
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
      "00765b5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00765b60",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00765b64",
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

- 旧版 [`00765780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765780.md#insn-00765780) · [`00765784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765780.md#insn-00765784) · [`00765788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765780.md#insn-00765788)

~~~diff
- 00765780 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00765780 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00765780 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00765780 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00765780 bytes fd7bbaa9
- 00765784 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00765784 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00765784 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00765784 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00765784 bytes fc6f01a9
- 00765788 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00765788 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00765788 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00765788 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00765788 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-869364e5583e38021752478a97b4e67e"></a>

### [`00765e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765e74.md) → [`00766250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00766/00766250.md) FUN_00766250

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`007662b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/007662b4.md) [`007671a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/007671a0.md) [`00767d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767d0c.md) · 呼出先 10件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459b10.md) [`0059705c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059705c.md) [`005971dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005971dc.md) [`00765780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765780.md)
- 新版 呼出元 3件 [`00766690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00766/00766690.md) [`0076757c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00767/0076757c.md) [`007680e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007680e8.md) · 呼出先 10件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00459e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459e30.md) [`0059737c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059737c.md) [`005974fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005974fc.md) [`00765b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765b5c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.20% / 新版 57.20%

CFGの説明率　旧版 23.53% / 新版 24.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `store_value` 2件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 6件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 39件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00765e78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00765e78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00765e7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00765e78",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00765e7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00765e80",
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
      "00766254",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00766258",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0076625c",
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

- 旧版 [`00765e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765e74.md#insn-00765e78) · [`00765e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765e74.md#insn-00765e7c) · [`00765e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765e74.md#insn-00765e80)

~~~diff
- 00765e78 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00765e78 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00765e78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00765e78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00765e78 bytes fd7b06a9
- 00765e7c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:70:8"]]
- 00765e7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00765e7c bytes f73b00f9
- 00765e80 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00765e80 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00765e80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00765e80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00765e80 bytes f65708a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae4c03129b81c18267c21705d7b4ee21"></a>

### [`007662b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/007662b4.md) → [`00766690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00766/00766690.md) FUN_00766690

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007692b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/007692b8.md) · 呼出先 27件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md) [`00459430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459430.md)
- 新版 呼出元 1件 [`00769694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769694.md) · 呼出先 27件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00451d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451d38.md) [`00459750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459750.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 63.12% / 新版 63.12%

CFGの説明率　旧版 20.57% / 新版 20.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_branch_alignment` 36件, `unresolved_call_alignment` 14件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 48件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007662d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007662f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00766368"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007662d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x208]",
        null,
        null
      ]
    ],
    [
      "unmatched:007662f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00766334",
      "DATA",
      [
        "storage",
        "003c7784",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "007666b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x208]",
        null,
        null
      ]
    ],
    [
      "007666d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00766710",
      "DATA",
      [
        "storage",
        "003c7784",
        "fde_003c7784",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007662d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/007662b4.md#insn-007662d4) · [`007662f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/007662b4.md#insn-007662f4) · [`00766368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/007662b4.md#insn-00766368)

~~~diff
- 007662d4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:78:8"]]
- 007662d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:8"]]
- 007662d4 bytes e53f00f9
- 007662f4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 007662f4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 007662f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 007662f4 bytes a8831ef8
- 00766368 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00766368 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00766368 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:109:8"]]
- 00766368 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00766368 bytes ff270439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8b1400b7d9efc1782c98ece358ca65d"></a>

### [`00767074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767074.md) → [`00767450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00767/00767450.md) FUN_00767450

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007662b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/007662b4.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0059725c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059725c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00766690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00766/00766690.md) · 呼出先 5件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0059757c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059757c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.94% / 新版 77.94%

CFGの説明率　旧版 61.11% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00767074"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00767074"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00767078"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00767074",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00767078",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0076707c",
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
      "00767450",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00767454",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00767458",
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

- 旧版 [`00767074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767074.md#insn-00767074) · [`00767078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767074.md#insn-00767078) · [`0076707c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767074.md#insn-0076707c)

~~~diff
- 00767074 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00767074 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00767074 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00767074 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00767074 bytes fd7bbba9
- 00767078 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00767078 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00767078 bytes f90b00f9
- 0076707c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0076707c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0076707c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0076707c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0076707c bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e3e40cb4fb64c61fc66b31e356b446f"></a>

### [`007671a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/007671a0.md) → [`0076757c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00767/0076757c.md) FUN_0076757c

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006972e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006972e8.md) · 呼出先 28件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md) [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md)
- 新版 呼出元 1件 [`00697698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697698.md) · 呼出先 28件 [`0043df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00451afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451afc.md) [`00451d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451d38.md) [`00459b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459b8c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.29% / 新版 66.29%

CFGの説明率　旧版 13.59% / 新版 13.51%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_condition` 2件, `unresolved_branch_alignment` 21件, `unresolved_call_alignment` 15件, `unresolved_store_alignment` 62件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007671b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007671b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007671b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007671b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:007671b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:007671c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x200]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0076758c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00767590",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0076759c",
      "WRITE",
      [
        "storage",
        "Stack[-0x200]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007671b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/007671a0.md#insn-007671b0) · [`007671b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/007671a0.md#insn-007671b4) · [`007671c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/007671a0.md#insn-007671c0)

~~~diff
- 007671b0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 007671b0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 007671b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 007671b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007671b0 bytes f65704a9
- 007671b4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 007671b4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 007671b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 007671b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007671b4 bytes f44f05a9
- 007671c0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 007671c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:8"]]
- 007671c0 bytes e52300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c497a2c169831d9bc4aecb4be22ceae"></a>

### [`00767d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767d0c.md) → [`007680e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007680e8.md) FUN_007680e8

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`006972e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006972e8.md) [`00767dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767dfc.md) [`007692b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/007692b8.md) [`0076984c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/0076984c.md) · 呼出先 5件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00550c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c68.md) [`00765e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765e74.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 4件 [`00697698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697698.md) [`007681d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007681d8.md) [`00769694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769694.md) [`00769c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769c28.md) · 呼出先 5件 [`0043df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md) [`00550f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f88.md) [`00766250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00766/00766250.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.74% / 新版 76.74%

CFGの説明率　旧版 50.00% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00767d1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00767d1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00767d3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00767d1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00767d3c",
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
      "007680f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00768118",
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

- 旧版 [`00767d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767d0c.md#insn-00767d1c) · [`00767d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767d0c.md#insn-00767d3c) · [`00767d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767d0c.md#insn-00767d68)
- 新版 [`00768144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007680e8.md#insn-00768144)

~~~diff
- 00767d1c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00767d1c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00767d1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00767d1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00767d1c bytes f44f07a9
- 00767d3c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00767d3c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00767d3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00767d3c bytes a8831ff8
- 00767d68 ["INT_ADD", "register:40f0:8", ["const:767d68:8", "const:4:8"]]
- 00767d68 ["CALL", null, ["callee:00766250:8"]]
+ 00768144 ["INT_ADD", "register:40f0:8", ["const:768144:8", "const:4:8"]]
+ 00768144 ["CALL", null, ["callee:00766250:8"]]
- 00767d68 bytes 43f8ff97
+ 00768144 bytes 43f8ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dad52c4d83e50c421bb5a13580b5ed4e"></a>

### [`00767dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767dfc.md) → [`007681d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007681d8.md) FUN_007681d8

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`00886f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f9c.md) · 呼出先 8件 [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md) [`00597150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597150.md) [`00764c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764c84.md) [`00767d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767d0c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 2件 [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) [`00887f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887f48.md) · 呼出先 8件 [`00459b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459b8c.md) [`00597470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597470.md) [`00765060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765060.md) [`007680e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007680e8.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.63% / 新版 62.63%

CFGの説明率　旧版 2.50% / 新版 2.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00767e24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00767e90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00767e94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00767e24",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00768220",
      "DATA",
      [
        "storage",
        "003c7784",
        null,
        "dword"
      ]
    ],
    [
      "unmatched:00767e8c",
      "READ",
      [
        "storage",
        "00c9acf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00768200",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00768220",
      "DATA",
      [
        "storage",
        "003c7784",
        "fde_003c7784",
        "dword"
      ]
    ],
    [
      "00768268",
      "READ",
      [
        "storage",
        "00c9bcc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00767e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767dfc.md#insn-00767e24) · [`00767e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767dfc.md#insn-00767e34) · [`00767e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767dfc.md#insn-00767e7c)
- 新版 [`00768210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007681d8.md#insn-00768210) · [`00768258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007681d8.md#insn-00768258)

~~~diff
- 00767e24 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00767e24 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00767e24 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00767e24 bytes a8831ff8
- 00767e34 ["INT_ADD", "register:40f0:8", ["const:767e34:8", "const:4:8"]]
- 00767e34 ["CALL", null, ["callee:007680e8:8"]]
+ 00768210 ["INT_ADD", "register:40f0:8", ["const:768210:8", "const:4:8"]]
+ 00768210 ["CALL", null, ["callee:007680e8:8"]]
- 00767e34 bytes b6ffff97
+ 00768210 bytes b6ffff97
- 00767e7c ["INT_ADD", "register:40f0:8", ["const:767e7c:8", "const:4:8"]]
- 00767e7c ["CALL", null, ["callee:00c58f30:8"]]
+ 00768258 ["INT_ADD", "register:40f0:8", ["const:768258:8", "const:4:8"]]
+ 00768258 ["CALL", null, ["callee:00c58f30:8"]]
- 00767e7c bytes 39c01394
+ 00768258 bytes 36c31394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86c0f7de10a203751c4d6d8fc7f0e910"></a>

### [`0076820c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/0076820c.md) → [`007685e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007685e8.md) FUN_007685e8

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00884bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884bcc.md) [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 9件 [`00597efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597efc.md) [`00878310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878310.md) [`00b3c978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c978.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 2件 [`00885b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885b78.md) [`00a07d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a07/00a07d9c.md) · 呼出先 9件 [`0059821c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059821c.md) [`008792bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/008792bc.md) [`00b3d96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d96c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.92% / 新版 91.92%

CFGの説明率　旧版 40.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00768290"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00768294"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00768298"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00768624",
      "DATA",
      [
        "storage",
        "003c76b8",
        null,
        "dword"
      ]
    ],
    [
      "00768628",
      "DATA",
      [
        "storage",
        "003c76c0",
        null,
        "byte[15]"
      ]
    ],
    [
      "unmatched:00768280",
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
      "00768624",
      "DATA",
      [
        "storage",
        "003c76b8",
        "fde_003c76b8",
        "dword"
      ]
    ],
    [
      "00768628",
      "DATA",
      [
        "storage",
        "003c76c0",
        null,
        "dword"
      ]
    ],
    [
      "0076865c",
      "READ",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00768264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/0076820c.md#insn-00768264) · [`00768290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/0076820c.md#insn-00768290) · [`00768294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/0076820c.md#insn-00768294)
- 新版 [`00768640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007685e8.md#insn-00768640)

~~~diff
- 00768264 ["INT_ADD", "register:40f0:8", ["const:768264:8", "const:4:8"]]
- 00768264 ["CALL", null, ["callee:0059821c:8"]]
+ 00768640 ["INT_ADD", "register:40f0:8", ["const:768640:8", "const:4:8"]]
+ 00768640 ["CALL", null, ["callee:0059821c:8"]]
- 00768264 bytes 26bff897
+ 00768640 bytes f7bef897
- 00768290 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00768290 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:20:8"]]
- 00768290 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00768290 bytes e8830039
- 00768294 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00768294 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00768294 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00768294 bytes ea1302f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52da52f6b7b792544d01d27099d251f7"></a>

### [`0076846c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/0076846c.md) → [`00768848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/00768848.md) FUN_00768848

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009ccb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009ccb84.md) · 呼出先 8件 [`00597efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597efc.md) [`00b3cb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3cb60.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`009cdb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cdb30.md) · 呼出先 8件 [`0059821c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059821c.md) [`00b3db54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3db54.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.00% / 新版 76.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00768470"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00768470"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00768474"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00768470",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00768474",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00768478",
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
      "0076884c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00768850",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00768854",
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

- 旧版 [`00768470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/0076846c.md#insn-00768470) · [`00768474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/0076846c.md#insn-00768474) · [`00768478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/0076846c.md#insn-00768478)

~~~diff
- 00768470 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00768470 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00768470 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00768470 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00768470 bytes fd7b03a9
- 00768474 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00768474 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00768474 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00768474 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00768474 bytes f65704a9
- 00768478 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00768478 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00768478 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00768478 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00768478 bytes f44f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe9070cb94a8075819e59437eb992876"></a>

### [`00768dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768dbc.md) → [`00769198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769198.md) FUN_00769198

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00768c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768c40.md) · 呼出先 3件 [`004499f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/004499f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`0076901c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/0076901c.md) · 呼出先 3件 [`00449d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d18.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 80.00% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00768e08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007691e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00768dfc",
      "incomplete_value": true,
      "site": "00768e0c",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00768e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768dbc.md#insn-00768e08) · [`00768e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768dbc.md#insn-00768e0c)
- 新版 [`007691e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769198.md#insn-007691e8) · [`007691e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769198.md#insn-007691e4)

~~~diff
- 00768e08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00768e08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00768e08 bytes 770a00f9
- 00768e0c ["INT_ADD", "register:40f0:8", ["const:768e0c:8", "const:4:8"]]
- 00768e0c ["CALL", null, ["callee:00c590a0:8"]]
+ 007691e8 ["INT_ADD", "register:40f0:8", ["const:7691e8:8", "const:4:8"]]
+ 007691e8 ["CALL", null, ["callee:00c590a0:8"]]
- 00768e0c bytes b1bc1394
+ 007691e8 bytes aebf1394
+ 007691e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
+ 007691e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
+ 007691e4 bytes 770a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-935a63765a24dbd14965277c8780f2eb"></a>

### [`007692b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/007692b8.md) → [`00769694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769694.md) FUN_00769694

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`0076984c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/0076984c.md) [`00769c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769c60.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) [`0088f4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f4f4.md) · 呼出先 11件 [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`00597efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597efc.md) [`007662b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/007662b4.md) [`00767d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767d0c.md) [`00767fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767fec.md)
- 新版 呼出元 6件 [`00769c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769c28.md) [`0076a03c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a03c.md) [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) [`008904a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/008904a0.md) · 呼出先 11件 [`00540abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540abc.md) [`0059821c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059821c.md) [`00766690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00766/00766690.md) [`007680e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007680e8.md) [`007683c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007683c8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.45% / 新版 87.45%

CFGの説明率　旧版 46.75% / 新版 48.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007692bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007692bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007692c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007692bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:007692c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:007692c4",
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
      "00769698",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0076969c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "007696a0",
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

- 旧版 [`007692bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/007692b8.md#insn-007692bc) · [`007692c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/007692b8.md#insn-007692c0) · [`007692c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/007692b8.md#insn-007692c4)

~~~diff
- 007692bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 007692bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 007692bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 007692bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007692bc bytes fd7b07a9
- 007692c0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:80:8"]]
- 007692c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 007692c0 bytes f94300f9
- 007692c4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 007692c4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 007692c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 007692c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007692c4 bytes f85f09a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76a656d443036025a79bbbf782a430fa"></a>

### [`00769778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769778.md) → [`00769b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769b54.md) FUN_00769b54

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 84.62% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007697a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769778.md#insn-007697a8) · [`007697bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769778.md#insn-007697bc) · [`007697cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769778.md#insn-007697cc)
- 新版 [`00769b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769b54.md#insn-00769b84) · [`00769b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769b54.md#insn-00769b98) · [`00769ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769b54.md#insn-00769ba8)

~~~diff
- 007697a8 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
+ 00769b84 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 007697a8 bytes 00020054
+ 00769b84 bytes 00020054
- 007697bc ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
+ 00769b98 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 007697bc bytes 40010054
+ 00769b98 bytes 40010054
- 007697cc ["INT_ADD", "register:40f0:8", ["const:7697cc:8", "const:4:8"]]
- 007697cc ["CALL", null, ["callee:00c58f50:8"]]
+ 00769ba8 ["INT_ADD", "register:40f0:8", ["const:769ba8:8", "const:4:8"]]
+ 00769ba8 ["CALL", null, ["callee:00c58f50:8"]]
- 007697cc bytes edb91394
+ 00769ba8 bytes eabc1394
~~~


<a id="compare-1e845d8592dbf1173737945ec046a608"></a>

### [`007697fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/007697fc.md) → [`00769bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769bd8.md) FUN_00769bd8

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0076980c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/007697fc.md#insn-0076980c) · [`00769818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/007697fc.md#insn-00769818) · [`0076981c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/007697fc.md#insn-0076981c)
- 新版 [`00769be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769bd8.md#insn-00769be8) · [`00769bf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769bd8.md#insn-00769bf4) · [`00769bf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769bd8.md#insn-00769bf8)

~~~diff
- 0076980c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 0076980c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00769be8 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00769be8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0076980c bytes b30000b4
+ 00769be8 bytes b30000b4
- 00769818 ["INT_ADD", "register:40f0:8", ["const:769818:8", "const:4:8"]]
- 00769818 ["CALL", null, ["callee:00c54d90:8"]]
+ 00769bf4 ["INT_ADD", "register:40f0:8", ["const:769bf4:8", "const:4:8"]]
+ 00769bf4 ["CALL", null, ["callee:00c54d90:8"]]
- 00769818 bytes 62a91394
+ 00769bf4 bytes 67ac1394
- 0076981c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0076981c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00769bf8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00769bf8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0076981c bytes 800000b4
+ 00769bf8 bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-767bbb37de9930224bb04c19090dfaaa"></a>

### [`0076984c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/0076984c.md) → [`00769c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769c28.md) FUN_00769c28

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00882128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882128.md) [`00922e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00922/00922e1c.md) · 呼出先 9件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00767d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767d0c.md) [`00767fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767fec.md) [`007692b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/007692b8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 2件 [`008830d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/008830d4.md) [`00923dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00923/00923dc8.md) · 呼出先 9件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`007680e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007680e8.md) [`007683c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007683c8.md) [`00769694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769694.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.62% / 新版 71.62%

CFGの説明率　旧版 39.02% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 3件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00769850"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00769850"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00769854"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00769850",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00769854",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00769858",
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
      "00769c2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00769c30",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00769c34",
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

- 旧版 [`00769850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/0076984c.md#insn-00769850) · [`00769854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/0076984c.md#insn-00769854) · [`00769858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/0076984c.md#insn-00769858)

~~~diff
- 00769850 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00769850 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00769850 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00769850 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00769850 bytes fd7b0aa9
- 00769854 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:b0:8"]]
- 00769854 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00769854 bytes f75b00f9
- 00769858 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00769858 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00769858 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00769858 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00769858 bytes f6570ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86aabcf54a098e0c37950a6d072c3f22"></a>

### [`00769d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769d3c.md) → [`0076a118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a118.md) FUN_0076a118

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00882128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882128.md) · 呼出先 5件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)
- 新版 呼出元 1件 [`008830d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/008830d4.md) · 呼出先 5件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) [`00c59420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59420.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 25.00% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00769d70"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0076a14c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0076a160",
      "incomplete_value": true,
      "site": "0076a164",
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
            "const:2c:8"
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
      "unmatched:00769d6c",
      "DATA",
      [
        "storage",
        "00337578",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "unmatched:00769d70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0076a18c"
      ]
    ]
  ],
  "added": [
    [
      "0076a148",
      "DATA",
      [
        "storage",
        "00337578",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "0076a14c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0076a18c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00769d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769d3c.md#insn-00769d70) · [`00769d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769d3c.md#insn-00769d88)
- 新版 [`0076a164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a118.md#insn-0076a164) · [`0076a14c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a118.md#insn-0076a14c)

~~~diff
- 00769d70 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00769d70 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00769d70 bytes 130200b4
- 00769d88 ["INT_ADD", "register:40f0:8", ["const:769d88:8", "const:4:8"]]
- 00769d88 ["CALL", null, ["callee:00c59420:8"]]
+ 0076a164 ["INT_ADD", "register:40f0:8", ["const:76a164:8", "const:4:8"]]
+ 0076a164 ["CALL", null, ["callee:00c59420:8"]]
- 00769d88 bytes b2b91394
+ 0076a164 bytes afbc1394
+ 0076a14c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 0076a14c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 0076a14c bytes 130200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bf36b2037da3ebe5162364bc2364e06"></a>

### [`00772938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00772/00772938.md) → [`00772d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00772/00772d14.md) FUN_00772d14

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`00914e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00914/00914e84.md) · 呼出先 22件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043e868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e868.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md)
- 新版 呼出元 2件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) [`00915e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00915/00915e30.md) · 呼出先 22件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043eb88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043eb88.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00493168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493168.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 91.60% / 新版 91.60%

CFGの説明率　旧版 95.50% / 新版 95.98%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 17件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00772938"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00772938"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077293c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00772938",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077293c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00772940",
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
      "00772d14",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00772d18",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00772d1c",
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

- 旧版 [`00772938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00772/00772938.md#insn-00772938) · [`0077293c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00772/00772938.md#insn-0077293c) · [`00772940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00772/00772938.md#insn-00772940)

~~~diff
- 00772938 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00772938 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00772938 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00772938 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00772938 bytes fd7bbaa9
- 0077293c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0077293c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0077293c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0077293c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077293c bytes fc6f01a9
- 00772940 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00772940 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00772940 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00772940 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00772940 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49a54084123a61f00c23f5a9fe4a8717"></a>

### [`007735ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007735ec.md) → [`007739c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/007739c8.md) FUN_007739c8

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 6件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 6件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) [`00894dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894dc0.md) [`0089cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089cc90.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00442e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442e98.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 71.43% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00773680",
      "incomplete_value": true,
      "site": "00773688",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00773680",
      "incomplete_value": true,
      "site": "00773688",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00773688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007735ec.md#insn-00773688) · [`0077364c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007735ec.md#insn-0077364c) · [`00773660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007735ec.md#insn-00773660)
- 新版 [`00773a64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/007739c8.md#insn-00773a64) · [`00773a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/007739c8.md#insn-00773a28) · [`00773a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/007739c8.md#insn-00773a3c)

~~~diff
- 00773688 ["INT_ADD", "register:40f0:8", ["const:773688:8", "const:4:8"]]
- 00773688 ["CALL", null, ["callee:0043be80:8"]]
+ 00773a64 ["INT_ADD", "register:40f0:8", ["const:773a64:8", "const:4:8"]]
+ 00773a64 ["CALL", null, ["callee:0043be80:8"]]
- 00773688 bytes 3621f397
+ 00773a64 bytes 0721f397
- 0077364c ["INT_ADD", "register:40f0:8", ["const:77364c:8", "const:4:8"]]
- 0077364c ["CALL", null, ["callee:0043be80:8"]]
+ 00773a28 ["INT_ADD", "register:40f0:8", ["const:773a28:8", "const:4:8"]]
+ 00773a28 ["CALL", null, ["callee:0043be80:8"]]
- 0077364c bytes 4521f397
+ 00773a28 bytes 1621f397
- 00773660 ["INT_ADD", "register:40f0:8", ["const:773660:8", "const:4:8"]]
- 00773660 ["CALL", null, ["callee:00442e98:8"]]
+ 00773a3c ["INT_ADD", "register:40f0:8", ["const:773a3c:8", "const:4:8"]]
+ 00773a3c ["CALL", null, ["callee:00442e98:8"]]
- 00773660 bytes 463df397
+ 00773a3c bytes 173df397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac62b73865838d4031ceecd82bc0ae05"></a>

### [`007736f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007736f4.md) → [`00773ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773ad0.md) FUN_00773ad0

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 5件 [`0077c8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c8a4.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 5件 [`0077cc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc80.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00773750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007736f4.md#insn-00773750) · [`00773758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007736f4.md#insn-00773758) · [`00773770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007736f4.md#insn-00773770)
- 新版 [`00773b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773ad0.md#insn-00773b2c) · [`00773b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773ad0.md#insn-00773b34) · [`00773b4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773ad0.md#insn-00773b4c)

~~~diff
- 00773750 ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
+ 00773b2c ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
- 00773750 bytes c2010054
+ 00773b2c bytes c2010054
- 00773758 ["INT_ADD", "register:40f0:8", ["const:773758:8", "const:4:8"]]
- 00773758 ["CALL", null, ["callee:00c58f30:8"]]
+ 00773b34 ["INT_ADD", "register:40f0:8", ["const:773b34:8", "const:4:8"]]
+ 00773b34 ["CALL", null, ["callee:00c58f30:8"]]
- 00773758 bytes 02921394
+ 00773b34 bytes ff941394
- 00773770 ["INT_ADD", "register:40f0:8", ["const:773770:8", "const:4:8"]]
- 00773770 ["CALL", null, ["callee:00c590a0:8"]]
+ 00773b4c ["INT_ADD", "register:40f0:8", ["const:773b4c:8", "const:4:8"]]
+ 00773b4c ["CALL", null, ["callee:00c590a0:8"]]
- 00773770 bytes 58921394
+ 00773b4c bytes 55951394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e27aad48dd001dac047ac45b7bc3add"></a>

### [`007737b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007737b0.md) → [`00773b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773b8c.md) FUN_00773b8c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 2件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00773bcc",
      "incomplete_value": false,
      "site": "00773bd0",
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
      "definition_site": "007737f0",
      "incomplete_value": false,
      "site": "007737f4",
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
      "00773bcc",
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
      "00773bcc",
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

- 旧版 [`007737f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007737b0.md#insn-007737f4) · [`007737f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007737b0.md#insn-007737f0)
- 新版 [`00773bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773b8c.md#insn-00773bd0) · [`00773bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773b8c.md#insn-00773bcc)

~~~diff
- 007737f4 ["INT_ADD", "register:40f0:8", ["const:7737f4:8", "const:4:8"]]
- 007737f4 ["CALL", null, ["callee:00442c90:8"]]
+ 00773bd0 ["INT_ADD", "register:40f0:8", ["const:773bd0:8", "const:4:8"]]
+ 00773bd0 ["CALL", null, ["callee:00442c90:8"]]
- 007737f4 bytes 5f3cf397
+ 00773bd0 bytes 303cf397
- 007737f0 ["COPY", "tmp:0:8", ["const:170:8"]]
- 007737f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007737f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007737f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00773bcc ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 00773bcc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00773bcc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00773bcc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007737f0 bytes 00c00591
+ 00773bcc bytes 00c00691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-899d600abf07af5c6c60596a2705b0dc"></a>

### [`00773804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/00773804.md) → [`00773be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773be0.md) FUN_00773be0

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 68.75% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00773854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/00773804.md#insn-00773854) · [`0077386c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/00773804.md#insn-0077386c) · [`007738b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/00773804.md#insn-007738b4)
- 新版 [`00773c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773be0.md#insn-00773c30) · [`00773c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773be0.md#insn-00773c48) · [`00773c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773be0.md#insn-00773c90)

~~~diff
- 00773854 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00773854 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00773c30 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00773c30 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00773854 bytes 0a040054
+ 00773c30 bytes 0a040054
- 0077386c ["INT_ADD", "register:40f0:8", ["const:77386c:8", "const:4:8"]]
- 0077386c ["CALL", null, ["callee:00c58f30:8"]]
+ 00773c48 ["INT_ADD", "register:40f0:8", ["const:773c48:8", "const:4:8"]]
+ 00773c48 ["CALL", null, ["callee:00c58f30:8"]]
- 0077386c bytes bd911394
+ 00773c48 bytes ba941394
- 007738b4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 007738b4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00773c90 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00773c90 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 007738b4 bytes 680000b4
+ 00773c90 bytes 680000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b079ae0e5122c81535434b68d90a1828"></a>

### [`0077a470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077a470.md) → [`0077a84c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077a/0077a84c.md) FUN_0077a84c

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) · 呼出先 10件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046a928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a928.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md)
- 新版 呼出元 1件 [`00773cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773cc8.md) · 呼出先 10件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046ac48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046a/0046ac48.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.78% / 新版 88.78%

CFGの説明率　旧版 21.43% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0077a884",
      "incomplete_value": true,
      "site": "0077a884",
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
      "definition_site": "0077a4a8",
      "incomplete_value": true,
      "site": "0077a4a8",
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
      "site": "0077a684"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0077a724"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0077a880",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0077a88c",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0077a894",
      "PARAM",
      [
        "storage",
        "00c77ad8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0077a880",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "0077a88c",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0077a894",
      "PARAM",
      [
        "storage",
        "00c78aa8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077a4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077a470.md#insn-0077a4c4) · [`0077a56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077a470.md#insn-0077a56c) · [`0077a62c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077a470.md#insn-0077a62c)
- 新版 [`0077a8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077a/0077a84c.md#insn-0077a8a0) · [`0077a948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077a/0077a84c.md#insn-0077a948) · [`0077aa08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077a/0077a84c.md#insn-0077aa08)

~~~diff
- 0077a4c4 ["INT_ADD", "register:40f0:8", ["const:77a4c4:8", "const:4:8"]]
- 0077a4c4 ["CALL", null, ["callee:00c596b0:8"]]
+ 0077a8a0 ["INT_ADD", "register:40f0:8", ["const:77a8a0:8", "const:4:8"]]
+ 0077a8a0 ["CALL", null, ["callee:00c596b0:8"]]
- 0077a4c4 bytes 87781394
+ 0077a8a0 bytes 847b1394
- 0077a56c ["INT_ADD", "register:40f0:8", ["const:77a56c:8", "const:4:8"]]
- 0077a56c ["CALL", null, ["callee:0073783c:8"]]
+ 0077a948 ["INT_ADD", "register:40f0:8", ["const:77a948:8", "const:4:8"]]
+ 0077a948 ["CALL", null, ["callee:0073783c:8"]]
- 0077a56c bytes c8f3fe97
+ 0077a948 bytes bdf3fe97
- 0077a62c ["INT_ADD", "register:40f0:8", ["const:77a62c:8", "const:4:8"]]
- 0077a62c ["CALL", null, ["callee:00469f64:8"]]
+ 0077aa08 ["INT_ADD", "register:40f0:8", ["const:77aa08:8", "const:4:8"]]
+ 0077aa08 ["CALL", null, ["callee:00469f64:8"]]
- 0077a62c bytes 86bdf397
+ 0077aa08 bytes 57bdf397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1501a8d851fe4a6e97ab7f60e3932ffa"></a>

### [`0077a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077a950.md) → [`0077ad2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077a/0077ad2c.md) FUN_0077ad2c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) · 呼出先 7件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046af4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af4c.md) [`0046db14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db14.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)
- 新版 呼出元 1件 [`00773cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773cc8.md) · 呼出先 7件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`0046b26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046b/0046b26c.md) [`0046de34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de34.md) [`0048a2ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2ac.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.35% / 新版 89.35%

CFGの説明率　旧版 30.00% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077a960"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077a960"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077a964"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0077a960",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077a964",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077a980",
      "WRITE",
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
      "0077ad3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0077ad40",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0077ad5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077a960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077a950.md#insn-0077a960) · [`0077a964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077a950.md#insn-0077a964) · [`0077a980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077a950.md#insn-0077a980)

~~~diff
- 0077a960 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0077a960 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0077a960 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 0077a960 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077a960 bytes f65707a9
- 0077a964 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0077a964 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0077a964 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 0077a964 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077a964 bytes f44f08a9
- 0077a980 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0077a980 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 0077a980 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0077a980 bytes a8831ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7de3d428ecb49faa58714ce51bd2a3f7"></a>

### [`0077acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077acb0.md) → [`0077b08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077b08c.md) FUN_0077b08c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00997090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00997/00997090.md) · 呼出先 3件 [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0077b364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077b364.md)
- 新版 呼出元 1件 [`0099803c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00998/0099803c.md) · 呼出先 3件 [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0077b740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077b740.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 55.56% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0077b0c0",
      "incomplete_value": true,
      "site": "0077b0d0",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": {
      "definition_site": "0077ace4",
      "incomplete_value": true,
      "site": "0077acf4",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0077accc",
      "incomplete_value": true,
      "site": "0077acf4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4018:4"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 6
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0077acf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077acb0.md#insn-0077acf4) · [`0077ace4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077acb0.md#insn-0077ace4) · [`0077ad04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077acb0.md#insn-0077ad04)
- 新版 [`0077b0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077b08c.md#insn-0077b0d0) · [`0077b0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077b08c.md#insn-0077b0e0)

~~~diff
- 0077acf4 ["INT_ADD", "register:40f0:8", ["const:77acf4:8", "const:4:8"]]
- 0077acf4 ["CALL", null, ["callee:0077b740:8"]]
+ 0077b0d0 ["INT_ADD", "register:40f0:8", ["const:77b0d0:8", "const:4:8"]]
+ 0077b0d0 ["CALL", null, ["callee:0077b740:8"]]
- 0077acf4 bytes 9c010094
+ 0077b0d0 bytes 9c010094
- 0077ace4 ["COPY", "register:4008:8", ["register:4098:8"]]
- 0077ace4 bytes e10313aa
- 0077ad04 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0077ad04 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 0077b0e0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0077b0e0 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 0077ad04 bytes 61030054
+ 0077b0e0 bytes 61030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-264c5b78658ba295386c6c7d82e13a54"></a>

### [`0077ad84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077ad84.md) → [`0077b160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077b160.md) FUN_0077b160

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00613ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/00613ca4.md) · 呼出先 7件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00468f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468f8c.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046af4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af4c.md) [`0046da9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da9c.md)
- 新版 呼出元 1件 [`00614054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00614/00614054.md) · 呼出先 7件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`004692ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692ac.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`0046b26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046b/0046b26c.md) [`0046ddbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046ddbc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.81% / 新版 88.81%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077ad88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077ad88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077ad8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0077ad88",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077ad8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077ad90",
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
      "0077b164",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0077b168",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0077b16c",
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

- 旧版 [`0077ad88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077ad84.md#insn-0077ad88) · [`0077ad8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077ad84.md#insn-0077ad8c) · [`0077ad90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077ad84.md#insn-0077ad90)

~~~diff
- 0077ad88 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0077ad88 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0077ad88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0077ad88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077ad88 bytes fd7b03a9
- 0077ad8c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0077ad8c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0077ad8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0077ad8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077ad8c bytes fc6f04a9
- 0077ad90 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0077ad90 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0077ad90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0077ad90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077ad90 bytes fa6705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aecd0a2b863cf3047cb259f019c59ddf"></a>

### [`0077afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077afc0.md) → [`0077b39c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077b39c.md) FUN_0077b39c

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 15件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487bc0.md)
- 新版 呼出元 1件 [`00b29fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b29/00b29fe4.md) · 呼出先 15件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_store_alignment

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 83.72% / 新版 83.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 3件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077b008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077b030"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077b034"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0077b008",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0077b008",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077b024",
      "READ",
      [
        "storage",
        "002bdd5e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0077b3e4",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "0077b3e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "0077b400",
      "READ",
      [
        "storage",
        "002bde3c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077b008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077afc0.md#insn-0077b008) · [`0077b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077afc0.md#insn-0077b030) · [`0077b034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077afc0.md#insn-0077b034)

~~~diff
- 0077b008 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 0077b008 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0077b008 bytes e91700f9
- 0077b030 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 0077b030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0077b030 bytes e01300f9
- 0077b034 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0077b034 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0077b034 bytes 0000803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a923687db1caf947d92392595a5b3b79"></a>

### [`0077b364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077b364.md) → [`0077b740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077b740.md) FUN_0077b740

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006b545c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b5/006b545c.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`0077acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077acb0.md) · 呼出先 11件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0072c22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072c/0072c22c.md) [`0072c334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072c/0072c334.md)
- 新版 呼出元 3件 [`006b580c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b5/006b580c.md) [`00773cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773cc8.md) [`0077b08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077b08c.md) · 呼出先 11件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0072c5dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0072c/0072c5dc.md) [`0072c6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0072c/0072c6e4.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.13% / 新版 94.13%

CFGの説明率　旧版 51.14% / 新版 51.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 4件, `store_value` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0077b9a4",
      "incomplete_value": true,
      "site": "0077b9b8",
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
                "const:b90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077b5c8",
      "incomplete_value": true,
      "site": "0077b5dc",
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
                "const:b40:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077b71c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0077bc70",
      "incomplete_value": true,
      "site": "0077bc84",
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
                "const:110:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077b894",
      "incomplete_value": true,
      "site": "0077b8a8",
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
                "const:c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 104,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0077b7c4",
      "READ",
      [
        "storage",
        "00c9b578",
        null,
        "pointer"
      ]
    ],
    [
      "0077b7d4",
      "DATA",
      [
        "storage",
        "00ca4554",
        null,
        null
      ]
    ],
    [
      "0077b9a4",
      "READ",
      [
        "storage",
        "002c2b40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0077b7c4",
      "READ",
      [
        "storage",
        "00c9c548",
        null,
        "pointer"
      ]
    ],
    [
      "0077b7d4",
      "DATA",
      [
        "storage",
        "00ca5524",
        null,
        null
      ]
    ],
    [
      "0077b9a4",
      "READ",
      [
        "storage",
        "002c2b90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077b704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077b364.md#insn-0077b704) · [`0077b71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077b364.md#insn-0077b71c) · [`0077b760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077b364.md#insn-0077b760)

~~~diff
- 0077b704 ["CBRANCH", null, ["local:b25:8", "register:102:1"]]
- 0077b704 bytes a2010054
- 0077b71c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:28:8"]]
- 0077b71c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0077b71c bytes e81600f9
- 0077b760 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0077b760 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0077b760 ["CBRANCH", null, ["local:b61:8", "tmp:1:1"]]
- 0077b760 bytes e8170054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c80ae826ccc98e737eb4316647127fc"></a>

### [`0077bb04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077bb04.md) → [`0077bee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077bee0.md) FUN_0077bee0

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 17件 [`00612324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00612/00612324.md) [`0067072c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00670/0067072c.md) [`00680e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00680/00680e48.md) [`006acfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ac/006acfb4.md) [`00722c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00722/00722c58.md) · 呼出先 1件 [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md)
- 新版 呼出元 17件 [`006126d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00612/006126d4.md) [`00670adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00670/00670adc.md) [`006811f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00681/006811f8.md) [`006ad364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ad/006ad364.md) [`00723008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00723/00723008.md) · 呼出先 1件 [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.86% / 新版 89.86%

CFGの説明率　旧版 11.11% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0077bb64"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0077bf40"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0077bbb8",
      "incomplete_value": true,
      "site": "0077bbd4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "INT_ADD",
            "4",
            [
              [
                "live",
                "register:40e0:4"
              ],
              [
                "leaf",
                "const:3c:4"
              ]
            ]
          ]
        ]
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
      "unmatched:0077bb3c",
      "READ",
      [
        "storage",
        "00c9b578",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0077bb50",
      "DATA",
      [
        "storage",
        "00ca4554",
        null,
        null
      ]
    ],
    [
      "unmatched:0077bb54",
      "DATA",
      [
        "storage",
        "0033207c",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "0077bf18",
      "READ",
      [
        "storage",
        "00c9c548",
        null,
        "pointer"
      ]
    ],
    [
      "0077bf2c",
      "DATA",
      [
        "storage",
        "00ca5524",
        null,
        null
      ]
    ],
    [
      "0077bf30",
      "DATA",
      [
        "storage",
        "0033207c",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077bb64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077bb04.md#insn-0077bb64) · [`0077bbd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077bb04.md#insn-0077bbd4)
- 新版 [`0077bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077bee0.md#insn-0077bfb0) · [`0077bf40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077bee0.md#insn-0077bf40)

~~~diff
- 0077bb64 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0077bb64 ["COPY", "tmp:1:4", ["const:0:4"]]
- 0077bb64 ["COPY", "tmp:2:4", ["register:4040:4"]]
- 0077bb64 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0077bb64 bytes 19119f1a
- 0077bbd4 ["INT_ADD", "register:40f0:8", ["const:77bbd4:8", "const:4:8"]]
- 0077bbd4 ["CALL", null, ["callee:00469f64:8"]]
+ 0077bfb0 ["INT_ADD", "register:40f0:8", ["const:77bfb0:8", "const:4:8"]]
+ 0077bfb0 ["CALL", null, ["callee:00469f64:8"]]
- 0077bbd4 bytes 1cb8f397
+ 0077bfb0 bytes edb7f397
+ 0077bf40 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0077bf40 ["COPY", "tmp:1:4", ["const:0:4"]]
+ 0077bf40 ["COPY", "tmp:2:4", ["register:4040:4"]]
+ 0077bf40 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 0077bf40 bytes 19119f1a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c953e83bea602cb71637689652cc18cd"></a>

### [`0077bc18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077bc18.md) → [`0077bff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077bff4.md) FUN_0077bff4

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0077c08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c08c.md) · 呼出先 6件 [`0067e628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e628.md) [`00682364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`00758550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758550.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0077c468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077c468.md) · 呼出先 6件 [`0067e9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0067e/0067e9d8.md) [`00682714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00682/00682714.md) [`00758900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/00758900.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.89% / 新版 77.89%

CFGの説明率　旧版 57.14% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0077c010",
      "incomplete_value": false,
      "site": "0077c014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077bc34",
      "incomplete_value": false,
      "site": "0077bc38",
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
            "const:3e0:8"
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
      "site": "0077c00c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c048"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0077c014",
      "DATA",
      [
        "storage",
        "00c783e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0077bcd8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ],
    [
      "unmatched:0077bcdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077c098"
      ]
    ]
  ],
  "added": [
    [
      "0077c014",
      "DATA",
      [
        "storage",
        "00c793b0",
        null,
        "pointer"
      ]
    ],
    [
      "0077c0b4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ],
    [
      "0077c0b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077c098"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077bc30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077bc18.md#insn-0077bc30) · [`0077bcd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077bc18.md#insn-0077bcd8) · [`0077bcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077bc18.md#insn-0077bcdc)
- 新版 [`0077c00c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077bff4.md#insn-0077c00c)

~~~diff
- 0077bc30 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 0077c00c ["COPY", "register:4040:8", ["const:c79000:8"]]
- 0077bc30 bytes e82700b0
+ 0077c00c bytes e82700b0
- 0077bcd8 ["INT_ADD", "register:40f0:8", ["const:77bcd8:8", "const:4:8"]]
- 0077bcd8 ["CALL", null, ["callee:00c54d90:8"]]
- 0077bcd8 bytes 32601394
- 0077bcdc ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0077bcdc ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 0077bcdc bytes 00ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-830074e08485771823bea23ce1a446b5"></a>

### [`0077c08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c08c.md) → [`0077c468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077c468.md) FUN_0077c468

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0077bc18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077bc18.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0077bff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077bff4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c08c.md#insn-0077c09c)
- 新版 [`0077c478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077c468.md#insn-0077c478)

~~~diff
- 0077c09c ["INT_ADD", "register:40f0:8", ["const:77c09c:8", "const:4:8"]]
- 0077c09c ["CALL", null, ["callee:0077bff4:8"]]
+ 0077c478 ["INT_ADD", "register:40f0:8", ["const:77c478:8", "const:4:8"]]
+ 0077c478 ["CALL", null, ["callee:0077bff4:8"]]
- 0077c09c bytes dffeff97
+ 0077c478 bytes dffeff97
~~~


<a id="compare-1a77132ef251cc677291ff71aa51cda9"></a>

### [`0077c1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c1e8.md) → [`0077c5c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077c5c4.md) FUN_0077c5c4

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0075d7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d7b4.md) · 呼出先 8件 [`007260e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007260e4.md) [`007260f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007260f8.md) [`0072615c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/0072615c.md) [`0077c5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c5b4.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)
- 新版 呼出元 1件 [`0075db64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075db64.md) · 呼出先 8件 [`00726494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00726/00726494.md) [`007264a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00726/007264a8.md) [`0072650c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00726/0072650c.md) [`0077c990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077c990.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.50% / 新版 79.50%

CFGの説明率　旧版 27.84% / 新版 27.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 1件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 28件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c1ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c1ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c1f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0077c1ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077c1f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077c1f4",
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
      "0077c5c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0077c5cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0077c5d0",
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

- 旧版 [`0077c1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c1e8.md#insn-0077c1ec) · [`0077c1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c1e8.md#insn-0077c1f0) · [`0077c1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c1e8.md#insn-0077c1f4)

~~~diff
- 0077c1ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0077c1ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0077c1ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0077c1ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077c1ec bytes fd7b05a9
- 0077c1f0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0077c1f0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0077c1f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 0077c1f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077c1f0 bytes fc6f06a9
- 0077c1f4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0077c1f4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0077c1f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 0077c1f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077c1f4 bytes fa6707a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1e6e3a25ef5a0ba4f92374c48121f9c"></a>

### [`0077c838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c838.md) → [`0077cc14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc14.md) FUN_0077cc14

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0077cc18",
      "incomplete_value": false,
      "site": "0077cc1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077c83c",
      "incomplete_value": false,
      "site": "0077c840",
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
            "const:420:8"
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
      "0077cc1c",
      "DATA",
      [
        "storage",
        "00c78420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0077cc1c",
      "DATA",
      [
        "storage",
        "00c793f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077c838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c838.md#insn-0077c838) · [`0077c83c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c838.md#insn-0077c83c)
- 新版 [`0077cc14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc14.md#insn-0077cc14) · [`0077cc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc14.md#insn-0077cc18)

~~~diff
- 0077c838 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 0077cc14 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 0077c838 bytes e8270090
+ 0077cc14 bytes e82700b0
- 0077c83c ["COPY", "tmp:0:8", ["const:420:8"]]
- 0077c83c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077c83c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077c83c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077cc18 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 0077cc18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077cc18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077cc18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077c83c bytes 08811091
+ 0077cc18 bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f1396bdfc4337e51c911f17112a9dc7"></a>

### [`0077c8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c8a4.md) → [`0077cc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc80.md) FUN_0077cc80

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`007736f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007736f4.md) [`0078384c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/0078384c.md) [`0078392c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/0078392c.md) [`00a2f680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2f/00a2f680.md) [`00a2fedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2f/00a2fedc.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 8件 [`00773ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773ad0.md) [`00783c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/00783c28.md) [`00783d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/00783d08.md) [`00a30674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a30/00a30674.md) [`00a30ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a30/00a30ed0.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0077cc8c",
      "incomplete_value": false,
      "site": "0077cc90",
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
      "definition_site": "0077c8b0",
      "incomplete_value": false,
      "site": "0077c8b4",
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
      "0077cc8c",
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
      "0077cc8c",
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

- 旧版 [`0077c8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c8a4.md#insn-0077c8b4) · [`0077c8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c8a4.md#insn-0077c8ac) · [`0077c8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c8a4.md#insn-0077c8b0)
- 新版 [`0077cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc80.md#insn-0077cc90) · [`0077cc88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc80.md#insn-0077cc88) · [`0077cc8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc80.md#insn-0077cc8c)

~~~diff
- 0077c8b4 ["INT_ADD", "register:40f0:8", ["const:77c8b4:8", "const:4:8"]]
- 0077c8b4 ["CALL", null, ["callee:0043bad8:8"]]
+ 0077cc90 ["INT_ADD", "register:40f0:8", ["const:77cc90:8", "const:4:8"]]
+ 0077cc90 ["CALL", null, ["callee:0043bad8:8"]]
- 0077c8b4 bytes c1fbf297
+ 0077cc90 bytes 92fbf297
- 0077c8ac ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0077cc88 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0077c8ac bytes c0d9fff0
+ 0077cc88 bytes e0d9ff90
- 0077c8b0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0077c8b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0077c8b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0077c8b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0077cc8c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0077cc8c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0077cc8c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0077cc8c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0077c8b0 bytes 00303e91
+ 0077cc8c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f932c046374459743001311914334058"></a>

### [`0077c968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c968.md) → [`0077cd44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cd44.md) FUN_0077cd44

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0075e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075e91c.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0077caec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077caec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0075eccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075eccc.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0077cec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cec8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 44.44% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c9ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077ca44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0077cd88"
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
      "unmatched:0077c9ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077ca44",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0077cd88",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "0077ce20",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077c9ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c968.md#insn-0077c9ac) · [`0077ca44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c968.md#insn-0077ca44) · [`0077ca50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c968.md#insn-0077ca50)
- 新版 [`0077ce2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cd44.md#insn-0077ce2c)

~~~diff
- 0077c9ac ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0077c9ac ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0077c9ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0077c9ac bytes a9831ff8
- 0077ca44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 0077ca44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0077ca44 bytes ea0f00f9
- 0077ca50 ["INT_ADD", "register:40f0:8", ["const:77ca50:8", "const:4:8"]]
- 0077ca50 ["CALL", null, ["callee:0077cec8:8"]]
+ 0077ce2c ["INT_ADD", "register:40f0:8", ["const:77ce2c:8", "const:4:8"]]
+ 0077ce2c ["CALL", null, ["callee:0077cec8:8"]]
- 0077ca50 bytes 27000094
+ 0077ce2c bytes 27000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e61ddbbf6c1e28e1f2ee5f5376ad037f"></a>

### [`0077caec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077caec.md) → [`0077cec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cec8.md) FUN_0077cec8

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0077c968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c968.md) [`0077caec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077caec.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`0077cd44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cd44.md) [`0077cec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cec8.md) · 呼出先 21件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.91% / 新版 78.91%

CFGの説明率　旧版 39.71% / 新版 40.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_condition` 4件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 11件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077cb14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077cb18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077cb1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0077cb14",
      "WRITE",
      [
        "storage",
        "Stack[-0x184]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077cb18",
      "WRITE",
      [
        "storage",
        "Stack[-0x18c]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077cb1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x198]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0077cef0",
      "WRITE",
      [
        "storage",
        "Stack[-0x184]",
        null,
        null
      ]
    ],
    [
      "0077cef4",
      "WRITE",
      [
        "storage",
        "Stack[-0x18c]",
        null,
        null
      ]
    ],
    [
      "0077cef8",
      "WRITE",
      [
        "storage",
        "Stack[-0x198]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077cb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077caec.md#insn-0077cb14) · [`0077cb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077caec.md#insn-0077cb18) · [`0077cb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077caec.md#insn-0077cb1c)

~~~diff
- 0077cb14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:6c:8"]]
- 0077cb14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:4"]]
- 0077cb14 bytes e56f00b9
- 0077cb18 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:64:8"]]
- 0077cb18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
- 0077cb18 bytes e46700b9
- 0077cb1c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:58:8"]]
- 0077cb1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4018:8"]]
- 0077cb1c bytes e32f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52769e40d25f97d19570e619b70392d6"></a>

### [`0077d5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077d/0077d5d4.md) → [`0077d9b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077d/0077d9b0.md) FUN_0077d9b0

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0077caec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077caec.md) [`0077d5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077d/0077d5d4.md) · 呼出先 23件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`0077cec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cec8.md) [`0077d9b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077d/0077d9b0.md) · 呼出先 23件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.54% / 新版 88.54%

CFGの説明率　旧版 56.72% / 新版 57.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_condition` 2件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077d6d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077db5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077dc6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0077d6d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077d6d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077dac4"
      ]
    ],
    [
      "unmatched:0077d6f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077db24"
      ]
    ]
  ],
  "added": [
    [
      "0077daac",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "0077dab0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077dac4"
      ]
    ],
    [
      "0077dad0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077db24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077d6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077d/0077d5d4.md#insn-0077d6d0) · [`0077d6d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077d/0077d5d4.md#insn-0077d6d4) · [`0077d6f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077d/0077d5d4.md#insn-0077d6f4)

~~~diff
- 0077d6d0 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0077d6d0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd0:8"]]
- 0077d6d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0077d6d0 bytes a8031d38
- 0077d6d4 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 0077d6d4 bytes a0000054
- 0077d6f4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0077d6f4 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 0077d6f4 bytes a3020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-863547b081836fa6fc68d76dfd465742"></a>

### [`0077e13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077e/0077e13c.md) → [`0077e518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077e/0077e518.md) FUN_0077e518

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0077d5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077d/0077d5d4.md) [`0077e13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077e/0077e13c.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`0077d9b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077d/0077d9b0.md) [`0077e518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077e/0077e518.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.84% / 新版 84.84%

CFGの説明率　旧版 49.72% / 新版 52.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_condition` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077e140"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077e140"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077e144"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0077e140",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077e144",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077e148",
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
      "0077e51c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0077e520",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0077e524",
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

- 旧版 [`0077e140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077e/0077e13c.md#insn-0077e140) · [`0077e144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077e/0077e13c.md#insn-0077e144) · [`0077e148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077e/0077e13c.md#insn-0077e148)

~~~diff
- 0077e140 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0077e140 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0077e140 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 0077e140 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077e140 bytes fd7b13a9
- 0077e144 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0077e144 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0077e144 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 0077e144 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077e144 bytes fc6f14a9
- 0077e148 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0077e148 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0077e148 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 0077e148 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077e148 bytes fa6715a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-747a7d059d8e26c39fec6b8f96f60686"></a>

### [`0077eae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077e/0077eae8.md) → [`0077eec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077e/0077eec4.md) FUN_0077eec4

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0077e13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077e/0077e13c.md) [`0077eae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077e/0077eae8.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`0077e518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077e/0077e518.md) [`0077eec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077e/0077eec4.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.05% / 新版 88.05%

CFGの説明率　旧版 66.86% / 新版 67.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077f020"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077f024"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077f150"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0077ef90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0077f31c"
      ]
    ],
    [
      "0077f02c",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "0077f050",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0077ef90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077f6f8"
      ]
    ],
    [
      "0077f02c",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "0077f050",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077ec38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077e/0077eae8.md#insn-0077ec38) · [`0077ec48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077e/0077eae8.md#insn-0077ec48) · [`0077ec58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077e/0077eae8.md#insn-0077ec58)
- 新版 [`0077f014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077e/0077eec4.md#insn-0077f014) · [`0077f024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077e/0077eec4.md#insn-0077f024) · [`0077f034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077e/0077eec4.md#insn-0077f034)

~~~diff
- 0077ec38 ["CBRANCH", null, ["local:b44:8", "register:101:1"]]
+ 0077f014 ["CBRANCH", null, ["local:b45:8", "register:101:1"]]
- 0077ec38 bytes 00160054
+ 0077f014 bytes 00160054
- 0077ec48 ["CBRANCH", null, ["local:b44:8", "register:101:1"]]
+ 0077f024 ["CBRANCH", null, ["local:b45:8", "register:101:1"]]
- 0077ec48 bytes 80150054
+ 0077f024 bytes 80150054
- 0077ec58 ["INT_ADD", "register:40f0:8", ["const:77ec58:8", "const:4:8"]]
- 0077ec58 ["CALL", null, ["callee:004421f4:8"]]
+ 0077f034 ["INT_ADD", "register:40f0:8", ["const:77f034:8", "const:4:8"]]
+ 0077f034 ["CALL", null, ["callee:004421f4:8"]]
- 0077ec58 bytes 9f0cf397
+ 0077f034 bytes 700cf397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fc554a5f44b2709d727017022275a06"></a>

### [`0077f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077f/0077f46c.md) → [`0077f848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077f/0077f848.md) FUN_0077f848

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0077eae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077e/0077eae8.md) [`0077f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077f/0077f46c.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`0077eec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077e/0077eec4.md) [`0077f848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077f/0077f848.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.74% / 新版 79.74%

CFGの説明率　旧版 43.82% / 新版 43.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 28件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077f47c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077f47c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077f480"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0077f47c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077f480",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077f484",
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
      "0077f858",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0077f85c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0077f860",
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

- 旧版 [`0077f47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077f/0077f46c.md#insn-0077f47c) · [`0077f480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077f/0077f46c.md#insn-0077f480) · [`0077f484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077f/0077f46c.md#insn-0077f484)

~~~diff
- 0077f47c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0077f47c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0077f47c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 0077f47c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077f47c bytes f85f14a9
- 0077f480 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0077f480 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0077f480 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 0077f480 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077f480 bytes f65715a9
- 0077f484 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0077f484 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0077f484 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 0077f484 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0077f484 bytes f44f16a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0166023f8e50582b492b0513ac3014e"></a>

### [`0077fdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077f/0077fdd8.md) → [`007801b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00780/007801b4.md) FUN_007801b4

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0077f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077f/0077f46c.md) [`0077fdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077f/0077fdd8.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`0077f848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077f/0077f848.md) [`007801b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00780/007801b4.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00780318",
      "incomplete_value": false,
      "site": "00780320",
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
            "const:62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077ff3c",
      "incomplete_value": false,
      "site": "0077ff44",
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
            "const:f93:8"
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
      "definition_site": "0078033c",
      "incomplete_value": false,
      "site": "00780348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:f73:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077ff60",
      "incomplete_value": false,
      "site": "0077ff6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:f29:8"
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
      "definition_site": "00780470",
      "incomplete_value": false,
      "site": "00780478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:ef6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00780094",
      "incomplete_value": false,
      "site": "0078009c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:e27:8"
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
      "00780318",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "0078033c",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "00780470",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00780318",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "0078033c",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ],
    [
      "00780470",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077ff44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077f/0077fdd8.md#insn-0077ff44) · [`0077ff6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077f/0077fdd8.md#insn-0077ff6c) · [`0078009c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077f/0077fdd8.md#insn-0078009c)
- 新版 [`00780320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00780/007801b4.md#insn-00780320) · [`00780348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00780/007801b4.md#insn-00780348) · [`00780478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00780/007801b4.md#insn-00780478)

~~~diff
- 0077ff44 ["INT_ADD", "register:40f0:8", ["const:77ff44:8", "const:4:8"]]
- 0077ff44 ["CALL", null, ["callee:004421f4:8"]]
+ 00780320 ["INT_ADD", "register:40f0:8", ["const:780320:8", "const:4:8"]]
+ 00780320 ["CALL", null, ["callee:004421f4:8"]]
- 0077ff44 bytes e407f397
+ 00780320 bytes b507f397
- 0077ff6c ["INT_ADD", "register:40f0:8", ["const:77ff6c:8", "const:4:8"]]
- 0077ff6c ["CALL", null, ["callee:00442b54:8"]]
+ 00780348 ["INT_ADD", "register:40f0:8", ["const:780348:8", "const:4:8"]]
+ 00780348 ["CALL", null, ["callee:00442b54:8"]]
- 0077ff6c bytes 320af397
+ 00780348 bytes 030af397
- 0078009c ["INT_ADD", "register:40f0:8", ["const:78009c:8", "const:4:8"]]
- 0078009c ["CALL", null, ["callee:004421f4:8"]]
+ 00780478 ["INT_ADD", "register:40f0:8", ["const:780478:8", "const:4:8"]]
+ 00780478 ["CALL", null, ["callee:004421f4:8"]]
- 0078009c bytes 8e07f397
+ 00780478 bytes 5f07f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5867a84a0df91c8ea4593dc659cfacdb"></a>

### [`00780744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00780/00780744.md) → [`00780b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00780/00780b20.md) FUN_00780b20

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0077fdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077f/0077fdd8.md) [`00780744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00780/00780744.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`007801b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00780/007801b4.md) [`00780b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00780/00780b20.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00780c80",
      "incomplete_value": false,
      "site": "00780c88",
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
            "const:62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007808a4",
      "incomplete_value": false,
      "site": "007808ac",
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
            "const:f93:8"
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
      "definition_site": "00780ca4",
      "incomplete_value": false,
      "site": "00780cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:f73:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007808c8",
      "incomplete_value": false,
      "site": "007808d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:f29:8"
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
      "definition_site": "00780dd8",
      "incomplete_value": false,
      "site": "00780de0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:ef6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007809fc",
      "incomplete_value": false,
      "site": "00780a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:e27:8"
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
      "00780c80",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00780ca4",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "00780dd8",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00780c80",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "00780ca4",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ],
    [
      "00780dd8",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007808ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00780/00780744.md#insn-007808ac) · [`007808d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00780/00780744.md#insn-007808d4) · [`00780944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00780/00780744.md#insn-00780944)
- 新版 [`00780c88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00780/00780b20.md#insn-00780c88) · [`00780cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00780/00780b20.md#insn-00780cb0) · [`00780d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00780/00780b20.md#insn-00780d20)

~~~diff
- 007808ac ["INT_ADD", "register:40f0:8", ["const:7808ac:8", "const:4:8"]]
- 007808ac ["CALL", null, ["callee:004421f4:8"]]
+ 00780c88 ["INT_ADD", "register:40f0:8", ["const:780c88:8", "const:4:8"]]
+ 00780c88 ["CALL", null, ["callee:004421f4:8"]]
- 007808ac bytes 8a05f397
+ 00780c88 bytes 5b05f397
- 007808d4 ["INT_ADD", "register:40f0:8", ["const:7808d4:8", "const:4:8"]]
- 007808d4 ["CALL", null, ["callee:00442b54:8"]]
+ 00780cb0 ["INT_ADD", "register:40f0:8", ["const:780cb0:8", "const:4:8"]]
+ 00780cb0 ["CALL", null, ["callee:00442b54:8"]]
- 007808d4 bytes d807f397
+ 00780cb0 bytes a907f397
- 00780944 ["INT_ADD", "register:40f0:8", ["const:780944:8", "const:4:8"]]
- 00780944 ["CALL", null, ["callee:00c58f50:8"]]
+ 00780d20 ["INT_ADD", "register:40f0:8", ["const:780d20:8", "const:4:8"]]
+ 00780d20 ["CALL", null, ["callee:00c58f50:8"]]
- 00780944 bytes 8f5d1394
+ 00780d20 bytes 8c601394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c35a57fd72466c2ff73da1da103c9d7e"></a>

### [`0078109c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00781/0078109c.md) → [`00781478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00781/00781478.md) FUN_00781478

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00780744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00780/00780744.md) [`0078109c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00781/0078109c.md) [`00a5e534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a5e/00a5e534.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 3件 [`00780b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00780/00780b20.md) [`00781478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00781/00781478.md) [`00a5f528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a5f/00a5f528.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007815d8",
      "incomplete_value": false,
      "site": "007815e0",
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
            "const:62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007811fc",
      "incomplete_value": false,
      "site": "00781204",
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
            "const:f93:8"
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
      "definition_site": "007815fc",
      "incomplete_value": false,
      "site": "00781608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:f73:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00781220",
      "incomplete_value": false,
      "site": "0078122c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:f29:8"
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
      "definition_site": "00781730",
      "incomplete_value": false,
      "site": "00781738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:ef6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00781354",
      "incomplete_value": false,
      "site": "0078135c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:e27:8"
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
      "007815d8",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "007815fc",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "00781730",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007815d8",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "007815fc",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ],
    [
      "00781730",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00781204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00781/0078109c.md#insn-00781204) · [`0078122c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00781/0078109c.md#insn-0078122c) · [`0078135c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00781/0078109c.md#insn-0078135c)
- 新版 [`007815e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00781/00781478.md#insn-007815e0) · [`00781608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00781/00781478.md#insn-00781608) · [`00781738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00781/00781478.md#insn-00781738)

~~~diff
- 00781204 ["INT_ADD", "register:40f0:8", ["const:781204:8", "const:4:8"]]
- 00781204 ["CALL", null, ["callee:004421f4:8"]]
+ 007815e0 ["INT_ADD", "register:40f0:8", ["const:7815e0:8", "const:4:8"]]
+ 007815e0 ["CALL", null, ["callee:004421f4:8"]]
- 00781204 bytes 3403f397
+ 007815e0 bytes 0503f397
- 0078122c ["INT_ADD", "register:40f0:8", ["const:78122c:8", "const:4:8"]]
- 0078122c ["CALL", null, ["callee:00442b54:8"]]
+ 00781608 ["INT_ADD", "register:40f0:8", ["const:781608:8", "const:4:8"]]
+ 00781608 ["CALL", null, ["callee:00442b54:8"]]
- 0078122c bytes 8205f397
+ 00781608 bytes 5305f397
- 0078135c ["INT_ADD", "register:40f0:8", ["const:78135c:8", "const:4:8"]]
- 0078135c ["CALL", null, ["callee:004421f4:8"]]
+ 00781738 ["INT_ADD", "register:40f0:8", ["const:781738:8", "const:4:8"]]
+ 00781738 ["CALL", null, ["callee:004421f4:8"]]
- 0078135c bytes de02f397
+ 00781738 bytes af02f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0dae7eab3990e717b13885be9320e5b"></a>

### [`00781a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00781/00781a10.md) → [`00781dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00781/00781dec.md) FUN_00781dec

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00781e10",
      "incomplete_value": false,
      "site": "00781e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00781a34",
      "incomplete_value": false,
      "site": "00781a34",
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
            "const:470:8"
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
      "00781e10",
      "DATA",
      [
        "storage",
        "00c78470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00781e10",
      "DATA",
      [
        "storage",
        "00c79440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00781a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00781/00781a10.md#insn-00781a24) · [`00781a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00781/00781a10.md#insn-00781a2c) · [`00781a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00781/00781a10.md#insn-00781a30)
- 新版 [`00781e00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00781/00781dec.md#insn-00781e00) · [`00781e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00781/00781dec.md#insn-00781e08) · [`00781e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00781/00781dec.md#insn-00781e0c)

~~~diff
- 00781a24 ["INT_ADD", "register:40f0:8", ["const:781a24:8", "const:4:8"]]
- 00781a24 ["CALL", null, ["callee:00c58f30:8"]]
+ 00781e00 ["INT_ADD", "register:40f0:8", ["const:781e00:8", "const:4:8"]]
+ 00781e00 ["CALL", null, ["callee:00c58f30:8"]]
- 00781a24 bytes 4f591394
+ 00781e00 bytes 4c5c1394
- 00781a2c ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00781e08 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00781a2c bytes a82700f0
+ 00781e08 bytes c8270090
- 00781a30 ["COPY", "tmp:0:8", ["const:470:8"]]
- 00781a30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00781a30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00781a30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00781e0c ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00781e0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00781e0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00781e0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00781a30 bytes 08c11191
+ 00781e0c bytes 08011191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

