# v16.0.1 → v16.0.2 · 最優先の変更候補 (60)

[一覧の目次](README.md)

<a id="compare-d4924de34de34d4fb25ca6cd39018921"></a>

### [`009f92c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f92c8.md) → [`009f931c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f931c.md) FUN_009f931c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009fabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md) · 呼出先 20件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0060ddc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060d/0060ddc0.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`009df634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df634.md)
- 新版 呼出元 1件 [`009fac20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fa/009fac20.md) · 呼出先 20件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0060de00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060d/0060de00.md) [`006648e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/006648e0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`009df688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df688.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.34% / 新版 98.34%

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
      "site": "009f95c0",
      "value": [
        "leaf",
        "ram:6648e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f956c",
      "value": [
        "leaf",
        "ram:6648a0:8"
      ]
    },
    "ordinal": 25,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f940c",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ],
    [
      "009f9414",
      "PARAM",
      [
        "storage",
        "003104a1",
        "_ZSt7nothrow",
        "undefined1"
      ]
    ],
    [
      "009f94c8",
      "PARAM",
      [
        "storage",
        "002bc7be",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009f940c",
      "READ",
      [
        "storage",
        "00c9b5f0",
        null,
        "pointer"
      ]
    ],
    [
      "009f9414",
      "PARAM",
      [
        "storage",
        "003104e1",
        "_ZSt7nothrow",
        "undefined1"
      ]
    ],
    [
      "009f94c8",
      "PARAM",
      [
        "storage",
        "002bc76a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f956c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f92c8.md#insn-009f956c) · [`009f95c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f92c8.md#insn-009f95c0) · [`009f9300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f92c8.md#insn-009f9300)
- 新版 `009f95c0`（命令位置の公開資料なし） · `009f9614`（命令位置の公開資料なし） · `009f9354`（命令位置の公開資料なし）

~~~diff
- 009f956c ["INT_ADD", "register:40f0:8", ["const:9f956c:8", "const:4:8"]]
- 009f956c ["CALL", null, ["ram:6648a0:8"]]
+ 009f95c0 ["INT_ADD", "register:40f0:8", ["const:9f95c0:8", "const:4:8"]]
+ 009f95c0 ["CALL", null, ["ram:6648e0:8"]]
- 009f956c bytes cdacf197
+ 009f95c0 bytes c8acf197
- 009f95c0 ["INT_ADD", "register:40f0:8", ["const:9f95c0:8", "const:4:8"]]
- 009f95c0 ["CALL", null, ["callee:0048ce94:8"]]
+ 009f9614 ["INT_ADD", "register:40f0:8", ["const:9f9614:8", "const:4:8"]]
+ 009f9614 ["CALL", null, ["callee:0048ce94:8"]]
- 009f95c0 bytes 254eea97
+ 009f9614 bytes 204eea97
- 009f9300 ["INT_ADD", "register:40f0:8", ["const:9f9300:8", "const:4:8"]]
- 009f9300 ["CALL", null, ["callee:00851550:8"]]
+ 009f9354 ["INT_ADD", "register:40f0:8", ["const:9f9354:8", "const:4:8"]]
+ 009f9354 ["CALL", null, ["callee:00851550:8"]]
- 009f9300 bytes 7e60f997
+ 009f9354 bytes 7f60f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b1c6eb41a89cac9d7f63a416222ccae"></a>

### [`009f9ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9ee0.md) → [`009f9f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f9f34.md) FUN_009f9f34

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a02be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md) · 呼出先 39件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md)
- 新版 呼出元 1件 [`00a02c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02c3c.md) · 呼出先 39件 [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b7044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7044.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.43% / 新版 95.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 12件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009fa008",
      "incomplete_value": true,
      "site": "009fa018",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4b9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f9fb4",
      "incomplete_value": true,
      "site": "009f9fc4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:50d:8"
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
      "definition_site": "009fa01c",
      "incomplete_value": true,
      "site": "009fa01c",
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
      "definition_site": "009f9fc8",
      "incomplete_value": true,
      "site": "009f9fc8",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009fa010",
      "incomplete_value": true,
      "site": "009fa020",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "009f9fbc",
      "incomplete_value": true,
      "site": "009f9fcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:450:8"
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
      "009f9f74",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f9f80",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f9f88",
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
      "009f9f74",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009f9f80",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f9f88",
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

- 旧版 [`009f9f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9ee0.md#insn-009f9f40) · [`009f9f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9ee0.md#insn-009f9f74) · [`009f9f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9ee0.md#insn-009f9f94)
- 新版 `009f9f94`（命令位置の公開資料なし） · `009f9fc8`（命令位置の公開資料なし） · `009f9fe8`（命令位置の公開資料なし）

~~~diff
- 009f9f40 ["INT_ADD", "register:40f0:8", ["const:9f9f40:8", "const:4:8"]]
- 009f9f40 ["CALL", null, ["callee:00c586e0:8"]]
+ 009f9f94 ["INT_ADD", "register:40f0:8", ["const:9f9f94:8", "const:4:8"]]
+ 009f9f94 ["CALL", null, ["callee:00c586e0:8"]]
- 009f9f40 bytes b4790994
+ 009f9f94 bytes d3790994
- 009f9f74 ["INT_ADD", "register:40f0:8", ["const:9f9f74:8", "const:4:8"]]
- 009f9f74 ["CALL", null, ["callee:00851550:8"]]
+ 009f9fc8 ["INT_ADD", "register:40f0:8", ["const:9f9fc8:8", "const:4:8"]]
+ 009f9fc8 ["CALL", null, ["callee:00851550:8"]]
- 009f9f74 bytes 615df997
+ 009f9fc8 bytes 625df997
- 009f9f94 ["INT_ADD", "register:40f0:8", ["const:9f9f94:8", "const:4:8"]]
- 009f9f94 ["CALL", null, ["callee:00a832d0:8"]]
+ 009f9fe8 ["INT_ADD", "register:40f0:8", ["const:9f9fe8:8", "const:4:8"]]
+ 009f9fe8 ["CALL", null, ["callee:00a832d0:8"]]
- 009f9f94 bytes b3240294
+ 009f9fe8 bytes ba240294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2efcbc91e9c1fecf53a974573c2705b6"></a>

### [`009fabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md) → [`009fac20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fa/009fac20.md) FUN_009fac20

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`007f36a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f36a8.md) [`009fdc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc50.md) [`00a012f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012f4.md) [`00a058bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a058bc.md) · 呼出先 40件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 4件 [`007f3700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3700.md) [`009fdca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdca4.md) [`00a01348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a01348.md) [`00a05910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05910.md) · 呼出先 40件 [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009fae08",
      "incomplete_value": false,
      "site": "009fae08",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fadb4",
      "incomplete_value": false,
      "site": "009fadb4",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009fafe0",
      "incomplete_value": false,
      "site": "009fafe0",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009faf8c",
      "incomplete_value": false,
      "site": "009faf8c",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009fb034",
      "incomplete_value": false,
      "site": "009fb034",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fafe0",
      "incomplete_value": false,
      "site": "009fafe0",
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
            "const:ca0:8"
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
      "009fac58",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009fac64",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009fac6c",
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
      "009fac58",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009fac64",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009fac6c",
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

- 旧版 [`009fac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md#insn-009fac24) · [`009fad3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md#insn-009fad3c) · [`009fae08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md#insn-009fae08)
- 新版 `009fac78`（命令位置の公開資料なし） · `009fad90`（命令位置の公開資料なし） · `009fae5c`（命令位置の公開資料なし）

~~~diff
- 009fac24 ["INT_ADD", "register:40f0:8", ["const:9fac24:8", "const:4:8"]]
- 009fac24 ["CALL", null, ["callee:00c586e0:8"]]
+ 009fac78 ["INT_ADD", "register:40f0:8", ["const:9fac78:8", "const:4:8"]]
+ 009fac78 ["CALL", null, ["callee:00c586e0:8"]]
- 009fac24 bytes 7b760994
+ 009fac78 bytes 9a760994
- 009fad3c ["INT_ADD", "register:40f0:8", ["const:9fad3c:8", "const:4:8"]]
- 009fad3c ["CALL", null, ["callee:0047e64c:8"]]
+ 009fad90 ["INT_ADD", "register:40f0:8", ["const:9fad90:8", "const:4:8"]]
+ 009fad90 ["CALL", null, ["callee:0047e64c:8"]]
- 009fad3c bytes 340eea97
+ 009fad90 bytes 2f0eea97
- 009fae08 ["INT_ADD", "register:40f0:8", ["const:9fae08:8", "const:4:8"]]
- 009fae08 ["CALL", null, ["callee:008b98b0:8"]]
+ 009fae5c ["INT_ADD", "register:40f0:8", ["const:9fae5c:8", "const:4:8"]]
+ 009fae5c ["CALL", null, ["callee:008b98b0:8"]]
- 009fae08 bytes 94fafa97
+ 009fae5c bytes 95fafa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b0b1b880cf7e0d135ae03b526e5ef39"></a>

### [`009fb44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md) → [`009fb4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fb/009fb4a0.md) FUN_009fb4a0

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 54件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 54件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`004709d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004709d4.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.64% / 新版 95.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_value` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009fb55c",
      "incomplete_value": true,
      "site": "009fb56c",
      "value": [
        "LOAD",
        "16",
        [
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
                "register:40b8:8"
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
    "old": {
      "definition_site": "009fb508",
      "incomplete_value": true,
      "site": "009fb518",
      "value": [
        "LOAD",
        "16",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:450:8"
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
      "definition_site": "009fb560",
      "incomplete_value": true,
      "site": "009fb570",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:671:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fb50c",
      "incomplete_value": true,
      "site": "009fb51c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:640:8"
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
      "definition_site": "009fb574",
      "incomplete_value": true,
      "site": "009fb574",
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
      "definition_site": "009fb520",
      "incomplete_value": true,
      "site": "009fb520",
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
      "009fb55c",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ],
    [
      "009fb560",
      "READ",
      [
        "storage",
        "002b5640",
        null,
        "string"
      ]
    ],
    [
      "009fb564",
      "READ",
      [
        "storage",
        "002b564f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009fb55c",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ],
    [
      "009fb560",
      "READ",
      [
        "storage",
        "002b5671",
        null,
        "string"
      ]
    ],
    [
      "009fb564",
      "READ",
      [
        "storage",
        "002b5680",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fb5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md#insn-009fb5a4) · [`009fb5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md#insn-009fb5c4) · [`009fb5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md#insn-009fb5c8)
- 新版 `009fb5f8`（命令位置の公開資料なし） · `009fb618`（命令位置の公開資料なし） · `009fb61c`（命令位置の公開資料なし）

~~~diff
- 009fb5a4 ["INT_ADD", "register:40f0:8", ["const:9fb5a4:8", "const:4:8"]]
- 009fb5a4 ["CALL", null, ["callee:00a834bc:8"]]
+ 009fb5f8 ["INT_ADD", "register:40f0:8", ["const:9fb5f8:8", "const:4:8"]]
+ 009fb5f8 ["CALL", null, ["callee:00a834bc:8"]]
- 009fb5a4 bytes aa1f0294
+ 009fb5f8 bytes b11f0294
- 009fb5c4 ["INT_ADD", "register:40f0:8", ["const:9fb5c4:8", "const:4:8"]]
- 009fb5c4 ["CALL", null, ["callee:00c57f80:8"]]
+ 009fb618 ["INT_ADD", "register:40f0:8", ["const:9fb618:8", "const:4:8"]]
+ 009fb618 ["CALL", null, ["callee:00c57f80:8"]]
- 009fb5c4 bytes 3b720994
+ 009fb618 bytes 5a720994
- 009fb5c8 ["INT_ADD", "register:40f0:8", ["const:9fb5c8:8", "const:4:8"]]
- 009fb5c8 ["CALL", null, ["callee:00851550:8"]]
+ 009fb61c ["INT_ADD", "register:40f0:8", ["const:9fb61c:8", "const:4:8"]]
+ 009fb61c ["CALL", null, ["callee:00851550:8"]]
- 009fb5c8 bytes cc57f997
+ 009fb61c bytes cd57f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e007689f9bacd2ec4b9600c4cbc0a6d"></a>

### [`009fcd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcd88.md) → [`009fcddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fc/009fcddc.md) FUN_009fcddc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "009fce00",
      "incomplete_value": false,
      "site": "009fce08",
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
    "old": {
      "definition_site": "009fcdac",
      "incomplete_value": false,
      "site": "009fcdb4",
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
      "009fce08",
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
      "009fce08",
      "DATA",
      [
        "storage",
        "00c8a550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fcdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcd88.md#insn-009fcdac) · [`009fcde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcd88.md#insn-009fcde4)
- 新版 `009fce00`（命令位置の公開資料なし） · `009fce38`（命令位置の公開資料なし）

~~~diff
- 009fcdac ["COPY", "tmp:0:8", ["const:480:8"]]
- 009fcdac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fcdac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fcdac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fce00 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 009fce00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fce00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fce00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fcdac bytes 08011291
+ 009fce00 bytes 08411591
- 009fcde4 ["COPY", "register:0:8", ["register:4040:8"]]
- 009fcde4 ["INT_ADD", "register:40f0:8", ["const:9fcde4:8", "const:4:8"]]
- 009fcde4 ["CALLIND", null, ["register:0:8"]]
+ 009fce38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009fce38 ["INT_ADD", "register:40f0:8", ["const:9fce38:8", "const:4:8"]]
+ 009fce38 ["CALLIND", null, ["register:0:8"]]
- 009fcde4 bytes 00013fd6
+ 009fce38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d44376e7e01b99098b113f5ed11097df"></a>

### [`009fd188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd188.md) → [`009fd1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd1dc.md) FUN_009fd1dc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009fd1f0",
      "incomplete_value": false,
      "site": "009fd1f4",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fd19c",
      "incomplete_value": false,
      "site": "009fd1a0",
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
            "const:520:8"
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
      "009fd1f4",
      "DATA",
      [
        "storage",
        "00c8a520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fd1f4",
      "DATA",
      [
        "storage",
        "00c8a5f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd188.md#insn-009fd194) · [`009fd19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd188.md#insn-009fd19c)
- 新版 `009fd1e8`（命令位置の公開資料なし） · `009fd1f0`（命令位置の公開資料なし）

~~~diff
- 009fd194 ["INT_ADD", "register:40f0:8", ["const:9fd194:8", "const:4:8"]]
- 009fd194 ["CALL", null, ["callee:00c57f60:8"]]
+ 009fd1e8 ["INT_ADD", "register:40f0:8", ["const:9fd1e8:8", "const:4:8"]]
+ 009fd1e8 ["CALL", null, ["callee:00c57f60:8"]]
- 009fd194 bytes 3f6b0994
+ 009fd1e8 bytes 5e6b0994
- 009fd19c ["COPY", "tmp:0:8", ["const:520:8"]]
- 009fd19c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fd19c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fd19c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fd1f0 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 009fd1f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd1f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd1f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fd19c bytes 08811491
+ 009fd1f0 bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b60e0c8b4e8aa4009f5db7740f453563"></a>

### [`009fd1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd1ac.md) → [`009fd200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd200.md) FUN_009fd200

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009fd204",
      "incomplete_value": false,
      "site": "009fd208",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fd1b0",
      "incomplete_value": false,
      "site": "009fd1b4",
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
            "const:520:8"
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
      "009fd208",
      "DATA",
      [
        "storage",
        "00c8a520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fd208",
      "DATA",
      [
        "storage",
        "00c8a5f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd1ac.md#insn-009fd1b0)
- 新版 `009fd204`（命令位置の公開資料なし）

~~~diff
- 009fd1b0 ["COPY", "tmp:0:8", ["const:520:8"]]
- 009fd1b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fd1b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fd1b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fd204 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 009fd204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fd1b0 bytes 08811491
+ 009fd204 bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18e610155280f669a04af5b670254270"></a>

### [`009fd238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd238.md) → [`009fd28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd28c.md) FUN_009fd28c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009fd2ac",
      "incomplete_value": false,
      "site": "009fd2b0",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fd258",
      "incomplete_value": false,
      "site": "009fd25c",
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
      "009fd2b0",
      "DATA",
      [
        "storage",
        "00c8a5a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fd2b0",
      "DATA",
      [
        "storage",
        "00c8a670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd24c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd238.md#insn-009fd24c) · [`009fd258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd238.md#insn-009fd258)
- 新版 `009fd2a0`（命令位置の公開資料なし） · `009fd2ac`（命令位置の公開資料なし）

~~~diff
- 009fd24c ["INT_ADD", "register:40f0:8", ["const:9fd24c:8", "const:4:8"]]
- 009fd24c ["CALL", null, ["callee:00c57f60:8"]]
+ 009fd2a0 ["INT_ADD", "register:40f0:8", ["const:9fd2a0:8", "const:4:8"]]
+ 009fd2a0 ["CALL", null, ["callee:00c57f60:8"]]
- 009fd24c bytes 116b0994
+ 009fd2a0 bytes 306b0994
- 009fd258 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 009fd258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fd258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fd258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fd2ac ["COPY", "tmp:0:8", ["const:670:8"]]
+ 009fd2ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd2ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd2ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fd258 bytes 08811691
+ 009fd2ac bytes 08c11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-250abb86439c4f788d311bd8a37e878a"></a>

### [`009fd270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd270.md) → [`009fd2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd2c4.md) FUN_009fd2c4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009fd2c8",
      "incomplete_value": false,
      "site": "009fd2cc",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fd274",
      "incomplete_value": false,
      "site": "009fd278",
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
      "009fd2cc",
      "DATA",
      [
        "storage",
        "00c8a5a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fd2cc",
      "DATA",
      [
        "storage",
        "00c8a670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd270.md#insn-009fd274)
- 新版 `009fd2c8`（命令位置の公開資料なし）

~~~diff
- 009fd274 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 009fd274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fd274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fd274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fd2c8 ["COPY", "tmp:0:8", ["const:670:8"]]
+ 009fd2c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd2c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd2c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fd274 bytes 08811691
+ 009fd2c8 bytes 08c11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ed7550a48ee2934e4d87b03d3bc10f9"></a>

### [`009fd290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd290.md) → [`009fd2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd2e4.md) FUN_009fd2e4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00859b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b4c.md) [`008b6a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6a5c.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`006648e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/006648e0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00859ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859ba4.md) [`008b6ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6ab4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.92% / 新版 98.92%

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
      "site": "009fd444",
      "value": [
        "leaf",
        "ram:6648e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fd3f0",
      "value": [
        "leaf",
        "ram:6648a0:8"
      ]
    },
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fd524",
      "value": [
        "leaf",
        "ram:adf288:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fd4d0",
      "value": [
        "leaf",
        "ram:adf218:8"
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
      "009fd444",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648a0"
      ]
    ],
    [
      "009fd524",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00adf218"
      ]
    ]
  ],
  "added": [
    [
      "009fd444",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648e0"
      ]
    ],
    [
      "009fd524",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00adf288"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd290.md#insn-009fd3f0) · [`009fd444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd290.md#insn-009fd444) · [`009fd4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd290.md#insn-009fd4d0)
- 新版 `009fd444`（命令位置の公開資料なし） · `009fd498`（命令位置の公開資料なし） · `009fd524`（命令位置の公開資料なし）

~~~diff
- 009fd3f0 ["INT_ADD", "register:40f0:8", ["const:9fd3f0:8", "const:4:8"]]
- 009fd3f0 ["CALL", null, ["ram:6648a0:8"]]
+ 009fd444 ["INT_ADD", "register:40f0:8", ["const:9fd444:8", "const:4:8"]]
+ 009fd444 ["CALL", null, ["ram:6648e0:8"]]
- 009fd3f0 bytes 2c9df197
+ 009fd444 bytes 279df197
- 009fd444 ["INT_ADD", "register:40f0:8", ["const:9fd444:8", "const:4:8"]]
- 009fd444 ["CALL", null, ["callee:00851550:8"]]
+ 009fd498 ["INT_ADD", "register:40f0:8", ["const:9fd498:8", "const:4:8"]]
+ 009fd498 ["CALL", null, ["callee:00851550:8"]]
- 009fd444 bytes 2d50f997
+ 009fd498 bytes 2e50f997
- 009fd4d0 ["INT_ADD", "register:40f0:8", ["const:9fd4d0:8", "const:4:8"]]
- 009fd4d0 ["CALL", null, ["ram:adf218:8"]]
+ 009fd524 ["INT_ADD", "register:40f0:8", ["const:9fd524:8", "const:4:8"]]
+ 009fd524 ["CALL", null, ["ram:adf288:8"]]
- 009fd4d0 bytes 52870394
+ 009fd524 bytes 59870394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-750ed791c864eb52e6eeae4fa7ec302d"></a>

### [`009fd5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd5d4.md) → [`009fd628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd628.md) FUN_009fd628

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009fd648",
      "incomplete_value": false,
      "site": "009fd64c",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fd5f4",
      "incomplete_value": false,
      "site": "009fd5f8",
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
            "const:620:8"
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
      "009fd64c",
      "DATA",
      [
        "storage",
        "00c8a620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fd64c",
      "DATA",
      [
        "storage",
        "00c8a6f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd5d4.md#insn-009fd5e8) · [`009fd5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd5d4.md#insn-009fd5f4)
- 新版 `009fd63c`（命令位置の公開資料なし） · `009fd648`（命令位置の公開資料なし）

~~~diff
- 009fd5e8 ["INT_ADD", "register:40f0:8", ["const:9fd5e8:8", "const:4:8"]]
- 009fd5e8 ["CALL", null, ["callee:00c57f60:8"]]
+ 009fd63c ["INT_ADD", "register:40f0:8", ["const:9fd63c:8", "const:4:8"]]
+ 009fd63c ["CALL", null, ["callee:00c57f60:8"]]
- 009fd5e8 bytes 2a6a0994
+ 009fd63c bytes 496a0994
- 009fd5f4 ["COPY", "tmp:0:8", ["const:620:8"]]
- 009fd5f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fd5f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fd5f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fd648 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 009fd648 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd648 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd648 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fd5f4 bytes 08811891
+ 009fd648 bytes 08c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e2225fb35604b07e0959cf964224147"></a>

### [`009fd60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd60c.md) → [`009fd660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd660.md) FUN_009fd660

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009fd664",
      "incomplete_value": false,
      "site": "009fd668",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fd610",
      "incomplete_value": false,
      "site": "009fd614",
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
            "const:620:8"
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
      "009fd668",
      "DATA",
      [
        "storage",
        "00c8a620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fd668",
      "DATA",
      [
        "storage",
        "00c8a6f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd60c.md#insn-009fd610)
- 新版 `009fd664`（命令位置の公開資料なし）

~~~diff
- 009fd610 ["COPY", "tmp:0:8", ["const:620:8"]]
- 009fd610 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fd610 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fd610 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fd664 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 009fd664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fd610 bytes 08811891
+ 009fd664 bytes 08c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a008897183cfa813ef6d1b7e57c948b"></a>

### [`009fd62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd62c.md) → [`009fd680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd680.md) FUN_009fd680

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) [`0046af18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af18.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/0046969c.md) [`0046af58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af58.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "009fd6e8",
      "incomplete_value": true,
      "site": "009fd6e8",
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
      "definition_site": "009fd694",
      "incomplete_value": true,
      "site": "009fd694",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009fd6f8",
      "incomplete_value": true,
      "site": "009fd700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fd6a4",
      "incomplete_value": true,
      "site": "009fd6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fd9f4",
      "value": [
        "leaf",
        "ram:9f79e4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fd9a0",
      "value": [
        "leaf",
        "ram:9f7990:8"
      ]
    },
    "ordinal": 26,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009fd6e4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009fd6f0",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009fd6f8",
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
      "009fd6e4",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009fd6f0",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009fd6f8",
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

- 旧版 [`009fd6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd62c.md#insn-009fd6ac) · [`009fd9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd62c.md#insn-009fd9a0) · [`009fd66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd62c.md#insn-009fd66c)
- 新版 `009fd700`（命令位置の公開資料なし） · `009fd9f4`（命令位置の公開資料なし） · `009fd6c0`（命令位置の公開資料なし）

~~~diff
- 009fd6ac ["INT_ADD", "register:40f0:8", ["const:9fd6ac:8", "const:4:8"]]
- 009fd6ac ["CALL", null, ["callee:00c586e0:8"]]
+ 009fd700 ["INT_ADD", "register:40f0:8", ["const:9fd700:8", "const:4:8"]]
+ 009fd700 ["CALL", null, ["callee:00c586e0:8"]]
- 009fd6ac bytes d96b0994
+ 009fd700 bytes f86b0994
- 009fd9a0 ["INT_ADD", "register:40f0:8", ["const:9fd9a0:8", "const:4:8"]]
- 009fd9a0 ["CALL", null, ["ram:9f7990:8"]]
+ 009fd9f4 ["INT_ADD", "register:40f0:8", ["const:9fd9f4:8", "const:4:8"]]
+ 009fd9f4 ["CALL", null, ["ram:9f79e4:8"]]
- 009fd9a0 bytes fce7ff97
+ 009fd9f4 bytes fce7ff97
- 009fd66c ["INT_ADD", "register:40f0:8", ["const:9fd66c:8", "const:4:8"]]
- 009fd66c ["CALL", null, ["callee:008b92e8:8"]]
+ 009fd6c0 ["INT_ADD", "register:40f0:8", ["const:9fd6c0:8", "const:4:8"]]
+ 009fd6c0 ["CALL", null, ["callee:008b92e8:8"]]
- 009fd66c bytes 09effa97
+ 009fd6c0 bytes 0aeffa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c026c0c6658a17520b57c9836819194"></a>

### [`009fdb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb30.md) → [`009fdb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdb84.md) FUN_009fdb84

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009fdba8",
      "incomplete_value": false,
      "site": "009fdba8",
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
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fdb54",
      "incomplete_value": false,
      "site": "009fdb54",
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
            "const:6a0:8"
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
      "009fdba8",
      "DATA",
      [
        "storage",
        "00c8a6a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fdba8",
      "DATA",
      [
        "storage",
        "00c8a770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fdb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb30.md#insn-009fdb44) · [`009fdb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb30.md#insn-009fdb50)
- 新版 `009fdb98`（命令位置の公開資料なし） · `009fdba4`（命令位置の公開資料なし）

~~~diff
- 009fdb44 ["INT_ADD", "register:40f0:8", ["const:9fdb44:8", "const:4:8"]]
- 009fdb44 ["CALL", null, ["callee:00c57f60:8"]]
+ 009fdb98 ["INT_ADD", "register:40f0:8", ["const:9fdb98:8", "const:4:8"]]
+ 009fdb98 ["CALL", null, ["callee:00c57f60:8"]]
- 009fdb44 bytes d3680994
+ 009fdb98 bytes f2680994
- 009fdb50 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 009fdb50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fdb50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fdb50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fdba4 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 009fdba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fdba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fdba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fdb50 bytes 08811a91
+ 009fdba4 bytes 08c11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ac1c2a0c3b9cc00200227802c6b32b8"></a>

### [`009fdb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb64.md) → [`009fdbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdbb8.md) FUN_009fdbb8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "009fdbc4",
      "incomplete_value": true,
      "site": "009fdbc4",
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
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fdb70",
      "incomplete_value": true,
      "site": "009fdb70",
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
            "const:6a0:8"
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
      "009fdbc4",
      "DATA",
      [
        "storage",
        "00c8a6a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fdbc4",
      "DATA",
      [
        "storage",
        "00c8a770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fdb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb64.md#insn-009fdb6c)
- 新版 `009fdbc0`（命令位置の公開資料なし）

~~~diff
- 009fdb6c ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 009fdb6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009fdb6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009fdb6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009fdbc0 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 009fdbc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009fdbc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009fdbc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009fdb6c bytes 29811a91
+ 009fdbc0 bytes 29c11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7f3db7b59e7bfffd93b6234edc2487b"></a>

### [`009fdb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb80.md) → [`009fdbd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdbd4.md) FUN_009fdbd4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "009fdbf4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fdba0",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "009fdc00",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fdbac",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "009fdbf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "009fdc00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "009fdbf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "009fdc00",
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

- 旧版 [`009fdba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb80.md#insn-009fdba0) · [`009fdbac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb80.md#insn-009fdbac)
- 新版 `009fdbf4`（命令位置の公開資料なし） · `009fdc00`（命令位置の公開資料なし）

~~~diff
- 009fdba0 ["INT_ADD", "register:40f0:8", ["const:9fdba0:8", "const:4:8"]]
- 009fdba0 ["CALL", null, ["ram:47acf4:8"]]
+ 009fdbf4 ["INT_ADD", "register:40f0:8", ["const:9fdbf4:8", "const:4:8"]]
+ 009fdbf4 ["CALL", null, ["ram:47ad34:8"]]
- 009fdba0 bytes 55f4e997
+ 009fdbf4 bytes 50f4e997
- 009fdbac ["INT_ADD", "register:40f0:8", ["const:9fdbac:8", "const:4:8"]]
- 009fdbac ["CALL", null, ["ram:47acf4:8"]]
+ 009fdc00 ["INT_ADD", "register:40f0:8", ["const:9fdc00:8", "const:4:8"]]
+ 009fdc00 ["CALL", null, ["ram:47ad34:8"]]
- 009fdbac bytes 52f4e997
+ 009fdc00 bytes 4df4e997
~~~


<a id="compare-adb3bca21adc3e599bb79f2aef5195f5"></a>

### [`009fdc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc00.md) → [`009fdc54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdc54.md) FUN_009fdc54

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009fdc78",
      "incomplete_value": false,
      "site": "009fdc78",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fdc24",
      "incomplete_value": false,
      "site": "009fdc24",
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
            "const:720:8"
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
      "009fdc78",
      "DATA",
      [
        "storage",
        "00c8a720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fdc78",
      "DATA",
      [
        "storage",
        "00c8a7f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fdc14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc00.md#insn-009fdc14) · [`009fdc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc00.md#insn-009fdc20)
- 新版 `009fdc68`（命令位置の公開資料なし） · `009fdc74`（命令位置の公開資料なし）

~~~diff
- 009fdc14 ["INT_ADD", "register:40f0:8", ["const:9fdc14:8", "const:4:8"]]
- 009fdc14 ["CALL", null, ["callee:00c57f60:8"]]
+ 009fdc68 ["INT_ADD", "register:40f0:8", ["const:9fdc68:8", "const:4:8"]]
+ 009fdc68 ["CALL", null, ["callee:00c57f60:8"]]
- 009fdc14 bytes 9f680994
+ 009fdc68 bytes be680994
- 009fdc20 ["COPY", "tmp:0:8", ["const:720:8"]]
- 009fdc20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fdc20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fdc20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fdc74 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 009fdc74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fdc74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fdc74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fdc20 bytes 08811c91
+ 009fdc74 bytes 08c11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84882a4116cf3d777785d2dff7a84eea"></a>

### [`009fdc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc34.md) → [`009fdc88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdc88.md) FUN_009fdc88

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009fdc94",
      "incomplete_value": false,
      "site": "009fdc94",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fdc40",
      "incomplete_value": false,
      "site": "009fdc40",
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
            "const:720:8"
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
      "009fdc94",
      "DATA",
      [
        "storage",
        "00c8a720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fdc94",
      "DATA",
      [
        "storage",
        "00c8a7f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fdc3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc34.md#insn-009fdc3c)
- 新版 `009fdc90`（命令位置の公開資料なし）

~~~diff
- 009fdc3c ["COPY", "tmp:0:8", ["const:720:8"]]
- 009fdc3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009fdc3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009fdc3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009fdc90 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 009fdc90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009fdc90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009fdc90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009fdc3c bytes 29811c91
+ 009fdc90 bytes 29c11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-457e8058f0200420c611061442e354ce"></a>

### [`009fdc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc50.md) → [`009fdca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdca4.md) FUN_009fdca4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`009fabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`009fac20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fa/009fac20.md)

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
      "site": "009fdcc4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fdc70",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "009fdcd0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fdc7c",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "009fdcc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "009fdcd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "009fdcc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "009fdcd0",
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

- 旧版 [`009fdc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc50.md#insn-009fdc70) · [`009fdc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc50.md#insn-009fdc7c)
- 新版 `009fdcc4`（命令位置の公開資料なし） · `009fdcd0`（命令位置の公開資料なし）

~~~diff
- 009fdc70 ["INT_ADD", "register:40f0:8", ["const:9fdc70:8", "const:4:8"]]
- 009fdc70 ["CALL", null, ["ram:47acf4:8"]]
+ 009fdcc4 ["INT_ADD", "register:40f0:8", ["const:9fdcc4:8", "const:4:8"]]
+ 009fdcc4 ["CALL", null, ["ram:47ad34:8"]]
- 009fdc70 bytes 21f4e997
+ 009fdcc4 bytes 1cf4e997
- 009fdc7c ["INT_ADD", "register:40f0:8", ["const:9fdc7c:8", "const:4:8"]]
- 009fdc7c ["CALL", null, ["ram:47acf4:8"]]
+ 009fdcd0 ["INT_ADD", "register:40f0:8", ["const:9fdcd0:8", "const:4:8"]]
+ 009fdcd0 ["CALL", null, ["ram:47ad34:8"]]
- 009fdc7c bytes 1ef4e997
+ 009fdcd0 bytes 19f4e997
~~~


<a id="compare-8002b85ccb64b7f0d7dc6a35b500f86e"></a>

### [`009ff1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff1b8.md) → [`009ff20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff20c.md) FUN_009ff20c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009ff218",
      "incomplete_value": false,
      "site": "009ff224",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ff1c4",
      "incomplete_value": false,
      "site": "009ff1d0",
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
            "const:7a0:8"
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
      "009ff224",
      "DATA",
      [
        "storage",
        "00c8a7a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ff224",
      "DATA",
      [
        "storage",
        "00c8a870",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ff1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff1b8.md#insn-009ff1c4)
- 新版 `009ff218`（命令位置の公開資料なし）

~~~diff
- 009ff1c4 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 009ff1c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009ff1c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009ff1c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009ff218 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 009ff218 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009ff218 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009ff218 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009ff1c4 bytes 4a811e91
+ 009ff218 bytes 4ac12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a9167cd2f924209a21256f0c7868124"></a>

### [`009ff1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff1fc.md) → [`009ff250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff250.md) FUN_009ff250

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "009ff268",
      "incomplete_value": false,
      "site": "009ff274",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ff214",
      "incomplete_value": false,
      "site": "009ff220",
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
            "const:7a0:8"
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
      "009ff274",
      "DATA",
      [
        "storage",
        "00c8a7a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ff274",
      "DATA",
      [
        "storage",
        "00c8a870",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ff214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff1fc.md#insn-009ff214) · [`009ff244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff1fc.md#insn-009ff244)
- 新版 `009ff268`（命令位置の公開資料なし） · `009ff298`（命令位置の公開資料なし）

~~~diff
- 009ff214 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 009ff214 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ff214 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ff214 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ff268 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 009ff268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ff268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ff268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ff214 bytes 08811e91
+ 009ff268 bytes 08c12191
- 009ff244 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ff244 ["INT_ADD", "register:40f0:8", ["const:9ff244:8", "const:4:8"]]
- 009ff244 ["CALLIND", null, ["register:0:8"]]
+ 009ff298 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ff298 ["INT_ADD", "register:40f0:8", ["const:9ff298:8", "const:4:8"]]
+ 009ff298 ["CALLIND", null, ["register:0:8"]]
- 009ff244 bytes 00013fd6
+ 009ff298 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecec6775dea0774472055426d0d37f1f"></a>

### [`009ff258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff258.md) → [`009ff2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff2ac.md) FUN_009ff2ac

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "009ff2c8",
      "incomplete_value": false,
      "site": "009ff2d8",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ff274",
      "incomplete_value": false,
      "site": "009ff284",
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
            "const:7a0:8"
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
      "009ff2d8",
      "DATA",
      [
        "storage",
        "00c8a7a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ff2d8",
      "DATA",
      [
        "storage",
        "00c8a870",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ff26c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff258.md#insn-009ff26c) · [`009ff274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff258.md#insn-009ff274) · [`009ff2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff258.md#insn-009ff2ac)
- 新版 `009ff2c0`（命令位置の公開資料なし） · `009ff2c8`（命令位置の公開資料なし） · `009ff300`（命令位置の公開資料なし）

~~~diff
- 009ff26c ["INT_ADD", "register:40f0:8", ["const:9ff26c:8", "const:4:8"]]
- 009ff26c ["CALL", null, ["callee:00c57f60:8"]]
+ 009ff2c0 ["INT_ADD", "register:40f0:8", ["const:9ff2c0:8", "const:4:8"]]
+ 009ff2c0 ["CALL", null, ["callee:00c57f60:8"]]
- 009ff26c bytes 09630994
+ 009ff2c0 bytes 28630994
- 009ff274 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 009ff274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ff274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ff274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ff2c8 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 009ff2c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ff2c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ff2c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ff274 bytes 08811e91
+ 009ff2c8 bytes 08c12191
- 009ff2ac ["COPY", "register:0:8", ["register:4040:8"]]
- 009ff2ac ["INT_ADD", "register:40f0:8", ["const:9ff2ac:8", "const:4:8"]]
- 009ff2ac ["CALLIND", null, ["register:0:8"]]
+ 009ff300 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ff300 ["INT_ADD", "register:40f0:8", ["const:9ff300:8", "const:4:8"]]
+ 009ff300 ["CALLIND", null, ["register:0:8"]]
- 009ff2ac bytes 00013fd6
+ 009ff300 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f164e12b65e04d41b315d386d7fce01"></a>

### [`009ff2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff2f8.md) → [`009ff34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff34c.md) FUN_009ff34c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "009ff35c",
      "incomplete_value": false,
      "site": "009ff364",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ff308",
      "incomplete_value": false,
      "site": "009ff310",
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
            "const:7a0:8"
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
      "009ff364",
      "DATA",
      [
        "storage",
        "00c8a7a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ff364",
      "DATA",
      [
        "storage",
        "00c8a870",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ff308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff2f8.md#insn-009ff308) · [`009ff344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff2f8.md#insn-009ff344) · [`009ff36c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff2f8.md#insn-009ff36c)
- 新版 `009ff35c`（命令位置の公開資料なし） · `009ff398`（命令位置の公開資料なし） · `009ff3c0`（命令位置の公開資料なし）

~~~diff
- 009ff308 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 009ff308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ff308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ff308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ff35c ["COPY", "tmp:0:8", ["const:870:8"]]
+ 009ff35c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ff35c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ff35c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ff308 bytes 08811e91
+ 009ff35c bytes 08c12191
- 009ff344 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ff344 ["INT_ADD", "register:40f0:8", ["const:9ff344:8", "const:4:8"]]
- 009ff344 ["CALLIND", null, ["register:0:8"]]
+ 009ff398 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ff398 ["INT_ADD", "register:40f0:8", ["const:9ff398:8", "const:4:8"]]
+ 009ff398 ["CALLIND", null, ["register:0:8"]]
- 009ff344 bytes 00013fd6
+ 009ff398 bytes 00013fd6
- 009ff36c ["COPY", "register:0:8", ["register:4040:8"]]
- 009ff36c ["INT_ADD", "register:40f0:8", ["const:9ff36c:8", "const:4:8"]]
- 009ff36c ["CALLIND", null, ["register:0:8"]]
+ 009ff3c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ff3c0 ["INT_ADD", "register:40f0:8", ["const:9ff3c0:8", "const:4:8"]]
+ 009ff3c0 ["CALLIND", null, ["register:0:8"]]
- 009ff36c bytes 00013fd6
+ 009ff3c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0405749524242495ca672a17206ff33"></a>

### [`009ff40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff40c.md) → [`009ff460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff460.md) FUN_009ff460

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 27件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.42% / 新版 93.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ff5dc",
      "incomplete_value": true,
      "site": "009ff5ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ec4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ff588",
      "incomplete_value": true,
      "site": "009ff598",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f18:8"
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
      "definition_site": "009ff5f0",
      "incomplete_value": true,
      "site": "009ff5f0",
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
      "definition_site": "009ff59c",
      "incomplete_value": true,
      "site": "009ff59c",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ff5e4",
      "incomplete_value": true,
      "site": "009ff5f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "009ff590",
      "incomplete_value": true,
      "site": "009ff5a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:450:8"
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
      "009ff4b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "009ff4d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "009ff5dc",
      "READ",
      [
        "storage",
        "002bcf18",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ff4b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "009ff4d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "009ff5dc",
      "READ",
      [
        "storage",
        "002bcec4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ff45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff40c.md#insn-009ff45c) · [`009ff484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff40c.md#insn-009ff484) · [`009ff4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff40c.md#insn-009ff4d8)
- 新版 `009ff4b0`（命令位置の公開資料なし） · `009ff4d8`（命令位置の公開資料なし） · `009ff52c`（命令位置の公開資料なし）

~~~diff
- 009ff45c ["INT_ADD", "register:40f0:8", ["const:9ff45c:8", "const:4:8"]]
- 009ff45c ["CALL", null, ["ram:47acf4:8"]]
+ 009ff4b0 ["INT_ADD", "register:40f0:8", ["const:9ff4b0:8", "const:4:8"]]
+ 009ff4b0 ["CALL", null, ["ram:47ad34:8"]]
- 009ff45c bytes 26eee997
+ 009ff4b0 bytes 21eee997
- 009ff484 ["INT_ADD", "register:40f0:8", ["const:9ff484:8", "const:4:8"]]
- 009ff484 ["CALL", null, ["ram:47acf4:8"]]
+ 009ff4d8 ["INT_ADD", "register:40f0:8", ["const:9ff4d8:8", "const:4:8"]]
+ 009ff4d8 ["CALL", null, ["ram:47ad34:8"]]
- 009ff484 bytes 1ceee997
+ 009ff4d8 bytes 17eee997
- 009ff4d8 ["INT_ADD", "register:40f0:8", ["const:9ff4d8:8", "const:4:8"]]
- 009ff4d8 ["CALL", null, ["callee:008b97ec:8"]]
+ 009ff52c ["INT_ADD", "register:40f0:8", ["const:9ff52c:8", "const:4:8"]]
+ 009ff52c ["CALL", null, ["callee:008b97ec:8"]]
- 009ff4d8 bytes afe8fa97
+ 009ff52c bytes b0e8fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56a25fc5ac836d23c399e1ed211fe58b"></a>

### [`009ffdb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffdb4.md) → [`009ffe08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ffe08.md) FUN_009ffe08

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009ffe14",
      "incomplete_value": false,
      "site": "009ffe20",
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
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ffdc0",
      "incomplete_value": false,
      "site": "009ffdcc",
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
            "const:810:8"
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
      "009ffe20",
      "DATA",
      [
        "storage",
        "00c8a810",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ffe20",
      "DATA",
      [
        "storage",
        "00c8a8e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ffdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffdb4.md#insn-009ffdc0)
- 新版 `009ffe14`（命令位置の公開資料なし）

~~~diff
- 009ffdc0 ["COPY", "tmp:0:8", ["const:810:8"]]
- 009ffdc0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009ffdc0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009ffdc0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009ffe14 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 009ffe14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009ffe14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009ffe14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009ffdc0 bytes 4a412091
+ 009ffe14 bytes 4a812391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-233b96f0eea6d2080f0cc629c012698d"></a>

### [`009ffe54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffe54.md) → [`009ffea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ffea8.md) FUN_009ffea8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "009ffed4",
      "incomplete_value": false,
      "site": "009ffed4",
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
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ffe80",
      "incomplete_value": false,
      "site": "009ffe80",
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
            "const:810:8"
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
      "009ffed4",
      "DATA",
      [
        "storage",
        "00c8a810",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ffed4",
      "DATA",
      [
        "storage",
        "00c8a8e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ffe68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffe54.md#insn-009ffe68) · [`009ffe78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffe54.md#insn-009ffe78) · [`009ffe9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffe54.md#insn-009ffe9c)
- 新版 `009ffebc`（命令位置の公開資料なし） · `009ffecc`（命令位置の公開資料なし） · `009ffef0`（命令位置の公開資料なし）

~~~diff
- 009ffe68 ["INT_ADD", "register:40f0:8", ["const:9ffe68:8", "const:4:8"]]
- 009ffe68 ["CALL", null, ["callee:00c57f60:8"]]
+ 009ffebc ["INT_ADD", "register:40f0:8", ["const:9ffebc:8", "const:4:8"]]
+ 009ffebc ["CALL", null, ["callee:00c57f60:8"]]
- 009ffe68 bytes 0a600994
+ 009ffebc bytes 29600994
- 009ffe78 ["COPY", "tmp:0:8", ["const:810:8"]]
- 009ffe78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ffe78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ffe78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ffecc ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 009ffecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ffecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ffecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ffe78 bytes 08412091
+ 009ffecc bytes 08812391
- 009ffe9c ["COPY", "register:0:8", ["register:4040:8"]]
- 009ffe9c ["INT_ADD", "register:40f0:8", ["const:9ffe9c:8", "const:4:8"]]
- 009ffe9c ["CALLIND", null, ["register:0:8"]]
+ 009ffef0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ffef0 ["INT_ADD", "register:40f0:8", ["const:9ffef0:8", "const:4:8"]]
+ 009ffef0 ["CALLIND", null, ["register:0:8"]]
- 009ffe9c bytes 00013fd6
+ 009ffef0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e40c77cb3cb8dfda5faac504311201ac"></a>

### [`009ffeec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffeec.md) → [`009fff40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009fff40.md) FUN_009fff40

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009fff60",
      "incomplete_value": false,
      "site": "009fff60",
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
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fff0c",
      "incomplete_value": false,
      "site": "009fff0c",
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
            "const:810:8"
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
      "009fff60",
      "DATA",
      [
        "storage",
        "00c8a810",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fff60",
      "DATA",
      [
        "storage",
        "00c8a8e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fff08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffeec.md#insn-009fff08) · [`009fff28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffeec.md#insn-009fff28) · [`009fff4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffeec.md#insn-009fff4c)
- 新版 `009fff5c`（命令位置の公開資料なし） · `009fff7c`（命令位置の公開資料なし） · `009fffa0`（命令位置の公開資料なし）

~~~diff
- 009fff08 ["COPY", "tmp:0:8", ["const:810:8"]]
- 009fff08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fff08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fff08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fff5c ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 009fff5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fff5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fff5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fff08 bytes 08412091
+ 009fff5c bytes 08812391
- 009fff28 ["COPY", "register:0:8", ["register:4040:8"]]
- 009fff28 ["INT_ADD", "register:40f0:8", ["const:9fff28:8", "const:4:8"]]
- 009fff28 ["CALLIND", null, ["register:0:8"]]
+ 009fff7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009fff7c ["INT_ADD", "register:40f0:8", ["const:9fff7c:8", "const:4:8"]]
+ 009fff7c ["CALLIND", null, ["register:0:8"]]
- 009fff28 bytes 00013fd6
+ 009fff7c bytes 00013fd6
- 009fff4c ["COPY", "register:0:8", ["register:4040:8"]]
- 009fff4c ["INT_ADD", "register:40f0:8", ["const:9fff4c:8", "const:4:8"]]
- 009fff4c ["CALLIND", null, ["register:0:8"]]
+ 009fffa0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009fffa0 ["INT_ADD", "register:40f0:8", ["const:9fffa0:8", "const:4:8"]]
+ 009fffa0 ["CALLIND", null, ["register:0:8"]]
- 009fff4c bytes 00013fd6
+ 009fffa0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c3f0574f4688142e456eaf1a61613d9"></a>

### [`009ffff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffff4.md) → [`00a00048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00048.md) FUN_00a00048

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.59% / 新版 98.59%

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
      "site": "00a00088",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a00034",
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
      "00a00088",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00a00088",
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

- 旧版 [`00a00034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffff4.md#insn-00a00034) · [`00a00040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffff4.md#insn-00a00040) · [`00a0009c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffff4.md#insn-00a0009c)
- 新版 `00a00088`（命令位置の公開資料なし） · `00a00094`（命令位置の公開資料なし） · `00a000f0`（命令位置の公開資料なし）

~~~diff
- 00a00034 ["INT_ADD", "register:40f0:8", ["const:a00034:8", "const:4:8"]]
- 00a00034 ["CALL", null, ["ram:47acf4:8"]]
+ 00a00088 ["INT_ADD", "register:40f0:8", ["const:a00088:8", "const:4:8"]]
+ 00a00088 ["CALL", null, ["ram:47ad34:8"]]
- 00a00034 bytes 30ebe997
+ 00a00088 bytes 2bebe997
- 00a00040 ["INT_ADD", "register:40f0:8", ["const:a00040:8", "const:4:8"]]
- 00a00040 ["CALL", null, ["callee:0047ce14:8"]]
+ 00a00094 ["INT_ADD", "register:40f0:8", ["const:a00094:8", "const:4:8"]]
+ 00a00094 ["CALL", null, ["callee:0047ce14:8"]]
- 00a00040 bytes 65f3e997
+ 00a00094 bytes 60f3e997
- 00a0009c ["COPY", "register:0:8", ["register:4040:8"]]
- 00a0009c ["INT_ADD", "register:40f0:8", ["const:a0009c:8", "const:4:8"]]
- 00a0009c ["CALLIND", null, ["register:0:8"]]
+ 00a000f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a000f0 ["INT_ADD", "register:40f0:8", ["const:a000f0:8", "const:4:8"]]
+ 00a000f0 ["CALLIND", null, ["register:0:8"]]
- 00a0009c bytes 00013fd6
+ 00a000f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f4d3212acbb5e20abbe140ab4c1be9e"></a>

### [`00a0013c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0013c.md) → [`00a00190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00190.md) FUN_00a00190

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00a001b8",
      "incomplete_value": false,
      "site": "00a001b8",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a00164",
      "incomplete_value": false,
      "site": "00a00164",
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
            "const:890:8"
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
      "00a001b8",
      "DATA",
      [
        "storage",
        "00c8a890",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a001b8",
      "DATA",
      [
        "storage",
        "00c8a960",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a00150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0013c.md#insn-00a00150) · [`00a00160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0013c.md#insn-00a00160)
- 新版 `00a001a4`（命令位置の公開資料なし） · `00a001b4`（命令位置の公開資料なし）

~~~diff
- 00a00150 ["INT_ADD", "register:40f0:8", ["const:a00150:8", "const:4:8"]]
- 00a00150 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a001a4 ["INT_ADD", "register:40f0:8", ["const:a001a4:8", "const:4:8"]]
+ 00a001a4 ["CALL", null, ["callee:00c57f60:8"]]
- 00a00150 bytes 505f0994
+ 00a001a4 bytes 6f5f0994
- 00a00160 ["COPY", "tmp:0:8", ["const:890:8"]]
- 00a00160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a00160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a00160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a001b4 ["COPY", "tmp:0:8", ["const:960:8"]]
+ 00a001b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a001b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a001b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a00160 bytes 08412291
+ 00a001b4 bytes 08812591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b9be70ab9f49f0dc97bc29377ab4f11"></a>

### [`00a00178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00178.md) → [`00a001cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a001cc.md) FUN_00a001cc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a001d0",
      "incomplete_value": false,
      "site": "00a001d4",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0017c",
      "incomplete_value": false,
      "site": "00a00180",
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
            "const:890:8"
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
      "00a001d4",
      "DATA",
      [
        "storage",
        "00c8a890",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a001d4",
      "DATA",
      [
        "storage",
        "00c8a960",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0017c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00178.md#insn-00a0017c)
- 新版 `00a001d0`（命令位置の公開資料なし）

~~~diff
- 00a0017c ["COPY", "tmp:0:8", ["const:890:8"]]
- 00a0017c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a0017c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a0017c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a001d0 ["COPY", "tmp:0:8", ["const:960:8"]]
+ 00a001d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a001d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a001d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a0017c bytes 08412291
+ 00a001d0 bytes 08812591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2854699c10c05865379655c8aafed11"></a>

### [`00a0033c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0033c.md) → [`00a00390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00390.md) FUN_00a00390

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a00394",
      "incomplete_value": false,
      "site": "00a00398",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a00340",
      "incomplete_value": false,
      "site": "00a00344",
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
            "const:920:8"
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
      "00a00398",
      "DATA",
      [
        "storage",
        "00c8a920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a00398",
      "DATA",
      [
        "storage",
        "00c8a9f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a00340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0033c.md#insn-00a00340)
- 新版 `00a00394`（命令位置の公開資料なし）

~~~diff
- 00a00340 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00a00340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a00340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a00340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a00394 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 00a00394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a00340 bytes 08812491
+ 00a00394 bytes 08c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16924f17df48e56dfb97f81389d3d5a1"></a>

### [`00a0035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0035c.md) → [`00a003b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a003b0.md) FUN_00a003b0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00859b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b4c.md) [`008b6a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6a5c.md)
- 新版 呼出元 0件  · 呼出先 17件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`006648e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/006648e0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00859ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859ba4.md) [`008b6ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6ab4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

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
      "site": "00a0054c",
      "value": [
        "leaf",
        "ram:6648e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a004f8",
      "value": [
        "leaf",
        "ram:6648a0:8"
      ]
    },
    "ordinal": 15,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a00640",
      "value": [
        "leaf",
        "ram:adf288:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a005ec",
      "value": [
        "leaf",
        "ram:adf218:8"
      ]
    },
    "ordinal": 26,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a0054c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648a0"
      ]
    ],
    [
      "00a00640",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00adf218"
      ]
    ]
  ],
  "added": [
    [
      "00a0054c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648e0"
      ]
    ],
    [
      "00a00640",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00adf288"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a004f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0035c.md#insn-00a004f8) · [`00a005ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0035c.md#insn-00a005ec) · [`00a00640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0035c.md#insn-00a00640)
- 新版 `00a0054c`（命令位置の公開資料なし） · `00a00640`（命令位置の公開資料なし） · `00a00694`（命令位置の公開資料なし）

~~~diff
- 00a004f8 ["INT_ADD", "register:40f0:8", ["const:a004f8:8", "const:4:8"]]
- 00a004f8 ["CALL", null, ["ram:6648a0:8"]]
+ 00a0054c ["INT_ADD", "register:40f0:8", ["const:a0054c:8", "const:4:8"]]
+ 00a0054c ["CALL", null, ["ram:6648e0:8"]]
- 00a004f8 bytes ea90f197
+ 00a0054c bytes e590f197
- 00a005ec ["INT_ADD", "register:40f0:8", ["const:a005ec:8", "const:4:8"]]
- 00a005ec ["CALL", null, ["ram:adf218:8"]]
+ 00a00640 ["INT_ADD", "register:40f0:8", ["const:a00640:8", "const:4:8"]]
+ 00a00640 ["CALL", null, ["ram:adf288:8"]]
- 00a005ec bytes 0b7b0394
+ 00a00640 bytes 127b0394
- 00a00640 ["INT_ADD", "register:40f0:8", ["const:a00640:8", "const:4:8"]]
- 00a00640 ["CALL", null, ["callee:00851550:8"]]
+ 00a00694 ["INT_ADD", "register:40f0:8", ["const:a00694:8", "const:4:8"]]
+ 00a00694 ["CALL", null, ["callee:00851550:8"]]
- 00a00640 bytes ae43f997
+ 00a00694 bytes af43f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b90f24ed9f00137472d11f065883e5d"></a>

### [`00a00724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00724.md) → [`00a00778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00778.md) FUN_00a00778

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a00798",
      "incomplete_value": false,
      "site": "00a0079c",
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
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a00744",
      "incomplete_value": false,
      "site": "00a00748",
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
      "00a0079c",
      "DATA",
      [
        "storage",
        "00c8a9a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a0079c",
      "DATA",
      [
        "storage",
        "00c8aa70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a00738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00724.md#insn-00a00738) · [`00a00744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00724.md#insn-00a00744)
- 新版 `00a0078c`（命令位置の公開資料なし） · `00a00798`（命令位置の公開資料なし）

~~~diff
- 00a00738 ["INT_ADD", "register:40f0:8", ["const:a00738:8", "const:4:8"]]
- 00a00738 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a0078c ["INT_ADD", "register:40f0:8", ["const:a0078c:8", "const:4:8"]]
+ 00a0078c ["CALL", null, ["callee:00c57f60:8"]]
- 00a00738 bytes d65d0994
+ 00a0078c bytes f55d0994
- 00a00744 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00a00744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a00744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a00744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a00798 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 00a00798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a00744 bytes 08812691
+ 00a00798 bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-067365eb8a62f2107a9ff62337fad1b9"></a>

### [`00a0075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0075c.md) → [`00a007b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a007b0.md) FUN_00a007b0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a007b4",
      "incomplete_value": false,
      "site": "00a007b8",
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
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a00760",
      "incomplete_value": false,
      "site": "00a00764",
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
            "const:9a0:8"
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
      "00a007b8",
      "DATA",
      [
        "storage",
        "00c8a9a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a007b8",
      "DATA",
      [
        "storage",
        "00c8aa70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a00760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0075c.md#insn-00a00760)
- 新版 `00a007b4`（命令位置の公開資料なし）

~~~diff
- 00a00760 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00a00760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a00760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a00760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a007b4 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 00a007b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a007b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a007b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a00760 bytes 08812691
+ 00a007b4 bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2286950b3139c0e9c4d6cf2d9b5885d7"></a>

### [`00a0077c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0077c.md) → [`00a007d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a007d0.md) FUN_00a007d0

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046af18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af18.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/0046969c.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046af58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af58.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a00834",
      "incomplete_value": true,
      "site": "00a00834",
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
      "definition_site": "00a007e0",
      "incomplete_value": true,
      "site": "00a007e0",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a00874",
      "incomplete_value": true,
      "site": "00a00874",
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
      "definition_site": "00a00820",
      "incomplete_value": true,
      "site": "00a00820",
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a0083c",
      "incomplete_value": false,
      "site": "00a0084c",
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
      "definition_site": "00a007e8",
      "incomplete_value": false,
      "site": "00a007f8",
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
      "00a00830",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00a0083c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a00844",
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
      "00a00830",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a0083c",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a00844",
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

- 旧版 [`00a007cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0077c.md#insn-00a007cc) · [`00a007f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0077c.md#insn-00a007f8) · [`00a00838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0077c.md#insn-00a00838)
- 新版 `00a00820`（命令位置の公開資料なし） · `00a0084c`（命令位置の公開資料なし） · `00a0088c`（命令位置の公開資料なし）

~~~diff
- 00a007cc ["INT_ADD", "register:40f0:8", ["const:a007cc:8", "const:4:8"]]
- 00a007cc ["CALL", null, ["callee:008b92e8:8"]]
+ 00a00820 ["INT_ADD", "register:40f0:8", ["const:a00820:8", "const:4:8"]]
+ 00a00820 ["CALL", null, ["callee:008b92e8:8"]]
- 00a007cc bytes b1e2fa97
+ 00a00820 bytes b2e2fa97
- 00a007f8 ["INT_ADD", "register:40f0:8", ["const:a007f8:8", "const:4:8"]]
- 00a007f8 ["CALL", null, ["callee:00c586e0:8"]]
+ 00a0084c ["INT_ADD", "register:40f0:8", ["const:a0084c:8", "const:4:8"]]
+ 00a0084c ["CALL", null, ["callee:00c586e0:8"]]
- 00a007f8 bytes 865f0994
+ 00a0084c bytes a55f0994
- 00a00838 ["INT_ADD", "register:40f0:8", ["const:a00838:8", "const:4:8"]]
- 00a00838 ["CALL", null, ["callee:00c586e0:8"]]
+ 00a0088c ["INT_ADD", "register:40f0:8", ["const:a0088c:8", "const:4:8"]]
+ 00a0088c ["CALL", null, ["callee:00c586e0:8"]]
- 00a00838 bytes 765f0994
+ 00a0088c bytes 955f0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a8ee386d5ead142f8bbbf74d4aa990d"></a>

### [`00a00e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e4c.md) → [`00a00ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00ea0.md) FUN_00a00ea0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a00ec4",
      "incomplete_value": false,
      "site": "00a00ec4",
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
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a00e70",
      "incomplete_value": false,
      "site": "00a00e70",
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
            "const:a20:8"
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
      "00a00ec4",
      "DATA",
      [
        "storage",
        "00c8aa20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a00ec4",
      "DATA",
      [
        "storage",
        "00c8aaf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a00e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e4c.md#insn-00a00e60) · [`00a00e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e4c.md#insn-00a00e6c)
- 新版 `00a00eb4`（命令位置の公開資料なし） · `00a00ec0`（命令位置の公開資料なし）

~~~diff
- 00a00e60 ["INT_ADD", "register:40f0:8", ["const:a00e60:8", "const:4:8"]]
- 00a00e60 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a00eb4 ["INT_ADD", "register:40f0:8", ["const:a00eb4:8", "const:4:8"]]
+ 00a00eb4 ["CALL", null, ["callee:00c57f60:8"]]
- 00a00e60 bytes 0c5c0994
+ 00a00eb4 bytes 2b5c0994
- 00a00e6c ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00a00e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a00e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a00e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a00ec0 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00a00ec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00ec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00ec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a00e6c bytes 08812891
+ 00a00ec0 bytes 08c12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-234952b207edd50b60108aefefaeaab3"></a>

### [`00a00e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e80.md) → [`00a00ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00ed4.md) FUN_00a00ed4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a00ee0",
      "incomplete_value": false,
      "site": "00a00ee0",
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
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a00e8c",
      "incomplete_value": false,
      "site": "00a00e8c",
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
            "const:a20:8"
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
      "00a00ee0",
      "DATA",
      [
        "storage",
        "00c8aa20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a00ee0",
      "DATA",
      [
        "storage",
        "00c8aaf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a00e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e80.md#insn-00a00e88)
- 新版 `00a00edc`（命令位置の公開資料なし）

~~~diff
- 00a00e88 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00a00e88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a00e88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a00e88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a00edc ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00a00edc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a00edc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a00edc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a00e88 bytes 29812891
+ 00a00edc bytes 29c12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-279731f8bf55472badd6c2ed12e577b4"></a>

### [`00a00e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e9c.md) → [`00a00ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00ef0.md) FUN_00a00ef0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 21件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)
- 新版 呼出元 0件  · 呼出先 21件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`006648e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/006648e0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.28% / 新版 98.28%

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
      "site": "00a00f40",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a00eec",
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
      "site": "00a00f5c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a00f08",
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
      "site": "00a01098",
      "value": [
        "leaf",
        "ram:6648e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a01044",
      "value": [
        "leaf",
        "ram:6648a0:8"
      ]
    },
    "ordinal": 18,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a00f40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a00f5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a01098",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648a0"
      ]
    ]
  ],
  "added": [
    [
      "00a00f40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00a00f5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00a01098",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a00eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e9c.md#insn-00a00eec) · [`00a00f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e9c.md#insn-00a00f08) · [`00a01044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e9c.md#insn-00a01044)
- 新版 `00a00f40`（命令位置の公開資料なし） · `00a00f5c`（命令位置の公開資料なし） · `00a01098`（命令位置の公開資料なし）

~~~diff
- 00a00eec ["INT_ADD", "register:40f0:8", ["const:a00eec:8", "const:4:8"]]
- 00a00eec ["CALL", null, ["ram:47acf4:8"]]
+ 00a00f40 ["INT_ADD", "register:40f0:8", ["const:a00f40:8", "const:4:8"]]
+ 00a00f40 ["CALL", null, ["ram:47ad34:8"]]
- 00a00eec bytes 82e7e997
+ 00a00f40 bytes 7de7e997
- 00a00f08 ["INT_ADD", "register:40f0:8", ["const:a00f08:8", "const:4:8"]]
- 00a00f08 ["CALL", null, ["ram:47acf4:8"]]
+ 00a00f5c ["INT_ADD", "register:40f0:8", ["const:a00f5c:8", "const:4:8"]]
+ 00a00f5c ["CALL", null, ["ram:47ad34:8"]]
- 00a00f08 bytes 7be7e997
+ 00a00f5c bytes 76e7e997
- 00a01044 ["INT_ADD", "register:40f0:8", ["const:a01044:8", "const:4:8"]]
- 00a01044 ["CALL", null, ["ram:6648a0:8"]]
+ 00a01098 ["INT_ADD", "register:40f0:8", ["const:a01098:8", "const:4:8"]]
+ 00a01098 ["CALL", null, ["ram:6648e0:8"]]
- 00a01044 bytes 178ef197
+ 00a01098 bytes 128ef197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ed756404f639d14aa367d6b119d3b54"></a>

### [`00a011b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a011b0.md) → [`00a01204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a01204.md) FUN_00a01204

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a01228",
      "incomplete_value": false,
      "site": "00a01228",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a011d4",
      "incomplete_value": false,
      "site": "00a011d4",
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
      "00a01228",
      "DATA",
      [
        "storage",
        "00c8aaa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a01228",
      "DATA",
      [
        "storage",
        "00c8ab70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a011c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a011b0.md#insn-00a011c4) · [`00a011d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a011b0.md#insn-00a011d0)
- 新版 `00a01218`（命令位置の公開資料なし） · `00a01224`（命令位置の公開資料なし）

~~~diff
- 00a011c4 ["INT_ADD", "register:40f0:8", ["const:a011c4:8", "const:4:8"]]
- 00a011c4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a01218 ["INT_ADD", "register:40f0:8", ["const:a01218:8", "const:4:8"]]
+ 00a01218 ["CALL", null, ["callee:00c57f60:8"]]
- 00a011c4 bytes 335b0994
+ 00a01218 bytes 525b0994
- 00a011d0 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00a011d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a011d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a011d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a01224 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00a01224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a01224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a01224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a011d0 bytes 08812a91
+ 00a01224 bytes 08c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73452b88a90cf082e62124c68ef587ed"></a>

### [`00a011e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a011e4.md) → [`00a01238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a01238.md) FUN_00a01238

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a01244",
      "incomplete_value": false,
      "site": "00a01244",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a011f0",
      "incomplete_value": false,
      "site": "00a011f0",
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
      "00a01244",
      "DATA",
      [
        "storage",
        "00c8aaa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a01244",
      "DATA",
      [
        "storage",
        "00c8ab70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a011ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a011e4.md#insn-00a011ec)
- 新版 `00a01240`（命令位置の公開資料なし）

~~~diff
- 00a011ec ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00a011ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a011ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a011ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a01240 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00a01240 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a01240 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a01240 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a011ec bytes 29812a91
+ 00a01240 bytes 29c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6970997227757b27ec364efc678dcac0"></a>

### [`00a01200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01200.md) → [`00a01254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a01254.md) FUN_00a01254

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f48.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa0.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "00a0128c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a01238",
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
      "site": "00a012a4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a01250",
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
      "00a0128c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a012a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00a0128c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00a012a4",
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

- 旧版 [`00a01238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01200.md#insn-00a01238) · [`00a01250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01200.md#insn-00a01250) · [`00a0121c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01200.md#insn-00a0121c)
- 新版 `00a0128c`（命令位置の公開資料なし） · `00a012a4`（命令位置の公開資料なし） · `00a01270`（命令位置の公開資料なし）

~~~diff
- 00a01238 ["INT_ADD", "register:40f0:8", ["const:a01238:8", "const:4:8"]]
- 00a01238 ["CALL", null, ["ram:47acf4:8"]]
+ 00a0128c ["INT_ADD", "register:40f0:8", ["const:a0128c:8", "const:4:8"]]
+ 00a0128c ["CALL", null, ["ram:47ad34:8"]]
- 00a01238 bytes afe6e997
+ 00a0128c bytes aae6e997
- 00a01250 ["INT_ADD", "register:40f0:8", ["const:a01250:8", "const:4:8"]]
- 00a01250 ["CALL", null, ["ram:47acf4:8"]]
+ 00a012a4 ["INT_ADD", "register:40f0:8", ["const:a012a4:8", "const:4:8"]]
+ 00a012a4 ["CALL", null, ["ram:47ad34:8"]]
- 00a01250 bytes a9e6e997
+ 00a012a4 bytes a4e6e997
- 00a0121c ["INT_ADD", "register:40f0:8", ["const:a0121c:8", "const:4:8"]]
- 00a0121c ["CALL", null, ["callee:008b6fa0:8"]]
+ 00a01270 ["INT_ADD", "register:40f0:8", ["const:a01270:8", "const:4:8"]]
+ 00a01270 ["CALL", null, ["callee:008b6fa0:8"]]
- 00a0121c bytes 4bd7fa97
+ 00a01270 bytes 4cd7fa97
~~~


<a id="compare-b654075118231d70689105e3f1520fcd"></a>

### [`00a012a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012a4.md) → [`00a012f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a012f8.md) FUN_00a012f8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a0131c",
      "incomplete_value": false,
      "site": "00a0131c",
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
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a012c8",
      "incomplete_value": false,
      "site": "00a012c8",
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
      "00a0131c",
      "DATA",
      [
        "storage",
        "00c8ab20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a0131c",
      "DATA",
      [
        "storage",
        "00c8abf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a012b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012a4.md#insn-00a012b8) · [`00a012c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012a4.md#insn-00a012c4)
- 新版 `00a0130c`（命令位置の公開資料なし） · `00a01318`（命令位置の公開資料なし）

~~~diff
- 00a012b8 ["INT_ADD", "register:40f0:8", ["const:a012b8:8", "const:4:8"]]
- 00a012b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a0130c ["INT_ADD", "register:40f0:8", ["const:a0130c:8", "const:4:8"]]
+ 00a0130c ["CALL", null, ["callee:00c57f60:8"]]
- 00a012b8 bytes f65a0994
+ 00a0130c bytes 155b0994
- 00a012c4 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00a012c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a012c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a012c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a01318 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 00a01318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a01318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a01318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a012c4 bytes 08812c91
+ 00a01318 bytes 08c12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f75cb6c82c24ee590fd0647e62ccef3f"></a>

### [`00a012d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012d8.md) → [`00a0132c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a0132c.md) FUN_00a0132c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a01338",
      "incomplete_value": false,
      "site": "00a01338",
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
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a012e4",
      "incomplete_value": false,
      "site": "00a012e4",
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
            "const:b20:8"
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
      "00a01338",
      "DATA",
      [
        "storage",
        "00c8ab20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a01338",
      "DATA",
      [
        "storage",
        "00c8abf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a012e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012d8.md#insn-00a012e0)
- 新版 `00a01334`（命令位置の公開資料なし）

~~~diff
- 00a012e0 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00a012e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a012e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a012e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a01334 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 00a01334 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a01334 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a01334 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a012e0 bytes 29812c91
+ 00a01334 bytes 29c12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-419863f86387df8fe340213784e22af2"></a>

### [`00a012f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012f4.md) → [`00a01348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a01348.md) FUN_00a01348

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`009fabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`009fac20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fa/009fac20.md)

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
      "site": "00a01368",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a01314",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "00a01374",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a01320",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00a01368",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a01374",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00a01368",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00a01374",
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

- 旧版 [`00a01314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012f4.md#insn-00a01314) · [`00a01320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012f4.md#insn-00a01320)
- 新版 `00a01368`（命令位置の公開資料なし） · `00a01374`（命令位置の公開資料なし）

~~~diff
- 00a01314 ["INT_ADD", "register:40f0:8", ["const:a01314:8", "const:4:8"]]
- 00a01314 ["CALL", null, ["ram:47acf4:8"]]
+ 00a01368 ["INT_ADD", "register:40f0:8", ["const:a01368:8", "const:4:8"]]
+ 00a01368 ["CALL", null, ["ram:47ad34:8"]]
- 00a01314 bytes 78e6e997
+ 00a01368 bytes 73e6e997
- 00a01320 ["INT_ADD", "register:40f0:8", ["const:a01320:8", "const:4:8"]]
- 00a01320 ["CALL", null, ["ram:47acf4:8"]]
+ 00a01374 ["INT_ADD", "register:40f0:8", ["const:a01374:8", "const:4:8"]]
+ 00a01374 ["CALL", null, ["ram:47ad34:8"]]
- 00a01320 bytes 75e6e997
+ 00a01374 bytes 70e6e997
~~~


<a id="compare-29a0877a802109a3f77cb9423e0e611f"></a>

### [`00a01374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01374.md) → [`00a013c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a013c8.md) FUN_00a013c8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a013dc",
      "incomplete_value": false,
      "site": "00a013e0",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a01388",
      "incomplete_value": false,
      "site": "00a0138c",
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
            "const:ba0:8"
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
      "00a013e0",
      "DATA",
      [
        "storage",
        "00c8aba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a013e0",
      "DATA",
      [
        "storage",
        "00c8ac70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a01380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01374.md#insn-00a01380) · [`00a01388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01374.md#insn-00a01388)
- 新版 `00a013d4`（命令位置の公開資料なし） · `00a013dc`（命令位置の公開資料なし）

~~~diff
- 00a01380 ["INT_ADD", "register:40f0:8", ["const:a01380:8", "const:4:8"]]
- 00a01380 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a013d4 ["INT_ADD", "register:40f0:8", ["const:a013d4:8", "const:4:8"]]
+ 00a013d4 ["CALL", null, ["callee:00c57f60:8"]]
- 00a01380 bytes c45a0994
+ 00a013d4 bytes e35a0994
- 00a01388 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00a01388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a01388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a01388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a013dc ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 00a013dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a013dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a013dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a01388 bytes 08812e91
+ 00a013dc bytes 08c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfcd44bf5f7792b05b06455e9ade8994"></a>

### [`00a01398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01398.md) → [`00a013ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a013ec.md) FUN_00a013ec

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a013f0",
      "incomplete_value": false,
      "site": "00a013f4",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0139c",
      "incomplete_value": false,
      "site": "00a013a0",
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
            "const:ba0:8"
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
      "00a013f4",
      "DATA",
      [
        "storage",
        "00c8aba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a013f4",
      "DATA",
      [
        "storage",
        "00c8ac70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0139c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01398.md#insn-00a0139c)
- 新版 `00a013f0`（命令位置の公開資料なし）

~~~diff
- 00a0139c ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00a0139c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a0139c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a0139c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a013f0 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 00a013f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a013f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a013f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a0139c bytes 08812e91
+ 00a013f0 bytes 08c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77d85ef8be1691dc4354f686974ca21f"></a>

### [`00a013b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a013b0.md) → [`00a01404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a01404.md) FUN_00a01404

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b7948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7948.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b79a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b79a0.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.67% / 新版 97.67%

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
      "site": "00a0142c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a013d8",
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
      "00a0142c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00a0142c",
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

- 旧版 [`00a013d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a013b0.md#insn-00a013d8) · [`00a013e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a013b0.md#insn-00a013e4) · [`00a01400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a013b0.md#insn-00a01400)
- 新版 `00a0142c`（命令位置の公開資料なし） · `00a01438`（命令位置の公開資料なし） · `00a01454`（命令位置の公開資料なし）

~~~diff
- 00a013d8 ["INT_ADD", "register:40f0:8", ["const:a013d8:8", "const:4:8"]]
- 00a013d8 ["CALL", null, ["ram:47acf4:8"]]
+ 00a0142c ["INT_ADD", "register:40f0:8", ["const:a0142c:8", "const:4:8"]]
+ 00a0142c ["CALL", null, ["ram:47ad34:8"]]
- 00a013d8 bytes 47e6e997
+ 00a0142c bytes 42e6e997
- 00a013e4 ["INT_ADD", "register:40f0:8", ["const:a013e4:8", "const:4:8"]]
- 00a013e4 ["CALL", null, ["callee:0047ce14:8"]]
+ 00a01438 ["INT_ADD", "register:40f0:8", ["const:a01438:8", "const:4:8"]]
+ 00a01438 ["CALL", null, ["callee:0047ce14:8"]]
- 00a013e4 bytes 7ceee997
+ 00a01438 bytes 77eee997
- 00a01400 ["INT_ADD", "register:40f0:8", ["const:a01400:8", "const:4:8"]]
- 00a01400 ["CALL", null, ["callee:00851550:8"]]
+ 00a01454 ["INT_ADD", "register:40f0:8", ["const:a01454:8", "const:4:8"]]
+ 00a01454 ["CALL", null, ["callee:00851550:8"]]
- 00a01400 bytes 3e40f997
+ 00a01454 bytes 3f40f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84e60b0b073bd1b311c18dd1f25ee6ec"></a>

### [`00a01488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01488.md) → [`00a014dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a014dc.md) FUN_00a014dc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a01500",
      "incomplete_value": true,
      "site": "00a01504",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a014ac",
      "incomplete_value": true,
      "site": "00a014b0",
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
      "00a01504",
      "DATA",
      [
        "storage",
        "00c8ac20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a01504",
      "DATA",
      [
        "storage",
        "00c8acf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0149c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01488.md#insn-00a0149c) · [`00a014ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01488.md#insn-00a014ac)
- 新版 `00a014f0`（命令位置の公開資料なし） · `00a01500`（命令位置の公開資料なし）

~~~diff
- 00a0149c ["INT_ADD", "register:40f0:8", ["const:a0149c:8", "const:4:8"]]
- 00a0149c ["CALL", null, ["callee:00c57f60:8"]]
+ 00a014f0 ["INT_ADD", "register:40f0:8", ["const:a014f0:8", "const:4:8"]]
+ 00a014f0 ["CALL", null, ["callee:00c57f60:8"]]
- 00a0149c bytes 7d5a0994
+ 00a014f0 bytes 9c5a0994
- 00a014ac ["COPY", "tmp:0:8", ["const:c20:8"]]
- 00a014ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a014ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a014ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a01500 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 00a01500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a01500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a01500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a014ac bytes 08813091
+ 00a01500 bytes 08c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c5e5b25a806cc5ab7bee452c206a94f"></a>

### [`00a014c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a014c8.md) → [`00a0151c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a0151c.md) FUN_00a0151c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a01520",
      "incomplete_value": false,
      "site": "00a01524",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a014cc",
      "incomplete_value": false,
      "site": "00a014d0",
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
      "00a01524",
      "DATA",
      [
        "storage",
        "00c8ac20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a01524",
      "DATA",
      [
        "storage",
        "00c8acf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a014cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a014c8.md#insn-00a014cc)
- 新版 `00a01520`（命令位置の公開資料なし）

~~~diff
- 00a014cc ["COPY", "tmp:0:8", ["const:c20:8"]]
- 00a014cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a014cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a014cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a01520 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 00a01520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a01520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a01520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a014cc bytes 08813091
+ 00a01520 bytes 08c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb886bc62ceecb41bd4f897dcfb8c37c"></a>

### [`00a014f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a014f0.md) → [`00a01544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a01544.md) FUN_00a01544

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 33件 [`0046da48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da48.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md)
- 新版 呼出元 0件  · 呼出先 33件 [`0046da88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da88.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`004939d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.03% / 新版 98.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a01be8",
      "incomplete_value": true,
      "site": "00a01be8",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:67d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a01b94",
      "incomplete_value": true,
      "site": "00a01b94",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:63d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a01bec",
      "incomplete_value": true,
      "site": "00a01bec",
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
      "definition_site": "00a01b98",
      "incomplete_value": true,
      "site": "00a01b98",
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
    "ordinal": 48,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a01790",
      "incomplete_value": false,
      "site": "00a0179c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:76d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0173c",
      "incomplete_value": false,
      "site": "00a01748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:7ba:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a015a0",
      "DATA",
      [
        "storage",
        "00436bd4",
        null,
        "byte[59]"
      ]
    ],
    [
      "00a015b8",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[59]"
      ]
    ],
    [
      "00a015c8",
      "DATA",
      [
        "storage",
        "00436bc8",
        null,
        "byte[59]"
      ]
    ]
  ],
  "added": [
    [
      "00a015a0",
      "DATA",
      [
        "storage",
        "00436bd4",
        null,
        "byte[47]"
      ]
    ],
    [
      "00a015b8",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[47]"
      ]
    ],
    [
      "00a015c8",
      "DATA",
      [
        "storage",
        "00436bc8",
        null,
        "byte[47]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a016f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a014f0.md#insn-00a016f4) · [`00a01748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a014f0.md#insn-00a01748) · [`00a01780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a014f0.md#insn-00a01780)
- 新版 `00a01748`（命令位置の公開資料なし） · `00a0179c`（命令位置の公開資料なし） · `00a017d4`（命令位置の公開資料なし）

~~~diff
- 00a016f4 ["INT_ADD", "register:40f0:8", ["const:a016f4:8", "const:4:8"]]
- 00a016f4 ["CALL", null, ["callee:00851550:8"]]
+ 00a01748 ["INT_ADD", "register:40f0:8", ["const:a01748:8", "const:4:8"]]
+ 00a01748 ["CALL", null, ["callee:00851550:8"]]
- 00a016f4 bytes 813ff997
+ 00a01748 bytes 823ff997
- 00a01748 ["INT_ADD", "register:40f0:8", ["const:a01748:8", "const:4:8"]]
- 00a01748 ["CALL", null, ["callee:00c58030:8"]]
+ 00a0179c ["INT_ADD", "register:40f0:8", ["const:a0179c:8", "const:4:8"]]
+ 00a0179c ["CALL", null, ["callee:00c58030:8"]]
- 00a01748 bytes 065a0994
+ 00a0179c bytes 255a0994
- 00a01780 ["INT_ADD", "register:40f0:8", ["const:a01780:8", "const:4:8"]]
- 00a01780 ["CALL", null, ["callee:00c58030:8"]]
+ 00a017d4 ["INT_ADD", "register:40f0:8", ["const:a017d4:8", "const:4:8"]]
+ 00a017d4 ["CALL", null, ["callee:00c58030:8"]]
- 00a01780 bytes f8590994
+ 00a017d4 bytes 175a0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71b74087b7e92db06c55e02587935142"></a>

### [`00a02280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02280.md) → [`00a022d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a022d4.md) FUN_00a022d4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a022f4",
      "incomplete_value": false,
      "site": "00a022f8",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a022a0",
      "incomplete_value": false,
      "site": "00a022a4",
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
      "00a022f8",
      "DATA",
      [
        "storage",
        "00c8aca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a022f8",
      "DATA",
      [
        "storage",
        "00c8ad70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a02294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02280.md#insn-00a02294) · [`00a022a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02280.md#insn-00a022a0)
- 新版 `00a022e8`（命令位置の公開資料なし） · `00a022f4`（命令位置の公開資料なし）

~~~diff
- 00a02294 ["INT_ADD", "register:40f0:8", ["const:a02294:8", "const:4:8"]]
- 00a02294 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a022e8 ["INT_ADD", "register:40f0:8", ["const:a022e8:8", "const:4:8"]]
+ 00a022e8 ["CALL", null, ["callee:00c57f60:8"]]
- 00a02294 bytes ff560994
+ 00a022e8 bytes 1e570994
- 00a022a0 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00a022a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a022a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a022a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a022f4 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00a022f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a022f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a022f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a022a0 bytes 08813291
+ 00a022f4 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-190e27df83fa883b29968145b8ec72f1"></a>

### [`00a022b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022b8.md) → [`00a0230c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a0230c.md) FUN_00a0230c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a02310",
      "incomplete_value": false,
      "site": "00a02314",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a022bc",
      "incomplete_value": false,
      "site": "00a022c0",
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
      "00a02314",
      "DATA",
      [
        "storage",
        "00c8aca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a02314",
      "DATA",
      [
        "storage",
        "00c8ad70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a022bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022b8.md#insn-00a022bc)
- 新版 `00a02310`（命令位置の公開資料なし）

~~~diff
- 00a022bc ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00a022bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a022bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a022bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a02310 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00a02310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a02310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a02310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a022bc bytes 08813291
+ 00a02310 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78972e77c9cbcda8ad90322bc61b49e9"></a>

### [`00a022d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022d8.md) → [`00a0232c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a0232c.md) FUN_00a0232c

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 19件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467df4.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.58% / 新版 99.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a026d4",
      "incomplete_value": false,
      "site": "00a026d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:da5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02680",
      "incomplete_value": false,
      "site": "00a02684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:d74:8"
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a02688",
      "DATA",
      [
        "storage",
        "00436bd4",
        null,
        "byte[59]"
      ]
    ],
    [
      "00a026d4",
      "PARAM",
      [
        "storage",
        "002b3d74",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a02688",
      "DATA",
      [
        "storage",
        "00436bd4",
        null,
        "byte[47]"
      ]
    ],
    [
      "00a026d4",
      "PARAM",
      [
        "storage",
        "002b3da5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a02684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022d8.md#insn-00a02684) · [`00a02308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022d8.md#insn-00a02308) · [`00a02318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022d8.md#insn-00a02318)
- 新版 `00a026d8`（命令位置の公開資料なし） · `00a0235c`（命令位置の公開資料なし） · `00a0236c`（命令位置の公開資料なし）

~~~diff
- 00a02684 ["INT_ADD", "register:40f0:8", ["const:a02684:8", "const:4:8"]]
- 00a02684 ["CALL", null, ["callee:00442970:8"]]
+ 00a026d8 ["INT_ADD", "register:40f0:8", ["const:a026d8:8", "const:4:8"]]
+ 00a026d8 ["CALL", null, ["callee:00442970:8"]]
- 00a02684 bytes ab00e997
+ 00a026d8 bytes a600e997
- 00a02308 ["INT_ADD", "register:40f0:8", ["const:a02308:8", "const:4:8"]]
- 00a02308 ["CALL", null, ["callee:008b92e8:8"]]
+ 00a0235c ["INT_ADD", "register:40f0:8", ["const:a0235c:8", "const:4:8"]]
+ 00a0235c ["CALL", null, ["callee:008b92e8:8"]]
- 00a02308 bytes e2dbfa97
+ 00a0235c bytes e3dbfa97
- 00a02318 ["INT_ADD", "register:40f0:8", ["const:a02318:8", "const:4:8"]]
- 00a02318 ["CALL", null, ["callee:008b92e8:8"]]
+ 00a0236c ["INT_ADD", "register:40f0:8", ["const:a0236c:8", "const:4:8"]]
+ 00a0236c ["CALL", null, ["callee:008b92e8:8"]]
- 00a02318 bytes dedbfa97
+ 00a0236c bytes dfdbfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e64405d3828a2ed1b19ea73e00ac2b7c"></a>

### [`00a026b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a026b4.md) → [`00a02708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02708.md) FUN_00a02708

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a0272c",
      "incomplete_value": false,
      "site": "00a0272c",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a026d8",
      "incomplete_value": false,
      "site": "00a026d8",
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
      "00a0272c",
      "DATA",
      [
        "storage",
        "00c8ad20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a0272c",
      "DATA",
      [
        "storage",
        "00c8adf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a026c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a026b4.md#insn-00a026c8) · [`00a026d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a026b4.md#insn-00a026d4)
- 新版 `00a0271c`（命令位置の公開資料なし） · `00a02728`（命令位置の公開資料なし）

~~~diff
- 00a026c8 ["INT_ADD", "register:40f0:8", ["const:a026c8:8", "const:4:8"]]
- 00a026c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a0271c ["INT_ADD", "register:40f0:8", ["const:a0271c:8", "const:4:8"]]
+ 00a0271c ["CALL", null, ["callee:00c57f60:8"]]
- 00a026c8 bytes f2550994
+ 00a0271c bytes 11560994
- 00a026d4 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00a026d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a026d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a026d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a02728 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 00a02728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a02728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a02728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a026d4 bytes 08813491
+ 00a02728 bytes 08c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbfbbd5a3e878fe0234b05065016afba"></a>

### [`00a026e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a026e8.md) → [`00a0273c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a0273c.md) FUN_00a0273c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a02748",
      "incomplete_value": false,
      "site": "00a02748",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a026f4",
      "incomplete_value": false,
      "site": "00a026f4",
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
      "00a02748",
      "DATA",
      [
        "storage",
        "00c8ad20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a02748",
      "DATA",
      [
        "storage",
        "00c8adf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a026f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a026e8.md#insn-00a026f0)
- 新版 `00a02744`（命令位置の公開資料なし）

~~~diff
- 00a026f0 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00a026f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a026f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a026f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a02744 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 00a02744 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a02744 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a02744 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a026f0 bytes 29813491
+ 00a02744 bytes 29c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ca4f990d07347c249dce5e10c3e9440"></a>

### [`00a02704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02704.md) → [`00a02758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02758.md) FUN_00a02758

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f48.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa0.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "00a02790",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0273c",
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
      "site": "00a027a8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a02754",
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
      "00a02790",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a027a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00a02790",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00a027a8",
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

- 旧版 [`00a0273c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02704.md#insn-00a0273c) · [`00a02754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02704.md#insn-00a02754) · [`00a02720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02704.md#insn-00a02720)
- 新版 `00a02790`（命令位置の公開資料なし） · `00a027a8`（命令位置の公開資料なし） · `00a02774`（命令位置の公開資料なし）

~~~diff
- 00a0273c ["INT_ADD", "register:40f0:8", ["const:a0273c:8", "const:4:8"]]
- 00a0273c ["CALL", null, ["ram:47acf4:8"]]
+ 00a02790 ["INT_ADD", "register:40f0:8", ["const:a02790:8", "const:4:8"]]
+ 00a02790 ["CALL", null, ["ram:47ad34:8"]]
- 00a0273c bytes 6ee1e997
+ 00a02790 bytes 69e1e997
- 00a02754 ["INT_ADD", "register:40f0:8", ["const:a02754:8", "const:4:8"]]
- 00a02754 ["CALL", null, ["ram:47acf4:8"]]
+ 00a027a8 ["INT_ADD", "register:40f0:8", ["const:a027a8:8", "const:4:8"]]
+ 00a027a8 ["CALL", null, ["ram:47ad34:8"]]
- 00a02754 bytes 68e1e997
+ 00a027a8 bytes 63e1e997
- 00a02720 ["INT_ADD", "register:40f0:8", ["const:a02720:8", "const:4:8"]]
- 00a02720 ["CALL", null, ["callee:008b6fa0:8"]]
+ 00a02774 ["INT_ADD", "register:40f0:8", ["const:a02774:8", "const:4:8"]]
+ 00a02774 ["CALL", null, ["callee:008b6fa0:8"]]
- 00a02720 bytes 0ad2fa97
+ 00a02774 bytes 0bd2fa97
~~~


<a id="compare-996735cf0b5174285d7760738d21e05c"></a>

### [`00a027a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a027a4.md) → [`00a027f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a027f8.md) FUN_00a027f8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00a02810",
      "incomplete_value": false,
      "site": "00a0281c",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a027bc",
      "incomplete_value": false,
      "site": "00a027c8",
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
      "00a0281c",
      "DATA",
      [
        "storage",
        "00c8ada0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a0281c",
      "DATA",
      [
        "storage",
        "00c8ae70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a027bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a027a4.md#insn-00a027bc) · [`00a027ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a027a4.md#insn-00a027ec)
- 新版 `00a02810`（命令位置の公開資料なし） · `00a02840`（命令位置の公開資料なし）

~~~diff
- 00a027bc ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00a027bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a027bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a027bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a02810 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00a02810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a02810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a02810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a027bc bytes 08813691
+ 00a02810 bytes 08c13991
- 00a027ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00a027ec ["INT_ADD", "register:40f0:8", ["const:a027ec:8", "const:4:8"]]
- 00a027ec ["CALLIND", null, ["register:0:8"]]
+ 00a02840 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a02840 ["INT_ADD", "register:40f0:8", ["const:a02840:8", "const:4:8"]]
+ 00a02840 ["CALLIND", null, ["register:0:8"]]
- 00a027ec bytes 00013fd6
+ 00a02840 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a9ce343bb4af504c543a691a73e83e6"></a>

### [`00a02834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02834.md) → [`00a02888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02888.md) FUN_00a02888

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00a028a0",
      "incomplete_value": false,
      "site": "00a028ac",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0284c",
      "incomplete_value": false,
      "site": "00a02858",
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
      "00a028ac",
      "DATA",
      [
        "storage",
        "00c8ada0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a028ac",
      "DATA",
      [
        "storage",
        "00c8ae70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a028ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02834.md#insn-00a028ac) · [`00a0284c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02834.md#insn-00a0284c) · [`00a0287c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02834.md#insn-00a0287c)
- 新版 `00a02900`（命令位置の公開資料なし） · `00a028a0`（命令位置の公開資料なし） · `00a028d0`（命令位置の公開資料なし）

~~~diff
- 00a028ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00a028ac ["INT_ADD", "register:40f0:8", ["const:a028ac:8", "const:4:8"]]
- 00a028ac ["CALLIND", null, ["register:0:8"]]
+ 00a02900 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a02900 ["INT_ADD", "register:40f0:8", ["const:a02900:8", "const:4:8"]]
+ 00a02900 ["CALLIND", null, ["register:0:8"]]
- 00a028ac bytes 00013fd6
+ 00a02900 bytes 00013fd6
- 00a0284c ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00a0284c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a0284c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a0284c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a028a0 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00a028a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a028a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a028a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a0284c bytes 08813691
+ 00a028a0 bytes 08c13991
- 00a0287c ["COPY", "register:0:8", ["register:4040:8"]]
- 00a0287c ["INT_ADD", "register:40f0:8", ["const:a0287c:8", "const:4:8"]]
- 00a0287c ["CALLIND", null, ["register:0:8"]]
+ 00a028d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a028d0 ["INT_ADD", "register:40f0:8", ["const:a028d0:8", "const:4:8"]]
+ 00a028d0 ["CALLIND", null, ["register:0:8"]]
- 00a0287c bytes 00013fd6
+ 00a028d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fdd4c4fb202a8e7f713f408d54fa3a2"></a>

### [`00a028c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a028c0.md) → [`00a02914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02914.md) FUN_00a02914

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00a02940",
      "incomplete_value": false,
      "site": "00a02948",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a028ec",
      "incomplete_value": false,
      "site": "00a028f4",
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
            "const:da0:8"
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
      "00a02948",
      "DATA",
      [
        "storage",
        "00c8ada0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a02948",
      "DATA",
      [
        "storage",
        "00c8ae70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a028d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a028c0.md#insn-00a028d8) · [`00a028ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a028c0.md#insn-00a028ec) · [`00a02914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a028c0.md#insn-00a02914)
- 新版 `00a0292c`（命令位置の公開資料なし） · `00a02940`（命令位置の公開資料なし） · `00a02968`（命令位置の公開資料なし）

~~~diff
- 00a028d8 ["INT_ADD", "register:40f0:8", ["const:a028d8:8", "const:4:8"]]
- 00a028d8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a0292c ["INT_ADD", "register:40f0:8", ["const:a0292c:8", "const:4:8"]]
+ 00a0292c ["CALL", null, ["callee:00c57f60:8"]]
- 00a028d8 bytes 6e550994
+ 00a0292c bytes 8d550994
- 00a028ec ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00a028ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a028ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a028ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a02940 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00a02940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a02940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a02940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a028ec bytes 29813691
+ 00a02940 bytes 29c13991
- 00a02914 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a02914 ["INT_ADD", "register:40f0:8", ["const:a02914:8", "const:4:8"]]
- 00a02914 ["CALLIND", null, ["register:0:8"]]
+ 00a02968 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a02968 ["INT_ADD", "register:40f0:8", ["const:a02968:8", "const:4:8"]]
+ 00a02968 ["CALLIND", null, ["register:0:8"]]
- 00a02914 bytes 00013fd6
+ 00a02968 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78c9870ad7a9637fcf156746d5c69dd9"></a>

### [`00a029d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a029d0.md) → [`00a02a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02a24.md) FUN_00a02a24

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a02a48",
      "incomplete_value": false,
      "site": "00a02a50",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a029f4",
      "incomplete_value": false,
      "site": "00a029fc",
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
            "const:da0:8"
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
      "00a02a50",
      "DATA",
      [
        "storage",
        "00c8ada0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a02a50",
      "DATA",
      [
        "storage",
        "00c8ae70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a029f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a029d0.md#insn-00a029f4) · [`00a02a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a029d0.md#insn-00a02a1c) · [`00a02a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a029d0.md#insn-00a02a54)
- 新版 `00a02a48`（命令位置の公開資料なし） · `00a02a70`（命令位置の公開資料なし） · `00a02aa8`（命令位置の公開資料なし）

~~~diff
- 00a029f4 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00a029f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a029f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a029f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a02a48 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00a02a48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a02a48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a02a48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a029f4 bytes 29813691
+ 00a02a48 bytes 29c13991
- 00a02a1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00a02a1c ["INT_ADD", "register:40f0:8", ["const:a02a1c:8", "const:4:8"]]
- 00a02a1c ["CALLIND", null, ["register:0:8"]]
+ 00a02a70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a02a70 ["INT_ADD", "register:40f0:8", ["const:a02a70:8", "const:4:8"]]
+ 00a02a70 ["CALLIND", null, ["register:0:8"]]
- 00a02a1c bytes 00013fd6
+ 00a02a70 bytes 00013fd6
- 00a02a54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a02a54 ["INT_ADD", "register:40f0:8", ["const:a02a54:8", "const:4:8"]]
- 00a02a54 ["CALLIND", null, ["register:0:8"]]
+ 00a02aa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a02aa8 ["INT_ADD", "register:40f0:8", ["const:a02aa8:8", "const:4:8"]]
+ 00a02aa8 ["CALLIND", null, ["register:0:8"]]
- 00a02a54 bytes 00013fd6
+ 00a02aa8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83a2c3632335a879553419d95809d11f"></a>

### [`00a02be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md) → [`00a02c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02c3c.md) FUN_00a02c3c

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 28件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 0件  · 呼出先 28件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a02fdc",
      "incomplete_value": true,
      "site": "00a02fec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:230:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02f88",
      "incomplete_value": true,
      "site": "00a02f98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:28c:8"
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
      "definition_site": "00a02ff0",
      "incomplete_value": true,
      "site": "00a02ff0",
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
      "definition_site": "00a02f9c",
      "incomplete_value": true,
      "site": "00a02f9c",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a02fe4",
      "incomplete_value": true,
      "site": "00a02ff4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00a02f90",
      "incomplete_value": true,
      "site": "00a02fa0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:450:8"
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
      "00a02cc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a02cf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a02fdc",
      "READ",
      [
        "storage",
        "002b028c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a02cc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00a02cf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00a02fdc",
      "READ",
      [
        "storage",
        "002b0230",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a02c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md#insn-00a02c20) · [`00a02c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md#insn-00a02c74) · [`00a02c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md#insn-00a02c9c)
- 新版 `00a02c74`（命令位置の公開資料なし） · `00a02cc8`（命令位置の公開資料なし） · `00a02cf0`（命令位置の公開資料なし）

~~~diff
- 00a02c20 ["INT_ADD", "register:40f0:8", ["const:a02c20:8", "const:4:8"]]
- 00a02c20 ["CALL", null, ["callee:00851550:8"]]
+ 00a02c74 ["INT_ADD", "register:40f0:8", ["const:a02c74:8", "const:4:8"]]
+ 00a02c74 ["CALL", null, ["callee:00851550:8"]]
- 00a02c20 bytes 363af997
+ 00a02c74 bytes 373af997
- 00a02c74 ["INT_ADD", "register:40f0:8", ["const:a02c74:8", "const:4:8"]]
- 00a02c74 ["CALL", null, ["ram:47acf4:8"]]
+ 00a02cc8 ["INT_ADD", "register:40f0:8", ["const:a02cc8:8", "const:4:8"]]
+ 00a02cc8 ["CALL", null, ["ram:47ad34:8"]]
- 00a02c74 bytes 20e0e997
+ 00a02cc8 bytes 1be0e997
- 00a02c9c ["INT_ADD", "register:40f0:8", ["const:a02c9c:8", "const:4:8"]]
- 00a02c9c ["CALL", null, ["ram:47acf4:8"]]
+ 00a02cf0 ["INT_ADD", "register:40f0:8", ["const:a02cf0:8", "const:4:8"]]
+ 00a02cf0 ["CALL", null, ["ram:47ad34:8"]]
- 00a02c9c bytes 16e0e997
+ 00a02cf0 bytes 11e0e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-affe4fa4640aa690d05f1ed0c0b1fa40"></a>

### [`00a03794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03794.md) → [`00a037e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a037e8.md) FUN_00a037e8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00a037f4",
      "incomplete_value": false,
      "site": "00a03800",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a037a0",
      "incomplete_value": false,
      "site": "00a037ac",
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
            "const:e10:8"
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
      "00a03800",
      "DATA",
      [
        "storage",
        "00c8ae10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a03800",
      "DATA",
      [
        "storage",
        "00c8aee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a037a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03794.md#insn-00a037a0)
- 新版 `00a037f4`（命令位置の公開資料なし）

~~~diff
- 00a037a0 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 00a037a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00a037a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00a037a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00a037f4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a037f4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00a037f4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00a037f4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00a037a0 bytes 4a413891
+ 00a037f4 bytes 4a813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b78202b0c19bfb25cee50972c2632ead"></a>

### [`00a037d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a037d8.md) → [`00a0382c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a0382c.md) FUN_00a0382c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00a03844",
      "incomplete_value": false,
      "site": "00a03850",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a037f0",
      "incomplete_value": false,
      "site": "00a037fc",
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
            "const:e10:8"
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
      "00a03850",
      "DATA",
      [
        "storage",
        "00c8ae10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a03850",
      "DATA",
      [
        "storage",
        "00c8aee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a037f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a037d8.md#insn-00a037f0) · [`00a03820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a037d8.md#insn-00a03820)
- 新版 `00a03844`（命令位置の公開資料なし） · `00a03874`（命令位置の公開資料なし）

~~~diff
- 00a037f0 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 00a037f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a037f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a037f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a03844 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a03844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a037f0 bytes 08413891
+ 00a03844 bytes 08813b91
- 00a03820 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03820 ["INT_ADD", "register:40f0:8", ["const:a03820:8", "const:4:8"]]
- 00a03820 ["CALLIND", null, ["register:0:8"]]
+ 00a03874 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03874 ["INT_ADD", "register:40f0:8", ["const:a03874:8", "const:4:8"]]
+ 00a03874 ["CALLIND", null, ["register:0:8"]]
- 00a03820 bytes 00013fd6
+ 00a03874 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3925113d653de013efbe46ef96cb1b48"></a>

### [`00a038c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a038c4.md) → [`00a03918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03918.md) FUN_00a03918

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00a03938",
      "incomplete_value": false,
      "site": "00a03938",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a038e4",
      "incomplete_value": false,
      "site": "00a038e4",
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
            "const:e10:8"
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
      "00a03938",
      "DATA",
      [
        "storage",
        "00c8ae10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a03938",
      "DATA",
      [
        "storage",
        "00c8aee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a038e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a038c4.md#insn-00a038e0) · [`00a03900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a038c4.md#insn-00a03900) · [`00a03924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a038c4.md#insn-00a03924)
- 新版 `00a03934`（命令位置の公開資料なし） · `00a03954`（命令位置の公開資料なし） · `00a03978`（命令位置の公開資料なし）

~~~diff
- 00a038e0 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 00a038e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a038e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a038e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a03934 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a03934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a038e0 bytes 08413891
+ 00a03934 bytes 08813b91
- 00a03900 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03900 ["INT_ADD", "register:40f0:8", ["const:a03900:8", "const:4:8"]]
- 00a03900 ["CALLIND", null, ["register:0:8"]]
+ 00a03954 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03954 ["INT_ADD", "register:40f0:8", ["const:a03954:8", "const:4:8"]]
+ 00a03954 ["CALLIND", null, ["register:0:8"]]
- 00a03900 bytes 00013fd6
+ 00a03954 bytes 00013fd6
- 00a03924 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03924 ["INT_ADD", "register:40f0:8", ["const:a03924:8", "const:4:8"]]
- 00a03924 ["CALLIND", null, ["register:0:8"]]
+ 00a03978 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03978 ["INT_ADD", "register:40f0:8", ["const:a03978:8", "const:4:8"]]
+ 00a03978 ["CALLIND", null, ["register:0:8"]]
- 00a03924 bytes 00013fd6
+ 00a03978 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af60555bac5929ca363dcc90a93861d1"></a>

### [`00a039c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a039c4.md) → [`00a03a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03a18.md) FUN_00a03a18

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`008b9204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9204.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`008b925c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b925c.md)

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
      "site": "00a03a54",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a03a00",
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
      "00a03a54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00a03a54",
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

- 旧版 [`00a03a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a039c4.md#insn-00a03a00) · [`00a03a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a039c4.md#insn-00a03a0c) · [`00a03a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a039c4.md#insn-00a03a68)
- 新版 `00a03a54`（命令位置の公開資料なし） · `00a03a60`（命令位置の公開資料なし） · `00a03abc`（命令位置の公開資料なし）

~~~diff
- 00a03a00 ["INT_ADD", "register:40f0:8", ["const:a03a00:8", "const:4:8"]]
- 00a03a00 ["CALL", null, ["ram:47acf4:8"]]
+ 00a03a54 ["INT_ADD", "register:40f0:8", ["const:a03a54:8", "const:4:8"]]
+ 00a03a54 ["CALL", null, ["ram:47ad34:8"]]
- 00a03a00 bytes bddce997
+ 00a03a54 bytes b8dce997
- 00a03a0c ["INT_ADD", "register:40f0:8", ["const:a03a0c:8", "const:4:8"]]
- 00a03a0c ["CALL", null, ["callee:0047ce14:8"]]
+ 00a03a60 ["INT_ADD", "register:40f0:8", ["const:a03a60:8", "const:4:8"]]
+ 00a03a60 ["CALL", null, ["callee:0047ce14:8"]]
- 00a03a0c bytes f2e4e997
+ 00a03a60 bytes ede4e997
- 00a03a68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03a68 ["INT_ADD", "register:40f0:8", ["const:a03a68:8", "const:4:8"]]
- 00a03a68 ["CALLIND", null, ["register:0:8"]]
+ 00a03abc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03abc ["INT_ADD", "register:40f0:8", ["const:a03abc:8", "const:4:8"]]
+ 00a03abc ["CALLIND", null, ["register:0:8"]]
- 00a03a68 bytes 00013fd6
+ 00a03abc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d058f62526af377514ef95287670d75"></a>

### [`00a03b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b18.md) → [`00a03b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03b6c.md) FUN_00a03b6c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00a03b84",
      "incomplete_value": false,
      "site": "00a03b90",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03b30",
      "incomplete_value": false,
      "site": "00a03b3c",
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
            "const:e90:8"
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
      "00a03b90",
      "DATA",
      [
        "storage",
        "00c8ae90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a03b90",
      "DATA",
      [
        "storage",
        "00c8af60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a03b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b18.md#insn-00a03b30) · [`00a03b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b18.md#insn-00a03b60)
- 新版 `00a03b84`（命令位置の公開資料なし） · `00a03bb4`（命令位置の公開資料なし）

~~~diff
- 00a03b30 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00a03b30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a03b30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a03b30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a03b84 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00a03b84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03b84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03b84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a03b30 bytes 08413a91
+ 00a03b84 bytes 08813d91
- 00a03b60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03b60 ["INT_ADD", "register:40f0:8", ["const:a03b60:8", "const:4:8"]]
- 00a03b60 ["CALLIND", null, ["register:0:8"]]
+ 00a03bb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03bb4 ["INT_ADD", "register:40f0:8", ["const:a03bb4:8", "const:4:8"]]
+ 00a03bb4 ["CALLIND", null, ["register:0:8"]]
- 00a03b60 bytes 00013fd6
+ 00a03bb4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c08332ec4c14d9edb06b2838ab43c0c6"></a>

### [`00a03b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b74.md) → [`00a03bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03bc8.md) FUN_00a03bc8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00a03bf4",
      "incomplete_value": false,
      "site": "00a03bf4",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03ba0",
      "incomplete_value": false,
      "site": "00a03ba0",
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
            "const:e90:8"
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
      "00a03bf4",
      "DATA",
      [
        "storage",
        "00c8ae90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a03bf4",
      "DATA",
      [
        "storage",
        "00c8af60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a03b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b74.md#insn-00a03b88) · [`00a03b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b74.md#insn-00a03b98) · [`00a03bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b74.md#insn-00a03bbc)
- 新版 `00a03bdc`（命令位置の公開資料なし） · `00a03bec`（命令位置の公開資料なし） · `00a03c10`（命令位置の公開資料なし）

~~~diff
- 00a03b88 ["INT_ADD", "register:40f0:8", ["const:a03b88:8", "const:4:8"]]
- 00a03b88 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a03bdc ["INT_ADD", "register:40f0:8", ["const:a03bdc:8", "const:4:8"]]
+ 00a03bdc ["CALL", null, ["callee:00c57f60:8"]]
- 00a03b88 bytes c2500994
+ 00a03bdc bytes e1500994
- 00a03b98 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00a03b98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a03b98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a03b98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a03bec ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00a03bec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03bec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03bec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a03b98 bytes 08413a91
+ 00a03bec bytes 08813d91
- 00a03bbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03bbc ["INT_ADD", "register:40f0:8", ["const:a03bbc:8", "const:4:8"]]
- 00a03bbc ["CALLIND", null, ["register:0:8"]]
+ 00a03c10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03c10 ["INT_ADD", "register:40f0:8", ["const:a03c10:8", "const:4:8"]]
+ 00a03c10 ["CALLIND", null, ["register:0:8"]]
- 00a03bbc bytes 00013fd6
+ 00a03c10 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d763bb5f39f56302b1cac985bae4fe9"></a>

### [`00a03c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03c04.md) → [`00a03c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03c58.md) FUN_00a03c58

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00a03c78",
      "incomplete_value": false,
      "site": "00a03c78",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03c24",
      "incomplete_value": false,
      "site": "00a03c24",
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
            "const:e90:8"
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
      "00a03c78",
      "DATA",
      [
        "storage",
        "00c8ae90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a03c78",
      "DATA",
      [
        "storage",
        "00c8af60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a03c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03c04.md#insn-00a03c20) · [`00a03c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03c04.md#insn-00a03c40) · [`00a03c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03c04.md#insn-00a03c64)
- 新版 `00a03c74`（命令位置の公開資料なし） · `00a03c94`（命令位置の公開資料なし） · `00a03cb8`（命令位置の公開資料なし）

~~~diff
- 00a03c20 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00a03c20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a03c20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a03c20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a03c74 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00a03c74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03c74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03c74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a03c20 bytes 08413a91
+ 00a03c74 bytes 08813d91
- 00a03c40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03c40 ["INT_ADD", "register:40f0:8", ["const:a03c40:8", "const:4:8"]]
- 00a03c40 ["CALLIND", null, ["register:0:8"]]
+ 00a03c94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03c94 ["INT_ADD", "register:40f0:8", ["const:a03c94:8", "const:4:8"]]
+ 00a03c94 ["CALLIND", null, ["register:0:8"]]
- 00a03c40 bytes 00013fd6
+ 00a03c94 bytes 00013fd6
- 00a03c64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03c64 ["INT_ADD", "register:40f0:8", ["const:a03c64:8", "const:4:8"]]
- 00a03c64 ["CALLIND", null, ["register:0:8"]]
+ 00a03cb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03cb8 ["INT_ADD", "register:40f0:8", ["const:a03cb8:8", "const:4:8"]]
+ 00a03cb8 ["CALLIND", null, ["register:0:8"]]
- 00a03c64 bytes 00013fd6
+ 00a03cb8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dff4d7cb640c861fba34c1ceaf24396b"></a>

### [`00a03d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03d04.md) → [`00a03d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03d58.md) FUN_00a03d58

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`008b9204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9204.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`008b925c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b925c.md)

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
      "site": "00a03d94",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a03d40",
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
      "00a03d94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00a03d94",
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

- 旧版 [`00a03d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03d04.md#insn-00a03d40) · [`00a03d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03d04.md#insn-00a03d4c) · [`00a03da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03d04.md#insn-00a03da8)
- 新版 `00a03d94`（命令位置の公開資料なし） · `00a03da0`（命令位置の公開資料なし） · `00a03dfc`（命令位置の公開資料なし）

~~~diff
- 00a03d40 ["INT_ADD", "register:40f0:8", ["const:a03d40:8", "const:4:8"]]
- 00a03d40 ["CALL", null, ["ram:47acf4:8"]]
+ 00a03d94 ["INT_ADD", "register:40f0:8", ["const:a03d94:8", "const:4:8"]]
+ 00a03d94 ["CALL", null, ["ram:47ad34:8"]]
- 00a03d40 bytes eddbe997
+ 00a03d94 bytes e8dbe997
- 00a03d4c ["INT_ADD", "register:40f0:8", ["const:a03d4c:8", "const:4:8"]]
- 00a03d4c ["CALL", null, ["callee:0047ce14:8"]]
+ 00a03da0 ["INT_ADD", "register:40f0:8", ["const:a03da0:8", "const:4:8"]]
+ 00a03da0 ["CALL", null, ["callee:0047ce14:8"]]
- 00a03d4c bytes 22e4e997
+ 00a03da0 bytes 1de4e997
- 00a03da8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03da8 ["INT_ADD", "register:40f0:8", ["const:a03da8:8", "const:4:8"]]
- 00a03da8 ["CALLIND", null, ["register:0:8"]]
+ 00a03dfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03dfc ["INT_ADD", "register:40f0:8", ["const:a03dfc:8", "const:4:8"]]
+ 00a03dfc ["CALLIND", null, ["register:0:8"]]
- 00a03da8 bytes 00013fd6
+ 00a03dfc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-482ddc0f041e0d3e9aa3494b94fd6b09"></a>

### [`00a03e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e18.md) → [`00a03e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03e6c.md) FUN_00a03e6c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a03e90",
      "incomplete_value": false,
      "site": "00a03e90",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03e3c",
      "incomplete_value": false,
      "site": "00a03e3c",
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
      "00a03e90",
      "DATA",
      [
        "storage",
        "00c8af20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a03e90",
      "DATA",
      [
        "storage",
        "00c8aff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a03e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e18.md#insn-00a03e2c) · [`00a03e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e18.md#insn-00a03e38)
- 新版 `00a03e80`（命令位置の公開資料なし） · `00a03e8c`（命令位置の公開資料なし）

~~~diff
- 00a03e2c ["INT_ADD", "register:40f0:8", ["const:a03e2c:8", "const:4:8"]]
- 00a03e2c ["CALL", null, ["callee:00c57f60:8"]]
+ 00a03e80 ["INT_ADD", "register:40f0:8", ["const:a03e80:8", "const:4:8"]]
+ 00a03e80 ["CALL", null, ["callee:00c57f60:8"]]
- 00a03e2c bytes 19500994
+ 00a03e80 bytes 38500994
- 00a03e38 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00a03e38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a03e38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a03e38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a03e8c ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00a03e8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03e8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03e8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a03e38 bytes 08813c91
+ 00a03e8c bytes 08c13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8737dbf52fe1e7d1bc22bce5125dabc9"></a>

### [`00a03e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e4c.md) → [`00a03ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03ea0.md) FUN_00a03ea0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a03eac",
      "incomplete_value": false,
      "site": "00a03eac",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03e58",
      "incomplete_value": false,
      "site": "00a03e58",
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
            "const:f20:8"
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
      "00a03eac",
      "DATA",
      [
        "storage",
        "00c8af20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a03eac",
      "DATA",
      [
        "storage",
        "00c8aff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a03e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e4c.md#insn-00a03e54)
- 新版 `00a03ea8`（命令位置の公開資料なし）

~~~diff
- 00a03e54 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00a03e54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a03e54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a03e54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a03ea8 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00a03ea8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a03ea8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a03ea8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a03e54 bytes 29813c91
+ 00a03ea8 bytes 29c13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d519cb24b6796e460baa86acc594e53"></a>

### [`00a03e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e68.md) → [`00a03ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03ebc.md) FUN_00a03ebc

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 0件  · 呼出先 25件 [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a03f18",
      "incomplete_value": true,
      "site": "00a03f18",
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
      "definition_site": "00a03ec4",
      "incomplete_value": true,
      "site": "00a03ec4",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a03f20",
      "incomplete_value": false,
      "site": "00a03f30",
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
      "definition_site": "00a03ecc",
      "incomplete_value": false,
      "site": "00a03edc",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a03f28",
      "incomplete_value": false,
      "site": "00a03f30",
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
      "definition_site": "00a03ed4",
      "incomplete_value": false,
      "site": "00a03edc",
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
      "00a03f14",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00a03f20",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a03f28",
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
      "00a03f14",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a03f20",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a03f28",
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

- 旧版 [`00a03edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e68.md#insn-00a03edc) · [`00a03f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e68.md#insn-00a03f30) · [`00a042b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e68.md#insn-00a042b8)
- 新版 `00a03f30`（命令位置の公開資料なし） · `00a03f84`（命令位置の公開資料なし） · `00a0430c`（命令位置の公開資料なし）

~~~diff
- 00a03edc ["INT_ADD", "register:40f0:8", ["const:a03edc:8", "const:4:8"]]
- 00a03edc ["CALL", null, ["callee:00c586e0:8"]]
+ 00a03f30 ["INT_ADD", "register:40f0:8", ["const:a03f30:8", "const:4:8"]]
+ 00a03f30 ["CALL", null, ["callee:00c586e0:8"]]
- 00a03edc bytes cd510994
+ 00a03f30 bytes ec510994
- 00a03f30 ["INT_ADD", "register:40f0:8", ["const:a03f30:8", "const:4:8"]]
- 00a03f30 ["CALL", null, ["callee:008b9344:8"]]
+ 00a03f84 ["INT_ADD", "register:40f0:8", ["const:a03f84:8", "const:4:8"]]
+ 00a03f84 ["CALL", null, ["callee:008b9344:8"]]
- 00a03f30 bytes efd4fa97
+ 00a03f84 bytes f0d4fa97
- 00a042b8 ["INT_ADD", "register:40f0:8", ["const:a042b8:8", "const:4:8"]]
- 00a042b8 ["CALL", null, ["ram:9f7990:8"]]
+ 00a0430c ["INT_ADD", "register:40f0:8", ["const:a0430c:8", "const:4:8"]]
+ 00a0430c ["CALL", null, ["ram:9f79e4:8"]]
- 00a042b8 bytes b6cdff97
+ 00a0430c bytes b6cdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fabb1d2b9f5eb47a1afa6af4aef62a7"></a>

### [`00a04558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04558.md) → [`00a045ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a045ac.md) FUN_00a045ac

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a045d0",
      "incomplete_value": false,
      "site": "00a045d0",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0457c",
      "incomplete_value": false,
      "site": "00a0457c",
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
            "const:fa0:8"
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
      "00a045d0",
      "DATA",
      [
        "storage",
        "00c8afa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a045d0",
      "DATA",
      [
        "storage",
        "00c8b070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0456c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04558.md#insn-00a0456c) · [`00a04574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04558.md#insn-00a04574) · [`00a04578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04558.md#insn-00a04578)
- 新版 `00a045c0`（命令位置の公開資料なし） · `00a045c8`（命令位置の公開資料なし） · `00a045cc`（命令位置の公開資料なし）

~~~diff
- 00a0456c ["INT_ADD", "register:40f0:8", ["const:a0456c:8", "const:4:8"]]
- 00a0456c ["CALL", null, ["callee:00c57f60:8"]]
+ 00a045c0 ["INT_ADD", "register:40f0:8", ["const:a045c0:8", "const:4:8"]]
+ 00a045c0 ["CALL", null, ["callee:00c57f60:8"]]
- 00a0456c bytes 494e0994
+ 00a045c0 bytes 684e0994
- 00a04574 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 00a045c8 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a04574 bytes 281400d0
+ 00a045c8 bytes 281400f0
- 00a04578 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 00a04578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a04578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a04578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a045cc ["COPY", "tmp:0:8", ["const:70:8"]]
+ 00a045cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a045cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a045cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a04578 bytes 08813e91
+ 00a045cc bytes 08c10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06bb541baccd0a63bcc898c687838dea"></a>

### [`00a0458c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a0458c.md) → [`00a045e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a045e0.md) FUN_00a045e0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a045ec",
      "incomplete_value": false,
      "site": "00a045ec",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04598",
      "incomplete_value": false,
      "site": "00a04598",
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
            "const:fa0:8"
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
      "00a045ec",
      "DATA",
      [
        "storage",
        "00c8afa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a045ec",
      "DATA",
      [
        "storage",
        "00c8b070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a04590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a0458c.md#insn-00a04590) · [`00a04594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a0458c.md#insn-00a04594)
- 新版 `00a045e4`（命令位置の公開資料なし） · `00a045e8`（命令位置の公開資料なし）

~~~diff
- 00a04590 ["COPY", "register:4048:8", ["const:c8a000:8"]]
+ 00a045e4 ["COPY", "register:4048:8", ["const:c8b000:8"]]
- 00a04590 bytes 291400d0
+ 00a045e4 bytes 291400f0
- 00a04594 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 00a04594 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a04594 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a04594 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a045e8 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 00a045e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a045e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a045e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a04594 bytes 29813e91
+ 00a045e8 bytes 29c10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a85dbdb55e0acee01f8640e044278b3"></a>

### [`00a045a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a045a8.md) → [`00a045fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a045fc.md) FUN_00a045fc

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md)
- 新版 呼出元 0件  · 呼出先 24件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`004939d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.97% / 新版 97.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a04770",
      "incomplete_value": false,
      "site": "00a0477c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:76d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0471c",
      "incomplete_value": false,
      "site": "00a04728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:7ba:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a047a8",
      "incomplete_value": false,
      "site": "00a047b4",
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
            "const:67d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04754",
      "incomplete_value": false,
      "site": "00a04760",
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
            "const:63d:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a047d4",
      "incomplete_value": false,
      "site": "00a047dc",
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
            "const:17f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04780",
      "incomplete_value": false,
      "site": "00a04788",
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
            "const:1d3:8"
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
      "00a04658",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[59]"
      ]
    ],
    [
      "00a04668",
      "DATA",
      [
        "storage",
        "00436bc8",
        null,
        "byte[59]"
      ]
    ],
    [
      "00a04674",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[59]"
      ]
    ]
  ],
  "added": [
    [
      "00a04658",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[47]"
      ]
    ],
    [
      "00a04668",
      "DATA",
      [
        "storage",
        "00436bc8",
        null,
        "byte[47]"
      ]
    ],
    [
      "00a04674",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[47]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a046d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a045a8.md#insn-00a046d4) · [`00a04728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a045a8.md#insn-00a04728) · [`00a04760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a045a8.md#insn-00a04760)
- 新版 `00a04728`（命令位置の公開資料なし） · `00a0477c`（命令位置の公開資料なし） · `00a047b4`（命令位置の公開資料なし）

~~~diff
- 00a046d4 ["INT_ADD", "register:40f0:8", ["const:a046d4:8", "const:4:8"]]
- 00a046d4 ["CALL", null, ["callee:00851550:8"]]
+ 00a04728 ["INT_ADD", "register:40f0:8", ["const:a04728:8", "const:4:8"]]
+ 00a04728 ["CALL", null, ["callee:00851550:8"]]
- 00a046d4 bytes 8933f997
+ 00a04728 bytes 8a33f997
- 00a04728 ["INT_ADD", "register:40f0:8", ["const:a04728:8", "const:4:8"]]
- 00a04728 ["CALL", null, ["callee:00c58030:8"]]
+ 00a0477c ["INT_ADD", "register:40f0:8", ["const:a0477c:8", "const:4:8"]]
+ 00a0477c ["CALL", null, ["callee:00c58030:8"]]
- 00a04728 bytes 0e4e0994
+ 00a0477c bytes 2d4e0994
- 00a04760 ["INT_ADD", "register:40f0:8", ["const:a04760:8", "const:4:8"]]
- 00a04760 ["CALL", null, ["callee:00c58030:8"]]
+ 00a047b4 ["INT_ADD", "register:40f0:8", ["const:a047b4:8", "const:4:8"]]
+ 00a047b4 ["CALL", null, ["callee:00c58030:8"]]
- 00a04760 bytes 004e0994
+ 00a047b4 bytes 1f4e0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79fe215170845ae6c55740ebe3892522"></a>

### [`00a04dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04dc4.md) → [`00a04e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04e18.md) FUN_00a04e18

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a04e3c",
      "incomplete_value": false,
      "site": "00a04e40",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04de8",
      "incomplete_value": false,
      "site": "00a04dec",
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
            "const:20:8"
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
      "00a04e40",
      "DATA",
      [
        "storage",
        "00c8b020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a04e40",
      "DATA",
      [
        "storage",
        "00c8b0f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a04dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04dc4.md#insn-00a04dd8) · [`00a04de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04dc4.md#insn-00a04de8)
- 新版 `00a04e2c`（命令位置の公開資料なし） · `00a04e3c`（命令位置の公開資料なし）

~~~diff
- 00a04dd8 ["INT_ADD", "register:40f0:8", ["const:a04dd8:8", "const:4:8"]]
- 00a04dd8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a04e2c ["INT_ADD", "register:40f0:8", ["const:a04e2c:8", "const:4:8"]]
+ 00a04e2c ["CALL", null, ["callee:00c57f60:8"]]
- 00a04dd8 bytes 2e4c0994
+ 00a04e2c bytes 4d4c0994
- 00a04de8 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00a04de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a04de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a04de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a04e3c ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 00a04e3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04e3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04e3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a04de8 bytes 08810091
+ 00a04e3c bytes 08c10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae9eb062ef595848a6367f32c86d4b4d"></a>

### [`00a04e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04e04.md) → [`00a04e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04e58.md) FUN_00a04e58

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a04e5c",
      "incomplete_value": false,
      "site": "00a04e60",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04e08",
      "incomplete_value": false,
      "site": "00a04e0c",
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
      "00a04e60",
      "DATA",
      [
        "storage",
        "00c8b020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a04e60",
      "DATA",
      [
        "storage",
        "00c8b0f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a04e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04e04.md#insn-00a04e08)
- 新版 `00a04e5c`（命令位置の公開資料なし）

~~~diff
- 00a04e08 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00a04e08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a04e08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a04e08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a04e5c ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 00a04e5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04e5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04e5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a04e08 bytes 08810091
+ 00a04e5c bytes 08c10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0e3ff11a63a25f52226608256253955"></a>

### [`00a04e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04e94.md) → [`00a04ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04ee8.md) FUN_00a04ee8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009fb44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`009fb4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fb/009fb4a0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00a04ef4",
      "incomplete_value": false,
      "site": "00a04ef8",
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
      "definition_site": "00a04ea0",
      "incomplete_value": false,
      "site": "00a04ea4",
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
      "00a04ef4",
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
      "00a04ef4",
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

- 旧版 [`00a04ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04e94.md#insn-00a04ea4) · [`00a04ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04e94.md#insn-00a04ea0)
- 新版 `00a04ef8`（命令位置の公開資料なし） · `00a04ef4`（命令位置の公開資料なし）

~~~diff
- 00a04ea4 ["INT_ADD", "register:40f0:8", ["const:a04ea4:8", "const:4:8"]]
- 00a04ea4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00a04ef8 ["INT_ADD", "register:40f0:8", ["const:a04ef8:8", "const:4:8"]]
+ 00a04ef8 ["CALL", null, ["callee:0043b7b8:8"]]
- 00a04ea4 bytes 35dae897
+ 00a04ef8 bytes 30dae897
- 00a04ea0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00a04ea0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a04ea0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a04ea0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a04ef4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00a04ef4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a04ef4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a04ef4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a04ea0 bytes 00303d91
+ 00a04ef4 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-512ec368d9f488823ecfd8e76d171d01"></a>

### [`00a04eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04eac.md) → [`00a04f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04f00.md) FUN_00a04f00

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a04f24",
      "incomplete_value": false,
      "site": "00a04f28",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04ed0",
      "incomplete_value": false,
      "site": "00a04ed4",
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
            "const:a0:8"
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
      "00a04f28",
      "DATA",
      [
        "storage",
        "00c8b0a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a04f28",
      "DATA",
      [
        "storage",
        "00c8b170",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a04ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04eac.md#insn-00a04ec0) · [`00a04ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04eac.md#insn-00a04ed0)
- 新版 `00a04f14`（命令位置の公開資料なし） · `00a04f24`（命令位置の公開資料なし）

~~~diff
- 00a04ec0 ["INT_ADD", "register:40f0:8", ["const:a04ec0:8", "const:4:8"]]
- 00a04ec0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a04f14 ["INT_ADD", "register:40f0:8", ["const:a04f14:8", "const:4:8"]]
+ 00a04f14 ["CALL", null, ["callee:00c57f60:8"]]
- 00a04ec0 bytes f44b0994
+ 00a04f14 bytes 134c0994
- 00a04ed0 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 00a04ed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a04ed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a04ed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a04f24 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 00a04f24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04f24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04f24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a04ed0 bytes 08810291
+ 00a04f24 bytes 08c10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58c6aa6bde6c1b5fa7003ab41210cdfd"></a>

### [`00a04eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04eec.md) → [`00a04f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04f40.md) FUN_00a04f40

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a04f44",
      "incomplete_value": false,
      "site": "00a04f48",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04ef0",
      "incomplete_value": false,
      "site": "00a04ef4",
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
            "const:a0:8"
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
      "00a04f48",
      "DATA",
      [
        "storage",
        "00c8b0a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a04f48",
      "DATA",
      [
        "storage",
        "00c8b170",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a04ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04eec.md#insn-00a04ef0)
- 新版 `00a04f44`（命令位置の公開資料なし）

~~~diff
- 00a04ef0 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 00a04ef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a04ef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a04ef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a04f44 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 00a04f44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04f44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04f44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a04ef0 bytes 08810291
+ 00a04f44 bytes 08c10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee0100ca14777665f63d4763777ac489"></a>

### [`00a04f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04f14.md) → [`00a04f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04f68.md) FUN_00a04f68

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b97a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b97a0.md) [`009df634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df634.md) [`009df8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8c4.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b97f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b97f8.md) [`009df688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df688.md) [`009df918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df918.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a05130",
      "incomplete_value": true,
      "site": "00a05140",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:689:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a050dc",
      "incomplete_value": true,
      "site": "00a050ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:658:8"
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
      "definition_site": "00a05134",
      "incomplete_value": true,
      "site": "00a05144",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00a050e0",
      "incomplete_value": true,
      "site": "00a050f0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a05138",
      "incomplete_value": true,
      "site": "00a05148",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a050e4",
      "incomplete_value": true,
      "site": "00a050f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:290:8"
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
      "00a05130",
      "READ",
      [
        "storage",
        "002b5658",
        null,
        "string"
      ]
    ],
    [
      "00a05134",
      "READ",
      [
        "storage",
        "002b5664",
        null,
        "string"
      ]
    ],
    [
      "00a05138",
      "READ",
      [
        "storage",
        "002c3290",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a05130",
      "READ",
      [
        "storage",
        "002b5689",
        null,
        "string"
      ]
    ],
    [
      "00a05134",
      "READ",
      [
        "storage",
        "002b5695",
        null,
        "string"
      ]
    ],
    [
      "00a05138",
      "READ",
      [
        "storage",
        "002c32d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04f14.md#insn-00a05140) · [`00a04f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04f14.md#insn-00a04f48) · [`00a04f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04f14.md#insn-00a04f5c)
- 新版 `00a05194`（命令位置の公開資料なし） · `00a04f9c`（命令位置の公開資料なし） · `00a04fb0`（命令位置の公開資料なし）

~~~diff
- 00a05140 ["INT_ADD", "register:40f0:8", ["const:a05140:8", "const:4:8"]]
- 00a05140 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a05194 ["INT_ADD", "register:40f0:8", ["const:a05194:8", "const:4:8"]]
+ 00a05194 ["CALL", null, ["callee:00c57f80:8"]]
- 00a05140 bytes 5c4b0994
+ 00a05194 bytes 7b4b0994
- 00a04f48 ["INT_ADD", "register:40f0:8", ["const:a04f48:8", "const:4:8"]]
- 00a04f48 ["CALL", null, ["callee:008b97f8:8"]]
+ 00a04f9c ["INT_ADD", "register:40f0:8", ["const:a04f9c:8", "const:4:8"]]
+ 00a04f9c ["CALL", null, ["callee:008b97f8:8"]]
- 00a04f48 bytes 16d2fa97
+ 00a04f9c bytes 17d2fa97
- 00a04f5c ["INT_ADD", "register:40f0:8", ["const:a04f5c:8", "const:4:8"]]
- 00a04f5c ["CALL", null, ["callee:00851550:8"]]
+ 00a04fb0 ["INT_ADD", "register:40f0:8", ["const:a04fb0:8", "const:4:8"]]
+ 00a04fb0 ["CALL", null, ["callee:00851550:8"]]
- 00a04f5c bytes 6731f997
+ 00a04fb0 bytes 6831f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f565dbdb2e4a69352a9bfd8be9b7b6e1"></a>

### [`00a05254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05254.md) → [`00a052a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a052a8.md) FUN_00a052a8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a052cc",
      "incomplete_value": false,
      "site": "00a052cc",
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
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05278",
      "incomplete_value": false,
      "site": "00a05278",
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
            "const:120:8"
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
      "00a052cc",
      "DATA",
      [
        "storage",
        "00c8b120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a052cc",
      "DATA",
      [
        "storage",
        "00c8b1f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05254.md#insn-00a05268) · [`00a05274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05254.md#insn-00a05274)
- 新版 `00a052bc`（命令位置の公開資料なし） · `00a052c8`（命令位置の公開資料なし）

~~~diff
- 00a05268 ["INT_ADD", "register:40f0:8", ["const:a05268:8", "const:4:8"]]
- 00a05268 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a052bc ["INT_ADD", "register:40f0:8", ["const:a052bc:8", "const:4:8"]]
+ 00a052bc ["CALL", null, ["callee:00c57f60:8"]]
- 00a05268 bytes 0a4b0994
+ 00a052bc bytes 294b0994
- 00a05274 ["COPY", "tmp:0:8", ["const:120:8"]]
- 00a05274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a05274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a05274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a052c8 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00a052c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a052c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a052c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a05274 bytes 08810491
+ 00a052c8 bytes 08c10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-546c0246534f20addd3a2cb3c78b5308"></a>

### [`00a05288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05288.md) → [`00a052dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a052dc.md) FUN_00a052dc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00a052e8",
      "incomplete_value": true,
      "site": "00a052e8",
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
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05294",
      "incomplete_value": true,
      "site": "00a05294",
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
            "const:120:8"
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
      "00a052e8",
      "DATA",
      [
        "storage",
        "00c8b120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a052e8",
      "DATA",
      [
        "storage",
        "00c8b1f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05288.md#insn-00a05290)
- 新版 `00a052e4`（命令位置の公開資料なし）

~~~diff
- 00a05290 ["COPY", "tmp:0:8", ["const:120:8"]]
- 00a05290 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a05290 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a05290 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a052e4 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00a052e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a052e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a052e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a05290 bytes 29810491
+ 00a052e4 bytes 29c10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a97f3de09fba4628df25ab5322779fd"></a>

### [`00a052a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a052a4.md) → [`00a052f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a052f8.md) FUN_00a052f8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`009f7de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7de0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`009f7e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f7e34.md)

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
      "site": "00a05318",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a052c4",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "00a05324",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a052d0",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00a05318",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a05324",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00a05318",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00a05324",
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

- 旧版 [`00a052c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a052a4.md#insn-00a052c4) · [`00a052d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a052a4.md#insn-00a052d0)
- 新版 `00a05318`（命令位置の公開資料なし） · `00a05324`（命令位置の公開資料なし）

~~~diff
- 00a052c4 ["INT_ADD", "register:40f0:8", ["const:a052c4:8", "const:4:8"]]
- 00a052c4 ["CALL", null, ["ram:47acf4:8"]]
+ 00a05318 ["INT_ADD", "register:40f0:8", ["const:a05318:8", "const:4:8"]]
+ 00a05318 ["CALL", null, ["ram:47ad34:8"]]
- 00a052c4 bytes 8cd6e997
+ 00a05318 bytes 87d6e997
- 00a052d0 ["INT_ADD", "register:40f0:8", ["const:a052d0:8", "const:4:8"]]
- 00a052d0 ["CALL", null, ["ram:47acf4:8"]]
+ 00a05324 ["INT_ADD", "register:40f0:8", ["const:a05324:8", "const:4:8"]]
+ 00a05324 ["CALL", null, ["ram:47ad34:8"]]
- 00a052d0 bytes 89d6e997
+ 00a05324 bytes 84d6e997
~~~


<a id="compare-4371e50fa788ff6bd41a0809b448910e"></a>

### [`00a05324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05324.md) → [`00a05378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05378.md) FUN_00a05378

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a05398",
      "incomplete_value": false,
      "site": "00a0539c",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05344",
      "incomplete_value": false,
      "site": "00a05348",
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
            "const:1a0:8"
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
      "00a0539c",
      "DATA",
      [
        "storage",
        "00c8b1a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a0539c",
      "DATA",
      [
        "storage",
        "00c8b270",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05324.md#insn-00a05338) · [`00a05344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05324.md#insn-00a05344)
- 新版 `00a0538c`（命令位置の公開資料なし） · `00a05398`（命令位置の公開資料なし）

~~~diff
- 00a05338 ["INT_ADD", "register:40f0:8", ["const:a05338:8", "const:4:8"]]
- 00a05338 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a0538c ["INT_ADD", "register:40f0:8", ["const:a0538c:8", "const:4:8"]]
+ 00a0538c ["CALL", null, ["callee:00c57f60:8"]]
- 00a05338 bytes d64a0994
+ 00a0538c bytes f54a0994
- 00a05344 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 00a05344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a05344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a05344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a05398 ["COPY", "tmp:0:8", ["const:270:8"]]
+ 00a05398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a05344 bytes 08810691
+ 00a05398 bytes 08c10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b2ecad0169208c9f4baeee595e8095d"></a>

### [`00a0535c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0535c.md) → [`00a053b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a053b0.md) FUN_00a053b0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a053b4",
      "incomplete_value": false,
      "site": "00a053b8",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05360",
      "incomplete_value": false,
      "site": "00a05364",
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
      "00a053b8",
      "DATA",
      [
        "storage",
        "00c8b1a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a053b8",
      "DATA",
      [
        "storage",
        "00c8b270",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0535c.md#insn-00a05360)
- 新版 `00a053b4`（命令位置の公開資料なし）

~~~diff
- 00a05360 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 00a05360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a05360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a05360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a053b4 ["COPY", "tmp:0:8", ["const:270:8"]]
+ 00a053b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a053b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a053b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a05360 bytes 08810691
+ 00a053b4 bytes 08c10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13125005b06990f64ac008c342558b28"></a>

### [`00a0537c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0537c.md) → [`00a053d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a053d0.md) FUN_00a053d0

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.62% / 新版 89.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a05480",
      "incomplete_value": true,
      "site": "00a05490",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7fe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0542c",
      "incomplete_value": true,
      "site": "00a0543c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:852:8"
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
      "definition_site": "00a05494",
      "incomplete_value": true,
      "site": "00a05494",
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
      "definition_site": "00a05440",
      "incomplete_value": true,
      "site": "00a05440",
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
      "definition_site": "00a05488",
      "incomplete_value": true,
      "site": "00a05498",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00a05434",
      "incomplete_value": true,
      "site": "00a05444",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:450:8"
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
      "00a0540c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a05428",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a05480",
      "READ",
      [
        "storage",
        "002b8852",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a0540c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00a05428",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00a05480",
      "READ",
      [
        "storage",
        "002b87fe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a053b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0537c.md#insn-00a053b8) · [`00a053d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0537c.md#insn-00a053d4) · [`00a05428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0537c.md#insn-00a05428)
- 新版 `00a0540c`（命令位置の公開資料なし） · `00a05428`（命令位置の公開資料なし）

~~~diff
- 00a053b8 ["INT_ADD", "register:40f0:8", ["const:a053b8:8", "const:4:8"]]
- 00a053b8 ["CALL", null, ["ram:47acf4:8"]]
+ 00a0540c ["INT_ADD", "register:40f0:8", ["const:a0540c:8", "const:4:8"]]
+ 00a0540c ["CALL", null, ["ram:47ad34:8"]]
- 00a053b8 bytes 4fd6e997
+ 00a0540c bytes 4ad6e997
- 00a053d4 ["INT_ADD", "register:40f0:8", ["const:a053d4:8", "const:4:8"]]
- 00a053d4 ["CALL", null, ["ram:47acf4:8"]]
+ 00a05428 ["INT_ADD", "register:40f0:8", ["const:a05428:8", "const:4:8"]]
+ 00a05428 ["CALL", null, ["ram:47ad34:8"]]
- 00a053d4 bytes 48d6e997
+ 00a05428 bytes 43d6e997
- 00a05428 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 00a05428 bytes e9c5ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8938a478ecc73052c85f24d5229384ac"></a>

### [`00a05790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05790.md) → [`00a057e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a057e4.md) FUN_00a057e4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a05808",
      "incomplete_value": false,
      "site": "00a05808",
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
            "const:2e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a057b4",
      "incomplete_value": false,
      "site": "00a057b4",
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
      "00a05808",
      "DATA",
      [
        "storage",
        "00c8b210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a05808",
      "DATA",
      [
        "storage",
        "00c8b2e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a057a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05790.md#insn-00a057a4) · [`00a057b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05790.md#insn-00a057b0)
- 新版 `00a057f8`（命令位置の公開資料なし） · `00a05804`（命令位置の公開資料なし）

~~~diff
- 00a057a4 ["INT_ADD", "register:40f0:8", ["const:a057a4:8", "const:4:8"]]
- 00a057a4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a057f8 ["INT_ADD", "register:40f0:8", ["const:a057f8:8", "const:4:8"]]
+ 00a057f8 ["CALL", null, ["callee:00c57f60:8"]]
- 00a057a4 bytes bb490994
+ 00a057f8 bytes da490994
- 00a057b0 ["COPY", "tmp:0:8", ["const:210:8"]]
- 00a057b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a057b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a057b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a05804 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 00a05804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a057b0 bytes 08410891
+ 00a05804 bytes 08810b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-988de454bccd58e27aea499e81ba6c11"></a>

### [`00a057c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a057c4.md) → [`00a05818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05818.md) FUN_00a05818

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a05824",
      "incomplete_value": false,
      "site": "00a05824",
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
            "const:2e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a057d0",
      "incomplete_value": false,
      "site": "00a057d0",
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
      "00a05824",
      "DATA",
      [
        "storage",
        "00c8b210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a05824",
      "DATA",
      [
        "storage",
        "00c8b2e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a057cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a057c4.md#insn-00a057cc)
- 新版 `00a05820`（命令位置の公開資料なし）

~~~diff
- 00a057cc ["COPY", "tmp:0:8", ["const:210:8"]]
- 00a057cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a057cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a057cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a05820 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 00a05820 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a05820 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a05820 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a057cc bytes 29410891
+ 00a05820 bytes 29810b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ae4e1daf8b6551a4b0f015a6ea3cf99"></a>

### [`00a057e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a057e0.md) → [`00a05834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05834.md) FUN_00a05834

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`008b9204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9204.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`008b925c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b925c.md)

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
      "site": "00a0585c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a05808",
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
      "00a0585c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00a0585c",
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

- 旧版 [`00a05808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a057e0.md#insn-00a05808) · [`00a05814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a057e0.md#insn-00a05814)
- 新版 `00a0585c`（命令位置の公開資料なし） · `00a05868`（命令位置の公開資料なし）

~~~diff
- 00a05808 ["INT_ADD", "register:40f0:8", ["const:a05808:8", "const:4:8"]]
- 00a05808 ["CALL", null, ["ram:47acf4:8"]]
+ 00a0585c ["INT_ADD", "register:40f0:8", ["const:a0585c:8", "const:4:8"]]
+ 00a0585c ["CALL", null, ["ram:47ad34:8"]]
- 00a05808 bytes 3bd5e997
+ 00a0585c bytes 36d5e997
- 00a05814 ["INT_ADD", "register:40f0:8", ["const:a05814:8", "const:4:8"]]
- 00a05814 ["CALL", null, ["callee:0047ce14:8"]]
+ 00a05868 ["INT_ADD", "register:40f0:8", ["const:a05868:8", "const:4:8"]]
+ 00a05868 ["CALL", null, ["callee:0047ce14:8"]]
- 00a05814 bytes 70dde997
+ 00a05868 bytes 6bdde997
~~~


<a id="compare-70134ea442460a560040f3c94b8fce43"></a>

### [`00a0586c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0586c.md) → [`00a058c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a058c0.md) FUN_00a058c0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a058e4",
      "incomplete_value": false,
      "site": "00a058e4",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05890",
      "incomplete_value": false,
      "site": "00a05890",
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
            "const:2a0:8"
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
      "00a058e4",
      "DATA",
      [
        "storage",
        "00c8b2a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a058e4",
      "DATA",
      [
        "storage",
        "00c8b370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0586c.md#insn-00a05880) · [`00a0588c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0586c.md#insn-00a0588c)
- 新版 `00a058d4`（命令位置の公開資料なし） · `00a058e0`（命令位置の公開資料なし）

~~~diff
- 00a05880 ["INT_ADD", "register:40f0:8", ["const:a05880:8", "const:4:8"]]
- 00a05880 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a058d4 ["INT_ADD", "register:40f0:8", ["const:a058d4:8", "const:4:8"]]
+ 00a058d4 ["CALL", null, ["callee:00c57f60:8"]]
- 00a05880 bytes 84490994
+ 00a058d4 bytes a3490994
- 00a0588c ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 00a0588c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a0588c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a0588c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a058e0 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 00a058e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a058e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a058e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a0588c bytes 08810a91
+ 00a058e0 bytes 08c10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4799e86a177c9852a141749ac302cf55"></a>

### [`00a058a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a058a0.md) → [`00a058f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a058f4.md) FUN_00a058f4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a05900",
      "incomplete_value": false,
      "site": "00a05900",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a058ac",
      "incomplete_value": false,
      "site": "00a058ac",
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
            "const:2a0:8"
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
      "00a05900",
      "DATA",
      [
        "storage",
        "00c8b2a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a05900",
      "DATA",
      [
        "storage",
        "00c8b370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a058a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a058a0.md#insn-00a058a8)
- 新版 `00a058fc`（命令位置の公開資料なし）

~~~diff
- 00a058a8 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 00a058a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a058a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a058a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a058fc ["COPY", "tmp:0:8", ["const:370:8"]]
+ 00a058fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a058fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a058fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a058a8 bytes 29810a91
+ 00a058fc bytes 29c10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c05abfe121853db7946164899b0462e"></a>

### [`00a058bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a058bc.md) → [`00a05910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05910.md) FUN_00a05910

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`009fabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`009fac20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fa/009fac20.md)

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
      "site": "00a05930",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a058dc",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "00a0593c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a058e8",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00a05930",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a0593c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00a05930",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00a0593c",
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

- 旧版 [`00a058dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a058bc.md#insn-00a058dc) · [`00a058e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a058bc.md#insn-00a058e8)
- 新版 `00a05930`（命令位置の公開資料なし） · `00a0593c`（命令位置の公開資料なし）

~~~diff
- 00a058dc ["INT_ADD", "register:40f0:8", ["const:a058dc:8", "const:4:8"]]
- 00a058dc ["CALL", null, ["ram:47acf4:8"]]
+ 00a05930 ["INT_ADD", "register:40f0:8", ["const:a05930:8", "const:4:8"]]
+ 00a05930 ["CALL", null, ["ram:47ad34:8"]]
- 00a058dc bytes 06d5e997
+ 00a05930 bytes 01d5e997
- 00a058e8 ["INT_ADD", "register:40f0:8", ["const:a058e8:8", "const:4:8"]]
- 00a058e8 ["CALL", null, ["ram:47acf4:8"]]
+ 00a0593c ["INT_ADD", "register:40f0:8", ["const:a0593c:8", "const:4:8"]]
+ 00a0593c ["CALL", null, ["ram:47ad34:8"]]
- 00a058e8 bytes 03d5e997
+ 00a0593c bytes fed4e997
~~~


<a id="compare-d4c9a206429c5fec263ea9288d8a124e"></a>

### [`00a0593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0593c.md) → [`00a05990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05990.md) FUN_00a05990

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a059a4",
      "incomplete_value": false,
      "site": "00a059a8",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05950",
      "incomplete_value": false,
      "site": "00a05954",
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
            "const:320:8"
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
      "00a059a8",
      "DATA",
      [
        "storage",
        "00c8b320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a059a8",
      "DATA",
      [
        "storage",
        "00c8b3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0593c.md#insn-00a05948) · [`00a05950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0593c.md#insn-00a05950)
- 新版 `00a0599c`（命令位置の公開資料なし） · `00a059a4`（命令位置の公開資料なし）

~~~diff
- 00a05948 ["INT_ADD", "register:40f0:8", ["const:a05948:8", "const:4:8"]]
- 00a05948 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a0599c ["INT_ADD", "register:40f0:8", ["const:a0599c:8", "const:4:8"]]
+ 00a0599c ["CALL", null, ["callee:00c57f60:8"]]
- 00a05948 bytes 52490994
+ 00a0599c bytes 71490994
- 00a05950 ["COPY", "tmp:0:8", ["const:320:8"]]
- 00a05950 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a05950 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a05950 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a059a4 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00a059a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a059a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a059a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a05950 bytes 08810c91
+ 00a059a4 bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a425eeebf317665ce6195b6000d35ca"></a>

### [`00a05960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05960.md) → [`00a059b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a059b4.md) FUN_00a059b4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a059b8",
      "incomplete_value": false,
      "site": "00a059bc",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05964",
      "incomplete_value": false,
      "site": "00a05968",
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
      "00a059bc",
      "DATA",
      [
        "storage",
        "00c8b320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a059bc",
      "DATA",
      [
        "storage",
        "00c8b3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05960.md#insn-00a05964)
- 新版 `00a059b8`（命令位置の公開資料なし）

~~~diff
- 00a05964 ["COPY", "tmp:0:8", ["const:320:8"]]
- 00a05964 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a05964 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a05964 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a059b8 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00a059b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a059b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a059b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a05964 bytes 08810c91
+ 00a059b8 bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee0db81d441c170853bde46968c5be9f"></a>

### [`00a05978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05978.md) → [`00a059cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a059cc.md) FUN_00a059cc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a46bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46bb8.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`00a46c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c0c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "site": "00a059ec",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a05998",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "00a05a0c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a059b8",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00a059ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a05a0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00a059ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00a05a0c",
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

- 旧版 [`00a05998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05978.md#insn-00a05998) · [`00a059b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05978.md#insn-00a059b8) · [`00a059c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05978.md#insn-00a059c4)
- 新版 `00a059ec`（命令位置の公開資料なし） · `00a05a0c`（命令位置の公開資料なし） · `00a05a18`（命令位置の公開資料なし）

~~~diff
- 00a05998 ["INT_ADD", "register:40f0:8", ["const:a05998:8", "const:4:8"]]
- 00a05998 ["CALL", null, ["ram:47acf4:8"]]
+ 00a059ec ["INT_ADD", "register:40f0:8", ["const:a059ec:8", "const:4:8"]]
+ 00a059ec ["CALL", null, ["ram:47ad34:8"]]
- 00a05998 bytes d7d4e997
+ 00a059ec bytes d2d4e997
- 00a059b8 ["INT_ADD", "register:40f0:8", ["const:a059b8:8", "const:4:8"]]
- 00a059b8 ["CALL", null, ["ram:47acf4:8"]]
+ 00a05a0c ["INT_ADD", "register:40f0:8", ["const:a05a0c:8", "const:4:8"]]
+ 00a05a0c ["CALL", null, ["ram:47ad34:8"]]
- 00a059b8 bytes cfd4e997
+ 00a05a0c bytes cad4e997
- 00a059c4 ["INT_ADD", "register:40f0:8", ["const:a059c4:8", "const:4:8"]]
- 00a059c4 ["CALL", null, ["callee:0047ce14:8"]]
+ 00a05a18 ["INT_ADD", "register:40f0:8", ["const:a05a18:8", "const:4:8"]]
+ 00a05a18 ["CALL", null, ["callee:0047ce14:8"]]
- 00a059c4 bytes 04dde997
+ 00a05a18 bytes ffdce997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27a9315ba10227d664e8d17f2636833f"></a>

### [`00a05a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05a50.md) → [`00a05aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05aa4.md) _INIT_206

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.88% / 新版 85.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a05ae0",
      "incomplete_value": true,
      "site": "00a05afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00a05a8c",
      "incomplete_value": true,
      "site": "00a05aa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f26:8"
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
      "definition_site": "00a05b24",
      "incomplete_value": true,
      "site": "00a05b40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00a05ad0",
      "incomplete_value": true,
      "site": "00a05aec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dc2:8"
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
      "definition_site": "00a05b44",
      "incomplete_value": true,
      "site": "00a05b5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00a05af0",
      "incomplete_value": true,
      "site": "00a05b08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f62:8"
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
      "00a05ae0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00a05b04",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00a05b24",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a05ae0",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00a05b04",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00a05b24",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05a50.md#insn-00a05c84) · [`00a05a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05a50.md#insn-00a05a7c) · [`00a05a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05a50.md#insn-00a05a84)
- 新版 `00a05cd8`（命令位置の公開資料なし） · `00a05ad0`（命令位置の公開資料なし）

~~~diff
- 00a05c84 ["INT_ADD", "register:40f0:8", ["const:a05c84:8", "const:4:8"]]
- 00a05c84 ["CALL", null, ["callee:00c57f00:8"]]
+ 00a05cd8 ["INT_ADD", "register:40f0:8", ["const:a05cd8:8", "const:4:8"]]
+ 00a05cd8 ["CALL", null, ["callee:00c57f00:8"]]
- 00a05c84 bytes 6b480994
+ 00a05cd8 bytes 8a480994
- 00a05a7c ["COPY", "tmp:0:8", ["const:d50:8"]]
- 00a05a7c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a05a7c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a05a7c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a05ad0 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00a05ad0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a05ad0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a05ad0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a05a7c bytes 73423591
+ 00a05ad0 bytes 73423991
- 00a05a84 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 00a05a84 bytes 89c5ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2946f09b5fe165ad83822e858bd216c9"></a>

### [`00a05de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05de0.md) → [`00a05e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05e34.md) FUN_00a05e34

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 15件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)
- 新版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 15件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.27% / 新版 96.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a05e74",
      "incomplete_value": false,
      "site": "00a05e80",
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
    "old": {
      "definition_site": "00a05e20",
      "incomplete_value": false,
      "site": "00a05e2c",
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
            "const:d38:8"
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
      "definition_site": "00a05eac",
      "incomplete_value": true,
      "site": "00a05eb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:76c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05e58",
      "incomplete_value": true,
      "site": "00a05e64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7b9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a06008",
      "incomplete_value": true,
      "site": "00a06014",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:69a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05fb4",
      "incomplete_value": true,
      "site": "00a05fc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ee:8"
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
      "00a05e80",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00a05eac",
      "READ",
      [
        "storage",
        "002a17b9",
        null,
        "string"
      ]
    ],
    [
      "00a06008",
      "READ",
      [
        "storage",
        "002b96ee",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a05e80",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "00a05eac",
      "READ",
      [
        "storage",
        "002a176c",
        null,
        "string"
      ]
    ],
    [
      "00a06008",
      "READ",
      [
        "storage",
        "002b969a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05de0.md#insn-00a05e18) · [`00a05e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05de0.md#insn-00a05e20) · [`00a05e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05de0.md#insn-00a05e54)
- 新版 `00a05e6c`（命令位置の公開資料なし） · `00a05e74`（命令位置の公開資料なし） · `00a05ea8`（命令位置の公開資料なし）

~~~diff
- 00a05e18 ["INT_ADD", "register:40f0:8", ["const:a05e18:8", "const:4:8"]]
- 00a05e18 ["CALL", null, ["callee:00487e60:8"]]
+ 00a05e6c ["INT_ADD", "register:40f0:8", ["const:a05e6c:8", "const:4:8"]]
+ 00a05e6c ["CALL", null, ["callee:00487e60:8"]]
- 00a05e18 bytes 0208ea97
+ 00a05e6c bytes fd07ea97
- 00a05e20 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00a05e20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a05e20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a05e20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a05e74 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00a05e74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05e74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05e74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a05e20 bytes 08e13491
+ 00a05e74 bytes 08213891
- 00a05e54 ["COPY", "tmp:0:8", ["const:7b9:8"]]
- 00a05e54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a05e54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a05e54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a05ea8 ["COPY", "tmp:0:8", ["const:76c:8"]]
+ 00a05ea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05ea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05ea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a05e54 bytes 08e51e91
+ 00a05ea8 bytes 08b11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f48a1d77c525a8c0d36d4c06d3b3ae9"></a>

### [`00a0672c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md) → [`00a06780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06780.md) FUN_00a06780

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007ef320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef320.md) · 呼出先 11件 [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`00802cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802cec.md) [`00802d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d4c.md) [`00802d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md) [`00802e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802e6c.md)
- 新版 呼出元 2件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007ef378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007ef378.md) · 呼出先 11件 [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md) [`00802d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d44.md) [`00802da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802da4.md) [`00802dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802dd0.md) [`00802ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802ec4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

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
      "site": "00a067f0",
      "value": [
        "leaf",
        "ram:a65e5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0679c",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0684c",
      "value": [
        "leaf",
        "ram:803dd4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a067f8",
      "value": [
        "leaf",
        "ram:803d7c:8"
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
      "00a067f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      "00a0684c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00803d7c"
      ]
    ]
  ],
  "added": [
    [
      "00a067f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65e5c"
      ]
    ],
    [
      "00a0684c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00803dd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a06748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md#insn-00a06748) · [`00a0679c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md#insn-00a0679c) · [`00a067f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md#insn-00a067f8)
- 新版 `00a0679c`（命令位置の公開資料なし） · `00a067f0`（命令位置の公開資料なし） · `00a0684c`（命令位置の公開資料なし）

~~~diff
- 00a06748 ["INT_ADD", "register:40f0:8", ["const:a06748:8", "const:4:8"]]
- 00a06748 ["CALL", null, ["callee:00851550:8"]]
+ 00a0679c ["INT_ADD", "register:40f0:8", ["const:a0679c:8", "const:4:8"]]
+ 00a0679c ["CALL", null, ["callee:00851550:8"]]
- 00a06748 bytes 6c2bf997
+ 00a0679c bytes 6d2bf997
- 00a0679c ["INT_ADD", "register:40f0:8", ["const:a0679c:8", "const:4:8"]]
- 00a0679c ["CALL", null, ["ram:a65dec:8"]]
+ 00a067f0 ["INT_ADD", "register:40f0:8", ["const:a067f0:8", "const:4:8"]]
+ 00a067f0 ["CALL", null, ["ram:a65e5c:8"]]
- 00a0679c bytes 947d0194
+ 00a067f0 bytes 9b7d0194
- 00a067f8 ["INT_ADD", "register:40f0:8", ["const:a067f8:8", "const:4:8"]]
- 00a067f8 ["CALL", null, ["ram:803d7c:8"]]
+ 00a0684c ["INT_ADD", "register:40f0:8", ["const:a0684c:8", "const:4:8"]]
+ 00a0684c ["CALL", null, ["ram:803dd4:8"]]
- 00a067f8 bytes 61f5f797
+ 00a0684c bytes 62f5f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61ff3d5b16e5523e2bdb3d5723a72e7a"></a>

### [`00a069f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a069f8.md) → [`00a06a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06a4c.md) FUN_00a06a4c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a05de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05de0.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00a05e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05e34.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00a06a58",
      "incomplete_value": false,
      "site": "00a06a5c",
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
      "definition_site": "00a06a04",
      "incomplete_value": false,
      "site": "00a06a08",
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
      "00a06a58",
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
      "00a06a58",
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

- 旧版 [`00a06a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a069f8.md#insn-00a06a08) · [`00a06a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a069f8.md#insn-00a06a04)
- 新版 `00a06a5c`（命令位置の公開資料なし） · `00a06a58`（命令位置の公開資料なし）

~~~diff
- 00a06a08 ["INT_ADD", "register:40f0:8", ["const:a06a08:8", "const:4:8"]]
- 00a06a08 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00a06a5c ["INT_ADD", "register:40f0:8", ["const:a06a5c:8", "const:4:8"]]
+ 00a06a5c ["CALL", null, ["callee:0043b7b8:8"]]
- 00a06a08 bytes 5cd3e897
+ 00a06a5c bytes 57d3e897
- 00a06a04 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00a06a04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a06a04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a06a04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a06a58 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00a06a58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a06a58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a06a58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a06a04 bytes 00303d91
+ 00a06a58 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

