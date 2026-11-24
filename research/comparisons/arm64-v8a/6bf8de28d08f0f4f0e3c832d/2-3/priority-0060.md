# v16.0.2 → v16.0.3 · 最優先の変更候補 (60)

[一覧の目次](README.md)

<a id="compare-fc0340602a9dc6296bbf9c142f68c470"></a>

### [`009caa24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ca/009caa24.md) → [`009cb9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cb/009cb9d0.md) FUN_009cb9d0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009c60c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009c6/009c60c8.md) [`009caa24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ca/009caa24.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`009caa24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ca/009caa24.md) [`009cb9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cb9e0.md) [`009cbc14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbc14.md) [`009cbe7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbe7c.md)
- 新版 呼出元 2件 [`009c7074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009c7/009c7074.md) [`009cb9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cb/009cb9d0.md) · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`009cb9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cb/009cb9d0.md) [`009cc98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cc98c.md) [`009ccbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009ccbc0.md) [`009cce28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cce28.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.90% / 新版 99.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009cc964",
      "incomplete_value": false,
      "site": "009cc968",
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
      "definition_site": "009cb9b8",
      "incomplete_value": false,
      "site": "009cb9bc",
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
      "009cc964",
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
      "009cc964",
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

- 旧版 [`009cb9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ca/009caa24.md#insn-009cb9bc) · [`009caad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ca/009caa24.md#insn-009caad8) · [`009cab00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ca/009caa24.md#insn-009cab00)
- 新版 [`009cc968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cb/009cb9d0.md#insn-009cc968) · [`009cba84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cb/009cb9d0.md#insn-009cba84) · [`009cbaac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cb/009cb9d0.md#insn-009cbaac)

~~~diff
- 009cb9bc ["INT_ADD", "register:40f0:8", ["const:9cb9bc:8", "const:4:8"]]
- 009cb9bc ["CALL", null, ["callee:00442c90:8"]]
+ 009cc968 ["INT_ADD", "register:40f0:8", ["const:9cc968:8", "const:4:8"]]
+ 009cc968 ["CALL", null, ["callee:00442c90:8"]]
- 009cb9bc bytes eddbe997
+ 009cc968 bytes cad8e997
- 009caad8 ["INT_ADD", "register:40f0:8", ["const:9caad8:8", "const:4:8"]]
- 009caad8 ["CALL", null, ["callee:009ccbc0:8"]]
+ 009cba84 ["INT_ADD", "register:40f0:8", ["const:9cba84:8", "const:4:8"]]
+ 009cba84 ["CALL", null, ["callee:009ccbc0:8"]]
- 009caad8 bytes 4f040094
+ 009cba84 bytes 4f040094
- 009cab00 ["INT_ADD", "register:40f0:8", ["const:9cab00:8", "const:4:8"]]
- 009cab00 ["CALL", null, ["callee:009ccbc0:8"]]
+ 009cbaac ["INT_ADD", "register:40f0:8", ["const:9cbaac:8", "const:4:8"]]
+ 009cbaac ["CALL", null, ["callee:009ccbc0:8"]]
- 009cab00 bytes 45040094
+ 009cbaac bytes 45040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afa0521352eb30122312dfcf2adf0fd6"></a>

### [`009cb9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cb9e0.md) → [`009cc98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cc98c.md) FUN_009cc98c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009caa24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ca/009caa24.md) [`009cbe7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbe7c.md) · 呼出先 2件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`009cc118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc118.md)
- 新版 呼出元 2件 [`009cb9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cb/009cb9d0.md) [`009cce28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cce28.md) · 呼出先 2件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`009cd0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd0c4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.29% / 新版 99.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009ccb90",
      "incomplete_value": false,
      "site": "009ccb94",
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
      "definition_site": "009cbbe4",
      "incomplete_value": false,
      "site": "009cbbe8",
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
      "009ccb90",
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
      "009ccb90",
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

- 旧版 [`009cbbe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cb9e0.md#insn-009cbbe8) · [`009cba10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cb9e0.md#insn-009cba10) · [`009cbbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cb9e0.md#insn-009cbbe4)
- 新版 [`009ccb94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cc98c.md#insn-009ccb94) · [`009cc9bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cc98c.md#insn-009cc9bc) · [`009ccb90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cc98c.md#insn-009ccb90)

~~~diff
- 009cbbe8 ["INT_ADD", "register:40f0:8", ["const:9cbbe8:8", "const:4:8"]]
- 009cbbe8 ["CALL", null, ["callee:00442c90:8"]]
+ 009ccb94 ["INT_ADD", "register:40f0:8", ["const:9ccb94:8", "const:4:8"]]
+ 009ccb94 ["CALL", null, ["callee:00442c90:8"]]
- 009cbbe8 bytes 62dbe997
+ 009ccb94 bytes 3fd8e997
- 009cba10 ["INT_ADD", "register:40f0:8", ["const:9cba10:8", "const:4:8"]]
- 009cba10 ["CALL", null, ["callee:009cd0c4:8"]]
+ 009cc9bc ["INT_ADD", "register:40f0:8", ["const:9cc9bc:8", "const:4:8"]]
+ 009cc9bc ["CALL", null, ["callee:009cd0c4:8"]]
- 009cba10 bytes c2010094
+ 009cc9bc bytes c2010094
- 009cbbe4 ["COPY", "tmp:0:8", ["const:170:8"]]
- 009cbbe4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009cbbe4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009cbbe4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009ccb90 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 009ccb90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009ccb90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009ccb90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009cbbe4 bytes 00c00591
+ 009ccb90 bytes 00c00691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bf0e05df1437d27ff5244e08ebe299c"></a>

### [`009cbc14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbc14.md) → [`009ccbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009ccbc0.md) FUN_009ccbc0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009caa24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ca/009caa24.md) [`009cbe7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbe7c.md) [`009cc118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc118.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 3件 [`009cb9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cb/009cb9d0.md) [`009cce28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cce28.md) [`009cd0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd0c4.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.35% / 新版 99.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009ccde8",
      "incomplete_value": false,
      "site": "009ccdec",
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
      "definition_site": "009cbe3c",
      "incomplete_value": false,
      "site": "009cbe40",
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
      "009ccde8",
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
      "009ccde8",
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

- 旧版 [`009cbe40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbc14.md#insn-009cbe40) · [`009cbe3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbc14.md#insn-009cbe3c)
- 新版 [`009ccdec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009ccbc0.md#insn-009ccdec) · [`009ccde8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009ccbc0.md#insn-009ccde8)

~~~diff
- 009cbe40 ["INT_ADD", "register:40f0:8", ["const:9cbe40:8", "const:4:8"]]
- 009cbe40 ["CALL", null, ["callee:00442c90:8"]]
+ 009ccdec ["INT_ADD", "register:40f0:8", ["const:9ccdec:8", "const:4:8"]]
+ 009ccdec ["CALL", null, ["callee:00442c90:8"]]
- 009cbe40 bytes ccdae997
+ 009ccdec bytes a9d7e997
- 009cbe3c ["COPY", "tmp:0:8", ["const:170:8"]]
- 009cbe3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009cbe3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009cbe3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009ccde8 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 009ccde8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009ccde8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009ccde8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009cbe3c bytes 00c00591
+ 009ccde8 bytes 00c00691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6258e531415f924c7927bdf4b03d4f33"></a>

### [`009cbe7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbe7c.md) → [`009cce28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cce28.md) FUN_009cce28

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009caa24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ca/009caa24.md) · 呼出先 4件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`009cb9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cb9e0.md) [`009cbc14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbc14.md) [`009cc118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc118.md)
- 新版 呼出元 1件 [`009cb9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cb/009cb9d0.md) · 呼出先 4件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`009cc98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cc98c.md) [`009ccbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009ccbc0.md) [`009cd0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd0c4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.40% / 新版 99.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009cd038",
      "incomplete_value": false,
      "site": "009cd03c",
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
      "definition_site": "009cc08c",
      "incomplete_value": false,
      "site": "009cc090",
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
      "009cd038",
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
      "009cd038",
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

- 旧版 [`009cc090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbe7c.md#insn-009cc090) · [`009cbf14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbe7c.md#insn-009cbf14) · [`009cbf28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbe7c.md#insn-009cbf28)
- 新版 [`009cd03c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cce28.md#insn-009cd03c) · [`009ccec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cce28.md#insn-009ccec0) · [`009cced4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cce28.md#insn-009cced4)

~~~diff
- 009cc090 ["INT_ADD", "register:40f0:8", ["const:9cc090:8", "const:4:8"]]
- 009cc090 ["CALL", null, ["callee:00442c90:8"]]
+ 009cd03c ["INT_ADD", "register:40f0:8", ["const:9cd03c:8", "const:4:8"]]
+ 009cd03c ["CALL", null, ["callee:00442c90:8"]]
- 009cc090 bytes 38dae997
+ 009cd03c bytes 15d7e997
- 009cbf14 ["INT_ADD", "register:40f0:8", ["const:9cbf14:8", "const:4:8"]]
- 009cbf14 ["CALL", null, ["callee:009cc98c:8"]]
+ 009ccec0 ["INT_ADD", "register:40f0:8", ["const:9ccec0:8", "const:4:8"]]
+ 009ccec0 ["CALL", null, ["callee:009cc98c:8"]]
- 009cbf14 bytes b3feff97
+ 009ccec0 bytes b3feff97
- 009cbf28 ["INT_ADD", "register:40f0:8", ["const:9cbf28:8", "const:4:8"]]
- 009cbf28 ["CALL", null, ["callee:009ccbc0:8"]]
+ 009cced4 ["INT_ADD", "register:40f0:8", ["const:9cced4:8", "const:4:8"]]
+ 009cced4 ["CALL", null, ["callee:009ccbc0:8"]]
- 009cbf28 bytes 3bffff97
+ 009cced4 bytes 3bffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97d63df2d955183b06c12a49c80dc292"></a>

### [`009cc118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc118.md) → [`009cd0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd0c4.md) FUN_009cd0c4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009caa24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ca/009caa24.md) [`009cb9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cb9e0.md) [`009cbe7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbe7c.md) · 呼出先 2件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`009cbc14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cb/009cbc14.md)
- 新版 呼出元 3件 [`009cb9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cb/009cb9d0.md) [`009cc98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cc98c.md) [`009cce28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cce28.md) · 呼出先 2件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`009ccbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009ccbc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009cd24c",
      "incomplete_value": false,
      "site": "009cd250",
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
      "definition_site": "009cc2a0",
      "incomplete_value": false,
      "site": "009cc2a4",
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
      "009cd24c",
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
      "009cd24c",
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

- 旧版 [`009cc2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc118.md#insn-009cc2a4) · [`009cc144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc118.md#insn-009cc144) · [`009cc2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc118.md#insn-009cc2a0)
- 新版 [`009cd250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd0c4.md#insn-009cd250) · [`009cd0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd0c4.md#insn-009cd0f0) · [`009cd24c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd0c4.md#insn-009cd24c)

~~~diff
- 009cc2a4 ["INT_ADD", "register:40f0:8", ["const:9cc2a4:8", "const:4:8"]]
- 009cc2a4 ["CALL", null, ["callee:00442c90:8"]]
+ 009cd250 ["INT_ADD", "register:40f0:8", ["const:9cd250:8", "const:4:8"]]
+ 009cd250 ["CALL", null, ["callee:00442c90:8"]]
- 009cc2a4 bytes b3d9e997
+ 009cd250 bytes 90d6e997
- 009cc144 ["INT_ADD", "register:40f0:8", ["const:9cc144:8", "const:4:8"]]
- 009cc144 ["CALL", null, ["callee:009ccbc0:8"]]
+ 009cd0f0 ["INT_ADD", "register:40f0:8", ["const:9cd0f0:8", "const:4:8"]]
+ 009cd0f0 ["CALL", null, ["callee:009ccbc0:8"]]
- 009cc144 bytes b4feff97
+ 009cd0f0 bytes b4feff97
- 009cc2a0 ["COPY", "tmp:0:8", ["const:170:8"]]
- 009cc2a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009cc2a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009cc2a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009cd24c ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 009cd24c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009cd24c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009cd24c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009cc2a0 bytes 00c00591
+ 009cd24c bytes 00c00691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34f4ae82356eb99a065551bbb57acc85"></a>

### [`009cc2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc2d0.md) → [`009cd27c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd27c.md) _INIT_200

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009cd2b8",
      "incomplete_value": true,
      "site": "009cd2d4",
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
      "definition_site": "009cc30c",
      "incomplete_value": true,
      "site": "009cc328",
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
      "definition_site": "009cd2dc",
      "incomplete_value": true,
      "site": "009cd2f8",
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
      "definition_site": "009cc330",
      "incomplete_value": true,
      "site": "009cc34c",
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
      "definition_site": "009cd2fc",
      "incomplete_value": true,
      "site": "009cd318",
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
      "definition_site": "009cc350",
      "incomplete_value": true,
      "site": "009cc36c",
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
      "009cd2b8",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009cd2dc",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009cd2fc",
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
      "009cd2b8",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "009cd2dc",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "009cd2fc",
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

- 旧版 [`009cc504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc2d0.md#insn-009cc504) · [`009cc2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc2d0.md#insn-009cc2f8) · [`009cc2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc2d0.md#insn-009cc2fc)
- 新版 [`009cd4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd27c.md#insn-009cd4b0) · [`009cd2a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd27c.md#insn-009cd2a4) · [`009cd2a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd27c.md#insn-009cd2a8)

~~~diff
- 009cc504 ["INT_ADD", "register:40f0:8", ["const:9cc504:8", "const:4:8"]]
- 009cc504 ["CALL", null, ["callee:00c58ed0:8"]]
+ 009cd4b0 ["INT_ADD", "register:40f0:8", ["const:9cd4b0:8", "const:4:8"]]
+ 009cd4b0 ["CALL", null, ["callee:00c58ed0:8"]]
- 009cc504 bytes 7f2e0a94
+ 009cd4b0 bytes 882e0a94
- 009cc2f8 ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 009cd2a4 ["COPY", "register:4098:8", ["const:1124000:8"]]
- 009cc2f8 bytes b33a00f0
+ 009cd2a4 bytes b33a00f0
- 009cc2fc ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 009cc2fc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009cc2fc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009cc2fc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009cd2a8 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 009cd2a8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009cd2a8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009cd2a8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009cc2fc bytes 73023791
+ 009cd2a8 bytes 73023691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b8a3b619c152a683050d60ede7c511d"></a>

### [`009cc7f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc7f4.md) → [`009cd7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd7a0.md) _INIT_201

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009cd7dc",
      "incomplete_value": true,
      "site": "009cd7f8",
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
      "definition_site": "009cc830",
      "incomplete_value": true,
      "site": "009cc84c",
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
      "definition_site": "009cd800",
      "incomplete_value": true,
      "site": "009cd81c",
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
      "definition_site": "009cc854",
      "incomplete_value": true,
      "site": "009cc870",
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
      "definition_site": "009cd820",
      "incomplete_value": true,
      "site": "009cd83c",
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
      "definition_site": "009cc874",
      "incomplete_value": true,
      "site": "009cc890",
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
      "009cd7dc",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009cd800",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009cd820",
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
      "009cd7dc",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "009cd800",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "009cd820",
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

- 旧版 [`009cca28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc7f4.md#insn-009cca28) · [`009cc81c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc7f4.md#insn-009cc81c) · [`009cc820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009cc7f4.md#insn-009cc820)
- 新版 [`009cd9d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd7a0.md#insn-009cd9d4) · [`009cd7c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd7a0.md#insn-009cd7c8) · [`009cd7cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cd7a0.md#insn-009cd7cc)

~~~diff
- 009cca28 ["INT_ADD", "register:40f0:8", ["const:9cca28:8", "const:4:8"]]
- 009cca28 ["CALL", null, ["callee:00c58ed0:8"]]
+ 009cd9d4 ["INT_ADD", "register:40f0:8", ["const:9cd9d4:8", "const:4:8"]]
+ 009cd9d4 ["CALL", null, ["callee:00c58ed0:8"]]
- 009cca28 bytes 362d0a94
+ 009cd9d4 bytes 3f2d0a94
- 009cc81c ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 009cd7c8 ["COPY", "register:4098:8", ["const:1124000:8"]]
- 009cc81c bytes b33a00f0
+ 009cd7c8 bytes b33a00f0
- 009cc820 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 009cc820 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009cc820 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009cc820 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009cd7cc ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 009cd7cc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009cd7cc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009cd7cc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009cc820 bytes 73623791
+ 009cd7cc bytes 73623691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afe9dab02418d871a2c4a06686aca21a"></a>

### [`009d3b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3b48.md) → [`009d4af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d4/009d4af4.md) FUN_009d4af4

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`0075d7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d7b4.md) [`0089b2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089b2e4.md) [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) [`00911c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00911/00911c38.md) · 呼出先 65件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0046e578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e578.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md)
- 新版 呼出元 5件 [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) [`0075db64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075db64.md) [`0089c290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089c290.md) [`0089e4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089e/0089e4cc.md) [`00912be4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00912/00912be4.md) · 呼出先 65件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0046e898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046e898.md) [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 27件, `call_target` 7件, `store_destination` 21件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "009d5e90",
      "incomplete_value": false,
      "site": "009d5e90",
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
      "definition_site": "009d4ee4",
      "incomplete_value": false,
      "site": "009d4ee4",
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
    "ordinal": 208,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "009d5e94",
      "incomplete_value": false,
      "site": "009d5e94",
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
      "definition_site": "009d4ee8",
      "incomplete_value": false,
      "site": "009d4ee8",
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
    "ordinal": 209,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009d5e90",
      "incomplete_value": false,
      "site": "009d5e94",
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
      "definition_site": "009d4ee4",
      "incomplete_value": false,
      "site": "009d4ee8",
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
    "ordinal": 209,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009d4b40",
      "DATA",
      [
        "storage",
        "00393c13",
        null,
        "byte[59]"
      ]
    ],
    [
      "009d4b4c",
      "DATA",
      [
        "storage",
        "00393c04",
        null,
        "byte[59]"
      ]
    ],
    [
      "009d4c50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a355a8"
      ]
    ]
  ],
  "added": [
    [
      "009d4b40",
      "DATA",
      [
        "storage",
        "00393c13",
        null,
        "byte[43]"
      ]
    ],
    [
      "009d4b4c",
      "DATA",
      [
        "storage",
        "00393c04",
        null,
        "byte[43]"
      ]
    ],
    [
      "009d4c50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a3659c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d3ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3b48.md#insn-009d3ca4) · [`009d3f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3b48.md#insn-009d3f38) · [`009d3f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3b48.md#insn-009d3f48)
- 新版 [`009d4c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d4/009d4af4.md#insn-009d4c50) · [`009d4ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d4/009d4af4.md#insn-009d4ee4) · [`009d4ef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d4/009d4af4.md#insn-009d4ef4)

~~~diff
- 009d3ca4 ["INT_ADD", "register:40f0:8", ["const:9d3ca4:8", "const:4:8"]]
- 009d3ca4 ["CALL", null, ["ram:a355a8:8"]]
+ 009d4c50 ["INT_ADD", "register:40f0:8", ["const:9d4c50:8", "const:4:8"]]
+ 009d4c50 ["CALL", null, ["ram:a3659c:8"]]
- 009d3ca4 bytes 41860194
+ 009d4c50 bytes 53860194
- 009d3f38 ["INT_ADD", "register:40f0:8", ["const:9d3f38:8", "const:4:8"]]
- 009d3f38 ["CALL", null, ["callee:00a36be0:8"]]
+ 009d4ee4 ["INT_ADD", "register:40f0:8", ["const:9d4ee4:8", "const:4:8"]]
+ 009d4ee4 ["CALL", null, ["callee:00a36be0:8"]]
- 009d3f38 bytes 2d870194
+ 009d4ee4 bytes 3f870194
- 009d3f48 ["INT_ADD", "register:40f0:8", ["const:9d3f48:8", "const:4:8"]]
- 009d3f48 ["CALL", null, ["callee:00a37af8:8"]]
+ 009d4ef4 ["INT_ADD", "register:40f0:8", ["const:9d4ef4:8", "const:4:8"]]
+ 009d4ef4 ["CALL", null, ["callee:00a37af8:8"]]
- 009d3f48 bytes ef8a0194
+ 009d4ef4 bytes 018b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb975472b8c3233ab4bdbe9fe1a2e2c4"></a>

### [`009d7bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d7/009d7bd0.md) → [`009d8b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d8/009d8b7c.md) FUN_009d8b7c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) · 呼出先 28件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`006755f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00675/006755f8.md) [`006d18a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d18a0.md) [`007562fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00756/007562fc.md)
- 新版 呼出元 1件 [`00852a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852a10.md) · 呼出先 28件 [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`006759a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00675/006759a8.md) [`006d1c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1c50.md) [`007566ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00756/007566ac.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 85.28% / 新版 85.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 8件, `call_target` 6件, `store_destination` 10件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "009d8c5c",
      "incomplete_value": false,
      "site": "009d8c5c",
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
      "definition_site": "009d7cb0",
      "incomplete_value": false,
      "site": "009d7cb0",
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
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009d8c54",
      "incomplete_value": true,
      "site": "009d8c5c",
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
                "const:a38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009d7ca8",
      "incomplete_value": true,
      "site": "009d7cb0",
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
                "const:a78:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "009d8c60",
      "incomplete_value": true,
      "site": "009d8c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009d7cb4",
      "incomplete_value": true,
      "site": "009d7cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009d8bd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a1a7a4"
      ]
    ],
    [
      "009d8c54",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009d8c58",
      "READ",
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
      "009d8bd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a1b750"
      ]
    ],
    [
      "009d8c54",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "009d8c58",
      "READ",
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

- 旧版 [`009d7c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d7/009d7bd0.md#insn-009d7c2c) · [`009d7cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d7/009d7bd0.md#insn-009d7cb0) · [`009d7cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d7/009d7bd0.md#insn-009d7cb4)
- 新版 [`009d8bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d8/009d8b7c.md#insn-009d8bd8) · [`009d8c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d8/009d8b7c.md#insn-009d8c5c) · [`009d8c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d8/009d8b7c.md#insn-009d8c60)

~~~diff
- 009d7c2c ["INT_ADD", "register:40f0:8", ["const:9d7c2c:8", "const:4:8"]]
- 009d7c2c ["CALL", null, ["ram:a1a7a4:8"]]
+ 009d8bd8 ["INT_ADD", "register:40f0:8", ["const:9d8bd8:8", "const:4:8"]]
+ 009d8bd8 ["CALL", null, ["ram:a1b750:8"]]
- 009d7c2c bytes de0a0194
+ 009d8bd8 bytes de0a0194
- 009d7cb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 009d7cb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 009d8c5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a28:8"]]
+ 009d8c5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 009d7cb0 bytes 093505f9
+ 009d8c5c bytes 091505f9
- 009d7cb4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 009d7cb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 009d8c60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a38:8"]]
+ 009d8c60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 009d7cb4 bytes aa3e05f9
+ 009d8c60 bytes aa1e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cd9c42dfdca7874bee677e1702d81f2"></a>

### [`009d803c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d8/009d803c.md) → [`009d8fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d8/009d8fe8.md) FUN_009d8fe8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`009d7bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d7/009d7bd0.md) · 呼出先 21件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md)
- 新版 呼出元 2件 [`007bea00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007be/007bea00.md) [`009d8b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d8/009d8b7c.md) · 呼出先 21件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487dc4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.54% / 新版 96.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009d9048",
      "incomplete_value": false,
      "site": "009d9054",
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
      "definition_site": "009d809c",
      "incomplete_value": false,
      "site": "009d80a8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009d905c",
      "incomplete_value": true,
      "site": "009d906c",
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
                "const:1d5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009d80b0",
      "incomplete_value": true,
      "site": "009d80c0",
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
                "const:18b:8"
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
      "definition_site": "009d9070",
      "incomplete_value": true,
      "site": "009d9070",
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
      "definition_site": "009d80c4",
      "incomplete_value": true,
      "site": "009d80c4",
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
    "ordinal": 20,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009d9024",
      "DATA",
      [
        "storage",
        "0038daa8",
        null,
        "dword"
      ]
    ],
    [
      "009d9028",
      "DATA",
      [
        "storage",
        "0038dac8",
        "fde_0038dac8",
        "dword"
      ]
    ],
    [
      "009d902c",
      "DATA",
      [
        "storage",
        "0038dab0",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "009d9024",
      "DATA",
      [
        "storage",
        "0038daa8",
        null,
        "qword"
      ]
    ],
    [
      "009d9028",
      "DATA",
      [
        "storage",
        "0038dac8",
        null,
        "dword"
      ]
    ],
    [
      "009d902c",
      "DATA",
      [
        "storage",
        "0038dab0",
        "fde_0038dab0",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d80cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d8/009d803c.md#insn-009d80cc) · [`009d8448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d8/009d803c.md#insn-009d8448) · [`009d8084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d8/009d803c.md#insn-009d8084)
- 新版 [`009d9078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d8/009d8fe8.md#insn-009d9078) · [`009d93f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d8/009d8fe8.md#insn-009d93f4) · [`009d9030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d8/009d8fe8.md#insn-009d9030)

~~~diff
- 009d80cc ["INT_ADD", "register:40f0:8", ["const:9d80cc:8", "const:4:8"]]
- 009d80cc ["CALL", null, ["ram:802be4:8"]]
+ 009d9078 ["INT_ADD", "register:40f0:8", ["const:9d9078:8", "const:4:8"]]
+ 009d9078 ["CALL", null, ["ram:803b48:8"]]
- 009d80cc bytes c6aaf897
+ 009d9078 bytes b4aaf897
- 009d8448 ["INT_ADD", "register:40f0:8", ["const:9d8448:8", "const:4:8"]]
- 009d8448 ["CALL", null, ["ram:802be4:8"]]
+ 009d93f4 ["INT_ADD", "register:40f0:8", ["const:9d93f4:8", "const:4:8"]]
+ 009d93f4 ["CALL", null, ["ram:803b48:8"]]
- 009d8448 bytes e7a9f897
+ 009d93f4 bytes d5a9f897
- 009d8084 ["INT_ADD", "register:40f0:8", ["const:9d8084:8", "const:4:8"]]
- 009d8084 ["CALL", null, ["callee:00803674:8"]]
+ 009d9030 ["INT_ADD", "register:40f0:8", ["const:9d9030:8", "const:4:8"]]
+ 009d9030 ["CALL", null, ["callee:00803674:8"]]
- 009d8084 bytes a3a9f897
+ 009d9030 bytes 91a9f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce5940776e5060a2f6f44f9d81b40121"></a>

### [`009dc1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc1a0.md) → [`009dd14c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009dd14c.md) FUN_009dd14c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 10件 [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md) [`00b11188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11188.md)
- 新版 呼出元 1件 [`00b29fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b29/00b29fe4.md) · 呼出先 10件 [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md) [`00b1217c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b12/00b1217c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.97% / 新版 94.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009dd188",
      "incomplete_value": false,
      "site": "009dd190",
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
      "definition_site": "009dc1dc",
      "incomplete_value": false,
      "site": "009dc1e4",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009dd1b4",
      "incomplete_value": true,
      "site": "009dd1b4",
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
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:f5c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dc208",
      "incomplete_value": true,
      "site": "009dc208",
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
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:e7e:8"
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
      "definition_site": "009dd294",
      "incomplete_value": true,
      "site": "009dd294",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:77d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dc2e8",
      "incomplete_value": true,
      "site": "009dc2e8",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:6b2:8"
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
      "009dd190",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009dd1a8",
      "READ",
      [
        "storage",
        "002bce7e",
        null,
        "string"
      ]
    ],
    [
      "009dd284",
      "READ",
      [
        "storage",
        "002a26b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009dd190",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "009dd1a8",
      "READ",
      [
        "storage",
        "002bcf5c",
        null,
        "string"
      ]
    ],
    [
      "009dd284",
      "READ",
      [
        "storage",
        "002a277d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dc1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc1a0.md#insn-009dc1d4) · [`009dc1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc1a0.md#insn-009dc1d8) · [`009dc1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc1a0.md#insn-009dc1dc)
- 新版 [`009dd180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009dd14c.md#insn-009dd180) · [`009dd184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009dd14c.md#insn-009dd184) · [`009dd188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009dd14c.md#insn-009dd188)

~~~diff
- 009dc1d4 ["INT_ADD", "register:40f0:8", ["const:9dc1d4:8", "const:4:8"]]
- 009dc1d4 ["CALL", null, ["callee:00488180:8"]]
+ 009dd180 ["INT_ADD", "register:40f0:8", ["const:9dd180:8", "const:4:8"]]
+ 009dd180 ["CALL", null, ["callee:00488180:8"]]
- 009dc1d4 bytes 23afea97
+ 009dd180 bytes 00acea97
- 009dc1d8 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 009dd184 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 009dc1d8 bytes 48140090
+ 009dd184 bytes 48140090
- 009dc1dc ["COPY", "tmp:0:8", ["const:e08:8"]]
- 009dc1dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009dc1dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009dc1dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009dd188 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 009dd188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009dd188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009dd188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009dc1dc bytes 08213891
+ 009dd188 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f92b54ac9d4ab2fc5e65fca9714b982"></a>

### [`009dc744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc744.md) → [`009dd6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009dd6f0.md) FUN_009dd6f0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 14件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)
- 新版 呼出元 1件 [`00b29fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b29/00b29fe4.md) · 呼出先 14件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487dc4.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.80% / 新版 93.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009dd738",
      "incomplete_value": false,
      "site": "009dd740",
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
      "definition_site": "009dc78c",
      "incomplete_value": false,
      "site": "009dc794",
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
    "kind": "store_value",
    "new": {
      "definition_site": "009dd764",
      "incomplete_value": true,
      "site": "009dd764",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:b66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dc7b8",
      "incomplete_value": true,
      "site": "009dc7b8",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:a9b:8"
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
      "definition_site": "009dda08",
      "incomplete_value": true,
      "site": "009dda0c",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dca5c",
      "incomplete_value": true,
      "site": "009dca60",
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
            "const:10:8"
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
      "009dd740",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009dd758",
      "READ",
      [
        "storage",
        "002a4a9b",
        null,
        "string"
      ]
    ],
    [
      "009dd7ec",
      "READ",
      [
        "storage",
        "002c4070",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "009dd740",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "009dd758",
      "READ",
      [
        "storage",
        "002a4b66",
        null,
        "string"
      ]
    ],
    [
      "009dd7ec",
      "READ",
      [
        "storage",
        "002c40c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dc784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc744.md#insn-009dc784) · [`009dc788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc744.md#insn-009dc788) · [`009dc78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc744.md#insn-009dc78c)
- 新版 [`009dd730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009dd6f0.md#insn-009dd730) · [`009dd734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009dd6f0.md#insn-009dd734) · [`009dd738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009dd6f0.md#insn-009dd738)

~~~diff
- 009dc784 ["INT_ADD", "register:40f0:8", ["const:9dc784:8", "const:4:8"]]
- 009dc784 ["CALL", null, ["callee:00488180:8"]]
+ 009dd730 ["INT_ADD", "register:40f0:8", ["const:9dd730:8", "const:4:8"]]
+ 009dd730 ["CALL", null, ["callee:00488180:8"]]
- 009dc784 bytes b7adea97
+ 009dd730 bytes 94aaea97
- 009dc788 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 009dd734 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 009dc788 bytes 48140090
+ 009dd734 bytes 48140090
- 009dc78c ["COPY", "tmp:0:8", ["const:e08:8"]]
- 009dc78c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009dc78c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009dc78c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009dd738 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 009dd738 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009dd738 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009dd738 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009dc78c bytes 08213891
+ 009dd738 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e72b5eaf07e58ecd616a9c8efa40a556"></a>

### [`009dcbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dcbb8.md) → [`009ddb64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009ddb64.md) FUN_009ddb64

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 11件 [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488598.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)
- 新版 呼出元 1件 [`00b29fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b29/00b29fe4.md) · 呼出先 11件 [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004888b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004888b8.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md)

変更の種類 comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ddba4",
      "incomplete_value": false,
      "site": "009ddbac",
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
      "definition_site": "009dcbf8",
      "incomplete_value": false,
      "site": "009dcc00",
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
      "definition_site": "009ddbcc",
      "incomplete_value": true,
      "site": "009ddbcc",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:e70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dcc20",
      "incomplete_value": true,
      "site": "009dcc20",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:da3:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dcda4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009ddbac",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009ddbc0",
      "READ",
      [
        "storage",
        "002acda3",
        null,
        "string"
      ]
    ],
    [
      "009ddc04",
      "READ",
      [
        "storage",
        "002c4070",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "009ddbac",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "009ddbc0",
      "READ",
      [
        "storage",
        "002ace70",
        null,
        "string"
      ]
    ],
    [
      "009ddc04",
      "READ",
      [
        "storage",
        "002c40c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dcda4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dcbb8.md#insn-009dcda4) · [`009dcda8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dcbb8.md#insn-009dcda8) · [`009dcdb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dcbb8.md#insn-009dcdb4)

~~~diff
- 009dcda4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 009dcda4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009dcda4 bytes e80f00f9
- 009dcda8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 009dcda8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 009dcda8 bytes e93300f9
- 009dcdb4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009dcdb4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 009dcdb4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 009dcdb4 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 009dcdb4 bytes 696a28f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5929fd50f4b972dda5653ef1256cd3b1"></a>

### [`009dd02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd02c.md) → [`009ddfd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009ddfd8.md) FUN_009ddfd8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`007562fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00756/007562fc.md) [`0082cd54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082cd54.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085bbc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085bbc8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 5件 [`007566ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00756/007566ac.md) [`0082dd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082d/0082dd00.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`0085cb74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085cb74.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.27% / 新版 87.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "009de014",
      "incomplete_value": true,
      "site": "009de014",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dd068",
      "incomplete_value": true,
      "site": "009dd068",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009de008",
      "incomplete_value": true,
      "site": "009de014",
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
                "const:a38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dd05c",
      "incomplete_value": true,
      "site": "009dd068",
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
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "009de018",
      "incomplete_value": true,
      "site": "009de018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dd06c",
      "incomplete_value": true,
      "site": "009dd06c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
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
      "009de008",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009de00c",
      "READ",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ],
    [
      "009de014",
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
      "009de008",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "009de00c",
      "READ",
      [
        "storage",
        "00ca5a28",
        null,
        "undefined8"
      ]
    ],
    [
      "009de014",
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

- 旧版 [`009dd068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd02c.md#insn-009dd068) · [`009dd06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd02c.md#insn-009dd06c) · [`009dd07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd02c.md#insn-009dd07c)
- 新版 [`009de014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009ddfd8.md#insn-009de014) · [`009de018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009ddfd8.md#insn-009de018) · [`009de028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009ddfd8.md#insn-009de028)

~~~diff
- 009dd068 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 009dd068 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 009de014 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a28:8"]]
+ 009de014 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 009dd068 bytes 093505f9
+ 009de014 bytes 091505f9
- 009dd06c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 009dd06c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 009de018 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a38:8"]]
+ 009de018 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 009dd06c bytes aa3e05f9
+ 009de018 bytes aa1e05f9
- 009dd07c ["INT_ADD", "register:40f0:8", ["const:9dd07c:8", "const:4:8"]]
- 009dd07c ["CALL", null, ["ram:7562fc:8"]]
+ 009de028 ["INT_ADD", "register:40f0:8", ["const:9de028:8", "const:4:8"]]
+ 009de028 ["CALL", null, ["ram:7566ac:8"]]
- 009dd07c bytes a0e4f597
+ 009de028 bytes a1e1f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da2528ea9a7ea68e495c49fb747c00c9"></a>

### [`009dd144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd144.md) → [`009de0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de0f0.md) FUN_009de0f0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009d5d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d5/009d5d4c.md) [`009d7a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d7/009d7a80.md) [`00a1a7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a7a4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`009d6cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d6/009d6cf8.md) [`009d8a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d8/009d8a2c.md) [`00a1b750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b750.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009de0fc",
      "incomplete_value": false,
      "site": "009de100",
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
      "definition_site": "009dd150",
      "incomplete_value": false,
      "site": "009dd154",
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
      "009de0fc",
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
      "009de0fc",
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

- 旧版 [`009dd154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd144.md#insn-009dd154) · [`009dd14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd144.md#insn-009dd14c) · [`009dd150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd144.md#insn-009dd150)
- 新版 [`009de100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de0f0.md#insn-009de100) · [`009de0f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de0f0.md#insn-009de0f8) · [`009de0fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de0f0.md#insn-009de0fc)

~~~diff
- 009dd154 ["INT_ADD", "register:40f0:8", ["const:9dd154:8", "const:4:8"]]
- 009dd154 ["CALL", null, ["callee:0043bad8:8"]]
+ 009de100 ["INT_ADD", "register:40f0:8", ["const:9de100:8", "const:4:8"]]
+ 009de100 ["CALL", null, ["callee:0043bad8:8"]]
- 009dd154 bytes 9979e997
+ 009de100 bytes 7676e997
- 009dd14c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009de0f8 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009dd14c bytes c0c6ffd0
+ 009de0f8 bytes c0c6ffd0
- 009dd150 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009dd150 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009dd150 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009dd150 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009de0fc ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009de0fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009de0fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009de0fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009dd150 bytes 00303e91
+ 009de0fc bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f688a735b902b3cd4e1327cb7225bc0"></a>

### [`009dd158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd158.md) → [`009de104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de104.md) FUN_009de104

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009d9980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d9/009d9980.md) [`009dd158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd158.md) [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 3件 [`009da92c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009da/009da92c.md) [`009de104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de104.md) [`00a48f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a48/00a48f48.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.50% / 新版 98.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009de260",
      "incomplete_value": false,
      "site": "009de268",
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
      "definition_site": "009dd2b4",
      "incomplete_value": false,
      "site": "009dd2bc",
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
      "definition_site": "009de3b8",
      "incomplete_value": false,
      "site": "009de3c0",
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
      "definition_site": "009dd40c",
      "incomplete_value": false,
      "site": "009dd414",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009de3d0",
      "incomplete_value": false,
      "site": "009de3dc",
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
      "definition_site": "009dd424",
      "incomplete_value": false,
      "site": "009dd430",
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
      "009de260",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "009de284",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "009de3b8",
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
      "009de260",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "009de284",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ],
    [
      "009de3b8",
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

- 旧版 [`009dd2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd158.md#insn-009dd2bc) · [`009dd414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd158.md#insn-009dd414) · [`009dd430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd158.md#insn-009dd430)
- 新版 [`009de268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de104.md#insn-009de268) · [`009de3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de104.md#insn-009de3c0) · [`009de3dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de104.md#insn-009de3dc)

~~~diff
- 009dd2bc ["INT_ADD", "register:40f0:8", ["const:9dd2bc:8", "const:4:8"]]
- 009dd2bc ["CALL", null, ["callee:004421f4:8"]]
+ 009de268 ["INT_ADD", "register:40f0:8", ["const:9de268:8", "const:4:8"]]
+ 009de268 ["CALL", null, ["callee:004421f4:8"]]
- 009dd2bc bytes 0693e997
+ 009de268 bytes e38fe997
- 009dd414 ["INT_ADD", "register:40f0:8", ["const:9dd414:8", "const:4:8"]]
- 009dd414 ["CALL", null, ["callee:004421f4:8"]]
+ 009de3c0 ["INT_ADD", "register:40f0:8", ["const:9de3c0:8", "const:4:8"]]
+ 009de3c0 ["CALL", null, ["callee:004421f4:8"]]
- 009dd414 bytes b092e997
+ 009de3c0 bytes 8d8fe997
- 009dd430 ["INT_ADD", "register:40f0:8", ["const:9dd430:8", "const:4:8"]]
- 009dd430 ["CALL", null, ["callee:00442b54:8"]]
+ 009de3dc ["INT_ADD", "register:40f0:8", ["const:9de3dc:8", "const:4:8"]]
+ 009de3dc ["CALL", null, ["callee:00442b54:8"]]
- 009dd430 bytes 0195e997
+ 009de3dc bytes de91e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e05be9375f606726bf1b84be8529937"></a>

### [`009dd970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd970.md) → [`009de91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de91c.md) FUN_009de91c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009d803c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d8/009d803c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`009d8fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d8/009d8fe8.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009de928",
      "incomplete_value": false,
      "site": "009de92c",
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
      "definition_site": "009dd97c",
      "incomplete_value": false,
      "site": "009dd980",
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
      "009de928",
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
      "009de928",
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

- 旧版 [`009dd980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd970.md#insn-009dd980) · [`009dd978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd970.md#insn-009dd978) · [`009dd97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd970.md#insn-009dd97c)
- 新版 [`009de92c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de91c.md#insn-009de92c) · [`009de924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de91c.md#insn-009de924) · [`009de928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de91c.md#insn-009de928)

~~~diff
- 009dd980 ["INT_ADD", "register:40f0:8", ["const:9dd980:8", "const:4:8"]]
- 009dd980 ["CALL", null, ["callee:0043bad8:8"]]
+ 009de92c ["INT_ADD", "register:40f0:8", ["const:9de92c:8", "const:4:8"]]
+ 009de92c ["CALL", null, ["callee:0043bad8:8"]]
- 009dd980 bytes 8e77e997
+ 009de92c bytes 6b74e997
- 009dd978 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009de924 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009dd978 bytes c0c6ffd0
+ 009de924 bytes c0c6ffd0
- 009dd97c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009dd97c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009dd97c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009dd97c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009de928 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009de928 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009de928 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009de928 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009dd97c bytes 00303e91
+ 009de928 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a91f5b1192aeceb6820f15801e294376"></a>

### [`009dd984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd984.md) → [`009de930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de930.md) FUN_009de930

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009d803c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d8/009d803c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`009d8fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d8/009d8fe8.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009de93c",
      "incomplete_value": false,
      "site": "009de940",
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
      "definition_site": "009dd990",
      "incomplete_value": false,
      "site": "009dd994",
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
      "009de93c",
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
      "009de93c",
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

- 旧版 [`009dd994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd984.md#insn-009dd994) · [`009dd98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd984.md#insn-009dd98c) · [`009dd990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd984.md#insn-009dd990)
- 新版 [`009de940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de930.md#insn-009de940) · [`009de938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de930.md#insn-009de938) · [`009de93c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de930.md#insn-009de93c)

~~~diff
- 009dd994 ["INT_ADD", "register:40f0:8", ["const:9dd994:8", "const:4:8"]]
- 009dd994 ["CALL", null, ["callee:0043bad8:8"]]
+ 009de940 ["INT_ADD", "register:40f0:8", ["const:9de940:8", "const:4:8"]]
+ 009de940 ["CALL", null, ["callee:0043bad8:8"]]
- 009dd994 bytes 8977e997
+ 009de940 bytes 6674e997
- 009dd98c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009de938 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009dd98c bytes c0c6ffd0
+ 009de938 bytes c0c6ffd0
- 009dd990 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009dd990 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009dd990 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009dd990 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009de93c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009de93c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009de93c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009de93c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009dd990 bytes 00303e91
+ 009de93c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0045288154685a387b34774b353fb2c3"></a>

### [`009dd998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd998.md) → [`009de944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de944.md) _INIT_202

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009de9e4",
      "incomplete_value": true,
      "site": "009de9fc",
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
      "definition_site": "009dda38",
      "incomplete_value": true,
      "site": "009dda50",
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
      "definition_site": "009dea00",
      "incomplete_value": true,
      "site": "009dea1c",
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
      "definition_site": "009dda54",
      "incomplete_value": true,
      "site": "009dda70",
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
      "definition_site": "009dea20",
      "incomplete_value": true,
      "site": "009dea3c",
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
      "definition_site": "009dda74",
      "incomplete_value": true,
      "site": "009dda90",
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
      "009de980",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009de9a4",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009de9c4",
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
      "009de980",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "009de9a4",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "009de9c4",
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

- 旧版 [`009ddbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd998.md#insn-009ddbcc) · [`009dd9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd998.md#insn-009dd9c0) · [`009dd9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd998.md#insn-009dd9c4)
- 新版 [`009deb78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de944.md#insn-009deb78) · [`009de96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de944.md#insn-009de96c) · [`009de970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de944.md#insn-009de970)

~~~diff
- 009ddbcc ["INT_ADD", "register:40f0:8", ["const:9ddbcc:8", "const:4:8"]]
- 009ddbcc ["CALL", null, ["callee:00c58ed0:8"]]
+ 009deb78 ["INT_ADD", "register:40f0:8", ["const:9deb78:8", "const:4:8"]]
+ 009deb78 ["CALL", null, ["callee:00c58ed0:8"]]
- 009ddbcc bytes cde80994
+ 009deb78 bytes d6e80994
- 009dd9c0 ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 009de96c ["COPY", "register:4098:8", ["const:1124000:8"]]
- 009dd9c0 bytes 333a00d0
+ 009de96c bytes 333a00d0
- 009dd9c4 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 009dd9c4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009dd9c4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009dd9c4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009de970 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 009de970 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009de970 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009de970 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009dd9c4 bytes 73c23791
+ 009de970 bytes 73c23691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d98b1a67ac64b89cfd4f797a83b3f98"></a>

### [`009ddd34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009ddd34.md) → [`009dece0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009dece0.md) FUN_009dece0

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 18件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)
- 新版 呼出元 1件 [`00b29fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b29/00b29fe4.md) · 呼出先 18件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.00% / 新版 91.00%

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
      "definition_site": "009ded20",
      "incomplete_value": false,
      "site": "009ded2c",
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
      "definition_site": "009ddd74",
      "incomplete_value": false,
      "site": "009ddd80",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ded54",
      "incomplete_value": true,
      "site": "009ded64",
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
                "const:6d9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ddda8",
      "incomplete_value": true,
      "site": "009dddb8",
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
                "const:699:8"
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
      "definition_site": "009ded68",
      "incomplete_value": true,
      "site": "009ded68",
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
      "definition_site": "009dddbc",
      "incomplete_value": true,
      "site": "009dddbc",
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
      "009ded2c",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009ded54",
      "READ",
      [
        "storage",
        "0029f699",
        null,
        "string"
      ]
    ],
    [
      "009ded58",
      "READ",
      [
        "storage",
        "0029f6a8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ded2c",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "009ded54",
      "READ",
      [
        "storage",
        "0029f6d9",
        null,
        "string"
      ]
    ],
    [
      "009ded58",
      "READ",
      [
        "storage",
        "0029f6e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ddd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009ddd34.md#insn-009ddd68) · [`009ddd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009ddd34.md#insn-009ddd70) · [`009ddd74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009ddd34.md#insn-009ddd74)
- 新版 [`009ded14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009dece0.md#insn-009ded14) · [`009ded1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009dece0.md#insn-009ded1c) · [`009ded20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009dece0.md#insn-009ded20)

~~~diff
- 009ddd68 ["INT_ADD", "register:40f0:8", ["const:9ddd68:8", "const:4:8"]]
- 009ddd68 ["CALL", null, ["callee:00488180:8"]]
+ 009ded14 ["INT_ADD", "register:40f0:8", ["const:9ded14:8", "const:4:8"]]
+ 009ded14 ["CALL", null, ["callee:00488180:8"]]
- 009ddd68 bytes 3ea8ea97
+ 009ded14 bytes 1ba5ea97
- 009ddd70 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 009ded1c ["COPY", "register:4040:8", ["const:c65000:8"]]
- 009ddd70 bytes 281400f0
+ 009ded1c bytes 281400f0
- 009ddd74 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 009ddd74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ddd74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ddd74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ded20 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 009ded20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ded20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ded20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ddd74 bytes 08213891
+ 009ded20 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e252e0986cba1d7911e955d5430b1b5"></a>

### [`009de0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de0d4.md) → [`009df080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009df/009df080.md) FUN_009df080

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a87b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a87/00a87b40.md) · 呼出先 3件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`00a88b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a88/00a88b34.md) · 呼出先 3件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

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
      "site": "009df0a4",
      "value": [
        "leaf",
        "ram:48d058:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009de0f8",
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
      "009df0a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ],
  "added": [
    [
      "009df0a4",
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

- 旧版 [`009de0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de0d4.md#insn-009de0f8) · [`009de0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de0d4.md#insn-009de0fc) · [`009de110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de0d4.md#insn-009de110)
- 新版 [`009df0a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009df/009df080.md#insn-009df0a4) · [`009df0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009df/009df080.md#insn-009df0a8) · [`009df0bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009df/009df080.md#insn-009df0bc)

~~~diff
- 009de0f8 ["INT_ADD", "register:40f0:8", ["const:9de0f8:8", "const:4:8"]]
- 009de0f8 ["CALL", null, ["ram:48cd38:8"]]
+ 009df0a4 ["INT_ADD", "register:40f0:8", ["const:9df0a4:8", "const:4:8"]]
+ 009df0a4 ["CALL", null, ["ram:48d058:8"]]
- 009de0f8 bytes 10bbea97
+ 009df0a4 bytes edb7ea97
- 009de0fc ["INT_ADD", "register:40f0:8", ["const:9de0fc:8", "const:4:8"]]
- 009de0fc ["CALL", null, ["callee:0048d1e4:8"]]
+ 009df0a8 ["INT_ADD", "register:40f0:8", ["const:9df0a8:8", "const:4:8"]]
+ 009df0a8 ["CALL", null, ["callee:0048d1e4:8"]]
- 009de0fc bytes 72bbea97
+ 009df0a8 bytes 4fb8ea97
- 009de110 ["INT_ADD", "register:40f0:8", ["const:9de110:8", "const:4:8"]]
- 009de110 ["CALL", null, ["callee:008524fc:8"]]
+ 009df0bc ["INT_ADD", "register:40f0:8", ["const:9df0bc:8", "const:4:8"]]
+ 009df0bc ["CALL", null, ["callee:008524fc:8"]]
- 009de110 bytes 10cdf997
+ 009df0bc bytes 10cdf997
~~~


<a id="compare-73ecbb4e2c6bdf22924c30bf3bc91bd7"></a>

### [`009de664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de664.md) → [`009df610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009df/009df610.md) FUN_009df610

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`007dd3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007dd/007dd3bc.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a84c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a84/00a84c60.md) [`00a84df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a84/00a84df8.md)
- 新版 呼出元 2件 [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) [`007de320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007de/007de320.md) · 呼出先 3件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00a85c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a85/00a85c54.md) [`00a85dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a85/00a85dec.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

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
      "site": "009df63c",
      "value": [
        "leaf",
        "ram:a85dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009de690",
      "value": [
        "leaf",
        "ram:a84df8:8"
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
      "site": "009df658",
      "value": [
        "leaf",
        "ram:a85dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009de6ac",
      "value": [
        "leaf",
        "ram:a84df8:8"
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
      "009df63c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84df8"
      ]
    ],
    [
      "009df658",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84df8"
      ]
    ]
  ],
  "added": [
    [
      "009df63c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a85dec"
      ]
    ],
    [
      "009df658",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a85dec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009de690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de664.md#insn-009de690) · [`009de6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de664.md#insn-009de6ac) · [`009de680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de664.md#insn-009de680)
- 新版 [`009df63c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009df/009df610.md#insn-009df63c) · [`009df658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009df/009df610.md#insn-009df658) · [`009df62c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009df/009df610.md#insn-009df62c)

~~~diff
- 009de690 ["INT_ADD", "register:40f0:8", ["const:9de690:8", "const:4:8"]]
- 009de690 ["CALL", null, ["ram:a84df8:8"]]
+ 009df63c ["INT_ADD", "register:40f0:8", ["const:9df63c:8", "const:4:8"]]
+ 009df63c ["CALL", null, ["ram:a85dec:8"]]
- 009de690 bytes da990294
+ 009df63c bytes ec990294
- 009de6ac ["INT_ADD", "register:40f0:8", ["const:9de6ac:8", "const:4:8"]]
- 009de6ac ["CALL", null, ["ram:a84df8:8"]]
+ 009df658 ["INT_ADD", "register:40f0:8", ["const:9df658:8", "const:4:8"]]
+ 009df658 ["CALL", null, ["ram:a85dec:8"]]
- 009de6ac bytes d3990294
+ 009df658 bytes e5990294
- 009de680 ["INT_ADD", "register:40f0:8", ["const:9de680:8", "const:4:8"]]
- 009de680 ["CALL", null, ["callee:008524fc:8"]]
+ 009df62c ["INT_ADD", "register:40f0:8", ["const:9df62c:8", "const:4:8"]]
+ 009df62c ["CALL", null, ["callee:008524fc:8"]]
- 009de680 bytes b4cbf997
+ 009df62c bytes b4cbf997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfdf3a2ac82343a7922d8cd68ec23449"></a>

### [`009de8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de8e4.md) → [`009df890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009df/009df890.md) _INIT_203

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009df8cc",
      "incomplete_value": true,
      "site": "009df8e8",
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
      "definition_site": "009de920",
      "incomplete_value": true,
      "site": "009de93c",
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
      "definition_site": "009df8f0",
      "incomplete_value": true,
      "site": "009df90c",
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
      "definition_site": "009de944",
      "incomplete_value": true,
      "site": "009de960",
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
      "definition_site": "009df910",
      "incomplete_value": true,
      "site": "009df92c",
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
      "definition_site": "009de964",
      "incomplete_value": true,
      "site": "009de980",
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
      "009df8cc",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009df8f0",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009df910",
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
      "009df8cc",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "009df8f0",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "009df910",
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

- 旧版 [`009dea44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de8e4.md#insn-009dea44) · [`009deb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de8e4.md#insn-009deb18) · [`009de90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de8e4.md#insn-009de90c)
- 新版 [`009df9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009df/009df890.md#insn-009df9f0) · [`009dfac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009df/009df890.md#insn-009dfac4) · [`009df8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009df/009df890.md#insn-009df8b8)

~~~diff
- 009dea44 ["INT_ADD", "register:40f0:8", ["const:9dea44:8", "const:4:8"]]
- 009dea44 ["CALL", null, ["callee:0043bb58:8"]]
+ 009df9f0 ["INT_ADD", "register:40f0:8", ["const:9df9f0:8", "const:4:8"]]
+ 009df9f0 ["CALL", null, ["callee:0043bb58:8"]]
- 009dea44 bytes 7d73e997
+ 009df9f0 bytes 5a70e997
- 009deb18 ["INT_ADD", "register:40f0:8", ["const:9deb18:8", "const:4:8"]]
- 009deb18 ["CALL", null, ["callee:00c58ed0:8"]]
+ 009dfac4 ["INT_ADD", "register:40f0:8", ["const:9dfac4:8", "const:4:8"]]
+ 009dfac4 ["CALL", null, ["callee:00c58ed0:8"]]
- 009deb18 bytes fae40994
+ 009dfac4 bytes 03e50994
- 009de90c ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 009df8b8 ["COPY", "register:4098:8", ["const:1124000:8"]]
- 009de90c bytes 333a00b0
+ 009df8b8 bytes 333a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f2b946c0f273511808371fa0b6b3dfe"></a>

### [`009df940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df940.md) → [`009e08ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e08ec.md) FUN_009e08ec

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 11件 [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) [`009dfaf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfaf0.md) [`009e12cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e12cc.md) [`009e340c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e340c.md) · 呼出先 8件 [`0046db14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db14.md) [`006650ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00665/006650ac.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00936618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00936/00936618.md) [`009df6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df6bc.md)
- 新版 呼出元 11件 [`00606ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/00606ed4.md) [`0093c770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0093c/0093c770.md) [`009e0a9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e0a9c.md) [`009e2278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e2/009e2278.md) [`009e43b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e4/009e43b8.md) · 呼出先 8件 [`0046de34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de34.md) [`0066545c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/0066545c.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`009375c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00937/009375c4.md) [`009e0668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e0668.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.72% / 新版 90.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e09ac",
      "incomplete_value": true,
      "site": "009e09bc",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:a52:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dfa00",
      "incomplete_value": true,
      "site": "009dfa10",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:983:8"
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
      "definition_site": "009e09b0",
      "incomplete_value": true,
      "site": "009e09c0",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dfa04",
      "incomplete_value": true,
      "site": "009dfa14",
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
                "const:e:8"
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
      "definition_site": "009e09b4",
      "incomplete_value": true,
      "site": "009e09c4",
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
                "const:4c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dfa08",
      "incomplete_value": true,
      "site": "009dfa18",
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
                "const:470:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009e09ac",
      "READ",
      [
        "storage",
        "002b6983",
        null,
        "string"
      ]
    ],
    [
      "009e09b0",
      "READ",
      [
        "storage",
        "002b6991",
        null,
        "string"
      ]
    ],
    [
      "009e09b4",
      "READ",
      [
        "storage",
        "002c2470",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e09ac",
      "READ",
      [
        "storage",
        "002b6a52",
        null,
        "string"
      ]
    ],
    [
      "009e09b0",
      "READ",
      [
        "storage",
        "002b6a60",
        null,
        "string"
      ]
    ],
    [
      "009e09b4",
      "READ",
      [
        "storage",
        "002c24c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dfa78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df940.md#insn-009dfa78) · [`009df974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df940.md#insn-009df974) · [`009df984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df940.md#insn-009df984)
- 新版 [`009e0a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e08ec.md#insn-009e0a24) · [`009e0920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e08ec.md#insn-009e0920) · [`009e0930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e08ec.md#insn-009e0930)

~~~diff
- 009dfa78 ["INT_ADD", "register:40f0:8", ["const:9dfa78:8", "const:4:8"]]
- 009dfa78 ["CALL", null, ["ram:6650ac:8"]]
+ 009e0a24 ["INT_ADD", "register:40f0:8", ["const:9e0a24:8", "const:4:8"]]
+ 009e0a24 ["CALL", null, ["ram:66545c:8"]]
- 009dfa78 bytes 8d15f297
+ 009e0a24 bytes 8e12f297
- 009df974 ["INT_ADD", "register:40f0:8", ["const:9df974:8", "const:4:8"]]
- 009df974 ["CALL", null, ["callee:009e0668:8"]]
+ 009e0920 ["INT_ADD", "register:40f0:8", ["const:9e0920:8", "const:4:8"]]
+ 009e0920 ["CALL", null, ["callee:009e0668:8"]]
- 009df974 bytes 52ffff97
+ 009e0920 bytes 52ffff97
- 009df984 ["INT_ADD", "register:40f0:8", ["const:9df984:8", "const:4:8"]]
- 009df984 ["CALL", null, ["callee:008524fc:8"]]
+ 009e0930 ["INT_ADD", "register:40f0:8", ["const:9e0930:8", "const:4:8"]]
+ 009e0930 ["CALL", null, ["callee:008524fc:8"]]
- 009df984 bytes f3c6f997
+ 009e0930 bytes f3c6f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a50f6b3e400da7340262d79d833be27"></a>

### [`009dfb6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfb6c.md) → [`009e0b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e0b18.md) FUN_009e0b18

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00658c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658c2c.md) [`00658dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658dec.md) [`0065ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065a/0065ad80.md) [`009dfe00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfe00.md) [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 7件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006881b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00688/006881b8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 5件 [`00658fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/00658fdc.md) [`0065919c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00659/0065919c.md) [`0065b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065b/0065b130.md) [`009e0dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e0dac.md) [`00a48f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a48/00a48f48.md) · 呼出先 7件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00688568`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00688/00688568.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.65% / 新版 98.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e0b48",
      "incomplete_value": true,
      "site": "009e0b6c",
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
      "definition_site": "009dfb9c",
      "incomplete_value": true,
      "site": "009dfbc0",
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
      "009e0b48",
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
      "009e0b48",
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

- 旧版 [`009dfb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfb6c.md#insn-009dfb9c) · [`009dfbc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfb6c.md#insn-009dfbc4) · [`009dfbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfb6c.md#insn-009dfbdc)
- 新版 [`009e0b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e0b18.md#insn-009e0b48) · [`009e0b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e0b18.md#insn-009e0b70) · [`009e0b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e0b18.md#insn-009e0b88)

~~~diff
- 009dfb9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:120:8"]]
- 009dfb9c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 009dfb9c ["COPY", "register:5008:8", ["const:0:8"]]
- 009dfb9c ["COPY", "register:5010:8", ["const:0:8"]]
+ 009e0b48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
+ 009e0b48 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 009e0b48 ["COPY", "register:5008:8", ["const:0:8"]]
+ 009e0b48 ["COPY", "register:5010:8", ["const:0:8"]]
- 009dfb9c bytes 009140fd
+ 009e0b48 bytes 00b940fd
- 009dfbc4 ["INT_ADD", "register:40f0:8", ["const:9dfbc4:8", "const:4:8"]]
- 009dfbc4 ["CALL", null, ["callee:00688568:8"]]
+ 009e0b70 ["INT_ADD", "register:40f0:8", ["const:9e0b70:8", "const:4:8"]]
+ 009e0b70 ["CALL", null, ["callee:00688568:8"]]
- 009dfbc4 bytes 7da1f297
+ 009e0b70 bytes 7e9ef297
- 009dfbdc ["INT_ADD", "register:40f0:8", ["const:9dfbdc:8", "const:4:8"]]
- 009dfbdc ["CALL", null, ["callee:00c54d60:8"]]
+ 009e0b88 ["INT_ADD", "register:40f0:8", ["const:9e0b88:8", "const:4:8"]]
+ 009e0b88 ["CALL", null, ["callee:00c54d60:8"]]
- 009dfbdc bytes 65d00994
+ 009e0b88 bytes 76d00994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-007e30b7b930dc3b8af263b2a8e948f9"></a>

### [`009e0228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e0228.md) → [`009e11d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e11d4.md) FUN_009e11d4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 7件 [`0086ab34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab34.md) [`009e6560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6560.md) [`009e6564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6564.md) [`009f2658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2658.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`0084f5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084f/0084f5a0.md) · 呼出先 7件 [`0086bae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086bae0.md) [`009e750c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e750c.md) [`009e7510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7510.md) [`009f3604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3604.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009e121c",
      "incomplete_value": false,
      "site": "009e1224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e0270",
      "incomplete_value": false,
      "site": "009e0278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "009e1224",
      "DATA",
      [
        "storage",
        "00c89d28",
        null,
        "undefined *"
      ]
    ],
    [
      "009e12cc",
      "READ",
      [
        "storage",
        "00c89d48",
        null,
        "pointer"
      ]
    ],
    [
      "009e12cc",
      "READ",
      [
        "storage",
        "00c89d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e1224",
      "DATA",
      [
        "storage",
        "00c8acf8",
        null,
        "undefined *"
      ]
    ],
    [
      "009e12cc",
      "READ",
      [
        "storage",
        "00c8ad18",
        null,
        "pointer"
      ]
    ],
    [
      "009e12cc",
      "READ",
      [
        "storage",
        "00c8ad20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e0258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e0228.md#insn-009e0258) · [`009e026c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e0228.md#insn-009e026c) · [`009e0270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e0228.md#insn-009e0270)
- 新版 [`009e1204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e11d4.md#insn-009e1204) · [`009e1218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e11d4.md#insn-009e1218) · [`009e121c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e11d4.md#insn-009e121c)

~~~diff
- 009e0258 ["INT_ADD", "register:40f0:8", ["const:9e0258:8", "const:4:8"]]
- 009e0258 ["CALL", null, ["callee:0086bae0:8"]]
+ 009e1204 ["INT_ADD", "register:40f0:8", ["const:9e1204:8", "const:4:8"]]
+ 009e1204 ["CALL", null, ["callee:0086bae0:8"]]
- 009e0258 bytes 372afa97
+ 009e1204 bytes 372afa97
- 009e026c ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009e1218 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009e026c bytes 481500b0
+ 009e1218 bytes 481500b0
- 009e0270 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 009e0270 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e0270 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e0270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e121c ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 009e121c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e121c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e121c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e0270 bytes 08a13491
+ 009e121c bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b996de9dae75a5b0c501194ac1357f0e"></a>

### [`009e03d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e03d0.md) → [`009e137c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e137c.md) FUN_009e137c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009e03a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e03a4.md) · 呼出先 22件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)
- 新版 呼出元 1件 [`009e1350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e1350.md) · 呼出先 22件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009e13c0",
      "incomplete_value": false,
      "site": "009e13cc",
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
      "definition_site": "009e0414",
      "incomplete_value": false,
      "site": "009e0420",
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
      "definition_site": "009e13f8",
      "incomplete_value": true,
      "site": "009e1408",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:6ee:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e044c",
      "incomplete_value": true,
      "site": "009e045c",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:6a4:8"
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
      "definition_site": "009e13fc",
      "incomplete_value": true,
      "site": "009e140c",
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
      "definition_site": "009e0450",
      "incomplete_value": true,
      "site": "009e0460",
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
      "009e13cc",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009e13f8",
      "READ",
      [
        "storage",
        "002c06a4",
        null,
        "string"
      ]
    ],
    [
      "009e13fc",
      "READ",
      [
        "storage",
        "002c06ad",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009e13cc",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "009e13f8",
      "READ",
      [
        "storage",
        "002c06ee",
        null,
        "string"
      ]
    ],
    [
      "009e13fc",
      "READ",
      [
        "storage",
        "002c06f7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e0408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e03d0.md#insn-009e0408) · [`009e0410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e03d0.md#insn-009e0410) · [`009e0414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e03d0.md#insn-009e0414)
- 新版 [`009e13b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e137c.md#insn-009e13b4) · [`009e13bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e137c.md#insn-009e13bc) · [`009e13c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e137c.md#insn-009e13c0)

~~~diff
- 009e0408 ["INT_ADD", "register:40f0:8", ["const:9e0408:8", "const:4:8"]]
- 009e0408 ["CALL", null, ["callee:00488180:8"]]
+ 009e13b4 ["INT_ADD", "register:40f0:8", ["const:9e13b4:8", "const:4:8"]]
+ 009e13b4 ["CALL", null, ["callee:00488180:8"]]
- 009e0408 bytes 969eea97
+ 009e13b4 bytes 739bea97
- 009e0410 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 009e13bc ["COPY", "register:4040:8", ["const:c65000:8"]]
- 009e0410 bytes 28140090
+ 009e13bc bytes 28140090
- 009e0414 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 009e0414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e0414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e0414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e13c0 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 009e13c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e13c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e13c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e0414 bytes 08213891
+ 009e13c0 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47c7dc86a3174aafe3e9c517280075dd"></a>

### [`009e4760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4760.md) → [`009e570c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e5/009e570c.md) FUN_009e570c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`009f5b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f5b08.md) [`00a02c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02c3c.md) · 呼出先 9件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md) [`005cd130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md)
- 新版 呼出元 2件 [`009f6ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f6/009f6ab4.md) [`00a03be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a03be8.md) · 呼出先 9件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0052e060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md) [`005cd4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cd4e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.62% / 新版 95.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e57a8",
      "incomplete_value": true,
      "site": "009e57b8",
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
                "register:4050:8"
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
      "definition_site": "009e47fc",
      "incomplete_value": true,
      "site": "009e480c",
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
                "register:4050:8"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e5848",
      "incomplete_value": false,
      "site": "009e5854",
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
            "const:aff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e489c",
      "incomplete_value": false,
      "site": "009e48a8",
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
            "const:a21:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009e57a0",
      "READ",
      [
        "storage",
        "002bee90",
        null,
        "string"
      ]
    ],
    [
      "009e57a4",
      "READ",
      [
        "storage",
        "002bee80",
        null,
        "string"
      ]
    ],
    [
      "009e57a8",
      "READ",
      [
        "storage",
        "002c22e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e57a0",
      "READ",
      [
        "storage",
        "002bef6e",
        null,
        "string"
      ]
    ],
    [
      "009e57a4",
      "READ",
      [
        "storage",
        "002bef5e",
        null,
        "string"
      ]
    ],
    [
      "009e57a8",
      "READ",
      [
        "storage",
        "002c2330",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e48a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4760.md#insn-009e48a8) · [`009e4794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4760.md#insn-009e4794) · [`009e47a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4760.md#insn-009e47a8)
- 新版 [`009e5854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e5/009e570c.md#insn-009e5854) · [`009e5740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e5/009e570c.md#insn-009e5740) · [`009e5754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e5/009e570c.md#insn-009e5754)

~~~diff
- 009e48a8 ["INT_ADD", "register:40f0:8", ["const:9e48a8:8", "const:4:8"]]
- 009e48a8 ["CALL", null, ["callee:0060d858:8"]]
+ 009e5854 ["INT_ADD", "register:40f0:8", ["const:9e5854:8", "const:4:8"]]
+ 009e5854 ["CALL", null, ["callee:0060d858:8"]]
- 009e48a8 bytes 00a3f097
+ 009e5854 bytes 01a0f097
- 009e4794 ["COPY", "register:0:8", ["register:4040:8"]]
- 009e4794 ["INT_ADD", "register:40f0:8", ["const:9e4794:8", "const:4:8"]]
- 009e4794 ["CALLIND", null, ["register:0:8"]]
+ 009e5740 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009e5740 ["INT_ADD", "register:40f0:8", ["const:9e5740:8", "const:4:8"]]
+ 009e5740 ["CALLIND", null, ["register:0:8"]]
- 009e4794 bytes 00013fd6
+ 009e5740 bytes 00013fd6
- 009e47a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 009e47a8 ["INT_ADD", "register:40f0:8", ["const:9e47a8:8", "const:4:8"]]
- 009e47a8 ["CALLIND", null, ["register:0:8"]]
+ 009e5754 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009e5754 ["INT_ADD", "register:40f0:8", ["const:9e5754:8", "const:4:8"]]
+ 009e5754 ["CALLIND", null, ["register:0:8"]]
- 009e47a8 bytes 00013fd6
+ 009e5754 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07a79e053e0e3b79269de23787fb11bc"></a>

### [`009e4a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4a5c.md) → [`009e5a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e5/009e5a08.md) FUN_009e5a08

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0061456c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md) [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) [`009f931c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f931c.md) [`009f9870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f9870.md) · 呼出先 14件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md) [`005cd130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md)
- 新版 呼出元 6件 [`00606ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/00606ed4.md) [`0061491c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00614/0061491c.md) [`0093c770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0093c/0093c770.md) [`009fa2c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fa/009fa2c8.md) [`009fa81c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fa/009fa81c.md) · 呼出先 14件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0052e060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md) [`005cd4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cd4e0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.71% / 新版 92.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e5b28",
      "incomplete_value": true,
      "site": "009e5b28",
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
                "const:466:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e4b7c",
      "incomplete_value": true,
      "site": "009e4b7c",
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
                "const:426:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e5b2c",
      "incomplete_value": true,
      "site": "009e5b2c",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e4b80",
      "incomplete_value": true,
      "site": "009e4b80",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e5c64",
      "incomplete_value": true,
      "site": "009e5c74",
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
      "definition_site": "009e4cb8",
      "incomplete_value": true,
      "site": "009e4cc8",
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
    "ordinal": 38,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009e5ad0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648e0"
      ]
    ],
    [
      "009e5b18",
      "READ",
      [
        "storage",
        "002a1426",
        null,
        "string"
      ]
    ],
    [
      "009e5b1c",
      "READ",
      [
        "storage",
        "002a142c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009e5ad0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664c90"
      ]
    ],
    [
      "009e5b18",
      "READ",
      [
        "storage",
        "002a1466",
        null,
        "string"
      ]
    ],
    [
      "009e5b1c",
      "READ",
      [
        "storage",
        "002a146c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e4b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4a5c.md#insn-009e4b24) · [`009e4ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4a5c.md#insn-009e4ed0) · [`009e4eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4a5c.md#insn-009e4eec)
- 新版 [`009e5ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e5/009e5a08.md#insn-009e5ad0) · [`009e5e7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e5/009e5a08.md#insn-009e5e7c) · [`009e5e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e5/009e5a08.md#insn-009e5e98)

~~~diff
- 009e4b24 ["INT_ADD", "register:40f0:8", ["const:9e4b24:8", "const:4:8"]]
- 009e4b24 ["CALL", null, ["ram:6648e0:8"]]
+ 009e5ad0 ["INT_ADD", "register:40f0:8", ["const:9e5ad0:8", "const:4:8"]]
+ 009e5ad0 ["CALL", null, ["ram:664c90:8"]]
- 009e4b24 bytes 6ffff197
+ 009e5ad0 bytes 70fcf197
- 009e4ed0 ["INT_ADD", "register:40f0:8", ["const:9e4ed0:8", "const:4:8"]]
- 009e4ed0 ["CALL", null, ["callee:0060df00:8"]]
+ 009e5e7c ["INT_ADD", "register:40f0:8", ["const:9e5e7c:8", "const:4:8"]]
+ 009e5e7c ["CALL", null, ["callee:0060df00:8"]]
- 009e4ed0 bytes 20a3f097
+ 009e5e7c bytes 21a0f097
- 009e4eec ["INT_ADD", "register:40f0:8", ["const:9e4eec:8", "const:4:8"]]
- 009e4eec ["CALL", null, ["callee:007f0a44:8"]]
+ 009e5e98 ["INT_ADD", "register:40f0:8", ["const:9e5e98:8", "const:4:8"]]
+ 009e5e98 ["CALL", null, ["callee:007f0a44:8"]]
- 009e4eec bytes fd2af897
+ 009e5e98 bytes eb2af897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b7f1a38fa8ea85f7e88cc88584a8ef2"></a>

### [`009e52b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e52b4.md) → [`009e6260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e6/009e6260.md) FUN_009e6260

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a02c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02c3c.md) · 呼出先 11件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b98b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b98b0.md) [`008bad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bad20.md) [`009e2fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e2fe8.md)
- 新版 呼出元 1件 [`00a03be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a03be8.md) · 呼出先 11件 [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba85c.md) [`008bbccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bbccc.md) [`009e3f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e3/009e3f94.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.42% / 新版 85.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e630c",
      "incomplete_value": true,
      "site": "009e631c",
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
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:69c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e5360",
      "incomplete_value": true,
      "site": "009e5370",
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
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:5be:8"
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
      "definition_site": "009e6310",
      "incomplete_value": true,
      "site": "009e6320",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e5364",
      "incomplete_value": true,
      "site": "009e5374",
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
                "const:a:8"
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
      "definition_site": "009e6314",
      "incomplete_value": true,
      "site": "009e6324",
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
                "const:b20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e5368",
      "incomplete_value": true,
      "site": "009e5378",
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
                "const:ad0:8"
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
      "009e630c",
      "READ",
      [
        "storage",
        "002b55be",
        null,
        "string"
      ]
    ],
    [
      "009e6310",
      "READ",
      [
        "storage",
        "002b55c8",
        null,
        "string"
      ]
    ],
    [
      "009e6314",
      "READ",
      [
        "storage",
        "002c2ad0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e630c",
      "READ",
      [
        "storage",
        "002b569c",
        null,
        "string"
      ]
    ],
    [
      "009e6310",
      "READ",
      [
        "storage",
        "002b56a6",
        null,
        "string"
      ]
    ],
    [
      "009e6314",
      "READ",
      [
        "storage",
        "002c2b20",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e52e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e52b4.md#insn-009e52e0) · [`009e5344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e52b4.md#insn-009e5344) · [`009e5350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e52b4.md#insn-009e5350)
- 新版 [`009e628c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e6/009e6260.md#insn-009e628c) · [`009e62f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e6/009e6260.md#insn-009e62f0) · [`009e62fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e6/009e6260.md#insn-009e62fc)

~~~diff
- 009e52e0 ["INT_ADD", "register:40f0:8", ["const:9e52e0:8", "const:4:8"]]
- 009e52e0 ["CALL", null, ["callee:009e3f94:8"]]
+ 009e628c ["INT_ADD", "register:40f0:8", ["const:9e628c:8", "const:4:8"]]
+ 009e628c ["CALL", null, ["callee:009e3f94:8"]]
- 009e52e0 bytes 42f7ff97
+ 009e628c bytes 42f7ff97
- 009e5344 ["INT_ADD", "register:40f0:8", ["const:9e5344:8", "const:4:8"]]
- 009e5344 ["CALL", null, ["callee:008524fc:8"]]
+ 009e62f0 ["INT_ADD", "register:40f0:8", ["const:9e62f0:8", "const:4:8"]]
+ 009e62f0 ["CALL", null, ["callee:008524fc:8"]]
- 009e5344 bytes 83b0f997
+ 009e62f0 bytes 83b0f997
- 009e5350 ["INT_ADD", "register:40f0:8", ["const:9e5350:8", "const:4:8"]]
- 009e5350 ["CALL", null, ["callee:00c58f30:8"]]
+ 009e62fc ["INT_ADD", "register:40f0:8", ["const:9e62fc:8", "const:4:8"]]
+ 009e62fc ["CALL", null, ["callee:00c58f30:8"]]
- 009e5350 bytes 04cb0994
+ 009e62fc bytes 0dcb0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2cca1da9e3ca0484e49b5975cc0fa29"></a>

### [`009e5670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e5670.md) → [`009e661c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e6/009e661c.md) FUN_009e661c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0061456c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md) · 呼出先 9件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b98b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b98b0.md) [`008bad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bad20.md) [`009e8cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cc0.md)
- 新版 呼出元 2件 [`00606ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/00606ed4.md) [`0061491c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00614/0061491c.md) · 呼出先 9件 [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba85c.md) [`008bbccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bbccc.md) [`009e9c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9c6c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e6664",
      "incomplete_value": true,
      "site": "009e6674",
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
                "const:e63:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e56b8",
      "incomplete_value": true,
      "site": "009e56c8",
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
                "const:d0b:8"
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
      "definition_site": "009e6668",
      "incomplete_value": true,
      "site": "009e6678",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e56bc",
      "incomplete_value": true,
      "site": "009e56cc",
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
                "const:a:8"
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
      "definition_site": "009e666c",
      "incomplete_value": true,
      "site": "009e667c",
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
                "const:b20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e56c0",
      "incomplete_value": true,
      "site": "009e56d0",
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
                "const:ad0:8"
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
      "009e6664",
      "READ",
      [
        "storage",
        "002a5d0b",
        null,
        "string"
      ]
    ],
    [
      "009e6668",
      "READ",
      [
        "storage",
        "002a5d15",
        null,
        "string"
      ]
    ],
    [
      "009e666c",
      "READ",
      [
        "storage",
        "002c2ad0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e6664",
      "READ",
      [
        "storage",
        "002a5e63",
        null,
        "string"
      ]
    ],
    [
      "009e6668",
      "READ",
      [
        "storage",
        "002a5e6d",
        null,
        "string"
      ]
    ],
    [
      "009e666c",
      "READ",
      [
        "storage",
        "002c2b20",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e569c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e5670.md#insn-009e569c) · [`009e56a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e5670.md#insn-009e56a8) · [`009e56b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e5670.md#insn-009e56b0)
- 新版 [`009e6648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e6/009e661c.md#insn-009e6648) · [`009e6654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e6/009e661c.md#insn-009e6654) · [`009e665c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e6/009e661c.md#insn-009e665c)

~~~diff
- 009e569c ["INT_ADD", "register:40f0:8", ["const:9e569c:8", "const:4:8"]]
- 009e569c ["CALL", null, ["callee:008524fc:8"]]
+ 009e6648 ["INT_ADD", "register:40f0:8", ["const:9e6648:8", "const:4:8"]]
+ 009e6648 ["CALL", null, ["callee:008524fc:8"]]
- 009e569c bytes adaff997
+ 009e6648 bytes adaff997
- 009e56a8 ["INT_ADD", "register:40f0:8", ["const:9e56a8:8", "const:4:8"]]
- 009e56a8 ["CALL", null, ["callee:00c58f30:8"]]
+ 009e6654 ["INT_ADD", "register:40f0:8", ["const:9e6654:8", "const:4:8"]]
+ 009e6654 ["CALL", null, ["callee:00c58f30:8"]]
- 009e56a8 bytes 2eca0994
+ 009e6654 bytes 37ca0994
- 009e56b0 ["COPY", "tmp:0:8", ["const:d0b:8"]]
- 009e56b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e56b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e56b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e665c ["COPY", "tmp:0:8", ["const:e63:8"]]
+ 009e665c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e665c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e665c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e56b0 bytes 082d3491
+ 009e665c bytes 088d3991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e4a5cc14d3c81b9cc76e27bc4a8bd3b"></a>

### [`009e6514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6514.md) → [`009e74c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e74c0.md) FUN_009e74c0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`009dec74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009dec74.md) [`009dfe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfe60.md) [`009e12cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e12cc.md) [`009e340c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e340c.md) [`009f931c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f931c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 6件 [`009dfc20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009df/009dfc20.md) [`009e0e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e0e0c.md) [`009e2278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e2/009e2278.md) [`009e43b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e4/009e43b8.md) [`009fa2c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fa/009fa2c8.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009e74cc",
      "incomplete_value": false,
      "site": "009e74d0",
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
      "definition_site": "009e6520",
      "incomplete_value": false,
      "site": "009e6524",
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
      "009e74cc",
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
      "009e74cc",
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

- 旧版 [`009e6524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6514.md#insn-009e6524) · [`009e651c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6514.md#insn-009e651c) · [`009e6520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6514.md#insn-009e6520)
- 新版 [`009e74d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e74c0.md#insn-009e74d0) · [`009e74c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e74c0.md#insn-009e74c8) · [`009e74cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e74c0.md#insn-009e74cc)

~~~diff
- 009e6524 ["INT_ADD", "register:40f0:8", ["const:9e6524:8", "const:4:8"]]
- 009e6524 ["CALL", null, ["callee:0043bad8:8"]]
+ 009e74d0 ["INT_ADD", "register:40f0:8", ["const:9e74d0:8", "const:4:8"]]
+ 009e74d0 ["CALL", null, ["callee:0043bad8:8"]]
- 009e6524 bytes a554e997
+ 009e74d0 bytes 8251e997
- 009e651c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009e74c8 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009e651c bytes 80c6ffb0
+ 009e74c8 bytes 80c6ffb0
- 009e6520 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009e6520 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009e6520 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009e6520 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009e74cc ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009e74cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009e74cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009e74cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009e6520 bytes 00303e91
+ 009e74cc bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9c9ac6f37b138f8810d72f7afe2ee60"></a>

### [`009e652c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e652c.md) → [`009e74d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e74d8.md) FUN_009e74d8

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
      "definition_site": "009e74ec",
      "incomplete_value": false,
      "site": "009e74f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e6540",
      "incomplete_value": false,
      "site": "009e6544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "009e74f0",
      "DATA",
      [
        "storage",
        "00c89d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e74f0",
      "DATA",
      [
        "storage",
        "00c8acf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e6538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e652c.md#insn-009e6538) · [`009e653c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e652c.md#insn-009e653c) · [`009e6540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e652c.md#insn-009e6540)
- 新版 [`009e74e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e74d8.md#insn-009e74e4) · [`009e74e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e74d8.md#insn-009e74e8) · [`009e74ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e74d8.md#insn-009e74ec)

~~~diff
- 009e6538 ["INT_ADD", "register:40f0:8", ["const:9e6538:8", "const:4:8"]]
- 009e6538 ["CALL", null, ["callee:00c58f30:8"]]
+ 009e74e4 ["INT_ADD", "register:40f0:8", ["const:9e74e4:8", "const:4:8"]]
+ 009e74e4 ["CALL", null, ["callee:00c58f30:8"]]
- 009e6538 bytes 8ac60994
+ 009e74e4 bytes 93c60994
- 009e653c ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009e74e8 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009e653c bytes 081500f0
+ 009e74e8 bytes 081500f0
- 009e6540 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 009e6540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e6540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e6540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e74ec ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 009e74ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e74ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e74ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e6540 bytes 08a13491
+ 009e74ec bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fafe4365bb4f272eb4e5064544583f32"></a>

### [`009e6550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6550.md) → [`009e74fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e74fc.md) FUN_009e74fc

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
      "definition_site": "009e7500",
      "incomplete_value": false,
      "site": "009e7504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e6554",
      "incomplete_value": false,
      "site": "009e6558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "009e7504",
      "DATA",
      [
        "storage",
        "00c89d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e7504",
      "DATA",
      [
        "storage",
        "00c8acf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e6550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6550.md#insn-009e6550) · [`009e6554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6550.md#insn-009e6554)
- 新版 [`009e74fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e74fc.md#insn-009e74fc) · [`009e7500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e74fc.md#insn-009e7500)

~~~diff
- 009e6550 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009e74fc ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009e6550 bytes 081500f0
+ 009e74fc bytes 081500f0
- 009e6554 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 009e6554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e6554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e6554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e7500 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 009e7500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e7500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e7500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e6554 bytes 08a13491
+ 009e7500 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-297e572af1986b3ff7d4ac78e4070a1c"></a>

### [`009e67c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e67c8.md) → [`009e7774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7774.md) FUN_009e7774

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009e6594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6594.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`009e7540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7540.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009e7780",
      "incomplete_value": false,
      "site": "009e7784",
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
      "definition_site": "009e67d4",
      "incomplete_value": false,
      "site": "009e67d8",
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
      "009e7780",
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
      "009e7780",
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

- 旧版 [`009e67d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e67c8.md#insn-009e67d8) · [`009e67d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e67c8.md#insn-009e67d0) · [`009e67d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e67c8.md#insn-009e67d4)
- 新版 [`009e7784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7774.md#insn-009e7784) · [`009e777c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7774.md#insn-009e777c) · [`009e7780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7774.md#insn-009e7780)

~~~diff
- 009e67d8 ["INT_ADD", "register:40f0:8", ["const:9e67d8:8", "const:4:8"]]
- 009e67d8 ["CALL", null, ["callee:0043bad8:8"]]
+ 009e7784 ["INT_ADD", "register:40f0:8", ["const:9e7784:8", "const:4:8"]]
+ 009e7784 ["CALL", null, ["callee:0043bad8:8"]]
- 009e67d8 bytes f853e997
+ 009e7784 bytes d550e997
- 009e67d0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009e777c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009e67d0 bytes 80c6ffb0
+ 009e777c bytes 80c6ffb0
- 009e67d4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009e67d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009e67d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009e67d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009e7780 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009e7780 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009e7780 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009e7780 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009e67d4 bytes 00303e91
+ 009e7780 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca8bab25159a5479a33a25553354f8a9"></a>

### [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) → [`009e7c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7c80.md) FUN_009e7c80

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009e3140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e3140.md) [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) · 呼出先 7件 [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) [`009e7c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md) [`009e7e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md) [`009e8178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md) [`009e84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md)
- 新版 呼出元 2件 [`009e40ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e4/009e40ec.md) [`009e7c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7c80.md) · 呼出先 7件 [`009e7c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7c80.md) [`009e8bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8bb0.md) [`009e8e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8e40.md) [`009e9124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9124.md) [`009e9458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9458.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e83e4",
      "incomplete_value": false,
      "site": "009e83ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:785:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e7438",
      "incomplete_value": false,
      "site": "009e7440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009e7e34",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e7e54",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e7e98",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e7e34",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ],
    [
      "009e7e54",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ],
    [
      "009e7e98",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e7440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md#insn-009e7440) · [`009e6d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md#insn-009e6d18) · [`009e6dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md#insn-009e6dc4)
- 新版 [`009e83ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7c80.md#insn-009e83ec) · [`009e7cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7c80.md#insn-009e7cc4) · [`009e7d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7c80.md#insn-009e7d70)

~~~diff
- 009e7440 ["INT_ADD", "register:40f0:8", ["const:9e7440:8", "const:4:8"]]
- 009e7440 ["CALL", null, ["callee:009e9458:8"]]
+ 009e83ec ["INT_ADD", "register:40f0:8", ["const:9e83ec:8", "const:4:8"]]
+ 009e83ec ["CALL", null, ["callee:009e9458:8"]]
- 009e7440 bytes 1b040094
+ 009e83ec bytes 1b040094
- 009e6d18 ["COPY", "tmp:0:8", ["const:735:8"]]
- 009e6d18 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 009e6d18 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 009e6d18 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 009e7cc4 ["COPY", "tmp:0:8", ["const:785:8"]]
+ 009e7cc4 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 009e7cc4 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 009e7cc4 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 009e6d18 bytes 18d71c91
+ 009e7cc4 bytes 18171e91
- 009e6dc4 ["INT_ADD", "register:40f0:8", ["const:9e6dc4:8", "const:4:8"]]
- 009e6dc4 ["CALL", null, ["callee:009e8e40:8"]]
+ 009e7d70 ["INT_ADD", "register:40f0:8", ["const:9e7d70:8", "const:4:8"]]
+ 009e7d70 ["CALL", null, ["callee:009e8e40:8"]]
- 009e6dc4 bytes 34040094
+ 009e7d70 bytes 34040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f869877ba7d03f0fefd2708dae6dfa74"></a>

### [`009e7c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md) → [`009e8bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8bb0.md) FUN_009e8bb0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) [`009e8178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md) · 呼出先 3件 [`009e84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md) [`009e8770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`009e7c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7c80.md) [`009e9124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9124.md) · 呼出先 3件 [`009e9458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9458.md) [`009e971c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e971c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e8c14",
      "incomplete_value": false,
      "site": "009e8c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:785:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e7c68",
      "incomplete_value": false,
      "site": "009e7c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e8c98",
      "incomplete_value": false,
      "site": "009e8ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:785:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e7cec",
      "incomplete_value": false,
      "site": "009e7cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e8d1c",
      "incomplete_value": false,
      "site": "009e8d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:785:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e7d70",
      "incomplete_value": false,
      "site": "009e7d78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
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
      "009e8c14",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e8c34",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e8c98",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e8c14",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ],
    [
      "009e8c34",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ],
    [
      "009e8c98",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e7c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md#insn-009e7c70) · [`009e7cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md#insn-009e7cf4) · [`009e7d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md#insn-009e7d78)
- 新版 [`009e8c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8bb0.md#insn-009e8c1c) · [`009e8ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8bb0.md#insn-009e8ca0) · [`009e8d24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8bb0.md#insn-009e8d24)

~~~diff
- 009e7c70 ["INT_ADD", "register:40f0:8", ["const:9e7c70:8", "const:4:8"]]
- 009e7c70 ["CALL", null, ["callee:009e9458:8"]]
+ 009e8c1c ["INT_ADD", "register:40f0:8", ["const:9e8c1c:8", "const:4:8"]]
+ 009e8c1c ["CALL", null, ["callee:009e9458:8"]]
- 009e7c70 bytes 0f020094
+ 009e8c1c bytes 0f020094
- 009e7cf4 ["INT_ADD", "register:40f0:8", ["const:9e7cf4:8", "const:4:8"]]
- 009e7cf4 ["CALL", null, ["callee:009e9458:8"]]
+ 009e8ca0 ["INT_ADD", "register:40f0:8", ["const:9e8ca0:8", "const:4:8"]]
+ 009e8ca0 ["CALL", null, ["callee:009e9458:8"]]
- 009e7cf4 bytes ee010094
+ 009e8ca0 bytes ee010094
- 009e7d78 ["INT_ADD", "register:40f0:8", ["const:9e7d78:8", "const:4:8"]]
- 009e7d78 ["CALL", null, ["callee:009e9458:8"]]
+ 009e8d24 ["INT_ADD", "register:40f0:8", ["const:9e8d24:8", "const:4:8"]]
+ 009e8d24 ["CALL", null, ["callee:009e9458:8"]]
- 009e7d78 bytes cd010094
+ 009e8d24 bytes cd010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58d1274c9edb9ac8f7ed8212e020cead"></a>

### [`009e7e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md) → [`009e8e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8e40.md) FUN_009e8e40

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) [`009e8178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md) [`009e8770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md) · 呼出先 2件 [`009e84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 3件 [`009e7c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7c80.md) [`009e9124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9124.md) [`009e971c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e971c.md) · 呼出先 2件 [`009e9458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9458.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.76% / 新版 96.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e8e7c",
      "incomplete_value": false,
      "site": "009e8e94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:785:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e7ed0",
      "incomplete_value": false,
      "site": "009e7ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e8fd0",
      "incomplete_value": false,
      "site": "009e8fd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:785:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8024",
      "incomplete_value": false,
      "site": "009e802c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e9084",
      "incomplete_value": false,
      "site": "009e9090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:785:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e80d8",
      "incomplete_value": false,
      "site": "009e80e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009e8e7c",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e8eac",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e8edc",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e8e7c",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ],
    [
      "009e8eac",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ],
    [
      "009e8edc",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e7ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md#insn-009e7ee8) · [`009e802c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md#insn-009e802c) · [`009e80e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md#insn-009e80e4)
- 新版 [`009e8e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8e40.md#insn-009e8e94) · [`009e8fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8e40.md#insn-009e8fd8) · [`009e9090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8e40.md#insn-009e9090)

~~~diff
- 009e7ee8 ["INT_ADD", "register:40f0:8", ["const:9e7ee8:8", "const:4:8"]]
- 009e7ee8 ["CALL", null, ["callee:009e9458:8"]]
+ 009e8e94 ["INT_ADD", "register:40f0:8", ["const:9e8e94:8", "const:4:8"]]
+ 009e8e94 ["CALL", null, ["callee:009e9458:8"]]
- 009e7ee8 bytes 71010094
+ 009e8e94 bytes 71010094
- 009e802c ["INT_ADD", "register:40f0:8", ["const:9e802c:8", "const:4:8"]]
- 009e802c ["CALL", null, ["callee:009e9458:8"]]
+ 009e8fd8 ["INT_ADD", "register:40f0:8", ["const:9e8fd8:8", "const:4:8"]]
+ 009e8fd8 ["CALL", null, ["callee:009e9458:8"]]
- 009e802c bytes 20010094
+ 009e8fd8 bytes 20010094
- 009e80e4 ["INT_ADD", "register:40f0:8", ["const:9e80e4:8", "const:4:8"]]
- 009e80e4 ["CALL", null, ["callee:009e9458:8"]]
+ 009e9090 ["INT_ADD", "register:40f0:8", ["const:9e9090:8", "const:4:8"]]
+ 009e9090 ["CALL", null, ["callee:009e9458:8"]]
- 009e80e4 bytes f2000094
+ 009e9090 bytes f2000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8665b51a71e93a198b4ee5d94ce32462"></a>

### [`009e8178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md) → [`009e9124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9124.md) FUN_009e9124

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) · 呼出先 5件 [`009e7c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md) [`009e7e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md) [`009e84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md) [`009e8770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`009e7c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7c80.md) · 呼出先 5件 [`009e8bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8bb0.md) [`009e8e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8e40.md) [`009e9458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9458.md) [`009e971c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e971c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.54% / 新版 98.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e91f0",
      "incomplete_value": false,
      "site": "009e91fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:785:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8244",
      "incomplete_value": false,
      "site": "009e8250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
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
      "009e91f0",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e9214",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e9318",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e91f0",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ],
    [
      "009e9214",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ],
    [
      "009e9318",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md#insn-009e8250) · [`009e8214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md#insn-009e8214) · [`009e8234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md#insn-009e8234)
- 新版 [`009e91fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9124.md#insn-009e91fc) · [`009e91c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9124.md#insn-009e91c0) · [`009e91e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9124.md#insn-009e91e0)

~~~diff
- 009e8250 ["INT_ADD", "register:40f0:8", ["const:9e8250:8", "const:4:8"]]
- 009e8250 ["CALL", null, ["callee:009e9458:8"]]
+ 009e91fc ["INT_ADD", "register:40f0:8", ["const:9e91fc:8", "const:4:8"]]
+ 009e91fc ["CALL", null, ["callee:009e9458:8"]]
- 009e8250 bytes 97000094
+ 009e91fc bytes 97000094
- 009e8214 ["INT_ADD", "register:40f0:8", ["const:9e8214:8", "const:4:8"]]
- 009e8214 ["CALL", null, ["callee:009e8bb0:8"]]
+ 009e91c0 ["INT_ADD", "register:40f0:8", ["const:9e91c0:8", "const:4:8"]]
+ 009e91c0 ["CALL", null, ["callee:009e8bb0:8"]]
- 009e8214 bytes 7cfeff97
+ 009e91c0 bytes 7cfeff97
- 009e8234 ["COPY", "tmp:0:8", ["const:735:8"]]
- 009e8234 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 009e8234 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 009e8234 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 009e91e0 ["COPY", "tmp:0:8", ["const:785:8"]]
+ 009e91e0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 009e91e0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 009e91e0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 009e8234 bytes d6d61c91
+ 009e91e0 bytes d6161e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3159fb6d030ba6c95aebf3ce125db64"></a>

### [`009e8770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md) → [`009e971c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e971c.md) FUN_009e971c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) [`009e7c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md) [`009e8178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md) · 呼出先 3件 [`009e7e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md) [`009e84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 3件 [`009e7c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e7/009e7c80.md) [`009e8bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8bb0.md) [`009e9124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9124.md) · 呼出先 3件 [`009e8e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e8/009e8e40.md) [`009e9458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9458.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.09% / 新版 96.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e97fc",
      "incomplete_value": false,
      "site": "009e9804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:785:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8850",
      "incomplete_value": false,
      "site": "009e8858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e9880",
      "incomplete_value": false,
      "site": "009e9888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:785:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e88d4",
      "incomplete_value": false,
      "site": "009e88dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
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
      "009e9778",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e9798",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e97fc",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e9778",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ],
    [
      "009e9798",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ],
    [
      "009e97fc",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md#insn-009e8858) · [`009e88dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md#insn-009e88dc) · [`009e87b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md#insn-009e87b0)
- 新版 [`009e9804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e971c.md#insn-009e9804) · [`009e9888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e971c.md#insn-009e9888) · [`009e975c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e971c.md#insn-009e975c)

~~~diff
- 009e8858 ["INT_ADD", "register:40f0:8", ["const:9e8858:8", "const:4:8"]]
- 009e8858 ["CALL", null, ["callee:009e9458:8"]]
+ 009e9804 ["INT_ADD", "register:40f0:8", ["const:9e9804:8", "const:4:8"]]
+ 009e9804 ["CALL", null, ["callee:009e9458:8"]]
- 009e8858 bytes 15ffff97
+ 009e9804 bytes 15ffff97
- 009e88dc ["INT_ADD", "register:40f0:8", ["const:9e88dc:8", "const:4:8"]]
- 009e88dc ["CALL", null, ["callee:009e9458:8"]]
+ 009e9888 ["INT_ADD", "register:40f0:8", ["const:9e9888:8", "const:4:8"]]
+ 009e9888 ["CALL", null, ["callee:009e9458:8"]]
- 009e88dc bytes f4feff97
+ 009e9888 bytes f4feff97
- 009e87b0 ["INT_ADD", "register:40f0:8", ["const:9e87b0:8", "const:4:8"]]
- 009e87b0 ["CALL", null, ["callee:009e8e40:8"]]
+ 009e975c ["INT_ADD", "register:40f0:8", ["const:9e975c:8", "const:4:8"]]
+ 009e975c ["CALL", null, ["callee:009e8e40:8"]]
- 009e87b0 bytes b9fdff97
+ 009e975c bytes b9fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd624772d646dd4345d8a2ec79352673"></a>

### [`009e8a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a98.md) → [`009e9a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9a44.md) FUN_009e9a44

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
      "definition_site": "009e9a68",
      "incomplete_value": false,
      "site": "009e9a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8abc",
      "incomplete_value": false,
      "site": "009e8abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "009e9a68",
      "DATA",
      [
        "storage",
        "00c89da8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e9a68",
      "DATA",
      [
        "storage",
        "00c8ad78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a98.md#insn-009e8aac) · [`009e8ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a98.md#insn-009e8ab4) · [`009e8ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a98.md#insn-009e8ab8)
- 新版 [`009e9a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9a44.md#insn-009e9a58) · [`009e9a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9a44.md#insn-009e9a60) · [`009e9a64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9a44.md#insn-009e9a64)

~~~diff
- 009e8aac ["INT_ADD", "register:40f0:8", ["const:9e8aac:8", "const:4:8"]]
- 009e8aac ["CALL", null, ["callee:00c58f30:8"]]
+ 009e9a58 ["INT_ADD", "register:40f0:8", ["const:9e9a58:8", "const:4:8"]]
+ 009e9a58 ["CALL", null, ["callee:00c58f30:8"]]
- 009e8aac bytes 2dbd0994
+ 009e9a58 bytes 36bd0994
- 009e8ab4 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009e9a60 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009e8ab4 bytes 081500b0
+ 009e9a60 bytes 081500b0
- 009e8ab8 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 009e8ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e8ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e8ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e9a64 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 009e9a64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e9a64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e9a64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e8ab8 bytes 08a13691
+ 009e9a64 bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abd014b04e64fb3451b1642a21e9826a"></a>

### [`009e8acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8acc.md) → [`009e9a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9a78.md) FUN_009e9a78

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
      "definition_site": "009e9a84",
      "incomplete_value": false,
      "site": "009e9a84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8ad8",
      "incomplete_value": false,
      "site": "009e8ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "009e9a84",
      "DATA",
      [
        "storage",
        "00c89da8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e9a84",
      "DATA",
      [
        "storage",
        "00c8ad78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8acc.md#insn-009e8ad0) · [`009e8ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8acc.md#insn-009e8ad4)
- 新版 [`009e9a7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9a78.md#insn-009e9a7c) · [`009e9a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9a78.md#insn-009e9a80)

~~~diff
- 009e8ad0 ["COPY", "register:4048:8", ["const:c89000:8"]]
+ 009e9a7c ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 009e8ad0 bytes 091500b0
+ 009e9a7c bytes 091500b0
- 009e8ad4 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 009e8ad4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009e8ad4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009e8ad4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009e9a80 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 009e9a80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009e9a80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009e9a80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009e8ad4 bytes 29a13691
+ 009e9a80 bytes 29e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a21b4ca3bacb3f7ea74a1856be3917fa"></a>

### [`009e8ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8ae8.md) → [`009e9a94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9a94.md) FUN_009e9a94

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`00a1b6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b6a4.md)

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
      "site": "009e9abc",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009e8b10",
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
      "009e9abc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "009e9abc",
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

- 旧版 [`009e8b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8ae8.md#insn-009e8b10) · [`009e8b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8ae8.md#insn-009e8b1c) · [`009e8b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8ae8.md#insn-009e8b40)
- 新版 [`009e9abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9a94.md#insn-009e9abc) · [`009e9ac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9a94.md#insn-009e9ac8) · [`009e9aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9a94.md#insn-009e9aec)

~~~diff
- 009e8b10 ["INT_ADD", "register:40f0:8", ["const:9e8b10:8", "const:4:8"]]
- 009e8b10 ["CALL", null, ["ram:47ad34:8"]]
+ 009e9abc ["INT_ADD", "register:40f0:8", ["const:9e9abc:8", "const:4:8"]]
+ 009e9abc ["CALL", null, ["ram:47b054:8"]]
- 009e8b10 bytes 8948ea97
+ 009e9abc bytes 6645ea97
- 009e8b1c ["INT_ADD", "register:40f0:8", ["const:9e8b1c:8", "const:4:8"]]
- 009e8b1c ["CALL", null, ["callee:0047d134:8"]]
+ 009e9ac8 ["INT_ADD", "register:40f0:8", ["const:9e9ac8:8", "const:4:8"]]
+ 009e9ac8 ["CALL", null, ["callee:0047d134:8"]]
- 009e8b1c bytes be50ea97
+ 009e9ac8 bytes 9b4dea97
- 009e8b40 ["INT_ADD", "register:40f0:8", ["const:9e8b40:8", "const:4:8"]]
- 009e8b40 ["CALL", null, ["callee:008524fc:8"]]
+ 009e9aec ["INT_ADD", "register:40f0:8", ["const:9e9aec:8", "const:4:8"]]
+ 009e9aec ["CALL", null, ["callee:008524fc:8"]]
- 009e8b40 bytes 84a2f997
+ 009e9aec bytes 84a2f997
~~~


<a id="compare-5e35b5af08224a53144cea995c35482c"></a>

### [`009e8b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8b88.md) → [`009e9b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9b34.md) FUN_009e9b34

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
      "definition_site": "009e9b58",
      "incomplete_value": false,
      "site": "009e9b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8bac",
      "incomplete_value": false,
      "site": "009e8bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
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
      "009e9b58",
      "DATA",
      [
        "storage",
        "00c89e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e9b58",
      "DATA",
      [
        "storage",
        "00c8adf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8b88.md#insn-009e8b9c) · [`009e8ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8b88.md#insn-009e8ba4) · [`009e8ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8b88.md#insn-009e8ba8)
- 新版 [`009e9b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9b34.md#insn-009e9b48) · [`009e9b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9b34.md#insn-009e9b50) · [`009e9b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9b34.md#insn-009e9b54)

~~~diff
- 009e8b9c ["INT_ADD", "register:40f0:8", ["const:9e8b9c:8", "const:4:8"]]
- 009e8b9c ["CALL", null, ["callee:00c58f30:8"]]
+ 009e9b48 ["INT_ADD", "register:40f0:8", ["const:9e9b48:8", "const:4:8"]]
+ 009e9b48 ["CALL", null, ["callee:00c58f30:8"]]
- 009e8b9c bytes f1bc0994
+ 009e9b48 bytes fabc0994
- 009e8ba4 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009e9b50 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009e8ba4 bytes 081500b0
+ 009e9b50 bytes 081500b0
- 009e8ba8 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 009e8ba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e8ba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e8ba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e9b54 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 009e9b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e9b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e9b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e8ba8 bytes 08a13891
+ 009e9b54 bytes 08e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bf2b78577d647764bc6d4b19f8a9951"></a>

### [`009e8bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8bbc.md) → [`009e9b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9b68.md) FUN_009e9b68

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
      "definition_site": "009e9b74",
      "incomplete_value": false,
      "site": "009e9b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8bc8",
      "incomplete_value": false,
      "site": "009e8bc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
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
      "009e9b74",
      "DATA",
      [
        "storage",
        "00c89e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e9b74",
      "DATA",
      [
        "storage",
        "00c8adf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8bbc.md#insn-009e8bc0) · [`009e8bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8bbc.md#insn-009e8bc4)
- 新版 [`009e9b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9b68.md#insn-009e9b6c) · [`009e9b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9b68.md#insn-009e9b70)

~~~diff
- 009e8bc0 ["COPY", "register:4048:8", ["const:c89000:8"]]
+ 009e9b6c ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 009e8bc0 bytes 091500b0
+ 009e9b6c bytes 091500b0
- 009e8bc4 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 009e8bc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009e8bc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009e8bc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009e9b70 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 009e9b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009e9b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009e9b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009e8bc4 bytes 29a13891
+ 009e9b70 bytes 29e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ca5d5e7508846e2931f05a226f0748b"></a>

### [`009e8bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8bd8.md) → [`009e9b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9b84.md) FUN_009e9b84

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`00a1b6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b6a4.md)

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
      "site": "009e9bac",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009e8c00",
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
      "009e9bac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "009e9bac",
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

- 旧版 [`009e8c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8bd8.md#insn-009e8c00) · [`009e8c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8bd8.md#insn-009e8c0c) · [`009e8c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8bd8.md#insn-009e8c30)
- 新版 [`009e9bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9b84.md#insn-009e9bac) · [`009e9bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9b84.md#insn-009e9bb8) · [`009e9bdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9b84.md#insn-009e9bdc)

~~~diff
- 009e8c00 ["INT_ADD", "register:40f0:8", ["const:9e8c00:8", "const:4:8"]]
- 009e8c00 ["CALL", null, ["ram:47ad34:8"]]
+ 009e9bac ["INT_ADD", "register:40f0:8", ["const:9e9bac:8", "const:4:8"]]
+ 009e9bac ["CALL", null, ["ram:47b054:8"]]
- 009e8c00 bytes 4d48ea97
+ 009e9bac bytes 2a45ea97
- 009e8c0c ["INT_ADD", "register:40f0:8", ["const:9e8c0c:8", "const:4:8"]]
- 009e8c0c ["CALL", null, ["callee:0047d134:8"]]
+ 009e9bb8 ["INT_ADD", "register:40f0:8", ["const:9e9bb8:8", "const:4:8"]]
+ 009e9bb8 ["CALL", null, ["callee:0047d134:8"]]
- 009e8c0c bytes 8250ea97
+ 009e9bb8 bytes 5f4dea97
- 009e8c30 ["INT_ADD", "register:40f0:8", ["const:9e8c30:8", "const:4:8"]]
- 009e8c30 ["CALL", null, ["callee:008524fc:8"]]
+ 009e9bdc ["INT_ADD", "register:40f0:8", ["const:9e9bdc:8", "const:4:8"]]
+ 009e9bdc ["CALL", null, ["callee:008524fc:8"]]
- 009e8c30 bytes 48a2f997
+ 009e9bdc bytes 48a2f997
~~~


<a id="compare-26c9b19de36f0434c4e3b31948af52cf"></a>

### [`009e8c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8c78.md) → [`009e9c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9c24.md) FUN_009e9c24

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
      "definition_site": "009e9c48",
      "incomplete_value": false,
      "site": "009e9c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8c9c",
      "incomplete_value": false,
      "site": "009e8c9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
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
      "009e9c48",
      "DATA",
      [
        "storage",
        "00c89ea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e9c48",
      "DATA",
      [
        "storage",
        "00c8ae78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8c78.md#insn-009e8c8c) · [`009e8c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8c78.md#insn-009e8c94) · [`009e8c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8c78.md#insn-009e8c98)
- 新版 [`009e9c38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9c24.md#insn-009e9c38) · [`009e9c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9c24.md#insn-009e9c40) · [`009e9c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9c24.md#insn-009e9c44)

~~~diff
- 009e8c8c ["INT_ADD", "register:40f0:8", ["const:9e8c8c:8", "const:4:8"]]
- 009e8c8c ["CALL", null, ["callee:00c58f30:8"]]
+ 009e9c38 ["INT_ADD", "register:40f0:8", ["const:9e9c38:8", "const:4:8"]]
+ 009e9c38 ["CALL", null, ["callee:00c58f30:8"]]
- 009e8c8c bytes b5bc0994
+ 009e9c38 bytes bebc0994
- 009e8c94 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009e9c40 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009e8c94 bytes 081500b0
+ 009e9c40 bytes 081500b0
- 009e8c98 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 009e8c98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e8c98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e8c98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e9c44 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 009e9c44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e9c44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e9c44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e8c98 bytes 08a13a91
+ 009e9c44 bytes 08e13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c36b1dad1396fa5f33daa6b052f7826d"></a>

### [`009e8cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cac.md) → [`009e9c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9c58.md) FUN_009e9c58

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
      "definition_site": "009e9c64",
      "incomplete_value": false,
      "site": "009e9c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8cb8",
      "incomplete_value": false,
      "site": "009e8cb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
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
      "009e9c64",
      "DATA",
      [
        "storage",
        "00c89ea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e9c64",
      "DATA",
      [
        "storage",
        "00c8ae78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cac.md#insn-009e8cb0) · [`009e8cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cac.md#insn-009e8cb4)
- 新版 [`009e9c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9c58.md#insn-009e9c5c) · [`009e9c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9c58.md#insn-009e9c60)

~~~diff
- 009e8cb0 ["COPY", "register:4048:8", ["const:c89000:8"]]
+ 009e9c5c ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 009e8cb0 bytes 091500b0
+ 009e9c5c bytes 091500b0
- 009e8cb4 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 009e8cb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009e8cb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009e8cb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009e9c60 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 009e9c60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009e9c60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009e9c60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009e8cb4 bytes 29a13a91
+ 009e9c60 bytes 29e13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5d5eadd31f890a41c628a3d76f4b1ff"></a>

### [`009e8cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cc8.md) → [`009e9c74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9c74.md) FUN_009e9c74

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`00a1b6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b6a4.md)

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
      "site": "009e9c9c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009e8cf0",
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
      "009e9c9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "009e9c9c",
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

- 旧版 [`009e8cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cc8.md#insn-009e8cf0) · [`009e8cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cc8.md#insn-009e8cfc) · [`009e8d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cc8.md#insn-009e8d20)
- 新版 [`009e9c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9c74.md#insn-009e9c9c) · [`009e9ca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9c74.md#insn-009e9ca8) · [`009e9ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9c74.md#insn-009e9ccc)

~~~diff
- 009e8cf0 ["INT_ADD", "register:40f0:8", ["const:9e8cf0:8", "const:4:8"]]
- 009e8cf0 ["CALL", null, ["ram:47ad34:8"]]
+ 009e9c9c ["INT_ADD", "register:40f0:8", ["const:9e9c9c:8", "const:4:8"]]
+ 009e9c9c ["CALL", null, ["ram:47b054:8"]]
- 009e8cf0 bytes 1148ea97
+ 009e9c9c bytes ee44ea97
- 009e8cfc ["INT_ADD", "register:40f0:8", ["const:9e8cfc:8", "const:4:8"]]
- 009e8cfc ["CALL", null, ["callee:0047d134:8"]]
+ 009e9ca8 ["INT_ADD", "register:40f0:8", ["const:9e9ca8:8", "const:4:8"]]
+ 009e9ca8 ["CALL", null, ["callee:0047d134:8"]]
- 009e8cfc bytes 4650ea97
+ 009e9ca8 bytes 234dea97
- 009e8d20 ["INT_ADD", "register:40f0:8", ["const:9e8d20:8", "const:4:8"]]
- 009e8d20 ["CALL", null, ["callee:008524fc:8"]]
+ 009e9ccc ["INT_ADD", "register:40f0:8", ["const:9e9ccc:8", "const:4:8"]]
+ 009e9ccc ["CALL", null, ["callee:008524fc:8"]]
- 009e8d20 bytes 0ca2f997
+ 009e9ccc bytes 0ca2f997
~~~


<a id="compare-3fdd7c299c6bc66a65ba87ca9a46f08d"></a>

### [`009e8d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8d64.md) → [`009e9d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9d10.md) _INIT_204

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e9d4c",
      "incomplete_value": true,
      "site": "009e9d68",
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
      "definition_site": "009e8da0",
      "incomplete_value": true,
      "site": "009e8dbc",
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
      "definition_site": "009e9d70",
      "incomplete_value": true,
      "site": "009e9d8c",
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
      "definition_site": "009e8dc4",
      "incomplete_value": true,
      "site": "009e8de0",
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
      "definition_site": "009e9d90",
      "incomplete_value": true,
      "site": "009e9dac",
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
      "definition_site": "009e8de4",
      "incomplete_value": true,
      "site": "009e8e00",
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
      "009e9d4c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009e9d70",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009e9d90",
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
      "009e9d4c",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "009e9d70",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "009e9d90",
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

- 旧版 [`009e8ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8d64.md#insn-009e8ec4) · [`009e8f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8d64.md#insn-009e8f98) · [`009e8d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8d64.md#insn-009e8d8c)
- 新版 [`009e9e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9d10.md#insn-009e9e70) · [`009e9f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9d10.md#insn-009e9f44) · [`009e9d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e9/009e9d10.md#insn-009e9d38)

~~~diff
- 009e8ec4 ["INT_ADD", "register:40f0:8", ["const:9e8ec4:8", "const:4:8"]]
- 009e8ec4 ["CALL", null, ["callee:0043bb58:8"]]
+ 009e9e70 ["INT_ADD", "register:40f0:8", ["const:9e9e70:8", "const:4:8"]]
+ 009e9e70 ["CALL", null, ["callee:0043bb58:8"]]
- 009e8ec4 bytes 5d4ae997
+ 009e9e70 bytes 3a47e997
- 009e8f98 ["INT_ADD", "register:40f0:8", ["const:9e8f98:8", "const:4:8"]]
- 009e8f98 ["CALL", null, ["callee:00c58ed0:8"]]
+ 009e9f44 ["INT_ADD", "register:40f0:8", ["const:9e9f44:8", "const:4:8"]]
+ 009e9f44 ["CALL", null, ["callee:00c58ed0:8"]]
- 009e8f98 bytes dabb0994
+ 009e9f44 bytes e3bb0994
- 009e8d8c ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 009e9d38 ["COPY", "register:4098:8", ["const:1124000:8"]]
- 009e8d8c bytes d33900f0
+ 009e9d38 bytes d33900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1007d089b1a09bef9a5ba8cc24d6a9b7"></a>

### [`009e90f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e90f4.md) → [`009ea0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009ea0a0.md) FUN_009ea0a0

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009e94b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e94b4.md) · 呼出先 5件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`009ea460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009ea460.md) · 呼出先 5件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.76% / 新版 91.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ea108",
      "incomplete_value": true,
      "site": "009ea114",
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
                "const:670:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e915c",
      "incomplete_value": true,
      "site": "009e9168",
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
                "const:620:8"
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
      "definition_site": "009ea104",
      "incomplete_value": true,
      "site": "009ea118",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e9158",
      "incomplete_value": true,
      "site": "009e916c",
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
                "const:20:8"
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
      "definition_site": "009ea104",
      "incomplete_value": true,
      "site": "009ea118",
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
      "definition_site": "009e9158",
      "incomplete_value": true,
      "site": "009e916c",
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
      "009ea104",
      "READ",
      [
        "storage",
        "002a7fb0",
        null,
        "string"
      ]
    ],
    [
      "009ea104",
      "READ",
      [
        "storage",
        "002a7fc0",
        null,
        "string"
      ]
    ],
    [
      "009ea108",
      "READ",
      [
        "storage",
        "002c2620",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009ea104",
      "READ",
      [
        "storage",
        "002a8108",
        null,
        "string"
      ]
    ],
    [
      "009ea104",
      "READ",
      [
        "storage",
        "002a8118",
        null,
        "string"
      ]
    ],
    [
      "009ea108",
      "READ",
      [
        "storage",
        "002c2670",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e9148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e90f4.md#insn-009e9148) · [`009e914c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e90f4.md#insn-009e914c) · [`009e9150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e90f4.md#insn-009e9150)
- 新版 [`009ea0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009ea0a0.md#insn-009ea0f4) · [`009ea0f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009ea0a0.md#insn-009ea0f8) · [`009ea0fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009ea0a0.md#insn-009ea0fc)

~~~diff
- 009e9148 ["INT_ADD", "register:40f0:8", ["const:9e9148:8", "const:4:8"]]
- 009e9148 ["CALL", null, ["callee:00c58f30:8"]]
+ 009ea0f4 ["INT_ADD", "register:40f0:8", ["const:9ea0f4:8", "const:4:8"]]
+ 009ea0f4 ["CALL", null, ["callee:00c58f30:8"]]
- 009e9148 bytes 86bb0994
+ 009ea0f4 bytes 8fbb0994
- 009e914c ["COPY", "register:4040:8", ["const:2a7000:8"]]
+ 009ea0f8 ["COPY", "register:4040:8", ["const:2a8000:8"]]
- 009e914c bytes e8c5ffd0
+ 009ea0f8 bytes e8c5ffd0
- 009e9150 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 009e9150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e9150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e9150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ea0fc ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 009ea0fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ea0fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ea0fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e9150 bytes 08413e91
+ 009ea0fc bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7bbabd34392f2a258c7ff4e5e3df5d7"></a>

### [`009e94b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e94b4.md) → [`009ea460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009ea460.md) FUN_009ea460

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 19件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md)
- 新版 呼出元 1件 [`009f08e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f08e0.md) · 呼出先 19件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`00488794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488794.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.05% / 新版 88.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 13件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ea4a4",
      "incomplete_value": false,
      "site": "009ea4a8",
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
      "definition_site": "009e94f8",
      "incomplete_value": false,
      "site": "009e94fc",
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
      "definition_site": "009ea4c0",
      "incomplete_value": true,
      "site": "009ea4d0",
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
                "const:817:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e9514",
      "incomplete_value": true,
      "site": "009e9524",
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
                "const:7d7:8"
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
      "definition_site": "009ea4c4",
      "incomplete_value": true,
      "site": "009ea4d4",
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
      "definition_site": "009e9518",
      "incomplete_value": true,
      "site": "009e9528",
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
      "009ea4a8",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009ea4c0",
      "READ",
      [
        "storage",
        "002a07d7",
        null,
        "string"
      ]
    ],
    [
      "009ea4c4",
      "READ",
      [
        "storage",
        "002a07e7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ea4a8",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "009ea4c0",
      "READ",
      [
        "storage",
        "002a0817",
        null,
        "string"
      ]
    ],
    [
      "009ea4c4",
      "READ",
      [
        "storage",
        "002a0827",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e94f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e94b4.md#insn-009e94f0) · [`009e94f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e94b4.md#insn-009e94f4) · [`009e94f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e94b4.md#insn-009e94f8)
- 新版 [`009ea49c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009ea460.md#insn-009ea49c) · [`009ea4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009ea460.md#insn-009ea4a0) · [`009ea4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009ea460.md#insn-009ea4a4)

~~~diff
- 009e94f0 ["INT_ADD", "register:40f0:8", ["const:9e94f0:8", "const:4:8"]]
- 009e94f0 ["CALL", null, ["callee:00488180:8"]]
+ 009ea49c ["INT_ADD", "register:40f0:8", ["const:9ea49c:8", "const:4:8"]]
+ 009ea49c ["CALL", null, ["callee:00488180:8"]]
- 009e94f0 bytes 5c7aea97
+ 009ea49c bytes 3977ea97
- 009e94f4 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 009ea4a0 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 009e94f4 bytes c81300f0
+ 009ea4a0 bytes c81300f0
- 009e94f8 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 009e94f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e94f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e94f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ea4a4 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 009ea4a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ea4a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ea4a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e94f8 bytes 08213891
+ 009ea4a4 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f82c3aa00b234345cce6fe32d92acc51"></a>

### [`009e9ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9ac8.md) → [`009eaa74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009eaa74.md) FUN_009eaa74

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 18件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)
- 新版 呼出元 1件 [`009f08e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f08e0.md) · 呼出先 18件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`00488794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488794.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 17件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009eaab8",
      "incomplete_value": false,
      "site": "009eaabc",
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
      "definition_site": "009e9b0c",
      "incomplete_value": false,
      "site": "009e9b10",
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
      "definition_site": "009eaad8",
      "incomplete_value": true,
      "site": "009eaae0",
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
                "const:810:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e9b2c",
      "incomplete_value": true,
      "site": "009e9b34",
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
                "const:7c0:8"
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
      "definition_site": "009eaad4",
      "incomplete_value": true,
      "site": "009eaae4",
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
                "const:b7e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e9b28",
      "incomplete_value": true,
      "site": "009e9b38",
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
                "const:ab3:8"
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
      "009eaabc",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009eaad4",
      "READ",
      [
        "storage",
        "002a4ab3",
        null,
        "string"
      ]
    ],
    [
      "009eaad4",
      "READ",
      [
        "storage",
        "002a4ac3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009eaabc",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "009eaad4",
      "READ",
      [
        "storage",
        "002a4b7e",
        null,
        "string"
      ]
    ],
    [
      "009eaad4",
      "READ",
      [
        "storage",
        "002a4b8e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e9b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9ac8.md#insn-009e9b04) · [`009e9b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9ac8.md#insn-009e9b08) · [`009e9b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9ac8.md#insn-009e9b0c)
- 新版 [`009eaab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009eaa74.md#insn-009eaab0) · [`009eaab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009eaa74.md#insn-009eaab4) · [`009eaab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009eaa74.md#insn-009eaab8)

~~~diff
- 009e9b04 ["INT_ADD", "register:40f0:8", ["const:9e9b04:8", "const:4:8"]]
- 009e9b04 ["CALL", null, ["callee:00488180:8"]]
+ 009eaab0 ["INT_ADD", "register:40f0:8", ["const:9eaab0:8", "const:4:8"]]
+ 009eaab0 ["CALL", null, ["callee:00488180:8"]]
- 009e9b04 bytes d778ea97
+ 009eaab0 bytes b475ea97
- 009e9b08 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 009eaab4 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 009e9b08 bytes c81300f0
+ 009eaab4 bytes c81300f0
- 009e9b0c ["COPY", "tmp:0:8", ["const:e08:8"]]
- 009e9b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e9b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e9b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009eaab8 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 009eaab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009eaab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009eaab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e9b0c bytes 08213891
+ 009eaab8 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43529183efe5b922f9bd7d7b97dcdb25"></a>

### [`009e9fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9fd4.md) → [`009eaf80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009eaf80.md) FUN_009eaf80

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009e9ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9ac8.md) · 呼出先 5件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`009eaa74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009eaa74.md) · 呼出先 5件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.27% / 新版 93.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009eafe4",
      "incomplete_value": true,
      "site": "009eafec",
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
                "const:140:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ea038",
      "incomplete_value": true,
      "site": "009ea040",
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
                "const:f0:8"
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
      "definition_site": "009eafe0",
      "incomplete_value": true,
      "site": "009eaff0",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ea034",
      "incomplete_value": true,
      "site": "009ea044",
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
                "const:20:8"
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
      "definition_site": "009eafe0",
      "incomplete_value": true,
      "site": "009eaff0",
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
      "definition_site": "009ea034",
      "incomplete_value": true,
      "site": "009ea044",
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
      "009eafe0",
      "READ",
      [
        "storage",
        "002be0db",
        null,
        "string"
      ]
    ],
    [
      "009eafe0",
      "READ",
      [
        "storage",
        "002be0eb",
        null,
        "string"
      ]
    ],
    [
      "009eafe4",
      "READ",
      [
        "storage",
        "002c30f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009eafe0",
      "READ",
      [
        "storage",
        "002be1b9",
        null,
        "string"
      ]
    ],
    [
      "009eafe0",
      "READ",
      [
        "storage",
        "002be1c9",
        null,
        "string"
      ]
    ],
    [
      "009eafe4",
      "READ",
      [
        "storage",
        "002c3140",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ea024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9fd4.md#insn-009ea024) · [`009ea02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9fd4.md#insn-009ea02c) · [`009ea030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9fd4.md#insn-009ea030)
- 新版 [`009eafd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009eaf80.md#insn-009eafd0) · [`009eafd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009eaf80.md#insn-009eafd8)

~~~diff
- 009ea024 ["INT_ADD", "register:40f0:8", ["const:9ea024:8", "const:4:8"]]
- 009ea024 ["CALL", null, ["callee:00c58f30:8"]]
+ 009eafd0 ["INT_ADD", "register:40f0:8", ["const:9eafd0:8", "const:4:8"]]
+ 009eafd0 ["CALL", null, ["callee:00c58f30:8"]]
- 009ea024 bytes cfb70994
+ 009eafd0 bytes d8b70994
- 009ea02c ["COPY", "tmp:0:8", ["const:bb:8"]]
- 009ea02c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ea02c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ea02c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009eafd8 ["COPY", "tmp:0:8", ["const:199:8"]]
+ 009eafd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009eafd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009eafd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ea02c bytes 08ed0291
+ 009eafd8 bytes 08650691
- 009ea030 ["COPY", "register:4048:8", ["const:2c3000:8"]]
- 009ea030 bytes c9c6ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93f298232f5359102c148da78851d814"></a>

### [`009ea3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea3b8.md) → [`009eb364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009eb/009eb364.md) FUN_009eb364

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ea9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea9c8.md) · 呼出先 9件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md)
- 新版 呼出元 1件 [`009eb974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009eb/009eb974.md) · 呼出先 9件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009eb3d8",
      "incomplete_value": true,
      "site": "009eb3e0",
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
                "const:140:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ea42c",
      "incomplete_value": true,
      "site": "009ea434",
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
                "const:f0:8"
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
      "definition_site": "009eb3d4",
      "incomplete_value": true,
      "site": "009eb3e4",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ea428",
      "incomplete_value": true,
      "site": "009ea438",
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
                "const:20:8"
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
      "definition_site": "009eb3d4",
      "incomplete_value": true,
      "site": "009eb3e4",
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
      "definition_site": "009ea428",
      "incomplete_value": true,
      "site": "009ea438",
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
      "009eb394",
      "READ",
      [
        "storage",
        "002a936c",
        null,
        "string"
      ]
    ],
    [
      "009eb3d4",
      "READ",
      [
        "storage",
        "002b4359",
        null,
        "string"
      ]
    ],
    [
      "009eb3d4",
      "READ",
      [
        "storage",
        "002b4369",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009eb394",
      "READ",
      [
        "storage",
        "002a9439",
        null,
        "string"
      ]
    ],
    [
      "009eb3d4",
      "READ",
      [
        "storage",
        "002b4437",
        null,
        "string"
      ]
    ],
    [
      "009eb3d4",
      "READ",
      [
        "storage",
        "002b4447",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ea3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea3b8.md#insn-009ea3e0) · [`009ea418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea3b8.md#insn-009ea418) · [`009ea420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea3b8.md#insn-009ea420)
- 新版 [`009eb38c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009eb/009eb364.md#insn-009eb38c) · [`009eb3c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009eb/009eb364.md#insn-009eb3c4) · [`009eb3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009eb/009eb364.md#insn-009eb3cc)

~~~diff
- 009ea3e0 ["COPY", "tmp:0:8", ["const:36c:8"]]
- 009ea3e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009ea3e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009ea3e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009eb38c ["COPY", "tmp:0:8", ["const:439:8"]]
+ 009eb38c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009eb38c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009eb38c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009ea3e0 bytes 29b10d91
+ 009eb38c bytes 29e51091
- 009ea418 ["INT_ADD", "register:40f0:8", ["const:9ea418:8", "const:4:8"]]
- 009ea418 ["CALL", null, ["callee:00c58f30:8"]]
+ 009eb3c4 ["INT_ADD", "register:40f0:8", ["const:9eb3c4:8", "const:4:8"]]
+ 009eb3c4 ["CALL", null, ["callee:00c58f30:8"]]
- 009ea418 bytes d2b60994
+ 009eb3c4 bytes dbb60994
- 009ea420 ["COPY", "tmp:0:8", ["const:339:8"]]
- 009ea420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ea420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ea420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009eb3cc ["COPY", "tmp:0:8", ["const:417:8"]]
+ 009eb3cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009eb3cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009eb3cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ea420 bytes 08e50c91
+ 009eb3cc bytes 085d1091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efb94935491fa161d249e222f60ffc26"></a>

### [`009ea9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea9c8.md) → [`009eb974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009eb/009eb974.md) FUN_009eb974

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 19件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md)
- 新版 呼出元 1件 [`009f08e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f08e0.md) · 呼出先 19件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`00488794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488794.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.86% / 新版 88.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 17件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009eb9b8",
      "incomplete_value": false,
      "site": "009eb9bc",
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
      "definition_site": "009eaa0c",
      "incomplete_value": false,
      "site": "009eaa10",
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
      "definition_site": "009eb9d4",
      "incomplete_value": true,
      "site": "009eb9e4",
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eaa28",
      "incomplete_value": true,
      "site": "009eaa38",
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
                "const:7f0:8"
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
      "definition_site": "009eb9d8",
      "incomplete_value": true,
      "site": "009eb9e8",
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
                "const:c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eaa2c",
      "incomplete_value": true,
      "site": "009eaa3c",
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
                "const:c:8"
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
      "009eb9bc",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009eb9d4",
      "READ",
      [
        "storage",
        "002a07f0",
        null,
        "string"
      ]
    ],
    [
      "009eb9d8",
      "READ",
      [
        "storage",
        "002a07fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009eb9bc",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "009eb9d4",
      "READ",
      [
        "storage",
        "002a0830",
        null,
        "string"
      ]
    ],
    [
      "009eb9d8",
      "READ",
      [
        "storage",
        "002a083c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009eaa04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea9c8.md#insn-009eaa04) · [`009eaa08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea9c8.md#insn-009eaa08) · [`009eaa0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea9c8.md#insn-009eaa0c)
- 新版 [`009eb9b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009eb/009eb974.md#insn-009eb9b0) · [`009eb9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009eb/009eb974.md#insn-009eb9b4) · [`009eb9b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009eb/009eb974.md#insn-009eb9b8)

~~~diff
- 009eaa04 ["INT_ADD", "register:40f0:8", ["const:9eaa04:8", "const:4:8"]]
- 009eaa04 ["CALL", null, ["callee:00488180:8"]]
+ 009eb9b0 ["INT_ADD", "register:40f0:8", ["const:9eb9b0:8", "const:4:8"]]
+ 009eb9b0 ["CALL", null, ["callee:00488180:8"]]
- 009eaa04 bytes 1775ea97
+ 009eb9b0 bytes f471ea97
- 009eaa08 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 009eb9b4 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 009eaa08 bytes c81300d0
+ 009eb9b4 bytes c81300d0
- 009eaa0c ["COPY", "tmp:0:8", ["const:e08:8"]]
- 009eaa0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009eaa0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009eaa0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009eb9b8 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 009eb9b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009eb9b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009eb9b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009eaa0c bytes 08213891
+ 009eb9b8 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cc412d907c33d9efbfbdd19b837c3c5"></a>

### [`009eafd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md) → [`009ebf84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009eb/009ebf84.md) FUN_009ebf84

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ec2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec2a4.md) · 呼出先 15件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009e942c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e942c.md)
- 新版 呼出元 1件 [`009ed250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ed/009ed250.md) · 呼出先 15件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`009ea3d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ea/009ea3d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.06% / 新版 88.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_value` 45件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ebff4",
      "incomplete_value": true,
      "site": "009ec000",
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
                "const:b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eb048",
      "incomplete_value": true,
      "site": "009eb054",
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
                "const:60:8"
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
      "definition_site": "009ebff0",
      "incomplete_value": true,
      "site": "009ec004",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eb044",
      "incomplete_value": true,
      "site": "009eb058",
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
                "const:20:8"
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
      "definition_site": "009ebff0",
      "incomplete_value": true,
      "site": "009ec004",
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
      "definition_site": "009eb044",
      "incomplete_value": true,
      "site": "009eb058",
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
      "009ebff0",
      "READ",
      [
        "storage",
        "002b43b7",
        null,
        "string"
      ]
    ],
    [
      "009ebff0",
      "READ",
      [
        "storage",
        "002b43c7",
        null,
        "string"
      ]
    ],
    [
      "009ebff4",
      "READ",
      [
        "storage",
        "002c3060",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009ebff0",
      "READ",
      [
        "storage",
        "002b4495",
        null,
        "string"
      ]
    ],
    [
      "009ebff0",
      "READ",
      [
        "storage",
        "002b44a5",
        null,
        "string"
      ]
    ],
    [
      "009ebff4",
      "READ",
      [
        "storage",
        "002c30b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009eb034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md#insn-009eb034) · [`009eb03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md#insn-009eb03c) · [`009eb040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md#insn-009eb040)
- 新版 [`009ebfe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009eb/009ebf84.md#insn-009ebfe0) · [`009ebfe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009eb/009ebf84.md#insn-009ebfe8)

~~~diff
- 009eb034 ["INT_ADD", "register:40f0:8", ["const:9eb034:8", "const:4:8"]]
- 009eb034 ["CALL", null, ["callee:00c58f30:8"]]
+ 009ebfe0 ["INT_ADD", "register:40f0:8", ["const:9ebfe0:8", "const:4:8"]]
+ 009ebfe0 ["CALL", null, ["callee:00c58f30:8"]]
- 009eb034 bytes cbb30994
+ 009ebfe0 bytes d4b30994
- 009eb03c ["COPY", "tmp:0:8", ["const:397:8"]]
- 009eb03c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009eb03c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009eb03c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ebfe8 ["COPY", "tmp:0:8", ["const:475:8"]]
+ 009ebfe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ebfe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ebfe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009eb03c bytes 085d0e91
+ 009ebfe8 bytes 08d51191
- 009eb040 ["COPY", "register:4048:8", ["const:2c3000:8"]]
- 009eb040 bytes c9c6ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73c66c0086314451adc7059ab7fb78e1"></a>

### [`009ec8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec8ec.md) → [`009ed898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ed/009ed898.md) FUN_009ed898

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ed8b4",
      "incomplete_value": false,
      "site": "009ed8b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ec908",
      "incomplete_value": false,
      "site": "009ec90c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "009ed8b8",
      "DATA",
      [
        "storage",
        "00c8a080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ed8b8",
      "DATA",
      [
        "storage",
        "00c8b050",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ec904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec8ec.md#insn-009ec904) · [`009ec908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec8ec.md#insn-009ec908) · [`009ec944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec8ec.md#insn-009ec944)
- 新版 [`009ed8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ed/009ed898.md#insn-009ed8b0) · [`009ed8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ed/009ed898.md#insn-009ed8b4) · [`009ed8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ed/009ed898.md#insn-009ed8f0)

~~~diff
- 009ec904 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009ed8b0 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009ec904 bytes e81400d0
+ 009ed8b0 bytes e81400d0
- 009ec908 ["COPY", "tmp:0:8", ["const:80:8"]]
- 009ec908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ec908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ec908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ed8b4 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 009ed8b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ed8b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ed8b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ec908 bytes 08010291
+ 009ed8b4 bytes 08410191
- 009ec944 ["INT_ADD", "register:40f0:8", ["const:9ec944:8", "const:4:8"]]
- 009ec944 ["CALL", null, ["callee:00c54d90:8"]]
+ 009ed8f0 ["INT_ADD", "register:40f0:8", ["const:9ed8f0:8", "const:4:8"]]
+ 009ed8f0 ["CALL", null, ["callee:00c54d90:8"]]
- 009ec944 bytes 179d0994
+ 009ed8f0 bytes 289d0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbf5e543173bf6b78ef4c9a23cfd25fc"></a>

### [`009ec9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec9b0.md) → [`009ed95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ed/009ed95c.md) FUN_009ed95c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 18件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)
- 新版 呼出元 1件 [`009f08e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f08e0.md) · 呼出先 18件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`00488794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488794.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.61% / 新版 85.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 1件, `store_value` 15件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ed99c",
      "incomplete_value": false,
      "site": "009ed9a0",
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
      "definition_site": "009ec9f0",
      "incomplete_value": false,
      "site": "009ec9f4",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ed9b8",
      "incomplete_value": true,
      "site": "009ed9c8",
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
                "const:c04:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eca0c",
      "incomplete_value": true,
      "site": "009eca1c",
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
                "const:b26:8"
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
      "definition_site": "009eda64",
      "incomplete_value": true,
      "site": "009eda6c",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ecab8",
      "incomplete_value": true,
      "site": "009ecac0",
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
                "const:20:8"
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
      "009ed9a0",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009ed9b8",
      "READ",
      [
        "storage",
        "002bbb26",
        null,
        "string"
      ]
    ],
    [
      "009ed9bc",
      "READ",
      [
        "storage",
        "002bbb35",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ed9a0",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "009ed9b8",
      "READ",
      [
        "storage",
        "002bbc04",
        null,
        "string"
      ]
    ],
    [
      "009ed9bc",
      "READ",
      [
        "storage",
        "002bbc13",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ecb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec9b0.md#insn-009ecb88) · [`009ec9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec9b0.md#insn-009ec9e8) · [`009ec9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec9b0.md#insn-009ec9ec)
- 新版 [`009edb34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ed/009ed95c.md#insn-009edb34) · [`009ed994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ed/009ed95c.md#insn-009ed994) · [`009ed998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ed/009ed95c.md#insn-009ed998)

~~~diff
- 009ecb88 ["INT_ADD", "register:40f0:8", ["const:9ecb88:8", "const:4:8"]]
- 009ecb88 ["CALL", null, ["ram:9ece88:8"]]
+ 009edb34 ["INT_ADD", "register:40f0:8", ["const:9edb34:8", "const:4:8"]]
+ 009edb34 ["CALL", null, ["ram:9ede34:8"]]
- 009ecb88 bytes c0000094
+ 009edb34 bytes c0000094
- 009ec9e8 ["INT_ADD", "register:40f0:8", ["const:9ec9e8:8", "const:4:8"]]
- 009ec9e8 ["CALL", null, ["callee:00488180:8"]]
+ 009ed994 ["INT_ADD", "register:40f0:8", ["const:9ed994:8", "const:4:8"]]
+ 009ed994 ["CALL", null, ["callee:00488180:8"]]
- 009ec9e8 bytes 1e6dea97
+ 009ed994 bytes fb69ea97
- 009ec9ec ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 009ed998 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 009ec9ec bytes c8130090
+ 009ed998 bytes c8130090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e648d5f250a711949e75647122d42c97"></a>

### [`009ed16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed16c.md) → [`009ee118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009ee118.md) FUN_009ee118

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ed60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed60c.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009f3650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3650.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`009ee5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009ee5b8.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`009f45fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f45fc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.04% / 新版 90.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ee170",
      "incomplete_value": true,
      "site": "009ee170",
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
                "const:7a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ed1c4",
      "incomplete_value": true,
      "site": "009ed1c4",
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
                "const:760:8"
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
      "definition_site": "009ee18c",
      "incomplete_value": true,
      "site": "009ee1a0",
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
                "const:310:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ed1e0",
      "incomplete_value": true,
      "site": "009ed1f4",
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
                "const:2c0:8"
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
      "definition_site": "009ee198",
      "incomplete_value": true,
      "site": "009ee1a8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ed1ec",
      "incomplete_value": true,
      "site": "009ed1fc",
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
                "const:20:8"
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
      "009ee148",
      "READ",
      [
        "storage",
        "002a1760",
        null,
        "string"
      ]
    ],
    [
      "009ee18c",
      "READ",
      [
        "storage",
        "002c22c0",
        null,
        null
      ]
    ],
    [
      "009ee198",
      "READ",
      [
        "storage",
        "002abd2b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ee148",
      "READ",
      [
        "storage",
        "002a17a0",
        null,
        "string"
      ]
    ],
    [
      "009ee18c",
      "READ",
      [
        "storage",
        "002c2310",
        null,
        null
      ]
    ],
    [
      "009ee198",
      "READ",
      [
        "storage",
        "002abdf8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ed194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed16c.md#insn-009ed194) · [`009ed1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed16c.md#insn-009ed1d0) · [`009ed1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed16c.md#insn-009ed1e0)
- 新版 [`009ee140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009ee118.md#insn-009ee140) · [`009ee17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009ee118.md#insn-009ee17c) · [`009ee18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009ee118.md#insn-009ee18c)

~~~diff
- 009ed194 ["COPY", "tmp:0:8", ["const:760:8"]]
- 009ed194 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009ed194 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009ed194 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009ee140 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 009ee140 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009ee140 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009ee140 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009ed194 bytes 4a811d91
+ 009ee140 bytes 4a811e91
- 009ed1d0 ["INT_ADD", "register:40f0:8", ["const:9ed1d0:8", "const:4:8"]]
- 009ed1d0 ["CALL", null, ["callee:00c58f30:8"]]
+ 009ee17c ["INT_ADD", "register:40f0:8", ["const:9ee17c:8", "const:4:8"]]
+ 009ee17c ["CALL", null, ["callee:00c58f30:8"]]
- 009ed1d0 bytes 64ab0994
+ 009ee17c bytes 6dab0994
- 009ed1e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c0:8"]]
- 009ed1e0 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 009ed1e0 ["COPY", "register:5010:8", ["const:0:8"]]
- 009ed1e0 ["COPY", "register:5018:8", ["const:0:8"]]
+ 009ee18c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:310:8"]]
+ 009ee18c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 009ee18c ["COPY", "register:5010:8", ["const:0:8"]]
+ 009ee18c ["COPY", "register:5018:8", ["const:0:8"]]
- 009ed1e0 bytes 00b1c03d
+ 009ee18c bytes 00c5c03d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d0ef908ae91159d43df7868b09bf77c"></a>

### [`009ed60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed60c.md) → [`009ee5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009ee5b8.md) FUN_009ee5b8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 19件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)
- 新版 呼出元 1件 [`009f08e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f08e0.md) · 呼出先 19件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`00488794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488794.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.11% / 新版 83.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 22件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ee5f4",
      "incomplete_value": false,
      "site": "009ee5f8",
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
      "definition_site": "009ed648",
      "incomplete_value": false,
      "site": "009ed64c",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ee610",
      "incomplete_value": true,
      "site": "009ee620",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:a7e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ed664",
      "incomplete_value": true,
      "site": "009ed674",
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
                "const:2b6000:8"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ee614",
      "incomplete_value": true,
      "site": "009ee624",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ed668",
      "incomplete_value": true,
      "site": "009ed678",
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
                "const:f:8"
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
      "009ee5f8",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009ee610",
      "READ",
      [
        "storage",
        "002b69af",
        null,
        "string"
      ]
    ],
    [
      "009ee614",
      "READ",
      [
        "storage",
        "002b69be",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ee5f8",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "009ee610",
      "READ",
      [
        "storage",
        "002b6a7e",
        null,
        "string"
      ]
    ],
    [
      "009ee614",
      "READ",
      [
        "storage",
        "002b6a8d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ed640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed60c.md#insn-009ed640) · [`009ed644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed60c.md#insn-009ed644) · [`009ed648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed60c.md#insn-009ed648)
- 新版 [`009ee5ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009ee5b8.md#insn-009ee5ec) · [`009ee5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009ee5b8.md#insn-009ee5f0) · [`009ee5f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009ee5b8.md#insn-009ee5f4)

~~~diff
- 009ed640 ["INT_ADD", "register:40f0:8", ["const:9ed640:8", "const:4:8"]]
- 009ed640 ["CALL", null, ["callee:00488180:8"]]
+ 009ee5ec ["INT_ADD", "register:40f0:8", ["const:9ee5ec:8", "const:4:8"]]
+ 009ee5ec ["CALL", null, ["callee:00488180:8"]]
- 009ed640 bytes 086aea97
+ 009ee5ec bytes e566ea97
- 009ed644 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 009ee5f0 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 009ed644 bytes a81300f0
+ 009ee5f0 bytes a81300f0
- 009ed648 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 009ed648 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ed648 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ed648 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ee5f4 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 009ee5f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ee5f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ee5f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ed648 bytes 08213891
+ 009ee5f4 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50273161c563f4ad727158532bff6fab"></a>

### [`009edb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edb90.md) → [`009eeb3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009eeb3c.md) FUN_009eeb3c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009edf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edf50.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009f2e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e38.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`009eeefc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009eeefc.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`009f3de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3de4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.59% / 新版 91.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009eeb94",
      "incomplete_value": true,
      "site": "009eeb94",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:46c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009edbe8",
      "incomplete_value": true,
      "site": "009edbe8",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:39f:8"
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
      "definition_site": "009eebb4",
      "incomplete_value": true,
      "site": "009eebc0",
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
                "const:850:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009edc08",
      "incomplete_value": true,
      "site": "009edc14",
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
                "const:800:8"
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
      "definition_site": "009eebb0",
      "incomplete_value": true,
      "site": "009eebc4",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009edc04",
      "incomplete_value": true,
      "site": "009edc18",
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
                "const:40:8"
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
      "009eeb6c",
      "READ",
      [
        "storage",
        "002aa39f",
        null,
        "string"
      ]
    ],
    [
      "009eebb0",
      "READ",
      [
        "storage",
        "002b5619",
        null,
        "string"
      ]
    ],
    [
      "009eebb0",
      "READ",
      [
        "storage",
        "002b5629",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009eeb6c",
      "READ",
      [
        "storage",
        "002aa46c",
        null,
        "string"
      ]
    ],
    [
      "009eebb0",
      "READ",
      [
        "storage",
        "002b56f7",
        null,
        "string"
      ]
    ],
    [
      "009eebb0",
      "READ",
      [
        "storage",
        "002b5707",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009edbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edb90.md#insn-009edbb8) · [`009edbf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edb90.md#insn-009edbf4) · [`009edbfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edb90.md#insn-009edbfc)
- 新版 [`009eeb64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009eeb3c.md#insn-009eeb64) · [`009eeba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009eeb3c.md#insn-009eeba0) · [`009eeba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009eeb3c.md#insn-009eeba8)

~~~diff
- 009edbb8 ["COPY", "tmp:0:8", ["const:39f:8"]]
- 009edbb8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009edbb8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009edbb8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009eeb64 ["COPY", "tmp:0:8", ["const:46c:8"]]
+ 009eeb64 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009eeb64 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009eeb64 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009edbb8 bytes 4a7d0e91
+ 009eeb64 bytes 4ab11191
- 009edbf4 ["INT_ADD", "register:40f0:8", ["const:9edbf4:8", "const:4:8"]]
- 009edbf4 ["CALL", null, ["callee:00c58f30:8"]]
+ 009eeba0 ["INT_ADD", "register:40f0:8", ["const:9eeba0:8", "const:4:8"]]
+ 009eeba0 ["CALL", null, ["callee:00c58f30:8"]]
- 009edbf4 bytes dba80994
+ 009eeba0 bytes e4a80994
- 009edbfc ["COPY", "tmp:0:8", ["const:5d9:8"]]
- 009edbfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009edbfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009edbfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009eeba8 ["COPY", "tmp:0:8", ["const:6b7:8"]]
+ 009eeba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009eeba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009eeba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009edbfc bytes 08651791
+ 009eeba8 bytes 08dd1a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0cf68fd69e8725a321c29d8d99e87ca"></a>

### [`009ee388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee388.md) → [`009ef334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ef/009ef334.md) FUN_009ef334

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 20件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md)
- 新版 呼出元 1件 [`009f08e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f08e0.md) · 呼出先 20件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`00488794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488794.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.97% / 新版 89.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 16件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ef378",
      "incomplete_value": false,
      "site": "009ef37c",
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
      "definition_site": "009ee3cc",
      "incomplete_value": false,
      "site": "009ee3d0",
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
      "definition_site": "009ef398",
      "incomplete_value": true,
      "site": "009ef3a8",
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
      "definition_site": "009ee3ec",
      "incomplete_value": true,
      "site": "009ee3fc",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ef394",
      "incomplete_value": true,
      "site": "009ef3ac",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ee3e8",
      "incomplete_value": true,
      "site": "009ee400",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:abc:8"
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
      "009ef37c",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009ef394",
      "READ",
      [
        "storage",
        "002baabc",
        null,
        "string"
      ]
    ],
    [
      "009ef394",
      "READ",
      [
        "storage",
        "002baacc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ef37c",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "009ef394",
      "READ",
      [
        "storage",
        "002bab9a",
        null,
        "string"
      ]
    ],
    [
      "009ef394",
      "READ",
      [
        "storage",
        "002babaa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ee3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee388.md#insn-009ee3c4) · [`009ee3c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee388.md#insn-009ee3c8) · [`009ee3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee388.md#insn-009ee3cc)
- 新版 [`009ef370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ef/009ef334.md#insn-009ef370) · [`009ef374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ef/009ef334.md#insn-009ef374) · [`009ef378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ef/009ef334.md#insn-009ef378)

~~~diff
- 009ee3c4 ["INT_ADD", "register:40f0:8", ["const:9ee3c4:8", "const:4:8"]]
- 009ee3c4 ["CALL", null, ["callee:00488180:8"]]
+ 009ef370 ["INT_ADD", "register:40f0:8", ["const:9ef370:8", "const:4:8"]]
+ 009ef370 ["CALL", null, ["callee:00488180:8"]]
- 009ee3c4 bytes a766ea97
+ 009ef370 bytes 8463ea97
- 009ee3c8 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 009ef374 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 009ee3c8 bytes a81300d0
+ 009ef374 bytes a81300d0
- 009ee3cc ["COPY", "tmp:0:8", ["const:e08:8"]]
- 009ee3cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ee3cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ee3cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ef378 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 009ef378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ef378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ef378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ee3cc bytes 08213891
+ 009ef378 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1325647fe466d3379723b8429b3ef809"></a>

### [`009ee9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee9c4.md) → [`009ef970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ef/009ef970.md) FUN_009ef970

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009eed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009eed04.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009f2e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e38.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`009efcb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ef/009efcb0.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`009f3de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3de4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.72% / 新版 95.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ef9c8",
      "incomplete_value": true,
      "site": "009ef9c8",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:46c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eea1c",
      "incomplete_value": true,
      "site": "009eea1c",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:39f:8"
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
      "009ef9a0",
      "READ",
      [
        "storage",
        "002aa39f",
        null,
        "string"
      ]
    ],
    [
      "009ef9e4",
      "READ",
      [
        "storage",
        "002b5619",
        null,
        "string"
      ]
    ],
    [
      "009ef9e4",
      "READ",
      [
        "storage",
        "002b5629",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ef9a0",
      "READ",
      [
        "storage",
        "002aa46c",
        null,
        "string"
      ]
    ],
    [
      "009ef9e4",
      "READ",
      [
        "storage",
        "002b56f7",
        null,
        "string"
      ]
    ],
    [
      "009ef9e4",
      "READ",
      [
        "storage",
        "002b5707",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ee9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee9c4.md#insn-009ee9ec) · [`009eea28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee9c4.md#insn-009eea28) · [`009eea30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee9c4.md#insn-009eea30)
- 新版 [`009ef998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ef/009ef970.md#insn-009ef998) · [`009ef9d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ef/009ef970.md#insn-009ef9d4) · [`009ef9dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ef/009ef970.md#insn-009ef9dc)

~~~diff
- 009ee9ec ["COPY", "tmp:0:8", ["const:39f:8"]]
- 009ee9ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009ee9ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009ee9ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009ef998 ["COPY", "tmp:0:8", ["const:46c:8"]]
+ 009ef998 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009ef998 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009ef998 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009ee9ec bytes 4a7d0e91
+ 009ef998 bytes 4ab11191
- 009eea28 ["INT_ADD", "register:40f0:8", ["const:9eea28:8", "const:4:8"]]
- 009eea28 ["CALL", null, ["callee:00c58f30:8"]]
+ 009ef9d4 ["INT_ADD", "register:40f0:8", ["const:9ef9d4:8", "const:4:8"]]
+ 009ef9d4 ["CALL", null, ["callee:00c58f30:8"]]
- 009eea28 bytes 4ea50994
+ 009ef9d4 bytes 57a50994
- 009eea30 ["COPY", "tmp:0:8", ["const:5d9:8"]]
- 009eea30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009eea30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009eea30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ef9dc ["COPY", "tmp:0:8", ["const:6b7:8"]]
+ 009ef9dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ef9dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ef9dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009eea30 bytes 08651791
+ 009ef9dc bytes 08dd1a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa0d551b84c9d4d73f2d21112171cf2d"></a>

### [`009ef078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef078.md) → [`009f0024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f0024.md) FUN_009f0024

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 20件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md)
- 新版 呼出元 1件 [`009f08e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f08e0.md) · 呼出先 20件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`00488794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488794.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.05% / 新版 92.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f0068",
      "incomplete_value": false,
      "site": "009f006c",
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
      "definition_site": "009ef0bc",
      "incomplete_value": false,
      "site": "009ef0c0",
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
      "definition_site": "009f0084",
      "incomplete_value": true,
      "site": "009f0094",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:479:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ef0d8",
      "incomplete_value": true,
      "site": "009ef0e8",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:3ac:8"
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
      "definition_site": "009f0088",
      "incomplete_value": true,
      "site": "009f0098",
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
                "const:c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ef0dc",
      "incomplete_value": true,
      "site": "009ef0ec",
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
                "const:c:8"
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
      "009f006c",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009f0084",
      "READ",
      [
        "storage",
        "002aa3ac",
        null,
        "string"
      ]
    ],
    [
      "009f0088",
      "READ",
      [
        "storage",
        "002aa3b8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009f006c",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "009f0084",
      "READ",
      [
        "storage",
        "002aa479",
        null,
        "string"
      ]
    ],
    [
      "009f0088",
      "READ",
      [
        "storage",
        "002aa485",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ef0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef078.md#insn-009ef0b4) · [`009ef0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef078.md#insn-009ef0b8) · [`009ef0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef078.md#insn-009ef0bc)
- 新版 [`009f0060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f0024.md#insn-009f0060) · [`009f0064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f0024.md#insn-009f0064) · [`009f0068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f0024.md#insn-009f0068)

~~~diff
- 009ef0b4 ["INT_ADD", "register:40f0:8", ["const:9ef0b4:8", "const:4:8"]]
- 009ef0b4 ["CALL", null, ["callee:00488180:8"]]
+ 009f0060 ["INT_ADD", "register:40f0:8", ["const:9f0060:8", "const:4:8"]]
+ 009f0060 ["CALL", null, ["callee:00488180:8"]]
- 009ef0b4 bytes 6b63ea97
+ 009f0060 bytes 4860ea97
- 009ef0b8 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 009f0064 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 009ef0b8 bytes a81300b0
+ 009f0064 bytes a81300b0
- 009ef0bc ["COPY", "tmp:0:8", ["const:e08:8"]]
- 009ef0bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ef0bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ef0bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f0068 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 009f0068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f0068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f0068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ef0bc bytes 08213891
+ 009f0068 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8dd7d2047f4bd13d4cf05c6b6e6e799"></a>

### [`009ef6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef6c0.md) → [`009f066c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f066c.md) FUN_009f066c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009f2658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2658.md) · 呼出先 2件 [`009f3938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3938.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`009f3604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3604.md) · 呼出先 2件 [`009f48e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f48e4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f06b8",
      "incomplete_value": false,
      "site": "009f06bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ef70c",
      "incomplete_value": false,
      "site": "009ef710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f06bc",
      "DATA",
      [
        "storage",
        "00c89f28",
        null,
        "undefined *"
      ]
    ],
    [
      "009f078c",
      "DATA",
      [
        "storage",
        "00c8a480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f06bc",
      "DATA",
      [
        "storage",
        "00c8aef8",
        null,
        "undefined *"
      ]
    ],
    [
      "009f078c",
      "DATA",
      [
        "storage",
        "00c8b450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ef708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef6c0.md#insn-009ef708) · [`009ef70c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef6c0.md#insn-009ef70c) · [`009ef7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef6c0.md#insn-009ef7c0)
- 新版 [`009f06b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f066c.md#insn-009f06b4) · [`009f06b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f066c.md#insn-009f06b8) · [`009f076c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f066c.md#insn-009f076c)

~~~diff
- 009ef708 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f06b4 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009ef708 bytes c81400d0
+ 009f06b4 bytes c81400d0
- 009ef70c ["COPY", "tmp:0:8", ["const:f28:8"]]
- 009ef70c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ef70c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ef70c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f06b8 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 009f06b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f06b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f06b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ef70c bytes 08a13c91
+ 009f06b8 bytes 08e13b91
- 009ef7c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 009ef7c0 ["INT_ADD", "register:40f0:8", ["const:9ef7c0:8", "const:4:8"]]
- 009ef7c0 ["CALLIND", null, ["register:0:8"]]
+ 009f076c ["COPY", "register:0:8", ["register:4048:8"]]
+ 009f076c ["INT_ADD", "register:40f0:8", ["const:9f076c:8", "const:4:8"]]
+ 009f076c ["CALLIND", null, ["register:0:8"]]
- 009ef7c0 bytes 20013fd6
+ 009f076c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9137473dd26b6320e7a659d5af2d11ad"></a>

### [`009efe3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md) → [`009f0de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f0de8.md) FUN_009f0de8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009f0560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md) [`009f0d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md) · 呼出先 9件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009f3b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b0c.md) [`009f3b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b20.md)
- 新版 呼出元 2件 [`009f150c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f1/009f150c.md) [`009f1d34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f1/009f1d34.md) · 呼出先 9件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`009f4ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4ab8.md) [`009f4acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4acc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f11c4",
      "incomplete_value": true,
      "site": "009f11cc",
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
                "const:2d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f0218",
      "incomplete_value": true,
      "site": "009f0220",
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
                "const:280:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f11c0",
      "incomplete_value": true,
      "site": "009f11d0",
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
                "const:eef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f0214",
      "incomplete_value": true,
      "site": "009f0224",
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
                "const:d97:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 49,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f11c0",
      "incomplete_value": true,
      "site": "009f11d0",
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
      "definition_site": "009f0214",
      "incomplete_value": true,
      "site": "009f0224",
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
      "009f11c0",
      "READ",
      [
        "storage",
        "002a5d97",
        null,
        "string"
      ]
    ],
    [
      "009f11c0",
      "READ",
      [
        "storage",
        "002a5da7",
        null,
        "string"
      ]
    ],
    [
      "009f11c4",
      "READ",
      [
        "storage",
        "002c2280",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009f11c0",
      "READ",
      [
        "storage",
        "002a5eef",
        null,
        "string"
      ]
    ],
    [
      "009f11c0",
      "READ",
      [
        "storage",
        "002a5eff",
        null,
        "string"
      ]
    ],
    [
      "009f11c4",
      "READ",
      [
        "storage",
        "002c22d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009effec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md#insn-009effec) · [`009f0024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md#insn-009f0024) · [`009f0038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md#insn-009f0038)
- 新版 [`009f0f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f0de8.md#insn-009f0f98) · [`009f0fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f0de8.md#insn-009f0fd0) · [`009f0fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f0de8.md#insn-009f0fe4)

~~~diff
- 009effec ["INT_ADD", "register:40f0:8", ["const:9effec:8", "const:4:8"]]
- 009effec ["CALL", null, ["callee:00c58f30:8"]]
+ 009f0f98 ["INT_ADD", "register:40f0:8", ["const:9f0f98:8", "const:4:8"]]
+ 009f0f98 ["CALL", null, ["callee:00c58f30:8"]]
- 009effec bytes dd9f0994
+ 009f0f98 bytes e69f0994
- 009f0024 ["INT_ADD", "register:40f0:8", ["const:9f0024:8", "const:4:8"]]
- 009f0024 ["CALL", null, ["callee:00c590a0:8"]]
+ 009f0fd0 ["INT_ADD", "register:40f0:8", ["const:9f0fd0:8", "const:4:8"]]
+ 009f0fd0 ["CALL", null, ["callee:00c590a0:8"]]
- 009f0024 bytes 2ba00994
+ 009f0fd0 bytes 34a00994
- 009f0038 ["INT_ADD", "register:40f0:8", ["const:9f0038:8", "const:4:8"]]
- 009f0038 ["CALL", null, ["callee:00c58f50:8"]]
+ 009f0fe4 ["INT_ADD", "register:40f0:8", ["const:9f0fe4:8", "const:4:8"]]
+ 009f0fe4 ["CALL", null, ["callee:00c58f50:8"]]
- 009f0038 bytes d29f0994
+ 009f0fe4 bytes db9f0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59cfb145ca0b820e7fe2c3da513203db"></a>

### [`009f0560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md) → [`009f150c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f1/009f150c.md) FUN_009f150c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009f24f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f24f8.md) · 呼出先 11件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`009efe3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md) [`009f3b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b0c.md)
- 新版 呼出元 1件 [`009f34a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f34a4.md) · 呼出先 11件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`009f0de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f0de8.md) [`009f4ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4ab8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.18% / 新版 99.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009f15f8",
      "incomplete_value": false,
      "site": "009f1608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f064c",
      "incomplete_value": false,
      "site": "009f065c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "definition_site": "009f1600",
      "incomplete_value": false,
      "site": "009f1608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f0654",
      "incomplete_value": false,
      "site": "009f065c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009f166c",
      "incomplete_value": false,
      "site": "009f167c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f06c0",
      "incomplete_value": false,
      "site": "009f06d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "009f15f8",
      "PARAM",
      [
        "storage",
        "00c89f88",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f1600",
      "PARAM",
      [
        "storage",
        "00c89fe0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f166c",
      "PARAM",
      [
        "storage",
        "00c89f88",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f15f8",
      "PARAM",
      [
        "storage",
        "00c8af58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f1600",
      "PARAM",
      [
        "storage",
        "00c8afb0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f166c",
      "PARAM",
      [
        "storage",
        "00c8af58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f065c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md#insn-009f065c) · [`009f06d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md#insn-009f06d0) · [`009f05ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md#insn-009f05ac)
- 新版 [`009f1608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f1/009f150c.md#insn-009f1608) · [`009f167c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f1/009f150c.md#insn-009f167c) · [`009f1558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f1/009f150c.md#insn-009f1558)

~~~diff
- 009f065c ["INT_ADD", "register:40f0:8", ["const:9f065c:8", "const:4:8"]]
- 009f065c ["CALL", null, ["callee:00c596b0:8"]]
+ 009f1608 ["INT_ADD", "register:40f0:8", ["const:9f1608:8", "const:4:8"]]
+ 009f1608 ["CALL", null, ["callee:00c596b0:8"]]
- 009f065c bytes 21a00994
+ 009f1608 bytes 2aa00994
- 009f06d0 ["INT_ADD", "register:40f0:8", ["const:9f06d0:8", "const:4:8"]]
- 009f06d0 ["CALL", null, ["callee:00c596b0:8"]]
+ 009f167c ["INT_ADD", "register:40f0:8", ["const:9f167c:8", "const:4:8"]]
+ 009f167c ["CALL", null, ["callee:00c596b0:8"]]
- 009f06d0 bytes 04a00994
+ 009f167c bytes 0da00994
- 009f05ac ["INT_ADD", "register:40f0:8", ["const:9f05ac:8", "const:4:8"]]
- 009f05ac ["CALL", null, ["callee:009f0de8:8"]]
+ 009f1558 ["INT_ADD", "register:40f0:8", ["const:9f1558:8", "const:4:8"]]
+ 009f1558 ["CALL", null, ["callee:009f0de8:8"]]
- 009f05ac bytes 24feff97
+ 009f1558 bytes 24feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c15c3808c9bac6e126f35da24c7602f"></a>

### [`009f0d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md) → [`009f1d34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f1/009f1d34.md) FUN_009f1d34

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009efe3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md) [`009f109c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f109c.md) [`009f3850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3850.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`009f0de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f0de8.md) [`009f2048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f2048.md) [`009f47fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f47fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f1df4",
      "incomplete_value": true,
      "site": "009f1e04",
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
                "const:150:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f0e48",
      "incomplete_value": true,
      "site": "009f0e58",
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
                "const:100:8"
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
      "definition_site": "009f1df8",
      "incomplete_value": true,
      "site": "009f1e14",
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
                "const:261:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f0e4c",
      "incomplete_value": true,
      "site": "009f0e68",
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
                "const:217:8"
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
      "definition_site": "009f1df8",
      "incomplete_value": true,
      "site": "009f1e14",
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
      "definition_site": "009f0e4c",
      "incomplete_value": true,
      "site": "009f0e68",
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
      "009f1df4",
      "READ",
      [
        "storage",
        "002c2100",
        null,
        null
      ]
    ],
    [
      "009f1df8",
      "READ",
      [
        "storage",
        "002b3217",
        null,
        "string"
      ]
    ],
    [
      "009f1df8",
      "READ",
      [
        "storage",
        "002b3227",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009f1df4",
      "READ",
      [
        "storage",
        "002c2150",
        null,
        null
      ]
    ],
    [
      "009f1df8",
      "READ",
      [
        "storage",
        "002b3261",
        null,
        "string"
      ]
    ],
    [
      "009f1df8",
      "READ",
      [
        "storage",
        "002b3271",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f0de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md#insn-009f0de0) · [`009f0e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md#insn-009f0e38) · [`009f0e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md#insn-009f0e44)
- 新版 [`009f1d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f1/009f1d34.md#insn-009f1d8c) · [`009f1de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f1/009f1d34.md#insn-009f1de4) · [`009f1df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f1/009f1d34.md#insn-009f1df0)

~~~diff
- 009f0de0 ["INT_ADD", "register:40f0:8", ["const:9f0de0:8", "const:4:8"]]
- 009f0de0 ["CALL", null, ["callee:009f4f34:8"]]
+ 009f1d8c ["INT_ADD", "register:40f0:8", ["const:9f1d8c:8", "const:4:8"]]
+ 009f1d8c ["CALL", null, ["callee:009f4f34:8"]]
- 009f0de0 bytes 6a0c0094
+ 009f1d8c bytes 6a0c0094
- 009f0e38 ["INT_ADD", "register:40f0:8", ["const:9f0e38:8", "const:4:8"]]
- 009f0e38 ["CALL", null, ["callee:00c58f30:8"]]
+ 009f1de4 ["INT_ADD", "register:40f0:8", ["const:9f1de4:8", "const:4:8"]]
+ 009f1de4 ["CALL", null, ["callee:00c58f30:8"]]
- 009f0e38 bytes 4a9c0994
+ 009f1de4 bytes 539c0994
- 009f0e44 ["COPY", "tmp:0:8", ["const:217:8"]]
- 009f0e44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009f0e44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009f0e44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009f1df0 ["COPY", "tmp:0:8", ["const:261:8"]]
+ 009f1df0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009f1df0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009f1df0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009f0e44 bytes 4a5d0891
+ 009f1df0 bytes 4a850991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51acc1fc74f400fedcef0eeb7f14587b"></a>

### [`009f19cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f19cc.md) → [`009f2978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f2978.md) FUN_009f2978

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009f3650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3650.md) [`009f38e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f38e8.md) [`009f3f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3f88.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`009f45fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f45fc.md) [`009f4894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4894.md) [`009f4f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4f34.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.73% / 新版 93.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f2a3c",
      "incomplete_value": true,
      "site": "009f2a4c",
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
                "const:150:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f1a90",
      "incomplete_value": true,
      "site": "009f1aa0",
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
                "const:100:8"
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
      "definition_site": "009f2a40",
      "incomplete_value": true,
      "site": "009f2a5c",
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
                "const:261:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f1a94",
      "incomplete_value": true,
      "site": "009f1ab0",
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
                "const:217:8"
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
      "definition_site": "009f2a40",
      "incomplete_value": true,
      "site": "009f2a5c",
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
      "definition_site": "009f1a94",
      "incomplete_value": true,
      "site": "009f1ab0",
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
      "009f2a3c",
      "READ",
      [
        "storage",
        "002c2100",
        null,
        null
      ]
    ],
    [
      "009f2a40",
      "READ",
      [
        "storage",
        "002b3217",
        null,
        "string"
      ]
    ],
    [
      "009f2a40",
      "READ",
      [
        "storage",
        "002b3227",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009f2a3c",
      "READ",
      [
        "storage",
        "002c2150",
        null,
        null
      ]
    ],
    [
      "009f2a40",
      "READ",
      [
        "storage",
        "002b3261",
        null,
        "string"
      ]
    ],
    [
      "009f2a40",
      "READ",
      [
        "storage",
        "002b3271",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f1a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f19cc.md#insn-009f1a28) · [`009f1a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f19cc.md#insn-009f1a80) · [`009f1a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f19cc.md#insn-009f1a8c)
- 新版 [`009f29d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f2978.md#insn-009f29d4) · [`009f2a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f2978.md#insn-009f2a2c) · [`009f2a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f2978.md#insn-009f2a38)

~~~diff
- 009f1a28 ["INT_ADD", "register:40f0:8", ["const:9f1a28:8", "const:4:8"]]
- 009f1a28 ["CALL", null, ["callee:009f4f34:8"]]
+ 009f29d4 ["INT_ADD", "register:40f0:8", ["const:9f29d4:8", "const:4:8"]]
+ 009f29d4 ["CALL", null, ["callee:009f4f34:8"]]
- 009f1a28 bytes 58090094
+ 009f29d4 bytes 58090094
- 009f1a80 ["INT_ADD", "register:40f0:8", ["const:9f1a80:8", "const:4:8"]]
- 009f1a80 ["CALL", null, ["callee:00c58f30:8"]]
+ 009f2a2c ["INT_ADD", "register:40f0:8", ["const:9f2a2c:8", "const:4:8"]]
+ 009f2a2c ["CALL", null, ["callee:00c58f30:8"]]
- 009f1a80 bytes 38990994
+ 009f2a2c bytes 41990994
- 009f1a8c ["COPY", "tmp:0:8", ["const:217:8"]]
- 009f1a8c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009f1a8c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009f1a8c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009f2a38 ["COPY", "tmp:0:8", ["const:261:8"]]
+ 009f2a38 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009f2a38 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009f2a38 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009f1a8c bytes 4a5d0891
+ 009f2a38 bytes 4a850991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fb0ecea7da5300e5aeddb0fdde36495"></a>

### [`009f1ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md) → [`009f2e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f2e4c.md) FUN_009f2e4c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009f3650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3650.md) [`009f37b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f37b8.md) [`009f3850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3850.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`009f45fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f45fc.md) [`009f4764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4764.md) [`009f47fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f47fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.99% / 新版 96.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f2f14",
      "incomplete_value": true,
      "site": "009f2f24",
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
                "const:150:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f1f68",
      "incomplete_value": true,
      "site": "009f1f78",
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
                "const:100:8"
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
      "definition_site": "009f2f18",
      "incomplete_value": true,
      "site": "009f2f34",
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
                "const:261:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f1f6c",
      "incomplete_value": true,
      "site": "009f1f88",
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
                "const:217:8"
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
      "definition_site": "009f2f18",
      "incomplete_value": true,
      "site": "009f2f34",
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
      "definition_site": "009f1f6c",
      "incomplete_value": true,
      "site": "009f1f88",
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
      "009f2f14",
      "READ",
      [
        "storage",
        "002c2100",
        null,
        null
      ]
    ],
    [
      "009f2f18",
      "READ",
      [
        "storage",
        "002b3217",
        null,
        "string"
      ]
    ],
    [
      "009f2f18",
      "READ",
      [
        "storage",
        "002b3227",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009f2f14",
      "READ",
      [
        "storage",
        "002c2150",
        null,
        null
      ]
    ],
    [
      "009f2f18",
      "READ",
      [
        "storage",
        "002b3261",
        null,
        "string"
      ]
    ],
    [
      "009f2f18",
      "READ",
      [
        "storage",
        "002b3271",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f1f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md#insn-009f1f00) · [`009f1f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md#insn-009f1f58) · [`009f1f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md#insn-009f1f64)
- 新版 [`009f2eac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f2e4c.md#insn-009f2eac) · [`009f2f04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f2e4c.md#insn-009f2f04) · [`009f2f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f2e4c.md#insn-009f2f10)

~~~diff
- 009f1f00 ["INT_ADD", "register:40f0:8", ["const:9f1f00:8", "const:4:8"]]
- 009f1f00 ["CALL", null, ["callee:009f4f34:8"]]
+ 009f2eac ["INT_ADD", "register:40f0:8", ["const:9f2eac:8", "const:4:8"]]
+ 009f2eac ["CALL", null, ["callee:009f4f34:8"]]
- 009f1f00 bytes 22080094
+ 009f2eac bytes 22080094
- 009f1f58 ["INT_ADD", "register:40f0:8", ["const:9f1f58:8", "const:4:8"]]
- 009f1f58 ["CALL", null, ["callee:00c58f30:8"]]
+ 009f2f04 ["INT_ADD", "register:40f0:8", ["const:9f2f04:8", "const:4:8"]]
+ 009f2f04 ["CALL", null, ["callee:00c58f30:8"]]
- 009f1f58 bytes 02980994
+ 009f2f04 bytes 0b980994
- 009f1f64 ["COPY", "tmp:0:8", ["const:217:8"]]
- 009f1f64 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009f1f64 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009f1f64 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009f2f10 ["COPY", "tmp:0:8", ["const:261:8"]]
+ 009f2f10 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009f2f10 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009f2f10 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009f1f64 bytes 4a5d0891
+ 009f2f10 bytes 4a850991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32032aa11f5f4003a5c7b38c078b5137"></a>

### [`009f2658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2658.md) → [`009f3604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3604.md) FUN_009f3604

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009e0228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e0228.md) · 呼出先 2件 [`009ef6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef6c0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`009e11d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e11d4.md) · 呼出先 2件 [`009f066c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f066c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f362c",
      "incomplete_value": false,
      "site": "009f3638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2680",
      "incomplete_value": false,
      "site": "009f268c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "009f3638",
      "DATA",
      [
        "storage",
        "00c8a500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3638",
      "DATA",
      [
        "storage",
        "00c8b4d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2658.md#insn-009f2674) · [`009f267c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2658.md#insn-009f267c) · [`009f2680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2658.md#insn-009f2680)
- 新版 [`009f3620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3604.md#insn-009f3620) · [`009f3628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3604.md#insn-009f3628) · [`009f362c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3604.md#insn-009f362c)

~~~diff
- 009f2674 ["INT_ADD", "register:40f0:8", ["const:9f2674:8", "const:4:8"]]
- 009f2674 ["CALL", null, ["callee:00c58f30:8"]]
+ 009f3620 ["INT_ADD", "register:40f0:8", ["const:9f3620:8", "const:4:8"]]
+ 009f3620 ["CALL", null, ["callee:00c58f30:8"]]
- 009f2674 bytes 3b960994
+ 009f3620 bytes 44960994
- 009f267c ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f3628 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f267c bytes c8140090
+ 009f3628 bytes c8140090
- 009f2680 ["COPY", "tmp:0:8", ["const:500:8"]]
- 009f2680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f362c ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 009f362c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f362c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f362c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2680 bytes 08011491
+ 009f362c bytes 08411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ac218c6d4142277282e9c33d6e6310e"></a>

### [`009f2700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2700.md) → [`009f36ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f36ac.md) FUN_009f36ac

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f36c8",
      "incomplete_value": false,
      "site": "009f36cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f271c",
      "incomplete_value": false,
      "site": "009f2720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "009f36cc",
      "DATA",
      [
        "storage",
        "00c8a080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f36cc",
      "DATA",
      [
        "storage",
        "00c8b050",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2700.md#insn-009f2718) · [`009f271c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2700.md#insn-009f271c) · [`009f2758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2700.md#insn-009f2758)
- 新版 [`009f36c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f36ac.md#insn-009f36c4) · [`009f36c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f36ac.md#insn-009f36c8) · [`009f3704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f36ac.md#insn-009f3704)

~~~diff
- 009f2718 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f36c4 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f2718 bytes c8140090
+ 009f36c4 bytes c8140090
- 009f271c ["COPY", "tmp:0:8", ["const:80:8"]]
- 009f271c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f271c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f271c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f36c8 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 009f36c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f36c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f36c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f271c bytes 08010291
+ 009f36c8 bytes 08410191
- 009f2758 ["INT_ADD", "register:40f0:8", ["const:9f2758:8", "const:4:8"]]
- 009f2758 ["CALL", null, ["callee:00c54d90:8"]]
+ 009f3704 ["INT_ADD", "register:40f0:8", ["const:9f3704:8", "const:4:8"]]
+ 009f3704 ["CALL", null, ["callee:00c54d90:8"]]
- 009f2758 bytes 92850994
+ 009f3704 bytes a3850994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32a31ed9efa36608f2614ef09611de72"></a>

### [`009f2a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a68.md) → [`009f3a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3a14.md) FUN_009f3a14

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009f2a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a1c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`009f39c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f39c8.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f3a30",
      "incomplete_value": false,
      "site": "009f3a34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2a84",
      "incomplete_value": false,
      "site": "009f2a88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "009f3a34",
      "DATA",
      [
        "storage",
        "00c8a080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3a34",
      "DATA",
      [
        "storage",
        "00c8b050",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a68.md#insn-009f2a80) · [`009f2a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a68.md#insn-009f2a84) · [`009f2ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a68.md#insn-009f2ac0)
- 新版 [`009f3a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3a14.md#insn-009f3a2c) · [`009f3a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3a14.md#insn-009f3a30) · [`009f3a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3a14.md#insn-009f3a6c)

~~~diff
- 009f2a80 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f3a2c ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f2a80 bytes c8140090
+ 009f3a2c bytes c8140090
- 009f2a84 ["COPY", "tmp:0:8", ["const:80:8"]]
- 009f2a84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2a84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2a84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f3a30 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 009f3a30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3a30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3a30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2a84 bytes 08010291
+ 009f3a30 bytes 08410191
- 009f2ac0 ["INT_ADD", "register:40f0:8", ["const:9f2ac0:8", "const:4:8"]]
- 009f2ac0 ["CALL", null, ["callee:00c54d90:8"]]
+ 009f3a6c ["INT_ADD", "register:40f0:8", ["const:9f3a6c:8", "const:4:8"]]
+ 009f3a6c ["CALL", null, ["callee:00c54d90:8"]]
- 009f2ac0 bytes b8840994
+ 009f3a6c bytes c9840994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0885d14770dce68bf7616678ab711112"></a>

### [`009f2e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e38.md) → [`009f3de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3de4.md) FUN_009f3de4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`009edb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edb90.md) [`009ee9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee9c4.md) [`009f2b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2b70.md) [`009f45f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f45f8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 4件 [`009eeb3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009eeb3c.md) [`009ef970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ef/009ef970.md) [`009f3b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3b1c.md) [`009f55a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f55a4.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009f3df0",
      "incomplete_value": false,
      "site": "009f3df4",
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
      "definition_site": "009f2e44",
      "incomplete_value": false,
      "site": "009f2e48",
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
      "009f3df0",
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
      "009f3df0",
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

- 旧版 [`009f2e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e38.md#insn-009f2e48) · [`009f2e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e38.md#insn-009f2e40) · [`009f2e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e38.md#insn-009f2e44)
- 新版 [`009f3df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3de4.md#insn-009f3df4) · [`009f3dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3de4.md#insn-009f3dec) · [`009f3df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3de4.md#insn-009f3df0)

~~~diff
- 009f2e48 ["INT_ADD", "register:40f0:8", ["const:9f2e48:8", "const:4:8"]]
- 009f2e48 ["CALL", null, ["callee:0043bad8:8"]]
+ 009f3df4 ["INT_ADD", "register:40f0:8", ["const:9f3df4:8", "const:4:8"]]
+ 009f3df4 ["CALL", null, ["callee:0043bad8:8"]]
- 009f2e48 bytes 5c22e997
+ 009f3df4 bytes 391fe997
- 009f2e40 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009f3dec ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009f2e40 bytes 20c6ffb0
+ 009f3dec bytes 20c6ffb0
- 009f2e44 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009f2e44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f2e44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f2e44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f3df0 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009f3df0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3df0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3df0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f2e44 bytes 00303e91
+ 009f3df0 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72907b3566a0a014f79fe9f711ac28a0"></a>

### [`009f2e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e4c.md) → [`009f3df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3df8.md) FUN_009f3df8

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
      "definition_site": "009f3dfc",
      "incomplete_value": false,
      "site": "009f3e00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2e50",
      "incomplete_value": false,
      "site": "009f2e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e0:8"
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
      "009f3e00",
      "DATA",
      [
        "storage",
        "00c8a0e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3e00",
      "DATA",
      [
        "storage",
        "00c8b0b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e4c.md#insn-009f2e4c) · [`009f2e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e4c.md#insn-009f2e50)
- 新版 [`009f3df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3df8.md#insn-009f3df8) · [`009f3dfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3df8.md#insn-009f3dfc)

~~~diff
- 009f2e4c ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f3df8 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f2e4c bytes c8140090
+ 009f3df8 bytes c8140090
- 009f2e50 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 009f2e50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2e50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2e50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f3dfc ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 009f3dfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3dfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3dfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2e50 bytes 08810391
+ 009f3dfc bytes 08c10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5933f59a803e6cec65e9b62bdd6f4c4"></a>

### [`009f2e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e5c.md) → [`009f3e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3e08.md) FUN_009f3e08

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
      "definition_site": "009f3e18",
      "incomplete_value": false,
      "site": "009f3e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2e6c",
      "incomplete_value": false,
      "site": "009f2e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e0:8"
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
      "009f3e20",
      "DATA",
      [
        "storage",
        "00c8a0e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3e20",
      "DATA",
      [
        "storage",
        "00c8b0b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e5c.md#insn-009f2e68) · [`009f2e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e5c.md#insn-009f2e6c) · [`009f2e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e5c.md#insn-009f2e78)
- 新版 [`009f3e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3e08.md#insn-009f3e14) · [`009f3e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3e08.md#insn-009f3e18) · [`009f3e24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3e08.md#insn-009f3e24)

~~~diff
- 009f2e68 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f3e14 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f2e68 bytes c8140090
+ 009f3e14 bytes c8140090
- 009f2e6c ["COPY", "tmp:0:8", ["const:e0:8"]]
- 009f2e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f3e18 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 009f3e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2e6c bytes 08810391
+ 009f3e18 bytes 08c10291
- 009f2e78 ["INT_ADD", "register:40f0:8", ["const:9f2e78:8", "const:4:8"]]
- 009f2e78 ["CALL", null, ["callee:00c58f40:8"]]
+ 009f3e24 ["INT_ADD", "register:40f0:8", ["const:9f3e24:8", "const:4:8"]]
+ 009f3e24 ["CALL", null, ["callee:00c58f40:8"]]
- 009f2e78 bytes 3e940994
+ 009f3e24 bytes 47940994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04dd94d4553eef6c2eb20000a2270dd3"></a>

### [`009f2ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2ff8.md) → [`009f3fa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3fa4.md) FUN_009f3fa4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009f2eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2eb8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`009f3e64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3e64.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009f3fb0",
      "incomplete_value": false,
      "site": "009f3fb4",
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
      "definition_site": "009f3004",
      "incomplete_value": false,
      "site": "009f3008",
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
      "009f3fb0",
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
      "009f3fb0",
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

- 旧版 [`009f3008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2ff8.md#insn-009f3008) · [`009f3000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2ff8.md#insn-009f3000) · [`009f3004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2ff8.md#insn-009f3004)
- 新版 [`009f3fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3fa4.md#insn-009f3fb4) · [`009f3fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3fa4.md#insn-009f3fac) · [`009f3fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3fa4.md#insn-009f3fb0)

~~~diff
- 009f3008 ["INT_ADD", "register:40f0:8", ["const:9f3008:8", "const:4:8"]]
- 009f3008 ["CALL", null, ["callee:0043bad8:8"]]
+ 009f3fb4 ["INT_ADD", "register:40f0:8", ["const:9f3fb4:8", "const:4:8"]]
+ 009f3fb4 ["CALL", null, ["callee:0043bad8:8"]]
- 009f3008 bytes ec21e997
+ 009f3fb4 bytes c91ee997
- 009f3000 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009f3fac ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009f3000 bytes 20c6ff90
+ 009f3fac bytes 20c6ffb0
- 009f3004 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009f3004 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f3004 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f3004 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f3fb0 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009f3fb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3fb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3fb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f3004 bytes 00303e91
+ 009f3fb0 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb89bba6635b29c864bdb0ab5c3c29f0"></a>

### [`009f30dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f30dc.md) → [`009f4088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4088.md) FUN_009f4088

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
      "definition_site": "009f408c",
      "incomplete_value": false,
      "site": "009f4090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f30e0",
      "incomplete_value": false,
      "site": "009f30e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
      "009f4090",
      "DATA",
      [
        "storage",
        "00c8a290",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f4090",
      "DATA",
      [
        "storage",
        "00c8b260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f30dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f30dc.md#insn-009f30dc) · [`009f30e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f30dc.md#insn-009f30e0)
- 新版 [`009f4088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4088.md#insn-009f4088) · [`009f408c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4088.md#insn-009f408c)

~~~diff
- 009f30dc ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f4088 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f30dc bytes a81400f0
+ 009f4088 bytes a81400f0
- 009f30e0 ["COPY", "tmp:0:8", ["const:290:8"]]
- 009f30e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f30e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f30e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f408c ["COPY", "tmp:0:8", ["const:260:8"]]
+ 009f408c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f408c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f408c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f30e0 bytes 08410a91
+ 009f408c bytes 08810991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61050d99f7cd362a65c2c6c7d3896bfc"></a>

### [`009f30ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f30ec.md) → [`009f4098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4098.md) FUN_009f4098

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
      "definition_site": "009f40a8",
      "incomplete_value": false,
      "site": "009f40b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f30fc",
      "incomplete_value": false,
      "site": "009f3104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "009f40b0",
      "DATA",
      [
        "storage",
        "00c8a290",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f40b0",
      "DATA",
      [
        "storage",
        "00c8b260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f30f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f30ec.md#insn-009f30f8) · [`009f30fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f30ec.md#insn-009f30fc) · [`009f3108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f30ec.md#insn-009f3108)
- 新版 [`009f40a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4098.md#insn-009f40a4) · [`009f40a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4098.md#insn-009f40a8) · [`009f40b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4098.md#insn-009f40b4)

~~~diff
- 009f30f8 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f40a4 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f30f8 bytes a81400f0
+ 009f40a4 bytes a81400f0
- 009f30fc ["COPY", "tmp:0:8", ["const:290:8"]]
- 009f30fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f30fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f30fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f40a8 ["COPY", "tmp:0:8", ["const:260:8"]]
+ 009f40a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f40a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f40a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f30fc bytes 08410a91
+ 009f40a8 bytes 08810991
- 009f3108 ["INT_ADD", "register:40f0:8", ["const:9f3108:8", "const:4:8"]]
- 009f3108 ["CALL", null, ["callee:00c58f40:8"]]
+ 009f40b4 ["INT_ADD", "register:40f0:8", ["const:9f40b4:8", "const:4:8"]]
+ 009f40b4 ["CALL", null, ["callee:00c58f40:8"]]
- 009f3108 bytes 9a930994
+ 009f40b4 bytes a3930994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2afd87c903f68b3fd4be749df43a6d6d"></a>

### [`009f3148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3148.md) → [`009f40f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f40f4.md) FUN_009f40f4

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
      "definition_site": "009f40f8",
      "incomplete_value": false,
      "site": "009f40fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f314c",
      "incomplete_value": false,
      "site": "009f3150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "009f40fc",
      "DATA",
      [
        "storage",
        "00c8a348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f40fc",
      "DATA",
      [
        "storage",
        "00c8b318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3148.md#insn-009f3148) · [`009f314c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3148.md#insn-009f314c)
- 新版 [`009f40f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f40f4.md#insn-009f40f4) · [`009f40f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f40f4.md#insn-009f40f8)

~~~diff
- 009f3148 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f40f4 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f3148 bytes a81400f0
+ 009f40f4 bytes a81400f0
- 009f314c ["COPY", "tmp:0:8", ["const:348:8"]]
- 009f314c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f314c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f314c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f40f8 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 009f40f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f40f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f40f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f314c bytes 08210d91
+ 009f40f8 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f42ec4bf23e810b11edb7ba28c5385f"></a>

### [`009f3158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3158.md) → [`009f4104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4104.md) FUN_009f4104

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
      "definition_site": "009f4114",
      "incomplete_value": false,
      "site": "009f411c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3168",
      "incomplete_value": false,
      "site": "009f3170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "009f411c",
      "DATA",
      [
        "storage",
        "00c8a348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f411c",
      "DATA",
      [
        "storage",
        "00c8b318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3158.md#insn-009f3164) · [`009f3168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3158.md#insn-009f3168) · [`009f3174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3158.md#insn-009f3174)
- 新版 [`009f4110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4104.md#insn-009f4110) · [`009f4114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4104.md#insn-009f4114) · [`009f4120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4104.md#insn-009f4120)

~~~diff
- 009f3164 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f4110 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f3164 bytes a81400f0
+ 009f4110 bytes a81400f0
- 009f3168 ["COPY", "tmp:0:8", ["const:348:8"]]
- 009f3168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f3168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f3168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f4114 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 009f4114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f3168 bytes 08210d91
+ 009f4114 bytes 08610c91
- 009f3174 ["INT_ADD", "register:40f0:8", ["const:9f3174:8", "const:4:8"]]
- 009f3174 ["CALL", null, ["callee:00c58f40:8"]]
+ 009f4120 ["INT_ADD", "register:40f0:8", ["const:9f4120:8", "const:4:8"]]
+ 009f4120 ["CALL", null, ["callee:00c58f40:8"]]
- 009f3174 bytes 7f930994
+ 009f4120 bytes 88930994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebdf6343372d15fc7d3f11598011ba90"></a>

### [`009f31b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f31b8.md) → [`009f4164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4164.md) FUN_009f4164

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009ec2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec2a4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`009ed250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ed/009ed250.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f41f0",
      "incomplete_value": false,
      "site": "009f4258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3244",
      "incomplete_value": false,
      "site": "009f32ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "009f4258",
      "DATA",
      [
        "storage",
        "00c8a080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f4258",
      "DATA",
      [
        "storage",
        "00c8b050",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f322c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f31b8.md#insn-009f322c) · [`009f3240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f31b8.md#insn-009f3240) · [`009f3244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f31b8.md#insn-009f3244)
- 新版 [`009f41d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4164.md#insn-009f41d8) · [`009f41ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4164.md#insn-009f41ec) · [`009f41f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4164.md#insn-009f41f0)

~~~diff
- 009f322c ["INT_ADD", "register:40f0:8", ["const:9f322c:8", "const:4:8"]]
- 009f322c ["CALL", null, ["callee:00c58f30:8"]]
+ 009f41d8 ["INT_ADD", "register:40f0:8", ["const:9f41d8:8", "const:4:8"]]
+ 009f41d8 ["CALL", null, ["callee:00c58f30:8"]]
- 009f322c bytes 4d930994
+ 009f41d8 bytes 56930994
- 009f3240 ["COPY", "register:4048:8", ["const:c8a000:8"]]
+ 009f41ec ["COPY", "register:4048:8", ["const:c8b000:8"]]
- 009f3240 bytes a91400f0
+ 009f41ec bytes a91400f0
- 009f3244 ["COPY", "tmp:0:8", ["const:80:8"]]
- 009f3244 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009f3244 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009f3244 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009f41f0 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 009f41f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009f41f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009f41f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009f3244 bytes 29010291
+ 009f41f0 bytes 29410191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1fb2bb01581fd2791489ebd6b2a8f94"></a>

### [`009f32f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f32f8.md) → [`009f42a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f42a4.md) FUN_009f42a4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ec9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec9b0.md) · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 1件 [`009ed95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ed/009ed95c.md) · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.23% / 新版 91.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f42c0",
      "incomplete_value": false,
      "site": "009f42c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3314",
      "incomplete_value": false,
      "site": "009f3314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f42cc",
      "incomplete_value": false,
      "site": "009f42cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3320",
      "incomplete_value": false,
      "site": "009f3320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "009f42c0",
      "DATA",
      [
        "storage",
        "00c8a400",
        null,
        "undefined *"
      ]
    ],
    [
      "009f42cc",
      "DATA",
      [
        "storage",
        "00c8a450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f42c0",
      "DATA",
      [
        "storage",
        "00c8b3d0",
        null,
        "undefined *"
      ]
    ],
    [
      "009f42cc",
      "DATA",
      [
        "storage",
        "00c8b420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f32f8.md#insn-009f3308) · [`009f330c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f32f8.md#insn-009f330c) · [`009f3318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f32f8.md#insn-009f3318)
- 新版 [`009f42b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f42a4.md#insn-009f42b4) · [`009f42b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f42a4.md#insn-009f42b8)

~~~diff
- 009f3308 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f42b4 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f3308 bytes a81400f0
+ 009f42b4 bytes a81400f0
- 009f330c ["COPY", "tmp:0:8", ["const:400:8"]]
- 009f330c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f330c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f330c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f42b8 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 009f42b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f42b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f42b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f330c bytes 08011091
+ 009f42b8 bytes 08410f91
- 009f3318 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f3318 bytes a81400f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c611c68c1ffc9609edb99aeaf3e339c3"></a>

### [`009f33f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f33f8.md) → [`009f43a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f43a4.md) FUN_009f43a4

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
      "definition_site": "009f43a8",
      "incomplete_value": false,
      "site": "009f43ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f33fc",
      "incomplete_value": false,
      "site": "009f3400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "009f43ac",
      "DATA",
      [
        "storage",
        "00c8a400",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f43ac",
      "DATA",
      [
        "storage",
        "00c8b3d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f33f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f33f8.md#insn-009f33f8) · [`009f33fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f33f8.md#insn-009f33fc)
- 新版 [`009f43a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f43a4.md#insn-009f43a4) · [`009f43a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f43a4.md#insn-009f43a8)

~~~diff
- 009f33f8 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f43a4 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f33f8 bytes a81400f0
+ 009f43a4 bytes a81400f0
- 009f33fc ["COPY", "tmp:0:8", ["const:400:8"]]
- 009f33fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f33fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f33fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f43a8 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 009f43a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f43a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f43a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f33fc bytes 08011091
+ 009f43a8 bytes 08410f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b76a416f6c471b898a1d5edc2e32869"></a>

### [`009f3408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3408.md) → [`009f43b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f43b4.md) FUN_009f43b4

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
      "definition_site": "009f43c4",
      "incomplete_value": false,
      "site": "009f43cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3418",
      "incomplete_value": false,
      "site": "009f3420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "009f43cc",
      "DATA",
      [
        "storage",
        "00c8a400",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f43cc",
      "DATA",
      [
        "storage",
        "00c8b3d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3408.md#insn-009f3414) · [`009f3418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3408.md#insn-009f3418) · [`009f3424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3408.md#insn-009f3424)
- 新版 [`009f43c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f43b4.md#insn-009f43c0) · [`009f43c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f43b4.md#insn-009f43c4) · [`009f43d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f43b4.md#insn-009f43d0)

~~~diff
- 009f3414 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f43c0 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f3414 bytes a81400f0
+ 009f43c0 bytes a81400f0
- 009f3418 ["COPY", "tmp:0:8", ["const:400:8"]]
- 009f3418 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f3418 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f3418 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f43c4 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 009f43c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f43c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f43c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f3418 bytes 08011091
+ 009f43c4 bytes 08410f91
- 009f3424 ["INT_ADD", "register:40f0:8", ["const:9f3424:8", "const:4:8"]]
- 009f3424 ["CALL", null, ["callee:00c58f40:8"]]
+ 009f43d0 ["INT_ADD", "register:40f0:8", ["const:9f43d0:8", "const:4:8"]]
+ 009f43d0 ["CALL", null, ["callee:00c58f40:8"]]
- 009f3424 bytes d3920994
+ 009f43d0 bytes dc920994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-105d0eedc571392c3553eeb140bd522a"></a>

### [`009f3448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3448.md) → [`009f43f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f43f4.md) FUN_009f43f4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

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
      "definition_site": "009f4408",
      "incomplete_value": false,
      "site": "009f440c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f345c",
      "incomplete_value": false,
      "site": "009f3460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
      "009f440c",
      "DATA",
      [
        "storage",
        "00c8a450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f440c",
      "DATA",
      [
        "storage",
        "00c8b420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3448.md#insn-009f3458) · [`009f345c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3448.md#insn-009f345c) · [`009f3470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3448.md#insn-009f3470)
- 新版 [`009f4404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f43f4.md#insn-009f4404) · [`009f4408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f43f4.md#insn-009f4408) · [`009f441c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f43f4.md#insn-009f441c)

~~~diff
- 009f3458 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f4404 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f3458 bytes a81400f0
+ 009f4404 bytes a81400f0
- 009f345c ["COPY", "tmp:0:8", ["const:450:8"]]
- 009f345c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f345c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f345c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f4408 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 009f4408 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4408 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f345c bytes 08411191
+ 009f4408 bytes 08811091
- 009f3470 ["INT_ADD", "register:40f0:8", ["const:9f3470:8", "const:4:8"]]
- 009f3470 ["CALL", null, ["callee:00c54d90:8"]]
+ 009f441c ["INT_ADD", "register:40f0:8", ["const:9f441c:8", "const:4:8"]]
+ 009f441c ["CALL", null, ["callee:00c54d90:8"]]
- 009f3470 bytes 4c820994
+ 009f441c bytes 5d820994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aa6ad5963d1bf3656988c0657c74dc2"></a>

### [`009f34a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f34a4.md) → [`009f4450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4450.md) FUN_009f4450

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
      "definition_site": "009f4468",
      "incomplete_value": false,
      "site": "009f446c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f34bc",
      "incomplete_value": false,
      "site": "009f34c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "009f446c",
      "DATA",
      [
        "storage",
        "00c8a450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f446c",
      "DATA",
      [
        "storage",
        "00c8b420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f34b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f34a4.md#insn-009f34b8) · [`009f34bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f34a4.md#insn-009f34bc) · [`009f34d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f34a4.md#insn-009f34d0)
- 新版 [`009f4464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4450.md#insn-009f4464) · [`009f4468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4450.md#insn-009f4468) · [`009f447c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4450.md#insn-009f447c)

~~~diff
- 009f34b8 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f4464 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f34b8 bytes a81400f0
+ 009f4464 bytes a81400f0
- 009f34bc ["COPY", "tmp:0:8", ["const:450:8"]]
- 009f34bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f34bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f34bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f4468 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 009f4468 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4468 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4468 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f34bc bytes 08411191
+ 009f4468 bytes 08811091
- 009f34d0 ["INT_ADD", "register:40f0:8", ["const:9f34d0:8", "const:4:8"]]
- 009f34d0 ["CALL", null, ["callee:00c54d90:8"]]
+ 009f447c ["INT_ADD", "register:40f0:8", ["const:9f447c:8", "const:4:8"]]
+ 009f447c ["CALL", null, ["callee:00c54d90:8"]]
- 009f34d0 bytes 34820994
+ 009f447c bytes 45820994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5846295f1a780c62638c1e34ea4fd098"></a>

### [`009f3650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3650.md) → [`009f45fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f45fc.md) FUN_009f45fc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009ed16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed16c.md) [`009f19cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f19cc.md) [`009f1ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`009ee118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ee/009ee118.md) [`009f2978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f2978.md) [`009f2e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f2e4c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009f4608",
      "incomplete_value": false,
      "site": "009f460c",
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
      "definition_site": "009f365c",
      "incomplete_value": false,
      "site": "009f3660",
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
      "009f4608",
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
      "009f4608",
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

- 旧版 [`009f3660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3650.md#insn-009f3660) · [`009f3658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3650.md#insn-009f3658) · [`009f365c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3650.md#insn-009f365c)
- 新版 [`009f460c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f45fc.md#insn-009f460c) · [`009f4604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f45fc.md#insn-009f4604) · [`009f4608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f45fc.md#insn-009f4608)

~~~diff
- 009f3660 ["INT_ADD", "register:40f0:8", ["const:9f3660:8", "const:4:8"]]
- 009f3660 ["CALL", null, ["callee:0043bad8:8"]]
+ 009f460c ["INT_ADD", "register:40f0:8", ["const:9f460c:8", "const:4:8"]]
+ 009f460c ["CALL", null, ["callee:0043bad8:8"]]
- 009f3660 bytes 5620e997
+ 009f460c bytes 331de997
- 009f3658 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009f4604 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009f3658 bytes 20c6ff90
+ 009f4604 bytes 20c6ff90
- 009f365c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009f365c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f365c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f365c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f4608 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009f4608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f365c bytes 00303e91
+ 009f4608 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34b72beccfb5241fbf433f99fe3cfd59"></a>

### [`009f3ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3ac8.md) → [`009f4a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4a74.md) FUN_009f4a74

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
      "definition_site": "009f4a78",
      "incomplete_value": false,
      "site": "009f4a7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3acc",
      "incomplete_value": false,
      "site": "009f3ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "009f4a7c",
      "DATA",
      [
        "storage",
        "00c8a480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f4a7c",
      "DATA",
      [
        "storage",
        "00c8b450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3ac8.md#insn-009f3ac8) · [`009f3acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3ac8.md#insn-009f3acc)
- 新版 [`009f4a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4a74.md#insn-009f4a74) · [`009f4a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4a74.md#insn-009f4a78)

~~~diff
- 009f3ac8 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f4a74 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f3ac8 bytes a81400f0
+ 009f4a74 bytes a81400f0
- 009f3acc ["COPY", "tmp:0:8", ["const:480:8"]]
- 009f3acc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f3acc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f3acc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f4a78 ["COPY", "tmp:0:8", ["const:450:8"]]
+ 009f4a78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4a78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4a78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f3acc bytes 08011291
+ 009f4a78 bytes 08411191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccaabe604ee3094c505ab09f8fc893d7"></a>

### [`009f3b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b0c.md) → [`009f4ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4ab8.md) FUN_009f4ab8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`009efe3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md) [`009f0560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md) [`009f1254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1254.md) [`009f3cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cc0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 4件 [`009f0de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f0/009f0de8.md) [`009f150c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f1/009f150c.md) [`009f2200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f2200.md) [`009f4c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4c6c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009f4ac4",
      "incomplete_value": false,
      "site": "009f4ac8",
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
      "definition_site": "009f3b18",
      "incomplete_value": false,
      "site": "009f3b1c",
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
      "009f4ac4",
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
      "009f4ac4",
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

- 旧版 [`009f3b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b0c.md#insn-009f3b1c) · [`009f3b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b0c.md#insn-009f3b14) · [`009f3b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b0c.md#insn-009f3b18)
- 新版 [`009f4ac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4ab8.md#insn-009f4ac8) · [`009f4ac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4ab8.md#insn-009f4ac0) · [`009f4ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4ab8.md#insn-009f4ac4)

~~~diff
- 009f3b1c ["INT_ADD", "register:40f0:8", ["const:9f3b1c:8", "const:4:8"]]
- 009f3b1c ["CALL", null, ["callee:0043bad8:8"]]
+ 009f4ac8 ["INT_ADD", "register:40f0:8", ["const:9f4ac8:8", "const:4:8"]]
+ 009f4ac8 ["CALL", null, ["callee:0043bad8:8"]]
- 009f3b1c bytes 271fe997
+ 009f4ac8 bytes 041ce997
- 009f3b14 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009f4ac0 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009f3b14 bytes 20c6ff90
+ 009f4ac0 bytes 20c6ff90
- 009f3b18 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009f3b18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f3b18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f3b18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f4ac4 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009f4ac4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4ac4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4ac4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f3b18 bytes 00303e91
+ 009f4ac4 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9038a5a5a5b9e600511f93ccf8135ff8"></a>

### [`009f3cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cac.md) → [`009f4c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4c58.md) FUN_009f4c58

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009f3b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b20.md) [`009f49a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f49a4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`009f4acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4acc.md) [`009f5950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5950.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009f4c64",
      "incomplete_value": false,
      "site": "009f4c68",
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
      "definition_site": "009f3cb8",
      "incomplete_value": false,
      "site": "009f3cbc",
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
      "009f4c64",
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
      "009f4c64",
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

- 旧版 [`009f3cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cac.md#insn-009f3cbc) · [`009f3cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cac.md#insn-009f3cb4) · [`009f3cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cac.md#insn-009f3cb8)
- 新版 [`009f4c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4c58.md#insn-009f4c68) · [`009f4c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4c58.md#insn-009f4c60) · [`009f4c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f4/009f4c58.md#insn-009f4c64)

~~~diff
- 009f3cbc ["INT_ADD", "register:40f0:8", ["const:9f3cbc:8", "const:4:8"]]
- 009f3cbc ["CALL", null, ["callee:0043bad8:8"]]
+ 009f4c68 ["INT_ADD", "register:40f0:8", ["const:9f4c68:8", "const:4:8"]]
+ 009f4c68 ["CALL", null, ["callee:0043bad8:8"]]
- 009f3cbc bytes bf1ee997
+ 009f4c68 bytes 9c1be997
- 009f3cb4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009f4c60 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009f3cb4 bytes 20c6ff90
+ 009f4c60 bytes 20c6ff90
- 009f3cb8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009f3cb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f3cb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f3cb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f4c64 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009f4c64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4c64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4c64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f3cb8 bytes 00303e91
+ 009f4c64 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74d171d56d12bb71ce31a29aabca4999"></a>

### [`009f4b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b30.md) → [`009f5adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5adc.md) FUN_009f5adc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009f1610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1610.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`009f25bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f25bc.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009f5ae8",
      "incomplete_value": false,
      "site": "009f5aec",
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
      "definition_site": "009f4b3c",
      "incomplete_value": false,
      "site": "009f4b40",
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
      "009f5ae8",
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
      "009f5ae8",
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

- 旧版 [`009f4b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b30.md#insn-009f4b40) · [`009f4b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b30.md#insn-009f4b38) · [`009f4b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b30.md#insn-009f4b3c)
- 新版 [`009f5aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5adc.md#insn-009f5aec) · [`009f5ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5adc.md#insn-009f5ae4) · [`009f5ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5adc.md#insn-009f5ae8)

~~~diff
- 009f4b40 ["INT_ADD", "register:40f0:8", ["const:9f4b40:8", "const:4:8"]]
- 009f4b40 ["CALL", null, ["callee:0043bad8:8"]]
+ 009f5aec ["INT_ADD", "register:40f0:8", ["const:9f5aec:8", "const:4:8"]]
+ 009f5aec ["CALL", null, ["callee:0043bad8:8"]]
- 009f4b40 bytes 1e1be997
+ 009f5aec bytes fb17e997
- 009f4b38 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009f5ae4 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009f4b38 bytes 00c6fff0
+ 009f5ae4 bytes 00c6fff0
- 009f4b3c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009f4b3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f4b3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f4b3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f5ae8 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009f5ae8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f5ae8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f5ae8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f4b3c bytes 00303e91
+ 009f5ae8 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d5d03695a2839c9f6231f7b48c97bb4"></a>

### [`009f4b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b44.md) → [`009f5af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5af0.md) FUN_009f5af0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009f1754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1754.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`009f2700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f2/009f2700.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009f5afc",
      "incomplete_value": false,
      "site": "009f5b00",
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
      "definition_site": "009f4b50",
      "incomplete_value": false,
      "site": "009f4b54",
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
      "009f5afc",
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
      "009f5afc",
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

- 旧版 [`009f4b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b44.md#insn-009f4b54) · [`009f4b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b44.md#insn-009f4b4c) · [`009f4b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b44.md#insn-009f4b50)
- 新版 [`009f5b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5af0.md#insn-009f5b00) · [`009f5af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5af0.md#insn-009f5af8) · [`009f5afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5af0.md#insn-009f5afc)

~~~diff
- 009f4b54 ["INT_ADD", "register:40f0:8", ["const:9f4b54:8", "const:4:8"]]
- 009f4b54 ["CALL", null, ["callee:0043bad8:8"]]
+ 009f5b00 ["INT_ADD", "register:40f0:8", ["const:9f5b00:8", "const:4:8"]]
+ 009f5b00 ["CALL", null, ["callee:0043bad8:8"]]
- 009f4b54 bytes 191be997
+ 009f5b00 bytes f617e997
- 009f4b4c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009f5af8 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009f4b4c bytes 00c6fff0
+ 009f5af8 bytes 00c6fff0
- 009f4b50 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009f4b50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f4b50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f4b50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f5afc ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009f5afc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f5afc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f5afc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f4b50 bytes 00303e91
+ 009f5afc bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80f531c00937a9b0ee972e93c8727809"></a>

### [`009f4b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b58.md) → [`009f5b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5b04.md) FUN_009f5b04

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
      "definition_site": "009f5b08",
      "incomplete_value": false,
      "site": "009f5b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f4b5c",
      "incomplete_value": false,
      "site": "009f4b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "009f5b0c",
      "DATA",
      [
        "storage",
        "00c8a500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f5b0c",
      "DATA",
      [
        "storage",
        "00c8b4d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f4b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b58.md#insn-009f4b58) · [`009f4b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b58.md#insn-009f4b5c)
- 新版 [`009f5b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5b04.md#insn-009f5b04) · [`009f5b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5b04.md#insn-009f5b08)

~~~diff
- 009f4b58 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f5b04 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f4b58 bytes a81400d0
+ 009f5b04 bytes a81400d0
- 009f4b5c ["COPY", "tmp:0:8", ["const:500:8"]]
- 009f4b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f4b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f4b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f5b08 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 009f5b08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f5b08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f5b08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f4b5c bytes 08011491
+ 009f5b08 bytes 08411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17b7298a5fa2a22d5ea04eb9e01ed716"></a>

### [`009f4b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b68.md) → [`009f5b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5b14.md) FUN_009f5b14

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
      "definition_site": "009f5b24",
      "incomplete_value": false,
      "site": "009f5b2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f4b78",
      "incomplete_value": false,
      "site": "009f4b80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "009f5b2c",
      "DATA",
      [
        "storage",
        "00c8a500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f5b2c",
      "DATA",
      [
        "storage",
        "00c8b4d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f4b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b68.md#insn-009f4b74) · [`009f4b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b68.md#insn-009f4b78) · [`009f4b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b68.md#insn-009f4b84)
- 新版 [`009f5b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5b14.md#insn-009f5b20) · [`009f5b24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5b14.md#insn-009f5b24) · [`009f5b30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5b14.md#insn-009f5b30)

~~~diff
- 009f4b74 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f5b20 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f4b74 bytes a81400d0
+ 009f5b20 bytes a81400d0
- 009f4b78 ["COPY", "tmp:0:8", ["const:500:8"]]
- 009f4b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f4b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f4b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f5b24 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 009f5b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f5b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f5b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f4b78 bytes 08011491
+ 009f5b24 bytes 08411391
- 009f4b84 ["INT_ADD", "register:40f0:8", ["const:9f4b84:8", "const:4:8"]]
- 009f4b84 ["CALL", null, ["callee:00c58f40:8"]]
+ 009f5b30 ["INT_ADD", "register:40f0:8", ["const:9f5b30:8", "const:4:8"]]
+ 009f5b30 ["CALL", null, ["callee:00c58f40:8"]]
- 009f4b84 bytes fb8c0994
+ 009f5b30 bytes 048d0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-573dc88a01769fc2e6e648f0bdb831c9"></a>

### [`009f4ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md) → [`009f5b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5b50.md) FUN_009f5b50

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009f4b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b98.md) · 呼出先 8件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`009f28e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f28e8.md) [`009f2938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2938.md) [`009f2988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2988.md) [`009f29cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f29cc.md)
- 新版 呼出元 1件 [`009f5b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5b44.md) · 呼出先 8件 [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`009f3894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3894.md) [`009f38e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f38e4.md) [`009f3934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3934.md) [`009f3978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f3/009f3978.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f5b6c",
      "incomplete_value": false,
      "site": "009f5b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f4bc0",
      "incomplete_value": false,
      "site": "009f4bc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "009f5b6c",
      "DATA",
      [
        "storage",
        "00c89f28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f5b6c",
      "DATA",
      [
        "storage",
        "00c8aef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f4bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md#insn-009f4bb4) · [`009f4bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md#insn-009f4bb8) · [`009f4bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md#insn-009f4bc4)
- 新版 [`009f5b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5b50.md#insn-009f5b60) · [`009f5b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5b50.md#insn-009f5b64) · [`009f5b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5b50.md#insn-009f5b70)

~~~diff
- 009f4bb4 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f5b60 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f4bb4 bytes a81400b0
+ 009f5b60 bytes a81400b0
- 009f4bb8 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 009f4bb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f4bb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f4bb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f5b64 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 009f5b64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f5b64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f5b64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f4bb8 bytes 08a13c91
+ 009f5b64 bytes 08e13b91
- 009f4bc4 ["INT_ADD", "register:40f0:8", ["const:9f4bc4:8", "const:4:8"]]
- 009f4bc4 ["CALL", null, ["callee:009f4894:8"]]
+ 009f5b70 ["INT_ADD", "register:40f0:8", ["const:9f5b70:8", "const:4:8"]]
+ 009f5b70 ["CALL", null, ["callee:009f4894:8"]]
- 009f4bc4 bytes 49fbff97
+ 009f5b70 bytes 49fbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-719e8ad5d19d3953092d77ce064dd8e5"></a>

### [`009f4c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4c60.md) → [`009f5c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5c0c.md) _INIT_205

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f5c48",
      "incomplete_value": true,
      "site": "009f5c64",
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
      "definition_site": "009f4c9c",
      "incomplete_value": true,
      "site": "009f4cb8",
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
      "definition_site": "009f5cc8",
      "incomplete_value": true,
      "site": "009f5ce4",
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
      "definition_site": "009f4d1c",
      "incomplete_value": true,
      "site": "009f4d38",
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
      "definition_site": "009f5ce8",
      "incomplete_value": true,
      "site": "009f5d04",
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
      "definition_site": "009f4d3c",
      "incomplete_value": true,
      "site": "009f4d58",
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
      "009f5c48",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009f5c6c",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009f5c8c",
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
      "009f5c48",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "009f5c6c",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "009f5c8c",
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

- 旧版 [`009f4e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4c60.md#insn-009f4e94) · [`009f4c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4c60.md#insn-009f4c88) · [`009f4c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4c60.md#insn-009f4c8c)
- 新版 [`009f5e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5c0c.md#insn-009f5e40) · [`009f5c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5c0c.md#insn-009f5c34) · [`009f5c38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5c0c.md#insn-009f5c38)

~~~diff
- 009f4e94 ["INT_ADD", "register:40f0:8", ["const:9f4e94:8", "const:4:8"]]
- 009f4e94 ["CALL", null, ["callee:00c58ed0:8"]]
+ 009f5e40 ["INT_ADD", "register:40f0:8", ["const:9f5e40:8", "const:4:8"]]
+ 009f5e40 ["CALL", null, ["callee:00c58ed0:8"]]
- 009f4e94 bytes 1b8c0994
+ 009f5e40 bytes 248c0994
- 009f4c88 ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 009f5c34 ["COPY", "register:4098:8", ["const:1124000:8"]]
- 009f4c88 bytes 733900f0
+ 009f5c34 bytes 733900f0
- 009f4c8c ["COPY", "tmp:0:8", ["const:e38:8"]]
- 009f4c8c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009f4c8c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009f4c8c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009f5c38 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 009f5c38 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009f5c38 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009f5c38 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009f4c8c bytes 73e23891
+ 009f5c38 bytes 73e23791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42e1cd8516f65e9394b8df72a6b76528"></a>

### [`009f4ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ff8.md) → [`009f5fa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5fa4.md) FUN_009f5fa4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009fb4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fb/009fb4a0.md) · 呼出先 14件 [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`006648e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/006648e0.md) [`006667e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00666/006667e8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`009df918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df918.md)
- 新版 呼出元 1件 [`009fc44c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fc/009fc44c.md) · 呼出先 14件 [`0057c208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c208.md) [`00664c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664c90.md) [`00666b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00666/00666b98.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`009e08c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e08c4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

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
      "site": "009f6288",
      "value": [
        "leaf",
        "ram:664c90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f52dc",
      "value": [
        "leaf",
        "ram:6648e0:8"
      ]
    },
    "ordinal": 30,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f5ffc",
      "DATA",
      [
        "storage",
        "00c8a580",
        null,
        "undefined *"
      ]
    ],
    [
      "009f6004",
      "READ",
      [
        "storage",
        "002c4248",
        null,
        "undefined8"
      ]
    ],
    [
      "009f6288",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648e0"
      ]
    ]
  ],
  "added": [
    [
      "009f5ffc",
      "DATA",
      [
        "storage",
        "00c8b550",
        null,
        "undefined *"
      ]
    ],
    [
      "009f6004",
      "READ",
      [
        "storage",
        "002c4298",
        null,
        "undefined8"
      ]
    ],
    [
      "009f6288",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664c90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f52dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ff8.md#insn-009f52dc) · [`009f503c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ff8.md#insn-009f503c) · [`009f5044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ff8.md#insn-009f5044)
- 新版 [`009f6288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5fa4.md#insn-009f6288) · [`009f5fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5fa4.md#insn-009f5fe8) · [`009f5ff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f5/009f5fa4.md#insn-009f5ff0)

~~~diff
- 009f52dc ["INT_ADD", "register:40f0:8", ["const:9f52dc:8", "const:4:8"]]
- 009f52dc ["CALL", null, ["ram:6648e0:8"]]
+ 009f6288 ["INT_ADD", "register:40f0:8", ["const:9f6288:8", "const:4:8"]]
+ 009f6288 ["CALL", null, ["ram:664c90:8"]]
- 009f52dc bytes 81bdf197
+ 009f6288 bytes 82baf197
- 009f503c ["INT_ADD", "register:40f0:8", ["const:9f503c:8", "const:4:8"]]
- 009f503c ["CALL", null, ["callee:00c58f30:8"]]
+ 009f5fe8 ["INT_ADD", "register:40f0:8", ["const:9f5fe8:8", "const:4:8"]]
+ 009f5fe8 ["CALL", null, ["callee:00c58f30:8"]]
- 009f503c bytes c98b0994
+ 009f5fe8 bytes d28b0994
- 009f5044 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f5ff0 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f5044 bytes a81400b0
+ 009f5ff0 bytes a81400d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-367bf398172e078211e86b216e793cbb"></a>

### [`009f53fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f53fc.md) → [`009f63a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f6/009f63a8.md) FUN_009f63a8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f63c8",
      "incomplete_value": false,
      "site": "009f63cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f541c",
      "incomplete_value": false,
      "site": "009f5420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f6408",
      "incomplete_value": false,
      "site": "009f6410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f545c",
      "incomplete_value": false,
      "site": "009f5464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f63cc",
      "DATA",
      [
        "storage",
        "00c8a580",
        null,
        "undefined *"
      ]
    ],
    [
      "009f6410",
      "DATA",
      [
        "storage",
        "00c8a550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f63cc",
      "DATA",
      [
        "storage",
        "00c8b550",
        null,
        "undefined *"
      ]
    ],
    [
      "009f6410",
      "DATA",
      [
        "storage",
        "00c8b520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f5418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f53fc.md#insn-009f5418) · [`009f541c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f53fc.md#insn-009f541c) · [`009f5430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f53fc.md#insn-009f5430)
- 新版 [`009f63c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f6/009f63a8.md#insn-009f63c4) · [`009f63c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f6/009f63a8.md#insn-009f63c8) · [`009f63dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f6/009f63a8.md#insn-009f63dc)

~~~diff
- 009f5418 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 009f63c4 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009f5418 bytes a81400b0
+ 009f63c4 bytes a81400b0
- 009f541c ["COPY", "tmp:0:8", ["const:580:8"]]
- 009f541c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f541c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f541c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f63c8 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 009f63c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f63c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f63c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f541c bytes 08011691
+ 009f63c8 bytes 08411591
- 009f5430 ["INT_ADD", "register:40f0:8", ["const:9f5430:8", "const:4:8"]]
- 009f5430 ["CALL", null, ["callee:00c54d90:8"]]
+ 009f63dc ["INT_ADD", "register:40f0:8", ["const:9f63dc:8", "const:4:8"]]
+ 009f63dc ["CALL", null, ["callee:00c54d90:8"]]
- 009f5430 bytes 5c7a0994
+ 009f63dc bytes 6d7a0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

