# v16.0.1 → v16.0.2 · 最優先の変更候補 (41)

[一覧の目次](README.md)

<a id="compare-9f9eceffcde6aadd58d395419dbb14f6"></a>

### [`007f6784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6784.md) → [`007f67dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f67dc.md) FUN_007f67dc

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
      "definition_site": "007f67e8",
      "incomplete_value": false,
      "site": "007f67e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6790",
      "incomplete_value": false,
      "site": "007f6790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "007f67e8",
      "DATA",
      [
        "storage",
        "00c7bb10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f67e8",
      "DATA",
      [
        "storage",
        "00c7bbe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f678c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6784.md#insn-007f678c)
- 新版 `007f67e4`（命令位置の公開資料なし）

~~~diff
- 007f678c ["COPY", "tmp:0:8", ["const:b10:8"]]
- 007f678c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f678c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f678c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f67e4 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 007f67e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f67e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f67e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f678c bytes 29412c91
+ 007f67e4 bytes 29812f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b5329cd6e49a7024355c619e0bd94f"></a>

### [`007f67a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f67a0.md) → [`007f67f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f67f8.md) FUN_007f67f8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

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
      "site": "007f6820",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f67c8",
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
      "007f6820",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f6820",
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

- 旧版 [`007f67c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f67a0.md#insn-007f67c8) · [`007f67d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f67a0.md#insn-007f67d4) · [`007f67ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f67a0.md#insn-007f67ec)
- 新版 `007f6820`（命令位置の公開資料なし） · `007f682c`（命令位置の公開資料なし） · `007f6844`（命令位置の公開資料なし）

~~~diff
- 007f67c8 ["INT_ADD", "register:40f0:8", ["const:7f67c8:8", "const:4:8"]]
- 007f67c8 ["CALL", null, ["ram:47acf4:8"]]
+ 007f6820 ["INT_ADD", "register:40f0:8", ["const:7f6820:8", "const:4:8"]]
+ 007f6820 ["CALL", null, ["ram:47ad34:8"]]
- 007f67c8 bytes 4b11f297
+ 007f6820 bytes 4511f297
- 007f67d4 ["INT_ADD", "register:40f0:8", ["const:7f67d4:8", "const:4:8"]]
- 007f67d4 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f682c ["INT_ADD", "register:40f0:8", ["const:7f682c:8", "const:4:8"]]
+ 007f682c ["CALL", null, ["callee:0047ce14:8"]]
- 007f67d4 bytes 8019f297
+ 007f682c bytes 7a19f297
- 007f67ec ["INT_ADD", "register:40f0:8", ["const:7f67ec:8", "const:4:8"]]
- 007f67ec ["CALL", null, ["callee:00a1a6f8:8"]]
+ 007f6844 ["INT_ADD", "register:40f0:8", ["const:7f6844:8", "const:4:8"]]
+ 007f6844 ["CALL", null, ["callee:00a1a6f8:8"]]
- 007f67ec bytes ae8f0894
+ 007f6844 bytes ad8f0894
~~~


<a id="compare-0e433c244be6bdab0e418c81972e2e63"></a>

### [`007f6830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6830.md) → [`007f6888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6888.md) FUN_007f6888

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
      "definition_site": "007f68ac",
      "incomplete_value": false,
      "site": "007f68ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6854",
      "incomplete_value": false,
      "site": "007f6854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "007f68ac",
      "DATA",
      [
        "storage",
        "00c7bbb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f68ac",
      "DATA",
      [
        "storage",
        "00c7bc80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6830.md#insn-007f6844) · [`007f6850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6830.md#insn-007f6850)
- 新版 `007f689c`（命令位置の公開資料なし） · `007f68a8`（命令位置の公開資料なし）

~~~diff
- 007f6844 ["INT_ADD", "register:40f0:8", ["const:7f6844:8", "const:4:8"]]
- 007f6844 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f689c ["INT_ADD", "register:40f0:8", ["const:7f689c:8", "const:4:8"]]
+ 007f689c ["CALL", null, ["callee:00c57f60:8"]]
- 007f6844 bytes 93851194
+ 007f689c bytes b1851194
- 007f6850 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 007f6850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f6850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f6850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f68a8 ["COPY", "tmp:0:8", ["const:c80:8"]]
+ 007f68a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f68a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f68a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f6850 bytes 08c12e91
+ 007f68a8 bytes 08013291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b48bc28c21a11d205012c3a9eafeee71"></a>

### [`007f6864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6864.md) → [`007f68bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f68bc.md) FUN_007f68bc

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
      "definition_site": "007f68c8",
      "incomplete_value": false,
      "site": "007f68c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6870",
      "incomplete_value": false,
      "site": "007f6870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "007f68c8",
      "DATA",
      [
        "storage",
        "00c7bbb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f68c8",
      "DATA",
      [
        "storage",
        "00c7bc80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f686c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6864.md#insn-007f686c)
- 新版 `007f68c4`（命令位置の公開資料なし）

~~~diff
- 007f686c ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 007f686c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f686c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f686c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f68c4 ["COPY", "tmp:0:8", ["const:c80:8"]]
+ 007f68c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f68c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f68c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f686c bytes 29c12e91
+ 007f68c4 bytes 29013291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b36dab01869caca76cd1f3809e474ad"></a>

### [`007f6880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6880.md) → [`007f68d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f68d8.md) FUN_007f68d8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007f6b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6b14.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`007f6b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6b6c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6994",
      "incomplete_value": false,
      "site": "007f6994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f693c",
      "incomplete_value": false,
      "site": "007f693c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "site": "007f6914",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f68bc",
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
      "007f6914",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f6964",
      "READ",
      [
        "storage",
        "002ba74b",
        null,
        "string"
      ]
    ],
    [
      "007f6994",
      "DATA",
      [
        "storage",
        "00c7bc20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f6914",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f6964",
      "READ",
      [
        "storage",
        "002ba6f7",
        null,
        "string"
      ]
    ],
    [
      "007f6994",
      "DATA",
      [
        "storage",
        "00c7bcf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f68bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6880.md#insn-007f68bc) · [`007f6994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6880.md#insn-007f6994) · [`007f68c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6880.md#insn-007f68c8)
- 新版 `007f6914`（命令位置の公開資料なし） · `007f69ec`（命令位置の公開資料なし） · `007f6920`（命令位置の公開資料なし）

~~~diff
- 007f68bc ["INT_ADD", "register:40f0:8", ["const:7f68bc:8", "const:4:8"]]
- 007f68bc ["CALL", null, ["ram:47acf4:8"]]
+ 007f6914 ["INT_ADD", "register:40f0:8", ["const:7f6914:8", "const:4:8"]]
+ 007f6914 ["CALL", null, ["ram:47ad34:8"]]
- 007f68bc bytes 0e11f297
+ 007f6914 bytes 0811f297
- 007f6994 ["INT_ADD", "register:40f0:8", ["const:7f6994:8", "const:4:8"]]
- 007f6994 ["CALL", null, ["callee:008b9558:8"]]
+ 007f69ec ["INT_ADD", "register:40f0:8", ["const:7f69ec:8", "const:4:8"]]
+ 007f69ec ["CALL", null, ["callee:008b9558:8"]]
- 007f6994 bytes db0a0394
+ 007f69ec bytes db0a0394
- 007f68c8 ["INT_ADD", "register:40f0:8", ["const:7f68c8:8", "const:4:8"]]
- 007f68c8 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f6920 ["INT_ADD", "register:40f0:8", ["const:7f6920:8", "const:4:8"]]
+ 007f6920 ["CALL", null, ["callee:0047ce14:8"]]
- 007f68c8 bytes 4319f297
+ 007f6920 bytes 3d19f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9e0289cb7870a19ea846477bf37fe2b"></a>

### [`007f6acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6acc.md) → [`007f6b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6b24.md) FUN_007f6b24

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
      "definition_site": "007f6b48",
      "incomplete_value": false,
      "site": "007f6b48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6af0",
      "incomplete_value": false,
      "site": "007f6af0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "007f6b48",
      "DATA",
      [
        "storage",
        "00c7bc20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f6b48",
      "DATA",
      [
        "storage",
        "00c7bcf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6acc.md#insn-007f6ae0) · [`007f6aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6acc.md#insn-007f6aec)
- 新版 `007f6b38`（命令位置の公開資料なし） · `007f6b44`（命令位置の公開資料なし）

~~~diff
- 007f6ae0 ["INT_ADD", "register:40f0:8", ["const:7f6ae0:8", "const:4:8"]]
- 007f6ae0 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f6b38 ["INT_ADD", "register:40f0:8", ["const:7f6b38:8", "const:4:8"]]
+ 007f6b38 ["CALL", null, ["callee:00c57f60:8"]]
- 007f6ae0 bytes ec841194
+ 007f6b38 bytes 0a851194
- 007f6aec ["COPY", "tmp:0:8", ["const:c20:8"]]
- 007f6aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f6aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f6aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f6b44 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 007f6b44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6b44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6b44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f6aec bytes 08813091
+ 007f6b44 bytes 08c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef41bfd9748d870af228847ddbf2ae75"></a>

### [`007f6b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6b00.md) → [`007f6b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6b58.md) FUN_007f6b58

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
      "definition_site": "007f6b64",
      "incomplete_value": false,
      "site": "007f6b64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6b0c",
      "incomplete_value": false,
      "site": "007f6b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "007f6b64",
      "DATA",
      [
        "storage",
        "00c7bc20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f6b64",
      "DATA",
      [
        "storage",
        "00c7bcf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6b00.md#insn-007f6b08)
- 新版 `007f6b60`（命令位置の公開資料なし）

~~~diff
- 007f6b08 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 007f6b08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f6b08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f6b08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f6b60 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 007f6b60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f6b60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f6b60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f6b08 bytes 29813091
+ 007f6b60 bytes 29c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca84849580b5af2e323d7bb8af787624"></a>

### [`007f6b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6b1c.md) → [`007f6b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6b74.md) FUN_007f6b74

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

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
      "site": "007f6b9c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f6b44",
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
      "007f6b9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f6b9c",
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

- 旧版 [`007f6b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6b1c.md#insn-007f6b44) · [`007f6b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6b1c.md#insn-007f6b50) · [`007f6b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6b1c.md#insn-007f6b68)
- 新版 `007f6b9c`（命令位置の公開資料なし） · `007f6ba8`（命令位置の公開資料なし） · `007f6bc0`（命令位置の公開資料なし）

~~~diff
- 007f6b44 ["INT_ADD", "register:40f0:8", ["const:7f6b44:8", "const:4:8"]]
- 007f6b44 ["CALL", null, ["ram:47acf4:8"]]
+ 007f6b9c ["INT_ADD", "register:40f0:8", ["const:7f6b9c:8", "const:4:8"]]
+ 007f6b9c ["CALL", null, ["ram:47ad34:8"]]
- 007f6b44 bytes 6c10f297
+ 007f6b9c bytes 6610f297
- 007f6b50 ["INT_ADD", "register:40f0:8", ["const:7f6b50:8", "const:4:8"]]
- 007f6b50 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f6ba8 ["INT_ADD", "register:40f0:8", ["const:7f6ba8:8", "const:4:8"]]
+ 007f6ba8 ["CALL", null, ["callee:0047ce14:8"]]
- 007f6b50 bytes a118f297
+ 007f6ba8 bytes 9b18f297
- 007f6b68 ["INT_ADD", "register:40f0:8", ["const:7f6b68:8", "const:4:8"]]
- 007f6b68 ["CALL", null, ["callee:00a1a6f8:8"]]
+ 007f6bc0 ["INT_ADD", "register:40f0:8", ["const:7f6bc0:8", "const:4:8"]]
+ 007f6bc0 ["CALL", null, ["callee:00a1a6f8:8"]]
- 007f6b68 bytes cf8e0894
+ 007f6bc0 bytes ce8e0894
~~~


<a id="compare-25629548cd7e4ce26beb71b715a139e4"></a>

### [`007f6bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6bac.md) → [`007f6c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6c04.md) FUN_007f6c04

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
      "definition_site": "007f6c28",
      "incomplete_value": false,
      "site": "007f6c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6bd0",
      "incomplete_value": false,
      "site": "007f6bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
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
      "007f6c28",
      "DATA",
      [
        "storage",
        "00c7bcb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f6c28",
      "DATA",
      [
        "storage",
        "00c7bd80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6bac.md#insn-007f6bc0) · [`007f6bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6bac.md#insn-007f6bcc)
- 新版 `007f6c18`（命令位置の公開資料なし） · `007f6c24`（命令位置の公開資料なし）

~~~diff
- 007f6bc0 ["INT_ADD", "register:40f0:8", ["const:7f6bc0:8", "const:4:8"]]
- 007f6bc0 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f6c18 ["INT_ADD", "register:40f0:8", ["const:7f6c18:8", "const:4:8"]]
+ 007f6c18 ["CALL", null, ["callee:00c57f60:8"]]
- 007f6bc0 bytes b4841194
+ 007f6c18 bytes d2841194
- 007f6bcc ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 007f6bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f6bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f6bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f6c24 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 007f6c24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6c24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6c24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f6bcc bytes 08c13291
+ 007f6c24 bytes 08013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5fea29fce08c62454bc356fcac30e7a"></a>

### [`007f6be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6be0.md) → [`007f6c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6c38.md) FUN_007f6c38

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
      "definition_site": "007f6c44",
      "incomplete_value": false,
      "site": "007f6c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6bec",
      "incomplete_value": false,
      "site": "007f6bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f6c44",
      "DATA",
      [
        "storage",
        "00c7bcb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f6c44",
      "DATA",
      [
        "storage",
        "00c7bd80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6be0.md#insn-007f6be8)
- 新版 `007f6c40`（命令位置の公開資料なし）

~~~diff
- 007f6be8 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 007f6be8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f6be8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f6be8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f6c40 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 007f6c40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f6c40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f6c40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f6be8 bytes 29c13291
+ 007f6c40 bytes 29013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd4ff60d7b91335b28909a3d37897834"></a>

### [`007f6bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6bfc.md) → [`007f6c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6c54.md) FUN_007f6c54

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 17件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007f6f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6f6c.md) [`007f6f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6f70.md)
- 新版 呼出元 0件  · 呼出先 17件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`007f6fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6fc4.md) [`007f6fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6fc8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.19% / 新版 88.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6ce4",
      "incomplete_value": true,
      "site": "007f6cf4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6d5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6c8c",
      "incomplete_value": true,
      "site": "007f6c9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:722:8"
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
      "definition_site": "007f6ce8",
      "incomplete_value": true,
      "site": "007f6cf8",
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
      "definition_site": "007f6c90",
      "incomplete_value": true,
      "site": "007f6ca0",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6cec",
      "incomplete_value": true,
      "site": "007f6cfc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "007f6c94",
      "incomplete_value": true,
      "site": "007f6ca4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a0:8"
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
      "007f6c8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f6ce4",
      "READ",
      [
        "storage",
        "002a4722",
        null,
        "string"
      ]
    ],
    [
      "007f6ce8",
      "READ",
      [
        "storage",
        "002a4732",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f6c8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f6ce4",
      "READ",
      [
        "storage",
        "002a46d5",
        null,
        "string"
      ]
    ],
    [
      "007f6ce8",
      "READ",
      [
        "storage",
        "002a46e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6bfc.md#insn-007f6c34) · [`007f6cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6bfc.md#insn-007f6cbc) · [`007f6d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6bfc.md#insn-007f6d4c)
- 新版 `007f6c8c`（命令位置の公開資料なし） · `007f6d14`（命令位置の公開資料なし） · `007f6da4`（命令位置の公開資料なし）

~~~diff
- 007f6c34 ["INT_ADD", "register:40f0:8", ["const:7f6c34:8", "const:4:8"]]
- 007f6c34 ["CALL", null, ["ram:47acf4:8"]]
+ 007f6c8c ["INT_ADD", "register:40f0:8", ["const:7f6c8c:8", "const:4:8"]]
+ 007f6c8c ["CALL", null, ["ram:47ad34:8"]]
- 007f6c34 bytes 3010f297
+ 007f6c8c bytes 2a10f297
- 007f6cbc ["COPY", "tmp:0:8", ["const:d20:8"]]
- 007f6cbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f6cbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f6cbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f6d14 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 007f6d14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6d14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6d14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f6cbc bytes 08813491
+ 007f6d14 bytes 08c13791
- 007f6d4c ["COPY", "register:0:8", ["register:4040:8"]]
- 007f6d4c ["INT_ADD", "register:40f0:8", ["const:7f6d4c:8", "const:4:8"]]
- 007f6d4c ["CALLIND", null, ["register:0:8"]]
+ 007f6da4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007f6da4 ["INT_ADD", "register:40f0:8", ["const:7f6da4:8", "const:4:8"]]
+ 007f6da4 ["CALLIND", null, ["register:0:8"]]
- 007f6d4c bytes 00013fd6
+ 007f6da4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a321be7fd297946bb53e3b5c42dd74aa"></a>

### [`007f6f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6f24.md) → [`007f6f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6f7c.md) FUN_007f6f7c

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
      "definition_site": "007f6fa0",
      "incomplete_value": false,
      "site": "007f6fa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6f48",
      "incomplete_value": false,
      "site": "007f6f48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "007f6fa0",
      "DATA",
      [
        "storage",
        "00c7bd20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f6fa0",
      "DATA",
      [
        "storage",
        "00c7bdf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6f24.md#insn-007f6f38) · [`007f6f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6f24.md#insn-007f6f44)
- 新版 `007f6f90`（命令位置の公開資料なし） · `007f6f9c`（命令位置の公開資料なし）

~~~diff
- 007f6f38 ["INT_ADD", "register:40f0:8", ["const:7f6f38:8", "const:4:8"]]
- 007f6f38 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f6f90 ["INT_ADD", "register:40f0:8", ["const:7f6f90:8", "const:4:8"]]
+ 007f6f90 ["CALL", null, ["callee:00c57f60:8"]]
- 007f6f38 bytes d6831194
+ 007f6f90 bytes f4831194
- 007f6f44 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 007f6f44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f6f44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f6f44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f6f9c ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 007f6f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f6f44 bytes 08813491
+ 007f6f9c bytes 08c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5753c7b8e9fd15ab3cbdadfd1462fba9"></a>

### [`007f6f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6f58.md) → [`007f6fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6fb0.md) FUN_007f6fb0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6fbc",
      "incomplete_value": true,
      "site": "007f6fbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6f64",
      "incomplete_value": true,
      "site": "007f6f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
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
      "007f6fbc",
      "DATA",
      [
        "storage",
        "00c7bd20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f6fbc",
      "DATA",
      [
        "storage",
        "00c7bdf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6f58.md#insn-007f6f60)
- 新版 `007f6fb8`（命令位置の公開資料なし）

~~~diff
- 007f6f60 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 007f6f60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f6f60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f6f60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f6fb8 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 007f6fb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f6fb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f6fb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f6f60 bytes 29813491
+ 007f6fb8 bytes 29c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-784a57bb2df33f7640a52dcade159502"></a>

### [`007f6fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6fa4.md) → [`007f6ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6ffc.md) FUN_007f6ffc

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
      "definition_site": "007f7020",
      "incomplete_value": false,
      "site": "007f7020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6fc8",
      "incomplete_value": false,
      "site": "007f6fc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f7020",
      "DATA",
      [
        "storage",
        "00c7bda0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7020",
      "DATA",
      [
        "storage",
        "00c7be70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6fa4.md#insn-007f6fb8) · [`007f6fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6fa4.md#insn-007f6fc4)
- 新版 `007f7010`（命令位置の公開資料なし） · `007f701c`（命令位置の公開資料なし）

~~~diff
- 007f6fb8 ["INT_ADD", "register:40f0:8", ["const:7f6fb8:8", "const:4:8"]]
- 007f6fb8 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f7010 ["INT_ADD", "register:40f0:8", ["const:7f7010:8", "const:4:8"]]
+ 007f7010 ["CALL", null, ["callee:00c57f60:8"]]
- 007f6fb8 bytes b6831194
+ 007f7010 bytes d4831194
- 007f6fc4 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 007f6fc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f6fc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f6fc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f701c ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 007f701c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f701c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f701c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f6fc4 bytes 08813691
+ 007f701c bytes 08c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b2a6d9025f365447392adbdb279a160"></a>

### [`007f6fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6fd8.md) → [`007f7030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7030.md) FUN_007f7030

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
      "definition_site": "007f703c",
      "incomplete_value": false,
      "site": "007f703c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6fe4",
      "incomplete_value": false,
      "site": "007f6fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:da0:8"
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
      "007f703c",
      "DATA",
      [
        "storage",
        "00c7bda0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f703c",
      "DATA",
      [
        "storage",
        "00c7be70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6fd8.md#insn-007f6fe0)
- 新版 `007f7038`（命令位置の公開資料なし）

~~~diff
- 007f6fe0 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 007f6fe0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f6fe0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f6fe0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f7038 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 007f7038 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f7038 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f7038 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f6fe0 bytes 29813691
+ 007f7038 bytes 29c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7de76c93506326f585cd66909c5d900"></a>

### [`007f6ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6ff4.md) → [`007f704c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f704c.md) FUN_007f704c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085b2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2a4.md) [`0085b2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2ac.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085b2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b2fc.md) [`0085b304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b304.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

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
      "site": "007f7148",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f70f0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 17,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f7148",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f7148",
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

- 旧版 [`007f70f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6ff4.md#insn-007f70f0) · [`007f7014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6ff4.md#insn-007f7014) · [`007f7028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6ff4.md#insn-007f7028)
- 新版 `007f7148`（命令位置の公開資料なし） · `007f706c`（命令位置の公開資料なし） · `007f7080`（命令位置の公開資料なし）

~~~diff
- 007f70f0 ["INT_ADD", "register:40f0:8", ["const:7f70f0:8", "const:4:8"]]
- 007f70f0 ["CALL", null, ["ram:47acf4:8"]]
+ 007f7148 ["INT_ADD", "register:40f0:8", ["const:7f7148:8", "const:4:8"]]
+ 007f7148 ["CALL", null, ["ram:47ad34:8"]]
- 007f70f0 bytes 010ff297
+ 007f7148 bytes fb0ef297
- 007f7014 ["INT_ADD", "register:40f0:8", ["const:7f7014:8", "const:4:8"]]
- 007f7014 ["CALL", null, ["callee:008b92e8:8"]]
+ 007f706c ["INT_ADD", "register:40f0:8", ["const:7f706c:8", "const:4:8"]]
+ 007f706c ["CALL", null, ["callee:008b92e8:8"]]
- 007f7014 bytes 9f080394
+ 007f706c bytes 9f080394
- 007f7028 ["INT_ADD", "register:40f0:8", ["const:7f7028:8", "const:4:8"]]
- 007f7028 ["CALL", null, ["callee:008b7a20:8"]]
+ 007f7080 ["INT_ADD", "register:40f0:8", ["const:7f7080:8", "const:4:8"]]
+ 007f7080 ["CALL", null, ["callee:008b7a20:8"]]
- 007f7028 bytes 68020394
+ 007f7080 bytes 68020394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-021895b09f37fe07759e9a2e4c8c992f"></a>

### [`007f7188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7188.md) → [`007f71e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f71e0.md) FUN_007f71e0

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
      "definition_site": "007f71ec",
      "incomplete_value": false,
      "site": "007f71ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7194",
      "incomplete_value": false,
      "site": "007f7194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f71ec",
      "DATA",
      [
        "storage",
        "00c7be20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f71ec",
      "DATA",
      [
        "storage",
        "00c7bef0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f7190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7188.md#insn-007f7190)
- 新版 `007f71e8`（命令位置の公開資料なし）

~~~diff
- 007f7190 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 007f7190 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f7190 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f7190 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f71e8 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 007f71e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f71e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f71e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f7190 bytes 29813891
+ 007f71e8 bytes 29c13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0db57045e41adddf106028b005536cc4"></a>

### [`007f71a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f71a4.md) → [`007f71fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f71fc.md) FUN_007f71fc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0046b880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b880.md) [`0046d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md) [`008b6d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6d9c.md) [`008b6e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6e58.md) [`008b6e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6e60.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0046b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b8c0.md) [`0046d9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d9b4.md) [`008b6df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6df4.md) [`008b6eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6eb0.md) [`008b6eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6eb8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f724c",
      "incomplete_value": true,
      "site": "007f725c",
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
                "register:4040:8"
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
    "old": {
      "definition_site": "007f71f4",
      "incomplete_value": true,
      "site": "007f7204",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f7254",
      "incomplete_value": false,
      "site": "007f725c",
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
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f71fc",
      "incomplete_value": false,
      "site": "007f7204",
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
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f7248",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f724c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007f7254",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f7248",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f724c",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f7254",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f7204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f71a4.md#insn-007f7204) · [`007f71d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f71a4.md#insn-007f71d4) · [`007f71e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f71a4.md#insn-007f71e4)
- 新版 `007f725c`（命令位置の公開資料なし） · `007f722c`（命令位置の公開資料なし） · `007f723c`（命令位置の公開資料なし）

~~~diff
- 007f7204 ["INT_ADD", "register:40f0:8", ["const:7f7204:8", "const:4:8"]]
- 007f7204 ["CALL", null, ["callee:00c586e0:8"]]
+ 007f725c ["INT_ADD", "register:40f0:8", ["const:7f725c:8", "const:4:8"]]
+ 007f725c ["CALL", null, ["callee:00c586e0:8"]]
- 007f7204 bytes 03851194
+ 007f725c bytes 21851194
- 007f71d4 ["INT_ADD", "register:40f0:8", ["const:7f71d4:8", "const:4:8"]]
- 007f71d4 ["CALL", null, ["callee:008b7a20:8"]]
+ 007f722c ["INT_ADD", "register:40f0:8", ["const:7f722c:8", "const:4:8"]]
+ 007f722c ["CALL", null, ["callee:008b7a20:8"]]
- 007f71d4 bytes fd010394
+ 007f722c bytes fd010394
- 007f71e4 ["INT_ADD", "register:40f0:8", ["const:7f71e4:8", "const:4:8"]]
- 007f71e4 ["CALL", null, ["callee:008b6df4:8"]]
+ 007f723c ["INT_ADD", "register:40f0:8", ["const:7f723c:8", "const:4:8"]]
+ 007f723c ["CALL", null, ["callee:008b6df4:8"]]
- 007f71e4 bytes eefe0294
+ 007f723c bytes eefe0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2a0b726d2f57551115fae70c617cb3e"></a>

### [`007f72e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f72e8.md) → [`007f7340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7340.md) FUN_007f7340

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f7364",
      "incomplete_value": true,
      "site": "007f7364",
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
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f730c",
      "incomplete_value": true,
      "site": "007f730c",
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
      "007f7364",
      "DATA",
      [
        "storage",
        "00c7beb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7364",
      "DATA",
      [
        "storage",
        "00c7bf80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f72fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f72e8.md#insn-007f72fc) · [`007f7308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f72e8.md#insn-007f7308)
- 新版 `007f7354`（命令位置の公開資料なし） · `007f7360`（命令位置の公開資料なし）

~~~diff
- 007f72fc ["INT_ADD", "register:40f0:8", ["const:7f72fc:8", "const:4:8"]]
- 007f72fc ["CALL", null, ["callee:00c57f60:8"]]
+ 007f7354 ["INT_ADD", "register:40f0:8", ["const:7f7354:8", "const:4:8"]]
+ 007f7354 ["CALL", null, ["callee:00c57f60:8"]]
- 007f72fc bytes e5821194
+ 007f7354 bytes 03831194
- 007f7308 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 007f7308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f7308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f7308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f7360 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 007f7360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f7308 bytes 08c13a91
+ 007f7360 bytes 08013e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95f777474b4132459c10e47012f591c5"></a>

### [`007f731c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f731c.md) → [`007f7374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7374.md) FUN_007f7374

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
      "definition_site": "007f7380",
      "incomplete_value": false,
      "site": "007f7380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7328",
      "incomplete_value": false,
      "site": "007f7328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f7380",
      "DATA",
      [
        "storage",
        "00c7beb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7380",
      "DATA",
      [
        "storage",
        "00c7bf80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f7324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f731c.md#insn-007f7324)
- 新版 `007f737c`（命令位置の公開資料なし）

~~~diff
- 007f7324 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 007f7324 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f7324 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f7324 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f737c ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 007f737c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f737c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f737c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f7324 bytes 29c13a91
+ 007f737c bytes 29013e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aed155fd78960a7daa18d8bc52073d3"></a>

### [`007f7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7390.md) → [`007f73e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f73e8.md) FUN_007f73e8

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
      "definition_site": "007f73fc",
      "incomplete_value": false,
      "site": "007f7400",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f73a4",
      "incomplete_value": false,
      "site": "007f73a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "007f7400",
      "DATA",
      [
        "storage",
        "00c7bf30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7400",
      "DATA",
      [
        "storage",
        "00c7c000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f739c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7390.md#insn-007f739c) · [`007f73a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7390.md#insn-007f73a0) · [`007f73a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7390.md#insn-007f73a4)
- 新版 `007f73f4`（命令位置の公開資料なし） · `007f73f8`（命令位置の公開資料なし） · `007f73fc`（命令位置の公開資料なし）

~~~diff
- 007f739c ["INT_ADD", "register:40f0:8", ["const:7f739c:8", "const:4:8"]]
- 007f739c ["CALL", null, ["callee:00c57f60:8"]]
+ 007f73f4 ["INT_ADD", "register:40f0:8", ["const:7f73f4:8", "const:4:8"]]
+ 007f73f4 ["CALL", null, ["callee:00c57f60:8"]]
- 007f739c bytes bd821194
+ 007f73f4 bytes db821194
- 007f73a0 ["COPY", "register:4040:8", ["const:c7b000:8"]]
+ 007f73f8 ["COPY", "register:4040:8", ["const:c7c000:8"]]
- 007f73a0 bytes 28240090
+ 007f73f8 bytes 282400b0
- 007f73a4 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 007f73a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f73a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f73a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f73fc ["COPY", "tmp:0:8", ["const:0:8"]]
+ 007f73fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f73fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f73fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f73a4 bytes 08c13c91
+ 007f73fc bytes 08010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-813002a9c089784b6ba9413da381afca"></a>

### [`007f73b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f73b4.md) → [`007f740c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f740c.md) FUN_007f740c

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
      "definition_site": "007f7410",
      "incomplete_value": false,
      "site": "007f7414",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f73b8",
      "incomplete_value": false,
      "site": "007f73bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f7414",
      "DATA",
      [
        "storage",
        "00c7bf30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7414",
      "DATA",
      [
        "storage",
        "00c7c000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f73b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f73b4.md#insn-007f73b4) · [`007f73b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f73b4.md#insn-007f73b8)
- 新版 `007f740c`（命令位置の公開資料なし） · `007f7410`（命令位置の公開資料なし）

~~~diff
- 007f73b4 ["COPY", "register:4040:8", ["const:c7b000:8"]]
+ 007f740c ["COPY", "register:4040:8", ["const:c7c000:8"]]
- 007f73b4 bytes 28240090
+ 007f740c bytes 282400b0
- 007f73b8 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 007f73b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f73b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f73b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f7410 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 007f7410 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7410 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7410 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f73b8 bytes 08c13c91
+ 007f7410 bytes 08010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de79a920bb42d365b4b7523dffa19a4a"></a>

### [`007f73cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f73cc.md) → [`007f7424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7424.md) FUN_007f7424

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
      "site": "007f7448",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f73f0",
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
      "007f7448",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f7448",
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

- 旧版 [`007f73f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f73cc.md#insn-007f73f0) · [`007f73fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f73cc.md#insn-007f73fc)
- 新版 `007f7448`（命令位置の公開資料なし） · `007f7454`（命令位置の公開資料なし）

~~~diff
- 007f73f0 ["INT_ADD", "register:40f0:8", ["const:7f73f0:8", "const:4:8"]]
- 007f73f0 ["CALL", null, ["ram:47acf4:8"]]
+ 007f7448 ["INT_ADD", "register:40f0:8", ["const:7f7448:8", "const:4:8"]]
+ 007f7448 ["CALL", null, ["ram:47ad34:8"]]
- 007f73f0 bytes 410ef297
+ 007f7448 bytes 3b0ef297
- 007f73fc ["INT_ADD", "register:40f0:8", ["const:7f73fc:8", "const:4:8"]]
- 007f73fc ["CALL", null, ["callee:0047ce14:8"]]
+ 007f7454 ["INT_ADD", "register:40f0:8", ["const:7f7454:8", "const:4:8"]]
+ 007f7454 ["CALL", null, ["callee:0047ce14:8"]]
- 007f73fc bytes 7616f297
+ 007f7454 bytes 7016f297
~~~


<a id="compare-b9cc80301e88a652184871f7ebc3bb3a"></a>

### [`007f7440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7440.md) → [`007f7498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7498.md) FUN_007f7498

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
      "definition_site": "007f74ac",
      "incomplete_value": false,
      "site": "007f74b0",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7454",
      "incomplete_value": false,
      "site": "007f7458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f74b0",
      "DATA",
      [
        "storage",
        "00c7bfb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f74b0",
      "DATA",
      [
        "storage",
        "00c7c080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f744c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7440.md#insn-007f744c) · [`007f7450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7440.md#insn-007f7450) · [`007f7454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7440.md#insn-007f7454)
- 新版 `007f74a4`（命令位置の公開資料なし） · `007f74a8`（命令位置の公開資料なし） · `007f74ac`（命令位置の公開資料なし）

~~~diff
- 007f744c ["INT_ADD", "register:40f0:8", ["const:7f744c:8", "const:4:8"]]
- 007f744c ["CALL", null, ["callee:00c57f60:8"]]
+ 007f74a4 ["INT_ADD", "register:40f0:8", ["const:7f74a4:8", "const:4:8"]]
+ 007f74a4 ["CALL", null, ["callee:00c57f60:8"]]
- 007f744c bytes 91821194
+ 007f74a4 bytes af821194
- 007f7450 ["COPY", "register:4040:8", ["const:c7b000:8"]]
+ 007f74a8 ["COPY", "register:4040:8", ["const:c7c000:8"]]
- 007f7450 bytes 28240090
+ 007f74a8 bytes 282400b0
- 007f7454 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 007f7454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f7454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f7454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f74ac ["COPY", "tmp:0:8", ["const:80:8"]]
+ 007f74ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f74ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f74ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f7454 bytes 08c13e91
+ 007f74ac bytes 08010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-156599bf0e4f3289951c843cca719643"></a>

### [`007f7464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7464.md) → [`007f74bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f74bc.md) FUN_007f74bc

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
      "definition_site": "007f74c0",
      "incomplete_value": false,
      "site": "007f74c4",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7468",
      "incomplete_value": false,
      "site": "007f746c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f74c4",
      "DATA",
      [
        "storage",
        "00c7bfb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f74c4",
      "DATA",
      [
        "storage",
        "00c7c080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f7464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7464.md#insn-007f7464) · [`007f7468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7464.md#insn-007f7468)
- 新版 `007f74bc`（命令位置の公開資料なし） · `007f74c0`（命令位置の公開資料なし）

~~~diff
- 007f7464 ["COPY", "register:4040:8", ["const:c7b000:8"]]
+ 007f74bc ["COPY", "register:4040:8", ["const:c7c000:8"]]
- 007f7464 bytes 28240090
+ 007f74bc bytes 282400b0
- 007f7468 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 007f7468 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f7468 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f7468 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f74c0 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 007f74c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f74c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f74c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f7468 bytes 08c13e91
+ 007f74c0 bytes 08010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91638bbf5f5b352128179b9c87f548c8"></a>

### [`007f747c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f747c.md) → [`007f74d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f74d4.md) FUN_007f74d4

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
      "site": "007f74f8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f74a0",
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
      "007f74f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f74f8",
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

- 旧版 [`007f74a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f747c.md#insn-007f74a0) · [`007f74ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f747c.md#insn-007f74ac)
- 新版 `007f74f8`（命令位置の公開資料なし） · `007f7504`（命令位置の公開資料なし）

~~~diff
- 007f74a0 ["INT_ADD", "register:40f0:8", ["const:7f74a0:8", "const:4:8"]]
- 007f74a0 ["CALL", null, ["ram:47acf4:8"]]
+ 007f74f8 ["INT_ADD", "register:40f0:8", ["const:7f74f8:8", "const:4:8"]]
+ 007f74f8 ["CALL", null, ["ram:47ad34:8"]]
- 007f74a0 bytes 150ef297
+ 007f74f8 bytes 0f0ef297
- 007f74ac ["INT_ADD", "register:40f0:8", ["const:7f74ac:8", "const:4:8"]]
- 007f74ac ["CALL", null, ["callee:0047ce14:8"]]
+ 007f7504 ["INT_ADD", "register:40f0:8", ["const:7f7504:8", "const:4:8"]]
+ 007f7504 ["CALL", null, ["callee:0047ce14:8"]]
- 007f74ac bytes 4a16f297
+ 007f7504 bytes 4416f297
~~~


<a id="compare-42c60c9e9cd66fa034e0b6f5c74f751c"></a>

### [`007f74f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f74f0.md) → [`007f7548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7548.md) FUN_007f7548

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
      "definition_site": "007f755c",
      "incomplete_value": false,
      "site": "007f7560",
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
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7504",
      "incomplete_value": false,
      "site": "007f7508",
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
      "007f7560",
      "DATA",
      [
        "storage",
        "00c7c030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7560",
      "DATA",
      [
        "storage",
        "00c7c100",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f74fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f74f0.md#insn-007f74fc) · [`007f7504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f74f0.md#insn-007f7504)
- 新版 `007f7554`（命令位置の公開資料なし） · `007f755c`（命令位置の公開資料なし）

~~~diff
- 007f74fc ["INT_ADD", "register:40f0:8", ["const:7f74fc:8", "const:4:8"]]
- 007f74fc ["CALL", null, ["callee:00c57f60:8"]]
+ 007f7554 ["INT_ADD", "register:40f0:8", ["const:7f7554:8", "const:4:8"]]
+ 007f7554 ["CALL", null, ["callee:00c57f60:8"]]
- 007f74fc bytes 65821194
+ 007f7554 bytes 83821194
- 007f7504 ["COPY", "tmp:0:8", ["const:30:8"]]
- 007f7504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f7504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f7504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f755c ["COPY", "tmp:0:8", ["const:100:8"]]
+ 007f755c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f755c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f755c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f7504 bytes 08c10091
+ 007f755c bytes 08010491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a231b5e819d265330651dc80e0a6dada"></a>

### [`007f7514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7514.md) → [`007f756c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f756c.md) FUN_007f756c

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
      "definition_site": "007f7570",
      "incomplete_value": false,
      "site": "007f7574",
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
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7518",
      "incomplete_value": false,
      "site": "007f751c",
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
      "007f7574",
      "DATA",
      [
        "storage",
        "00c7c030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7574",
      "DATA",
      [
        "storage",
        "00c7c100",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f7518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7514.md#insn-007f7518)
- 新版 `007f7570`（命令位置の公開資料なし）

~~~diff
- 007f7518 ["COPY", "tmp:0:8", ["const:30:8"]]
- 007f7518 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f7518 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f7518 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f7570 ["COPY", "tmp:0:8", ["const:100:8"]]
+ 007f7570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f7518 bytes 08c10091
+ 007f7570 bytes 08010491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4263ca07b95dc626fa25bc5626e0abd3"></a>

### [`007f752c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f752c.md) → [`007f7584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7584.md) FUN_007f7584

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
      "site": "007f75a8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f7550",
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
      "007f75a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f75a8",
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

- 旧版 [`007f7550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f752c.md#insn-007f7550) · [`007f755c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f752c.md#insn-007f755c)
- 新版 `007f75a8`（命令位置の公開資料なし） · `007f75b4`（命令位置の公開資料なし）

~~~diff
- 007f7550 ["INT_ADD", "register:40f0:8", ["const:7f7550:8", "const:4:8"]]
- 007f7550 ["CALL", null, ["ram:47acf4:8"]]
+ 007f75a8 ["INT_ADD", "register:40f0:8", ["const:7f75a8:8", "const:4:8"]]
+ 007f75a8 ["CALL", null, ["ram:47ad34:8"]]
- 007f7550 bytes e90df297
+ 007f75a8 bytes e30df297
- 007f755c ["INT_ADD", "register:40f0:8", ["const:7f755c:8", "const:4:8"]]
- 007f755c ["CALL", null, ["callee:0047ce14:8"]]
+ 007f75b4 ["INT_ADD", "register:40f0:8", ["const:7f75b4:8", "const:4:8"]]
+ 007f75b4 ["CALL", null, ["callee:0047ce14:8"]]
- 007f755c bytes 1e16f297
+ 007f75b4 bytes 1816f297
~~~


<a id="compare-de72731b6c8ad4d8b1ebd33c116b2930"></a>

### [`007f75a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f75a0.md) → [`007f75f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f75f8.md) FUN_007f75f8

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
      "definition_site": "007f760c",
      "incomplete_value": false,
      "site": "007f7610",
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
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f75b4",
      "incomplete_value": false,
      "site": "007f75b8",
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
      "007f7610",
      "DATA",
      [
        "storage",
        "00c7c0b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7610",
      "DATA",
      [
        "storage",
        "00c7c180",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f75ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f75a0.md#insn-007f75ac) · [`007f75b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f75a0.md#insn-007f75b4)
- 新版 `007f7604`（命令位置の公開資料なし） · `007f760c`（命令位置の公開資料なし）

~~~diff
- 007f75ac ["INT_ADD", "register:40f0:8", ["const:7f75ac:8", "const:4:8"]]
- 007f75ac ["CALL", null, ["callee:00c57f60:8"]]
+ 007f7604 ["INT_ADD", "register:40f0:8", ["const:7f7604:8", "const:4:8"]]
+ 007f7604 ["CALL", null, ["callee:00c57f60:8"]]
- 007f75ac bytes 39821194
+ 007f7604 bytes 57821194
- 007f75b4 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 007f75b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f75b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f75b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f760c ["COPY", "tmp:0:8", ["const:180:8"]]
+ 007f760c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f760c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f760c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f75b4 bytes 08c10291
+ 007f760c bytes 08010691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9717e05261f217955535317669034e4"></a>

### [`007f75c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f75c4.md) → [`007f761c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f761c.md) FUN_007f761c

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
      "definition_site": "007f7620",
      "incomplete_value": false,
      "site": "007f7624",
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
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f75c8",
      "incomplete_value": false,
      "site": "007f75cc",
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
      "007f7624",
      "DATA",
      [
        "storage",
        "00c7c0b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7624",
      "DATA",
      [
        "storage",
        "00c7c180",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f75c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f75c4.md#insn-007f75c8)
- 新版 `007f7620`（命令位置の公開資料なし）

~~~diff
- 007f75c8 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 007f75c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f75c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f75c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f7620 ["COPY", "tmp:0:8", ["const:180:8"]]
+ 007f7620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f75c8 bytes 08c10291
+ 007f7620 bytes 08010691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3176229b3ea9c7bfaa3746f821fa0d02"></a>

### [`007f75dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f75dc.md) → [`007f7634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7634.md) FUN_007f7634

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
      "site": "007f7658",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f7600",
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
      "007f7658",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f7658",
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

- 旧版 [`007f7600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f75dc.md#insn-007f7600) · [`007f760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f75dc.md#insn-007f760c)
- 新版 `007f7658`（命令位置の公開資料なし） · `007f7664`（命令位置の公開資料なし）

~~~diff
- 007f7600 ["INT_ADD", "register:40f0:8", ["const:7f7600:8", "const:4:8"]]
- 007f7600 ["CALL", null, ["ram:47acf4:8"]]
+ 007f7658 ["INT_ADD", "register:40f0:8", ["const:7f7658:8", "const:4:8"]]
+ 007f7658 ["CALL", null, ["ram:47ad34:8"]]
- 007f7600 bytes bd0df297
+ 007f7658 bytes b70df297
- 007f760c ["INT_ADD", "register:40f0:8", ["const:7f760c:8", "const:4:8"]]
- 007f760c ["CALL", null, ["callee:0047ce14:8"]]
+ 007f7664 ["INT_ADD", "register:40f0:8", ["const:7f7664:8", "const:4:8"]]
+ 007f7664 ["CALL", null, ["callee:0047ce14:8"]]
- 007f760c bytes f215f297
+ 007f7664 bytes ec15f297
~~~


<a id="compare-a6d493fb6060b5a9a608fe95389c8eeb"></a>

### [`007f7650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7650.md) → [`007f76a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f76a8.md) FUN_007f76a8

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
      "definition_site": "007f76cc",
      "incomplete_value": false,
      "site": "007f76cc",
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
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7674",
      "incomplete_value": false,
      "site": "007f7674",
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
      "007f76cc",
      "DATA",
      [
        "storage",
        "00c7c130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f76cc",
      "DATA",
      [
        "storage",
        "00c7c200",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f7664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7650.md#insn-007f7664) · [`007f7670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7650.md#insn-007f7670)
- 新版 `007f76bc`（命令位置の公開資料なし） · `007f76c8`（命令位置の公開資料なし）

~~~diff
- 007f7664 ["INT_ADD", "register:40f0:8", ["const:7f7664:8", "const:4:8"]]
- 007f7664 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f76bc ["INT_ADD", "register:40f0:8", ["const:7f76bc:8", "const:4:8"]]
+ 007f76bc ["CALL", null, ["callee:00c57f60:8"]]
- 007f7664 bytes 0b821194
+ 007f76bc bytes 29821194
- 007f7670 ["COPY", "tmp:0:8", ["const:130:8"]]
- 007f7670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f7670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f7670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f76c8 ["COPY", "tmp:0:8", ["const:200:8"]]
+ 007f76c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f76c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f76c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f7670 bytes 08c10491
+ 007f76c8 bytes 08010891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62a84f98b9a35e5f55d1ed18e8d9b851"></a>

### [`007f7684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7684.md) → [`007f76dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f76dc.md) FUN_007f76dc

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
      "definition_site": "007f76e8",
      "incomplete_value": false,
      "site": "007f76e8",
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
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7690",
      "incomplete_value": false,
      "site": "007f7690",
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
      "007f76e8",
      "DATA",
      [
        "storage",
        "00c7c130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f76e8",
      "DATA",
      [
        "storage",
        "00c7c200",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f768c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7684.md#insn-007f768c)
- 新版 `007f76e4`（命令位置の公開資料なし）

~~~diff
- 007f768c ["COPY", "tmp:0:8", ["const:130:8"]]
- 007f768c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f768c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f768c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f76e4 ["COPY", "tmp:0:8", ["const:200:8"]]
+ 007f76e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f76e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f76e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f768c bytes 29c10491
+ 007f76e4 bytes 29010891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f24c1552150b57d1fd375f56cc118ab0"></a>

### [`007f76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f76a0.md) → [`007f76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f76f8.md) FUN_007f76f8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007f7984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7984.md) [`007f7988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7988.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`007f79dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f79dc.md) [`007f79e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f79e0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f7790",
      "incomplete_value": true,
      "site": "007f7790",
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
                "const:b51:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7738",
      "incomplete_value": true,
      "site": "007f7738",
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
                "const:bad:8"
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
      "definition_site": "007f7794",
      "incomplete_value": true,
      "site": "007f7794",
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
      "definition_site": "007f773c",
      "incomplete_value": true,
      "site": "007f773c",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f7730",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f76d8",
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
      "007f7730",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f777c",
      "READ",
      [
        "storage",
        "002acbad",
        null,
        "string"
      ]
    ],
    [
      "007f7784",
      "READ",
      [
        "storage",
        "002acbb3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f7730",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f777c",
      "READ",
      [
        "storage",
        "002acb51",
        null,
        "string"
      ]
    ],
    [
      "007f7784",
      "READ",
      [
        "storage",
        "002acb57",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f76d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f76a0.md#insn-007f76d8) · [`007f76e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f76a0.md#insn-007f76e4) · [`007f7714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f76a0.md#insn-007f7714)
- 新版 `007f7730`（命令位置の公開資料なし） · `007f773c`（命令位置の公開資料なし） · `007f776c`（命令位置の公開資料なし）

~~~diff
- 007f76d8 ["INT_ADD", "register:40f0:8", ["const:7f76d8:8", "const:4:8"]]
- 007f76d8 ["CALL", null, ["ram:47acf4:8"]]
+ 007f7730 ["INT_ADD", "register:40f0:8", ["const:7f7730:8", "const:4:8"]]
+ 007f7730 ["CALL", null, ["ram:47ad34:8"]]
- 007f76d8 bytes 870df297
+ 007f7730 bytes 810df297
- 007f76e4 ["INT_ADD", "register:40f0:8", ["const:7f76e4:8", "const:4:8"]]
- 007f76e4 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f773c ["INT_ADD", "register:40f0:8", ["const:7f773c:8", "const:4:8"]]
+ 007f773c ["CALL", null, ["callee:0047ce14:8"]]
- 007f76e4 bytes bc15f297
+ 007f773c bytes b615f297
- 007f7714 ["INT_ADD", "register:40f0:8", ["const:7f7714:8", "const:4:8"]]
- 007f7714 ["CALL", null, ["callee:00851550:8"]]
+ 007f776c ["INT_ADD", "register:40f0:8", ["const:7f776c:8", "const:4:8"]]
+ 007f776c ["CALL", null, ["callee:00851550:8"]]
- 007f7714 bytes 79670194
+ 007f776c bytes 79670194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5deed0857167f7f21a7d5fce29308e49"></a>

### [`007f7970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7970.md) → [`007f79c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f79c8.md) FUN_007f79c8

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
      "definition_site": "007f79d4",
      "incomplete_value": false,
      "site": "007f79d4",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f797c",
      "incomplete_value": false,
      "site": "007f797c",
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
            "const:1a0:8"
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
      "007f79d4",
      "DATA",
      [
        "storage",
        "00c7c1a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f79d4",
      "DATA",
      [
        "storage",
        "00c7c270",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f7978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7970.md#insn-007f7978)
- 新版 `007f79d0`（命令位置の公開資料なし）

~~~diff
- 007f7978 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 007f7978 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f7978 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f7978 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f79d0 ["COPY", "tmp:0:8", ["const:270:8"]]
+ 007f79d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f79d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f79d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f7978 bytes 29810691
+ 007f79d0 bytes 29c10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88cb74508de96e497ce45b6b071364b8"></a>

### [`007f798c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f798c.md) → [`007f79e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f79e4.md) FUN_007f79e4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007f7ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7ce4.md)
- 新版 呼出元 0件  · 呼出先 17件 [`0046cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`007f7d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7d3c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.02% / 新版 94.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f7a84",
      "incomplete_value": false,
      "site": "007f7a84",
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
            "const:2e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7a2c",
      "incomplete_value": false,
      "site": "007f7a2c",
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
            "const:210:8"
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
      "definition_site": "007f7ab4",
      "incomplete_value": true,
      "site": "007f7ab4",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7a5c",
      "incomplete_value": true,
      "site": "007f7a5c",
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
            "const:390:8"
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
      "definition_site": "007f7ad4",
      "incomplete_value": false,
      "site": "007f7ad4",
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
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7a7c",
      "incomplete_value": false,
      "site": "007f7a7c",
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
            "const:410:8"
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
      "007f7a1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f7a84",
      "DATA",
      [
        "storage",
        "00c7c210",
        null,
        "undefined *"
      ]
    ],
    [
      "007f7ab4",
      "DATA",
      [
        "storage",
        "00c7c390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7a1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f7a84",
      "DATA",
      [
        "storage",
        "00c7c2e0",
        null,
        "undefined *"
      ]
    ],
    [
      "007f7ab4",
      "DATA",
      [
        "storage",
        "00c7c460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f79c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f798c.md#insn-007f79c4) · [`007f7a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f798c.md#insn-007f7a1c) · [`007f7a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f798c.md#insn-007f7a24)
- 新版 `007f7a1c`（命令位置の公開資料なし） · `007f7a74`（命令位置の公開資料なし） · `007f7a7c`（命令位置の公開資料なし）

~~~diff
- 007f79c4 ["INT_ADD", "register:40f0:8", ["const:7f79c4:8", "const:4:8"]]
- 007f79c4 ["CALL", null, ["ram:47acf4:8"]]
+ 007f7a1c ["INT_ADD", "register:40f0:8", ["const:7f7a1c:8", "const:4:8"]]
+ 007f7a1c ["CALL", null, ["ram:47ad34:8"]]
- 007f79c4 bytes cc0cf297
+ 007f7a1c bytes c60cf297
- 007f7a1c ["INT_ADD", "register:40f0:8", ["const:7f7a1c:8", "const:4:8"]]
- 007f7a1c ["CALL", null, ["callee:0046cac4:8"]]
+ 007f7a74 ["INT_ADD", "register:40f0:8", ["const:7f7a74:8", "const:4:8"]]
+ 007f7a74 ["CALL", null, ["callee:0046cac4:8"]]
- 007f7a1c bytes 1ad4f197
+ 007f7a74 bytes 14d4f197
- 007f7a24 ["COPY", "tmp:0:8", ["const:210:8"]]
- 007f7a24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f7a24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f7a24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f7a7c ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 007f7a7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7a7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7a7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f7a24 bytes 08410891
+ 007f7a7c bytes 08810b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1630639dcfd618ae882c4c23accacd8a"></a>

### [`007f7c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7c9c.md) → [`007f7cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7cf4.md) FUN_007f7cf4

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
      "definition_site": "007f7d18",
      "incomplete_value": false,
      "site": "007f7d18",
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
            "const:2e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7cc0",
      "incomplete_value": false,
      "site": "007f7cc0",
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
      "007f7d18",
      "DATA",
      [
        "storage",
        "00c7c210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7d18",
      "DATA",
      [
        "storage",
        "00c7c2e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f7cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7c9c.md#insn-007f7cb0) · [`007f7cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7c9c.md#insn-007f7cbc)
- 新版 `007f7d08`（命令位置の公開資料なし） · `007f7d14`（命令位置の公開資料なし）

~~~diff
- 007f7cb0 ["INT_ADD", "register:40f0:8", ["const:7f7cb0:8", "const:4:8"]]
- 007f7cb0 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f7d08 ["INT_ADD", "register:40f0:8", ["const:7f7d08:8", "const:4:8"]]
+ 007f7d08 ["CALL", null, ["callee:00c57f60:8"]]
- 007f7cb0 bytes 78801194
+ 007f7d08 bytes 96801194
- 007f7cbc ["COPY", "tmp:0:8", ["const:210:8"]]
- 007f7cbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f7cbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f7cbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f7d14 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 007f7d14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7d14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7d14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f7cbc bytes 08410891
+ 007f7d14 bytes 08810b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d7a95eb4db23ea52f146e47025d0556"></a>

### [`007f7cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7cec.md) → [`007f7d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7d44.md) FUN_007f7d44

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007f7f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7f8c.md) [`007f7f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7f90.md) [`007f8048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8048.md) [`007f804c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f804c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`007f7fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7fe4.md) [`007f7fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7fe8.md) [`007f80a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f80a0.md) [`007f80a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f80a4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.26% / 新版 93.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f7df4",
      "incomplete_value": false,
      "site": "007f7df4",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7d9c",
      "incomplete_value": false,
      "site": "007f7d9c",
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
            "const:300:8"
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
      "007f7d84",
      "READ",
      [
        "storage",
        "002c03c0",
        null,
        "string"
      ]
    ],
    [
      "007f7d8c",
      "READ",
      [
        "storage",
        "002c03c6",
        null,
        "string"
      ]
    ],
    [
      "007f7db8",
      "DATA",
      [
        "storage",
        "00c7c280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7d84",
      "READ",
      [
        "storage",
        "002c0400",
        null,
        "string"
      ]
    ],
    [
      "007f7d8c",
      "READ",
      [
        "storage",
        "002c0406",
        null,
        "string"
      ]
    ],
    [
      "007f7db8",
      "DATA",
      [
        "storage",
        "00c7c350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f7d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7cec.md#insn-007f7d1c) · [`007f7d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7cec.md#insn-007f7d28) · [`007f7d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7cec.md#insn-007f7d50)
- 新版 `007f7d74`（命令位置の公開資料なし） · `007f7d80`（命令位置の公開資料なし） · `007f7da8`（命令位置の公開資料なし）

~~~diff
- 007f7d1c ["INT_ADD", "register:40f0:8", ["const:7f7d1c:8", "const:4:8"]]
- 007f7d1c ["CALL", null, ["callee:00851550:8"]]
+ 007f7d74 ["INT_ADD", "register:40f0:8", ["const:7f7d74:8", "const:4:8"]]
+ 007f7d74 ["CALL", null, ["callee:00851550:8"]]
- 007f7d1c bytes f7650194
+ 007f7d74 bytes f7650194
- 007f7d28 ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 007f7d28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f7d28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f7d28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f7d80 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 007f7d80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f7d80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f7d80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f7d28 bytes 29010f91
+ 007f7d80 bytes 29011091
- 007f7d50 ["INT_ADD", "register:40f0:8", ["const:7f7d50:8", "const:4:8"]]
- 007f7d50 ["CALL", null, ["callee:0048ce94:8"]]
+ 007f7da8 ["INT_ADD", "register:40f0:8", ["const:7f7da8:8", "const:4:8"]]
+ 007f7da8 ["CALL", null, ["callee:0048ce94:8"]]
- 007f7d50 bytes 4154f297
+ 007f7da8 bytes 3b54f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8199b4711fb1ffb26c3e42170411aa82"></a>

### [`007f7f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7f44.md) → [`007f7f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7f9c.md) FUN_007f7f9c

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
      "definition_site": "007f7fc0",
      "incomplete_value": false,
      "site": "007f7fc0",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7f68",
      "incomplete_value": false,
      "site": "007f7f68",
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
            "const:280:8"
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
      "007f7fc0",
      "DATA",
      [
        "storage",
        "00c7c280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7fc0",
      "DATA",
      [
        "storage",
        "00c7c350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f7f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7f44.md#insn-007f7f58) · [`007f7f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7f44.md#insn-007f7f64)
- 新版 `007f7fb0`（命令位置の公開資料なし） · `007f7fbc`（命令位置の公開資料なし）

~~~diff
- 007f7f58 ["INT_ADD", "register:40f0:8", ["const:7f7f58:8", "const:4:8"]]
- 007f7f58 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f7fb0 ["INT_ADD", "register:40f0:8", ["const:7f7fb0:8", "const:4:8"]]
+ 007f7fb0 ["CALL", null, ["callee:00c57f60:8"]]
- 007f7f58 bytes ce7f1194
+ 007f7fb0 bytes ec7f1194
- 007f7f64 ["COPY", "tmp:0:8", ["const:280:8"]]
- 007f7f64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f7f64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f7f64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f7fbc ["COPY", "tmp:0:8", ["const:350:8"]]
+ 007f7fbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7fbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f7fbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f7f64 bytes 08010a91
+ 007f7fbc bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e18c6874ee0bdf51b90258971f1bbc3"></a>

### [`007f7f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7f78.md) → [`007f7fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7fd0.md) FUN_007f7fd0

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
      "definition_site": "007f7fdc",
      "incomplete_value": false,
      "site": "007f7fdc",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f7f84",
      "incomplete_value": false,
      "site": "007f7f84",
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
            "const:280:8"
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
      "007f7fdc",
      "DATA",
      [
        "storage",
        "00c7c280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f7fdc",
      "DATA",
      [
        "storage",
        "00c7c350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f7f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7f78.md#insn-007f7f80)
- 新版 `007f7fd8`（命令位置の公開資料なし）

~~~diff
- 007f7f80 ["COPY", "tmp:0:8", ["const:280:8"]]
- 007f7f80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f7f80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f7f80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f7fd8 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 007f7fd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f7fd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f7fd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f7f80 bytes 29010a91
+ 007f7fd8 bytes 29410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-091e594c8c0996924827330eba28f641"></a>

### [`007f7f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7f94.md) → [`007f7fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7fec.md) FUN_007f7fec

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
      "site": "007f8008",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f7fb0",
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
      "007f8008",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f8008",
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

- 旧版 [`007f7fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7f94.md#insn-007f7fb0) · [`007f7fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7f94.md#insn-007f7fbc)
- 新版 `007f8008`（命令位置の公開資料なし） · `007f8014`（命令位置の公開資料なし）

~~~diff
- 007f7fb0 ["INT_ADD", "register:40f0:8", ["const:7f7fb0:8", "const:4:8"]]
- 007f7fb0 ["CALL", null, ["ram:47acf4:8"]]
+ 007f8008 ["INT_ADD", "register:40f0:8", ["const:7f8008:8", "const:4:8"]]
+ 007f8008 ["CALL", null, ["ram:47ad34:8"]]
- 007f7fb0 bytes 510bf297
+ 007f8008 bytes 4b0bf297
- 007f7fbc ["INT_ADD", "register:40f0:8", ["const:7f7fbc:8", "const:4:8"]]
- 007f7fbc ["CALL", null, ["callee:0047ce14:8"]]
+ 007f8014 ["INT_ADD", "register:40f0:8", ["const:7f8014:8", "const:4:8"]]
+ 007f8014 ["CALL", null, ["callee:0047ce14:8"]]
- 007f7fbc bytes 8613f297
+ 007f8014 bytes 8013f297
~~~


<a id="compare-4f91eba841d62a51f5d34e9dce457245"></a>

### [`007f8000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8000.md) → [`007f8058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8058.md) FUN_007f8058

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
      "definition_site": "007f807c",
      "incomplete_value": false,
      "site": "007f807c",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8024",
      "incomplete_value": false,
      "site": "007f8024",
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
            "const:300:8"
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
      "007f807c",
      "DATA",
      [
        "storage",
        "00c7c300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f807c",
      "DATA",
      [
        "storage",
        "00c7c3d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8000.md#insn-007f8014) · [`007f8020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8000.md#insn-007f8020)
- 新版 `007f806c`（命令位置の公開資料なし） · `007f8078`（命令位置の公開資料なし）

~~~diff
- 007f8014 ["INT_ADD", "register:40f0:8", ["const:7f8014:8", "const:4:8"]]
- 007f8014 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f806c ["INT_ADD", "register:40f0:8", ["const:7f806c:8", "const:4:8"]]
+ 007f806c ["CALL", null, ["callee:00c57f60:8"]]
- 007f8014 bytes 9f7f1194
+ 007f806c bytes bd7f1194
- 007f8020 ["COPY", "tmp:0:8", ["const:300:8"]]
- 007f8020 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8020 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8020 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8078 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 007f8078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8020 bytes 08010c91
+ 007f8078 bytes 08410f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6f0c8f0753992e7974e6b5e46c151cf"></a>

### [`007f8034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8034.md) → [`007f808c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f808c.md) FUN_007f808c

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
      "definition_site": "007f8098",
      "incomplete_value": false,
      "site": "007f8098",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8040",
      "incomplete_value": false,
      "site": "007f8040",
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
            "const:300:8"
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
      "007f8098",
      "DATA",
      [
        "storage",
        "00c7c300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8098",
      "DATA",
      [
        "storage",
        "00c7c3d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f803c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8034.md#insn-007f803c)
- 新版 `007f8094`（命令位置の公開資料なし）

~~~diff
- 007f803c ["COPY", "tmp:0:8", ["const:300:8"]]
- 007f803c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f803c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f803c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f8094 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 007f8094 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f8094 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f8094 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f803c bytes 29010c91
+ 007f8094 bytes 29410f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a9503a6e814ade7cf40ee4f4f27ccf0"></a>

### [`007f8050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8050.md) → [`007f80a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f80a8.md) FUN_007f80a8

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 23件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046b880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b880.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md) [`0046d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md)
- 新版 呼出元 0件  · 呼出先 23件 [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b8c0.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md) [`0046d9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d9b4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 9件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f80f0",
      "incomplete_value": true,
      "site": "007f80f0",
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
      "definition_site": "007f8098",
      "incomplete_value": true,
      "site": "007f8098",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f8100",
      "incomplete_value": false,
      "site": "007f8108",
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
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f80a8",
      "incomplete_value": false,
      "site": "007f80b0",
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f81dc",
      "value": [
        "leaf",
        "ram:8035b8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f8184",
      "value": [
        "leaf",
        "ram:803560:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f80d4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007f80f8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f8100",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f80d4",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f80f8",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f8100",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f80b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8050.md#insn-007f80b0) · [`007f80f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8050.md#insn-007f80f0) · [`007f8184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8050.md#insn-007f8184)
- 新版 `007f8108`（命令位置の公開資料なし） · `007f8148`（命令位置の公開資料なし） · `007f81dc`（命令位置の公開資料なし）

~~~diff
- 007f80b0 ["INT_ADD", "register:40f0:8", ["const:7f80b0:8", "const:4:8"]]
- 007f80b0 ["CALL", null, ["callee:00c586e0:8"]]
+ 007f8108 ["INT_ADD", "register:40f0:8", ["const:7f8108:8", "const:4:8"]]
+ 007f8108 ["CALL", null, ["callee:00c586e0:8"]]
- 007f80b0 bytes 58811194
+ 007f8108 bytes 76811194
- 007f80f0 ["INT_ADD", "register:40f0:8", ["const:7f80f0:8", "const:4:8"]]
- 007f80f0 ["CALL", null, ["callee:00802d00:8"]]
+ 007f8148 ["INT_ADD", "register:40f0:8", ["const:7f8148:8", "const:4:8"]]
+ 007f8148 ["CALL", null, ["callee:00802d00:8"]]
- 007f80f0 bytes ee2a0094
+ 007f8148 bytes ee2a0094
- 007f8184 ["INT_ADD", "register:40f0:8", ["const:7f8184:8", "const:4:8"]]
- 007f8184 ["CALL", null, ["ram:803560:8"]]
+ 007f81dc ["INT_ADD", "register:40f0:8", ["const:7f81dc:8", "const:4:8"]]
+ 007f81dc ["CALL", null, ["ram:8035b8:8"]]
- 007f8184 bytes f72c0094
+ 007f81dc bytes f72c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bf769e5aa9358f9568594a7b4e70f2d"></a>

### [`007f8388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8388.md) → [`007f83e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f83e0.md) FUN_007f83e0

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
      "definition_site": "007f8404",
      "incomplete_value": false,
      "site": "007f8404",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f83ac",
      "incomplete_value": false,
      "site": "007f83ac",
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
            "const:390:8"
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
      "007f8404",
      "DATA",
      [
        "storage",
        "00c7c390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8404",
      "DATA",
      [
        "storage",
        "00c7c460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f839c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8388.md#insn-007f839c) · [`007f83a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8388.md#insn-007f83a8)
- 新版 `007f83f4`（命令位置の公開資料なし） · `007f8400`（命令位置の公開資料なし）

~~~diff
- 007f839c ["INT_ADD", "register:40f0:8", ["const:7f839c:8", "const:4:8"]]
- 007f839c ["CALL", null, ["callee:00c57f60:8"]]
+ 007f83f4 ["INT_ADD", "register:40f0:8", ["const:7f83f4:8", "const:4:8"]]
+ 007f83f4 ["CALL", null, ["callee:00c57f60:8"]]
- 007f839c bytes bd7e1194
+ 007f83f4 bytes db7e1194
- 007f83a8 ["COPY", "tmp:0:8", ["const:390:8"]]
- 007f83a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f83a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f83a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8400 ["COPY", "tmp:0:8", ["const:460:8"]]
+ 007f8400 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8400 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8400 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f83a8 bytes 08410e91
+ 007f8400 bytes 08811191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-461507a1a3843bb56596514a42a05096"></a>

### [`007f83bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f83bc.md) → [`007f8414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8414.md) FUN_007f8414

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
      "definition_site": "007f8420",
      "incomplete_value": false,
      "site": "007f8420",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f83c8",
      "incomplete_value": false,
      "site": "007f83c8",
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
            "const:390:8"
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
      "007f8420",
      "DATA",
      [
        "storage",
        "00c7c390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8420",
      "DATA",
      [
        "storage",
        "00c7c460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f83c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f83bc.md#insn-007f83c4)
- 新版 `007f841c`（命令位置の公開資料なし）

~~~diff
- 007f83c4 ["COPY", "tmp:0:8", ["const:390:8"]]
- 007f83c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f83c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f83c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f841c ["COPY", "tmp:0:8", ["const:460:8"]]
+ 007f841c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f841c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f841c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f83c4 bytes 29410e91
+ 007f841c bytes 29811191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdfb229350c3278527f343375a5d911e"></a>

### [`007f83d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f83d8.md) → [`007f8430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8430.md) FUN_007f8430

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0085b2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2e0.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`009dce40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dce40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0085b338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b338.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`009dce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dce94.md)

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
      "site": "007f847c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f8424",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f847c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f847c",
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

- 旧版 [`007f8424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f83d8.md#insn-007f8424) · [`007f83f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f83d8.md#insn-007f83f4) · [`007f8414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f83d8.md#insn-007f8414)
- 新版 `007f847c`（命令位置の公開資料なし） · `007f844c`（命令位置の公開資料なし） · `007f846c`（命令位置の公開資料なし）

~~~diff
- 007f8424 ["INT_ADD", "register:40f0:8", ["const:7f8424:8", "const:4:8"]]
- 007f8424 ["CALL", null, ["ram:47acf4:8"]]
+ 007f847c ["INT_ADD", "register:40f0:8", ["const:7f847c:8", "const:4:8"]]
+ 007f847c ["CALL", null, ["ram:47ad34:8"]]
- 007f8424 bytes 340af297
+ 007f847c bytes 2e0af297
- 007f83f4 ["INT_ADD", "register:40f0:8", ["const:7f83f4:8", "const:4:8"]]
- 007f83f4 ["CALL", null, ["callee:0085b338:8"]]
+ 007f844c ["INT_ADD", "register:40f0:8", ["const:7f844c:8", "const:4:8"]]
+ 007f844c ["CALL", null, ["callee:0085b338:8"]]
- 007f83f4 bytes bb8b0194
+ 007f844c bytes bb8b0194
- 007f8414 ["INT_ADD", "register:40f0:8", ["const:7f8414:8", "const:4:8"]]
- 007f8414 ["CALL", null, ["callee:009dce94:8"]]
+ 007f846c ["INT_ADD", "register:40f0:8", ["const:7f846c:8", "const:4:8"]]
+ 007f846c ["CALL", null, ["callee:009dce94:8"]]
- 007f8414 bytes 8b920794
+ 007f846c bytes 8a920794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1077ebe787d0f3120d5154a40c1ca8da"></a>

### [`007f847c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f847c.md) → [`007f84d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f84d4.md) FUN_007f84d4

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
      "definition_site": "007f84f8",
      "incomplete_value": false,
      "site": "007f84f8",
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
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f84a0",
      "incomplete_value": false,
      "site": "007f84a0",
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
            "const:410:8"
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
      "007f84f8",
      "DATA",
      [
        "storage",
        "00c7c410",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f84f8",
      "DATA",
      [
        "storage",
        "00c7c4e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f847c.md#insn-007f8490) · [`007f849c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f847c.md#insn-007f849c)
- 新版 `007f84e8`（命令位置の公開資料なし） · `007f84f4`（命令位置の公開資料なし）

~~~diff
- 007f8490 ["INT_ADD", "register:40f0:8", ["const:7f8490:8", "const:4:8"]]
- 007f8490 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f84e8 ["INT_ADD", "register:40f0:8", ["const:7f84e8:8", "const:4:8"]]
+ 007f84e8 ["CALL", null, ["callee:00c57f60:8"]]
- 007f8490 bytes 807e1194
+ 007f84e8 bytes 9e7e1194
- 007f849c ["COPY", "tmp:0:8", ["const:410:8"]]
- 007f849c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f849c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f849c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f84f4 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 007f84f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f84f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f84f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f849c bytes 08411091
+ 007f84f4 bytes 08811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24bfbe0b36b1588a98658a3ea4a8eb5d"></a>

### [`007f84b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f84b0.md) → [`007f8508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8508.md) FUN_007f8508

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
      "definition_site": "007f8514",
      "incomplete_value": false,
      "site": "007f8514",
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
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f84bc",
      "incomplete_value": false,
      "site": "007f84bc",
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
            "const:410:8"
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
      "007f8514",
      "DATA",
      [
        "storage",
        "00c7c410",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8514",
      "DATA",
      [
        "storage",
        "00c7c4e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f84b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f84b0.md#insn-007f84b8)
- 新版 `007f8510`（命令位置の公開資料なし）

~~~diff
- 007f84b8 ["COPY", "tmp:0:8", ["const:410:8"]]
- 007f84b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f84b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f84b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f8510 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 007f8510 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f8510 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f8510 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f84b8 bytes 29411091
+ 007f8510 bytes 29811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa314514e95f08920487d80ec06b2505"></a>

### [`007f84cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f84cc.md) → [`007f8524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8524.md) FUN_007f8524

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0046b880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b880.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0046b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b8c0.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d9b4.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.60% / 新版 95.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f8570",
      "incomplete_value": true,
      "site": "007f8570",
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
      "definition_site": "007f8518",
      "incomplete_value": true,
      "site": "007f8518",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f8578",
      "incomplete_value": false,
      "site": "007f8588",
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
    "old": {
      "definition_site": "007f8520",
      "incomplete_value": false,
      "site": "007f8530",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f8580",
      "incomplete_value": false,
      "site": "007f8588",
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
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8528",
      "incomplete_value": false,
      "site": "007f8530",
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
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f8554",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007f8578",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f8580",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f8554",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f8578",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f8580",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f84cc.md#insn-007f8530) · [`007f84fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f84cc.md#insn-007f84fc) · [`007f8520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f84cc.md#insn-007f8520)
- 新版 `007f8588`（命令位置の公開資料なし） · `007f8554`（命令位置の公開資料なし） · `007f8578`（命令位置の公開資料なし）

~~~diff
- 007f8530 ["INT_ADD", "register:40f0:8", ["const:7f8530:8", "const:4:8"]]
- 007f8530 ["CALL", null, ["callee:00c586e0:8"]]
+ 007f8588 ["INT_ADD", "register:40f0:8", ["const:7f8588:8", "const:4:8"]]
+ 007f8588 ["CALL", null, ["callee:00c586e0:8"]]
- 007f8530 bytes 38801194
+ 007f8588 bytes 56801194
- 007f84fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
- 007f84fc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f8554 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007f8554 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007f84fc bytes 00bd44f9
+ 007f8554 bytes 003d45f9
- 007f8520 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 007f8520 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f8520 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f8520 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f8578 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 007f8578 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f8578 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f8578 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f8520 bytes 21603991
+ 007f8578 bytes 21a03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7948c4cd0e669c123edc10d154e62f9b"></a>

### [`007f8664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8664.md) → [`007f86bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f86bc.md) FUN_007f86bc

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
      "definition_site": "007f86e0",
      "incomplete_value": false,
      "site": "007f86e0",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8688",
      "incomplete_value": false,
      "site": "007f8688",
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
            "const:4a0:8"
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
      "007f86e0",
      "DATA",
      [
        "storage",
        "00c7c4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f86e0",
      "DATA",
      [
        "storage",
        "00c7c570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8664.md#insn-007f8678) · [`007f8684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8664.md#insn-007f8684)
- 新版 `007f86d0`（命令位置の公開資料なし） · `007f86dc`（命令位置の公開資料なし）

~~~diff
- 007f8678 ["INT_ADD", "register:40f0:8", ["const:7f8678:8", "const:4:8"]]
- 007f8678 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f86d0 ["INT_ADD", "register:40f0:8", ["const:7f86d0:8", "const:4:8"]]
+ 007f86d0 ["CALL", null, ["callee:00c57f60:8"]]
- 007f8678 bytes 067e1194
+ 007f86d0 bytes 247e1194
- 007f8684 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 007f8684 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8684 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8684 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f86dc ["COPY", "tmp:0:8", ["const:570:8"]]
+ 007f86dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f86dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f86dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8684 bytes 08811291
+ 007f86dc bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0f98741ed672b2e768fbc006a32c272"></a>

### [`007f8698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8698.md) → [`007f86f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f86f0.md) FUN_007f86f0

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
      "definition_site": "007f86fc",
      "incomplete_value": false,
      "site": "007f86fc",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f86a4",
      "incomplete_value": false,
      "site": "007f86a4",
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
            "const:4a0:8"
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
      "007f86fc",
      "DATA",
      [
        "storage",
        "00c7c4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f86fc",
      "DATA",
      [
        "storage",
        "00c7c570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f86a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8698.md#insn-007f86a0)
- 新版 `007f86f8`（命令位置の公開資料なし）

~~~diff
- 007f86a0 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 007f86a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f86a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f86a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f86f8 ["COPY", "tmp:0:8", ["const:570:8"]]
+ 007f86f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f86f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f86f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f86a0 bytes 29811291
+ 007f86f8 bytes 29c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4991eb4a0b2e69d34c0fe80db64a1903"></a>

### [`007f86b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f86b4.md) → [`007f870c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f870c.md) FUN_007f870c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0046a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md) [`0046b880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b880.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0046a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a290.md) [`0046b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b8c0.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d9b4.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.99% / 新版 97.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f8764",
      "incomplete_value": true,
      "site": "007f8764",
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
      "definition_site": "007f870c",
      "incomplete_value": true,
      "site": "007f870c",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f876c",
      "incomplete_value": false,
      "site": "007f877c",
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
    "old": {
      "definition_site": "007f8714",
      "incomplete_value": false,
      "site": "007f8724",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f8774",
      "incomplete_value": false,
      "site": "007f877c",
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
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f871c",
      "incomplete_value": false,
      "site": "007f8724",
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
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f8748",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007f876c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f8774",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f8748",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f876c",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f8774",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f86b4.md#insn-007f8724) · [`007f86f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f86b4.md#insn-007f86f0) · [`007f8714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f86b4.md#insn-007f8714)
- 新版 `007f877c`（命令位置の公開資料なし） · `007f8748`（命令位置の公開資料なし） · `007f876c`（命令位置の公開資料なし）

~~~diff
- 007f8724 ["INT_ADD", "register:40f0:8", ["const:7f8724:8", "const:4:8"]]
- 007f8724 ["CALL", null, ["callee:00c586e0:8"]]
+ 007f877c ["INT_ADD", "register:40f0:8", ["const:7f877c:8", "const:4:8"]]
+ 007f877c ["CALL", null, ["callee:00c586e0:8"]]
- 007f8724 bytes bb7f1194
+ 007f877c bytes d97f1194
- 007f86f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
- 007f86f0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f8748 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007f8748 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007f86f0 bytes 00bd44f9
+ 007f8748 bytes 003d45f9
- 007f8714 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 007f8714 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f8714 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f8714 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f876c ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 007f876c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f876c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f876c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f8714 bytes 21603991
+ 007f876c bytes 21a03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb05db7cfb2053912041759a43653172"></a>

### [`007f89fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f89fc.md) → [`007f8a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8a54.md) FUN_007f8a54

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
      "definition_site": "007f8a78",
      "incomplete_value": false,
      "site": "007f8a78",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8a20",
      "incomplete_value": false,
      "site": "007f8a20",
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
            "const:530:8"
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
      "007f8a78",
      "DATA",
      [
        "storage",
        "00c7c530",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8a78",
      "DATA",
      [
        "storage",
        "00c7c600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f89fc.md#insn-007f8a10) · [`007f8a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f89fc.md#insn-007f8a1c)
- 新版 `007f8a68`（命令位置の公開資料なし） · `007f8a74`（命令位置の公開資料なし）

~~~diff
- 007f8a10 ["INT_ADD", "register:40f0:8", ["const:7f8a10:8", "const:4:8"]]
- 007f8a10 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f8a68 ["INT_ADD", "register:40f0:8", ["const:7f8a68:8", "const:4:8"]]
+ 007f8a68 ["CALL", null, ["callee:00c57f60:8"]]
- 007f8a10 bytes 207d1194
+ 007f8a68 bytes 3e7d1194
- 007f8a1c ["COPY", "tmp:0:8", ["const:530:8"]]
- 007f8a1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8a1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8a1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8a74 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 007f8a74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8a74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8a74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8a1c bytes 08c11491
+ 007f8a74 bytes 08011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53dc595c56de807aa45dbbbe4be185bb"></a>

### [`007f8a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8a30.md) → [`007f8a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8a88.md) FUN_007f8a88

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
      "definition_site": "007f8a94",
      "incomplete_value": false,
      "site": "007f8a94",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8a3c",
      "incomplete_value": false,
      "site": "007f8a3c",
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
      "007f8a94",
      "DATA",
      [
        "storage",
        "00c7c530",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8a94",
      "DATA",
      [
        "storage",
        "00c7c600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8a30.md#insn-007f8a38)
- 新版 `007f8a90`（命令位置の公開資料なし）

~~~diff
- 007f8a38 ["COPY", "tmp:0:8", ["const:530:8"]]
- 007f8a38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f8a38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f8a38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f8a90 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 007f8a90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f8a90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f8a90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f8a38 bytes 29c11491
+ 007f8a90 bytes 29011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b3dad762c505100b2f6ee2b27a6802b"></a>

### [`007f8a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8a4c.md) → [`007f8aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8aa4.md) FUN_007f8aa4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046b880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b880.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b8c0.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b92e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92e8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.58% / 新版 93.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f8b68",
      "incomplete_value": true,
      "site": "007f8b78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e47:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8b10",
      "incomplete_value": true,
      "site": "007f8b20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ea3:8"
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
      "definition_site": "007f8b7c",
      "incomplete_value": true,
      "site": "007f8b7c",
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
      "definition_site": "007f8b24",
      "incomplete_value": true,
      "site": "007f8b24",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f8ae4",
      "incomplete_value": true,
      "site": "007f8ae4",
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
      "definition_site": "007f8a8c",
      "incomplete_value": true,
      "site": "007f8a8c",
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
      "007f8ad4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007f8aec",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f8af4",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f8ad4",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f8aec",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f8af4",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8a4c.md#insn-007f8aa4) · [`007f8afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8a4c.md#insn-007f8afc) · [`007f8a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8a4c.md#insn-007f8a7c)
- 新版 `007f8afc`（命令位置の公開資料なし） · `007f8b54`（命令位置の公開資料なし） · `007f8ad4`（命令位置の公開資料なし）

~~~diff
- 007f8aa4 ["INT_ADD", "register:40f0:8", ["const:7f8aa4:8", "const:4:8"]]
- 007f8aa4 ["CALL", null, ["callee:00c586e0:8"]]
+ 007f8afc ["INT_ADD", "register:40f0:8", ["const:7f8afc:8", "const:4:8"]]
+ 007f8afc ["CALL", null, ["callee:00c586e0:8"]]
- 007f8aa4 bytes db7e1194
+ 007f8afc bytes f97e1194
- 007f8afc ["INT_ADD", "register:40f0:8", ["const:7f8afc:8", "const:4:8"]]
- 007f8afc ["CALL", null, ["callee:00468fc8:8"]]
+ 007f8b54 ["INT_ADD", "register:40f0:8", ["const:7f8b54:8", "const:4:8"]]
+ 007f8b54 ["CALL", null, ["callee:00468fc8:8"]]
- 007f8afc bytes 23c1f197
+ 007f8b54 bytes 1dc1f197
- 007f8a7c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:978:8"]]
- 007f8a7c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f8ad4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 007f8ad4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007f8a7c bytes 20bd44f9
+ 007f8ad4 bytes 203d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d84d6a6ef359549945bcb45d82f4cda1"></a>

### [`007f8c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8c58.md) → [`007f8cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8cb0.md) FUN_007f8cb0

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
      "definition_site": "007f8cc4",
      "incomplete_value": false,
      "site": "007f8cc8",
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
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8c6c",
      "incomplete_value": false,
      "site": "007f8c70",
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
      "007f8cc8",
      "DATA",
      [
        "storage",
        "00c7c5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8cc8",
      "DATA",
      [
        "storage",
        "00c7c680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8c58.md#insn-007f8c64) · [`007f8c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8c58.md#insn-007f8c6c)
- 新版 `007f8cbc`（命令位置の公開資料なし） · `007f8cc4`（命令位置の公開資料なし）

~~~diff
- 007f8c64 ["INT_ADD", "register:40f0:8", ["const:7f8c64:8", "const:4:8"]]
- 007f8c64 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f8cbc ["INT_ADD", "register:40f0:8", ["const:7f8cbc:8", "const:4:8"]]
+ 007f8cbc ["CALL", null, ["callee:00c57f60:8"]]
- 007f8c64 bytes 8b7c1194
+ 007f8cbc bytes a97c1194
- 007f8c6c ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 007f8c6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8c6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8c6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8cc4 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 007f8cc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8cc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8cc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8c6c bytes 08c11691
+ 007f8cc4 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3747c4557837d626f83288c46d144e4a"></a>

### [`007f8c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8c7c.md) → [`007f8cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8cd4.md) FUN_007f8cd4

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
      "definition_site": "007f8cd8",
      "incomplete_value": false,
      "site": "007f8cdc",
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
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8c80",
      "incomplete_value": false,
      "site": "007f8c84",
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
      "007f8cdc",
      "DATA",
      [
        "storage",
        "00c7c5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8cdc",
      "DATA",
      [
        "storage",
        "00c7c680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8c7c.md#insn-007f8c80)
- 新版 `007f8cd8`（命令位置の公開資料なし）

~~~diff
- 007f8c80 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 007f8c80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8c80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8c80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8cd8 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 007f8cd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8cd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8cd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8c80 bytes 08c11691
+ 007f8cd8 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0571f1fd86b4761d5c51f23ceef3872"></a>

### [`007f8c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8c94.md) → [`007f8cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8cec.md) FUN_007f8cec

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
      "site": "007f8d10",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f8cb8",
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
      "007f8d10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f8d10",
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

- 旧版 [`007f8cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8c94.md#insn-007f8cb8) · [`007f8cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8c94.md#insn-007f8cc4)
- 新版 `007f8d10`（命令位置の公開資料なし） · `007f8d1c`（命令位置の公開資料なし）

~~~diff
- 007f8cb8 ["INT_ADD", "register:40f0:8", ["const:7f8cb8:8", "const:4:8"]]
- 007f8cb8 ["CALL", null, ["ram:47acf4:8"]]
+ 007f8d10 ["INT_ADD", "register:40f0:8", ["const:7f8d10:8", "const:4:8"]]
+ 007f8d10 ["CALL", null, ["ram:47ad34:8"]]
- 007f8cb8 bytes 0f08f297
+ 007f8d10 bytes 0908f297
- 007f8cc4 ["INT_ADD", "register:40f0:8", ["const:7f8cc4:8", "const:4:8"]]
- 007f8cc4 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f8d1c ["INT_ADD", "register:40f0:8", ["const:7f8d1c:8", "const:4:8"]]
+ 007f8d1c ["CALL", null, ["callee:0047ce14:8"]]
- 007f8cc4 bytes 4410f297
+ 007f8d1c bytes 3e10f297
~~~


<a id="compare-b22ee2735ab0da84217657fa3202392e"></a>

### [`007f8d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8d08.md) → [`007f8d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8d60.md) FUN_007f8d60

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
      "definition_site": "007f8d74",
      "incomplete_value": false,
      "site": "007f8d78",
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
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8d1c",
      "incomplete_value": false,
      "site": "007f8d20",
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
            "const:630:8"
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
      "007f8d78",
      "DATA",
      [
        "storage",
        "00c7c630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8d78",
      "DATA",
      [
        "storage",
        "00c7c700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8d08.md#insn-007f8d14) · [`007f8d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8d08.md#insn-007f8d1c)
- 新版 `007f8d6c`（命令位置の公開資料なし） · `007f8d74`（命令位置の公開資料なし）

~~~diff
- 007f8d14 ["INT_ADD", "register:40f0:8", ["const:7f8d14:8", "const:4:8"]]
- 007f8d14 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f8d6c ["INT_ADD", "register:40f0:8", ["const:7f8d6c:8", "const:4:8"]]
+ 007f8d6c ["CALL", null, ["callee:00c57f60:8"]]
- 007f8d14 bytes 5f7c1194
+ 007f8d6c bytes 7d7c1194
- 007f8d1c ["COPY", "tmp:0:8", ["const:630:8"]]
- 007f8d1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8d1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8d1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8d74 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 007f8d74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8d74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8d74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8d1c bytes 08c11891
+ 007f8d74 bytes 08011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be135b673fcd547b4558f7da7e2d15ea"></a>

### [`007f8d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8d2c.md) → [`007f8d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8d84.md) FUN_007f8d84

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
      "definition_site": "007f8d88",
      "incomplete_value": false,
      "site": "007f8d8c",
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
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8d30",
      "incomplete_value": false,
      "site": "007f8d34",
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
      "007f8d8c",
      "DATA",
      [
        "storage",
        "00c7c630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8d8c",
      "DATA",
      [
        "storage",
        "00c7c700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8d2c.md#insn-007f8d30)
- 新版 `007f8d88`（命令位置の公開資料なし）

~~~diff
- 007f8d30 ["COPY", "tmp:0:8", ["const:630:8"]]
- 007f8d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8d88 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 007f8d88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8d88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8d88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8d30 bytes 08c11891
+ 007f8d88 bytes 08011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e1f6109b63adf50778fb651fe7fe98f"></a>

### [`007f8d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8d44.md) → [`007f8d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8d9c.md) FUN_007f8d9c

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
      "site": "007f8dc0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f8d68",
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
      "007f8dc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f8dc0",
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

- 旧版 [`007f8d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8d44.md#insn-007f8d68) · [`007f8d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8d44.md#insn-007f8d74)
- 新版 `007f8dc0`（命令位置の公開資料なし） · `007f8dcc`（命令位置の公開資料なし）

~~~diff
- 007f8d68 ["INT_ADD", "register:40f0:8", ["const:7f8d68:8", "const:4:8"]]
- 007f8d68 ["CALL", null, ["ram:47acf4:8"]]
+ 007f8dc0 ["INT_ADD", "register:40f0:8", ["const:7f8dc0:8", "const:4:8"]]
+ 007f8dc0 ["CALL", null, ["ram:47ad34:8"]]
- 007f8d68 bytes e307f297
+ 007f8dc0 bytes dd07f297
- 007f8d74 ["INT_ADD", "register:40f0:8", ["const:7f8d74:8", "const:4:8"]]
- 007f8d74 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f8dcc ["INT_ADD", "register:40f0:8", ["const:7f8dcc:8", "const:4:8"]]
+ 007f8dcc ["CALL", null, ["callee:0047ce14:8"]]
- 007f8d74 bytes 1810f297
+ 007f8dcc bytes 1210f297
~~~


<a id="compare-ea2e806c7a6c9eadcb7195247d584b6b"></a>

### [`007f8db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8db8.md) → [`007f8e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8e10.md) FUN_007f8e10

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
      "definition_site": "007f8e24",
      "incomplete_value": false,
      "site": "007f8e28",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8dcc",
      "incomplete_value": false,
      "site": "007f8dd0",
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
            "const:6b0:8"
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
      "007f8e28",
      "DATA",
      [
        "storage",
        "00c7c6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8e28",
      "DATA",
      [
        "storage",
        "00c7c780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8db8.md#insn-007f8dc4) · [`007f8dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8db8.md#insn-007f8dcc)
- 新版 `007f8e1c`（命令位置の公開資料なし） · `007f8e24`（命令位置の公開資料なし）

~~~diff
- 007f8dc4 ["INT_ADD", "register:40f0:8", ["const:7f8dc4:8", "const:4:8"]]
- 007f8dc4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f8e1c ["INT_ADD", "register:40f0:8", ["const:7f8e1c:8", "const:4:8"]]
+ 007f8e1c ["CALL", null, ["callee:00c57f60:8"]]
- 007f8dc4 bytes 337c1194
+ 007f8e1c bytes 517c1194
- 007f8dcc ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 007f8dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8e24 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 007f8e24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8e24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8e24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8dcc bytes 08c11a91
+ 007f8e24 bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59687bd5f88b3bb1dfceefe78946d601"></a>

### [`007f8ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8ddc.md) → [`007f8e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8e34.md) FUN_007f8e34

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
      "definition_site": "007f8e38",
      "incomplete_value": false,
      "site": "007f8e3c",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8de0",
      "incomplete_value": false,
      "site": "007f8de4",
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
      "007f8e3c",
      "DATA",
      [
        "storage",
        "00c7c6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8e3c",
      "DATA",
      [
        "storage",
        "00c7c780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8ddc.md#insn-007f8de0)
- 新版 `007f8e38`（命令位置の公開資料なし）

~~~diff
- 007f8de0 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 007f8de0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8de0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8de0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8e38 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 007f8e38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8e38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8e38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8de0 bytes 08c11a91
+ 007f8e38 bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fa72a9630e92a71425501e249b03f99"></a>

### [`007f8df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8df4.md) → [`007f8e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8e4c.md) FUN_007f8e4c

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
      "site": "007f8e70",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f8e18",
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
      "007f8e70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f8e70",
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

- 旧版 [`007f8e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8df4.md#insn-007f8e18) · [`007f8e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8df4.md#insn-007f8e24)
- 新版 `007f8e70`（命令位置の公開資料なし） · `007f8e7c`（命令位置の公開資料なし）

~~~diff
- 007f8e18 ["INT_ADD", "register:40f0:8", ["const:7f8e18:8", "const:4:8"]]
- 007f8e18 ["CALL", null, ["ram:47acf4:8"]]
+ 007f8e70 ["INT_ADD", "register:40f0:8", ["const:7f8e70:8", "const:4:8"]]
+ 007f8e70 ["CALL", null, ["ram:47ad34:8"]]
- 007f8e18 bytes b707f297
+ 007f8e70 bytes b107f297
- 007f8e24 ["INT_ADD", "register:40f0:8", ["const:7f8e24:8", "const:4:8"]]
- 007f8e24 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f8e7c ["INT_ADD", "register:40f0:8", ["const:7f8e7c:8", "const:4:8"]]
+ 007f8e7c ["CALL", null, ["callee:0047ce14:8"]]
- 007f8e24 bytes ec0ff297
+ 007f8e7c bytes e60ff297
~~~


<a id="compare-6ca28056d46ad54fdd121fa6512a0888"></a>

### [`007f8e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8e68.md) → [`007f8ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8ec0.md) FUN_007f8ec0

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
      "definition_site": "007f8ed4",
      "incomplete_value": false,
      "site": "007f8ed8",
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
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8e7c",
      "incomplete_value": false,
      "site": "007f8e80",
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
            "const:730:8"
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
      "007f8ed8",
      "DATA",
      [
        "storage",
        "00c7c730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8ed8",
      "DATA",
      [
        "storage",
        "00c7c800",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8e68.md#insn-007f8e74) · [`007f8e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8e68.md#insn-007f8e7c)
- 新版 `007f8ecc`（命令位置の公開資料なし） · `007f8ed4`（命令位置の公開資料なし）

~~~diff
- 007f8e74 ["INT_ADD", "register:40f0:8", ["const:7f8e74:8", "const:4:8"]]
- 007f8e74 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f8ecc ["INT_ADD", "register:40f0:8", ["const:7f8ecc:8", "const:4:8"]]
+ 007f8ecc ["CALL", null, ["callee:00c57f60:8"]]
- 007f8e74 bytes 077c1194
+ 007f8ecc bytes 257c1194
- 007f8e7c ["COPY", "tmp:0:8", ["const:730:8"]]
- 007f8e7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8e7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8e7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8ed4 ["COPY", "tmp:0:8", ["const:800:8"]]
+ 007f8ed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8ed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8ed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8e7c bytes 08c11c91
+ 007f8ed4 bytes 08012091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a7a982e0ca08643bf4d53df2205b32c"></a>

### [`007f8e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8e8c.md) → [`007f8ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8ee4.md) FUN_007f8ee4

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
      "definition_site": "007f8ee8",
      "incomplete_value": false,
      "site": "007f8eec",
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
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8e90",
      "incomplete_value": false,
      "site": "007f8e94",
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
      "007f8eec",
      "DATA",
      [
        "storage",
        "00c7c730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8eec",
      "DATA",
      [
        "storage",
        "00c7c800",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8e8c.md#insn-007f8e90)
- 新版 `007f8ee8`（命令位置の公開資料なし）

~~~diff
- 007f8e90 ["COPY", "tmp:0:8", ["const:730:8"]]
- 007f8e90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8e90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8e90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8ee8 ["COPY", "tmp:0:8", ["const:800:8"]]
+ 007f8ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8e90 bytes 08c11c91
+ 007f8ee8 bytes 08012091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca6c4685fc254626d8303a6eb35d4050"></a>

### [`007f8ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8ea4.md) → [`007f8efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8efc.md) FUN_007f8efc

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
      "site": "007f8f20",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f8ec8",
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
      "007f8f20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f8f20",
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

- 旧版 [`007f8ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8ea4.md#insn-007f8ec8) · [`007f8ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8ea4.md#insn-007f8ed4)
- 新版 `007f8f20`（命令位置の公開資料なし） · `007f8f2c`（命令位置の公開資料なし）

~~~diff
- 007f8ec8 ["INT_ADD", "register:40f0:8", ["const:7f8ec8:8", "const:4:8"]]
- 007f8ec8 ["CALL", null, ["ram:47acf4:8"]]
+ 007f8f20 ["INT_ADD", "register:40f0:8", ["const:7f8f20:8", "const:4:8"]]
+ 007f8f20 ["CALL", null, ["ram:47ad34:8"]]
- 007f8ec8 bytes 8b07f297
+ 007f8f20 bytes 8507f297
- 007f8ed4 ["INT_ADD", "register:40f0:8", ["const:7f8ed4:8", "const:4:8"]]
- 007f8ed4 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f8f2c ["INT_ADD", "register:40f0:8", ["const:7f8f2c:8", "const:4:8"]]
+ 007f8f2c ["CALL", null, ["callee:0047ce14:8"]]
- 007f8ed4 bytes c00ff297
+ 007f8f2c bytes ba0ff297
~~~


<a id="compare-663e530fa260d95b0fc0ceefbe579e05"></a>

### [`007f8f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8f18.md) → [`007f8f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8f70.md) FUN_007f8f70

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
      "definition_site": "007f8f84",
      "incomplete_value": false,
      "site": "007f8f88",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8f2c",
      "incomplete_value": false,
      "site": "007f8f30",
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
            "const:7b0:8"
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
      "007f8f88",
      "DATA",
      [
        "storage",
        "00c7c7b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8f88",
      "DATA",
      [
        "storage",
        "00c7c880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8f18.md#insn-007f8f24) · [`007f8f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8f18.md#insn-007f8f2c)
- 新版 `007f8f7c`（命令位置の公開資料なし） · `007f8f84`（命令位置の公開資料なし）

~~~diff
- 007f8f24 ["INT_ADD", "register:40f0:8", ["const:7f8f24:8", "const:4:8"]]
- 007f8f24 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f8f7c ["INT_ADD", "register:40f0:8", ["const:7f8f7c:8", "const:4:8"]]
+ 007f8f7c ["CALL", null, ["callee:00c57f60:8"]]
- 007f8f24 bytes db7b1194
+ 007f8f7c bytes f97b1194
- 007f8f2c ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 007f8f2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8f2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8f2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8f84 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 007f8f84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8f84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8f84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8f2c bytes 08c11e91
+ 007f8f84 bytes 08012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6af4559303e13f6fd254432acb6f6339"></a>

### [`007f8f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8f3c.md) → [`007f8f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8f94.md) FUN_007f8f94

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
      "definition_site": "007f8f98",
      "incomplete_value": false,
      "site": "007f8f9c",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8f40",
      "incomplete_value": false,
      "site": "007f8f44",
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
      "007f8f9c",
      "DATA",
      [
        "storage",
        "00c7c7b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f8f9c",
      "DATA",
      [
        "storage",
        "00c7c880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8f3c.md#insn-007f8f40)
- 新版 `007f8f98`（命令位置の公開資料なし）

~~~diff
- 007f8f40 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 007f8f40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8f40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8f40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8f98 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 007f8f98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8f98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8f98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8f40 bytes 08c11e91
+ 007f8f98 bytes 08012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f38beae6f3bc5d27a0dab2cf64d2c08"></a>

### [`007f8f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8f54.md) → [`007f8fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8fac.md) FUN_007f8fac

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
      "site": "007f8fd0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f8f78",
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
      "007f8fd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f8fd0",
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

- 旧版 [`007f8f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8f54.md#insn-007f8f78) · [`007f8f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8f54.md#insn-007f8f84)
- 新版 `007f8fd0`（命令位置の公開資料なし） · `007f8fdc`（命令位置の公開資料なし）

~~~diff
- 007f8f78 ["INT_ADD", "register:40f0:8", ["const:7f8f78:8", "const:4:8"]]
- 007f8f78 ["CALL", null, ["ram:47acf4:8"]]
+ 007f8fd0 ["INT_ADD", "register:40f0:8", ["const:7f8fd0:8", "const:4:8"]]
+ 007f8fd0 ["CALL", null, ["ram:47ad34:8"]]
- 007f8f78 bytes 5f07f297
+ 007f8fd0 bytes 5907f297
- 007f8f84 ["INT_ADD", "register:40f0:8", ["const:7f8f84:8", "const:4:8"]]
- 007f8f84 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f8fdc ["INT_ADD", "register:40f0:8", ["const:7f8fdc:8", "const:4:8"]]
+ 007f8fdc ["CALL", null, ["callee:0047ce14:8"]]
- 007f8f84 bytes 940ff297
+ 007f8fdc bytes 8e0ff297
~~~


<a id="compare-78182990a82112ce7f5e99b071660b93"></a>

### [`007f8fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8fc8.md) → [`007f9020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9020.md) FUN_007f9020

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
      "definition_site": "007f9040",
      "incomplete_value": false,
      "site": "007f9044",
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
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8fe8",
      "incomplete_value": false,
      "site": "007f8fec",
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
      "007f9044",
      "DATA",
      [
        "storage",
        "00c7c830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f9044",
      "DATA",
      [
        "storage",
        "00c7c900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8fc8.md#insn-007f8fdc) · [`007f8fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8fc8.md#insn-007f8fe8)
- 新版 `007f9034`（命令位置の公開資料なし） · `007f9040`（命令位置の公開資料なし）

~~~diff
- 007f8fdc ["INT_ADD", "register:40f0:8", ["const:7f8fdc:8", "const:4:8"]]
- 007f8fdc ["CALL", null, ["callee:00c57f60:8"]]
+ 007f9034 ["INT_ADD", "register:40f0:8", ["const:7f9034:8", "const:4:8"]]
+ 007f9034 ["CALL", null, ["callee:00c57f60:8"]]
- 007f8fdc bytes ad7b1194
+ 007f9034 bytes cb7b1194
- 007f8fe8 ["COPY", "tmp:0:8", ["const:830:8"]]
- 007f8fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f9040 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 007f9040 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9040 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9040 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8fe8 bytes 08c12091
+ 007f9040 bytes 08012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0fe88430c5eafff2338a01ba63394c5"></a>

### [`007f9000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9000.md) → [`007f9058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9058.md) FUN_007f9058

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
      "definition_site": "007f905c",
      "incomplete_value": false,
      "site": "007f9060",
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
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9004",
      "incomplete_value": false,
      "site": "007f9008",
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
      "007f9060",
      "DATA",
      [
        "storage",
        "00c7c830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f9060",
      "DATA",
      [
        "storage",
        "00c7c900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f9004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9000.md#insn-007f9004)
- 新版 `007f905c`（命令位置の公開資料なし）

~~~diff
- 007f9004 ["COPY", "tmp:0:8", ["const:830:8"]]
- 007f9004 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f9004 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f9004 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f905c ["COPY", "tmp:0:8", ["const:900:8"]]
+ 007f905c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f905c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f905c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f9004 bytes 08c12091
+ 007f905c bytes 08012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23e0cc44d06113dbf3405475df2fe9ce"></a>

### [`007f9020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9020.md) → [`007f9078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9078.md) FUN_007f9078

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
      "site": "007f909c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f9044",
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
      "007f909c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f909c",
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

- 旧版 [`007f9044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9020.md#insn-007f9044) · [`007f9050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9020.md#insn-007f9050)
- 新版 `007f909c`（命令位置の公開資料なし） · `007f90a8`（命令位置の公開資料なし）

~~~diff
- 007f9044 ["INT_ADD", "register:40f0:8", ["const:7f9044:8", "const:4:8"]]
- 007f9044 ["CALL", null, ["ram:47acf4:8"]]
+ 007f909c ["INT_ADD", "register:40f0:8", ["const:7f909c:8", "const:4:8"]]
+ 007f909c ["CALL", null, ["ram:47ad34:8"]]
- 007f9044 bytes 2c07f297
+ 007f909c bytes 2607f297
- 007f9050 ["INT_ADD", "register:40f0:8", ["const:7f9050:8", "const:4:8"]]
- 007f9050 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f90a8 ["INT_ADD", "register:40f0:8", ["const:7f90a8:8", "const:4:8"]]
+ 007f90a8 ["CALL", null, ["callee:0047ce14:8"]]
- 007f9050 bytes 610ff297
+ 007f90a8 bytes 5b0ff297
~~~


<a id="compare-16aaef57aa82042003089cea806ada6d"></a>

### [`007f9094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9094.md) → [`007f90ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f90ec.md) FUN_007f90ec

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
      "definition_site": "007f9100",
      "incomplete_value": false,
      "site": "007f9104",
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
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f90a8",
      "incomplete_value": false,
      "site": "007f90ac",
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
            "const:8b0:8"
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
      "007f9104",
      "DATA",
      [
        "storage",
        "00c7c8b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f9104",
      "DATA",
      [
        "storage",
        "00c7c980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f90a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9094.md#insn-007f90a0) · [`007f90a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9094.md#insn-007f90a8)
- 新版 `007f90f8`（命令位置の公開資料なし） · `007f9100`（命令位置の公開資料なし）

~~~diff
- 007f90a0 ["INT_ADD", "register:40f0:8", ["const:7f90a0:8", "const:4:8"]]
- 007f90a0 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f90f8 ["INT_ADD", "register:40f0:8", ["const:7f90f8:8", "const:4:8"]]
+ 007f90f8 ["CALL", null, ["callee:00c57f60:8"]]
- 007f90a0 bytes 7c7b1194
+ 007f90f8 bytes 9a7b1194
- 007f90a8 ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 007f90a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f90a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f90a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f9100 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 007f9100 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9100 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9100 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f90a8 bytes 08c12291
+ 007f9100 bytes 08012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bb85a87292a36e91fdfe7d8aa2e54d2"></a>

### [`007f90b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f90b8.md) → [`007f9110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9110.md) FUN_007f9110

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
      "definition_site": "007f9114",
      "incomplete_value": false,
      "site": "007f9118",
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
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f90bc",
      "incomplete_value": false,
      "site": "007f90c0",
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
      "007f9118",
      "DATA",
      [
        "storage",
        "00c7c8b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f9118",
      "DATA",
      [
        "storage",
        "00c7c980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f90bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f90b8.md#insn-007f90bc)
- 新版 `007f9114`（命令位置の公開資料なし）

~~~diff
- 007f90bc ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 007f90bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f90bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f90bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f9114 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 007f9114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f90bc bytes 08c12291
+ 007f9114 bytes 08012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30449c865fdde605c2d2ca9376b2d5e2"></a>

### [`007f90d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f90d0.md) → [`007f9128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9128.md) FUN_007f9128

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
      "site": "007f914c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f90f4",
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
      "007f914c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f914c",
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

- 旧版 [`007f90f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f90d0.md#insn-007f90f4) · [`007f9100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f90d0.md#insn-007f9100)
- 新版 `007f914c`（命令位置の公開資料なし） · `007f9158`（命令位置の公開資料なし）

~~~diff
- 007f90f4 ["INT_ADD", "register:40f0:8", ["const:7f90f4:8", "const:4:8"]]
- 007f90f4 ["CALL", null, ["ram:47acf4:8"]]
+ 007f914c ["INT_ADD", "register:40f0:8", ["const:7f914c:8", "const:4:8"]]
+ 007f914c ["CALL", null, ["ram:47ad34:8"]]
- 007f90f4 bytes 0007f297
+ 007f914c bytes fa06f297
- 007f9100 ["INT_ADD", "register:40f0:8", ["const:7f9100:8", "const:4:8"]]
- 007f9100 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f9158 ["INT_ADD", "register:40f0:8", ["const:7f9158:8", "const:4:8"]]
+ 007f9158 ["CALL", null, ["callee:0047ce14:8"]]
- 007f9100 bytes 350ff297
+ 007f9158 bytes 2f0ff297
~~~


<a id="compare-bb344e09a71cc3dd4359a9cf2597aee8"></a>

### [`007f9144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9144.md) → [`007f919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f919c.md) FUN_007f919c

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
      "definition_site": "007f91c0",
      "incomplete_value": false,
      "site": "007f91c0",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9168",
      "incomplete_value": false,
      "site": "007f9168",
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
            "const:930:8"
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
      "007f91c0",
      "DATA",
      [
        "storage",
        "00c7c930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f91c0",
      "DATA",
      [
        "storage",
        "00c7ca00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f9158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9144.md#insn-007f9158) · [`007f9164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9144.md#insn-007f9164)
- 新版 `007f91b0`（命令位置の公開資料なし） · `007f91bc`（命令位置の公開資料なし）

~~~diff
- 007f9158 ["INT_ADD", "register:40f0:8", ["const:7f9158:8", "const:4:8"]]
- 007f9158 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f91b0 ["INT_ADD", "register:40f0:8", ["const:7f91b0:8", "const:4:8"]]
+ 007f91b0 ["CALL", null, ["callee:00c57f60:8"]]
- 007f9158 bytes 4e7b1194
+ 007f91b0 bytes 6c7b1194
- 007f9164 ["COPY", "tmp:0:8", ["const:930:8"]]
- 007f9164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f9164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f9164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f91bc ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 007f91bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f91bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f91bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f9164 bytes 08c12491
+ 007f91bc bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-343060ea5125e4a80497ee0c7ad782d5"></a>

### [`007f9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9178.md) → [`007f91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f91d0.md) FUN_007f91d0

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
      "definition_site": "007f91dc",
      "incomplete_value": false,
      "site": "007f91dc",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9184",
      "incomplete_value": false,
      "site": "007f9184",
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
      "007f91dc",
      "DATA",
      [
        "storage",
        "00c7c930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f91dc",
      "DATA",
      [
        "storage",
        "00c7ca00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f9180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9178.md#insn-007f9180)
- 新版 `007f91d8`（命令位置の公開資料なし）

~~~diff
- 007f9180 ["COPY", "tmp:0:8", ["const:930:8"]]
- 007f9180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f9180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f9180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f91d8 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 007f91d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f91d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f91d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f9180 bytes 29c12491
+ 007f91d8 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0512d15d3131075624907c164bf21c43"></a>

### [`007f9194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9194.md) → [`007f91ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f91ec.md) FUN_007f91ec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`009e3a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3a80.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`009e3ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e3ad4.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

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
      "site": "007f922c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f91d4",
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
      "007f922c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f922c",
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

- 旧版 [`007f91d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9194.md#insn-007f91d4) · [`007f91c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9194.md#insn-007f91c8) · [`007f91d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9194.md#insn-007f91d0)
- 新版 `007f922c`（命令位置の公開資料なし） · `007f9220`（命令位置の公開資料なし） · `007f9228`（命令位置の公開資料なし）

~~~diff
- 007f91d4 ["INT_ADD", "register:40f0:8", ["const:7f91d4:8", "const:4:8"]]
- 007f91d4 ["CALL", null, ["ram:47acf4:8"]]
+ 007f922c ["INT_ADD", "register:40f0:8", ["const:7f922c:8", "const:4:8"]]
+ 007f922c ["CALL", null, ["ram:47ad34:8"]]
- 007f91d4 bytes c806f297
+ 007f922c bytes c206f297
- 007f91c8 ["INT_ADD", "register:40f0:8", ["const:7f91c8:8", "const:4:8"]]
- 007f91c8 ["CALL", null, ["callee:009e3ad4:8"]]
+ 007f9220 ["INT_ADD", "register:40f0:8", ["const:7f9220:8", "const:4:8"]]
+ 007f9220 ["CALL", null, ["callee:009e3ad4:8"]]
- 007f91c8 bytes 2eaa0794
+ 007f9220 bytes 2daa0794
- 007f91d0 ["INT_ADD", "register:40f0:8", ["const:7f91d0:8", "const:4:8"]]
- 007f91d0 ["CALL", null, ["callee:00a1a6f8:8"]]
+ 007f9228 ["INT_ADD", "register:40f0:8", ["const:7f9228:8", "const:4:8"]]
+ 007f9228 ["CALL", null, ["callee:00a1a6f8:8"]]
- 007f91d0 bytes 35850894
+ 007f9228 bytes 34850894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c1989a317dc6f7fc51d106086d714e1"></a>

### [`007f9224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9224.md) → [`007f927c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f927c.md) FUN_007f927c

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
      "definition_site": "007f929c",
      "incomplete_value": false,
      "site": "007f92a0",
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
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9244",
      "incomplete_value": false,
      "site": "007f9248",
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
      "007f92a0",
      "DATA",
      [
        "storage",
        "00c7c9b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f92a0",
      "DATA",
      [
        "storage",
        "00c7ca80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f9238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9224.md#insn-007f9238) · [`007f9244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9224.md#insn-007f9244)
- 新版 `007f9290`（命令位置の公開資料なし） · `007f929c`（命令位置の公開資料なし）

~~~diff
- 007f9238 ["INT_ADD", "register:40f0:8", ["const:7f9238:8", "const:4:8"]]
- 007f9238 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f9290 ["INT_ADD", "register:40f0:8", ["const:7f9290:8", "const:4:8"]]
+ 007f9290 ["CALL", null, ["callee:00c57f60:8"]]
- 007f9238 bytes 167b1194
+ 007f9290 bytes 347b1194
- 007f9244 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 007f9244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f9244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f9244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f929c ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 007f929c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f929c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f929c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f9244 bytes 08c12691
+ 007f929c bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee03a8ad9cbbd10a0485f1b9cd7b779a"></a>

### [`007f925c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f925c.md) → [`007f92b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f92b4.md) FUN_007f92b4

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
      "definition_site": "007f92b8",
      "incomplete_value": false,
      "site": "007f92bc",
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
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9260",
      "incomplete_value": false,
      "site": "007f9264",
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
      "007f92bc",
      "DATA",
      [
        "storage",
        "00c7c9b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f92bc",
      "DATA",
      [
        "storage",
        "00c7ca80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f9260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f925c.md#insn-007f9260)
- 新版 `007f92b8`（命令位置の公開資料なし）

~~~diff
- 007f9260 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 007f9260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f9260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f9260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f92b8 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 007f92b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f92b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f92b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f9260 bytes 08c12691
+ 007f92b8 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f17519607b186d798e3165fdf8e80c46"></a>

### [`007f94a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f94a8.md) → [`007f9500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9500.md) FUN_007f9500

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
      "definition_site": "007f9524",
      "incomplete_value": false,
      "site": "007f9524",
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
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f94cc",
      "incomplete_value": false,
      "site": "007f94cc",
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
      "007f9524",
      "DATA",
      [
        "storage",
        "00c7ca30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f9524",
      "DATA",
      [
        "storage",
        "00c7cb00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f94bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f94a8.md#insn-007f94bc) · [`007f94c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f94a8.md#insn-007f94c8)
- 新版 `007f9514`（命令位置の公開資料なし） · `007f9520`（命令位置の公開資料なし）

~~~diff
- 007f94bc ["INT_ADD", "register:40f0:8", ["const:7f94bc:8", "const:4:8"]]
- 007f94bc ["CALL", null, ["callee:00c57f60:8"]]
+ 007f9514 ["INT_ADD", "register:40f0:8", ["const:7f9514:8", "const:4:8"]]
+ 007f9514 ["CALL", null, ["callee:00c57f60:8"]]
- 007f94bc bytes 757a1194
+ 007f9514 bytes 937a1194
- 007f94c8 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 007f94c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f94c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f94c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f9520 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 007f9520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f94c8 bytes 08c12891
+ 007f9520 bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2716ccec3dc522db6c88cc7a3d338b2"></a>

### [`007f94dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f94dc.md) → [`007f9534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9534.md) FUN_007f9534

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
      "definition_site": "007f9540",
      "incomplete_value": false,
      "site": "007f9540",
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
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f94e8",
      "incomplete_value": false,
      "site": "007f94e8",
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
      "007f9540",
      "DATA",
      [
        "storage",
        "00c7ca30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f9540",
      "DATA",
      [
        "storage",
        "00c7cb00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f94e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f94dc.md#insn-007f94e4)
- 新版 `007f953c`（命令位置の公開資料なし）

~~~diff
- 007f94e4 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 007f94e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f94e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f94e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f953c ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 007f953c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f953c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f953c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f94e4 bytes 29c12891
+ 007f953c bytes 29012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e16299be7738fcf72ae45f4138f0532a"></a>

### [`007f94f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f94f8.md) → [`007f9550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9550.md) FUN_007f9550

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`009e3a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3a80.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`009e3ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e3ad4.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

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
      "site": "007f9590",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f9538",
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
      "007f9590",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f9590",
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

- 旧版 [`007f9538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f94f8.md#insn-007f9538) · [`007f952c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f94f8.md#insn-007f952c) · [`007f9534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f94f8.md#insn-007f9534)
- 新版 `007f9590`（命令位置の公開資料なし） · `007f9584`（命令位置の公開資料なし） · `007f958c`（命令位置の公開資料なし）

~~~diff
- 007f9538 ["INT_ADD", "register:40f0:8", ["const:7f9538:8", "const:4:8"]]
- 007f9538 ["CALL", null, ["ram:47acf4:8"]]
+ 007f9590 ["INT_ADD", "register:40f0:8", ["const:7f9590:8", "const:4:8"]]
+ 007f9590 ["CALL", null, ["ram:47ad34:8"]]
- 007f9538 bytes ef05f297
+ 007f9590 bytes e905f297
- 007f952c ["INT_ADD", "register:40f0:8", ["const:7f952c:8", "const:4:8"]]
- 007f952c ["CALL", null, ["callee:009e3ad4:8"]]
+ 007f9584 ["INT_ADD", "register:40f0:8", ["const:7f9584:8", "const:4:8"]]
+ 007f9584 ["CALL", null, ["callee:009e3ad4:8"]]
- 007f952c bytes 55a90794
+ 007f9584 bytes 54a90794
- 007f9534 ["INT_ADD", "register:40f0:8", ["const:7f9534:8", "const:4:8"]]
- 007f9534 ["CALL", null, ["callee:00a1a6f8:8"]]
+ 007f958c ["INT_ADD", "register:40f0:8", ["const:7f958c:8", "const:4:8"]]
+ 007f958c ["CALL", null, ["callee:00a1a6f8:8"]]
- 007f9534 bytes 5c840894
+ 007f958c bytes 5b840894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-696c94702e15d96f3445fc8dcbebfd62"></a>

### [`007f9588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9588.md) → [`007f95e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f95e0.md) FUN_007f95e0

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
      "definition_site": "007f9600",
      "incomplete_value": false,
      "site": "007f9604",
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
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f95a8",
      "incomplete_value": false,
      "site": "007f95ac",
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
            "const:ab0:8"
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
      "007f9604",
      "DATA",
      [
        "storage",
        "00c7cab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f9604",
      "DATA",
      [
        "storage",
        "00c7cb80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f959c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9588.md#insn-007f959c) · [`007f95a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9588.md#insn-007f95a8)
- 新版 `007f95f4`（命令位置の公開資料なし） · `007f9600`（命令位置の公開資料なし）

~~~diff
- 007f959c ["INT_ADD", "register:40f0:8", ["const:7f959c:8", "const:4:8"]]
- 007f959c ["CALL", null, ["callee:00c57f60:8"]]
+ 007f95f4 ["INT_ADD", "register:40f0:8", ["const:7f95f4:8", "const:4:8"]]
+ 007f95f4 ["CALL", null, ["callee:00c57f60:8"]]
- 007f959c bytes 3d7a1194
+ 007f95f4 bytes 5b7a1194
- 007f95a8 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 007f95a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f95a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f95a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f9600 ["COPY", "tmp:0:8", ["const:b80:8"]]
+ 007f9600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f95a8 bytes 08c12a91
+ 007f9600 bytes 08012e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff8dd1437370cc426cab35a9c4030803"></a>

### [`007f95c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f95c0.md) → [`007f9618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9618.md) FUN_007f9618

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
      "definition_site": "007f961c",
      "incomplete_value": false,
      "site": "007f9620",
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
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f95c4",
      "incomplete_value": false,
      "site": "007f95c8",
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
            "const:ab0:8"
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
      "007f9620",
      "DATA",
      [
        "storage",
        "00c7cab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f9620",
      "DATA",
      [
        "storage",
        "00c7cb80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f95c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f95c0.md#insn-007f95c4)
- 新版 `007f961c`（命令位置の公開資料なし）

~~~diff
- 007f95c4 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 007f95c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f95c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f95c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f961c ["COPY", "tmp:0:8", ["const:b80:8"]]
+ 007f961c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f961c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f961c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f95c4 bytes 08c12a91
+ 007f961c bytes 08012e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3401f53a2e91de9a4354bd7ac38dfaf"></a>

### [`007f9674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9674.md) → [`007f96cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f96cc.md) FUN_007f96cc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "007f96e0",
      "incomplete_value": false,
      "site": "007f96e4",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9688",
      "incomplete_value": false,
      "site": "007f968c",
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
            "const:b30:8"
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
      "007f96e4",
      "DATA",
      [
        "storage",
        "00c7cb30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f96e4",
      "DATA",
      [
        "storage",
        "00c7cc00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f9688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9674.md#insn-007f9688) · [`007f969c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9674.md#insn-007f969c) · [`007f96bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9674.md#insn-007f96bc)
- 新版 `007f96e0`（命令位置の公開資料なし） · `007f96f4`（命令位置の公開資料なし） · `007f9714`（命令位置の公開資料なし）

~~~diff
- 007f9688 ["COPY", "tmp:0:8", ["const:b30:8"]]
- 007f9688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f9688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f9688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f96e0 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 007f96e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f96e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f96e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f9688 bytes 08c12c91
+ 007f96e0 bytes 08013091
- 007f969c ["INT_ADD", "register:40f0:8", ["const:7f969c:8", "const:4:8"]]
- 007f969c ["CALL", null, ["callee:00c53da0:8"]]
+ 007f96f4 ["INT_ADD", "register:40f0:8", ["const:7f96f4:8", "const:4:8"]]
+ 007f96f4 ["CALL", null, ["callee:00c53da0:8"]]
- 007f969c bytes 99691194
+ 007f96f4 bytes ab691194
- 007f96bc ["COPY", "register:0:8", ["register:4040:8"]]
- 007f96bc ["INT_ADD", "register:40f0:8", ["const:7f96bc:8", "const:4:8"]]
- 007f96bc ["CALLIND", null, ["register:0:8"]]
+ 007f9714 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007f9714 ["INT_ADD", "register:40f0:8", ["const:7f9714:8", "const:4:8"]]
+ 007f9714 ["CALLIND", null, ["register:0:8"]]
- 007f96bc bytes 00013fd6
+ 007f9714 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7feb4ccf080f8c84d6348411fc36c8c"></a>

### [`007f96d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f96d0.md) → [`007f9728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9728.md) FUN_007f9728

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "007f9740",
      "incomplete_value": false,
      "site": "007f9744",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f96e8",
      "incomplete_value": false,
      "site": "007f96ec",
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
            "const:b30:8"
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
      "007f9744",
      "DATA",
      [
        "storage",
        "00c7cb30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f9744",
      "DATA",
      [
        "storage",
        "00c7cc00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f96e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f96d0.md#insn-007f96e8) · [`007f96fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f96d0.md#insn-007f96fc) · [`007f9710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f96d0.md#insn-007f9710)
- 新版 `007f9740`（命令位置の公開資料なし） · `007f9754`（命令位置の公開資料なし） · `007f9768`（命令位置の公開資料なし）

~~~diff
- 007f96e8 ["COPY", "tmp:0:8", ["const:b30:8"]]
- 007f96e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f96e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f96e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f9740 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 007f9740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f96e8 bytes 08c12c91
+ 007f9740 bytes 08013091
- 007f96fc ["INT_ADD", "register:40f0:8", ["const:7f96fc:8", "const:4:8"]]
- 007f96fc ["CALL", null, ["callee:00c53da0:8"]]
+ 007f9754 ["INT_ADD", "register:40f0:8", ["const:7f9754:8", "const:4:8"]]
+ 007f9754 ["CALL", null, ["callee:00c53da0:8"]]
- 007f96fc bytes 81691194
+ 007f9754 bytes 93691194
- 007f9710 ["COPY", "register:0:8", ["register:4040:8"]]
- 007f9710 ["INT_ADD", "register:40f0:8", ["const:7f9710:8", "const:4:8"]]
- 007f9710 ["CALLIND", null, ["register:0:8"]]
+ 007f9768 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007f9768 ["INT_ADD", "register:40f0:8", ["const:7f9768:8", "const:4:8"]]
+ 007f9768 ["CALLIND", null, ["register:0:8"]]
- 007f9710 bytes 00013fd6
+ 007f9768 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-427e4441c39e743e077b104cdcee0de6"></a>

### [`007f972c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f972c.md) → [`007f9784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9784.md) FUN_007f9784

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f97a8",
      "incomplete_value": false,
      "site": "007f97ac",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9750",
      "incomplete_value": false,
      "site": "007f9754",
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
            "const:b30:8"
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
      "007f97ac",
      "DATA",
      [
        "storage",
        "00c7cb30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f97ac",
      "DATA",
      [
        "storage",
        "00c7cc00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f9740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f972c.md#insn-007f9740) · [`007f9750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f972c.md#insn-007f9750) · [`007f9770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f972c.md#insn-007f9770)
- 新版 `007f9798`（命令位置の公開資料なし） · `007f97a8`（命令位置の公開資料なし） · `007f97c8`（命令位置の公開資料なし）

~~~diff
- 007f9740 ["INT_ADD", "register:40f0:8", ["const:7f9740:8", "const:4:8"]]
- 007f9740 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f9798 ["INT_ADD", "register:40f0:8", ["const:7f9798:8", "const:4:8"]]
+ 007f9798 ["CALL", null, ["callee:00c57f60:8"]]
- 007f9740 bytes d4791194
+ 007f9798 bytes f2791194
- 007f9750 ["COPY", "tmp:0:8", ["const:b30:8"]]
- 007f9750 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f9750 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f9750 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f97a8 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 007f97a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f97a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f97a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f9750 bytes 29c12c91
+ 007f97a8 bytes 29013091
- 007f9770 ["INT_ADD", "register:40f0:8", ["const:7f9770:8", "const:4:8"]]
- 007f9770 ["CALL", null, ["callee:00c53d70:8"]]
+ 007f97c8 ["INT_ADD", "register:40f0:8", ["const:7f97c8:8", "const:4:8"]]
+ 007f97c8 ["CALL", null, ["callee:00c53d70:8"]]
- 007f9770 bytes 58691194
+ 007f97c8 bytes 6a691194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b03e060b0526c4645c826665c2fbad5"></a>

### [`007f9784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9784.md) → [`007f97dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f97dc.md) FUN_007f97dc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f97e4",
      "incomplete_value": false,
      "site": "007f97e8",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f978c",
      "incomplete_value": false,
      "site": "007f9790",
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
            "const:b30:8"
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
      "007f97e8",
      "DATA",
      [
        "storage",
        "00c7cb30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f97e8",
      "DATA",
      [
        "storage",
        "00c7cc00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f978c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9784.md#insn-007f978c) · [`007f97b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9784.md#insn-007f97b4)
- 新版 `007f97e4`（命令位置の公開資料なし） · `007f980c`（命令位置の公開資料なし）

~~~diff
- 007f978c ["COPY", "tmp:0:8", ["const:b30:8"]]
- 007f978c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f978c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f978c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f97e4 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 007f97e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f97e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f97e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f978c bytes 29c12c91
+ 007f97e4 bytes 29013091
- 007f97b4 ["INT_ADD", "register:40f0:8", ["const:7f97b4:8", "const:4:8"]]
- 007f97b4 ["CALL", null, ["callee:00c53d70:8"]]
+ 007f980c ["INT_ADD", "register:40f0:8", ["const:7f980c:8", "const:4:8"]]
+ 007f980c ["CALL", null, ["callee:00c53d70:8"]]
- 007f97b4 bytes 47691194
+ 007f980c bytes 59691194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b55c5cc8c348a8224116bfe092d2483b"></a>

### [`007f9e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e84.md) → [`007f9edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9edc.md) FUN_007f9edc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`007f9860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9860.md) [`007f9bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9bd0.md) [`009dec20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009dec20.md) [`009e1278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1278.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 4件 [`007f98b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f98b8.md) [`007f9c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9c28.md) [`009dec74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009dec74.md) [`009e12cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e12cc.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "007f9ee8",
      "incomplete_value": false,
      "site": "007f9eec",
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
    "old": {
      "definition_site": "007f9e90",
      "incomplete_value": false,
      "site": "007f9e94",
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
            "const:f4c:8"
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
      "007f9ee8",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f9ee8",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f9e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e84.md#insn-007f9e94) · [`007f9e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e84.md#insn-007f9e90)
- 新版 `007f9eec`（命令位置の公開資料なし） · `007f9ee8`（命令位置の公開資料なし）

~~~diff
- 007f9e94 ["INT_ADD", "register:40f0:8", ["const:7f9e94:8", "const:4:8"]]
- 007f9e94 ["CALL", null, ["callee:0043b7b8:8"]]
+ 007f9eec ["INT_ADD", "register:40f0:8", ["const:7f9eec:8", "const:4:8"]]
+ 007f9eec ["CALL", null, ["callee:0043b7b8:8"]]
- 007f9e94 bytes 3906f197
+ 007f9eec bytes 3306f197
- 007f9e90 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 007f9e90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007f9e90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007f9e90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007f9ee8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 007f9ee8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007f9ee8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007f9ee8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007f9e90 bytes 00303d91
+ 007f9ee8 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b0ab8609c597b4b6d79fb018d8a22d8"></a>

### [`007fa010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa010.md) → [`007fa068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa068.md) FUN_007fa068

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
      "definition_site": "007fa08c",
      "incomplete_value": false,
      "site": "007fa08c",
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
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fa034",
      "incomplete_value": false,
      "site": "007fa034",
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
            "const:bb0:8"
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
      "007fa08c",
      "DATA",
      [
        "storage",
        "00c7cbb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fa08c",
      "DATA",
      [
        "storage",
        "00c7cc80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fa024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa010.md#insn-007fa024) · [`007fa030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa010.md#insn-007fa030)
- 新版 `007fa07c`（命令位置の公開資料なし） · `007fa088`（命令位置の公開資料なし）

~~~diff
- 007fa024 ["INT_ADD", "register:40f0:8", ["const:7fa024:8", "const:4:8"]]
- 007fa024 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fa07c ["INT_ADD", "register:40f0:8", ["const:7fa07c:8", "const:4:8"]]
+ 007fa07c ["CALL", null, ["callee:00c57f60:8"]]
- 007fa024 bytes 9b771194
+ 007fa07c bytes b9771194
- 007fa030 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 007fa030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fa030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fa030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fa088 ["COPY", "tmp:0:8", ["const:c80:8"]]
+ 007fa088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fa030 bytes 08c12e91
+ 007fa088 bytes 08013291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbd30c79e039cbc0a5124d19819cc4c1"></a>

### [`007fa044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa044.md) → [`007fa09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa09c.md) FUN_007fa09c

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
      "definition_site": "007fa0a8",
      "incomplete_value": false,
      "site": "007fa0a8",
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
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fa050",
      "incomplete_value": false,
      "site": "007fa050",
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
            "const:bb0:8"
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
      "007fa0a8",
      "DATA",
      [
        "storage",
        "00c7cbb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fa0a8",
      "DATA",
      [
        "storage",
        "00c7cc80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fa04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa044.md#insn-007fa04c)
- 新版 `007fa0a4`（命令位置の公開資料なし）

~~~diff
- 007fa04c ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 007fa04c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fa04c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fa04c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fa0a4 ["COPY", "tmp:0:8", ["const:c80:8"]]
+ 007fa0a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fa0a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fa0a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fa04c bytes 29c12e91
+ 007fa0a4 bytes 29013291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0951d47a4dc6d2ad6b57fc054a3f304"></a>

### [`007fa060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa060.md) → [`007fa0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa0b8.md) FUN_007fa0b8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`009e3a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3a80.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`009e3ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e3ad4.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

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
      "site": "007fa0f8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fa0a0",
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
      "007fa0f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007fa0f8",
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

- 旧版 [`007fa0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa060.md#insn-007fa0a0) · [`007fa094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa060.md#insn-007fa094) · [`007fa09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa060.md#insn-007fa09c)
- 新版 `007fa0f8`（命令位置の公開資料なし） · `007fa0ec`（命令位置の公開資料なし） · `007fa0f4`（命令位置の公開資料なし）

~~~diff
- 007fa0a0 ["INT_ADD", "register:40f0:8", ["const:7fa0a0:8", "const:4:8"]]
- 007fa0a0 ["CALL", null, ["ram:47acf4:8"]]
+ 007fa0f8 ["INT_ADD", "register:40f0:8", ["const:7fa0f8:8", "const:4:8"]]
+ 007fa0f8 ["CALL", null, ["ram:47ad34:8"]]
- 007fa0a0 bytes 1503f297
+ 007fa0f8 bytes 0f03f297
- 007fa094 ["INT_ADD", "register:40f0:8", ["const:7fa094:8", "const:4:8"]]
- 007fa094 ["CALL", null, ["callee:009e3ad4:8"]]
+ 007fa0ec ["INT_ADD", "register:40f0:8", ["const:7fa0ec:8", "const:4:8"]]
+ 007fa0ec ["CALL", null, ["callee:009e3ad4:8"]]
- 007fa094 bytes 7ba60794
+ 007fa0ec bytes 7aa60794
- 007fa09c ["INT_ADD", "register:40f0:8", ["const:7fa09c:8", "const:4:8"]]
- 007fa09c ["CALL", null, ["callee:00a1a6f8:8"]]
+ 007fa0f4 ["INT_ADD", "register:40f0:8", ["const:7fa0f4:8", "const:4:8"]]
+ 007fa0f4 ["CALL", null, ["callee:00a1a6f8:8"]]
- 007fa09c bytes 82810894
+ 007fa0f4 bytes 81810894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7b5c456834735808f3c4c3135a5cc4e"></a>

### [`007fa0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa0f0.md) → [`007fa148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa148.md) FUN_007fa148

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
      "definition_site": "007fa168",
      "incomplete_value": false,
      "site": "007fa16c",
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
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fa110",
      "incomplete_value": false,
      "site": "007fa114",
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
      "007fa16c",
      "DATA",
      [
        "storage",
        "00c7cc30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fa16c",
      "DATA",
      [
        "storage",
        "00c7cd00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fa104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa0f0.md#insn-007fa104) · [`007fa110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa0f0.md#insn-007fa110)
- 新版 `007fa15c`（命令位置の公開資料なし） · `007fa168`（命令位置の公開資料なし）

~~~diff
- 007fa104 ["INT_ADD", "register:40f0:8", ["const:7fa104:8", "const:4:8"]]
- 007fa104 ["CALL", null, ["callee:00c57f60:8"]]
+ 007fa15c ["INT_ADD", "register:40f0:8", ["const:7fa15c:8", "const:4:8"]]
+ 007fa15c ["CALL", null, ["callee:00c57f60:8"]]
- 007fa104 bytes 63771194
+ 007fa15c bytes 81771194
- 007fa110 ["COPY", "tmp:0:8", ["const:c30:8"]]
- 007fa110 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fa110 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fa110 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fa168 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 007fa168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fa110 bytes 08c13091
+ 007fa168 bytes 08013491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b650d21702458a46b16aeed362bbb6b"></a>

### [`007fa128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa128.md) → [`007fa180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa180.md) FUN_007fa180

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
      "definition_site": "007fa184",
      "incomplete_value": false,
      "site": "007fa188",
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
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fa12c",
      "incomplete_value": false,
      "site": "007fa130",
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
            "const:c30:8"
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
      "007fa188",
      "DATA",
      [
        "storage",
        "00c7cc30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fa188",
      "DATA",
      [
        "storage",
        "00c7cd00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fa12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa128.md#insn-007fa12c)
- 新版 `007fa184`（命令位置の公開資料なし）

~~~diff
- 007fa12c ["COPY", "tmp:0:8", ["const:c30:8"]]
- 007fa12c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fa12c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fa12c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fa184 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 007fa184 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa184 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fa12c bytes 08c13091
+ 007fa184 bytes 08013491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d8b43e40ca2019c9352357ba1604d49"></a>

### [`007fa148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa148.md) → [`007fa1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa1a0.md) FUN_007fa1a0

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 25件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007fa2c8",
      "incomplete_value": true,
      "site": "007fa2c8",
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
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:103:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fa270",
      "incomplete_value": true,
      "site": "007fa270",
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
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:d2:8"
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
      "definition_site": "007fa3c0",
      "incomplete_value": true,
      "site": "007fa3c0",
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
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fa368",
      "incomplete_value": true,
      "site": "007fa368",
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
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:f31:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007fa400",
      "incomplete_value": false,
      "site": "007fa400",
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
      "definition_site": "007fa3a8",
      "incomplete_value": false,
      "site": "007fa3a8",
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
      "007fa298",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007fa2b4",
      "READ",
      [
        "storage",
        "002b40d2",
        null,
        "string"
      ]
    ],
    [
      "007fa3a4",
      "READ",
      [
        "storage",
        "002b2f31",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007fa298",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007fa2b4",
      "READ",
      [
        "storage",
        "002b4103",
        null,
        "string"
      ]
    ],
    [
      "007fa3a4",
      "READ",
      [
        "storage",
        "002b2f62",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fa1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa148.md#insn-007fa1e8) · [`007fa240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa148.md#insn-007fa240) · [`007fa298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa148.md#insn-007fa298)
- 新版 `007fa240`（命令位置の公開資料なし） · `007fa298`（命令位置の公開資料なし） · `007fa2f0`（命令位置の公開資料なし）

~~~diff
- 007fa1e8 ["INT_ADD", "register:40f0:8", ["const:7fa1e8:8", "const:4:8"]]
- 007fa1e8 ["CALL", null, ["callee:00744fdc:8"]]
+ 007fa240 ["INT_ADD", "register:40f0:8", ["const:7fa240:8", "const:4:8"]]
+ 007fa240 ["CALL", null, ["callee:00744fdc:8"]]
- 007fa1e8 bytes 672bfd97
+ 007fa240 bytes 672bfd97
- 007fa240 ["INT_ADD", "register:40f0:8", ["const:7fa240:8", "const:4:8"]]
- 007fa240 ["CALL", null, ["ram:47acf4:8"]]
+ 007fa298 ["INT_ADD", "register:40f0:8", ["const:7fa298:8", "const:4:8"]]
+ 007fa298 ["CALL", null, ["ram:47ad34:8"]]
- 007fa240 bytes ad02f297
+ 007fa298 bytes a702f297
- 007fa298 ["INT_ADD", "register:40f0:8", ["const:7fa298:8", "const:4:8"]]
- 007fa298 ["CALL", null, ["callee:00744fdc:8"]]
+ 007fa2f0 ["INT_ADD", "register:40f0:8", ["const:7fa2f0:8", "const:4:8"]]
+ 007fa2f0 ["CALL", null, ["callee:00744fdc:8"]]
- 007fa298 bytes 3b2bfd97
+ 007fa2f0 bytes 3b2bfd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b807957852ae4552b0d7560d6fd5234"></a>

### [`007fa758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa758.md) → [`007fa7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa7b0.md) FUN_007fa7b0

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
      "definition_site": "007fa7d0",
      "incomplete_value": false,
      "site": "007fa7d4",
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
      "definition_site": "007fa778",
      "incomplete_value": false,
      "site": "007fa77c",
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
      "007fa7d4",
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
      "007fa7d4",
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

- 旧版 [`007fa76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa758.md#insn-007fa76c) · [`007fa778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa758.md#insn-007fa778)
- 新版 `007fa7c4`（命令位置の公開資料なし） · `007fa7d0`（命令位置の公開資料なし）

~~~diff
- 007fa76c ["INT_ADD", "register:40f0:8", ["const:7fa76c:8", "const:4:8"]]
- 007fa76c ["CALL", null, ["callee:00c57f60:8"]]
+ 007fa7c4 ["INT_ADD", "register:40f0:8", ["const:7fa7c4:8", "const:4:8"]]
+ 007fa7c4 ["CALL", null, ["callee:00c57f60:8"]]
- 007fa76c bytes c9751194
+ 007fa7c4 bytes e7751194
- 007fa778 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 007fa778 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fa778 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fa778 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fa7d0 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 007fa7d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa7d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fa7d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fa778 bytes 08813291
+ 007fa7d0 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

