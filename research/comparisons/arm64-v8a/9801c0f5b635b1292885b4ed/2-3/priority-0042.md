# v16.0.1 → v16.0.2 · 最優先の変更候補 (42)

[一覧の目次](README.md)

<a id="compare-70074064072de66e913f2f0b3f038d7a"></a>

### [`007fa790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa790.md) → [`007fa7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa7e8.md) FUN_007fa7e8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fa7ec",
      "incomplete_value": false,
      "site": "007fa7f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fa794",
      "incomplete_value": false,
      "site": "007fa798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "007fa7f0",
      "DATA",
      [
        "storage",
        "00c7cca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fa7f0",
      "DATA",
      [
        "storage",
        "00c7cd70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fa794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa790.md#insn-007fa794)
- 新版 `007fa7ec`（命令位置の公開資料なし）

~~~diff
- 007fa794 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 007fa794 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fa794 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fa794 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fa7ec ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 007fa7ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa7ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa7ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fa794 bytes 08813291
+ 007fa7ec bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93673b96766bcd17242de28d7ebfd348"></a>

### [`007fa7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa7b0.md) → [`007fa808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa808.md) FUN_007fa808

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f10.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f68.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

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
      "site": "007fa83c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fa7e4",
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
      "007fa83c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fa83c",
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

- 旧版 [`007fa7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa7b0.md#insn-007fa7e4) · [`007fa7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa7b0.md#insn-007fa7f0) · [`007fa7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa7b0.md#insn-007fa7f8)
- 新版 `007fa83c`（命令位置の公開資料なし） · `007fa848`（命令位置の公開資料なし） · `007fa850`（命令位置の公開資料なし）

~~~diff
- 007fa7e4 ["INT_ADD", "register:40f0:8", ["const:7fa7e4:8", "const:4:8"]]
- 007fa7e4 ["CALL", null, ["ram:47acf4:8"]]
+ 007fa83c ["INT_ADD", "register:40f0:8", ["const:7fa83c:8", "const:4:8"]]
+ 007fa83c ["CALL", null, ["ram:47ad34:8"]]
- 007fa7e4 bytes 4401f297
+ 007fa83c bytes 3e01f297
- 007fa7f0 ["INT_ADD", "register:40f0:8", ["const:7fa7f0:8", "const:4:8"]]
- 007fa7f0 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fa848 ["INT_ADD", "register:40f0:8", ["const:7fa848:8", "const:4:8"]]
+ 007fa848 ["CALL", null, ["callee:0047ce14:8"]]
- 007fa7f0 bytes 7909f297
+ 007fa848 bytes 7309f297
- 007fa7f8 ["INT_ADD", "register:40f0:8", ["const:7fa7f8:8", "const:4:8"]]
- 007fa7f8 ["CALL", null, ["callee:008b91d0:8"]]
+ 007fa850 ["INT_ADD", "register:40f0:8", ["const:7fa850:8", "const:4:8"]]
+ 007fa850 ["CALL", null, ["callee:008b91d0:8"]]
- 007fa7f8 bytes 60fa0294
+ 007fa850 bytes 60fa0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5b82da9ad2eeeb95568021630a11d14"></a>

### [`007fa868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa868.md) → [`007fa8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa8c0.md) FUN_007fa8c0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fa8d4",
      "incomplete_value": false,
      "site": "007fa8d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fa87c",
      "incomplete_value": false,
      "site": "007fa880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "007fa8d8",
      "DATA",
      [
        "storage",
        "00c7cd20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fa8d8",
      "DATA",
      [
        "storage",
        "00c7cdf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fa874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa868.md#insn-007fa874) · [`007fa87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa868.md#insn-007fa87c)
- 新版 `007fa8cc`（命令位置の公開資料なし） · `007fa8d4`（命令位置の公開資料なし）

~~~diff
- 007fa874 ["INT_ADD", "register:40f0:8", ["const:7fa874:8", "const:4:8"]]
- 007fa874 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fa8cc ["INT_ADD", "register:40f0:8", ["const:7fa8cc:8", "const:4:8"]]
+ 007fa8cc ["CALL", null, ["callee:00c57f60:8"]]
- 007fa874 bytes 87751194
+ 007fa8cc bytes a5751194
- 007fa87c ["COPY", "tmp:0:8", ["const:d20:8"]]
- 007fa87c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fa87c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fa87c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fa8d4 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 007fa8d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa8d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa8d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fa87c bytes 08813491
+ 007fa8d4 bytes 08c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f6fc4398a0da2b9c4cb5171b34cc053"></a>

### [`007fa88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa88c.md) → [`007fa8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa8e4.md) FUN_007fa8e4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fa8e8",
      "incomplete_value": false,
      "site": "007fa8ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fa890",
      "incomplete_value": false,
      "site": "007fa894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "007fa8ec",
      "DATA",
      [
        "storage",
        "00c7cd20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fa8ec",
      "DATA",
      [
        "storage",
        "00c7cdf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fa890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa88c.md#insn-007fa890)
- 新版 `007fa8e8`（命令位置の公開資料なし）

~~~diff
- 007fa890 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 007fa890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fa890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fa890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fa8e8 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 007fa8e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa8e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa8e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fa890 bytes 08813491
+ 007fa8e8 bytes 08c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05b01815a2b3bdc7aab7bc7a3eecbc72"></a>

### [`007fa8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa8a4.md) → [`007fa8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa8fc.md) FUN_007fa8fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fa920",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fa8c8",
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
      "007fa920",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fa920",
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

- 旧版 [`007fa8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa8a4.md#insn-007fa8c8) · [`007fa8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa8a4.md#insn-007fa8d4)
- 新版 `007fa920`（命令位置の公開資料なし） · `007fa92c`（命令位置の公開資料なし）

~~~diff
- 007fa8c8 ["INT_ADD", "register:40f0:8", ["const:7fa8c8:8", "const:4:8"]]
- 007fa8c8 ["CALL", null, ["ram:47acf4:8"]]
+ 007fa920 ["INT_ADD", "register:40f0:8", ["const:7fa920:8", "const:4:8"]]
+ 007fa920 ["CALL", null, ["ram:47ad34:8"]]
- 007fa8c8 bytes 0b01f297
+ 007fa920 bytes 0501f297
- 007fa8d4 ["INT_ADD", "register:40f0:8", ["const:7fa8d4:8", "const:4:8"]]
- 007fa8d4 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fa92c ["INT_ADD", "register:40f0:8", ["const:7fa92c:8", "const:4:8"]]
+ 007fa92c ["CALL", null, ["callee:0047ce14:8"]]
- 007fa8d4 bytes 4009f297
+ 007fa92c bytes 3a09f297
~~~


<a id="compare-099e0977ae51916b56d9f69d19354e28"></a>

### [`007fa918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa918.md) → [`007fa970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa970.md) FUN_007fa970

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fa98c",
      "incomplete_value": false,
      "site": "007fa998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fa934",
      "incomplete_value": false,
      "site": "007fa940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "007fa998",
      "DATA",
      [
        "storage",
        "00c7cdb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007fa998",
      "DATA",
      [
        "storage",
        "00c7ce80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fa92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa918.md#insn-007fa92c) · [`007fa934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa918.md#insn-007fa934)
- 新版 `007fa984`（命令位置の公開資料なし） · `007fa98c`（命令位置の公開資料なし）

~~~diff
- 007fa92c ["INT_ADD", "register:40f0:8", ["const:7fa92c:8", "const:4:8"]]
- 007fa92c ["CALL", null, ["callee:00c57f60:8"]]
+ 007fa984 ["INT_ADD", "register:40f0:8", ["const:7fa984:8", "const:4:8"]]
+ 007fa984 ["CALL", null, ["callee:00c57f60:8"]]
- 007fa92c bytes 59751194
+ 007fa984 bytes 77751194
- 007fa934 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 007fa934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fa934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fa934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fa98c ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 007fa98c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa98c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa98c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fa934 bytes 08c13691
+ 007fa98c bytes 08013a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16e274b5898ba76d15c4340a30bfb9d9"></a>

### [`007fa960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa960.md) → [`007fa9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa9b8.md) FUN_007fa9b8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007fa9bc",
      "incomplete_value": false,
      "site": "007fa9c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fa964",
      "incomplete_value": false,
      "site": "007fa968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "007fa9c0",
      "DATA",
      [
        "storage",
        "00c7cdb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007fa9c0",
      "DATA",
      [
        "storage",
        "00c7ce80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fa964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa960.md#insn-007fa964)
- 新版 `007fa9bc`（命令位置の公開資料なし）

~~~diff
- 007fa964 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 007fa964 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fa964 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fa964 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fa9bc ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 007fa9bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa9bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa9bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fa964 bytes 08c13691
+ 007fa9bc bytes 08013a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0a65ec393881e1873ca5296cade7368"></a>

### [`007fa990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa990.md) → [`007fa9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa9e8.md) FUN_007fa9e8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 27件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.47% / 新版 97.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007fae50",
      "incomplete_value": false,
      "site": "007fae50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fadf8",
      "incomplete_value": false,
      "site": "007fadf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:e20:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fac68",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fac10",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 19,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007faca0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fac48",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 23,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007fac68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007faca0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007face4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fac68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007faca0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007face4",
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

- 旧版 [`007fac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa990.md#insn-007fac10) · [`007fac48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa990.md#insn-007fac48) · [`007fac8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa990.md#insn-007fac8c)
- 新版 `007fac68`（命令位置の公開資料なし） · `007faca0`（命令位置の公開資料なし） · `007face4`（命令位置の公開資料なし）

~~~diff
- 007fac10 ["INT_ADD", "register:40f0:8", ["const:7fac10:8", "const:4:8"]]
- 007fac10 ["CALL", null, ["ram:47acf4:8"]]
+ 007fac68 ["INT_ADD", "register:40f0:8", ["const:7fac68:8", "const:4:8"]]
+ 007fac68 ["CALL", null, ["ram:47ad34:8"]]
- 007fac10 bytes 3900f297
+ 007fac68 bytes 3300f297
- 007fac48 ["INT_ADD", "register:40f0:8", ["const:7fac48:8", "const:4:8"]]
- 007fac48 ["CALL", null, ["ram:47acf4:8"]]
+ 007faca0 ["INT_ADD", "register:40f0:8", ["const:7faca0:8", "const:4:8"]]
+ 007faca0 ["CALL", null, ["ram:47ad34:8"]]
- 007fac48 bytes 2b00f297
+ 007faca0 bytes 2500f297
- 007fac8c ["INT_ADD", "register:40f0:8", ["const:7fac8c:8", "const:4:8"]]
- 007fac8c ["CALL", null, ["ram:47acf4:8"]]
+ 007face4 ["INT_ADD", "register:40f0:8", ["const:7face4:8", "const:4:8"]]
+ 007face4 ["CALL", null, ["ram:47ad34:8"]]
- 007fac8c bytes 1a00f297
+ 007face4 bytes 1400f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-585347d43a6660e3883b7f2fca101d70"></a>

### [`007faf3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007faf3c.md) → [`007faf94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007faf94.md) FUN_007faf94

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007fa990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa990.md) [`007fbe08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbe08.md) · 呼出先 11件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md) [`00744198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744198.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 2件 [`007fa9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa9e8.md) [`007fbe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fbe60.md) · 呼出先 11件 [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`006648e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/006648e0.md) [`007441f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/007441f0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 81.31% / 新版 81.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007fb10c",
      "incomplete_value": false,
      "site": "007fb10c",
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
    "old": {
      "definition_site": "007fb0b4",
      "incomplete_value": false,
      "site": "007fb0b4",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007fb110",
      "incomplete_value": false,
      "site": "007fb110",
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
    "old": {
      "definition_site": "007fb0b8",
      "incomplete_value": false,
      "site": "007fb0b8",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007fb10c",
      "incomplete_value": false,
      "site": "007fb110",
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
    "old": {
      "definition_site": "007fb0b4",
      "incomplete_value": false,
      "site": "007fb0b8",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
      "007fafe0",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "007fafec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648a0"
      ]
    ],
    [
      "007faff8",
      "PARAM",
      [
        "storage",
        "00ca4f00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "007fafe0",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "007fafec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648e0"
      ]
    ],
    [
      "007faff8",
      "PARAM",
      [
        "storage",
        "00ca5000",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007faf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007faf3c.md#insn-007faf94) · [`007fafc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007faf3c.md#insn-007fafc0) · [`007fb018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007faf3c.md#insn-007fb018)
- 新版 `007fafec`（命令位置の公開資料なし） · `007fb018`（命令位置の公開資料なし） · `007fb070`（命令位置の公開資料なし）

~~~diff
- 007faf94 ["INT_ADD", "register:40f0:8", ["const:7faf94:8", "const:4:8"]]
- 007faf94 ["CALL", null, ["ram:6648a0:8"]]
+ 007fafec ["INT_ADD", "register:40f0:8", ["const:7fafec:8", "const:4:8"]]
+ 007fafec ["CALL", null, ["ram:6648e0:8"]]
- 007faf94 bytes 43a6f997
+ 007fafec bytes 3da6f997
- 007fafc0 ["INT_ADD", "register:40f0:8", ["const:7fafc0:8", "const:4:8"]]
- 007fafc0 ["CALL", null, ["callee:0047e91c:8"]]
+ 007fb018 ["INT_ADD", "register:40f0:8", ["const:7fb018:8", "const:4:8"]]
+ 007fb018 ["CALL", null, ["callee:0047e91c:8"]]
- 007fafc0 bytes 470ef297
+ 007fb018 bytes 410ef297
- 007fb018 ["INT_ADD", "register:40f0:8", ["const:7fb018:8", "const:4:8"]]
- 007fb018 ["CALL", null, ["callee:00c53da0:8"]]
+ 007fb070 ["INT_ADD", "register:40f0:8", ["const:7fb070:8", "const:4:8"]]
+ 007fb070 ["CALL", null, ["callee:00c53da0:8"]]
- 007fb018 bytes 3a631194
+ 007fb070 bytes 4c631194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b33b11c5e747c426af620b50bab34178"></a>

### [`007fb118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb118.md) → [`007fb170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fb170.md) FUN_007fb170

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fb184",
      "incomplete_value": false,
      "site": "007fb188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fb12c",
      "incomplete_value": false,
      "site": "007fb130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "007fb188",
      "DATA",
      [
        "storage",
        "00c7ce20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fb188",
      "DATA",
      [
        "storage",
        "00c7cef0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fb124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb118.md#insn-007fb124) · [`007fb12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb118.md#insn-007fb12c)
- 新版 `007fb17c`（命令位置の公開資料なし） · `007fb184`（命令位置の公開資料なし）

~~~diff
- 007fb124 ["INT_ADD", "register:40f0:8", ["const:7fb124:8", "const:4:8"]]
- 007fb124 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fb17c ["INT_ADD", "register:40f0:8", ["const:7fb17c:8", "const:4:8"]]
+ 007fb17c ["CALL", null, ["callee:00c57f60:8"]]
- 007fb124 bytes 5b731194
+ 007fb17c bytes 79731194
- 007fb12c ["COPY", "tmp:0:8", ["const:e20:8"]]
- 007fb12c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fb12c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fb12c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fb184 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 007fb184 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb184 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fb12c bytes 08813891
+ 007fb184 bytes 08c13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3afe80cd8a82b9ef1a8a61fb8388d003"></a>

### [`007fb13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb13c.md) → [`007fb194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fb194.md) FUN_007fb194

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fb198",
      "incomplete_value": false,
      "site": "007fb19c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fb140",
      "incomplete_value": false,
      "site": "007fb144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "007fb19c",
      "DATA",
      [
        "storage",
        "00c7ce20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fb19c",
      "DATA",
      [
        "storage",
        "00c7cef0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fb140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb13c.md#insn-007fb140)
- 新版 `007fb198`（命令位置の公開資料なし）

~~~diff
- 007fb140 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 007fb140 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fb140 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fb140 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fb198 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 007fb198 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb198 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb198 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fb140 bytes 08813891
+ 007fb198 bytes 08c13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26a01f59436d3a40c11945d3f17c4d5c"></a>

### [`007fb154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb154.md) → [`007fb1ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fb1ac.md) FUN_007fb1ac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fb1d0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fb178",
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
      "007fb1d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fb1d0",
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

- 旧版 [`007fb178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb154.md#insn-007fb178) · [`007fb184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb154.md#insn-007fb184)
- 新版 `007fb1d0`（命令位置の公開資料なし） · `007fb1dc`（命令位置の公開資料なし）

~~~diff
- 007fb178 ["INT_ADD", "register:40f0:8", ["const:7fb178:8", "const:4:8"]]
- 007fb178 ["CALL", null, ["ram:47acf4:8"]]
+ 007fb1d0 ["INT_ADD", "register:40f0:8", ["const:7fb1d0:8", "const:4:8"]]
+ 007fb1d0 ["CALL", null, ["ram:47ad34:8"]]
- 007fb178 bytes dffef197
+ 007fb1d0 bytes d9fef197
- 007fb184 ["INT_ADD", "register:40f0:8", ["const:7fb184:8", "const:4:8"]]
- 007fb184 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fb1dc ["INT_ADD", "register:40f0:8", ["const:7fb1dc:8", "const:4:8"]]
+ 007fb1dc ["CALL", null, ["callee:0047ce14:8"]]
- 007fb184 bytes 1407f297
+ 007fb1dc bytes 0e07f297
~~~


<a id="compare-ac5faa202cf78c133c8e70913ec8aa1e"></a>

### [`007fb1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb1c8.md) → [`007fb220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fb220.md) FUN_007fb220

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fb244",
      "incomplete_value": false,
      "site": "007fb248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fb1ec",
      "incomplete_value": false,
      "site": "007fb1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "007fb248",
      "DATA",
      [
        "storage",
        "00c7ceb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fb248",
      "DATA",
      [
        "storage",
        "00c7cf80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fb1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb1c8.md#insn-007fb1dc) · [`007fb1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb1c8.md#insn-007fb1ec)
- 新版 `007fb234`（命令位置の公開資料なし） · `007fb244`（命令位置の公開資料なし）

~~~diff
- 007fb1dc ["INT_ADD", "register:40f0:8", ["const:7fb1dc:8", "const:4:8"]]
- 007fb1dc ["CALL", null, ["callee:00c57f60:8"]]
+ 007fb234 ["INT_ADD", "register:40f0:8", ["const:7fb234:8", "const:4:8"]]
+ 007fb234 ["CALL", null, ["callee:00c57f60:8"]]
- 007fb1dc bytes 2d731194
+ 007fb234 bytes 4b731194
- 007fb1ec ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 007fb1ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fb1ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fb1ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fb244 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 007fb244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fb1ec bytes 08c13a91
+ 007fb244 bytes 08013e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b8990c7ae3860c30d94d339fa2af113"></a>

### [`007fb208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb208.md) → [`007fb260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fb260.md) FUN_007fb260

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "007fb264",
      "incomplete_value": false,
      "site": "007fb268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fb20c",
      "incomplete_value": false,
      "site": "007fb210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "007fb268",
      "DATA",
      [
        "storage",
        "00c7ceb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fb268",
      "DATA",
      [
        "storage",
        "00c7cf80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fb20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb208.md#insn-007fb20c)
- 新版 `007fb264`（命令位置の公開資料なし）

~~~diff
- 007fb20c ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 007fb20c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fb20c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fb20c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fb264 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 007fb264 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb264 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb264 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fb20c bytes 08c13a91
+ 007fb264 bytes 08013e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62b3e1f42f998994741e9798a195efec"></a>

### [`007fbda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbda0.md) → [`007fbdf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fbdf8.md) FUN_007fbdf8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fbe1c",
      "incomplete_value": false,
      "site": "007fbe20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fbdc4",
      "incomplete_value": false,
      "site": "007fbdc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
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
      "007fbe20",
      "DATA",
      [
        "storage",
        "00c7cf30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fbe20",
      "DATA",
      [
        "storage",
        "00c7d000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fbdb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbda0.md#insn-007fbdb4) · [`007fbdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbda0.md#insn-007fbdc0) · [`007fbdc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbda0.md#insn-007fbdc4)
- 新版 `007fbe0c`（命令位置の公開資料なし） · `007fbe18`（命令位置の公開資料なし） · `007fbe1c`（命令位置の公開資料なし）

~~~diff
- 007fbdb4 ["INT_ADD", "register:40f0:8", ["const:7fbdb4:8", "const:4:8"]]
- 007fbdb4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fbe0c ["INT_ADD", "register:40f0:8", ["const:7fbe0c:8", "const:4:8"]]
+ 007fbe0c ["CALL", null, ["callee:00c57f60:8"]]
- 007fbdb4 bytes 37701194
+ 007fbe0c bytes 55701194
- 007fbdc0 ["COPY", "register:4040:8", ["const:c7c000:8"]]
+ 007fbe18 ["COPY", "register:4040:8", ["const:c7d000:8"]]
- 007fbdc0 bytes 082400b0
+ 007fbe18 bytes 082400d0
- 007fbdc4 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 007fbdc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fbdc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fbdc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fbe1c ["COPY", "tmp:0:8", ["const:0:8"]]
+ 007fbe1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fbe1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fbe1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fbdc4 bytes 08c13c91
+ 007fbe1c bytes 08010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43c61e5389fc610cf29b706379ed8330"></a>

### [`007fbde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbde0.md) → [`007fbe38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fbe38.md) FUN_007fbe38

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "007fbe3c",
      "incomplete_value": false,
      "site": "007fbe40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fbde4",
      "incomplete_value": false,
      "site": "007fbde8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
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
      "007fbe40",
      "DATA",
      [
        "storage",
        "00c7cf30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fbe40",
      "DATA",
      [
        "storage",
        "00c7d000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fbde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbde0.md#insn-007fbde0) · [`007fbde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbde0.md#insn-007fbde4)
- 新版 `007fbe38`（命令位置の公開資料なし） · `007fbe3c`（命令位置の公開資料なし）

~~~diff
- 007fbde0 ["COPY", "register:4040:8", ["const:c7c000:8"]]
+ 007fbe38 ["COPY", "register:4040:8", ["const:c7d000:8"]]
- 007fbde0 bytes 082400b0
+ 007fbe38 bytes 082400d0
- 007fbde4 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 007fbde4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fbde4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fbde4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fbe3c ["COPY", "tmp:0:8", ["const:0:8"]]
+ 007fbe3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fbe3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fbe3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fbde4 bytes 08c13c91
+ 007fbe3c bytes 08010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f331d2c5f3c921cc935b38a77af0f32f"></a>

### [`007fbe08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbe08.md) → [`007fbe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fbe60.md) FUN_007fbe60

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00743d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743d90.md) [`00743e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743e5c.md) [`00744f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744f74.md)
- 新版 呼出元 0件  · 呼出先 17件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00743de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743de8.md) [`00743eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743eb4.md) [`00744fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744fcc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

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
      "site": "007fbea4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fbe4c",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "007fbec4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fbe6c",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007fbea4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007fbec4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fbea4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007fbec4",
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

- 旧版 [`007fbe4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbe08.md#insn-007fbe4c) · [`007fbe6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbe08.md#insn-007fbe6c) · [`007fbea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbe08.md#insn-007fbea4)
- 新版 `007fbea4`（命令位置の公開資料なし） · `007fbec4`（命令位置の公開資料なし） · `007fbefc`（命令位置の公開資料なし）

~~~diff
- 007fbe4c ["INT_ADD", "register:40f0:8", ["const:7fbe4c:8", "const:4:8"]]
- 007fbe4c ["CALL", null, ["ram:47acf4:8"]]
+ 007fbea4 ["INT_ADD", "register:40f0:8", ["const:7fbea4:8", "const:4:8"]]
+ 007fbea4 ["CALL", null, ["ram:47ad34:8"]]
- 007fbe4c bytes aafbf197
+ 007fbea4 bytes a4fbf197
- 007fbe6c ["INT_ADD", "register:40f0:8", ["const:7fbe6c:8", "const:4:8"]]
- 007fbe6c ["CALL", null, ["ram:47acf4:8"]]
+ 007fbec4 ["INT_ADD", "register:40f0:8", ["const:7fbec4:8", "const:4:8"]]
+ 007fbec4 ["CALL", null, ["ram:47ad34:8"]]
- 007fbe6c bytes a2fbf197
+ 007fbec4 bytes 9cfbf197
- 007fbea4 ["INT_ADD", "register:40f0:8", ["const:7fbea4:8", "const:4:8"]]
- 007fbea4 ["CALL", null, ["callee:008bb568:8"]]
+ 007fbefc ["INT_ADD", "register:40f0:8", ["const:7fbefc:8", "const:4:8"]]
+ 007fbefc ["CALL", null, ["callee:008bb568:8"]]
- 007fbea4 bytes 9bfd0294
+ 007fbefc bytes 9bfd0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72fb90cd731b224212b7dfb0e908aff9"></a>

### [`007fc020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc020.md) → [`007fc078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc078.md) FUN_007fc078

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 0件 
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007fc088",
      "incomplete_value": true,
      "site": "007fc08c",
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
    "old": {
      "definition_site": "007fc030",
      "incomplete_value": true,
      "site": "007fc034",
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


#### 変更候補の命令位置

- 旧版 [`007fc028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc020.md#insn-007fc028)
- 新版 `007fc080`（命令位置の公開資料なし）

~~~diff
- 007fc028 ["COPY", "tmp:0:8", ["const:97b:8"]]
- 007fc028 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fc028 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fc028 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fc080 ["COPY", "tmp:0:8", ["const:9bb:8"]]
+ 007fc080 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fc080 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fc080 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fc028 bytes 29ed2591
+ 007fc080 bytes 29ed2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2be65242eb95bb4f8c60dbf04d7cf604"></a>

### [`007fc04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc04c.md) → [`007fc0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc0a4.md) FUN_007fc0a4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fc0b8",
      "incomplete_value": false,
      "site": "007fc0bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc060",
      "incomplete_value": false,
      "site": "007fc064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      "007fc0bc",
      "DATA",
      [
        "storage",
        "00c7cfb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc0bc",
      "DATA",
      [
        "storage",
        "00c7d080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc04c.md#insn-007fc058) · [`007fc05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc04c.md#insn-007fc05c) · [`007fc060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc04c.md#insn-007fc060)
- 新版 `007fc0b0`（命令位置の公開資料なし） · `007fc0b4`（命令位置の公開資料なし） · `007fc0b8`（命令位置の公開資料なし）

~~~diff
- 007fc058 ["INT_ADD", "register:40f0:8", ["const:7fc058:8", "const:4:8"]]
- 007fc058 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fc0b0 ["INT_ADD", "register:40f0:8", ["const:7fc0b0:8", "const:4:8"]]
+ 007fc0b0 ["CALL", null, ["callee:00c57f60:8"]]
- 007fc058 bytes 8e6f1194
+ 007fc0b0 bytes ac6f1194
- 007fc05c ["COPY", "register:4040:8", ["const:c7c000:8"]]
+ 007fc0b4 ["COPY", "register:4040:8", ["const:c7d000:8"]]
- 007fc05c bytes 08240090
+ 007fc0b4 bytes 082400b0
- 007fc060 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 007fc060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc0b8 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 007fc0b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc0b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc0b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc060 bytes 08c13e91
+ 007fc0b8 bytes 08010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b05845b58b5f764d9094985f539a8ec8"></a>

### [`007fc070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc070.md) → [`007fc0c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc0c8.md) FUN_007fc0c8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fc0cc",
      "incomplete_value": false,
      "site": "007fc0d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc074",
      "incomplete_value": false,
      "site": "007fc078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
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
      "007fc0d0",
      "DATA",
      [
        "storage",
        "00c7cfb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc0d0",
      "DATA",
      [
        "storage",
        "00c7d080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc070.md#insn-007fc070) · [`007fc074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc070.md#insn-007fc074)
- 新版 `007fc0c8`（命令位置の公開資料なし） · `007fc0cc`（命令位置の公開資料なし）

~~~diff
- 007fc070 ["COPY", "register:4040:8", ["const:c7c000:8"]]
+ 007fc0c8 ["COPY", "register:4040:8", ["const:c7d000:8"]]
- 007fc070 bytes 08240090
+ 007fc0c8 bytes 082400b0
- 007fc074 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 007fc074 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc074 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc074 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc0cc ["COPY", "tmp:0:8", ["const:80:8"]]
+ 007fc0cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc0cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc0cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc074 bytes 08c13e91
+ 007fc0cc bytes 08010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-465c643cef9d396a014e3377327d53d7"></a>

### [`007fc088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc088.md) → [`007fc0e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc0e0.md) FUN_007fc0e0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fc104",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc0ac",
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
      "007fc104",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fc104",
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

- 旧版 [`007fc0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc088.md#insn-007fc0ac) · [`007fc0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc088.md#insn-007fc0b8)
- 新版 `007fc104`（命令位置の公開資料なし） · `007fc110`（命令位置の公開資料なし）

~~~diff
- 007fc0ac ["INT_ADD", "register:40f0:8", ["const:7fc0ac:8", "const:4:8"]]
- 007fc0ac ["CALL", null, ["ram:47acf4:8"]]
+ 007fc104 ["INT_ADD", "register:40f0:8", ["const:7fc104:8", "const:4:8"]]
+ 007fc104 ["CALL", null, ["ram:47ad34:8"]]
- 007fc0ac bytes 12fbf197
+ 007fc104 bytes 0cfbf197
- 007fc0b8 ["INT_ADD", "register:40f0:8", ["const:7fc0b8:8", "const:4:8"]]
- 007fc0b8 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fc110 ["INT_ADD", "register:40f0:8", ["const:7fc110:8", "const:4:8"]]
+ 007fc110 ["CALL", null, ["callee:0047ce14:8"]]
- 007fc0b8 bytes 4703f297
+ 007fc110 bytes 4103f297
~~~


<a id="compare-a6043c25aa01cb30edff26b7b5e350d8"></a>

### [`007fc0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc0fc.md) → [`007fc154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc154.md) FUN_007fc154

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fc168",
      "incomplete_value": false,
      "site": "007fc16c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc110",
      "incomplete_value": false,
      "site": "007fc114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:30:8"
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
      "007fc16c",
      "DATA",
      [
        "storage",
        "00c7d030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc16c",
      "DATA",
      [
        "storage",
        "00c7d100",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc0fc.md#insn-007fc108) · [`007fc110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc0fc.md#insn-007fc110)
- 新版 `007fc160`（命令位置の公開資料なし） · `007fc168`（命令位置の公開資料なし）

~~~diff
- 007fc108 ["INT_ADD", "register:40f0:8", ["const:7fc108:8", "const:4:8"]]
- 007fc108 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fc160 ["INT_ADD", "register:40f0:8", ["const:7fc160:8", "const:4:8"]]
+ 007fc160 ["CALL", null, ["callee:00c57f60:8"]]
- 007fc108 bytes 626f1194
+ 007fc160 bytes 806f1194
- 007fc110 ["COPY", "tmp:0:8", ["const:30:8"]]
- 007fc110 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc110 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc110 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc168 ["COPY", "tmp:0:8", ["const:100:8"]]
+ 007fc168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc110 bytes 08c10091
+ 007fc168 bytes 08010491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20facea2d488911324ef1af45efe4f4d"></a>

### [`007fc120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc120.md) → [`007fc178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc178.md) FUN_007fc178

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fc17c",
      "incomplete_value": false,
      "site": "007fc180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc124",
      "incomplete_value": false,
      "site": "007fc128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007fc180",
      "DATA",
      [
        "storage",
        "00c7d030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc180",
      "DATA",
      [
        "storage",
        "00c7d100",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc120.md#insn-007fc124)
- 新版 `007fc17c`（命令位置の公開資料なし）

~~~diff
- 007fc124 ["COPY", "tmp:0:8", ["const:30:8"]]
- 007fc124 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc124 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc124 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc17c ["COPY", "tmp:0:8", ["const:100:8"]]
+ 007fc17c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc17c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc17c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc124 bytes 08c10091
+ 007fc17c bytes 08010491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efa60d2fc18d20a7d246c05992fcdc40"></a>

### [`007fc138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc138.md) → [`007fc190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc190.md) FUN_007fc190

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fc1b4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc15c",
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
      "007fc1b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fc1b4",
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

- 旧版 [`007fc15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc138.md#insn-007fc15c) · [`007fc168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc138.md#insn-007fc168)
- 新版 `007fc1b4`（命令位置の公開資料なし） · `007fc1c0`（命令位置の公開資料なし）

~~~diff
- 007fc15c ["INT_ADD", "register:40f0:8", ["const:7fc15c:8", "const:4:8"]]
- 007fc15c ["CALL", null, ["ram:47acf4:8"]]
+ 007fc1b4 ["INT_ADD", "register:40f0:8", ["const:7fc1b4:8", "const:4:8"]]
+ 007fc1b4 ["CALL", null, ["ram:47ad34:8"]]
- 007fc15c bytes e6faf197
+ 007fc1b4 bytes e0faf197
- 007fc168 ["INT_ADD", "register:40f0:8", ["const:7fc168:8", "const:4:8"]]
- 007fc168 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fc1c0 ["INT_ADD", "register:40f0:8", ["const:7fc1c0:8", "const:4:8"]]
+ 007fc1c0 ["CALL", null, ["callee:0047ce14:8"]]
- 007fc168 bytes 1b03f297
+ 007fc1c0 bytes 1503f297
~~~


<a id="compare-84b2c6db69dd867230b6907b2b7c6627"></a>

### [`007fc1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc1ac.md) → [`007fc204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc204.md) FUN_007fc204

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fc218",
      "incomplete_value": false,
      "site": "007fc21c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc1c0",
      "incomplete_value": false,
      "site": "007fc1c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "007fc21c",
      "DATA",
      [
        "storage",
        "00c7d0b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc21c",
      "DATA",
      [
        "storage",
        "00c7d180",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc1ac.md#insn-007fc1b8) · [`007fc1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc1ac.md#insn-007fc1c0)
- 新版 `007fc210`（命令位置の公開資料なし） · `007fc218`（命令位置の公開資料なし）

~~~diff
- 007fc1b8 ["INT_ADD", "register:40f0:8", ["const:7fc1b8:8", "const:4:8"]]
- 007fc1b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fc210 ["INT_ADD", "register:40f0:8", ["const:7fc210:8", "const:4:8"]]
+ 007fc210 ["CALL", null, ["callee:00c57f60:8"]]
- 007fc1b8 bytes 366f1194
+ 007fc210 bytes 546f1194
- 007fc1c0 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 007fc1c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc1c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc1c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc218 ["COPY", "tmp:0:8", ["const:180:8"]]
+ 007fc218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc1c0 bytes 08c10291
+ 007fc218 bytes 08010691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77a064f9218c022eb8f28ec556ce7b1f"></a>

### [`007fc1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc1d0.md) → [`007fc228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc228.md) FUN_007fc228

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fc22c",
      "incomplete_value": false,
      "site": "007fc230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc1d4",
      "incomplete_value": false,
      "site": "007fc1d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007fc230",
      "DATA",
      [
        "storage",
        "00c7d0b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc230",
      "DATA",
      [
        "storage",
        "00c7d180",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc1d0.md#insn-007fc1d4)
- 新版 `007fc22c`（命令位置の公開資料なし）

~~~diff
- 007fc1d4 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 007fc1d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc1d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc1d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc22c ["COPY", "tmp:0:8", ["const:180:8"]]
+ 007fc22c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc22c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc22c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc1d4 bytes 08c10291
+ 007fc22c bytes 08010691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a6e4a3852f043d53b175ff84e02fd40"></a>

### [`007fc1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc1e8.md) → [`007fc240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc240.md) FUN_007fc240

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fc264",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc20c",
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
      "007fc264",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fc264",
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

- 旧版 [`007fc20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc1e8.md#insn-007fc20c) · [`007fc218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc1e8.md#insn-007fc218)
- 新版 `007fc264`（命令位置の公開資料なし） · `007fc270`（命令位置の公開資料なし）

~~~diff
- 007fc20c ["INT_ADD", "register:40f0:8", ["const:7fc20c:8", "const:4:8"]]
- 007fc20c ["CALL", null, ["ram:47acf4:8"]]
+ 007fc264 ["INT_ADD", "register:40f0:8", ["const:7fc264:8", "const:4:8"]]
+ 007fc264 ["CALL", null, ["ram:47ad34:8"]]
- 007fc20c bytes bafaf197
+ 007fc264 bytes b4faf197
- 007fc218 ["INT_ADD", "register:40f0:8", ["const:7fc218:8", "const:4:8"]]
- 007fc218 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fc270 ["INT_ADD", "register:40f0:8", ["const:7fc270:8", "const:4:8"]]
+ 007fc270 ["CALL", null, ["callee:0047ce14:8"]]
- 007fc218 bytes ef02f297
+ 007fc270 bytes e902f297
~~~


<a id="compare-b4ef0eb93885fe33ed1fd2d1a6e9302f"></a>

### [`007fc25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc25c.md) → [`007fc2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc2b4.md) FUN_007fc2b4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fc2d8",
      "incomplete_value": false,
      "site": "007fc2d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc280",
      "incomplete_value": false,
      "site": "007fc280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007fc2d8",
      "DATA",
      [
        "storage",
        "00c7d130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc2d8",
      "DATA",
      [
        "storage",
        "00c7d200",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc25c.md#insn-007fc270) · [`007fc27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc25c.md#insn-007fc27c)
- 新版 `007fc2c8`（命令位置の公開資料なし） · `007fc2d4`（命令位置の公開資料なし）

~~~diff
- 007fc270 ["INT_ADD", "register:40f0:8", ["const:7fc270:8", "const:4:8"]]
- 007fc270 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fc2c8 ["INT_ADD", "register:40f0:8", ["const:7fc2c8:8", "const:4:8"]]
+ 007fc2c8 ["CALL", null, ["callee:00c57f60:8"]]
- 007fc270 bytes 086f1194
+ 007fc2c8 bytes 266f1194
- 007fc27c ["COPY", "tmp:0:8", ["const:130:8"]]
- 007fc27c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc27c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc27c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc2d4 ["COPY", "tmp:0:8", ["const:200:8"]]
+ 007fc2d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc2d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc2d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc27c bytes 08c10491
+ 007fc2d4 bytes 08010891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e68a37d0c152342ab88d205d96769fa"></a>

### [`007fc290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc290.md) → [`007fc2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc2e8.md) FUN_007fc2e8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fc2f4",
      "incomplete_value": false,
      "site": "007fc2f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc29c",
      "incomplete_value": false,
      "site": "007fc29c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007fc2f4",
      "DATA",
      [
        "storage",
        "00c7d130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc2f4",
      "DATA",
      [
        "storage",
        "00c7d200",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc290.md#insn-007fc298)
- 新版 `007fc2f0`（命令位置の公開資料なし）

~~~diff
- 007fc298 ["COPY", "tmp:0:8", ["const:130:8"]]
- 007fc298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fc298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fc298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fc2f0 ["COPY", "tmp:0:8", ["const:200:8"]]
+ 007fc2f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fc2f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fc2f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fc298 bytes 29c10491
+ 007fc2f0 bytes 29010891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6db19d8aea2402aa900c3e84bc3b3d05"></a>

### [`007fc2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc2ac.md) → [`007fc304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc304.md) FUN_007fc304

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fc328",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc2d0",
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
      "007fc328",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fc328",
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

- 旧版 [`007fc2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc2ac.md#insn-007fc2d0) · [`007fc2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc2ac.md#insn-007fc2dc)
- 新版 `007fc328`（命令位置の公開資料なし） · `007fc334`（命令位置の公開資料なし）

~~~diff
- 007fc2d0 ["INT_ADD", "register:40f0:8", ["const:7fc2d0:8", "const:4:8"]]
- 007fc2d0 ["CALL", null, ["ram:47acf4:8"]]
+ 007fc328 ["INT_ADD", "register:40f0:8", ["const:7fc328:8", "const:4:8"]]
+ 007fc328 ["CALL", null, ["ram:47ad34:8"]]
- 007fc2d0 bytes 89faf197
+ 007fc328 bytes 83faf197
- 007fc2dc ["INT_ADD", "register:40f0:8", ["const:7fc2dc:8", "const:4:8"]]
- 007fc2dc ["CALL", null, ["callee:0047ce14:8"]]
+ 007fc334 ["INT_ADD", "register:40f0:8", ["const:7fc334:8", "const:4:8"]]
+ 007fc334 ["CALL", null, ["callee:0047ce14:8"]]
- 007fc2dc bytes be02f297
+ 007fc334 bytes b802f297
~~~


<a id="compare-e41aa405c8a032e7a4ad8e845ce524d6"></a>

### [`007fc320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc320.md) → [`007fc378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc378.md) FUN_007fc378

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fc39c",
      "incomplete_value": false,
      "site": "007fc39c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc344",
      "incomplete_value": false,
      "site": "007fc344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "007fc39c",
      "DATA",
      [
        "storage",
        "00c7d1b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc39c",
      "DATA",
      [
        "storage",
        "00c7d280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc320.md#insn-007fc334) · [`007fc340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc320.md#insn-007fc340)
- 新版 `007fc38c`（命令位置の公開資料なし） · `007fc398`（命令位置の公開資料なし）

~~~diff
- 007fc334 ["INT_ADD", "register:40f0:8", ["const:7fc334:8", "const:4:8"]]
- 007fc334 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fc38c ["INT_ADD", "register:40f0:8", ["const:7fc38c:8", "const:4:8"]]
+ 007fc38c ["CALL", null, ["callee:00c57f60:8"]]
- 007fc334 bytes d76e1194
+ 007fc38c bytes f56e1194
- 007fc340 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 007fc340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc398 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 007fc398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc340 bytes 08c10691
+ 007fc398 bytes 08010a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44bba2fac424e978562abf87e1b0f860"></a>

### [`007fc354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc354.md) → [`007fc3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc3ac.md) FUN_007fc3ac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fc3b8",
      "incomplete_value": false,
      "site": "007fc3b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc360",
      "incomplete_value": false,
      "site": "007fc360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007fc3b8",
      "DATA",
      [
        "storage",
        "00c7d1b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc3b8",
      "DATA",
      [
        "storage",
        "00c7d280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc354.md#insn-007fc35c)
- 新版 `007fc3b4`（命令位置の公開資料なし）

~~~diff
- 007fc35c ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 007fc35c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fc35c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fc35c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fc3b4 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 007fc3b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fc3b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fc3b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fc35c bytes 29c10691
+ 007fc3b4 bytes 29010a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9333319641f66cfa90cfe46215c348af"></a>

### [`007fc370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc370.md) → [`007fc3c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc3c8.md) FUN_007fc3c8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fc3ec",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc394",
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
      "007fc3ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fc3ec",
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

- 旧版 [`007fc394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc370.md#insn-007fc394) · [`007fc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc370.md#insn-007fc3a0)
- 新版 `007fc3ec`（命令位置の公開資料なし） · `007fc3f8`（命令位置の公開資料なし）

~~~diff
- 007fc394 ["INT_ADD", "register:40f0:8", ["const:7fc394:8", "const:4:8"]]
- 007fc394 ["CALL", null, ["ram:47acf4:8"]]
+ 007fc3ec ["INT_ADD", "register:40f0:8", ["const:7fc3ec:8", "const:4:8"]]
+ 007fc3ec ["CALL", null, ["ram:47ad34:8"]]
- 007fc394 bytes 58faf197
+ 007fc3ec bytes 52faf197
- 007fc3a0 ["INT_ADD", "register:40f0:8", ["const:7fc3a0:8", "const:4:8"]]
- 007fc3a0 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fc3f8 ["INT_ADD", "register:40f0:8", ["const:7fc3f8:8", "const:4:8"]]
+ 007fc3f8 ["CALL", null, ["callee:0047ce14:8"]]
- 007fc3a0 bytes 8d02f297
+ 007fc3f8 bytes 8702f297
~~~


<a id="compare-c6c8a93e0b68067c5390e18fe97740d2"></a>

### [`007fc3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc3e4.md) → [`007fc43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc43c.md) FUN_007fc43c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fc450",
      "incomplete_value": false,
      "site": "007fc454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc3f8",
      "incomplete_value": false,
      "site": "007fc3fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "007fc454",
      "DATA",
      [
        "storage",
        "00c7d230",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc454",
      "DATA",
      [
        "storage",
        "00c7d300",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc3e4.md#insn-007fc3f0) · [`007fc3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc3e4.md#insn-007fc3f8)
- 新版 `007fc448`（命令位置の公開資料なし） · `007fc450`（命令位置の公開資料なし）

~~~diff
- 007fc3f0 ["INT_ADD", "register:40f0:8", ["const:7fc3f0:8", "const:4:8"]]
- 007fc3f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fc448 ["INT_ADD", "register:40f0:8", ["const:7fc448:8", "const:4:8"]]
+ 007fc448 ["CALL", null, ["callee:00c57f60:8"]]
- 007fc3f0 bytes a86e1194
+ 007fc448 bytes c66e1194
- 007fc3f8 ["COPY", "tmp:0:8", ["const:230:8"]]
- 007fc3f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc3f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc3f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc450 ["COPY", "tmp:0:8", ["const:300:8"]]
+ 007fc450 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc450 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc450 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc3f8 bytes 08c10891
+ 007fc450 bytes 08010c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-329de62f2aad7c2563e527a8bb05642b"></a>

### [`007fc408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc408.md) → [`007fc460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc460.md) FUN_007fc460

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fc464",
      "incomplete_value": false,
      "site": "007fc468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc40c",
      "incomplete_value": false,
      "site": "007fc410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "007fc468",
      "DATA",
      [
        "storage",
        "00c7d230",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc468",
      "DATA",
      [
        "storage",
        "00c7d300",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc408.md#insn-007fc40c)
- 新版 `007fc464`（命令位置の公開資料なし）

~~~diff
- 007fc40c ["COPY", "tmp:0:8", ["const:230:8"]]
- 007fc40c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc40c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc40c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc464 ["COPY", "tmp:0:8", ["const:300:8"]]
+ 007fc464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc40c bytes 08c10891
+ 007fc464 bytes 08010c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2214388974df3225f16e66f222e11c3b"></a>

### [`007fc420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc420.md) → [`007fc478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc478.md) FUN_007fc478

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fc49c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc444",
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
      "007fc49c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fc49c",
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

- 旧版 [`007fc444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc420.md#insn-007fc444) · [`007fc450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc420.md#insn-007fc450)
- 新版 `007fc49c`（命令位置の公開資料なし） · `007fc4a8`（命令位置の公開資料なし）

~~~diff
- 007fc444 ["INT_ADD", "register:40f0:8", ["const:7fc444:8", "const:4:8"]]
- 007fc444 ["CALL", null, ["ram:47acf4:8"]]
+ 007fc49c ["INT_ADD", "register:40f0:8", ["const:7fc49c:8", "const:4:8"]]
+ 007fc49c ["CALL", null, ["ram:47ad34:8"]]
- 007fc444 bytes 2cfaf197
+ 007fc49c bytes 26faf197
- 007fc450 ["INT_ADD", "register:40f0:8", ["const:7fc450:8", "const:4:8"]]
- 007fc450 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fc4a8 ["INT_ADD", "register:40f0:8", ["const:7fc4a8:8", "const:4:8"]]
+ 007fc4a8 ["CALL", null, ["callee:0047ce14:8"]]
- 007fc450 bytes 6102f297
+ 007fc4a8 bytes 5b02f297
~~~


<a id="compare-3aab4c011470899c8bc7a672aab13cc5"></a>

### [`007fc494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc494.md) → [`007fc4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc4ec.md) FUN_007fc4ec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fc510",
      "incomplete_value": false,
      "site": "007fc510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc4b8",
      "incomplete_value": false,
      "site": "007fc4b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "007fc510",
      "DATA",
      [
        "storage",
        "00c7d2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc510",
      "DATA",
      [
        "storage",
        "00c7d380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc494.md#insn-007fc4a8) · [`007fc4b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc494.md#insn-007fc4b4)
- 新版 `007fc500`（命令位置の公開資料なし） · `007fc50c`（命令位置の公開資料なし）

~~~diff
- 007fc4a8 ["INT_ADD", "register:40f0:8", ["const:7fc4a8:8", "const:4:8"]]
- 007fc4a8 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fc500 ["INT_ADD", "register:40f0:8", ["const:7fc500:8", "const:4:8"]]
+ 007fc500 ["CALL", null, ["callee:00c57f60:8"]]
- 007fc4a8 bytes 7a6e1194
+ 007fc500 bytes 986e1194
- 007fc4b4 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 007fc4b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc4b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc4b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc50c ["COPY", "tmp:0:8", ["const:380:8"]]
+ 007fc50c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc50c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc50c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc4b4 bytes 08c10a91
+ 007fc50c bytes 08010e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f2b5d8f72de8149b501305de4d5cbc6"></a>

### [`007fc4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc4c8.md) → [`007fc520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc520.md) FUN_007fc520

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fc52c",
      "incomplete_value": false,
      "site": "007fc52c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc4d4",
      "incomplete_value": false,
      "site": "007fc4d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "007fc52c",
      "DATA",
      [
        "storage",
        "00c7d2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc52c",
      "DATA",
      [
        "storage",
        "00c7d380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc4c8.md#insn-007fc4d0)
- 新版 `007fc528`（命令位置の公開資料なし）

~~~diff
- 007fc4d0 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 007fc4d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fc4d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fc4d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fc528 ["COPY", "tmp:0:8", ["const:380:8"]]
+ 007fc528 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fc528 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fc528 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fc4d0 bytes 29c10a91
+ 007fc528 bytes 29010e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7f2a3eabe5fcb642577fc610621032e"></a>

### [`007fc4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc4e4.md) → [`007fc53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc53c.md) FUN_007fc53c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

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
      "site": "007fc564",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc50c",
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
      "007fc564",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fc564",
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

- 旧版 [`007fc50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc4e4.md#insn-007fc50c) · [`007fc518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc4e4.md#insn-007fc518)
- 新版 `007fc564`（命令位置の公開資料なし） · `007fc570`（命令位置の公開資料なし）

~~~diff
- 007fc50c ["INT_ADD", "register:40f0:8", ["const:7fc50c:8", "const:4:8"]]
- 007fc50c ["CALL", null, ["ram:47acf4:8"]]
+ 007fc564 ["INT_ADD", "register:40f0:8", ["const:7fc564:8", "const:4:8"]]
+ 007fc564 ["CALL", null, ["ram:47ad34:8"]]
- 007fc50c bytes faf9f197
+ 007fc564 bytes f4f9f197
- 007fc518 ["INT_ADD", "register:40f0:8", ["const:7fc518:8", "const:4:8"]]
- 007fc518 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fc570 ["INT_ADD", "register:40f0:8", ["const:7fc570:8", "const:4:8"]]
+ 007fc570 ["CALL", null, ["callee:0047ce14:8"]]
- 007fc518 bytes 2f02f297
+ 007fc570 bytes 2902f297
~~~


<a id="compare-c77ed40fe5fb02ff7b543d5c7a79f355"></a>

### [`007fc5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5a0.md) → [`007fc5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc5f8.md) FUN_007fc5f8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fc60c",
      "incomplete_value": false,
      "site": "007fc610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc5b4",
      "incomplete_value": false,
      "site": "007fc5b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:330:8"
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
      "007fc610",
      "DATA",
      [
        "storage",
        "00c7d330",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc610",
      "DATA",
      [
        "storage",
        "00c7d400",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5a0.md#insn-007fc5ac) · [`007fc5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5a0.md#insn-007fc5b4)
- 新版 `007fc604`（命令位置の公開資料なし） · `007fc60c`（命令位置の公開資料なし）

~~~diff
- 007fc5ac ["INT_ADD", "register:40f0:8", ["const:7fc5ac:8", "const:4:8"]]
- 007fc5ac ["CALL", null, ["callee:00c57f60:8"]]
+ 007fc604 ["INT_ADD", "register:40f0:8", ["const:7fc604:8", "const:4:8"]]
+ 007fc604 ["CALL", null, ["callee:00c57f60:8"]]
- 007fc5ac bytes 396e1194
+ 007fc604 bytes 576e1194
- 007fc5b4 ["COPY", "tmp:0:8", ["const:330:8"]]
- 007fc5b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc5b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc5b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc60c ["COPY", "tmp:0:8", ["const:400:8"]]
+ 007fc60c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc60c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc60c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc5b4 bytes 08c10c91
+ 007fc60c bytes 08011091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d9e7eb4f7bb749e5870f5b1ef847eb1"></a>

### [`007fc5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5c4.md) → [`007fc61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc61c.md) FUN_007fc61c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fc620",
      "incomplete_value": false,
      "site": "007fc624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc5c8",
      "incomplete_value": false,
      "site": "007fc5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:330:8"
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
      "007fc624",
      "DATA",
      [
        "storage",
        "00c7d330",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc624",
      "DATA",
      [
        "storage",
        "00c7d400",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5c4.md#insn-007fc5c8)
- 新版 `007fc620`（命令位置の公開資料なし）

~~~diff
- 007fc5c8 ["COPY", "tmp:0:8", ["const:330:8"]]
- 007fc5c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc5c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc5c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc620 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 007fc620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc5c8 bytes 08c10c91
+ 007fc620 bytes 08011091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10609605e24d8b1eec96cd2a3b1c43f0"></a>

### [`007fc5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5dc.md) → [`007fc634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc634.md) FUN_007fc634

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

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
      "site": "007fc658",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc600",
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
      "007fc658",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fc658",
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

- 旧版 [`007fc600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5dc.md#insn-007fc600) · [`007fc60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5dc.md#insn-007fc60c) · [`007fc62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5dc.md#insn-007fc62c)
- 新版 `007fc658`（命令位置の公開資料なし） · `007fc664`（命令位置の公開資料なし） · `007fc684`（命令位置の公開資料なし）

~~~diff
- 007fc600 ["INT_ADD", "register:40f0:8", ["const:7fc600:8", "const:4:8"]]
- 007fc600 ["CALL", null, ["ram:47acf4:8"]]
+ 007fc658 ["INT_ADD", "register:40f0:8", ["const:7fc658:8", "const:4:8"]]
+ 007fc658 ["CALL", null, ["ram:47ad34:8"]]
- 007fc600 bytes bdf9f197
+ 007fc658 bytes b7f9f197
- 007fc60c ["INT_ADD", "register:40f0:8", ["const:7fc60c:8", "const:4:8"]]
- 007fc60c ["CALL", null, ["callee:0047ce14:8"]]
+ 007fc664 ["INT_ADD", "register:40f0:8", ["const:7fc664:8", "const:4:8"]]
+ 007fc664 ["CALL", null, ["callee:0047ce14:8"]]
- 007fc60c bytes f201f297
+ 007fc664 bytes ec01f297
- 007fc62c ["INT_ADD", "register:40f0:8", ["const:7fc62c:8", "const:4:8"]]
- 007fc62c ["CALL", null, ["callee:00851550:8"]]
+ 007fc684 ["INT_ADD", "register:40f0:8", ["const:7fc684:8", "const:4:8"]]
+ 007fc684 ["CALL", null, ["callee:00851550:8"]]
- 007fc62c bytes b3530194
+ 007fc684 bytes b3530194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caf37bfbb192a9f9957caa352caae0e7"></a>

### [`007fc680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc680.md) → [`007fc6d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc6d8.md) FUN_007fc6d8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fc6ec",
      "incomplete_value": false,
      "site": "007fc6f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc694",
      "incomplete_value": false,
      "site": "007fc698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "007fc6f0",
      "DATA",
      [
        "storage",
        "00c7d3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc6f0",
      "DATA",
      [
        "storage",
        "00c7d480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc680.md#insn-007fc68c) · [`007fc694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc680.md#insn-007fc694)
- 新版 `007fc6e4`（命令位置の公開資料なし） · `007fc6ec`（命令位置の公開資料なし）

~~~diff
- 007fc68c ["INT_ADD", "register:40f0:8", ["const:7fc68c:8", "const:4:8"]]
- 007fc68c ["CALL", null, ["callee:00c57f60:8"]]
+ 007fc6e4 ["INT_ADD", "register:40f0:8", ["const:7fc6e4:8", "const:4:8"]]
+ 007fc6e4 ["CALL", null, ["callee:00c57f60:8"]]
- 007fc68c bytes 016e1194
+ 007fc6e4 bytes 1f6e1194
- 007fc694 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 007fc694 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc694 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc694 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc6ec ["COPY", "tmp:0:8", ["const:480:8"]]
+ 007fc6ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc6ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc6ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc694 bytes 08c10e91
+ 007fc6ec bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd608ac84e932441968d48a5840ce7bc"></a>

### [`007fc6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc6a4.md) → [`007fc6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc6fc.md) FUN_007fc6fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fc700",
      "incomplete_value": false,
      "site": "007fc704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc6a8",
      "incomplete_value": false,
      "site": "007fc6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "007fc704",
      "DATA",
      [
        "storage",
        "00c7d3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc704",
      "DATA",
      [
        "storage",
        "00c7d480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc6a4.md#insn-007fc6a8)
- 新版 `007fc700`（命令位置の公開資料なし）

~~~diff
- 007fc6a8 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 007fc6a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc6a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc6a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc700 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 007fc700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc6a8 bytes 08c10e91
+ 007fc700 bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bccc972a0bec08eef9d48a509154062f"></a>

### [`007fc6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc6bc.md) → [`007fc714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc714.md) FUN_007fc714

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.28% / 新版 98.28%

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
      "site": "007fc738",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc6e0",
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
      "007fc738",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fc738",
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

- 旧版 [`007fc6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc6bc.md#insn-007fc6e0) · [`007fc738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc6bc.md#insn-007fc738) · [`007fc6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc6bc.md#insn-007fc6ec)
- 新版 `007fc738`（命令位置の公開資料なし） · `007fc790`（命令位置の公開資料なし） · `007fc744`（命令位置の公開資料なし）

~~~diff
- 007fc6e0 ["INT_ADD", "register:40f0:8", ["const:7fc6e0:8", "const:4:8"]]
- 007fc6e0 ["CALL", null, ["ram:47acf4:8"]]
+ 007fc738 ["INT_ADD", "register:40f0:8", ["const:7fc738:8", "const:4:8"]]
+ 007fc738 ["CALL", null, ["ram:47ad34:8"]]
- 007fc6e0 bytes 85f9f197
+ 007fc738 bytes 7ff9f197
- 007fc738 ["INT_ADD", "register:40f0:8", ["const:7fc738:8", "const:4:8"]]
- 007fc738 ["CALL", null, ["callee:008b7a20:8"]]
+ 007fc790 ["INT_ADD", "register:40f0:8", ["const:7fc790:8", "const:4:8"]]
+ 007fc790 ["CALL", null, ["callee:008b7a20:8"]]
- 007fc738 bytes a4ec0294
+ 007fc790 bytes a4ec0294
- 007fc6ec ["INT_ADD", "register:40f0:8", ["const:7fc6ec:8", "const:4:8"]]
- 007fc6ec ["CALL", null, ["callee:0047ce14:8"]]
+ 007fc744 ["INT_ADD", "register:40f0:8", ["const:7fc744:8", "const:4:8"]]
+ 007fc744 ["CALL", null, ["callee:0047ce14:8"]]
- 007fc6ec bytes ba01f297
+ 007fc744 bytes b401f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad42bcfe3577148ea4d7eeeb0927d19e"></a>

### [`007fc7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc7d0.md) → [`007fc828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc828.md) FUN_007fc828

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fc83c",
      "incomplete_value": false,
      "site": "007fc840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc7e4",
      "incomplete_value": false,
      "site": "007fc7e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:430:8"
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
      "007fc840",
      "DATA",
      [
        "storage",
        "00c7d430",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc840",
      "DATA",
      [
        "storage",
        "00c7d500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc7dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc7d0.md#insn-007fc7dc) · [`007fc7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc7d0.md#insn-007fc7e4)
- 新版 `007fc834`（命令位置の公開資料なし） · `007fc83c`（命令位置の公開資料なし）

~~~diff
- 007fc7dc ["INT_ADD", "register:40f0:8", ["const:7fc7dc:8", "const:4:8"]]
- 007fc7dc ["CALL", null, ["callee:00c57f60:8"]]
+ 007fc834 ["INT_ADD", "register:40f0:8", ["const:7fc834:8", "const:4:8"]]
+ 007fc834 ["CALL", null, ["callee:00c57f60:8"]]
- 007fc7dc bytes ad6d1194
+ 007fc834 bytes cb6d1194
- 007fc7e4 ["COPY", "tmp:0:8", ["const:430:8"]]
- 007fc7e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc7e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc7e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc83c ["COPY", "tmp:0:8", ["const:500:8"]]
+ 007fc83c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc83c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc83c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc7e4 bytes 08c11091
+ 007fc83c bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4b9d78b8d00a8bcc843fbc43c5527aa"></a>

### [`007fc7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc7f4.md) → [`007fc84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc84c.md) FUN_007fc84c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fc850",
      "incomplete_value": false,
      "site": "007fc854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc7f8",
      "incomplete_value": false,
      "site": "007fc7fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007fc854",
      "DATA",
      [
        "storage",
        "00c7d430",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc854",
      "DATA",
      [
        "storage",
        "00c7d500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc7f4.md#insn-007fc7f8)
- 新版 `007fc850`（命令位置の公開資料なし）

~~~diff
- 007fc7f8 ["COPY", "tmp:0:8", ["const:430:8"]]
- 007fc7f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc7f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc7f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc850 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 007fc850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc7f8 bytes 08c11091
+ 007fc850 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ce720da19ec28ae56691b46969b3ecd"></a>

### [`007fc80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc80c.md) → [`007fc864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc864.md) FUN_007fc864

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fc888",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc830",
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
      "007fc888",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fc888",
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

- 旧版 [`007fc830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc80c.md#insn-007fc830) · [`007fc83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc80c.md#insn-007fc83c)
- 新版 `007fc888`（命令位置の公開資料なし） · `007fc894`（命令位置の公開資料なし）

~~~diff
- 007fc830 ["INT_ADD", "register:40f0:8", ["const:7fc830:8", "const:4:8"]]
- 007fc830 ["CALL", null, ["ram:47acf4:8"]]
+ 007fc888 ["INT_ADD", "register:40f0:8", ["const:7fc888:8", "const:4:8"]]
+ 007fc888 ["CALL", null, ["ram:47ad34:8"]]
- 007fc830 bytes 31f9f197
+ 007fc888 bytes 2bf9f197
- 007fc83c ["INT_ADD", "register:40f0:8", ["const:7fc83c:8", "const:4:8"]]
- 007fc83c ["CALL", null, ["callee:0047ce14:8"]]
+ 007fc894 ["INT_ADD", "register:40f0:8", ["const:7fc894:8", "const:4:8"]]
+ 007fc894 ["CALL", null, ["callee:0047ce14:8"]]
- 007fc83c bytes 6601f297
+ 007fc894 bytes 6001f297
~~~


<a id="compare-317d3acdb4701ca8563a6fd0103065d9"></a>

### [`007fc880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc880.md) → [`007fc8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc8d8.md) FUN_007fc8d8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fc8ec",
      "incomplete_value": false,
      "site": "007fc8f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc894",
      "incomplete_value": false,
      "site": "007fc898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "007fc8f0",
      "DATA",
      [
        "storage",
        "00c7d4b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc8f0",
      "DATA",
      [
        "storage",
        "00c7d580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc880.md#insn-007fc88c) · [`007fc894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc880.md#insn-007fc894)
- 新版 `007fc8e4`（命令位置の公開資料なし） · `007fc8ec`（命令位置の公開資料なし）

~~~diff
- 007fc88c ["INT_ADD", "register:40f0:8", ["const:7fc88c:8", "const:4:8"]]
- 007fc88c ["CALL", null, ["callee:00c57f60:8"]]
+ 007fc8e4 ["INT_ADD", "register:40f0:8", ["const:7fc8e4:8", "const:4:8"]]
+ 007fc8e4 ["CALL", null, ["callee:00c57f60:8"]]
- 007fc88c bytes 816d1194
+ 007fc8e4 bytes 9f6d1194
- 007fc894 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 007fc894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc8ec ["COPY", "tmp:0:8", ["const:580:8"]]
+ 007fc8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc894 bytes 08c11291
+ 007fc8ec bytes 08011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-257fe10a7546e484c8952cb8adaee365"></a>

### [`007fc8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc8a4.md) → [`007fc8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc8fc.md) FUN_007fc8fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fc900",
      "incomplete_value": false,
      "site": "007fc904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc8a8",
      "incomplete_value": false,
      "site": "007fc8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007fc904",
      "DATA",
      [
        "storage",
        "00c7d4b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc904",
      "DATA",
      [
        "storage",
        "00c7d580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc8a4.md#insn-007fc8a8)
- 新版 `007fc900`（命令位置の公開資料なし）

~~~diff
- 007fc8a8 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 007fc8a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc8a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc8a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc900 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 007fc900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc8a8 bytes 08c11291
+ 007fc900 bytes 08011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e7f1eb67d1d747f2405a0fe37c9dea3"></a>

### [`007fc8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc8bc.md) → [`007fc914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc914.md) FUN_007fc914

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fc938",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc8e0",
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
      "007fc938",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fc938",
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

- 旧版 [`007fc8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc8bc.md#insn-007fc8e0) · [`007fc8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc8bc.md#insn-007fc8ec)
- 新版 `007fc938`（命令位置の公開資料なし） · `007fc944`（命令位置の公開資料なし）

~~~diff
- 007fc8e0 ["INT_ADD", "register:40f0:8", ["const:7fc8e0:8", "const:4:8"]]
- 007fc8e0 ["CALL", null, ["ram:47acf4:8"]]
+ 007fc938 ["INT_ADD", "register:40f0:8", ["const:7fc938:8", "const:4:8"]]
+ 007fc938 ["CALL", null, ["ram:47ad34:8"]]
- 007fc8e0 bytes 05f9f197
+ 007fc938 bytes fff8f197
- 007fc8ec ["INT_ADD", "register:40f0:8", ["const:7fc8ec:8", "const:4:8"]]
- 007fc8ec ["CALL", null, ["callee:0047ce14:8"]]
+ 007fc944 ["INT_ADD", "register:40f0:8", ["const:7fc944:8", "const:4:8"]]
+ 007fc944 ["CALL", null, ["callee:0047ce14:8"]]
- 007fc8ec bytes 3a01f297
+ 007fc944 bytes 3401f297
~~~


<a id="compare-c449606e01b4aa658548962f1e89fc03"></a>

### [`007fc930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc930.md) → [`007fc988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc988.md) FUN_007fc988

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fc99c",
      "incomplete_value": false,
      "site": "007fc9a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc944",
      "incomplete_value": false,
      "site": "007fc948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:530:8"
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
      "007fc9a0",
      "DATA",
      [
        "storage",
        "00c7d530",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc9a0",
      "DATA",
      [
        "storage",
        "00c7d600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc930.md#insn-007fc93c) · [`007fc944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc930.md#insn-007fc944)
- 新版 `007fc994`（命令位置の公開資料なし） · `007fc99c`（命令位置の公開資料なし）

~~~diff
- 007fc93c ["INT_ADD", "register:40f0:8", ["const:7fc93c:8", "const:4:8"]]
- 007fc93c ["CALL", null, ["callee:00c57f60:8"]]
+ 007fc994 ["INT_ADD", "register:40f0:8", ["const:7fc994:8", "const:4:8"]]
+ 007fc994 ["CALL", null, ["callee:00c57f60:8"]]
- 007fc93c bytes 556d1194
+ 007fc994 bytes 736d1194
- 007fc944 ["COPY", "tmp:0:8", ["const:530:8"]]
- 007fc944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc99c ["COPY", "tmp:0:8", ["const:600:8"]]
+ 007fc99c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc99c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc99c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc944 bytes 08c11491
+ 007fc99c bytes 08011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8c641b4891be18fc2f6093eed043571"></a>

### [`007fc954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc954.md) → [`007fc9ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc9ac.md) FUN_007fc9ac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fc9b0",
      "incomplete_value": false,
      "site": "007fc9b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc958",
      "incomplete_value": false,
      "site": "007fc95c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:530:8"
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
      "007fc9b4",
      "DATA",
      [
        "storage",
        "00c7d530",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc9b4",
      "DATA",
      [
        "storage",
        "00c7d600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc954.md#insn-007fc958)
- 新版 `007fc9b0`（命令位置の公開資料なし）

~~~diff
- 007fc958 ["COPY", "tmp:0:8", ["const:530:8"]]
- 007fc958 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc958 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc958 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc9b0 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 007fc9b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc9b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc9b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc958 bytes 08c11491
+ 007fc9b0 bytes 08011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a764d1228e95cee15d840fe7910b8920"></a>

### [`007fc96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc96c.md) → [`007fc9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fc9c4.md) FUN_007fc9c4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fc9e8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc990",
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
      "007fc9e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fc9e8",
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

- 旧版 [`007fc990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc96c.md#insn-007fc990) · [`007fc99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc96c.md#insn-007fc99c)
- 新版 `007fc9e8`（命令位置の公開資料なし） · `007fc9f4`（命令位置の公開資料なし）

~~~diff
- 007fc990 ["INT_ADD", "register:40f0:8", ["const:7fc990:8", "const:4:8"]]
- 007fc990 ["CALL", null, ["ram:47acf4:8"]]
+ 007fc9e8 ["INT_ADD", "register:40f0:8", ["const:7fc9e8:8", "const:4:8"]]
+ 007fc9e8 ["CALL", null, ["ram:47ad34:8"]]
- 007fc990 bytes d9f8f197
+ 007fc9e8 bytes d3f8f197
- 007fc99c ["INT_ADD", "register:40f0:8", ["const:7fc99c:8", "const:4:8"]]
- 007fc99c ["CALL", null, ["callee:0047ce14:8"]]
+ 007fc9f4 ["INT_ADD", "register:40f0:8", ["const:7fc9f4:8", "const:4:8"]]
+ 007fc9f4 ["CALL", null, ["callee:0047ce14:8"]]
- 007fc99c bytes 0e01f297
+ 007fc9f4 bytes 0801f297
~~~


<a id="compare-6b8f951e2378ecf94993082790dc7856"></a>

### [`007fc9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc9e0.md) → [`007fca38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fca38.md) FUN_007fca38

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fca4c",
      "incomplete_value": false,
      "site": "007fca50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc9f4",
      "incomplete_value": false,
      "site": "007fc9f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "007fca50",
      "DATA",
      [
        "storage",
        "00c7d5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fca50",
      "DATA",
      [
        "storage",
        "00c7d680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc9e0.md#insn-007fc9ec) · [`007fc9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc9e0.md#insn-007fc9f4)
- 新版 `007fca44`（命令位置の公開資料なし） · `007fca4c`（命令位置の公開資料なし）

~~~diff
- 007fc9ec ["INT_ADD", "register:40f0:8", ["const:7fc9ec:8", "const:4:8"]]
- 007fc9ec ["CALL", null, ["callee:00c57f60:8"]]
+ 007fca44 ["INT_ADD", "register:40f0:8", ["const:7fca44:8", "const:4:8"]]
+ 007fca44 ["CALL", null, ["callee:00c57f60:8"]]
- 007fc9ec bytes 296d1194
+ 007fca44 bytes 476d1194
- 007fc9f4 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 007fc9f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc9f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc9f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fca4c ["COPY", "tmp:0:8", ["const:680:8"]]
+ 007fca4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fca4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fca4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc9f4 bytes 08c11691
+ 007fca4c bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcf40883bd384505908c06f80c3aaf41"></a>

### [`007fca04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca04.md) → [`007fca5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fca5c.md) FUN_007fca5c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fca60",
      "incomplete_value": false,
      "site": "007fca64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fca08",
      "incomplete_value": false,
      "site": "007fca0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "007fca64",
      "DATA",
      [
        "storage",
        "00c7d5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fca64",
      "DATA",
      [
        "storage",
        "00c7d680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fca08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca04.md#insn-007fca08)
- 新版 `007fca60`（命令位置の公開資料なし）

~~~diff
- 007fca08 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 007fca08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fca08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fca08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fca60 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 007fca60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fca60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fca60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fca08 bytes 08c11691
+ 007fca60 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f57081e274ec0665e36f6a333cd26c26"></a>

### [`007fca1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca1c.md) → [`007fca74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fca74.md) FUN_007fca74

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fca98",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fca40",
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
      "007fca98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fca98",
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

- 旧版 [`007fca40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca1c.md#insn-007fca40) · [`007fca4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca1c.md#insn-007fca4c)
- 新版 `007fca98`（命令位置の公開資料なし） · `007fcaa4`（命令位置の公開資料なし）

~~~diff
- 007fca40 ["INT_ADD", "register:40f0:8", ["const:7fca40:8", "const:4:8"]]
- 007fca40 ["CALL", null, ["ram:47acf4:8"]]
+ 007fca98 ["INT_ADD", "register:40f0:8", ["const:7fca98:8", "const:4:8"]]
+ 007fca98 ["CALL", null, ["ram:47ad34:8"]]
- 007fca40 bytes adf8f197
+ 007fca98 bytes a7f8f197
- 007fca4c ["INT_ADD", "register:40f0:8", ["const:7fca4c:8", "const:4:8"]]
- 007fca4c ["CALL", null, ["callee:0047ce14:8"]]
+ 007fcaa4 ["INT_ADD", "register:40f0:8", ["const:7fcaa4:8", "const:4:8"]]
+ 007fcaa4 ["CALL", null, ["callee:0047ce14:8"]]
- 007fca4c bytes e200f297
+ 007fcaa4 bytes dc00f297
~~~


<a id="compare-988e244b932c495803b2e07c4af048bf"></a>

### [`007fca90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca90.md) → [`007fcae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcae8.md) FUN_007fcae8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fcb0c",
      "incomplete_value": false,
      "site": "007fcb0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fcab4",
      "incomplete_value": false,
      "site": "007fcab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "007fcb0c",
      "DATA",
      [
        "storage",
        "00c7d630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fcb0c",
      "DATA",
      [
        "storage",
        "00c7d700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fcaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca90.md#insn-007fcaa4) · [`007fcab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca90.md#insn-007fcab0)
- 新版 `007fcafc`（命令位置の公開資料なし） · `007fcb08`（命令位置の公開資料なし）

~~~diff
- 007fcaa4 ["INT_ADD", "register:40f0:8", ["const:7fcaa4:8", "const:4:8"]]
- 007fcaa4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fcafc ["INT_ADD", "register:40f0:8", ["const:7fcafc:8", "const:4:8"]]
+ 007fcafc ["CALL", null, ["callee:00c57f60:8"]]
- 007fcaa4 bytes fb6c1194
+ 007fcafc bytes 196d1194
- 007fcab0 ["COPY", "tmp:0:8", ["const:630:8"]]
- 007fcab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fcab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fcab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fcb08 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 007fcb08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcb08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcb08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fcab0 bytes 08c11891
+ 007fcb08 bytes 08011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f187851ed5bd454909f53fea06eca2a"></a>

### [`007fcac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcac4.md) → [`007fcb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcb1c.md) FUN_007fcb1c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fcb28",
      "incomplete_value": false,
      "site": "007fcb28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fcad0",
      "incomplete_value": false,
      "site": "007fcad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "007fcb28",
      "DATA",
      [
        "storage",
        "00c7d630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fcb28",
      "DATA",
      [
        "storage",
        "00c7d700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fcacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcac4.md#insn-007fcacc)
- 新版 `007fcb24`（命令位置の公開資料なし）

~~~diff
- 007fcacc ["COPY", "tmp:0:8", ["const:630:8"]]
- 007fcacc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fcacc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fcacc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fcb24 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 007fcb24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fcb24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fcb24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fcacc bytes 29c11891
+ 007fcb24 bytes 29011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70cec4e5f18771082ae22b40e8ff9621"></a>

### [`007fcae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcae0.md) → [`007fcb38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcb38.md) FUN_007fcb38

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

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
      "site": "007fcb60",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fcb08",
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
      "007fcb60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fcb60",
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

- 旧版 [`007fcb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcae0.md#insn-007fcb08) · [`007fcb60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcae0.md#insn-007fcb60) · [`007fcb14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcae0.md#insn-007fcb14)
- 新版 `007fcb60`（命令位置の公開資料なし） · `007fcbb8`（命令位置の公開資料なし） · `007fcb6c`（命令位置の公開資料なし）

~~~diff
- 007fcb08 ["INT_ADD", "register:40f0:8", ["const:7fcb08:8", "const:4:8"]]
- 007fcb08 ["CALL", null, ["ram:47acf4:8"]]
+ 007fcb60 ["INT_ADD", "register:40f0:8", ["const:7fcb60:8", "const:4:8"]]
+ 007fcb60 ["CALL", null, ["ram:47ad34:8"]]
- 007fcb08 bytes 7bf8f197
+ 007fcb60 bytes 75f8f197
- 007fcb60 ["INT_ADD", "register:40f0:8", ["const:7fcb60:8", "const:4:8"]]
- 007fcb60 ["CALL", null, ["callee:00851550:8"]]
+ 007fcbb8 ["INT_ADD", "register:40f0:8", ["const:7fcbb8:8", "const:4:8"]]
+ 007fcbb8 ["CALL", null, ["callee:00851550:8"]]
- 007fcb60 bytes 66520194
+ 007fcbb8 bytes 66520194
- 007fcb14 ["INT_ADD", "register:40f0:8", ["const:7fcb14:8", "const:4:8"]]
- 007fcb14 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fcb6c ["INT_ADD", "register:40f0:8", ["const:7fcb6c:8", "const:4:8"]]
+ 007fcb6c ["CALL", null, ["callee:0047ce14:8"]]
- 007fcb14 bytes b000f297
+ 007fcb6c bytes aa00f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4aeebc57fc0af42738b10a5bb63058b0"></a>

### [`007fcbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcbc8.md) → [`007fcc20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcc20.md) FUN_007fcc20

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fcc40",
      "incomplete_value": false,
      "site": "007fcc44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fcbe8",
      "incomplete_value": false,
      "site": "007fcbec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "007fcc44",
      "DATA",
      [
        "storage",
        "00c7d6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fcc44",
      "DATA",
      [
        "storage",
        "00c7d780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fcbdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcbc8.md#insn-007fcbdc) · [`007fcbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcbc8.md#insn-007fcbe8)
- 新版 `007fcc34`（命令位置の公開資料なし） · `007fcc40`（命令位置の公開資料なし）

~~~diff
- 007fcbdc ["INT_ADD", "register:40f0:8", ["const:7fcbdc:8", "const:4:8"]]
- 007fcbdc ["CALL", null, ["callee:00c57f60:8"]]
+ 007fcc34 ["INT_ADD", "register:40f0:8", ["const:7fcc34:8", "const:4:8"]]
+ 007fcc34 ["CALL", null, ["callee:00c57f60:8"]]
- 007fcbdc bytes ad6c1194
+ 007fcc34 bytes cb6c1194
- 007fcbe8 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 007fcbe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fcbe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fcbe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fcc40 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 007fcc40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcc40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcc40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fcbe8 bytes 08c11a91
+ 007fcc40 bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ee73ab4be6f4fee87a3bf1b5a0a1ea1"></a>

### [`007fcc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcc00.md) → [`007fcc58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcc58.md) FUN_007fcc58

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fcc60",
      "incomplete_value": false,
      "site": "007fcc64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fcc08",
      "incomplete_value": false,
      "site": "007fcc0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "007fcc64",
      "DATA",
      [
        "storage",
        "00c7d6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fcc64",
      "DATA",
      [
        "storage",
        "00c7d780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fcc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcc00.md#insn-007fcc08)
- 新版 `007fcc60`（命令位置の公開資料なし）

~~~diff
- 007fcc08 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 007fcc08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fcc08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fcc08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fcc60 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 007fcc60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fcc60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fcc60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fcc08 bytes 29c11a91
+ 007fcc60 bytes 29011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7442d5cd2cb5571a3bf031e21ae2184"></a>

### [`007fcc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcc20.md) → [`007fcc78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcc78.md) FUN_007fcc78

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

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
      "site": "007fcca0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fcc48",
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
      "007fcca0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fcca0",
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

- 旧版 [`007fcc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcc20.md#insn-007fcc48) · [`007fcca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcc20.md#insn-007fcca0) · [`007fcc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcc20.md#insn-007fcc54)
- 新版 `007fcca0`（命令位置の公開資料なし） · `007fccf8`（命令位置の公開資料なし） · `007fccac`（命令位置の公開資料なし）

~~~diff
- 007fcc48 ["INT_ADD", "register:40f0:8", ["const:7fcc48:8", "const:4:8"]]
- 007fcc48 ["CALL", null, ["ram:47acf4:8"]]
+ 007fcca0 ["INT_ADD", "register:40f0:8", ["const:7fcca0:8", "const:4:8"]]
+ 007fcca0 ["CALL", null, ["ram:47ad34:8"]]
- 007fcc48 bytes 2bf8f197
+ 007fcca0 bytes 25f8f197
- 007fcca0 ["INT_ADD", "register:40f0:8", ["const:7fcca0:8", "const:4:8"]]
- 007fcca0 ["CALL", null, ["callee:00851550:8"]]
+ 007fccf8 ["INT_ADD", "register:40f0:8", ["const:7fccf8:8", "const:4:8"]]
+ 007fccf8 ["CALL", null, ["callee:00851550:8"]]
- 007fcca0 bytes 16520194
+ 007fccf8 bytes 16520194
- 007fcc54 ["INT_ADD", "register:40f0:8", ["const:7fcc54:8", "const:4:8"]]
- 007fcc54 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fccac ["INT_ADD", "register:40f0:8", ["const:7fccac:8", "const:4:8"]]
+ 007fccac ["CALL", null, ["callee:0047ce14:8"]]
- 007fcc54 bytes 6000f297
+ 007fccac bytes 5a00f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58b64749a0a3f1bc0a3e1da1fb007e84"></a>

### [`007fccfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fccfc.md) → [`007fcd54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcd54.md) FUN_007fcd54

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fcd74",
      "incomplete_value": false,
      "site": "007fcd78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fcd1c",
      "incomplete_value": false,
      "site": "007fcd20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "007fcd78",
      "DATA",
      [
        "storage",
        "00c7d730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fcd78",
      "DATA",
      [
        "storage",
        "00c7d800",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fcd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fccfc.md#insn-007fcd10) · [`007fcd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fccfc.md#insn-007fcd1c)
- 新版 `007fcd68`（命令位置の公開資料なし） · `007fcd74`（命令位置の公開資料なし）

~~~diff
- 007fcd10 ["INT_ADD", "register:40f0:8", ["const:7fcd10:8", "const:4:8"]]
- 007fcd10 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fcd68 ["INT_ADD", "register:40f0:8", ["const:7fcd68:8", "const:4:8"]]
+ 007fcd68 ["CALL", null, ["callee:00c57f60:8"]]
- 007fcd10 bytes 606c1194
+ 007fcd68 bytes 7e6c1194
- 007fcd1c ["COPY", "tmp:0:8", ["const:730:8"]]
- 007fcd1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fcd1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fcd1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fcd74 ["COPY", "tmp:0:8", ["const:800:8"]]
+ 007fcd74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcd74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcd74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fcd1c bytes 08c11c91
+ 007fcd74 bytes 08012091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16aee642c9ad8687d38310d716653d32"></a>

### [`007fcd34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcd34.md) → [`007fcd8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcd8c.md) FUN_007fcd8c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fcd94",
      "incomplete_value": false,
      "site": "007fcd98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fcd3c",
      "incomplete_value": false,
      "site": "007fcd40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "007fcd98",
      "DATA",
      [
        "storage",
        "00c7d730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fcd98",
      "DATA",
      [
        "storage",
        "00c7d800",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fcd3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcd34.md#insn-007fcd3c)
- 新版 `007fcd94`（命令位置の公開資料なし）

~~~diff
- 007fcd3c ["COPY", "tmp:0:8", ["const:730:8"]]
- 007fcd3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fcd3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fcd3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fcd94 ["COPY", "tmp:0:8", ["const:800:8"]]
+ 007fcd94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fcd94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fcd94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fcd3c bytes 29c11c91
+ 007fcd94 bytes 29012091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cc40ed378dc97cb0bcdcc2d2611a320"></a>

### [`007fcd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcd54.md) → [`007fcdac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcdac.md) FUN_007fcdac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fcdd0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fcd78",
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
      "007fcdd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fcdd0",
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

- 旧版 [`007fcd78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcd54.md#insn-007fcd78) · [`007fcd84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcd54.md#insn-007fcd84)
- 新版 `007fcdd0`（命令位置の公開資料なし） · `007fcddc`（命令位置の公開資料なし）

~~~diff
- 007fcd78 ["INT_ADD", "register:40f0:8", ["const:7fcd78:8", "const:4:8"]]
- 007fcd78 ["CALL", null, ["ram:47acf4:8"]]
+ 007fcdd0 ["INT_ADD", "register:40f0:8", ["const:7fcdd0:8", "const:4:8"]]
+ 007fcdd0 ["CALL", null, ["ram:47ad34:8"]]
- 007fcd78 bytes dff7f197
+ 007fcdd0 bytes d9f7f197
- 007fcd84 ["INT_ADD", "register:40f0:8", ["const:7fcd84:8", "const:4:8"]]
- 007fcd84 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fcddc ["INT_ADD", "register:40f0:8", ["const:7fcddc:8", "const:4:8"]]
+ 007fcddc ["CALL", null, ["callee:0047ce14:8"]]
- 007fcd84 bytes 1400f297
+ 007fcddc bytes 0e00f297
~~~


<a id="compare-11e664d178adb346e3f4fc85bf7a1160"></a>

### [`007fcdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcdc8.md) → [`007fce20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fce20.md) FUN_007fce20

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fce40",
      "incomplete_value": false,
      "site": "007fce44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fcde8",
      "incomplete_value": false,
      "site": "007fcdec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:7b0:8"
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
      "007fce44",
      "DATA",
      [
        "storage",
        "00c7d7b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fce44",
      "DATA",
      [
        "storage",
        "00c7d880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fcddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcdc8.md#insn-007fcddc) · [`007fcde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcdc8.md#insn-007fcde8)
- 新版 `007fce34`（命令位置の公開資料なし） · `007fce40`（命令位置の公開資料なし）

~~~diff
- 007fcddc ["INT_ADD", "register:40f0:8", ["const:7fcddc:8", "const:4:8"]]
- 007fcddc ["CALL", null, ["callee:00c57f60:8"]]
+ 007fce34 ["INT_ADD", "register:40f0:8", ["const:7fce34:8", "const:4:8"]]
+ 007fce34 ["CALL", null, ["callee:00c57f60:8"]]
- 007fcddc bytes 2d6c1194
+ 007fce34 bytes 4b6c1194
- 007fcde8 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 007fcde8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fcde8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fcde8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fce40 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 007fce40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fce40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fce40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fcde8 bytes 08c11e91
+ 007fce40 bytes 08012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17b30465674de37e344cfe1df543212f"></a>

### [`007fce00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce00.md) → [`007fce58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fce58.md) FUN_007fce58

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fce60",
      "incomplete_value": false,
      "site": "007fce64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fce08",
      "incomplete_value": false,
      "site": "007fce0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:7b0:8"
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
      "007fce64",
      "DATA",
      [
        "storage",
        "00c7d7b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fce64",
      "DATA",
      [
        "storage",
        "00c7d880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fce08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce00.md#insn-007fce08)
- 新版 `007fce60`（命令位置の公開資料なし）

~~~diff
- 007fce08 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 007fce08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fce08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fce08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fce60 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 007fce60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fce60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fce60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fce08 bytes 29c11e91
+ 007fce60 bytes 29012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-171122b05094d47f36c061b7beaed910"></a>

### [`007fce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce20.md) → [`007fce78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fce78.md) FUN_007fce78

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fce9c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fce44",
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
      "007fce9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fce9c",
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

- 旧版 [`007fce44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce20.md#insn-007fce44) · [`007fce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce20.md#insn-007fce50)
- 新版 `007fce9c`（命令位置の公開資料なし） · `007fcea8`（命令位置の公開資料なし）

~~~diff
- 007fce44 ["INT_ADD", "register:40f0:8", ["const:7fce44:8", "const:4:8"]]
- 007fce44 ["CALL", null, ["ram:47acf4:8"]]
+ 007fce9c ["INT_ADD", "register:40f0:8", ["const:7fce9c:8", "const:4:8"]]
+ 007fce9c ["CALL", null, ["ram:47ad34:8"]]
- 007fce44 bytes acf7f197
+ 007fce9c bytes a6f7f197
- 007fce50 ["INT_ADD", "register:40f0:8", ["const:7fce50:8", "const:4:8"]]
- 007fce50 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fcea8 ["INT_ADD", "register:40f0:8", ["const:7fcea8:8", "const:4:8"]]
+ 007fcea8 ["CALL", null, ["callee:0047ce14:8"]]
- 007fce50 bytes e1fff197
+ 007fcea8 bytes dbfff197
~~~


<a id="compare-74785836169d6e916cf51bb1e0aa089f"></a>

### [`007fce94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce94.md) → [`007fceec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fceec.md) FUN_007fceec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fcf0c",
      "incomplete_value": false,
      "site": "007fcf10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fceb4",
      "incomplete_value": false,
      "site": "007fceb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "007fcf10",
      "DATA",
      [
        "storage",
        "00c7d830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fcf10",
      "DATA",
      [
        "storage",
        "00c7d900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fcea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce94.md#insn-007fcea8) · [`007fceb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce94.md#insn-007fceb4)
- 新版 `007fcf00`（命令位置の公開資料なし） · `007fcf0c`（命令位置の公開資料なし）

~~~diff
- 007fcea8 ["INT_ADD", "register:40f0:8", ["const:7fcea8:8", "const:4:8"]]
- 007fcea8 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fcf00 ["INT_ADD", "register:40f0:8", ["const:7fcf00:8", "const:4:8"]]
+ 007fcf00 ["CALL", null, ["callee:00c57f60:8"]]
- 007fcea8 bytes fa6b1194
+ 007fcf00 bytes 186c1194
- 007fceb4 ["COPY", "tmp:0:8", ["const:830:8"]]
- 007fceb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fceb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fceb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fcf0c ["COPY", "tmp:0:8", ["const:900:8"]]
+ 007fcf0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcf0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcf0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fceb4 bytes 08c12091
+ 007fcf0c bytes 08012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f66d510108366d320bb575fd7a2b13d"></a>

### [`007fcecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcecc.md) → [`007fcf24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcf24.md) FUN_007fcf24

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fcf28",
      "incomplete_value": false,
      "site": "007fcf2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fced0",
      "incomplete_value": false,
      "site": "007fced4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "007fcf2c",
      "DATA",
      [
        "storage",
        "00c7d830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fcf2c",
      "DATA",
      [
        "storage",
        "00c7d900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fced0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcecc.md#insn-007fced0)
- 新版 `007fcf28`（命令位置の公開資料なし）

~~~diff
- 007fced0 ["COPY", "tmp:0:8", ["const:830:8"]]
- 007fced0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fced0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fced0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fcf28 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 007fcf28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcf28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcf28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fced0 bytes 08c12091
+ 007fcf28 bytes 08012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5144fa25c0f2cbf2a5efbaf33c0532a3"></a>

### [`007fceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fceec.md) → [`007fcf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcf44.md) FUN_007fcf44

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`007efd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efd00.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fcf6c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fcf14",
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
      "007fcf6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fcf6c",
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

- 旧版 [`007fcf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fceec.md#insn-007fcf14) · [`007fcf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fceec.md#insn-007fcf20)
- 新版 `007fcf6c`（命令位置の公開資料なし） · `007fcf78`（命令位置の公開資料なし）

~~~diff
- 007fcf14 ["INT_ADD", "register:40f0:8", ["const:7fcf14:8", "const:4:8"]]
- 007fcf14 ["CALL", null, ["ram:47acf4:8"]]
+ 007fcf6c ["INT_ADD", "register:40f0:8", ["const:7fcf6c:8", "const:4:8"]]
+ 007fcf6c ["CALL", null, ["ram:47ad34:8"]]
- 007fcf14 bytes 78f7f197
+ 007fcf6c bytes 72f7f197
- 007fcf20 ["INT_ADD", "register:40f0:8", ["const:7fcf20:8", "const:4:8"]]
- 007fcf20 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fcf78 ["INT_ADD", "register:40f0:8", ["const:7fcf78:8", "const:4:8"]]
+ 007fcf78 ["CALL", null, ["callee:0047ce14:8"]]
- 007fcf20 bytes adfff197
+ 007fcf78 bytes a7fff197
~~~


<a id="compare-31e2d1cf2217d9d0d4c0a99d8b419d2b"></a>

### [`007fcf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcf84.md) → [`007fcfdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcfdc.md) FUN_007fcfdc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fcffc",
      "incomplete_value": false,
      "site": "007fd000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fcfa4",
      "incomplete_value": false,
      "site": "007fcfa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
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
      "007fd000",
      "DATA",
      [
        "storage",
        "00c7d8b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd000",
      "DATA",
      [
        "storage",
        "00c7d980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fcf98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcf84.md#insn-007fcf98) · [`007fcfa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcf84.md#insn-007fcfa4)
- 新版 `007fcff0`（命令位置の公開資料なし） · `007fcffc`（命令位置の公開資料なし）

~~~diff
- 007fcf98 ["INT_ADD", "register:40f0:8", ["const:7fcf98:8", "const:4:8"]]
- 007fcf98 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fcff0 ["INT_ADD", "register:40f0:8", ["const:7fcff0:8", "const:4:8"]]
+ 007fcff0 ["CALL", null, ["callee:00c57f60:8"]]
- 007fcf98 bytes be6b1194
+ 007fcff0 bytes dc6b1194
- 007fcfa4 ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 007fcfa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fcfa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fcfa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fcffc ["COPY", "tmp:0:8", ["const:980:8"]]
+ 007fcffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fcfa4 bytes 08c12291
+ 007fcffc bytes 08012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9833d5b25abbed87aa6b42e21f5a9354"></a>

### [`007fcfbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcfbc.md) → [`007fd014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd014.md) FUN_007fd014

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fd018",
      "incomplete_value": false,
      "site": "007fd01c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fcfc0",
      "incomplete_value": false,
      "site": "007fcfc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
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
      "007fd01c",
      "DATA",
      [
        "storage",
        "00c7d8b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd01c",
      "DATA",
      [
        "storage",
        "00c7d980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fcfc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcfbc.md#insn-007fcfc0)
- 新版 `007fd018`（命令位置の公開資料なし）

~~~diff
- 007fcfc0 ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 007fcfc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fcfc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fcfc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd018 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 007fd018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fcfc0 bytes 08c12291
+ 007fd018 bytes 08012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb2723544eb4e5dda9e4c49feef7a523"></a>

### [`007fcfdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcfdc.md) → [`007fd034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd034.md) FUN_007fd034

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`007efd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efd00.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fd05c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fd004",
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
      "007fd05c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fd05c",
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

- 旧版 [`007fd004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcfdc.md#insn-007fd004) · [`007fd010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcfdc.md#insn-007fd010)
- 新版 `007fd05c`（命令位置の公開資料なし） · `007fd068`（命令位置の公開資料なし）

~~~diff
- 007fd004 ["INT_ADD", "register:40f0:8", ["const:7fd004:8", "const:4:8"]]
- 007fd004 ["CALL", null, ["ram:47acf4:8"]]
+ 007fd05c ["INT_ADD", "register:40f0:8", ["const:7fd05c:8", "const:4:8"]]
+ 007fd05c ["CALL", null, ["ram:47ad34:8"]]
- 007fd004 bytes 3cf7f197
+ 007fd05c bytes 36f7f197
- 007fd010 ["INT_ADD", "register:40f0:8", ["const:7fd010:8", "const:4:8"]]
- 007fd010 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fd068 ["INT_ADD", "register:40f0:8", ["const:7fd068:8", "const:4:8"]]
+ 007fd068 ["CALL", null, ["callee:0047ce14:8"]]
- 007fd010 bytes 71fff197
+ 007fd068 bytes 6bfff197
~~~


<a id="compare-efd20d6e2b16ac1dfdcdc3fe5ee6e55b"></a>

### [`007fd074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd074.md) → [`007fd0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd0cc.md) FUN_007fd0cc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fd0e0",
      "incomplete_value": false,
      "site": "007fd0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd088",
      "incomplete_value": false,
      "site": "007fd08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "007fd0e4",
      "DATA",
      [
        "storage",
        "00c7d930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd0e4",
      "DATA",
      [
        "storage",
        "00c7da00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd074.md#insn-007fd080) · [`007fd088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd074.md#insn-007fd088)
- 新版 `007fd0d8`（命令位置の公開資料なし） · `007fd0e0`（命令位置の公開資料なし）

~~~diff
- 007fd080 ["INT_ADD", "register:40f0:8", ["const:7fd080:8", "const:4:8"]]
- 007fd080 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fd0d8 ["INT_ADD", "register:40f0:8", ["const:7fd0d8:8", "const:4:8"]]
+ 007fd0d8 ["CALL", null, ["callee:00c57f60:8"]]
- 007fd080 bytes 846b1194
+ 007fd0d8 bytes a26b1194
- 007fd088 ["COPY", "tmp:0:8", ["const:930:8"]]
- 007fd088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fd088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fd088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd0e0 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 007fd0e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd0e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd0e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fd088 bytes 08c12491
+ 007fd0e0 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f85eba232fe7ddbe194a7db46056b04d"></a>

### [`007fd098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd098.md) → [`007fd0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd0f0.md) FUN_007fd0f0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fd0f4",
      "incomplete_value": false,
      "site": "007fd0f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd09c",
      "incomplete_value": false,
      "site": "007fd0a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "007fd0f8",
      "DATA",
      [
        "storage",
        "00c7d930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd0f8",
      "DATA",
      [
        "storage",
        "00c7da00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd098.md#insn-007fd09c)
- 新版 `007fd0f4`（命令位置の公開資料なし）

~~~diff
- 007fd09c ["COPY", "tmp:0:8", ["const:930:8"]]
- 007fd09c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fd09c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fd09c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd0f4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 007fd0f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd0f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd0f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fd09c bytes 08c12491
+ 007fd0f4 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4223efea818811838aaf5990f1d93df"></a>

### [`007fd0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd0b0.md) → [`007fd108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd108.md) FUN_007fd108

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fd12c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fd0d4",
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
      "007fd12c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fd12c",
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

- 旧版 [`007fd0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd0b0.md#insn-007fd0d4) · [`007fd0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd0b0.md#insn-007fd0e0)
- 新版 `007fd12c`（命令位置の公開資料なし） · `007fd138`（命令位置の公開資料なし）

~~~diff
- 007fd0d4 ["INT_ADD", "register:40f0:8", ["const:7fd0d4:8", "const:4:8"]]
- 007fd0d4 ["CALL", null, ["ram:47acf4:8"]]
+ 007fd12c ["INT_ADD", "register:40f0:8", ["const:7fd12c:8", "const:4:8"]]
+ 007fd12c ["CALL", null, ["ram:47ad34:8"]]
- 007fd0d4 bytes 08f7f197
+ 007fd12c bytes 02f7f197
- 007fd0e0 ["INT_ADD", "register:40f0:8", ["const:7fd0e0:8", "const:4:8"]]
- 007fd0e0 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fd138 ["INT_ADD", "register:40f0:8", ["const:7fd138:8", "const:4:8"]]
+ 007fd138 ["CALL", null, ["callee:0047ce14:8"]]
- 007fd0e0 bytes 3dfff197
+ 007fd138 bytes 37fff197
~~~


<a id="compare-0d69ca79fbe51ca39809f084f7242332"></a>

### [`007fd124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd124.md) → [`007fd17c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd17c.md) FUN_007fd17c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fd1a0",
      "incomplete_value": false,
      "site": "007fd1a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd148",
      "incomplete_value": false,
      "site": "007fd14c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
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
      "007fd1a4",
      "DATA",
      [
        "storage",
        "00c7d9b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd1a4",
      "DATA",
      [
        "storage",
        "00c7da80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd124.md#insn-007fd138) · [`007fd148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd124.md#insn-007fd148)
- 新版 `007fd190`（命令位置の公開資料なし） · `007fd1a0`（命令位置の公開資料なし）

~~~diff
- 007fd138 ["INT_ADD", "register:40f0:8", ["const:7fd138:8", "const:4:8"]]
- 007fd138 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fd190 ["INT_ADD", "register:40f0:8", ["const:7fd190:8", "const:4:8"]]
+ 007fd190 ["CALL", null, ["callee:00c57f60:8"]]
- 007fd138 bytes 566b1194
+ 007fd190 bytes 746b1194
- 007fd148 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 007fd148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fd148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fd148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd1a0 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 007fd1a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd1a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd1a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fd148 bytes 08c12691
+ 007fd1a0 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0835f02297c152438554415ba313672c"></a>

### [`007fd164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd164.md) → [`007fd1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd1bc.md) FUN_007fd1bc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "007fd1c0",
      "incomplete_value": false,
      "site": "007fd1c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd168",
      "incomplete_value": false,
      "site": "007fd16c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
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
      "007fd1c4",
      "DATA",
      [
        "storage",
        "00c7d9b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd1c4",
      "DATA",
      [
        "storage",
        "00c7da80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd164.md#insn-007fd168)
- 新版 `007fd1c0`（命令位置の公開資料なし）

~~~diff
- 007fd168 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 007fd168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fd168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fd168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd1c0 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 007fd1c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd1c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd1c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fd168 bytes 08c12691
+ 007fd1c0 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7faf1fecd97b8a3badf31498a30e0ec8"></a>

### [`007fd324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd324.md) → [`007fd37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd37c.md) FUN_007fd37c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fd39c",
      "incomplete_value": false,
      "site": "007fd3a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd344",
      "incomplete_value": false,
      "site": "007fd348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "007fd3a0",
      "DATA",
      [
        "storage",
        "00c7da30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd3a0",
      "DATA",
      [
        "storage",
        "00c7db00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd324.md#insn-007fd338) · [`007fd344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd324.md#insn-007fd344)
- 新版 `007fd390`（命令位置の公開資料なし） · `007fd39c`（命令位置の公開資料なし）

~~~diff
- 007fd338 ["INT_ADD", "register:40f0:8", ["const:7fd338:8", "const:4:8"]]
- 007fd338 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fd390 ["INT_ADD", "register:40f0:8", ["const:7fd390:8", "const:4:8"]]
+ 007fd390 ["CALL", null, ["callee:00c57f60:8"]]
- 007fd338 bytes d66a1194
+ 007fd390 bytes f46a1194
- 007fd344 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 007fd344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fd344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fd344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd39c ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 007fd39c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd39c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd39c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fd344 bytes 08c12891
+ 007fd39c bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-893f3cd1e3a4fd01f80d489bd032d474"></a>

### [`007fd35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd35c.md) → [`007fd3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd3b4.md) FUN_007fd3b4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fd3b8",
      "incomplete_value": false,
      "site": "007fd3bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd360",
      "incomplete_value": false,
      "site": "007fd364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "007fd3bc",
      "DATA",
      [
        "storage",
        "00c7da30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd3bc",
      "DATA",
      [
        "storage",
        "00c7db00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd35c.md#insn-007fd360)
- 新版 `007fd3b8`（命令位置の公開資料なし）

~~~diff
- 007fd360 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 007fd360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fd360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fd360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd3b8 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 007fd3b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd3b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd3b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fd360 bytes 08c12891
+ 007fd3b8 bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b2cca13197baea41a3500e483d47a96"></a>

### [`007fd37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd37c.md) → [`007fd3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd3d4.md) FUN_007fd3d4

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047ce28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md) [`007fd5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5e8.md) [`007fd5ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5ec.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0047ce68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce68.md) [`007fd640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd640.md) [`007fd644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd644.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.63% / 新版 92.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007fd47c",
      "incomplete_value": false,
      "site": "007fd47c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd424",
      "incomplete_value": false,
      "site": "007fd424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
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
      "definition_site": "007fd4cc",
      "incomplete_value": true,
      "site": "007fd4cc",
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
                "const:118:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd474",
      "incomplete_value": true,
      "site": "007fd474",
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
                "const:16c:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fd414",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fd3bc",
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
      "007fd414",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007fd464",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007fd47c",
      "DATA",
      [
        "storage",
        "00c7daa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd414",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007fd464",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007fd47c",
      "DATA",
      [
        "storage",
        "00c7db70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd37c.md#insn-007fd3bc) · [`007fd40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd37c.md#insn-007fd40c) · [`007fd41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd37c.md#insn-007fd41c)
- 新版 `007fd414`（命令位置の公開資料なし） · `007fd464`（命令位置の公開資料なし） · `007fd474`（命令位置の公開資料なし）

~~~diff
- 007fd3bc ["INT_ADD", "register:40f0:8", ["const:7fd3bc:8", "const:4:8"]]
- 007fd3bc ["CALL", null, ["ram:47acf4:8"]]
+ 007fd414 ["INT_ADD", "register:40f0:8", ["const:7fd414:8", "const:4:8"]]
+ 007fd414 ["CALL", null, ["ram:47ad34:8"]]
- 007fd3bc bytes 4ef6f197
+ 007fd414 bytes 48f6f197
- 007fd40c ["INT_ADD", "register:40f0:8", ["const:7fd40c:8", "const:4:8"]]
- 007fd40c ["CALL", null, ["ram:47acf4:8"]]
+ 007fd464 ["INT_ADD", "register:40f0:8", ["const:7fd464:8", "const:4:8"]]
+ 007fd464 ["CALL", null, ["ram:47ad34:8"]]
- 007fd40c bytes 3af6f197
+ 007fd464 bytes 34f6f197
- 007fd41c ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 007fd41c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fd41c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fd41c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fd474 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 007fd474 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fd474 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fd474 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fd41c bytes 29812a91
+ 007fd474 bytes 29c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ca78431d87ceed9981175055ae80f70"></a>

### [`007fd598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd598.md) → [`007fd5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd5f0.md) FUN_007fd5f0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fd610",
      "incomplete_value": false,
      "site": "007fd614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd5b8",
      "incomplete_value": false,
      "site": "007fd5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007fd614",
      "DATA",
      [
        "storage",
        "00c7daa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd614",
      "DATA",
      [
        "storage",
        "00c7db70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd598.md#insn-007fd5ac) · [`007fd5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd598.md#insn-007fd5b8)
- 新版 `007fd604`（命令位置の公開資料なし） · `007fd610`（命令位置の公開資料なし）

~~~diff
- 007fd5ac ["INT_ADD", "register:40f0:8", ["const:7fd5ac:8", "const:4:8"]]
- 007fd5ac ["CALL", null, ["callee:00c57f60:8"]]
+ 007fd604 ["INT_ADD", "register:40f0:8", ["const:7fd604:8", "const:4:8"]]
+ 007fd604 ["CALL", null, ["callee:00c57f60:8"]]
- 007fd5ac bytes 396a1194
+ 007fd604 bytes 576a1194
- 007fd5b8 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 007fd5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fd5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fd5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd610 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 007fd610 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd610 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd610 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fd5b8 bytes 08812a91
+ 007fd610 bytes 08c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d48401b2ed0ff6a279f1f7d323c10ba"></a>

### [`007fd5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5d0.md) → [`007fd628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd628.md) FUN_007fd628

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fd62c",
      "incomplete_value": false,
      "site": "007fd630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd5d4",
      "incomplete_value": false,
      "site": "007fd5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
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
      "007fd630",
      "DATA",
      [
        "storage",
        "00c7daa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd630",
      "DATA",
      [
        "storage",
        "00c7db70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5d0.md#insn-007fd5d4)
- 新版 `007fd62c`（命令位置の公開資料なし）

~~~diff
- 007fd5d4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 007fd5d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fd5d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fd5d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd62c ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 007fd62c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd62c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd62c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fd5d4 bytes 08812a91
+ 007fd62c bytes 08c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b3030b0244226c1bb0cc2e662d5081c"></a>

### [`007fd5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5f0.md) → [`007fd648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd648.md) FUN_007fd648

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 23件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md)
- 新版 呼出元 0件  · 呼出先 23件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047cf48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cf48.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00597f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f0c.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.67% / 新版 88.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007fd780",
      "incomplete_value": true,
      "site": "007fd780",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:e6c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd728",
      "incomplete_value": true,
      "site": "007fd728",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:ec8:8"
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
      "definition_site": "007fd784",
      "incomplete_value": true,
      "site": "007fd784",
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
      "definition_site": "007fd72c",
      "incomplete_value": true,
      "site": "007fd72c",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007fd7e8",
      "incomplete_value": true,
      "site": "007fd7fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "007fd790",
      "incomplete_value": true,
      "site": "007fd7a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:110:8"
              ]
            ]
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
      "007fd6a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007fd6b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84d88"
      ]
    ],
    [
      "007fd708",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84d88"
      ]
    ]
  ],
  "added": [
    [
      "007fd6a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007fd6b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84df8"
      ]
    ],
    [
      "007fd708",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84df8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5f0.md#insn-007fd64c) · [`007fd65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5f0.md#insn-007fd65c) · [`007fd6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5f0.md#insn-007fd6b0)
- 新版 `007fd6a4`（命令位置の公開資料なし） · `007fd6b4`（命令位置の公開資料なし） · `007fd708`（命令位置の公開資料なし）

~~~diff
- 007fd64c ["INT_ADD", "register:40f0:8", ["const:7fd64c:8", "const:4:8"]]
- 007fd64c ["CALL", null, ["ram:47acf4:8"]]
+ 007fd6a4 ["INT_ADD", "register:40f0:8", ["const:7fd6a4:8", "const:4:8"]]
+ 007fd6a4 ["CALL", null, ["ram:47ad34:8"]]
- 007fd64c bytes aaf5f197
+ 007fd6a4 bytes a4f5f197
- 007fd65c ["INT_ADD", "register:40f0:8", ["const:7fd65c:8", "const:4:8"]]
- 007fd65c ["CALL", null, ["ram:a84d88:8"]]
+ 007fd6b4 ["INT_ADD", "register:40f0:8", ["const:7fd6b4:8", "const:4:8"]]
+ 007fd6b4 ["CALL", null, ["ram:a84df8:8"]]
- 007fd65c bytes cb1d0a94
+ 007fd6b4 bytes d11d0a94
- 007fd6b0 ["INT_ADD", "register:40f0:8", ["const:7fd6b0:8", "const:4:8"]]
- 007fd6b0 ["CALL", null, ["ram:a84d88:8"]]
+ 007fd708 ["INT_ADD", "register:40f0:8", ["const:7fd708:8", "const:4:8"]]
+ 007fd708 ["CALL", null, ["ram:a84df8:8"]]
- 007fd6b0 bytes b61d0a94
+ 007fd708 bytes bc1d0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17ad06bd7dbe8f5a7a249172caf76302"></a>

### [`007fdc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdc20.md) → [`007fdc78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fdc78.md) FUN_007fdc78

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fdc8c",
      "incomplete_value": false,
      "site": "007fdc90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fdc34",
      "incomplete_value": false,
      "site": "007fdc38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "007fdc90",
      "DATA",
      [
        "storage",
        "00c7db10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fdc90",
      "DATA",
      [
        "storage",
        "00c7dbe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fdc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdc20.md#insn-007fdc2c) · [`007fdc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdc20.md#insn-007fdc34)
- 新版 `007fdc84`（命令位置の公開資料なし） · `007fdc8c`（命令位置の公開資料なし）

~~~diff
- 007fdc2c ["INT_ADD", "register:40f0:8", ["const:7fdc2c:8", "const:4:8"]]
- 007fdc2c ["CALL", null, ["callee:00c57f60:8"]]
+ 007fdc84 ["INT_ADD", "register:40f0:8", ["const:7fdc84:8", "const:4:8"]]
+ 007fdc84 ["CALL", null, ["callee:00c57f60:8"]]
- 007fdc2c bytes 99681194
+ 007fdc84 bytes b7681194
- 007fdc34 ["COPY", "tmp:0:8", ["const:b10:8"]]
- 007fdc34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fdc34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fdc34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fdc8c ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 007fdc8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdc8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdc8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fdc34 bytes 08412c91
+ 007fdc8c bytes 08812f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab6e4c4b9fb280a9101e10d5e823834f"></a>

### [`007fdc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdc5c.md) → [`007fdcb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fdcb4.md) FUN_007fdcb4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fdcd8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fdc80",
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
      "007fdcd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fdcd8",
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

- 旧版 [`007fdc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdc5c.md#insn-007fdc80) · [`007fdc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdc5c.md#insn-007fdc8c)
- 新版 `007fdcd8`（命令位置の公開資料なし） · `007fdce4`（命令位置の公開資料なし）

~~~diff
- 007fdc80 ["INT_ADD", "register:40f0:8", ["const:7fdc80:8", "const:4:8"]]
- 007fdc80 ["CALL", null, ["ram:47acf4:8"]]
+ 007fdcd8 ["INT_ADD", "register:40f0:8", ["const:7fdcd8:8", "const:4:8"]]
+ 007fdcd8 ["CALL", null, ["ram:47ad34:8"]]
- 007fdc80 bytes 1df4f197
+ 007fdcd8 bytes 17f4f197
- 007fdc8c ["INT_ADD", "register:40f0:8", ["const:7fdc8c:8", "const:4:8"]]
- 007fdc8c ["CALL", null, ["callee:0047ce14:8"]]
+ 007fdce4 ["INT_ADD", "register:40f0:8", ["const:7fdce4:8", "const:4:8"]]
+ 007fdce4 ["CALL", null, ["callee:0047ce14:8"]]
- 007fdc8c bytes 52fcf197
+ 007fdce4 bytes 4cfcf197
~~~


<a id="compare-306a187e44924e863a654e415900150c"></a>

### [`007fdcd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdcd0.md) → [`007fdd28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fdd28.md) FUN_007fdd28

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fdd3c",
      "incomplete_value": false,
      "site": "007fdd40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fdce4",
      "incomplete_value": false,
      "site": "007fdce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "007fdd40",
      "DATA",
      [
        "storage",
        "00c7db90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fdd40",
      "DATA",
      [
        "storage",
        "00c7dc60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fdcdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdcd0.md#insn-007fdcdc) · [`007fdce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdcd0.md#insn-007fdce4)
- 新版 `007fdd34`（命令位置の公開資料なし） · `007fdd3c`（命令位置の公開資料なし）

~~~diff
- 007fdcdc ["INT_ADD", "register:40f0:8", ["const:7fdcdc:8", "const:4:8"]]
- 007fdcdc ["CALL", null, ["callee:00c57f60:8"]]
+ 007fdd34 ["INT_ADD", "register:40f0:8", ["const:7fdd34:8", "const:4:8"]]
+ 007fdd34 ["CALL", null, ["callee:00c57f60:8"]]
- 007fdcdc bytes 6d681194
+ 007fdd34 bytes 8b681194
- 007fdce4 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 007fdce4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fdce4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fdce4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fdd3c ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 007fdd3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdd3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdd3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fdce4 bytes 08412e91
+ 007fdd3c bytes 08813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeaedf96adc1f8ee555ec2a088a31c83"></a>

### [`007fdcf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdcf4.md) → [`007fdd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fdd4c.md) FUN_007fdd4c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fdd50",
      "incomplete_value": false,
      "site": "007fdd54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fdcf8",
      "incomplete_value": false,
      "site": "007fdcfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "007fdd54",
      "DATA",
      [
        "storage",
        "00c7db90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fdd54",
      "DATA",
      [
        "storage",
        "00c7dc60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fdcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdcf4.md#insn-007fdcf8)
- 新版 `007fdd50`（命令位置の公開資料なし）

~~~diff
- 007fdcf8 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 007fdcf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fdcf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fdcf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fdd50 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 007fdd50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdd50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdd50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fdcf8 bytes 08412e91
+ 007fdd50 bytes 08813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0758bb3e7f4426c658f8cdc47177d16e"></a>

### [`007fdd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdd0c.md) → [`007fdd64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fdd64.md) FUN_007fdd64

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fdd88",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fdd30",
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
      "007fdd88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fdd88",
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

- 旧版 [`007fdd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdd0c.md#insn-007fdd30) · [`007fdd3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdd0c.md#insn-007fdd3c)
- 新版 `007fdd88`（命令位置の公開資料なし） · `007fdd94`（命令位置の公開資料なし）

~~~diff
- 007fdd30 ["INT_ADD", "register:40f0:8", ["const:7fdd30:8", "const:4:8"]]
- 007fdd30 ["CALL", null, ["ram:47acf4:8"]]
+ 007fdd88 ["INT_ADD", "register:40f0:8", ["const:7fdd88:8", "const:4:8"]]
+ 007fdd88 ["CALL", null, ["ram:47ad34:8"]]
- 007fdd30 bytes f1f3f197
+ 007fdd88 bytes ebf3f197
- 007fdd3c ["INT_ADD", "register:40f0:8", ["const:7fdd3c:8", "const:4:8"]]
- 007fdd3c ["CALL", null, ["callee:0047ce14:8"]]
+ 007fdd94 ["INT_ADD", "register:40f0:8", ["const:7fdd94:8", "const:4:8"]]
+ 007fdd94 ["CALL", null, ["callee:0047ce14:8"]]
- 007fdd3c bytes 26fcf197
+ 007fdd94 bytes 20fcf197
~~~


<a id="compare-f723e5f667786c8cf7728d5aec1d0264"></a>

### [`007fdd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdd80.md) → [`007fddd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fddd8.md) FUN_007fddd8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fddf8",
      "incomplete_value": false,
      "site": "007fddfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fdda0",
      "incomplete_value": false,
      "site": "007fdda4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:c30:8"
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
      "007fddfc",
      "DATA",
      [
        "storage",
        "00c7dc30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fddfc",
      "DATA",
      [
        "storage",
        "00c7dd00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fdd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdd80.md#insn-007fdd94) · [`007fdda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdd80.md#insn-007fdda0)
- 新版 `007fddec`（命令位置の公開資料なし） · `007fddf8`（命令位置の公開資料なし）

~~~diff
- 007fdd94 ["INT_ADD", "register:40f0:8", ["const:7fdd94:8", "const:4:8"]]
- 007fdd94 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fddec ["INT_ADD", "register:40f0:8", ["const:7fddec:8", "const:4:8"]]
+ 007fddec ["CALL", null, ["callee:00c57f60:8"]]
- 007fdd94 bytes 3f681194
+ 007fddec bytes 5d681194
- 007fdda0 ["COPY", "tmp:0:8", ["const:c30:8"]]
- 007fdda0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fdda0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fdda0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fddf8 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 007fddf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fddf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fddf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fdda0 bytes 08c13091
+ 007fddf8 bytes 08013491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a361cf8b6810ebfa83b69313dec9c87"></a>

### [`007fddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fddd8.md) → [`007fde30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fde30.md) FUN_007fde30

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

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
      "site": "007fde58",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fde00",
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
      "007fde58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fde58",
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

- 旧版 [`007fde00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fddd8.md#insn-007fde00) · [`007fde58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fddd8.md#insn-007fde58) · [`007fde0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fddd8.md#insn-007fde0c)
- 新版 `007fde58`（命令位置の公開資料なし） · `007fdeb0`（命令位置の公開資料なし） · `007fde64`（命令位置の公開資料なし）

~~~diff
- 007fde00 ["INT_ADD", "register:40f0:8", ["const:7fde00:8", "const:4:8"]]
- 007fde00 ["CALL", null, ["ram:47acf4:8"]]
+ 007fde58 ["INT_ADD", "register:40f0:8", ["const:7fde58:8", "const:4:8"]]
+ 007fde58 ["CALL", null, ["ram:47ad34:8"]]
- 007fde00 bytes bdf3f197
+ 007fde58 bytes b7f3f197
- 007fde58 ["INT_ADD", "register:40f0:8", ["const:7fde58:8", "const:4:8"]]
- 007fde58 ["CALL", null, ["callee:00851550:8"]]
+ 007fdeb0 ["INT_ADD", "register:40f0:8", ["const:7fdeb0:8", "const:4:8"]]
+ 007fdeb0 ["CALL", null, ["callee:00851550:8"]]
- 007fde58 bytes a84d0194
+ 007fdeb0 bytes a84d0194
- 007fde0c ["INT_ADD", "register:40f0:8", ["const:7fde0c:8", "const:4:8"]]
- 007fde0c ["CALL", null, ["callee:0047ce14:8"]]
+ 007fde64 ["INT_ADD", "register:40f0:8", ["const:7fde64:8", "const:4:8"]]
+ 007fde64 ["CALL", null, ["callee:0047ce14:8"]]
- 007fde0c bytes f2fbf197
+ 007fde64 bytes ecfbf197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d4c0ddc988b0abfed9467fddfa11fb0"></a>

### [`007fdeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdeb4.md) → [`007fdf0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fdf0c.md) FUN_007fdf0c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fdf20",
      "incomplete_value": false,
      "site": "007fdf24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fdec8",
      "incomplete_value": false,
      "site": "007fdecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
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
      "007fdf24",
      "DATA",
      [
        "storage",
        "00c7dcb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fdf24",
      "DATA",
      [
        "storage",
        "00c7dd80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fdec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdeb4.md#insn-007fdec0) · [`007fdec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdeb4.md#insn-007fdec8)
- 新版 `007fdf18`（命令位置の公開資料なし） · `007fdf20`（命令位置の公開資料なし）

~~~diff
- 007fdec0 ["INT_ADD", "register:40f0:8", ["const:7fdec0:8", "const:4:8"]]
- 007fdec0 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fdf18 ["INT_ADD", "register:40f0:8", ["const:7fdf18:8", "const:4:8"]]
+ 007fdf18 ["CALL", null, ["callee:00c57f60:8"]]
- 007fdec0 bytes f4671194
+ 007fdf18 bytes 12681194
- 007fdec8 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 007fdec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fdec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fdec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fdf20 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 007fdf20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdf20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdf20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fdec8 bytes 08c13291
+ 007fdf20 bytes 08013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a8bdbe2c639531d25fd9f24fa3f3c95"></a>

### [`007fded8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fded8.md) → [`007fdf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fdf30.md) FUN_007fdf30

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fdf34",
      "incomplete_value": false,
      "site": "007fdf38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fdedc",
      "incomplete_value": false,
      "site": "007fdee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
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
      "007fdf38",
      "DATA",
      [
        "storage",
        "00c7dcb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fdf38",
      "DATA",
      [
        "storage",
        "00c7dd80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fdedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fded8.md#insn-007fdedc)
- 新版 `007fdf34`（命令位置の公開資料なし）

~~~diff
- 007fdedc ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 007fdedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fdedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fdedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fdf34 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 007fdf34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdf34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdf34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fdedc bytes 08c13291
+ 007fdf34 bytes 08013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11a505ef4cec76e20f728f00dcffc7f9"></a>

### [`007fdef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdef0.md) → [`007fdf48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fdf48.md) FUN_007fdf48

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "007fdf64",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fdf0c",
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
      "007fdf64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fdf64",
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

- 旧版 [`007fdf0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdef0.md#insn-007fdf0c) · [`007fdf18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdef0.md#insn-007fdf18)
- 新版 `007fdf64`（命令位置の公開資料なし） · `007fdf70`（命令位置の公開資料なし）

~~~diff
- 007fdf0c ["INT_ADD", "register:40f0:8", ["const:7fdf0c:8", "const:4:8"]]
- 007fdf0c ["CALL", null, ["ram:47acf4:8"]]
+ 007fdf64 ["INT_ADD", "register:40f0:8", ["const:7fdf64:8", "const:4:8"]]
+ 007fdf64 ["CALL", null, ["ram:47ad34:8"]]
- 007fdf0c bytes 7af3f197
+ 007fdf64 bytes 74f3f197
- 007fdf18 ["INT_ADD", "register:40f0:8", ["const:7fdf18:8", "const:4:8"]]
- 007fdf18 ["CALL", null, ["callee:0047ce14:8"]]
+ 007fdf70 ["INT_ADD", "register:40f0:8", ["const:7fdf70:8", "const:4:8"]]
+ 007fdf70 ["CALL", null, ["callee:0047ce14:8"]]
- 007fdf18 bytes affbf197
+ 007fdf70 bytes a9fbf197
~~~


<a id="compare-7618877d9f6657f21318cc280fae500a"></a>

### [`007fdf5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdf5c.md) → [`007fdfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fdfb4.md) FUN_007fdfb4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fdfd8",
      "incomplete_value": false,
      "site": "007fdfd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fdf80",
      "incomplete_value": false,
      "site": "007fdf80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "007fdfd8",
      "DATA",
      [
        "storage",
        "00c7dd30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fdfd8",
      "DATA",
      [
        "storage",
        "00c7de00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fdf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdf5c.md#insn-007fdf70) · [`007fdf7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdf5c.md#insn-007fdf7c)
- 新版 `007fdfc8`（命令位置の公開資料なし） · `007fdfd4`（命令位置の公開資料なし）

~~~diff
- 007fdf70 ["INT_ADD", "register:40f0:8", ["const:7fdf70:8", "const:4:8"]]
- 007fdf70 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fdfc8 ["INT_ADD", "register:40f0:8", ["const:7fdfc8:8", "const:4:8"]]
+ 007fdfc8 ["CALL", null, ["callee:00c57f60:8"]]
- 007fdf70 bytes c8671194
+ 007fdfc8 bytes e6671194
- 007fdf7c ["COPY", "tmp:0:8", ["const:d30:8"]]
- 007fdf7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fdf7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fdf7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fdfd4 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 007fdfd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdfd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdfd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fdf7c bytes 08c13491
+ 007fdfd4 bytes 08013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfb9ea1f38ed92f3b72b54402ded05f7"></a>

### [`007fdfac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdfac.md) → [`007fe004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fe/007fe004.md) FUN_007fe004

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`008b9298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9298.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`008b92f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92f0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

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
      "site": "007fe058",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fe000",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "007fe0a0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fe048",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007fe058",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007fe0a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fe058",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007fe0a0",
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

- 旧版 [`007fe000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdfac.md#insn-007fe000) · [`007fe048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdfac.md#insn-007fe048) · [`007fdfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdfac.md#insn-007fdfd0)
- 新版 `007fe058`（命令位置の公開資料なし） · `007fe0a0`（命令位置の公開資料なし） · `007fe028`（命令位置の公開資料なし）

~~~diff
- 007fe000 ["INT_ADD", "register:40f0:8", ["const:7fe000:8", "const:4:8"]]
- 007fe000 ["CALL", null, ["ram:47acf4:8"]]
+ 007fe058 ["INT_ADD", "register:40f0:8", ["const:7fe058:8", "const:4:8"]]
+ 007fe058 ["CALL", null, ["ram:47ad34:8"]]
- 007fe000 bytes 3df3f197
+ 007fe058 bytes 37f3f197
- 007fe048 ["INT_ADD", "register:40f0:8", ["const:7fe048:8", "const:4:8"]]
- 007fe048 ["CALL", null, ["ram:47acf4:8"]]
+ 007fe0a0 ["INT_ADD", "register:40f0:8", ["const:7fe0a0:8", "const:4:8"]]
+ 007fe0a0 ["CALL", null, ["ram:47ad34:8"]]
- 007fe048 bytes 2bf3f197
+ 007fe0a0 bytes 25f3f197
- 007fdfd0 ["INT_ADD", "register:40f0:8", ["const:7fdfd0:8", "const:4:8"]]
- 007fdfd0 ["CALL", null, ["callee:008b92f0:8"]]
+ 007fe028 ["INT_ADD", "register:40f0:8", ["const:7fe028:8", "const:4:8"]]
+ 007fe028 ["CALL", null, ["callee:008b92f0:8"]]
- 007fdfd0 bytes b2ec0294
+ 007fe028 bytes b2ec0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cac48ab7a20d346573711112487c4e1"></a>

### [`007fe0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe0a8.md) → [`007fe100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fe/007fe100.md) FUN_007fe100

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007fe120",
      "incomplete_value": false,
      "site": "007fe124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fe0c8",
      "incomplete_value": false,
      "site": "007fe0cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "007fe124",
      "DATA",
      [
        "storage",
        "00c7ddb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fe124",
      "DATA",
      [
        "storage",
        "00c7de80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fe0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe0a8.md#insn-007fe0bc) · [`007fe0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe0a8.md#insn-007fe0c8)
- 新版 `007fe114`（命令位置の公開資料なし） · `007fe120`（命令位置の公開資料なし）

~~~diff
- 007fe0bc ["INT_ADD", "register:40f0:8", ["const:7fe0bc:8", "const:4:8"]]
- 007fe0bc ["CALL", null, ["callee:00c57f60:8"]]
+ 007fe114 ["INT_ADD", "register:40f0:8", ["const:7fe114:8", "const:4:8"]]
+ 007fe114 ["CALL", null, ["callee:00c57f60:8"]]
- 007fe0bc bytes 75671194
+ 007fe114 bytes 93671194
- 007fe0c8 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 007fe0c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fe0c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fe0c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fe120 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 007fe120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fe120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fe120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fe0c8 bytes 08c13691
+ 007fe120 bytes 08013a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57c65de68244b954f150055e37039ba7"></a>

### [`007fe0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe0e0.md) → [`007fe138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fe/007fe138.md) FUN_007fe138

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fe140",
      "incomplete_value": false,
      "site": "007fe144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fe0e8",
      "incomplete_value": false,
      "site": "007fe0ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "007fe144",
      "DATA",
      [
        "storage",
        "00c7ddb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fe144",
      "DATA",
      [
        "storage",
        "00c7de80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fe0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe0e0.md#insn-007fe0e8)
- 新版 `007fe140`（命令位置の公開資料なし）

~~~diff
- 007fe0e8 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 007fe0e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fe0e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fe0e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fe140 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 007fe140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fe140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fe140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fe0e8 bytes 29c13691
+ 007fe140 bytes 29013a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

