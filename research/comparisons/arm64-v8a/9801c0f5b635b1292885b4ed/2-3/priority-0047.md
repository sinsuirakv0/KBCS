# v16.0.1 → v16.0.2 · 最優先の変更候補 (47)

[一覧の目次](README.md)

<a id="compare-d9efb1fce3ffeb860dec94adf16a8473"></a>

### [`0087bc44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bc44.md) → [`0087bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bc9c.md) FUN_0087bc9c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 11件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00879644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879644.md) [`0087a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a748.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0087969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087969c.md) [`0087a7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a7a0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087bd14",
      "incomplete_value": true,
      "site": "0087bd28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087bcbc",
      "incomplete_value": true,
      "site": "0087bcd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:660:8"
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
      "definition_site": "0087bd2c",
      "incomplete_value": true,
      "site": "0087bd3c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:7c1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087bcd4",
      "incomplete_value": true,
      "site": "0087bce4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:781:8"
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
      "definition_site": "0087bd2c",
      "incomplete_value": true,
      "site": "0087bd3c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0087bcd4",
      "incomplete_value": true,
      "site": "0087bce4",
      "value": [
        "LOAD",
        "16",
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
      "0087bd14",
      "READ",
      [
        "storage",
        "002c2660",
        null,
        null
      ]
    ],
    [
      "0087bd2c",
      "READ",
      [
        "storage",
        "002c1781",
        null,
        null
      ]
    ],
    [
      "0087bd2c",
      "READ",
      [
        "storage",
        "002c1791",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0087bd14",
      "READ",
      [
        "storage",
        "002c26a0",
        null,
        null
      ]
    ],
    [
      "0087bd2c",
      "READ",
      [
        "storage",
        "002c17c1",
        null,
        null
      ]
    ],
    [
      "0087bd2c",
      "READ",
      [
        "storage",
        "002c17d1",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bc44.md#insn-0087bc8c) · [`0087bd64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bc44.md#insn-0087bd64) · [`0087bdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bc44.md#insn-0087bdbc)
- 新版 `0087bce4`（命令位置の公開資料なし） · `0087bdbc`（命令位置の公開資料なし） · `0087be14`（命令位置の公開資料なし）

~~~diff
- 0087bc8c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087bc8c ["INT_ADD", "register:40f0:8", ["const:87bc8c:8", "const:4:8"]]
- 0087bc8c ["CALLIND", null, ["register:0:8"]]
+ 0087bce4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087bce4 ["INT_ADD", "register:40f0:8", ["const:87bce4:8", "const:4:8"]]
+ 0087bce4 ["CALLIND", null, ["register:0:8"]]
- 0087bc8c bytes 00013fd6
+ 0087bce4 bytes 00013fd6
- 0087bd64 ["INT_ADD", "register:40f0:8", ["const:87bd64:8", "const:4:8"]]
- 0087bd64 ["CALL", null, ["callee:00c5ab80:8"]]
+ 0087bdbc ["INT_ADD", "register:40f0:8", ["const:87bdbc:8", "const:4:8"]]
+ 0087bdbc ["CALL", null, ["callee:00c5ab80:8"]]
- 0087bd64 bytes 537b0f94
+ 0087bdbc bytes 717b0f94
- 0087bdbc ["INT_ADD", "register:40f0:8", ["const:87bdbc:8", "const:4:8"]]
- 0087bdbc ["CALL", null, ["ram:87a748:8"]]
+ 0087be14 ["INT_ADD", "register:40f0:8", ["const:87be14:8", "const:4:8"]]
+ 0087be14 ["CALL", null, ["ram:87a7a0:8"]]
- 0087bdbc bytes 63faff97
+ 0087be14 bytes 63faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abc08963d852b8e3a63e468e49c43b12"></a>

### [`0087bfa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfa4.md) → [`0087bffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bffc.md) FUN_0087bffc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c008",
      "incomplete_value": false,
      "site": "0087c014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087bfb0",
      "incomplete_value": false,
      "site": "0087bfbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:388:8"
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
      "0087c014",
      "DATA",
      [
        "storage",
        "00c80388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c014",
      "DATA",
      [
        "storage",
        "00c80458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087bfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfa4.md#insn-0087bfb0)
- 新版 `0087c008`（命令位置の公開資料なし）

~~~diff
- 0087bfb0 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0087bfb0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087bfb0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087bfb0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087c008 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0087c008 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087c008 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087c008 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087bfb0 bytes 4a210e91
+ 0087c008 bytes 4a611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5028bc1b28303dedd6c29a3bd9e3cb74"></a>

### [`0087bfe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfe8.md) → [`0087c040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c040.md) FUN_0087c040

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c058",
      "incomplete_value": false,
      "site": "0087c064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c000",
      "incomplete_value": false,
      "site": "0087c00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:388:8"
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
      "0087c064",
      "DATA",
      [
        "storage",
        "00c80388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c064",
      "DATA",
      [
        "storage",
        "00c80458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfe8.md#insn-0087c000) · [`0087c030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfe8.md#insn-0087c030)
- 新版 `0087c058`（命令位置の公開資料なし） · `0087c088`（命令位置の公開資料なし）

~~~diff
- 0087c000 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0087c000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c058 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0087c058 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c058 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c058 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c000 bytes 08210e91
+ 0087c058 bytes 08611191
- 0087c030 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c030 ["INT_ADD", "register:40f0:8", ["const:87c030:8", "const:4:8"]]
- 0087c030 ["CALLIND", null, ["register:0:8"]]
+ 0087c088 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c088 ["INT_ADD", "register:40f0:8", ["const:87c088:8", "const:4:8"]]
+ 0087c088 ["CALLIND", null, ["register:0:8"]]
- 0087c030 bytes 00013fd6
+ 0087c088 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-319554a3bf802c2684803f2164b19ea0"></a>

### [`0087c044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c044.md) → [`0087c09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c09c.md) FUN_0087c09c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0087c0c8",
      "incomplete_value": false,
      "site": "0087c0c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c070",
      "incomplete_value": false,
      "site": "0087c070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:388:8"
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
      "0087c0c8",
      "DATA",
      [
        "storage",
        "00c80388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c0c8",
      "DATA",
      [
        "storage",
        "00c80458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c044.md#insn-0087c058) · [`0087c068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c044.md#insn-0087c068) · [`0087c08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c044.md#insn-0087c08c)
- 新版 `0087c0b0`（命令位置の公開資料なし） · `0087c0c0`（命令位置の公開資料なし） · `0087c0e4`（命令位置の公開資料なし）

~~~diff
- 0087c058 ["INT_ADD", "register:40f0:8", ["const:87c058:8", "const:4:8"]]
- 0087c058 ["CALL", null, ["callee:00c57f60:8"]]
+ 0087c0b0 ["INT_ADD", "register:40f0:8", ["const:87c0b0:8", "const:4:8"]]
+ 0087c0b0 ["CALL", null, ["callee:00c57f60:8"]]
- 0087c058 bytes 8e6f0f94
+ 0087c0b0 bytes ac6f0f94
- 0087c068 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0087c068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c0c0 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0087c0c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c0c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c0c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c068 bytes 08210e91
+ 0087c0c0 bytes 08611191
- 0087c08c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c08c ["INT_ADD", "register:40f0:8", ["const:87c08c:8", "const:4:8"]]
- 0087c08c ["CALLIND", null, ["register:0:8"]]
+ 0087c0e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c0e4 ["INT_ADD", "register:40f0:8", ["const:87c0e4:8", "const:4:8"]]
+ 0087c0e4 ["CALLIND", null, ["register:0:8"]]
- 0087c08c bytes 00013fd6
+ 0087c0e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf4d2b02f83e56ac88de0c433326e215"></a>

### [`0087c0cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c0cc.md) → [`0087c124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c124.md) FUN_0087c124

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c140",
      "incomplete_value": false,
      "site": "0087c140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c0e8",
      "incomplete_value": false,
      "site": "0087c0e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:388:8"
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
      "0087c140",
      "DATA",
      [
        "storage",
        "00c80388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c140",
      "DATA",
      [
        "storage",
        "00c80458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c0e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c0cc.md#insn-0087c0e4) · [`0087c108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c0cc.md#insn-0087c108)
- 新版 `0087c13c`（命令位置の公開資料なし） · `0087c160`（命令位置の公開資料なし）

~~~diff
- 0087c0e4 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0087c0e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087c0e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087c0e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087c13c ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0087c13c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c13c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c13c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087c0e4 bytes 29210e91
+ 0087c13c bytes 29611191
- 0087c108 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087c108 ["INT_ADD", "register:40f0:8", ["const:87c108:8", "const:4:8"]]
- 0087c108 ["CALLIND", null, ["register:0:8"]]
+ 0087c160 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087c160 ["INT_ADD", "register:40f0:8", ["const:87c160:8", "const:4:8"]]
+ 0087c160 ["CALLIND", null, ["register:0:8"]]
- 0087c108 bytes 20013fd6
+ 0087c160 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3b535036ee9063b91f28992eb79a816"></a>

### [`0087c210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c210.md) → [`0087c268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c268.md) FUN_0087c268

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c274",
      "incomplete_value": false,
      "site": "0087c280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c21c",
      "incomplete_value": false,
      "site": "0087c228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "0087c280",
      "DATA",
      [
        "storage",
        "00c80408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c280",
      "DATA",
      [
        "storage",
        "00c804d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c210.md#insn-0087c21c)
- 新版 `0087c274`（命令位置の公開資料なし）

~~~diff
- 0087c21c ["COPY", "tmp:0:8", ["const:408:8"]]
- 0087c21c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087c21c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087c21c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087c274 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 0087c274 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087c274 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087c274 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087c21c bytes 4a211091
+ 0087c274 bytes 4a611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7d10253f50d568a79da10363096256d"></a>

### [`0087c254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c254.md) → [`0087c2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c2ac.md) FUN_0087c2ac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c2c4",
      "incomplete_value": false,
      "site": "0087c2d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c26c",
      "incomplete_value": false,
      "site": "0087c278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "0087c2d0",
      "DATA",
      [
        "storage",
        "00c80408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c2d0",
      "DATA",
      [
        "storage",
        "00c804d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c26c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c254.md#insn-0087c26c) · [`0087c29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c254.md#insn-0087c29c)
- 新版 `0087c2c4`（命令位置の公開資料なし） · `0087c2f4`（命令位置の公開資料なし）

~~~diff
- 0087c26c ["COPY", "tmp:0:8", ["const:408:8"]]
- 0087c26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c2c4 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 0087c2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c26c bytes 08211091
+ 0087c2c4 bytes 08611391
- 0087c29c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c29c ["INT_ADD", "register:40f0:8", ["const:87c29c:8", "const:4:8"]]
- 0087c29c ["CALLIND", null, ["register:0:8"]]
+ 0087c2f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c2f4 ["INT_ADD", "register:40f0:8", ["const:87c2f4:8", "const:4:8"]]
+ 0087c2f4 ["CALLIND", null, ["register:0:8"]]
- 0087c29c bytes 00013fd6
+ 0087c2f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4b3c7c8858066e6c6a813a57277b698"></a>

### [`0087c2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c2b0.md) → [`0087c308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c308.md) FUN_0087c308

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0087c334",
      "incomplete_value": false,
      "site": "0087c334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c2dc",
      "incomplete_value": false,
      "site": "0087c2dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "0087c334",
      "DATA",
      [
        "storage",
        "00c80408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c334",
      "DATA",
      [
        "storage",
        "00c804d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c2b0.md#insn-0087c2c4) · [`0087c2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c2b0.md#insn-0087c2d4) · [`0087c2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c2b0.md#insn-0087c2f8)
- 新版 `0087c31c`（命令位置の公開資料なし） · `0087c32c`（命令位置の公開資料なし） · `0087c350`（命令位置の公開資料なし）

~~~diff
- 0087c2c4 ["INT_ADD", "register:40f0:8", ["const:87c2c4:8", "const:4:8"]]
- 0087c2c4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0087c31c ["INT_ADD", "register:40f0:8", ["const:87c31c:8", "const:4:8"]]
+ 0087c31c ["CALL", null, ["callee:00c57f60:8"]]
- 0087c2c4 bytes f36e0f94
+ 0087c31c bytes 116f0f94
- 0087c2d4 ["COPY", "tmp:0:8", ["const:408:8"]]
- 0087c2d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c2d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c2d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c32c ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 0087c32c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c32c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c32c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c2d4 bytes 08211091
+ 0087c32c bytes 08611391
- 0087c2f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c2f8 ["INT_ADD", "register:40f0:8", ["const:87c2f8:8", "const:4:8"]]
- 0087c2f8 ["CALLIND", null, ["register:0:8"]]
+ 0087c350 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c350 ["INT_ADD", "register:40f0:8", ["const:87c350:8", "const:4:8"]]
+ 0087c350 ["CALLIND", null, ["register:0:8"]]
- 0087c2f8 bytes 00013fd6
+ 0087c350 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcc49b83e294024aee52971c65c902e2"></a>

### [`0087c338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c338.md) → [`0087c390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c390.md) FUN_0087c390

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c3ac",
      "incomplete_value": false,
      "site": "0087c3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c354",
      "incomplete_value": false,
      "site": "0087c354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "0087c3ac",
      "DATA",
      [
        "storage",
        "00c80408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c3ac",
      "DATA",
      [
        "storage",
        "00c804d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c338.md#insn-0087c350) · [`0087c374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c338.md#insn-0087c374)
- 新版 `0087c3a8`（命令位置の公開資料なし） · `0087c3cc`（命令位置の公開資料なし）

~~~diff
- 0087c350 ["COPY", "tmp:0:8", ["const:408:8"]]
- 0087c350 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087c350 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087c350 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087c3a8 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 0087c3a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c3a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c3a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087c350 bytes 29211091
+ 0087c3a8 bytes 29611391
- 0087c374 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087c374 ["INT_ADD", "register:40f0:8", ["const:87c374:8", "const:4:8"]]
- 0087c374 ["CALLIND", null, ["register:0:8"]]
+ 0087c3cc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087c3cc ["INT_ADD", "register:40f0:8", ["const:87c3cc:8", "const:4:8"]]
+ 0087c3cc ["CALLIND", null, ["register:0:8"]]
- 0087c374 bytes 20013fd6
+ 0087c3cc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b873c0e8a9101f6726d463dfa9e981c2"></a>

### [`0087c60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c60c.md) → [`0087c664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c664.md) FUN_0087c664

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c670",
      "incomplete_value": false,
      "site": "0087c67c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c618",
      "incomplete_value": false,
      "site": "0087c624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "0087c67c",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c67c",
      "DATA",
      [
        "storage",
        "00c80568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c60c.md#insn-0087c618)
- 新版 `0087c670`（命令位置の公開資料なし）

~~~diff
- 0087c618 ["COPY", "tmp:0:8", ["const:498:8"]]
- 0087c618 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087c618 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087c618 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087c670 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 0087c670 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087c670 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087c670 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087c618 bytes 4a611291
+ 0087c670 bytes 4aa11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fe9ca062bf4b40c3993eb74a11ebff7"></a>

### [`0087c650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c650.md) → [`0087c6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c6a8.md) FUN_0087c6a8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c6c0",
      "incomplete_value": false,
      "site": "0087c6cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c668",
      "incomplete_value": false,
      "site": "0087c674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "0087c6cc",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c6cc",
      "DATA",
      [
        "storage",
        "00c80568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c650.md#insn-0087c668) · [`0087c698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c650.md#insn-0087c698)
- 新版 `0087c6c0`（命令位置の公開資料なし） · `0087c6f0`（命令位置の公開資料なし）

~~~diff
- 0087c668 ["COPY", "tmp:0:8", ["const:498:8"]]
- 0087c668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c6c0 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 0087c6c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c6c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c6c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c668 bytes 08611291
+ 0087c6c0 bytes 08a11591
- 0087c698 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c698 ["INT_ADD", "register:40f0:8", ["const:87c698:8", "const:4:8"]]
- 0087c698 ["CALLIND", null, ["register:0:8"]]
+ 0087c6f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c6f0 ["INT_ADD", "register:40f0:8", ["const:87c6f0:8", "const:4:8"]]
+ 0087c6f0 ["CALLIND", null, ["register:0:8"]]
- 0087c698 bytes 00013fd6
+ 0087c6f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9c0a2ce4c6b74c0d216c502b4bd5d8b"></a>

### [`0087c6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c6ac.md) → [`0087c704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c704.md) FUN_0087c704

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0087c730",
      "incomplete_value": false,
      "site": "0087c730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c6d8",
      "incomplete_value": false,
      "site": "0087c6d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "0087c730",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c730",
      "DATA",
      [
        "storage",
        "00c80568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c6ac.md#insn-0087c6c0) · [`0087c6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c6ac.md#insn-0087c6d0) · [`0087c6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c6ac.md#insn-0087c6f4)
- 新版 `0087c718`（命令位置の公開資料なし） · `0087c728`（命令位置の公開資料なし） · `0087c74c`（命令位置の公開資料なし）

~~~diff
- 0087c6c0 ["INT_ADD", "register:40f0:8", ["const:87c6c0:8", "const:4:8"]]
- 0087c6c0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0087c718 ["INT_ADD", "register:40f0:8", ["const:87c718:8", "const:4:8"]]
+ 0087c718 ["CALL", null, ["callee:00c57f60:8"]]
- 0087c6c0 bytes f46d0f94
+ 0087c718 bytes 126e0f94
- 0087c6d0 ["COPY", "tmp:0:8", ["const:498:8"]]
- 0087c6d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c6d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c6d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c728 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 0087c728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c6d0 bytes 08611291
+ 0087c728 bytes 08a11591
- 0087c6f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c6f4 ["INT_ADD", "register:40f0:8", ["const:87c6f4:8", "const:4:8"]]
- 0087c6f4 ["CALLIND", null, ["register:0:8"]]
+ 0087c74c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c74c ["INT_ADD", "register:40f0:8", ["const:87c74c:8", "const:4:8"]]
+ 0087c74c ["CALLIND", null, ["register:0:8"]]
- 0087c6f4 bytes 00013fd6
+ 0087c74c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39d86793c3c3311cc9042f5dd8f38434"></a>

### [`0087c734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c734.md) → [`0087c78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c78c.md) FUN_0087c78c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c7a8",
      "incomplete_value": false,
      "site": "0087c7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c750",
      "incomplete_value": false,
      "site": "0087c750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "0087c7a8",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c7a8",
      "DATA",
      [
        "storage",
        "00c80568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c74c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c734.md#insn-0087c74c) · [`0087c770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c734.md#insn-0087c770)
- 新版 `0087c7a4`（命令位置の公開資料なし） · `0087c7c8`（命令位置の公開資料なし）

~~~diff
- 0087c74c ["COPY", "tmp:0:8", ["const:498:8"]]
- 0087c74c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087c74c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087c74c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087c7a4 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 0087c7a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c7a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c7a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087c74c bytes 29611291
+ 0087c7a4 bytes 29a11591
- 0087c770 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087c770 ["INT_ADD", "register:40f0:8", ["const:87c770:8", "const:4:8"]]
- 0087c770 ["CALLIND", null, ["register:0:8"]]
+ 0087c7c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087c7c8 ["INT_ADD", "register:40f0:8", ["const:87c7c8:8", "const:4:8"]]
+ 0087c7c8 ["CALLIND", null, ["register:0:8"]]
- 0087c770 bytes 20013fd6
+ 0087c7c8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bda2f6012d57768c8b05e53a3b0617e"></a>

### [`0087c878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c878.md) → [`0087c8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c8d0.md) FUN_0087c8d0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c8e8",
      "incomplete_value": false,
      "site": "0087c8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c890",
      "incomplete_value": false,
      "site": "0087c8a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "0087c8f8",
      "DATA",
      [
        "storage",
        "00c80518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c8f8",
      "DATA",
      [
        "storage",
        "00c805e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c878.md#insn-0087c890) · [`0087c8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c878.md#insn-0087c8c4)
- 新版 `0087c8e8`（命令位置の公開資料なし） · `0087c91c`（命令位置の公開資料なし）

~~~diff
- 0087c890 ["COPY", "tmp:0:8", ["const:518:8"]]
- 0087c890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c8e8 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 0087c8e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c8e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c8e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c890 bytes 08611491
+ 0087c8e8 bytes 08a11791
- 0087c8c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c8c4 ["INT_ADD", "register:40f0:8", ["const:87c8c4:8", "const:4:8"]]
- 0087c8c4 ["CALLIND", null, ["register:0:8"]]
+ 0087c91c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c91c ["INT_ADD", "register:40f0:8", ["const:87c91c:8", "const:4:8"]]
+ 0087c91c ["CALLIND", null, ["register:0:8"]]
- 0087c8c4 bytes 00013fd6
+ 0087c91c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b650259e1258212df1ebba9570d6131e"></a>

### [`0087c908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c908.md) → [`0087c960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c960.md) FUN_0087c960

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c978",
      "incomplete_value": false,
      "site": "0087c988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c920",
      "incomplete_value": false,
      "site": "0087c930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "0087c988",
      "DATA",
      [
        "storage",
        "00c80518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c988",
      "DATA",
      [
        "storage",
        "00c805e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c908.md#insn-0087c920) · [`0087c954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c908.md#insn-0087c954) · [`0087c980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c908.md#insn-0087c980)
- 新版 `0087c978`（命令位置の公開資料なし） · `0087c9ac`（命令位置の公開資料なし） · `0087c9d8`（命令位置の公開資料なし）

~~~diff
- 0087c920 ["COPY", "tmp:0:8", ["const:518:8"]]
- 0087c920 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c920 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c920 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c978 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 0087c978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c920 bytes 08611491
+ 0087c978 bytes 08a11791
- 0087c954 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c954 ["INT_ADD", "register:40f0:8", ["const:87c954:8", "const:4:8"]]
- 0087c954 ["CALLIND", null, ["register:0:8"]]
+ 0087c9ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c9ac ["INT_ADD", "register:40f0:8", ["const:87c9ac:8", "const:4:8"]]
+ 0087c9ac ["CALLIND", null, ["register:0:8"]]
- 0087c954 bytes 00013fd6
+ 0087c9ac bytes 00013fd6
- 0087c980 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c980 ["INT_ADD", "register:40f0:8", ["const:87c980:8", "const:4:8"]]
- 0087c980 ["CALLIND", null, ["register:0:8"]]
+ 0087c9d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c9d8 ["INT_ADD", "register:40f0:8", ["const:87c9d8:8", "const:4:8"]]
+ 0087c9d8 ["CALLIND", null, ["register:0:8"]]
- 0087c980 bytes 00013fd6
+ 0087c9d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26859b1ef514c37cf439549c9e17572b"></a>

### [`0087c994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c994.md) → [`0087c9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c9ec.md) FUN_0087c9ec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0087ca1c",
      "incomplete_value": false,
      "site": "0087ca1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c9c4",
      "incomplete_value": false,
      "site": "0087c9c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "0087ca1c",
      "DATA",
      [
        "storage",
        "00c80518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087ca1c",
      "DATA",
      [
        "storage",
        "00c805e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087ca1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c994.md#insn-0087ca1c) · [`0087c9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c994.md#insn-0087c9ac) · [`0087c9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c994.md#insn-0087c9bc)
- 新版 `0087ca74`（命令位置の公開資料なし） · `0087ca04`（命令位置の公開資料なし） · `0087ca14`（命令位置の公開資料なし）

~~~diff
- 0087ca1c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087ca1c ["INT_ADD", "register:40f0:8", ["const:87ca1c:8", "const:4:8"]]
- 0087ca1c ["CALLIND", null, ["register:0:8"]]
+ 0087ca74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087ca74 ["INT_ADD", "register:40f0:8", ["const:87ca74:8", "const:4:8"]]
+ 0087ca74 ["CALLIND", null, ["register:0:8"]]
- 0087ca1c bytes 00013fd6
+ 0087ca74 bytes 00013fd6
- 0087c9ac ["INT_ADD", "register:40f0:8", ["const:87c9ac:8", "const:4:8"]]
- 0087c9ac ["CALL", null, ["callee:00c57f60:8"]]
+ 0087ca04 ["INT_ADD", "register:40f0:8", ["const:87ca04:8", "const:4:8"]]
+ 0087ca04 ["CALL", null, ["callee:00c57f60:8"]]
- 0087c9ac bytes 396d0f94
+ 0087ca04 bytes 576d0f94
- 0087c9bc ["COPY", "tmp:0:8", ["const:518:8"]]
- 0087c9bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c9bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c9bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087ca14 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 0087ca14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087ca14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087ca14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c9bc bytes 08611491
+ 0087ca14 bytes 08a11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aca7355e90239de168efe43df6168f06"></a>

### [`0087ca9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ca9c.md) → [`0087caf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087caf4.md) FUN_0087caf4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087cb1c",
      "incomplete_value": false,
      "site": "0087cb1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087cac4",
      "incomplete_value": false,
      "site": "0087cac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "0087cb1c",
      "DATA",
      [
        "storage",
        "00c80518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087cb1c",
      "DATA",
      [
        "storage",
        "00c805e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087cabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ca9c.md#insn-0087cabc) · [`0087cac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ca9c.md#insn-0087cac0) · [`0087cae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ca9c.md#insn-0087cae0)
- 新版 `0087cb14`（命令位置の公開資料なし） · `0087cb38`（命令位置の公開資料なし）

~~~diff
- 0087cabc ["COPY", "tmp:0:8", ["const:518:8"]]
- 0087cabc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087cabc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087cabc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087cb14 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 0087cb14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087cb14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087cb14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087cabc bytes 08611491
+ 0087cb14 bytes 08a11791
- 0087cac0 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 0087cac0 bytes f40301aa
- 0087cae0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087cae0 ["INT_ADD", "register:40f0:8", ["const:87cae0:8", "const:4:8"]]
- 0087cae0 ["CALLIND", null, ["register:0:8"]]
+ 0087cb38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087cb38 ["INT_ADD", "register:40f0:8", ["const:87cb38:8", "const:4:8"]]
+ 0087cb38 ["CALLIND", null, ["register:0:8"]]
- 0087cae0 bytes 00013fd6
+ 0087cb38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93d663f1dbd138c07b16f961d0d72da6"></a>

### [`0087ce70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ce70.md) → [`0087cec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087cec8.md) _INIT_161

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 78.74% / 新版 78.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 7件, `store_value` 5件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087cf04",
      "incomplete_value": true,
      "site": "0087cf20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0087ceac",
      "incomplete_value": true,
      "site": "0087cec8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0087cf68",
      "incomplete_value": true,
      "site": "0087cf80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0087cf10",
      "incomplete_value": true,
      "site": "0087cf28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087cfa4",
      "incomplete_value": true,
      "site": "0087cfc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0087cf4c",
      "incomplete_value": true,
      "site": "0087cf68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f5d:8"
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
      "0087cf04",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0087cf28",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0087cf48",
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
      "0087cf04",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0087cf28",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0087cf48",
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

- 旧版 [`0087d08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ce70.md#insn-0087d08c) · [`0087d0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ce70.md#insn-0087d0a8) · [`0087d0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ce70.md#insn-0087d0c0)
- 新版 `0087d0e4`（命令位置の公開資料なし） · `0087d100`（命令位置の公開資料なし） · `0087d118`（命令位置の公開資料なし）

~~~diff
- 0087d08c ["COPY", "register:4098:8", ["const:c62000:8"]]
+ 0087d0e4 ["COPY", "register:4098:8", ["const:c63000:8"]]
- 0087d08c bytes 331f00b0
+ 0087d0e4 bytes 331f00d0
- 0087d0a8 ["INT_ADD", "register:40f0:8", ["const:87d0a8:8", "const:4:8"]]
- 0087d0a8 ["CALL", null, ["callee:00c57f00:8"]]
+ 0087d100 ["INT_ADD", "register:40f0:8", ["const:87d100:8", "const:4:8"]]
+ 0087d100 ["CALL", null, ["callee:00c57f00:8"]]
- 0087d0a8 bytes 626b0f94
+ 0087d100 bytes 806b0f94
- 0087d0c0 ["COPY", "tmp:0:8", ["const:686:8"]]
- 0087d0c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087d0c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087d0c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087d118 ["COPY", "tmp:0:8", ["const:639:8"]]
+ 0087d118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087d118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087d118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087d0c0 bytes 08191a91
+ 0087d118 bytes 08e51891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6922506346cc8f43de3007873ef065f3"></a>

### [`0087d50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d50c.md) → [`0087d564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d564.md) FUN_0087d564

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00861388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00861/00861388.md) · 呼出先 6件 [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a950.md)
- 新版 呼出元 1件 [`008613e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00861/008613e0.md) · 呼出先 6件 [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5aa20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087d5a0",
      "incomplete_value": false,
      "site": "0087d5a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087d548",
      "incomplete_value": false,
      "site": "0087d550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
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
      "0087d5a8",
      "DATA",
      [
        "storage",
        "00c805a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087d5a8",
      "DATA",
      [
        "storage",
        "00c80678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087d518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d50c.md#insn-0087d518) · [`0087d520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d50c.md#insn-0087d520) · [`0087d524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d50c.md#insn-0087d524)
- 新版 `0087d570`（命令位置の公開資料なし） · `0087d578`（命令位置の公開資料なし） · `0087d57c`（命令位置の公開資料なし）

~~~diff
- 0087d518 ["INT_ADD", "register:40f0:8", ["const:87d518:8", "const:4:8"]]
- 0087d518 ["CALL", null, ["callee:00588eac:8"]]
+ 0087d570 ["INT_ADD", "register:40f0:8", ["const:87d570:8", "const:4:8"]]
+ 0087d570 ["CALL", null, ["callee:00588eac:8"]]
- 0087d518 bytes 552ef497
+ 0087d570 bytes 4f2ef497
- 0087d520 ["INT_ADD", "register:40f0:8", ["const:87d520:8", "const:4:8"]]
- 0087d520 ["CALL", null, ["callee:0058919c:8"]]
+ 0087d578 ["INT_ADD", "register:40f0:8", ["const:87d578:8", "const:4:8"]]
+ 0087d578 ["CALL", null, ["callee:0058919c:8"]]
- 0087d520 bytes 0f2ff497
+ 0087d578 bytes 092ff497
- 0087d524 ["INT_ADD", "register:40f0:8", ["const:87d524:8", "const:4:8"]]
- 0087d524 ["CALL", null, ["callee:00589890:8"]]
+ 0087d57c ["INT_ADD", "register:40f0:8", ["const:87d57c:8", "const:4:8"]]
+ 0087d57c ["CALL", null, ["callee:00589890:8"]]
- 0087d524 bytes cb30f497
+ 0087d57c bytes c530f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9372e12c817a7fe831f9be313a916f2"></a>

### [`0087d560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d560.md) → [`0087d5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d5b8.md) _INIT_162

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "0087d5f4",
      "incomplete_value": true,
      "site": "0087d610",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0087d59c",
      "incomplete_value": true,
      "site": "0087d5b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0087d618",
      "incomplete_value": true,
      "site": "0087d634",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0087d5c0",
      "incomplete_value": true,
      "site": "0087d5dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f39:8"
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
      "definition_site": "0087d638",
      "incomplete_value": true,
      "site": "0087d654",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0087d5e0",
      "incomplete_value": true,
      "site": "0087d5fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0087d5f4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0087d618",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0087d638",
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
      "0087d5f4",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0087d618",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0087d638",
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

- 旧版 [`0087d634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d560.md#insn-0087d634) · [`0087d654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d560.md#insn-0087d654) · [`0087d6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d560.md#insn-0087d6c0)
- 新版 `0087d68c`（命令位置の公開資料なし） · `0087d6ac`（命令位置の公開資料なし） · `0087d718`（命令位置の公開資料なし）

~~~diff
- 0087d634 ["COPY", "tmp:0:8", ["const:f5d:8"]]
- 0087d634 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087d634 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087d634 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087d68c ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 0087d68c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087d68c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087d68c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087d634 bytes 29753d91
+ 0087d68c bytes 29413c91
- 0087d654 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 0087d654 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087d654 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087d654 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087d6ac ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 0087d6ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087d6ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087d6ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087d654 bytes 29253c91
+ 0087d6ac bytes 29f13a91
- 0087d6c0 ["INT_ADD", "register:40f0:8", ["const:87d6c0:8", "const:4:8"]]
- 0087d6c0 ["CALL", null, ["callee:0043b838:8"]]
+ 0087d718 ["INT_ADD", "register:40f0:8", ["const:87d718:8", "const:4:8"]]
+ 0087d718 ["CALL", null, ["callee:0043b838:8"]]
- 0087d6c0 bytes 4ef8ee97
+ 0087d718 bytes 48f8ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf4ee04bf8328c0b4064748fc3cd40b9"></a>

### [`0087dc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dc24.md) → [`0087dc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dc7c.md) FUN_0087dc7c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0087dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dd10.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0087dd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dd68.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.92% / 新版 94.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087dc94",
      "incomplete_value": true,
      "site": "0087dc98",
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
                "const:1123000:8"
              ],
              [
                "leaf",
                "const:938:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087dc3c",
      "incomplete_value": true,
      "site": "0087dc40",
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
                "const:1123000:8"
              ],
              [
                "leaf",
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087dcac",
      "incomplete_value": true,
      "site": "0087dcb0",
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
                "const:1123000:8"
              ],
              [
                "leaf",
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087dc54",
      "incomplete_value": true,
      "site": "0087dc58",
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
                "const:1123000:8"
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087dcdc",
      "incomplete_value": true,
      "site": "0087dce0",
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
                "const:1123000:8"
              ],
              [
                "leaf",
                "const:8f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087dc84",
      "incomplete_value": true,
      "site": "0087dc88",
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
                "const:1123000:8"
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
      "0087dc88",
      "READ",
      [
        "storage",
        "01123828",
        null,
        "undefined1"
      ]
    ],
    [
      "0087dc94",
      "READ",
      [
        "storage",
        "01123838",
        null,
        "undefined8"
      ]
    ],
    [
      "0087dca0",
      "READ",
      [
        "storage",
        "01123810",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0087dc88",
      "READ",
      [
        "storage",
        "01123928",
        null,
        "undefined1"
      ]
    ],
    [
      "0087dc94",
      "READ",
      [
        "storage",
        "01123938",
        null,
        "undefined8"
      ]
    ],
    [
      "0087dca0",
      "READ",
      [
        "storage",
        "01123910",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087dc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dc24.md#insn-0087dc30) · [`0087dc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dc24.md#insn-0087dc40) · [`0087dc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dc24.md#insn-0087dc48)
- 新版 `0087dc88`（命令位置の公開資料なし） · `0087dc98`（命令位置の公開資料なし） · `0087dca0`（命令位置の公開資料なし）

~~~diff
- 0087dc30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:828:8"]]
- 0087dc30 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0087dc30 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 0087dc88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:928:8"]]
+ 0087dc88 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 0087dc88 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 0087dc30 bytes 08a16039
+ 0087dc88 bytes 08a16439
- 0087dc40 ["INT_ADD", "register:40f0:8", ["const:87dc40:8", "const:4:8"]]
- 0087dc40 ["CALL", null, ["callee:00c57f80:8"]]
+ 0087dc98 ["INT_ADD", "register:40f0:8", ["const:87dc98:8", "const:4:8"]]
+ 0087dc98 ["CALL", null, ["callee:00c57f80:8"]]
- 0087dc40 bytes 9c680f94
+ 0087dc98 bytes ba680f94
- 0087dc48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:810:8"]]
- 0087dc48 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0087dc48 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 0087dca0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:910:8"]]
+ 0087dca0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 0087dca0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 0087dc48 bytes 08416039
+ 0087dca0 bytes 08416439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7571a502bf0dc38da38618aed2a445d6"></a>

### [`0087dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dd10.md) → [`0087dd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dd68.md) _INIT_163

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0087dc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dc24.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0087dc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dc7c.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 66.94% / 新版 66.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `store_destination` 32件, `store_value` 14件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087ddb0",
      "incomplete_value": true,
      "site": "0087ddcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0087dd58",
      "incomplete_value": true,
      "site": "0087dd74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087ddf4",
      "incomplete_value": true,
      "site": "0087de10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0087dd9c",
      "incomplete_value": true,
      "site": "0087ddb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087de50",
      "incomplete_value": true,
      "site": "0087de6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0087ddf8",
      "incomplete_value": true,
      "site": "0087de14",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f5d:8"
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
      "0087ddb0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0087ddd4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0087ddf4",
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
      "0087ddb0",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0087ddd4",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0087ddf4",
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

- 旧版 [`0087de10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dd10.md#insn-0087de10) · [`0087e038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dd10.md#insn-0087e038) · [`0087e0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dd10.md#insn-0087e0b4)
- 新版 `0087de68`（命令位置の公開資料なし） · `0087e090`（命令位置の公開資料なし） · `0087e10c`（命令位置の公開資料なし）

~~~diff
- 0087de10 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 0087de10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087de10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087de10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087de68 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 0087de68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087de68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087de68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087de10 bytes 29253c91
+ 0087de68 bytes 29f13a91
- 0087e038 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:790:8"]]
- 0087e038 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0087e038 ["COPY", "register:5030:8", ["const:0:8"]]
- 0087e038 ["COPY", "register:5038:8", ["const:0:8"]]
+ 0087e090 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7d0:8"]]
+ 0087e090 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0087e090 ["COPY", "register:5030:8", ["const:0:8"]]
+ 0087e090 ["COPY", "register:5038:8", ["const:0:8"]]
- 0087e038 bytes 01e5c13d
+ 0087e090 bytes 01f5c13d
- 0087e0b4 ["COPY", "tmp:0:8", ["const:6df:8"]]
- 0087e0b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087e0b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087e0b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087e10c ["COPY", "tmp:0:8", ["const:68b:8"]]
+ 0087e10c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087e10c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087e10c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087e0b4 bytes 297d1b91
+ 0087e10c bytes 292d1a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7b030c91cfa1d27f21c42f47e9c3ada"></a>

### [`0087e710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e710.md) → [`0087e768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e768.md) FUN_0087e768

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087e70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e70c.md) · 呼出先 15件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0087ed4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ed4c.md) [`0087f038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f038.md)
- 新版 呼出元 1件 [`0087e764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e764.md) · 呼出先 15件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0087eda4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eda4.md) [`0087f090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.52% / 新版 97.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087e960",
      "incomplete_value": false,
      "site": "0087e964",
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
    "old": {
      "definition_site": "0087e908",
      "incomplete_value": false,
      "site": "0087e90c",
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
            "const:6f5:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0087e7f0",
      "READ",
      [
        "storage",
        "01123768",
        null,
        "undefined1"
      ]
    ],
    [
      "0087e7f0",
      "READ",
      [
        "storage",
        "01123780",
        null,
        "undefined1"
      ]
    ],
    [
      "0087e7f8",
      "READ",
      [
        "storage",
        "01123768",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0087e7f0",
      "READ",
      [
        "storage",
        "01123868",
        null,
        "undefined1"
      ]
    ],
    [
      "0087e7f0",
      "READ",
      [
        "storage",
        "01123880",
        null,
        "undefined1"
      ]
    ],
    [
      "0087e7f8",
      "READ",
      [
        "storage",
        "01123868",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087e90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e710.md#insn-0087e90c) · [`0087e748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e710.md#insn-0087e748) · [`0087e790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e710.md#insn-0087e790)
- 新版 `0087e964`（命令位置の公開資料なし） · `0087e7a0`（命令位置の公開資料なし） · `0087e7e8`（命令位置の公開資料なし）

~~~diff
- 0087e90c ["INT_ADD", "register:40f0:8", ["const:87e90c:8", "const:4:8"]]
- 0087e90c ["CALL", null, ["callee:0087eda4:8"]]
+ 0087e964 ["INT_ADD", "register:40f0:8", ["const:87e964:8", "const:4:8"]]
+ 0087e964 ["CALL", null, ["callee:0087eda4:8"]]
- 0087e90c bytes 10010094
+ 0087e964 bytes 10010094
- 0087e748 ["INT_ADD", "register:40f0:8", ["const:87e748:8", "const:4:8"]]
- 0087e748 ["CALL", null, ["callee:00b363d4:8"]]
+ 0087e7a0 ["INT_ADD", "register:40f0:8", ["const:87e7a0:8", "const:4:8"]]
+ 0087e7a0 ["CALL", null, ["callee:00b363d4:8"]]
- 0087e748 bytes fcde0a94
+ 0087e7a0 bytes 0ddf0a94
- 0087e790 ["COPY", "tmp:0:8", ["const:768:8"]]
- 0087e790 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087e790 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087e790 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087e7e8 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 0087e7e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087e7e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087e7e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087e790 bytes 08a11d91
+ 0087e7e8 bytes 08a12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5946d8b7d29a2d763e36da21a5eded52"></a>

### [`0087eff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eff8.md) → [`0087f050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f050.md) FUN_0087f050

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "0087f054",
      "incomplete_value": false,
      "site": "0087f058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087effc",
      "incomplete_value": false,
      "site": "0087f000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0087f058",
      "DATA",
      [
        "storage",
        "00c80600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0087f058",
      "DATA",
      [
        "storage",
        "00c806d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087effc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eff8.md#insn-0087effc)
- 新版 `0087f054`（命令位置の公開資料なし）

~~~diff
- 0087effc ["COPY", "tmp:0:8", ["const:600:8"]]
- 0087effc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087effc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087effc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087f054 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 0087f054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087f054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087f054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087effc bytes 08011891
+ 0087f054 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be23bafb21135398731cf98d36944a89"></a>

### [`0087f008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f008.md) → [`0087f060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f060.md) FUN_0087f060

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0087f070",
      "incomplete_value": false,
      "site": "0087f078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087f018",
      "incomplete_value": false,
      "site": "0087f020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0087f078",
      "DATA",
      [
        "storage",
        "00c80600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0087f078",
      "DATA",
      [
        "storage",
        "00c806d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087f018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f008.md#insn-0087f018) · [`0087f024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f008.md#insn-0087f024)
- 新版 `0087f070`（命令位置の公開資料なし） · `0087f07c`（命令位置の公開資料なし）

~~~diff
- 0087f018 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0087f018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087f018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087f018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087f070 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 0087f070 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087f070 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087f070 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087f018 bytes 08011891
+ 0087f070 bytes 08411b91
- 0087f024 ["INT_ADD", "register:40f0:8", ["const:87f024:8", "const:4:8"]]
- 0087f024 ["CALL", null, ["callee:00c57f70:8"]]
+ 0087f07c ["INT_ADD", "register:40f0:8", ["const:87f07c:8", "const:4:8"]]
+ 0087f07c ["CALL", null, ["callee:00c57f70:8"]]
- 0087f024 bytes 9f630f94
+ 0087f07c bytes bd630f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9da907ffa25f7d4e1dbab9c5a2d95581"></a>

### [`0087f10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f10c.md) → [`0087f164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f164.md) FUN_0087f164

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.29% / 新版 94.29%

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
      "site": "0087f18c",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087f134",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "site": "0087f194",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087f13c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "0087f18c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0087f194",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0087f1a4",
      "READ",
      [
        "storage",
        "002b78ac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0087f18c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0087f194",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0087f1a4",
      "READ",
      [
        "storage",
        "002b78ec",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087f134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f10c.md#insn-0087f134) · [`0087f13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f10c.md#insn-0087f13c) · [`0087f18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f10c.md#insn-0087f18c)
- 新版 `0087f18c`（命令位置の公開資料なし） · `0087f194`（命令位置の公開資料なし） · `0087f1e4`（命令位置の公開資料なし）

~~~diff
- 0087f134 ["INT_ADD", "register:40f0:8", ["const:87f134:8", "const:4:8"]]
- 0087f134 ["CALL", null, ["ram:48ccf8:8"]]
+ 0087f18c ["INT_ADD", "register:40f0:8", ["const:87f18c:8", "const:4:8"]]
+ 0087f18c ["CALL", null, ["ram:48cd38:8"]]
- 0087f134 bytes f136f097
+ 0087f18c bytes eb36f097
- 0087f13c ["INT_ADD", "register:40f0:8", ["const:87f13c:8", "const:4:8"]]
- 0087f13c ["CALL", null, ["ram:48ccf8:8"]]
+ 0087f194 ["INT_ADD", "register:40f0:8", ["const:87f194:8", "const:4:8"]]
+ 0087f194 ["CALL", null, ["ram:48cd38:8"]]
- 0087f13c bytes ef36f097
+ 0087f194 bytes e936f097
- 0087f18c ["INT_ADD", "register:40f0:8", ["const:87f18c:8", "const:4:8"]]
- 0087f18c ["CALL", null, ["callee:00c57f80:8"]]
+ 0087f1e4 ["INT_ADD", "register:40f0:8", ["const:87f1e4:8", "const:4:8"]]
+ 0087f1e4 ["CALL", null, ["callee:00c57f80:8"]]
- 0087f18c bytes 49630f94
+ 0087f1e4 bytes 67630f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-253c3f1607a9bf3a76821bff0bcb677b"></a>

### [`0087f268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f268.md) → [`0087f2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f2c0.md) FUN_0087f2c0

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087f304",
      "incomplete_value": true,
      "site": "0087f318",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:507:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087f2ac",
      "incomplete_value": true,
      "site": "0087f2c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:554:8"
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
      "site": "0087f2ec",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087f294",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "site": "0087f2f4",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087f29c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "0087f2e8",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "0087f2ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0087f2f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "0087f2e8",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "0087f2ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0087f2f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087f294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f268.md#insn-0087f294) · [`0087f29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f268.md#insn-0087f29c) · [`0087f2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f268.md#insn-0087f2ec)
- 新版 `0087f2ec`（命令位置の公開資料なし） · `0087f2f4`（命令位置の公開資料なし） · `0087f344`（命令位置の公開資料なし）

~~~diff
- 0087f294 ["INT_ADD", "register:40f0:8", ["const:87f294:8", "const:4:8"]]
- 0087f294 ["CALL", null, ["ram:48ccf8:8"]]
+ 0087f2ec ["INT_ADD", "register:40f0:8", ["const:87f2ec:8", "const:4:8"]]
+ 0087f2ec ["CALL", null, ["ram:48cd38:8"]]
- 0087f294 bytes 9936f097
+ 0087f2ec bytes 9336f097
- 0087f29c ["INT_ADD", "register:40f0:8", ["const:87f29c:8", "const:4:8"]]
- 0087f29c ["CALL", null, ["ram:48ccf8:8"]]
+ 0087f2f4 ["INT_ADD", "register:40f0:8", ["const:87f2f4:8", "const:4:8"]]
+ 0087f2f4 ["CALL", null, ["ram:48cd38:8"]]
- 0087f29c bytes 9736f097
+ 0087f2f4 bytes 9136f097
- 0087f2ec ["INT_ADD", "register:40f0:8", ["const:87f2ec:8", "const:4:8"]]
- 0087f2ec ["CALL", null, ["callee:00c57f80:8"]]
+ 0087f344 ["INT_ADD", "register:40f0:8", ["const:87f344:8", "const:4:8"]]
+ 0087f344 ["CALL", null, ["callee:00c57f80:8"]]
- 0087f2ec bytes f1620f94
+ 0087f344 bytes 0f630f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f9a73a2051d20c00440810d03f74727"></a>

### [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) → [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) FUN_0087f3c0

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 55件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`0043f78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f78c.md)
- 新版 呼出元 0件  · 呼出先 55件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`0043f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md) [`0043f7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f7cc.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 92.43% / 新版 92.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 21件, `store_value` 12件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087f488",
      "incomplete_value": false,
      "site": "0087f488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087f430",
      "incomplete_value": false,
      "site": "0087f430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "definition_site": "0087f4e0",
      "incomplete_value": true,
      "site": "0087f4e0",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:857:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087f488",
      "incomplete_value": true,
      "site": "0087f488",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:8ab:8"
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
      "definition_site": "0087f70c",
      "incomplete_value": true,
      "site": "0087f70c",
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
                "const:54b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087f6b4",
      "incomplete_value": true,
      "site": "0087f6b4",
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
                "const:50b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0087f488",
      "DATA",
      [
        "storage",
        "00c80998",
        null,
        "undefined *"
      ]
    ],
    [
      "0087f4d0",
      "READ",
      [
        "storage",
        "002ba8ab",
        null,
        "string"
      ]
    ],
    [
      "0087f4ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a14d8c"
      ]
    ]
  ],
  "added": [
    [
      "0087f488",
      "DATA",
      [
        "storage",
        "00c80a68",
        null,
        "undefined *"
      ]
    ],
    [
      "0087f4d0",
      "READ",
      [
        "storage",
        "002ba857",
        null,
        "string"
      ]
    ],
    [
      "0087f4ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a14de0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087f43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md#insn-0087f43c) · [`0087f494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md#insn-0087f494) · [`0087f4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md#insn-0087f4a4)
- 新版 `0087f494`（命令位置の公開資料なし） · `0087f4ec`（命令位置の公開資料なし） · `0087f4fc`（命令位置の公開資料なし）

~~~diff
- 0087f43c ["INT_ADD", "register:40f0:8", ["const:87f43c:8", "const:4:8"]]
- 0087f43c ["CALL", null, ["callee:008801e4:8"]]
+ 0087f494 ["INT_ADD", "register:40f0:8", ["const:87f494:8", "const:4:8"]]
+ 0087f494 ["CALL", null, ["callee:008801e4:8"]]
- 0087f43c bytes 54030094
+ 0087f494 bytes 54030094
- 0087f494 ["INT_ADD", "register:40f0:8", ["const:87f494:8", "const:4:8"]]
- 0087f494 ["CALL", null, ["ram:a14d8c:8"]]
+ 0087f4ec ["INT_ADD", "register:40f0:8", ["const:87f4ec:8", "const:4:8"]]
+ 0087f4ec ["CALL", null, ["ram:a14de0:8"]]
- 0087f494 bytes 3e560694
+ 0087f4ec bytes 3d560694
- 0087f4a4 ["INT_ADD", "register:40f0:8", ["const:87f4a4:8", "const:4:8"]]
- 0087f4a4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0087f4fc ["INT_ADD", "register:40f0:8", ["const:87f4fc:8", "const:4:8"]]
+ 0087f4fc ["CALL", null, ["callee:00c57f80:8"]]
- 0087f4a4 bytes 83620f94
+ 0087f4fc bytes a1620f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eab68275bebf59fa4ede39615a93bbef"></a>

### [`0088018c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088018c.md) → [`008801e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/008801e4.md) FUN_008801e4

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) · 呼出先 9件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`00492c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492c00.md) [`004938d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md)
- 新版 呼出元 1件 [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) · 呼出先 9件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00492c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492c40.md) [`00493914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008802a4",
      "incomplete_value": false,
      "site": "008802a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088024c",
      "incomplete_value": false,
      "site": "0088024c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00880220",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008801c8",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "site": "00880230",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008801d8",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "00880218",
      "DATA",
      [
        "storage",
        "0039b1d7",
        null,
        "dword"
      ]
    ],
    [
      "00880220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00880230",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "00880218",
      "DATA",
      [
        "storage",
        "0039b1d7",
        null,
        "qword"
      ]
    ],
    [
      "00880220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "00880230",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008801c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088018c.md#insn-008801c8) · [`008801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088018c.md#insn-008801d8) · [`008801cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088018c.md#insn-008801cc)
- 新版 `00880220`（命令位置の公開資料なし） · `00880230`（命令位置の公開資料なし） · `00880224`（命令位置の公開資料なし）

~~~diff
- 008801c8 ["INT_ADD", "register:40f0:8", ["const:8801c8:8", "const:4:8"]]
- 008801c8 ["CALL", null, ["ram:48ccf8:8"]]
+ 00880220 ["INT_ADD", "register:40f0:8", ["const:880220:8", "const:4:8"]]
+ 00880220 ["CALL", null, ["ram:48cd38:8"]]
- 008801c8 bytes cc32f097
+ 00880220 bytes c632f097
- 008801d8 ["INT_ADD", "register:40f0:8", ["const:8801d8:8", "const:4:8"]]
- 008801d8 ["CALL", null, ["ram:48ccf8:8"]]
+ 00880230 ["INT_ADD", "register:40f0:8", ["const:880230:8", "const:4:8"]]
+ 00880230 ["CALL", null, ["ram:48cd38:8"]]
- 008801d8 bytes c832f097
+ 00880230 bytes c232f097
- 008801cc ["INT_ADD", "register:40f0:8", ["const:8801cc:8", "const:4:8"]]
- 008801cc ["CALL", null, ["callee:00492c40:8"]]
+ 00880224 ["INT_ADD", "register:40f0:8", ["const:880224:8", "const:4:8"]]
+ 00880224 ["CALL", null, ["callee:00492c40:8"]]
- 008801cc bytes 8d4af097
+ 00880224 bytes 874af097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd82fa031c0e69b4f47aee63a990a8f6"></a>

### [`008803c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008803c0.md) → [`00880418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880418.md) FUN_00880418

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00880434",
      "incomplete_value": true,
      "site": "00880438",
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
      "definition_site": "008803dc",
      "incomplete_value": true,
      "site": "008803e0",
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
      "0088042c",
      "READ",
      [
        "storage",
        "00c9ac98",
        null,
        "pointer"
      ]
    ],
    [
      "00880438",
      "DATA",
      [
        "storage",
        "00c65598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088042c",
      "READ",
      [
        "storage",
        "00c9ad68",
        null,
        "pointer"
      ]
    ],
    [
      "00880438",
      "DATA",
      [
        "storage",
        "00c65668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008803d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008803c0.md#insn-008803d4) · [`008803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008803c0.md#insn-008803f0) · [`00880418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008803c0.md#insn-00880418)
- 新版 `0088042c`（命令位置の公開資料なし） · `00880448`（命令位置の公開資料なし） · `00880470`（命令位置の公開資料なし）

~~~diff
- 008803d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
- 008803d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0088042c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d68:8"]]
+ 0088042c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008803d4 bytes 084d46f9
+ 0088042c bytes 08b546f9
- 008803f0 ["INT_ADD", "register:40f0:8", ["const:8803f0:8", "const:4:8"]]
- 008803f0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00880448 ["INT_ADD", "register:40f0:8", ["const:880448:8", "const:4:8"]]
+ 00880448 ["CALL", null, ["callee:00c53da0:8"]]
- 008803f0 bytes 444e0f94
+ 00880448 bytes 564e0f94
- 00880418 ["COPY", "register:0:8", ["register:4040:8"]]
- 00880418 ["INT_ADD", "register:40f0:8", ["const:880418:8", "const:4:8"]]
- 00880418 ["CALLIND", null, ["register:0:8"]]
+ 00880470 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00880470 ["INT_ADD", "register:40f0:8", ["const:880470:8", "const:4:8"]]
+ 00880470 ["CALLIND", null, ["register:0:8"]]
- 00880418 bytes 00013fd6
+ 00880470 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b28bdf9000eb1f103269e66a5a2f06e5"></a>

### [`0088043c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088043c.md) → [`00880494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880494.md) FUN_00880494

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f78c.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cf98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf98.md) [`0047cfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cfb8.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f7cc.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047cfd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cfd8.md) [`0047cff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cff8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 6件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008804f8",
      "incomplete_value": true,
      "site": "00880508",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:7e5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008804a0",
      "incomplete_value": true,
      "site": "008804b0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:7a5:8"
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
      "definition_site": "0088050c",
      "incomplete_value": true,
      "site": "0088050c",
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
      "definition_site": "008804b4",
      "incomplete_value": true,
      "site": "008804b4",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008805a4",
      "incomplete_value": true,
      "site": "008805b4",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:470:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088054c",
      "incomplete_value": true,
      "site": "0088055c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:430:8"
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
      "008804c4",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "008804c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "008804e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "008804c4",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "008804c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "008804e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00880470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088043c.md#insn-00880470) · [`00880488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088043c.md#insn-00880488) · [`00880498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088043c.md#insn-00880498)
- 新版 `008804c8`（命令位置の公開資料なし） · `008804e0`（命令位置の公開資料なし） · `008804f0`（命令位置の公開資料なし）

~~~diff
- 00880470 ["INT_ADD", "register:40f0:8", ["const:880470:8", "const:4:8"]]
- 00880470 ["CALL", null, ["ram:48ccf8:8"]]
+ 008804c8 ["INT_ADD", "register:40f0:8", ["const:8804c8:8", "const:4:8"]]
+ 008804c8 ["CALL", null, ["ram:48cd38:8"]]
- 00880470 bytes 2232f097
+ 008804c8 bytes 1c32f097
- 00880488 ["INT_ADD", "register:40f0:8", ["const:880488:8", "const:4:8"]]
- 00880488 ["CALL", null, ["ram:48ccf8:8"]]
+ 008804e0 ["INT_ADD", "register:40f0:8", ["const:8804e0:8", "const:4:8"]]
+ 008804e0 ["CALL", null, ["ram:48cd38:8"]]
- 00880488 bytes 1c32f097
+ 008804e0 bytes 1632f097
- 00880498 ["COPY", "tmp:0:8", ["const:7a5:8"]]
- 00880498 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00880498 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00880498 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008804f0 ["COPY", "tmp:0:8", ["const:7e5:8"]]
+ 008804f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008804f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008804f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00880498 bytes 29951e91
+ 008804f0 bytes 29951f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c87913dcbf8b70c4cd916d41507b45d"></a>

### [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md) → [`00880700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880700.md) FUN_00880700

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 13件 [`00873c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873c50.md) [`0088441c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/0088441c.md) [`008847c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008847c8.md) [`00885368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885368.md) [`00885724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885724.md) · 呼出先 15件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00451ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md) [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md)
- 新版 呼出元 13件 [`00873ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873ca8.md) [`00884474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884474.md) [`00884820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884820.md) [`008853c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008853c0.md) [`0088577c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088577c.md) · 呼出先 15件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00451f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451f18.md) [`00452528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md) [`00597728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597728.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00880860",
      "incomplete_value": false,
      "site": "00880868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00880808",
      "incomplete_value": false,
      "site": "00880810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "definition_site": "008809c4",
      "incomplete_value": false,
      "site": "008809cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088096c",
      "incomplete_value": false,
      "site": "00880974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0088073c",
      "value": [
        "leaf",
        "ram:768c34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008806e4",
      "value": [
        "leaf",
        "ram:768bdc:8"
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
      "0088073c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768bdc"
      ]
    ],
    [
      "0088076c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "unmatched:00880718",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ]
  ],
  "added": [
    [
      "0088073c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768c34"
      ]
    ],
    [
      "0088076c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ],
    [
      "00880770",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008806e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md#insn-008806e4) · [`00880714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md#insn-00880714) · [`00880718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md#insn-00880718)
- 新版 `0088073c`（命令位置の公開資料なし） · `0088076c`（命令位置の公開資料なし）

~~~diff
- 008806e4 ["INT_ADD", "register:40f0:8", ["const:8806e4:8", "const:4:8"]]
- 008806e4 ["CALL", null, ["ram:768bdc:8"]]
+ 0088073c ["INT_ADD", "register:40f0:8", ["const:88073c:8", "const:4:8"]]
+ 0088073c ["CALL", null, ["ram:768c34:8"]]
- 008806e4 bytes 3ea1fb97
+ 0088073c bytes 3ea1fb97
- 00880714 ["INT_ADD", "register:40f0:8", ["const:880714:8", "const:4:8"]]
- 00880714 ["CALL", null, ["ram:764384:8"]]
+ 0088076c ["INT_ADD", "register:40f0:8", ["const:88076c:8", "const:4:8"]]
+ 0088076c ["CALL", null, ["ram:7643dc:8"]]
- 00880714 bytes 1c8ffb97
+ 0088076c bytes 1c8ffb97
- 00880718 ["INT_ADD", "register:40f0:8", ["const:880718:8", "const:4:8"]]
- 00880718 ["CALL", null, ["callee:00851550:8"]]
- 00880718 bytes 7843ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2df4cf66d34b607caa9fe303851d4bf2"></a>

### [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md) → [`00880d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md) FUN_00880d4c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 16件 [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00873dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873dc8.md) [`00881098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md) [`00883ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883ad4.md) · 呼出先 14件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`007683c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007683c8.md)
- 新版 呼出元 16件 [`004737bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004737bc.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`00873e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873e20.md) [`008810f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008810f0.md) [`00883b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883b2c.md) · 呼出先 14件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md) [`00768420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768420.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.52% / 新版 97.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00880e90",
      "incomplete_value": false,
      "site": "00880e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00880e38",
      "incomplete_value": false,
      "site": "00880e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00880d80",
      "value": [
        "leaf",
        "ram:768420:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00880d28",
      "value": [
        "leaf",
        "ram:7683c8:8"
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
      "site": "00880db4",
      "value": [
        "leaf",
        "ram:7643dc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00880d5c",
      "value": [
        "leaf",
        "ram:764384:8"
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
      "00880d80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683c8"
      ]
    ],
    [
      "00880db4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "00880e90",
      "DATA",
      [
        "storage",
        "00c80d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00880d80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768420"
      ]
    ],
    [
      "00880db4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ],
    [
      "00880e90",
      "DATA",
      [
        "storage",
        "00c80df8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00880d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md#insn-00880d28) · [`00880d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md#insn-00880d5c) · [`00880db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md#insn-00880db4)
- 新版 `00880d80`（命令位置の公開資料なし） · `00880db4`（命令位置の公開資料なし） · `00880e0c`（命令位置の公開資料なし）

~~~diff
- 00880d28 ["INT_ADD", "register:40f0:8", ["const:880d28:8", "const:4:8"]]
- 00880d28 ["CALL", null, ["ram:7683c8:8"]]
+ 00880d80 ["INT_ADD", "register:40f0:8", ["const:880d80:8", "const:4:8"]]
+ 00880d80 ["CALL", null, ["ram:768420:8"]]
- 00880d28 bytes a89dfb97
+ 00880d80 bytes a89dfb97
- 00880d5c ["INT_ADD", "register:40f0:8", ["const:880d5c:8", "const:4:8"]]
- 00880d5c ["CALL", null, ["ram:764384:8"]]
+ 00880db4 ["INT_ADD", "register:40f0:8", ["const:880db4:8", "const:4:8"]]
+ 00880db4 ["CALL", null, ["ram:7643dc:8"]]
- 00880d5c bytes 8a8dfb97
+ 00880db4 bytes 8a8dfb97
- 00880db4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00880db4 ["INT_ADD", "register:40f0:8", ["const:880db4:8", "const:4:8"]]
- 00880db4 ["CALLIND", null, ["register:0:8"]]
+ 00880e0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00880e0c ["INT_ADD", "register:40f0:8", ["const:880e0c:8", "const:4:8"]]
+ 00880e0c ["CALLIND", null, ["register:0:8"]]
- 00880db4 bytes 00013fd6
+ 00880e0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86dfbd98db05e52c199cbc32511a7264"></a>

### [`00881098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md) → [`008810f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008810f0.md) FUN_008810f0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0056085c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056085c.md) [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md) [`008861a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008861a0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0056089c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/0056089c.md) [`00880d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md) [`008861f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008861f8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.79% / 新版 97.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008811c0",
      "incomplete_value": false,
      "site": "008811c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00881168",
      "incomplete_value": false,
      "site": "00881168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "008811c0",
      "DATA",
      [
        "storage",
        "00c80e28",
        null,
        "undefined *"
      ]
    ],
    [
      "00881240",
      "READ",
      [
        "storage",
        "00c80e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008811c0",
      "DATA",
      [
        "storage",
        "00c80ef8",
        null,
        "undefined *"
      ]
    ],
    [
      "00881240",
      "READ",
      [
        "storage",
        "00c80f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008810cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md#insn-008810cc) · [`00881100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md#insn-00881100) · [`00881124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md#insn-00881124)
- 新版 `00881124`（命令位置の公開資料なし） · `00881158`（命令位置の公開資料なし） · `0088117c`（命令位置の公開資料なし）

~~~diff
- 008810cc ["INT_ADD", "register:40f0:8", ["const:8810cc:8", "const:4:8"]]
- 008810cc ["CALL", null, ["callee:0056089c:8"]]
+ 00881124 ["INT_ADD", "register:40f0:8", ["const:881124:8", "const:4:8"]]
+ 00881124 ["CALL", null, ["callee:0056089c:8"]]
- 008810cc bytes e47df397
+ 00881124 bytes de7df397
- 00881100 ["INT_ADD", "register:40f0:8", ["const:881100:8", "const:4:8"]]
- 00881100 ["CALL", null, ["callee:0043bb60:8"]]
+ 00881158 ["INT_ADD", "register:40f0:8", ["const:881158:8", "const:4:8"]]
+ 00881158 ["CALL", null, ["callee:0043bb60:8"]]
- 00881100 bytes 88eaee97
+ 00881158 bytes 82eaee97
- 00881124 ["COPY", "register:0:8", ["register:4040:8"]]
- 00881124 ["INT_ADD", "register:40f0:8", ["const:881124:8", "const:4:8"]]
- 00881124 ["CALLIND", null, ["register:0:8"]]
+ 0088117c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088117c ["INT_ADD", "register:40f0:8", ["const:88117c:8", "const:4:8"]]
+ 0088117c ["CALLIND", null, ["register:0:8"]]
- 00881124 bytes 00013fd6
+ 0088117c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa4fd6743162884d764ad6c82a0d3ec2"></a>

### [`008813b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/008813b0.md) → [`00881408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881408.md) FUN_00881408

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00484210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00484250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484250.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.95% / 新版 84.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008814f8",
      "incomplete_value": true,
      "site": "00881508",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:20c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008814a0",
      "incomplete_value": true,
      "site": "008814b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:260:8"
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
      "definition_site": "008814fc",
      "incomplete_value": true,
      "site": "0088150c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008814a4",
      "incomplete_value": true,
      "site": "008814b4",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00881500",
      "incomplete_value": true,
      "site": "00881510",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008814a8",
      "incomplete_value": true,
      "site": "008814b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00881444",
      "READ",
      [
        "storage",
        "002ba8ab",
        null,
        "string"
      ]
    ],
    [
      "00881448",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "00881480",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "00881444",
      "READ",
      [
        "storage",
        "002ba857",
        null,
        "string"
      ]
    ],
    [
      "00881448",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "00881480",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00881428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/008813b0.md#insn-00881428) · [`00881460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/008813b0.md#insn-00881460) · [`00881484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/008813b0.md#insn-00881484)
- 新版 `00881480`（命令位置の公開資料なし） · `008814b8`（命令位置の公開資料なし） · `008814dc`（命令位置の公開資料なし）

~~~diff
- 00881428 ["INT_ADD", "register:40f0:8", ["const:881428:8", "const:4:8"]]
- 00881428 ["CALL", null, ["ram:48ccf8:8"]]
+ 00881480 ["INT_ADD", "register:40f0:8", ["const:881480:8", "const:4:8"]]
+ 00881480 ["CALL", null, ["ram:48cd38:8"]]
- 00881428 bytes 342ef097
+ 00881480 bytes 2e2ef097
- 00881460 ["INT_ADD", "register:40f0:8", ["const:881460:8", "const:4:8"]]
- 00881460 ["CALL", null, ["callee:00492d44:8"]]
+ 008814b8 ["INT_ADD", "register:40f0:8", ["const:8814b8:8", "const:4:8"]]
+ 008814b8 ["CALL", null, ["callee:00492d44:8"]]
- 00881460 bytes 2946f097
+ 008814b8 bytes 2346f097
- 00881484 ["INT_ADD", "register:40f0:8", ["const:881484:8", "const:4:8"]]
- 00881484 ["CALL", null, ["ram:48ccf8:8"]]
+ 008814dc ["INT_ADD", "register:40f0:8", ["const:8814dc:8", "const:4:8"]]
+ 008814dc ["CALL", null, ["ram:48cd38:8"]]
- 00881484 bytes 1d2ef097
+ 008814dc bytes 172ef097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c71adbad235d4cd0c70a62af1807327"></a>

### [`00881584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881584.md) → [`008815dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008815dc.md) FUN_008815dc

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00484210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00484250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484250.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.80% / 新版 82.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00881628",
      "incomplete_value": true,
      "site": "00881628",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:857:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008815d0",
      "incomplete_value": true,
      "site": "008815d0",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:8ab:8"
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
      "definition_site": "008816cc",
      "incomplete_value": true,
      "site": "008816dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:20c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00881674",
      "incomplete_value": true,
      "site": "00881684",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:260:8"
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
      "definition_site": "008816d0",
      "incomplete_value": true,
      "site": "008816e0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00881678",
      "incomplete_value": true,
      "site": "00881688",
      "value": [
        "LOAD",
        "16",
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
      "00881618",
      "READ",
      [
        "storage",
        "002ba8ab",
        null,
        "string"
      ]
    ],
    [
      "0088161c",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "00881654",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "00881618",
      "READ",
      [
        "storage",
        "002ba857",
        null,
        "string"
      ]
    ],
    [
      "0088161c",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "00881654",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008815fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881584.md#insn-008815fc) · [`00881634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881584.md#insn-00881634) · [`00881658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881584.md#insn-00881658)
- 新版 `00881654`（命令位置の公開資料なし） · `0088168c`（命令位置の公開資料なし） · `008816b0`（命令位置の公開資料なし）

~~~diff
- 008815fc ["INT_ADD", "register:40f0:8", ["const:8815fc:8", "const:4:8"]]
- 008815fc ["CALL", null, ["ram:48ccf8:8"]]
+ 00881654 ["INT_ADD", "register:40f0:8", ["const:881654:8", "const:4:8"]]
+ 00881654 ["CALL", null, ["ram:48cd38:8"]]
- 008815fc bytes bf2df097
+ 00881654 bytes b92df097
- 00881634 ["INT_ADD", "register:40f0:8", ["const:881634:8", "const:4:8"]]
- 00881634 ["CALL", null, ["callee:00492d44:8"]]
+ 0088168c ["INT_ADD", "register:40f0:8", ["const:88168c:8", "const:4:8"]]
+ 0088168c ["CALL", null, ["callee:00492d44:8"]]
- 00881634 bytes b445f097
+ 0088168c bytes ae45f097
- 00881658 ["INT_ADD", "register:40f0:8", ["const:881658:8", "const:4:8"]]
- 00881658 ["CALL", null, ["ram:48ccf8:8"]]
+ 008816b0 ["INT_ADD", "register:40f0:8", ["const:8816b0:8", "const:4:8"]]
+ 008816b0 ["CALL", null, ["ram:48cd38:8"]]
- 00881658 bytes a82df097
+ 008816b0 bytes a22df097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77e676dc9fcb5a6f8aac8c43a9c56328"></a>

### [`00881758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md) → [`008817b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008817b0.md) FUN_008817b0

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`0045440c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md) [`00456324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md) [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`0045444c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/0045444c.md) [`00456364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456364.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008819c4",
      "incomplete_value": false,
      "site": "008819c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088196c",
      "incomplete_value": false,
      "site": "0088196c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00881a94",
      "incomplete_value": false,
      "site": "00881a98",
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
                "const:c65000:8"
              ],
              [
                "leaf",
                "const:600:8"
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
      "definition_site": "00881a3c",
      "incomplete_value": false,
      "site": "00881a40",
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
                "const:c65000:8"
              ],
              [
                "leaf",
                "const:530:8"
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008817f0",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00881798",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "008817ec",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "008817f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0088180c",
      "READ",
      [
        "storage",
        "002a15cd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008817ec",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "008817f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0088180c",
      "READ",
      [
        "storage",
        "002a1580",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00881798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md#insn-00881798) · [`0088181c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md#insn-0088181c) · [`008818a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md#insn-008818a4)
- 新版 `008817f0`（命令位置の公開資料なし） · `00881874`（命令位置の公開資料なし） · `008818fc`（命令位置の公開資料なし）

~~~diff
- 00881798 ["INT_ADD", "register:40f0:8", ["const:881798:8", "const:4:8"]]
- 00881798 ["CALL", null, ["ram:48ccf8:8"]]
+ 008817f0 ["INT_ADD", "register:40f0:8", ["const:8817f0:8", "const:4:8"]]
+ 008817f0 ["CALL", null, ["ram:48cd38:8"]]
- 00881798 bytes 582df097
+ 008817f0 bytes 522df097
- 0088181c ["INT_ADD", "register:40f0:8", ["const:88181c:8", "const:4:8"]]
- 0088181c ["CALL", null, ["ram:48ccf8:8"]]
+ 00881874 ["INT_ADD", "register:40f0:8", ["const:881874:8", "const:4:8"]]
+ 00881874 ["CALL", null, ["ram:48cd38:8"]]
- 0088181c bytes 372df097
+ 00881874 bytes 312df097
- 008818a4 ["INT_ADD", "register:40f0:8", ["const:8818a4:8", "const:4:8"]]
- 008818a4 ["CALL", null, ["callee:004820ec:8"]]
+ 008818fc ["INT_ADD", "register:40f0:8", ["const:8818fc:8", "const:4:8"]]
+ 008818fc ["CALL", null, ["callee:004820ec:8"]]
- 008818a4 bytes 0202f097
+ 008818fc bytes fc01f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53c4ceeef6ae7c463512b09eac2d2846"></a>

### [`00881c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881c7c.md) → [`00881cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881cd4.md) FUN_00881cd4

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00881d10",
      "incomplete_value": true,
      "site": "00881d24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:507:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00881cb8",
      "incomplete_value": true,
      "site": "00881ccc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:554:8"
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
      "site": "00881d00",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00881ca8",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "site": "00881d64",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00881d0c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "00881cfc",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "00881d00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00881d10",
      "READ",
      [
        "storage",
        "002a2554",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00881cfc",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "00881d00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "00881d10",
      "READ",
      [
        "storage",
        "002a2507",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00881ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881c7c.md#insn-00881ca8) · [`00881d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881c7c.md#insn-00881d0c) · [`00881c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881c7c.md#insn-00881c98)
- 新版 `00881d00`（命令位置の公開資料なし） · `00881d64`（命令位置の公開資料なし） · `00881cf0`（命令位置の公開資料なし）

~~~diff
- 00881ca8 ["INT_ADD", "register:40f0:8", ["const:881ca8:8", "const:4:8"]]
- 00881ca8 ["CALL", null, ["ram:48ccf8:8"]]
+ 00881d00 ["INT_ADD", "register:40f0:8", ["const:881d00:8", "const:4:8"]]
+ 00881d00 ["CALL", null, ["ram:48cd38:8"]]
- 00881ca8 bytes 142cf097
+ 00881d00 bytes 0e2cf097
- 00881d0c ["INT_ADD", "register:40f0:8", ["const:881d0c:8", "const:4:8"]]
- 00881d0c ["CALL", null, ["ram:48ccf8:8"]]
+ 00881d64 ["INT_ADD", "register:40f0:8", ["const:881d64:8", "const:4:8"]]
+ 00881d64 ["CALL", null, ["ram:48cd38:8"]]
- 00881d0c bytes fb2bf097
+ 00881d64 bytes f52bf097
- 00881c98 ["INT_ADD", "register:40f0:8", ["const:881c98:8", "const:4:8"]]
- 00881c98 ["CALL", null, ["callee:00851550:8"]]
+ 00881cf0 ["INT_ADD", "register:40f0:8", ["const:881cf0:8", "const:4:8"]]
+ 00881cf0 ["CALL", null, ["callee:00851550:8"]]
- 00881c98 bytes 183eff97
+ 00881cf0 bytes 183eff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-894d1f1570af3ec47625f61ead49fd1b"></a>

### [`00882170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882170.md) → [`008821c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008821c8.md) FUN_008821c8

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0086d67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d67c.md) · 呼出先 5件 [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0086d6d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d6d4.md) · 呼出先 5件 [`00764f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.15% / 新版 98.15%

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
      "site": "00882240",
      "value": [
        "leaf",
        "ram:764f38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008821e8",
      "value": [
        "leaf",
        "ram:764ee0:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00882208",
      "DATA",
      [
        "storage",
        "003c7788",
        "fde_003c7788",
        "dword"
      ]
    ],
    [
      "00882228",
      "DATA",
      [
        "storage",
        "003c7788",
        "fde_003c7788",
        "dword"
      ]
    ],
    [
      "00882240",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ]
  ],
  "added": [
    [
      "00882208",
      "DATA",
      [
        "storage",
        "003c7788",
        null,
        "dword"
      ]
    ],
    [
      "00882228",
      "DATA",
      [
        "storage",
        "003c7788",
        null,
        "dword"
      ]
    ],
    [
      "00882240",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764f38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882170.md#insn-00882190) · [`008821e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882170.md#insn-008821e8) · [`008821a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882170.md#insn-008821a4)
- 新版 `008821e8`（命令位置の公開資料なし） · `00882240`（命令位置の公開資料なし） · `008821fc`（命令位置の公開資料なし）

~~~diff
- 00882190 ["INT_ADD", "register:40f0:8", ["const:882190:8", "const:4:8"]]
- 00882190 ["CALL", null, ["callee:00851550:8"]]
+ 008821e8 ["INT_ADD", "register:40f0:8", ["const:8821e8:8", "const:4:8"]]
+ 008821e8 ["CALL", null, ["callee:00851550:8"]]
- 00882190 bytes da3cff97
+ 008821e8 bytes da3cff97
- 008821e8 ["INT_ADD", "register:40f0:8", ["const:8821e8:8", "const:4:8"]]
- 008821e8 ["CALL", null, ["ram:764ee0:8"]]
+ 00882240 ["INT_ADD", "register:40f0:8", ["const:882240:8", "const:4:8"]]
+ 00882240 ["CALL", null, ["ram:764f38:8"]]
- 008821e8 bytes 3e8bfb97
+ 00882240 bytes 3e8bfb97
- 008821a4 ["INT_ADD", "register:40f0:8", ["const:8821a4:8", "const:4:8"]]
- 008821a4 ["CALL", null, ["callee:00851550:8"]]
+ 008821fc ["INT_ADD", "register:40f0:8", ["const:8821fc:8", "const:4:8"]]
+ 008821fc ["CALL", null, ["callee:00851550:8"]]
- 008821a4 bytes d53cff97
+ 008821fc bytes d53cff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71e597c20e28876a23bd21113d765701"></a>

### [`00882440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882440.md) → [`00882498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882498.md) FUN_00882498

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "008824a4",
      "incomplete_value": false,
      "site": "008824b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088244c",
      "incomplete_value": false,
      "site": "00882458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "008824b0",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008824b0",
      "DATA",
      [
        "storage",
        "00c807e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088244c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882440.md#insn-0088244c)
- 新版 `008824a4`（命令位置の公開資料なし）

~~~diff
- 0088244c ["COPY", "tmp:0:8", ["const:718:8"]]
- 0088244c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0088244c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0088244c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008824a4 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 008824a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008824a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008824a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0088244c bytes 4a611c91
+ 008824a4 bytes 4aa11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ba741a50d6dd05268285ac70160f7e3"></a>

### [`00882484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882484.md) → [`008824dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008824dc.md) FUN_008824dc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "008824f4",
      "incomplete_value": false,
      "site": "00882500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088249c",
      "incomplete_value": false,
      "site": "008824a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "00882500",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882500",
      "DATA",
      [
        "storage",
        "00c807e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088249c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882484.md#insn-0088249c) · [`008824cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882484.md#insn-008824cc)
- 新版 `008824f4`（命令位置の公開資料なし） · `00882524`（命令位置の公開資料なし）

~~~diff
- 0088249c ["COPY", "tmp:0:8", ["const:718:8"]]
- 0088249c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088249c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088249c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008824f4 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 008824f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008824f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008824f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088249c bytes 08611c91
+ 008824f4 bytes 08a11f91
- 008824cc ["COPY", "register:0:8", ["register:4040:8"]]
- 008824cc ["INT_ADD", "register:40f0:8", ["const:8824cc:8", "const:4:8"]]
- 008824cc ["CALLIND", null, ["register:0:8"]]
+ 00882524 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00882524 ["INT_ADD", "register:40f0:8", ["const:882524:8", "const:4:8"]]
+ 00882524 ["CALLIND", null, ["register:0:8"]]
- 008824cc bytes 00013fd6
+ 00882524 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cbb40a0703216485e9355da9a7464c6"></a>

### [`008824e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008824e0.md) → [`00882538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882538.md) FUN_00882538

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00882564",
      "incomplete_value": false,
      "site": "00882564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088250c",
      "incomplete_value": false,
      "site": "0088250c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "00882564",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882564",
      "DATA",
      [
        "storage",
        "00c807e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008824f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008824e0.md#insn-008824f4) · [`00882504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008824e0.md#insn-00882504) · [`00882528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008824e0.md#insn-00882528)
- 新版 `0088254c`（命令位置の公開資料なし） · `0088255c`（命令位置の公開資料なし） · `00882580`（命令位置の公開資料なし）

~~~diff
- 008824f4 ["INT_ADD", "register:40f0:8", ["const:8824f4:8", "const:4:8"]]
- 008824f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088254c ["INT_ADD", "register:40f0:8", ["const:88254c:8", "const:4:8"]]
+ 0088254c ["CALL", null, ["callee:00c57f60:8"]]
- 008824f4 bytes 67560f94
+ 0088254c bytes 85560f94
- 00882504 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00882504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00882504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00882504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088255c ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 0088255c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088255c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088255c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00882504 bytes 08611c91
+ 0088255c bytes 08a11f91
- 00882528 ["COPY", "register:0:8", ["register:4040:8"]]
- 00882528 ["INT_ADD", "register:40f0:8", ["const:882528:8", "const:4:8"]]
- 00882528 ["CALLIND", null, ["register:0:8"]]
+ 00882580 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00882580 ["INT_ADD", "register:40f0:8", ["const:882580:8", "const:4:8"]]
+ 00882580 ["CALLIND", null, ["register:0:8"]]
- 00882528 bytes 00013fd6
+ 00882580 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc47d9cc57c390c72b4284e170b1a345"></a>

### [`00882568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882568.md) → [`008825c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008825c0.md) FUN_008825c0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "008825dc",
      "incomplete_value": false,
      "site": "008825dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882584",
      "incomplete_value": false,
      "site": "00882584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "008825dc",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008825dc",
      "DATA",
      [
        "storage",
        "00c807e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882568.md#insn-00882580) · [`008825a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882568.md#insn-008825a4)
- 新版 `008825d8`（命令位置の公開資料なし） · `008825fc`（命令位置の公開資料なし）

~~~diff
- 00882580 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00882580 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00882580 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00882580 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008825d8 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 008825d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008825d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008825d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00882580 bytes 29611c91
+ 008825d8 bytes 29a11f91
- 008825a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 008825a4 ["INT_ADD", "register:40f0:8", ["const:8825a4:8", "const:4:8"]]
- 008825a4 ["CALLIND", null, ["register:0:8"]]
+ 008825fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 008825fc ["INT_ADD", "register:40f0:8", ["const:8825fc:8", "const:4:8"]]
+ 008825fc ["CALLIND", null, ["register:0:8"]]
- 008825a4 bytes 20013fd6
+ 008825fc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb9b3bc5bdfa418279ca067826d0df46"></a>

### [`008826a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008826a8.md) → [`00882700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882700.md) FUN_00882700

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
      "definition_site": "00882714",
      "incomplete_value": false,
      "site": "00882718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008826bc",
      "incomplete_value": false,
      "site": "008826c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "00882718",
      "DATA",
      [
        "storage",
        "00c80798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882718",
      "DATA",
      [
        "storage",
        "00c80868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008826b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008826a8.md#insn-008826b4) · [`008826bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008826a8.md#insn-008826bc)
- 新版 `0088270c`（命令位置の公開資料なし） · `00882714`（命令位置の公開資料なし）

~~~diff
- 008826b4 ["INT_ADD", "register:40f0:8", ["const:8826b4:8", "const:4:8"]]
- 008826b4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088270c ["INT_ADD", "register:40f0:8", ["const:88270c:8", "const:4:8"]]
+ 0088270c ["CALL", null, ["callee:00c57f60:8"]]
- 008826b4 bytes f7550f94
+ 0088270c bytes 15560f94
- 008826bc ["COPY", "tmp:0:8", ["const:798:8"]]
- 008826bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008826bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008826bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00882714 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 00882714 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00882714 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00882714 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008826bc bytes 08611e91
+ 00882714 bytes 08a12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f23fbe76b2299c721df9cbf1fcf3daef"></a>

### [`008826cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008826cc.md) → [`00882724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882724.md) FUN_00882724

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
      "definition_site": "00882728",
      "incomplete_value": false,
      "site": "0088272c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008826d0",
      "incomplete_value": false,
      "site": "008826d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "0088272c",
      "DATA",
      [
        "storage",
        "00c80798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088272c",
      "DATA",
      [
        "storage",
        "00c80868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008826d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008826cc.md#insn-008826d0)
- 新版 `00882728`（命令位置の公開資料なし）

~~~diff
- 008826d0 ["COPY", "tmp:0:8", ["const:798:8"]]
- 008826d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008826d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008826d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00882728 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 00882728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00882728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00882728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008826d0 bytes 08611e91
+ 00882728 bytes 08a12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed9e6e1781e3999dabfc32a5a1991a3c"></a>

### [`008826e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008826e4.md) → [`0088273c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088273c.md) FUN_0088273c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.35% / 新版 91.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00882778",
      "incomplete_value": true,
      "site": "00882780",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00882720",
      "incomplete_value": true,
      "site": "00882728",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:240:8"
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
      "definition_site": "00882774",
      "incomplete_value": true,
      "site": "00882784",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:74a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088271c",
      "incomplete_value": true,
      "site": "0088272c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:70a:8"
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
      "definition_site": "00882774",
      "incomplete_value": true,
      "site": "00882784",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0088271c",
      "incomplete_value": true,
      "site": "0088272c",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00882758",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00882774",
      "READ",
      [
        "storage",
        "002b670a",
        null,
        "string"
      ]
    ],
    [
      "00882774",
      "READ",
      [
        "storage",
        "002b671a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00882758",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "00882774",
      "READ",
      [
        "storage",
        "002b674a",
        null,
        "string"
      ]
    ],
    [
      "00882774",
      "READ",
      [
        "storage",
        "002b675a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008826e4.md#insn-00882700) · [`00882790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008826e4.md#insn-00882790) · [`0088270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008826e4.md#insn-0088270c)
- 新版 `00882758`（命令位置の公開資料なし） · `008827e8`（命令位置の公開資料なし） · `00882764`（命令位置の公開資料なし）

~~~diff
- 00882700 ["INT_ADD", "register:40f0:8", ["const:882700:8", "const:4:8"]]
- 00882700 ["CALL", null, ["ram:48ccf8:8"]]
+ 00882758 ["INT_ADD", "register:40f0:8", ["const:882758:8", "const:4:8"]]
+ 00882758 ["CALL", null, ["ram:48cd38:8"]]
- 00882700 bytes 7e29f097
+ 00882758 bytes 7829f097
- 00882790 ["INT_ADD", "register:40f0:8", ["const:882790:8", "const:4:8"]]
- 00882790 ["CALL", null, ["callee:0043bb60:8"]]
+ 008827e8 ["INT_ADD", "register:40f0:8", ["const:8827e8:8", "const:4:8"]]
+ 008827e8 ["CALL", null, ["callee:0043bb60:8"]]
- 00882790 bytes e4e4ee97
+ 008827e8 bytes dee4ee97
- 0088270c ["INT_ADD", "register:40f0:8", ["const:88270c:8", "const:4:8"]]
- 0088270c ["CALL", null, ["callee:00c57f60:8"]]
+ 00882764 ["INT_ADD", "register:40f0:8", ["const:882764:8", "const:4:8"]]
+ 00882764 ["CALL", null, ["callee:00c57f60:8"]]
- 0088270c bytes e1550f94
+ 00882764 bytes ff550f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27f0fef01b0e16acb21863c67a78c2d3"></a>

### [`00882964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882964.md) → [`008829bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829bc.md) FUN_008829bc

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
      "definition_site": "008829d0",
      "incomplete_value": false,
      "site": "008829d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882978",
      "incomplete_value": false,
      "site": "0088297c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:818:8"
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
      "008829d4",
      "DATA",
      [
        "storage",
        "00c80818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008829d4",
      "DATA",
      [
        "storage",
        "00c808e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882964.md#insn-00882970) · [`00882978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882964.md#insn-00882978)
- 新版 `008829c8`（命令位置の公開資料なし） · `008829d0`（命令位置の公開資料なし）

~~~diff
- 00882970 ["INT_ADD", "register:40f0:8", ["const:882970:8", "const:4:8"]]
- 00882970 ["CALL", null, ["callee:00c57f60:8"]]
+ 008829c8 ["INT_ADD", "register:40f0:8", ["const:8829c8:8", "const:4:8"]]
+ 008829c8 ["CALL", null, ["callee:00c57f60:8"]]
- 00882970 bytes 48550f94
+ 008829c8 bytes 66550f94
- 00882978 ["COPY", "tmp:0:8", ["const:818:8"]]
- 00882978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00882978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00882978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008829d0 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 008829d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008829d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008829d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00882978 bytes 08612091
+ 008829d0 bytes 08a12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75e633bb3b73707ce924c48e70f83b02"></a>

### [`00882988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882988.md) → [`008829e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829e0.md) FUN_008829e0

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
      "definition_site": "008829e4",
      "incomplete_value": false,
      "site": "008829e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088298c",
      "incomplete_value": false,
      "site": "00882990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:818:8"
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
      "008829e8",
      "DATA",
      [
        "storage",
        "00c80818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008829e8",
      "DATA",
      [
        "storage",
        "00c808e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088298c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882988.md#insn-0088298c)
- 新版 `008829e4`（命令位置の公開資料なし）

~~~diff
- 0088298c ["COPY", "tmp:0:8", ["const:818:8"]]
- 0088298c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088298c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088298c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008829e4 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 008829e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008829e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008829e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088298c bytes 08612091
+ 008829e4 bytes 08a12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-950105beed5cfe59ef94bf72bdd4d534"></a>

### [`008829a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008829a0.md) → [`008829f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829f8.md) FUN_008829f8

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.35% / 新版 91.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00882a34",
      "incomplete_value": true,
      "site": "00882a3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "008829dc",
      "incomplete_value": true,
      "site": "008829e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:240:8"
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
      "definition_site": "00882a30",
      "incomplete_value": true,
      "site": "00882a40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4fd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008829d8",
      "incomplete_value": true,
      "site": "008829e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:551:8"
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
      "definition_site": "00882a30",
      "incomplete_value": true,
      "site": "00882a40",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008829d8",
      "incomplete_value": true,
      "site": "008829e8",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00882a14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00882a30",
      "READ",
      [
        "storage",
        "002b9551",
        null,
        "string"
      ]
    ],
    [
      "00882a30",
      "READ",
      [
        "storage",
        "002b9561",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00882a14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "00882a30",
      "READ",
      [
        "storage",
        "002b94fd",
        null,
        "string"
      ]
    ],
    [
      "00882a30",
      "READ",
      [
        "storage",
        "002b950d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008829bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008829a0.md#insn-008829bc) · [`00882a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008829a0.md#insn-00882a4c) · [`008829c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008829a0.md#insn-008829c8)
- 新版 `00882a14`（命令位置の公開資料なし） · `00882aa4`（命令位置の公開資料なし） · `00882a20`（命令位置の公開資料なし）

~~~diff
- 008829bc ["INT_ADD", "register:40f0:8", ["const:8829bc:8", "const:4:8"]]
- 008829bc ["CALL", null, ["ram:48ccf8:8"]]
+ 00882a14 ["INT_ADD", "register:40f0:8", ["const:882a14:8", "const:4:8"]]
+ 00882a14 ["CALL", null, ["ram:48cd38:8"]]
- 008829bc bytes cf28f097
+ 00882a14 bytes c928f097
- 00882a4c ["INT_ADD", "register:40f0:8", ["const:882a4c:8", "const:4:8"]]
- 00882a4c ["CALL", null, ["callee:0043bb60:8"]]
+ 00882aa4 ["INT_ADD", "register:40f0:8", ["const:882aa4:8", "const:4:8"]]
+ 00882aa4 ["CALL", null, ["callee:0043bb60:8"]]
- 00882a4c bytes 35e4ee97
+ 00882aa4 bytes 2fe4ee97
- 008829c8 ["INT_ADD", "register:40f0:8", ["const:8829c8:8", "const:4:8"]]
- 008829c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00882a20 ["INT_ADD", "register:40f0:8", ["const:882a20:8", "const:4:8"]]
+ 00882a20 ["CALL", null, ["callee:00c57f60:8"]]
- 008829c8 bytes 32550f94
+ 00882a20 bytes 50550f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29a6baf4557c34db8701eb1c3ba7c684"></a>

### [`00882c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882c1c.md) → [`00882c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882c74.md) FUN_00882c74

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00882c7c",
      "incomplete_value": false,
      "site": "00882c80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882c24",
      "incomplete_value": false,
      "site": "00882c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00882c80",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882c80",
      "DATA",
      [
        "storage",
        "00c80968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882c1c.md#insn-00882c24)
- 新版 `00882c7c`（命令位置の公開資料なし）

~~~diff
- 00882c24 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00882c24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00882c24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00882c24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00882c7c ["COPY", "tmp:0:8", ["const:968:8"]]
+ 00882c7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00882c7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00882c7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00882c24 bytes 29612291
+ 00882c7c bytes 29a12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef922a952bc96ee779bcea927ac3f912"></a>

### [`00882c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882c3c.md) → [`00882c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882c94.md) FUN_00882c94

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00882c9c",
      "incomplete_value": false,
      "site": "00882ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882c44",
      "incomplete_value": false,
      "site": "00882c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00882ca0",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882ca0",
      "DATA",
      [
        "storage",
        "00c80968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882c3c.md#insn-00882c44) · [`00882c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882c3c.md#insn-00882c68)
- 新版 `00882c9c`（命令位置の公開資料なし） · `00882cc0`（命令位置の公開資料なし）

~~~diff
- 00882c44 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00882c44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00882c44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00882c44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00882c9c ["COPY", "tmp:0:8", ["const:968:8"]]
+ 00882c9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00882c9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00882c9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00882c44 bytes 29612291
+ 00882c9c bytes 29a12591
- 00882c68 ["INT_ADD", "register:40f0:8", ["const:882c68:8", "const:4:8"]]
- 00882c68 ["CALL", null, ["callee:00c57f80:8"]]
+ 00882cc0 ["INT_ADD", "register:40f0:8", ["const:882cc0:8", "const:4:8"]]
+ 00882cc0 ["CALL", null, ["callee:00c57f80:8"]]
- 00882c68 bytes 92540f94
+ 00882cc0 bytes b0540f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c40e24a555571c7f0d9c69b375762c33"></a>

### [`00882c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882c7c.md) → [`00882cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882cd4.md) FUN_00882cd4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00882d00",
      "incomplete_value": false,
      "site": "00882d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882ca8",
      "incomplete_value": false,
      "site": "00882ca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00882d00",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882d00",
      "DATA",
      [
        "storage",
        "00c80968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882c7c.md#insn-00882c90) · [`00882ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882c7c.md#insn-00882ca0) · [`00882cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882c7c.md#insn-00882cc8)
- 新版 `00882ce8`（命令位置の公開資料なし） · `00882cf8`（命令位置の公開資料なし） · `00882d20`（命令位置の公開資料なし）

~~~diff
- 00882c90 ["INT_ADD", "register:40f0:8", ["const:882c90:8", "const:4:8"]]
- 00882c90 ["CALL", null, ["callee:00c57f60:8"]]
+ 00882ce8 ["INT_ADD", "register:40f0:8", ["const:882ce8:8", "const:4:8"]]
+ 00882ce8 ["CALL", null, ["callee:00c57f60:8"]]
- 00882c90 bytes 80540f94
+ 00882ce8 bytes 9e540f94
- 00882ca0 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00882ca0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00882ca0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00882ca0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00882cf8 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 00882cf8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00882cf8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00882cf8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00882ca0 bytes 4a612291
+ 00882cf8 bytes 4aa12591
- 00882cc8 ["INT_ADD", "register:40f0:8", ["const:882cc8:8", "const:4:8"]]
- 00882cc8 ["CALL", null, ["callee:0043bb60:8"]]
+ 00882d20 ["INT_ADD", "register:40f0:8", ["const:882d20:8", "const:4:8"]]
+ 00882d20 ["CALL", null, ["callee:0043bb60:8"]]
- 00882cc8 bytes 96e3ee97
+ 00882d20 bytes 90e3ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60b1a091b92b9546b2e5efe4c91084a1"></a>

### [`00882cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882cf0.md) → [`00882d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882d48.md) FUN_00882d48

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

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
      "definition_site": "00882d50",
      "incomplete_value": false,
      "site": "00882d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882cf8",
      "incomplete_value": false,
      "site": "00882cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00882d50",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882d50",
      "DATA",
      [
        "storage",
        "00c80968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882cf0.md#insn-00882cf4)
- 新版 `00882d4c`（命令位置の公開資料なし）

~~~diff
- 00882cf4 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00882cf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00882cf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00882cf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00882d4c ["COPY", "tmp:0:8", ["const:968:8"]]
+ 00882d4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00882d4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00882d4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00882cf4 bytes 08612291
+ 00882d4c bytes 08a12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61e29f017955be8bc3c45d45117ecf38"></a>

### [`00882d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882d74.md) → [`00882dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882dcc.md) FUN_00882dcc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

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
      "site": "00882df0",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00882d98",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "00882df0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "00882df0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882d74.md#insn-00882d98) · [`00882da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882d74.md#insn-00882da8) · [`00882db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882d74.md#insn-00882db4)
- 新版 `00882df0`（命令位置の公開資料なし） · `00882e00`（命令位置の公開資料なし） · `00882e0c`（命令位置の公開資料なし）

~~~diff
- 00882d98 ["INT_ADD", "register:40f0:8", ["const:882d98:8", "const:4:8"]]
- 00882d98 ["CALL", null, ["ram:48ccf8:8"]]
+ 00882df0 ["INT_ADD", "register:40f0:8", ["const:882df0:8", "const:4:8"]]
+ 00882df0 ["CALL", null, ["ram:48cd38:8"]]
- 00882d98 bytes d827f097
+ 00882df0 bytes d227f097
- 00882da8 ["INT_ADD", "register:40f0:8", ["const:882da8:8", "const:4:8"]]
- 00882da8 ["CALL", null, ["callee:0048ce94:8"]]
+ 00882e00 ["INT_ADD", "register:40f0:8", ["const:882e00:8", "const:4:8"]]
+ 00882e00 ["CALL", null, ["callee:0048ce94:8"]]
- 00882da8 bytes 2b28f097
+ 00882e00 bytes 2528f097
- 00882db4 ["INT_ADD", "register:40f0:8", ["const:882db4:8", "const:4:8"]]
- 00882db4 ["CALL", null, ["callee:00492f68:8"]]
+ 00882e0c ["INT_ADD", "register:40f0:8", ["const:882e0c:8", "const:4:8"]]
+ 00882e0c ["CALL", null, ["callee:00492f68:8"]]
- 00882db4 bytes 5d40f097
+ 00882e0c bytes 5740f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2257bbae22cc237413563293e3baed85"></a>

### [`00882e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882e48.md) → [`00882ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882ea0.md) FUN_00882ea0

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
      "definition_site": "00882eb4",
      "incomplete_value": false,
      "site": "00882eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882e5c",
      "incomplete_value": false,
      "site": "00882e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:918:8"
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
      "00882eb8",
      "DATA",
      [
        "storage",
        "00c80918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882eb8",
      "DATA",
      [
        "storage",
        "00c809e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882e48.md#insn-00882e54) · [`00882e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882e48.md#insn-00882e5c)
- 新版 `00882eac`（命令位置の公開資料なし） · `00882eb4`（命令位置の公開資料なし）

~~~diff
- 00882e54 ["INT_ADD", "register:40f0:8", ["const:882e54:8", "const:4:8"]]
- 00882e54 ["CALL", null, ["callee:00c57f60:8"]]
+ 00882eac ["INT_ADD", "register:40f0:8", ["const:882eac:8", "const:4:8"]]
+ 00882eac ["CALL", null, ["callee:00c57f60:8"]]
- 00882e54 bytes 0f540f94
+ 00882eac bytes 2d540f94
- 00882e5c ["COPY", "tmp:0:8", ["const:918:8"]]
- 00882e5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00882e5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00882e5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00882eb4 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00882eb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00882eb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00882eb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00882e5c bytes 08612491
+ 00882eb4 bytes 08a12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2915919fa9651190afc34dba168aa4bc"></a>

### [`00882e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882e6c.md) → [`00882ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882ec4.md) FUN_00882ec4

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
      "definition_site": "00882ec8",
      "incomplete_value": false,
      "site": "00882ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882e70",
      "incomplete_value": false,
      "site": "00882e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:918:8"
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
      "00882ecc",
      "DATA",
      [
        "storage",
        "00c80918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882ecc",
      "DATA",
      [
        "storage",
        "00c809e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882e6c.md#insn-00882e70)
- 新版 `00882ec8`（命令位置の公開資料なし）

~~~diff
- 00882e70 ["COPY", "tmp:0:8", ["const:918:8"]]
- 00882e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00882e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00882e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00882ec8 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00882ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00882ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00882ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00882e70 bytes 08612491
+ 00882ec8 bytes 08a12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e50394d9cabf2faf9a521b3c83127ee2"></a>

### [`00882e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882e84.md) → [`00882edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882edc.md) FUN_00882edc

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.20% / 新版 93.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00882f14",
      "incomplete_value": true,
      "site": "00882f28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882ebc",
      "incomplete_value": true,
      "site": "00882ed0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:690:8"
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
      "definition_site": "00882f20",
      "incomplete_value": true,
      "site": "00882f2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882ec8",
      "incomplete_value": true,
      "site": "00882ed4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c40:8"
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
      "definition_site": "00882f20",
      "incomplete_value": true,
      "site": "00882f2c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00882ec8",
      "incomplete_value": true,
      "site": "00882ed4",
      "value": [
        "LOAD",
        "16",
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
      "00882ef8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00882f14",
      "READ",
      [
        "storage",
        "002c2690",
        null,
        null
      ]
    ],
    [
      "00882f20",
      "READ",
      [
        "storage",
        "002bcc40",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00882ef8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "00882f14",
      "READ",
      [
        "storage",
        "002c26d0",
        null,
        null
      ]
    ],
    [
      "00882f20",
      "READ",
      [
        "storage",
        "002bcbec",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882e84.md#insn-00882ea0) · [`00882f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882e84.md#insn-00882f2c) · [`00882eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882e84.md#insn-00882eac)
- 新版 `00882ef8`（命令位置の公開資料なし） · `00882f84`（命令位置の公開資料なし） · `00882f04`（命令位置の公開資料なし）

~~~diff
- 00882ea0 ["INT_ADD", "register:40f0:8", ["const:882ea0:8", "const:4:8"]]
- 00882ea0 ["CALL", null, ["ram:48ccf8:8"]]
+ 00882ef8 ["INT_ADD", "register:40f0:8", ["const:882ef8:8", "const:4:8"]]
+ 00882ef8 ["CALL", null, ["ram:48cd38:8"]]
- 00882ea0 bytes 9627f097
+ 00882ef8 bytes 9027f097
- 00882f2c ["INT_ADD", "register:40f0:8", ["const:882f2c:8", "const:4:8"]]
- 00882f2c ["CALL", null, ["callee:0043bb60:8"]]
+ 00882f84 ["INT_ADD", "register:40f0:8", ["const:882f84:8", "const:4:8"]]
+ 00882f84 ["CALL", null, ["callee:0043bb60:8"]]
- 00882f2c bytes fde2ee97
+ 00882f84 bytes f7e2ee97
- 00882eac ["INT_ADD", "register:40f0:8", ["const:882eac:8", "const:4:8"]]
- 00882eac ["CALL", null, ["callee:00c57f60:8"]]
+ 00882f04 ["INT_ADD", "register:40f0:8", ["const:882f04:8", "const:4:8"]]
+ 00882f04 ["CALL", null, ["callee:00c57f60:8"]]
- 00882eac bytes f9530f94
+ 00882f04 bytes 17540f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1c45a758e57f177daca895d197194f2"></a>

### [`00883100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883100.md) → [`00883158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883158.md) FUN_00883158

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
      "definition_site": "00883178",
      "incomplete_value": false,
      "site": "0088317c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883120",
      "incomplete_value": false,
      "site": "00883124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "0088317c",
      "DATA",
      [
        "storage",
        "00c80998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088317c",
      "DATA",
      [
        "storage",
        "00c80a68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883100.md#insn-00883114) · [`00883120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883100.md#insn-00883120)
- 新版 `0088316c`（命令位置の公開資料なし） · `00883178`（命令位置の公開資料なし）

~~~diff
- 00883114 ["INT_ADD", "register:40f0:8", ["const:883114:8", "const:4:8"]]
- 00883114 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088316c ["INT_ADD", "register:40f0:8", ["const:88316c:8", "const:4:8"]]
+ 0088316c ["CALL", null, ["callee:00c57f60:8"]]
- 00883114 bytes 5f530f94
+ 0088316c bytes 7d530f94
- 00883120 ["COPY", "tmp:0:8", ["const:998:8"]]
- 00883120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00883120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00883120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00883178 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 00883178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00883178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00883178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00883120 bytes 08612691
+ 00883178 bytes 08a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-570fc23fddd0dee794c130337b53d7b0"></a>

### [`00883138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883138.md) → [`00883190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883190.md) FUN_00883190

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
      "definition_site": "00883198",
      "incomplete_value": false,
      "site": "0088319c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883140",
      "incomplete_value": false,
      "site": "00883144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "0088319c",
      "DATA",
      [
        "storage",
        "00c80998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088319c",
      "DATA",
      [
        "storage",
        "00c80a68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883138.md#insn-00883140)
- 新版 `00883198`（命令位置の公開資料なし）

~~~diff
- 00883140 ["COPY", "tmp:0:8", ["const:998:8"]]
- 00883140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00883140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00883140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00883198 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 00883198 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00883198 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00883198 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00883140 bytes 29612691
+ 00883198 bytes 29a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a6225b8bcfead630de4c516fc2aa0d7"></a>

### [`00883158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883158.md) → [`008831b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008831b0.md) FUN_008831b0

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`004932dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004932dc.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0049331c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/0049331c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.88% / 新版 93.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00883210",
      "incomplete_value": true,
      "site": "00883210",
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
                "const:576:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008831b8",
      "incomplete_value": true,
      "site": "008831b8",
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
                "const:5c3:8"
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
      "definition_site": "00883218",
      "incomplete_value": true,
      "site": "00883218",
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008831c0",
      "incomplete_value": true,
      "site": "008831c0",
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
                "const:fc2:8"
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
      "site": "00883328",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008832d0",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "00883204",
      "READ",
      [
        "storage",
        "002a15c3",
        null,
        "string"
      ]
    ],
    [
      "00883208",
      "READ",
      [
        "storage",
        "002affc2",
        null,
        "string"
      ]
    ],
    [
      "00883328",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "00883204",
      "READ",
      [
        "storage",
        "002a1576",
        null,
        "string"
      ]
    ],
    [
      "00883208",
      "READ",
      [
        "storage",
        "002aff66",
        null,
        "string"
      ]
    ],
    [
      "00883328",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883158.md#insn-00883218) · [`008832d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883158.md#insn-008832d0) · [`00883194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883158.md#insn-00883194)
- 新版 `00883270`（命令位置の公開資料なし） · `00883328`（命令位置の公開資料なし） · `008831ec`（命令位置の公開資料なし）

~~~diff
- 00883218 ["INT_ADD", "register:40f0:8", ["const:883218:8", "const:4:8"]]
- 00883218 ["CALL", null, ["callee:0043bb60:8"]]
+ 00883270 ["INT_ADD", "register:40f0:8", ["const:883270:8", "const:4:8"]]
+ 00883270 ["CALL", null, ["callee:0043bb60:8"]]
- 00883218 bytes 42e2ee97
+ 00883270 bytes 3ce2ee97
- 008832d0 ["INT_ADD", "register:40f0:8", ["const:8832d0:8", "const:4:8"]]
- 008832d0 ["CALL", null, ["ram:48ccf8:8"]]
+ 00883328 ["INT_ADD", "register:40f0:8", ["const:883328:8", "const:4:8"]]
+ 00883328 ["CALL", null, ["ram:48cd38:8"]]
- 008832d0 bytes 8a26f097
+ 00883328 bytes 8426f097
- 00883194 ["COPY", "tmp:0:8", ["const:fc2:8"]]
- 00883194 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00883194 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00883194 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008831ec ["COPY", "tmp:0:8", ["const:f66:8"]]
+ 008831ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008831ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008831ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00883194 bytes 29093f91
+ 008831ec bytes 29993d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-275a710d83126cc469c03f704eea793b"></a>

### [`00883618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883618.md) → [`00883670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883670.md) FUN_00883670

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
      "definition_site": "00883684",
      "incomplete_value": false,
      "site": "00883688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088362c",
      "incomplete_value": false,
      "site": "00883630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a08:8"
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
      "00883688",
      "DATA",
      [
        "storage",
        "00c80a08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883688",
      "DATA",
      [
        "storage",
        "00c80ad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883618.md#insn-00883624) · [`0088362c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883618.md#insn-0088362c)
- 新版 `0088367c`（命令位置の公開資料なし） · `00883684`（命令位置の公開資料なし）

~~~diff
- 00883624 ["INT_ADD", "register:40f0:8", ["const:883624:8", "const:4:8"]]
- 00883624 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088367c ["INT_ADD", "register:40f0:8", ["const:88367c:8", "const:4:8"]]
+ 0088367c ["CALL", null, ["callee:00c57f60:8"]]
- 00883624 bytes 1b520f94
+ 0088367c bytes 39520f94
- 0088362c ["COPY", "tmp:0:8", ["const:a08:8"]]
- 0088362c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088362c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088362c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00883684 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 00883684 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00883684 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00883684 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088362c bytes 08212891
+ 00883684 bytes 08612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d7406ef38c3e9e1745cee5f2a66b881"></a>

### [`0088363c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/0088363c.md) → [`00883694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883694.md) FUN_00883694

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
      "definition_site": "00883698",
      "incomplete_value": false,
      "site": "0088369c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883640",
      "incomplete_value": false,
      "site": "00883644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "0088369c",
      "DATA",
      [
        "storage",
        "00c80a08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088369c",
      "DATA",
      [
        "storage",
        "00c80ad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/0088363c.md#insn-00883640)
- 新版 `00883698`（命令位置の公開資料なし）

~~~diff
- 00883640 ["COPY", "tmp:0:8", ["const:a08:8"]]
- 00883640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00883640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00883640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00883698 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 00883698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00883698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00883698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00883640 bytes 08212891
+ 00883698 bytes 08612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9619a0032c47b26e4d610265c7e431e5"></a>

### [`00883654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883654.md) → [`008836ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008836ac.md) FUN_008836ac

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048dc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0048dca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dca0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008836f0",
      "incomplete_value": true,
      "site": "008836f0",
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
    "old": {
      "definition_site": "00883698",
      "incomplete_value": true,
      "site": "00883698",
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
                "const:edf:8"
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
      "site": "008836c8",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00883670",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "008836c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "008836dc",
      "READ",
      [
        "storage",
        "002a9edf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008836c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "008836dc",
      "READ",
      [
        "storage",
        "002a9e83",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883654.md#insn-00883670) · [`0088367c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883654.md#insn-0088367c) · [`008836a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883654.md#insn-008836a4)
- 新版 `008836c8`（命令位置の公開資料なし） · `008836d4`（命令位置の公開資料なし） · `008836fc`（命令位置の公開資料なし）

~~~diff
- 00883670 ["INT_ADD", "register:40f0:8", ["const:883670:8", "const:4:8"]]
- 00883670 ["CALL", null, ["ram:48ccf8:8"]]
+ 008836c8 ["INT_ADD", "register:40f0:8", ["const:8836c8:8", "const:4:8"]]
+ 008836c8 ["CALL", null, ["ram:48cd38:8"]]
- 00883670 bytes a225f097
+ 008836c8 bytes 9c25f097
- 0088367c ["COPY", "tmp:0:8", ["const:edf:8"]]
- 0088367c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088367c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088367c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008836d4 ["COPY", "tmp:0:8", ["const:e83:8"]]
+ 008836d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008836d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008836d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088367c bytes 297d3b91
+ 008836d4 bytes 290d3a91
- 008836a4 ["INT_ADD", "register:40f0:8", ["const:8836a4:8", "const:4:8"]]
- 008836a4 ["CALL", null, ["callee:0048ce94:8"]]
+ 008836fc ["INT_ADD", "register:40f0:8", ["const:8836fc:8", "const:4:8"]]
+ 008836fc ["CALL", null, ["callee:0048ce94:8"]]
- 008836a4 bytes ec25f097
+ 008836fc bytes e625f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37c31ccde5261162a86054005d4917ec"></a>

### [`00883764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883764.md) → [`008837bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008837bc.md) FUN_008837bc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "008837d4",
      "incomplete_value": false,
      "site": "008837e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088377c",
      "incomplete_value": false,
      "site": "00883788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "008837e0",
      "DATA",
      [
        "storage",
        "00c80a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008837e0",
      "DATA",
      [
        "storage",
        "00c80b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008837e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883764.md#insn-008837e0) · [`0088377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883764.md#insn-0088377c) · [`008837ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883764.md#insn-008837ac)
- 新版 `00883838`（命令位置の公開資料なし） · `008837d4`（命令位置の公開資料なし） · `00883804`（命令位置の公開資料なし）

~~~diff
- 008837e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008837e0 ["INT_ADD", "register:40f0:8", ["const:8837e0:8", "const:4:8"]]
- 008837e0 ["CALLIND", null, ["register:0:8"]]
+ 00883838 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883838 ["INT_ADD", "register:40f0:8", ["const:883838:8", "const:4:8"]]
+ 00883838 ["CALLIND", null, ["register:0:8"]]
- 008837e0 bytes 00013fd6
+ 00883838 bytes 00013fd6
- 0088377c ["COPY", "tmp:0:8", ["const:a98:8"]]
- 0088377c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088377c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088377c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008837d4 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 008837d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008837d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008837d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088377c bytes 08612a91
+ 008837d4 bytes 08a12d91
- 008837ac ["COPY", "register:0:8", ["register:4040:8"]]
- 008837ac ["INT_ADD", "register:40f0:8", ["const:8837ac:8", "const:4:8"]]
- 008837ac ["CALLIND", null, ["register:0:8"]]
+ 00883804 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883804 ["INT_ADD", "register:40f0:8", ["const:883804:8", "const:4:8"]]
+ 00883804 ["CALLIND", null, ["register:0:8"]]
- 008837ac bytes 00013fd6
+ 00883804 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18e552168a4c2318f6b97d3e17efb52c"></a>

### [`008837f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/008837f4.md) → [`0088384c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/0088384c.md) FUN_0088384c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00883864",
      "incomplete_value": false,
      "site": "00883870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088380c",
      "incomplete_value": false,
      "site": "00883818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "00883870",
      "DATA",
      [
        "storage",
        "00c80a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883870",
      "DATA",
      [
        "storage",
        "00c80b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088380c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/008837f4.md#insn-0088380c) · [`0088383c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/008837f4.md#insn-0088383c) · [`00883850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/008837f4.md#insn-00883850)
- 新版 `00883864`（命令位置の公開資料なし） · `00883894`（命令位置の公開資料なし） · `008838a8`（命令位置の公開資料なし）

~~~diff
- 0088380c ["COPY", "tmp:0:8", ["const:a98:8"]]
- 0088380c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088380c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088380c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00883864 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 00883864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00883864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00883864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088380c bytes 08612a91
+ 00883864 bytes 08a12d91
- 0088383c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088383c ["INT_ADD", "register:40f0:8", ["const:88383c:8", "const:4:8"]]
- 0088383c ["CALLIND", null, ["register:0:8"]]
+ 00883894 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883894 ["INT_ADD", "register:40f0:8", ["const:883894:8", "const:4:8"]]
+ 00883894 ["CALLIND", null, ["register:0:8"]]
- 0088383c bytes 00013fd6
+ 00883894 bytes 00013fd6
- 00883850 ["INT_ADD", "register:40f0:8", ["const:883850:8", "const:4:8"]]
- 00883850 ["CALL", null, ["callee:00c53da0:8"]]
+ 008838a8 ["INT_ADD", "register:40f0:8", ["const:8838a8:8", "const:4:8"]]
+ 008838a8 ["CALL", null, ["callee:00c53da0:8"]]
- 00883850 bytes 2c410f94
+ 008838a8 bytes 3e410f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8166997e213ced220fca2110df7fca0d"></a>

### [`00883930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883930.md) → [`00883988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883988.md) FUN_00883988

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "008839a4",
      "incomplete_value": false,
      "site": "008839b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088394c",
      "incomplete_value": false,
      "site": "00883958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "008839b0",
      "DATA",
      [
        "storage",
        "00c80a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008839b0",
      "DATA",
      [
        "storage",
        "00c80b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088394c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883930.md#insn-0088394c) · [`0088396c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883930.md#insn-0088396c) · [`0088398c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883930.md#insn-0088398c)
- 新版 `008839a4`（命令位置の公開資料なし） · `008839c4`（命令位置の公開資料なし） · `008839e4`（命令位置の公開資料なし）

~~~diff
- 0088394c ["COPY", "tmp:0:8", ["const:a98:8"]]
- 0088394c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088394c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088394c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008839a4 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 008839a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008839a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008839a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088394c bytes 29612a91
+ 008839a4 bytes 29a12d91
- 0088396c ["INT_ADD", "register:40f0:8", ["const:88396c:8", "const:4:8"]]
- 0088396c ["CALL", null, ["callee:00c53d70:8"]]
+ 008839c4 ["INT_ADD", "register:40f0:8", ["const:8839c4:8", "const:4:8"]]
+ 008839c4 ["CALL", null, ["callee:00c53d70:8"]]
- 0088396c bytes d9400f94
+ 008839c4 bytes eb400f94
- 0088398c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088398c ["INT_ADD", "register:40f0:8", ["const:88398c:8", "const:4:8"]]
- 0088398c ["CALLIND", null, ["register:0:8"]]
+ 008839e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008839e4 ["INT_ADD", "register:40f0:8", ["const:8839e4:8", "const:4:8"]]
+ 008839e4 ["CALLIND", null, ["register:0:8"]]
- 0088398c bytes 00013fd6
+ 008839e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93e38df39157901d18e7fd454251f370"></a>

### [`00883ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883ad4.md) → [`00883b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883b2c.md) FUN_00883b2c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`007687f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007687f0.md) [`00768be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768be8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00768848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768848.md) [`00768c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768c40.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00880d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00883d28",
      "incomplete_value": false,
      "site": "00883d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883cd0",
      "incomplete_value": false,
      "site": "00883cd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "definition_site": "00883dd4",
      "incomplete_value": false,
      "site": "00883ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883d7c",
      "incomplete_value": false,
      "site": "00883d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00883bd8",
      "value": [
        "leaf",
        "ram:768c40:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00883b80",
      "value": [
        "leaf",
        "ram:768be8:8"
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
      "00883bd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768be8"
      ]
    ],
    [
      "00883d30",
      "DATA",
      [
        "storage",
        "00c80b98",
        null,
        "undefined *"
      ]
    ],
    [
      "00883ddc",
      "DATA",
      [
        "storage",
        "00c80b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883bd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768c40"
      ]
    ],
    [
      "00883d30",
      "DATA",
      [
        "storage",
        "00c80c68",
        null,
        "undefined *"
      ]
    ],
    [
      "00883ddc",
      "DATA",
      [
        "storage",
        "00c80be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883ad4.md#insn-00883b80) · [`00883b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883ad4.md#insn-00883b3c) · [`00883b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883ad4.md#insn-00883b78)
- 新版 `00883bd8`（命令位置の公開資料なし） · `00883b94`（命令位置の公開資料なし） · `00883bd0`（命令位置の公開資料なし）

~~~diff
- 00883b80 ["INT_ADD", "register:40f0:8", ["const:883b80:8", "const:4:8"]]
- 00883b80 ["CALL", null, ["ram:768be8:8"]]
+ 00883bd8 ["INT_ADD", "register:40f0:8", ["const:883bd8:8", "const:4:8"]]
+ 00883bd8 ["CALL", null, ["ram:768c40:8"]]
- 00883b80 bytes 1a94fb97
+ 00883bd8 bytes 1a94fb97
- 00883b3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00883b3c ["INT_ADD", "register:40f0:8", ["const:883b3c:8", "const:4:8"]]
- 00883b3c ["CALLIND", null, ["register:0:8"]]
+ 00883b94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883b94 ["INT_ADD", "register:40f0:8", ["const:883b94:8", "const:4:8"]]
+ 00883b94 ["CALLIND", null, ["register:0:8"]]
- 00883b3c bytes 00013fd6
+ 00883b94 bytes 00013fd6
- 00883b78 ["INT_ADD", "register:40f0:8", ["const:883b78:8", "const:4:8"]]
- 00883b78 ["CALL", null, ["callee:00851550:8"]]
+ 00883bd0 ["INT_ADD", "register:40f0:8", ["const:883bd0:8", "const:4:8"]]
+ 00883bd0 ["CALL", null, ["callee:00851550:8"]]
- 00883b78 bytes 6036ff97
+ 00883bd0 bytes 6036ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2724aa7294f6464c312ea251bd0c42c0"></a>

### [`008840ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008840ac.md) → [`00884104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884104.md) FUN_00884104

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "0088411c",
      "incomplete_value": false,
      "site": "00884128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008840c4",
      "incomplete_value": false,
      "site": "008840d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "00884128",
      "DATA",
      [
        "storage",
        "00c80b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00884128",
      "DATA",
      [
        "storage",
        "00c80be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008840ac.md#insn-00884128) · [`008840c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008840ac.md#insn-008840c4) · [`008840f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008840ac.md#insn-008840f4)
- 新版 `00884180`（命令位置の公開資料なし） · `0088411c`（命令位置の公開資料なし） · `0088414c`（命令位置の公開資料なし）

~~~diff
- 00884128 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884128 ["INT_ADD", "register:40f0:8", ["const:884128:8", "const:4:8"]]
- 00884128 ["CALLIND", null, ["register:0:8"]]
+ 00884180 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884180 ["INT_ADD", "register:40f0:8", ["const:884180:8", "const:4:8"]]
+ 00884180 ["CALLIND", null, ["register:0:8"]]
- 00884128 bytes 00013fd6
+ 00884180 bytes 00013fd6
- 008840c4 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 008840c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008840c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008840c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088411c ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 0088411c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088411c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088411c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008840c4 bytes 08612c91
+ 0088411c bytes 08a12f91
- 008840f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008840f4 ["INT_ADD", "register:40f0:8", ["const:8840f4:8", "const:4:8"]]
- 008840f4 ["CALLIND", null, ["register:0:8"]]
+ 0088414c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088414c ["INT_ADD", "register:40f0:8", ["const:88414c:8", "const:4:8"]]
+ 0088414c ["CALLIND", null, ["register:0:8"]]
- 008840f4 bytes 00013fd6
+ 0088414c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91631dc2386b2b64197eb9d973033700"></a>

### [`0088413c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/0088413c.md) → [`00884194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884194.md) FUN_00884194

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "008841ac",
      "incomplete_value": false,
      "site": "008841b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884154",
      "incomplete_value": false,
      "site": "00884160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "008841b8",
      "DATA",
      [
        "storage",
        "00c80b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008841b8",
      "DATA",
      [
        "storage",
        "00c80be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/0088413c.md#insn-00884154) · [`00884184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/0088413c.md#insn-00884184) · [`00884198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/0088413c.md#insn-00884198)
- 新版 `008841ac`（命令位置の公開資料なし） · `008841dc`（命令位置の公開資料なし） · `008841f0`（命令位置の公開資料なし）

~~~diff
- 00884154 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 00884154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00884154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00884154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008841ac ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 008841ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008841ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008841ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00884154 bytes 08612c91
+ 008841ac bytes 08a12f91
- 00884184 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884184 ["INT_ADD", "register:40f0:8", ["const:884184:8", "const:4:8"]]
- 00884184 ["CALLIND", null, ["register:0:8"]]
+ 008841dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008841dc ["INT_ADD", "register:40f0:8", ["const:8841dc:8", "const:4:8"]]
+ 008841dc ["CALLIND", null, ["register:0:8"]]
- 00884184 bytes 00013fd6
+ 008841dc bytes 00013fd6
- 00884198 ["INT_ADD", "register:40f0:8", ["const:884198:8", "const:4:8"]]
- 00884198 ["CALL", null, ["callee:00c53da0:8"]]
+ 008841f0 ["INT_ADD", "register:40f0:8", ["const:8841f0:8", "const:4:8"]]
+ 008841f0 ["CALL", null, ["callee:00c53da0:8"]]
- 00884198 bytes da3e0f94
+ 008841f0 bytes ec3e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-628906a2c187955356cca0b85c0d40b3"></a>

### [`008841c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008841c8.md) → [`00884220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884220.md) FUN_00884220

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00884248",
      "incomplete_value": false,
      "site": "0088424c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008841f0",
      "incomplete_value": false,
      "site": "008841f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "0088424c",
      "DATA",
      [
        "storage",
        "00c80b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088424c",
      "DATA",
      [
        "storage",
        "00c80be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008841dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008841c8.md#insn-008841dc) · [`008841f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008841c8.md#insn-008841f0) · [`0088420c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008841c8.md#insn-0088420c)
- 新版 `00884234`（命令位置の公開資料なし） · `00884248`（命令位置の公開資料なし） · `00884264`（命令位置の公開資料なし）

~~~diff
- 008841dc ["INT_ADD", "register:40f0:8", ["const:8841dc:8", "const:4:8"]]
- 008841dc ["CALL", null, ["callee:00c57f60:8"]]
+ 00884234 ["INT_ADD", "register:40f0:8", ["const:884234:8", "const:4:8"]]
+ 00884234 ["CALL", null, ["callee:00c57f60:8"]]
- 008841dc bytes 2d4f0f94
+ 00884234 bytes 4b4f0f94
- 008841f0 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 008841f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008841f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008841f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00884248 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00884248 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00884248 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00884248 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008841f0 bytes 29612c91
+ 00884248 bytes 29a12f91
- 0088420c ["INT_ADD", "register:40f0:8", ["const:88420c:8", "const:4:8"]]
- 0088420c ["CALL", null, ["callee:00c53d70:8"]]
+ 00884264 ["INT_ADD", "register:40f0:8", ["const:884264:8", "const:4:8"]]
+ 00884264 ["CALL", null, ["callee:00c53d70:8"]]
- 0088420c bytes b13e0f94
+ 00884264 bytes c33e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2966c1a7991681e057b974577e2ea66a"></a>

### [`00884278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884278.md) → [`008842d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008842d0.md) FUN_008842d0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "008842ec",
      "incomplete_value": false,
      "site": "008842f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884294",
      "incomplete_value": false,
      "site": "008842a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "008842f8",
      "DATA",
      [
        "storage",
        "00c80b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008842f8",
      "DATA",
      [
        "storage",
        "00c80be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884278.md#insn-00884294) · [`008842b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884278.md#insn-008842b4) · [`008842d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884278.md#insn-008842d4)
- 新版 `008842ec`（命令位置の公開資料なし） · `0088430c`（命令位置の公開資料なし） · `0088432c`（命令位置の公開資料なし）

~~~diff
- 00884294 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 00884294 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00884294 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00884294 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008842ec ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 008842ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008842ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008842ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00884294 bytes 29612c91
+ 008842ec bytes 29a12f91
- 008842b4 ["INT_ADD", "register:40f0:8", ["const:8842b4:8", "const:4:8"]]
- 008842b4 ["CALL", null, ["callee:00c53d70:8"]]
+ 0088430c ["INT_ADD", "register:40f0:8", ["const:88430c:8", "const:4:8"]]
+ 0088430c ["CALL", null, ["callee:00c53d70:8"]]
- 008842b4 bytes 873e0f94
+ 0088430c bytes 993e0f94
- 008842d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008842d4 ["INT_ADD", "register:40f0:8", ["const:8842d4:8", "const:4:8"]]
- 008842d4 ["CALLIND", null, ["register:0:8"]]
+ 0088432c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088432c ["INT_ADD", "register:40f0:8", ["const:88432c:8", "const:4:8"]]
+ 0088432c ["CALLIND", null, ["register:0:8"]]
- 008842d4 bytes 00013fd6
+ 0088432c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9522594b74c6b8e1871e29ab3155166"></a>

### [`00884458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884458.md) → [`008844b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008844b0.md) FUN_008844b0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "008844c8",
      "incomplete_value": false,
      "site": "008844d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884470",
      "incomplete_value": false,
      "site": "0088447c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "008844d4",
      "DATA",
      [
        "storage",
        "00c80b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008844d4",
      "DATA",
      [
        "storage",
        "00c80c68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008844d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884458.md#insn-008844d4) · [`00884470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884458.md#insn-00884470) · [`008844a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884458.md#insn-008844a0)
- 新版 `0088452c`（命令位置の公開資料なし） · `008844c8`（命令位置の公開資料なし） · `008844f8`（命令位置の公開資料なし）

~~~diff
- 008844d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008844d4 ["INT_ADD", "register:40f0:8", ["const:8844d4:8", "const:4:8"]]
- 008844d4 ["CALLIND", null, ["register:0:8"]]
+ 0088452c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088452c ["INT_ADD", "register:40f0:8", ["const:88452c:8", "const:4:8"]]
+ 0088452c ["CALLIND", null, ["register:0:8"]]
- 008844d4 bytes 00013fd6
+ 0088452c bytes 00013fd6
- 00884470 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 00884470 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00884470 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00884470 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008844c8 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 008844c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008844c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008844c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00884470 bytes 08612e91
+ 008844c8 bytes 08a13191
- 008844a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008844a0 ["INT_ADD", "register:40f0:8", ["const:8844a0:8", "const:4:8"]]
- 008844a0 ["CALLIND", null, ["register:0:8"]]
+ 008844f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008844f8 ["INT_ADD", "register:40f0:8", ["const:8844f8:8", "const:4:8"]]
+ 008844f8 ["CALLIND", null, ["register:0:8"]]
- 008844a0 bytes 00013fd6
+ 008844f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbaa2a3ed7c79fde5625b5bdbf34d8da"></a>

### [`008844e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008844e8.md) → [`00884540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884540.md) FUN_00884540

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00884558",
      "incomplete_value": false,
      "site": "00884564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884500",
      "incomplete_value": false,
      "site": "0088450c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "00884564",
      "DATA",
      [
        "storage",
        "00c80b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00884564",
      "DATA",
      [
        "storage",
        "00c80c68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008844e8.md#insn-00884500) · [`00884530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008844e8.md#insn-00884530) · [`00884544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008844e8.md#insn-00884544)
- 新版 `00884558`（命令位置の公開資料なし） · `00884588`（命令位置の公開資料なし） · `0088459c`（命令位置の公開資料なし）

~~~diff
- 00884500 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 00884500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00884500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00884500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00884558 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 00884558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00884558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00884558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00884500 bytes 08612e91
+ 00884558 bytes 08a13191
- 00884530 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884530 ["INT_ADD", "register:40f0:8", ["const:884530:8", "const:4:8"]]
- 00884530 ["CALLIND", null, ["register:0:8"]]
+ 00884588 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884588 ["INT_ADD", "register:40f0:8", ["const:884588:8", "const:4:8"]]
+ 00884588 ["CALLIND", null, ["register:0:8"]]
- 00884530 bytes 00013fd6
+ 00884588 bytes 00013fd6
- 00884544 ["INT_ADD", "register:40f0:8", ["const:884544:8", "const:4:8"]]
- 00884544 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088459c ["INT_ADD", "register:40f0:8", ["const:88459c:8", "const:4:8"]]
+ 0088459c ["CALL", null, ["callee:00c53da0:8"]]
- 00884544 bytes ef3d0f94
+ 0088459c bytes 013e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64aa3b062c4cf88ccb3f0a290b52d84f"></a>

### [`00884574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884574.md) → [`008845cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008845cc.md) FUN_008845cc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008845f4",
      "incomplete_value": false,
      "site": "008845f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088459c",
      "incomplete_value": false,
      "site": "008845a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "008845f8",
      "DATA",
      [
        "storage",
        "00c80b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008845f8",
      "DATA",
      [
        "storage",
        "00c80c68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884574.md#insn-00884588) · [`0088459c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884574.md#insn-0088459c) · [`008845b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884574.md#insn-008845b8)
- 新版 `008845e0`（命令位置の公開資料なし） · `008845f4`（命令位置の公開資料なし） · `00884610`（命令位置の公開資料なし）

~~~diff
- 00884588 ["INT_ADD", "register:40f0:8", ["const:884588:8", "const:4:8"]]
- 00884588 ["CALL", null, ["callee:00c57f60:8"]]
+ 008845e0 ["INT_ADD", "register:40f0:8", ["const:8845e0:8", "const:4:8"]]
+ 008845e0 ["CALL", null, ["callee:00c57f60:8"]]
- 00884588 bytes 424e0f94
+ 008845e0 bytes 604e0f94
- 0088459c ["COPY", "tmp:0:8", ["const:b98:8"]]
- 0088459c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088459c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088459c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008845f4 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 008845f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008845f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008845f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088459c bytes 29612e91
+ 008845f4 bytes 29a13191
- 008845b8 ["INT_ADD", "register:40f0:8", ["const:8845b8:8", "const:4:8"]]
- 008845b8 ["CALL", null, ["callee:00c53d70:8"]]
+ 00884610 ["INT_ADD", "register:40f0:8", ["const:884610:8", "const:4:8"]]
+ 00884610 ["CALL", null, ["callee:00c53d70:8"]]
- 008845b8 bytes c63d0f94
+ 00884610 bytes d83d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-234dbf06990e35cb0d5f886879a63f97"></a>

### [`00884804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884804.md) → [`0088485c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/0088485c.md) FUN_0088485c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00884874",
      "incomplete_value": false,
      "site": "00884880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088481c",
      "incomplete_value": false,
      "site": "00884828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "00884880",
      "DATA",
      [
        "storage",
        "00c80c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00884880",
      "DATA",
      [
        "storage",
        "00c80cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884804.md#insn-00884880) · [`0088481c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884804.md#insn-0088481c) · [`0088484c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884804.md#insn-0088484c)
- 新版 `008848d8`（命令位置の公開資料なし） · `00884874`（命令位置の公開資料なし） · `008848a4`（命令位置の公開資料なし）

~~~diff
- 00884880 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884880 ["INT_ADD", "register:40f0:8", ["const:884880:8", "const:4:8"]]
- 00884880 ["CALLIND", null, ["register:0:8"]]
+ 008848d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008848d8 ["INT_ADD", "register:40f0:8", ["const:8848d8:8", "const:4:8"]]
+ 008848d8 ["CALLIND", null, ["register:0:8"]]
- 00884880 bytes 00013fd6
+ 008848d8 bytes 00013fd6
- 0088481c ["COPY", "tmp:0:8", ["const:c28:8"]]
- 0088481c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088481c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088481c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00884874 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00884874 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00884874 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00884874 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088481c bytes 08a13091
+ 00884874 bytes 08e13391
- 0088484c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088484c ["INT_ADD", "register:40f0:8", ["const:88484c:8", "const:4:8"]]
- 0088484c ["CALLIND", null, ["register:0:8"]]
+ 008848a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008848a4 ["INT_ADD", "register:40f0:8", ["const:8848a4:8", "const:4:8"]]
+ 008848a4 ["CALLIND", null, ["register:0:8"]]
- 0088484c bytes 00013fd6
+ 008848a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa53640586dd25b16f1fad27a37a5078"></a>

### [`00884894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884894.md) → [`008848ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008848ec.md) FUN_008848ec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00884904",
      "incomplete_value": false,
      "site": "00884910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008848ac",
      "incomplete_value": false,
      "site": "008848b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "00884910",
      "DATA",
      [
        "storage",
        "00c80c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00884910",
      "DATA",
      [
        "storage",
        "00c80cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008848ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884894.md#insn-008848ac) · [`008848dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884894.md#insn-008848dc) · [`008848f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884894.md#insn-008848f0)
- 新版 `00884904`（命令位置の公開資料なし） · `00884934`（命令位置の公開資料なし） · `00884948`（命令位置の公開資料なし）

~~~diff
- 008848ac ["COPY", "tmp:0:8", ["const:c28:8"]]
- 008848ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008848ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008848ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00884904 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00884904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00884904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00884904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008848ac bytes 08a13091
+ 00884904 bytes 08e13391
- 008848dc ["COPY", "register:0:8", ["register:4040:8"]]
- 008848dc ["INT_ADD", "register:40f0:8", ["const:8848dc:8", "const:4:8"]]
- 008848dc ["CALLIND", null, ["register:0:8"]]
+ 00884934 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884934 ["INT_ADD", "register:40f0:8", ["const:884934:8", "const:4:8"]]
+ 00884934 ["CALLIND", null, ["register:0:8"]]
- 008848dc bytes 00013fd6
+ 00884934 bytes 00013fd6
- 008848f0 ["INT_ADD", "register:40f0:8", ["const:8848f0:8", "const:4:8"]]
- 008848f0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00884948 ["INT_ADD", "register:40f0:8", ["const:884948:8", "const:4:8"]]
+ 00884948 ["CALL", null, ["callee:00c53da0:8"]]
- 008848f0 bytes 043d0f94
+ 00884948 bytes 163d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57fea1b1f0a81158263a3d1dcfbf34af"></a>

### [`00884920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884920.md) → [`00884978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884978.md) FUN_00884978

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008849a0",
      "incomplete_value": false,
      "site": "008849a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884948",
      "incomplete_value": false,
      "site": "0088494c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "008849a4",
      "DATA",
      [
        "storage",
        "00c80c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008849a4",
      "DATA",
      [
        "storage",
        "00c80cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884920.md#insn-00884934) · [`00884948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884920.md#insn-00884948) · [`00884964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884920.md#insn-00884964)
- 新版 `0088498c`（命令位置の公開資料なし） · `008849a0`（命令位置の公開資料なし） · `008849bc`（命令位置の公開資料なし）

~~~diff
- 00884934 ["INT_ADD", "register:40f0:8", ["const:884934:8", "const:4:8"]]
- 00884934 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088498c ["INT_ADD", "register:40f0:8", ["const:88498c:8", "const:4:8"]]
+ 0088498c ["CALL", null, ["callee:00c57f60:8"]]
- 00884934 bytes 574d0f94
+ 0088498c bytes 754d0f94
- 00884948 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00884948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00884948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00884948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008849a0 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 008849a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008849a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008849a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00884948 bytes 29a13091
+ 008849a0 bytes 29e13391
- 00884964 ["INT_ADD", "register:40f0:8", ["const:884964:8", "const:4:8"]]
- 00884964 ["CALL", null, ["callee:00c53d70:8"]]
+ 008849bc ["INT_ADD", "register:40f0:8", ["const:8849bc:8", "const:4:8"]]
+ 008849bc ["CALL", null, ["callee:00c53d70:8"]]
- 00884964 bytes db3c0f94
+ 008849bc bytes ed3c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5f0663cdf0a662319330c81f519d178"></a>

### [`008849d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008849d0.md) → [`00884a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884a28.md) FUN_00884a28

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "00884a44",
      "incomplete_value": false,
      "site": "00884a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008849ec",
      "incomplete_value": false,
      "site": "008849f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "00884a50",
      "DATA",
      [
        "storage",
        "00c80c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00884a50",
      "DATA",
      [
        "storage",
        "00c80cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008849ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008849d0.md#insn-008849ec) · [`00884a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008849d0.md#insn-00884a0c) · [`00884a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008849d0.md#insn-00884a2c)
- 新版 `00884a44`（命令位置の公開資料なし） · `00884a64`（命令位置の公開資料なし） · `00884a84`（命令位置の公開資料なし）

~~~diff
- 008849ec ["COPY", "tmp:0:8", ["const:c28:8"]]
- 008849ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008849ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008849ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00884a44 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00884a44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00884a44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00884a44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008849ec bytes 29a13091
+ 00884a44 bytes 29e13391
- 00884a0c ["INT_ADD", "register:40f0:8", ["const:884a0c:8", "const:4:8"]]
- 00884a0c ["CALL", null, ["callee:00c53d70:8"]]
+ 00884a64 ["INT_ADD", "register:40f0:8", ["const:884a64:8", "const:4:8"]]
+ 00884a64 ["CALL", null, ["callee:00c53d70:8"]]
- 00884a0c bytes b13c0f94
+ 00884a64 bytes c33c0f94
- 00884a2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00884a2c ["INT_ADD", "register:40f0:8", ["const:884a2c:8", "const:4:8"]]
- 00884a2c ["CALLIND", null, ["register:0:8"]]
+ 00884a84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884a84 ["INT_ADD", "register:40f0:8", ["const:884a84:8", "const:4:8"]]
+ 00884a84 ["CALLIND", null, ["register:0:8"]]
- 00884a2c bytes 00013fd6
+ 00884a84 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56a60dffd783a6d50cca3014928bd077"></a>

### [`00884b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884b74.md) → [`00884bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884bcc.md) FUN_00884bcc

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`007681b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007681b4.md) [`007687f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007687f0.md) [`00768be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768be8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0076820c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/0076820c.md) [`00768848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768848.md) [`00768c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768c40.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.56% / 新版 98.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00884de0",
      "incomplete_value": false,
      "site": "00884de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884d88",
      "incomplete_value": false,
      "site": "00884d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00884c34",
      "value": [
        "leaf",
        "ram:768c40:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00884bdc",
      "value": [
        "leaf",
        "ram:768be8:8"
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
      "00884c34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768be8"
      ]
    ],
    [
      "00884c70",
      "DATA",
      [
        "storage",
        "003c76c0",
        null,
        "byte[11]"
      ]
    ],
    [
      "00884c78",
      "DATA",
      [
        "storage",
        "003c76c0",
        null,
        "byte[11]"
      ]
    ]
  ],
  "added": [
    [
      "00884c34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768c40"
      ]
    ],
    [
      "00884c70",
      "DATA",
      [
        "storage",
        "003c76c0",
        null,
        "byte[15]"
      ]
    ],
    [
      "00884c78",
      "DATA",
      [
        "storage",
        "003c76c0",
        null,
        "byte[15]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884b74.md#insn-00884bdc) · [`00884bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884b74.md#insn-00884bc8) · [`00884bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884b74.md#insn-00884bd0)
- 新版 `00884c34`（命令位置の公開資料なし） · `00884c20`（命令位置の公開資料なし） · `00884c28`（命令位置の公開資料なし）

~~~diff
- 00884bdc ["INT_ADD", "register:40f0:8", ["const:884bdc:8", "const:4:8"]]
- 00884bdc ["CALL", null, ["ram:768be8:8"]]
+ 00884c34 ["INT_ADD", "register:40f0:8", ["const:884c34:8", "const:4:8"]]
+ 00884c34 ["CALL", null, ["ram:768c40:8"]]
- 00884bdc bytes 0390fb97
+ 00884c34 bytes 0390fb97
- 00884bc8 ["INT_ADD", "register:40f0:8", ["const:884bc8:8", "const:4:8"]]
- 00884bc8 ["CALL", null, ["callee:00851550:8"]]
+ 00884c20 ["INT_ADD", "register:40f0:8", ["const:884c20:8", "const:4:8"]]
+ 00884c20 ["CALL", null, ["callee:00851550:8"]]
- 00884bc8 bytes 4c32ff97
+ 00884c20 bytes 4c32ff97
- 00884bd0 ["INT_ADD", "register:40f0:8", ["const:884bd0:8", "const:4:8"]]
- 00884bd0 ["CALL", null, ["callee:00768848:8"]]
+ 00884c28 ["INT_ADD", "register:40f0:8", ["const:884c28:8", "const:4:8"]]
+ 00884c28 ["CALL", null, ["callee:00768848:8"]]
- 00884bd0 bytes 088ffb97
+ 00884c28 bytes 088ffb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6faf107d820fe9990c4e9b5a5538d17a"></a>

### [`00884ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884ff8.md) → [`00885050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885050.md) FUN_00885050

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00885068",
      "incomplete_value": false,
      "site": "00885074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885010",
      "incomplete_value": false,
      "site": "0088501c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "00885074",
      "DATA",
      [
        "storage",
        "00c80c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885074",
      "DATA",
      [
        "storage",
        "00c80d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884ff8.md#insn-00885074) · [`00885010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884ff8.md#insn-00885010) · [`00885040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884ff8.md#insn-00885040)
- 新版 `008850cc`（命令位置の公開資料なし） · `00885068`（命令位置の公開資料なし） · `00885098`（命令位置の公開資料なし）

~~~diff
- 00885074 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885074 ["INT_ADD", "register:40f0:8", ["const:885074:8", "const:4:8"]]
- 00885074 ["CALLIND", null, ["register:0:8"]]
+ 008850cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008850cc ["INT_ADD", "register:40f0:8", ["const:8850cc:8", "const:4:8"]]
+ 008850cc ["CALLIND", null, ["register:0:8"]]
- 00885074 bytes 00013fd6
+ 008850cc bytes 00013fd6
- 00885010 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 00885010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885068 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00885068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885010 bytes 08613291
+ 00885068 bytes 08a13591
- 00885040 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885040 ["INT_ADD", "register:40f0:8", ["const:885040:8", "const:4:8"]]
- 00885040 ["CALLIND", null, ["register:0:8"]]
+ 00885098 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885098 ["INT_ADD", "register:40f0:8", ["const:885098:8", "const:4:8"]]
+ 00885098 ["CALLIND", null, ["register:0:8"]]
- 00885040 bytes 00013fd6
+ 00885098 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21ea355259673d9f0f608df7b118d39f"></a>

### [`00885088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885088.md) → [`008850e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008850e0.md) FUN_008850e0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "008850f8",
      "incomplete_value": false,
      "site": "00885104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008850a0",
      "incomplete_value": false,
      "site": "008850ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "00885104",
      "DATA",
      [
        "storage",
        "00c80c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885104",
      "DATA",
      [
        "storage",
        "00c80d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008850a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885088.md#insn-008850a0) · [`008850d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885088.md#insn-008850d0) · [`008850e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885088.md#insn-008850e4)
- 新版 `008850f8`（命令位置の公開資料なし） · `00885128`（命令位置の公開資料なし） · `0088513c`（命令位置の公開資料なし）

~~~diff
- 008850a0 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 008850a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008850a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008850a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008850f8 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 008850f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008850f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008850f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008850a0 bytes 08613291
+ 008850f8 bytes 08a13591
- 008850d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008850d0 ["INT_ADD", "register:40f0:8", ["const:8850d0:8", "const:4:8"]]
- 008850d0 ["CALLIND", null, ["register:0:8"]]
+ 00885128 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885128 ["INT_ADD", "register:40f0:8", ["const:885128:8", "const:4:8"]]
+ 00885128 ["CALLIND", null, ["register:0:8"]]
- 008850d0 bytes 00013fd6
+ 00885128 bytes 00013fd6
- 008850e4 ["INT_ADD", "register:40f0:8", ["const:8850e4:8", "const:4:8"]]
- 008850e4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088513c ["INT_ADD", "register:40f0:8", ["const:88513c:8", "const:4:8"]]
+ 0088513c ["CALL", null, ["callee:00c53da0:8"]]
- 008850e4 bytes 073b0f94
+ 0088513c bytes 193b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6112322603b109d7d21b3802995d3ab3"></a>

### [`00885114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885114.md) → [`0088516c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088516c.md) FUN_0088516c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885194",
      "incomplete_value": false,
      "site": "00885198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088513c",
      "incomplete_value": false,
      "site": "00885140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "00885198",
      "DATA",
      [
        "storage",
        "00c80c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885198",
      "DATA",
      [
        "storage",
        "00c80d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885114.md#insn-00885128) · [`0088513c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885114.md#insn-0088513c) · [`00885158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885114.md#insn-00885158)
- 新版 `00885180`（命令位置の公開資料なし） · `00885194`（命令位置の公開資料なし） · `008851b0`（命令位置の公開資料なし）

~~~diff
- 00885128 ["INT_ADD", "register:40f0:8", ["const:885128:8", "const:4:8"]]
- 00885128 ["CALL", null, ["callee:00c57f60:8"]]
+ 00885180 ["INT_ADD", "register:40f0:8", ["const:885180:8", "const:4:8"]]
+ 00885180 ["CALL", null, ["callee:00c57f60:8"]]
- 00885128 bytes 5a4b0f94
+ 00885180 bytes 784b0f94
- 0088513c ["COPY", "tmp:0:8", ["const:c98:8"]]
- 0088513c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088513c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088513c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00885194 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00885194 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00885194 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00885194 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088513c bytes 29613291
+ 00885194 bytes 29a13591
- 00885158 ["INT_ADD", "register:40f0:8", ["const:885158:8", "const:4:8"]]
- 00885158 ["CALL", null, ["callee:00c53d70:8"]]
+ 008851b0 ["INT_ADD", "register:40f0:8", ["const:8851b0:8", "const:4:8"]]
+ 008851b0 ["CALL", null, ["callee:00c53d70:8"]]
- 00885158 bytes de3a0f94
+ 008851b0 bytes f03a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93b5da53b75ac844beac1649e5baae39"></a>

### [`008851c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008851c4.md) → [`0088521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088521c.md) FUN_0088521c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "00885238",
      "incomplete_value": false,
      "site": "00885244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008851e0",
      "incomplete_value": false,
      "site": "008851ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "00885244",
      "DATA",
      [
        "storage",
        "00c80c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885244",
      "DATA",
      [
        "storage",
        "00c80d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008851e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008851c4.md#insn-008851e0) · [`00885200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008851c4.md#insn-00885200) · [`00885220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008851c4.md#insn-00885220)
- 新版 `00885238`（命令位置の公開資料なし） · `00885258`（命令位置の公開資料なし） · `00885278`（命令位置の公開資料なし）

~~~diff
- 008851e0 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 008851e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008851e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008851e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00885238 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00885238 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00885238 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00885238 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008851e0 bytes 29613291
+ 00885238 bytes 29a13591
- 00885200 ["INT_ADD", "register:40f0:8", ["const:885200:8", "const:4:8"]]
- 00885200 ["CALL", null, ["callee:00c53d70:8"]]
+ 00885258 ["INT_ADD", "register:40f0:8", ["const:885258:8", "const:4:8"]]
+ 00885258 ["CALL", null, ["callee:00c53d70:8"]]
- 00885200 bytes b43a0f94
+ 00885258 bytes c63a0f94
- 00885220 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885220 ["INT_ADD", "register:40f0:8", ["const:885220:8", "const:4:8"]]
- 00885220 ["CALLIND", null, ["register:0:8"]]
+ 00885278 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885278 ["INT_ADD", "register:40f0:8", ["const:885278:8", "const:4:8"]]
+ 00885278 ["CALLIND", null, ["register:0:8"]]
- 00885220 bytes 00013fd6
+ 00885278 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-796e33732d40775569e9196bcd272a39"></a>

### [`008853a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008853a4.md) → [`008853fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008853fc.md) FUN_008853fc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885418",
      "incomplete_value": false,
      "site": "00885420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008853c0",
      "incomplete_value": false,
      "site": "008853c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "00885420",
      "DATA",
      [
        "storage",
        "00c80d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885420",
      "DATA",
      [
        "storage",
        "00c80df8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008853c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008853a4.md#insn-008853c0) · [`008853d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008853a4.md#insn-008853d8) · [`008853ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008853a4.md#insn-008853ec)
- 新版 `00885418`（命令位置の公開資料なし） · `00885430`（命令位置の公開資料なし） · `00885444`（命令位置の公開資料なし）

~~~diff
- 008853c0 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 008853c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008853c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008853c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885418 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 00885418 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885418 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885418 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008853c0 bytes 08a13491
+ 00885418 bytes 08e13791
- 008853d8 ["INT_ADD", "register:40f0:8", ["const:8853d8:8", "const:4:8"]]
- 008853d8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00885430 ["INT_ADD", "register:40f0:8", ["const:885430:8", "const:4:8"]]
+ 00885430 ["CALL", null, ["callee:00c53da0:8"]]
- 008853d8 bytes 4a3a0f94
+ 00885430 bytes 5c3a0f94
- 008853ec ["COPY", "register:0:8", ["register:4040:8"]]
- 008853ec ["INT_ADD", "register:40f0:8", ["const:8853ec:8", "const:4:8"]]
- 008853ec ["CALLIND", null, ["register:0:8"]]
+ 00885444 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885444 ["INT_ADD", "register:40f0:8", ["const:885444:8", "const:4:8"]]
+ 00885444 ["CALLIND", null, ["register:0:8"]]
- 008853ec bytes 00013fd6
+ 00885444 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edb4f907c63d8e93520ffe0730b71a2b"></a>

### [`00885440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885440.md) → [`00885498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885498.md) FUN_00885498

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008854b4",
      "incomplete_value": false,
      "site": "008854bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088545c",
      "incomplete_value": false,
      "site": "00885464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "008854bc",
      "DATA",
      [
        "storage",
        "00c80d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008854bc",
      "DATA",
      [
        "storage",
        "00c80df8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008854bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885440.md#insn-008854bc) · [`0088545c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885440.md#insn-0088545c) · [`00885474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885440.md#insn-00885474)
- 新版 `00885514`（命令位置の公開資料なし） · `008854b4`（命令位置の公開資料なし） · `008854cc`（命令位置の公開資料なし）

~~~diff
- 008854bc ["COPY", "register:0:8", ["register:4040:8"]]
- 008854bc ["INT_ADD", "register:40f0:8", ["const:8854bc:8", "const:4:8"]]
- 008854bc ["CALLIND", null, ["register:0:8"]]
+ 00885514 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885514 ["INT_ADD", "register:40f0:8", ["const:885514:8", "const:4:8"]]
+ 00885514 ["CALLIND", null, ["register:0:8"]]
- 008854bc bytes 00013fd6
+ 00885514 bytes 00013fd6
- 0088545c ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0088545c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088545c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088545c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008854b4 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 008854b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008854b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008854b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088545c bytes 08a13491
+ 008854b4 bytes 08e13791
- 00885474 ["INT_ADD", "register:40f0:8", ["const:885474:8", "const:4:8"]]
- 00885474 ["CALL", null, ["callee:00c53da0:8"]]
+ 008854cc ["INT_ADD", "register:40f0:8", ["const:8854cc:8", "const:4:8"]]
+ 008854cc ["CALL", null, ["callee:00c53da0:8"]]
- 00885474 bytes 233a0f94
+ 008854cc bytes 353a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d94772b988c4b25c75d987e8ce047cdc"></a>

### [`008854d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008854d4.md) → [`0088552c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088552c.md) FUN_0088552c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885558",
      "incomplete_value": false,
      "site": "00885558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885500",
      "incomplete_value": false,
      "site": "00885500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "00885558",
      "DATA",
      [
        "storage",
        "00c80d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885558",
      "DATA",
      [
        "storage",
        "00c80df8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008854e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008854d4.md#insn-008854e8) · [`008854f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008854d4.md#insn-008854f8) · [`0088551c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008854d4.md#insn-0088551c)
- 新版 `00885540`（命令位置の公開資料なし） · `00885550`（命令位置の公開資料なし） · `00885574`（命令位置の公開資料なし）

~~~diff
- 008854e8 ["INT_ADD", "register:40f0:8", ["const:8854e8:8", "const:4:8"]]
- 008854e8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00885540 ["INT_ADD", "register:40f0:8", ["const:885540:8", "const:4:8"]]
+ 00885540 ["CALL", null, ["callee:00c57f60:8"]]
- 008854e8 bytes 6a4a0f94
+ 00885540 bytes 884a0f94
- 008854f8 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 008854f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008854f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008854f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885550 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 00885550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008854f8 bytes 08a13491
+ 00885550 bytes 08e13791
- 0088551c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088551c ["INT_ADD", "register:40f0:8", ["const:88551c:8", "const:4:8"]]
- 0088551c ["CALLIND", null, ["register:0:8"]]
+ 00885574 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885574 ["INT_ADD", "register:40f0:8", ["const:885574:8", "const:4:8"]]
+ 00885574 ["CALLIND", null, ["register:0:8"]]
- 0088551c bytes 00013fd6
+ 00885574 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f54ba26e26e40cb76555520ac642d2e5"></a>

### [`0088557c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088557c.md) → [`008855d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008855d4.md) FUN_008855d4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "008855f4",
      "incomplete_value": false,
      "site": "008855f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088559c",
      "incomplete_value": false,
      "site": "0088559c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "008855f4",
      "DATA",
      [
        "storage",
        "00c80d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008855f4",
      "DATA",
      [
        "storage",
        "00c80df8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088557c.md#insn-00885598) · [`008855b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088557c.md#insn-008855b8) · [`008855dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088557c.md#insn-008855dc)
- 新版 `008855f0`（命令位置の公開資料なし） · `00885610`（命令位置の公開資料なし） · `00885634`（命令位置の公開資料なし）

~~~diff
- 00885598 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00885598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008855f0 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 008855f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008855f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008855f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885598 bytes 08a13491
+ 008855f0 bytes 08e13791
- 008855b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008855b8 ["INT_ADD", "register:40f0:8", ["const:8855b8:8", "const:4:8"]]
- 008855b8 ["CALLIND", null, ["register:0:8"]]
+ 00885610 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885610 ["INT_ADD", "register:40f0:8", ["const:885610:8", "const:4:8"]]
+ 00885610 ["CALLIND", null, ["register:0:8"]]
- 008855b8 bytes 00013fd6
+ 00885610 bytes 00013fd6
- 008855dc ["COPY", "register:0:8", ["register:4040:8"]]
- 008855dc ["INT_ADD", "register:40f0:8", ["const:8855dc:8", "const:4:8"]]
- 008855dc ["CALLIND", null, ["register:0:8"]]
+ 00885634 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885634 ["INT_ADD", "register:40f0:8", ["const:885634:8", "const:4:8"]]
+ 00885634 ["CALLIND", null, ["register:0:8"]]
- 008855dc bytes 00013fd6
+ 00885634 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b55cbb0e715d4ac77a3c5b1fcaf807f8"></a>

### [`00885724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885724.md) → [`0088577c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088577c.md) FUN_0088577c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00768a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768a28.md) [`00768e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768e90.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00768a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768a80.md) [`00768ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768ee8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00880700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880700.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.30% / 新版 98.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885910",
      "incomplete_value": false,
      "site": "00885918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008858b8",
      "incomplete_value": false,
      "site": "008858c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00885830",
      "value": [
        "leaf",
        "ram:768ee8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008857d8",
      "value": [
        "leaf",
        "ram:768e90:8"
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
      "00885830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e90"
      ]
    ],
    [
      "00885918",
      "DATA",
      [
        "storage",
        "00c80d98",
        null,
        "undefined *"
      ]
    ],
    [
      "008859b8",
      "READ",
      [
        "storage",
        "00c80dc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768ee8"
      ]
    ],
    [
      "00885918",
      "DATA",
      [
        "storage",
        "00c80e68",
        null,
        "undefined *"
      ]
    ],
    [
      "008859b8",
      "READ",
      [
        "storage",
        "00c80e90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008857d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885724.md#insn-008857d8) · [`0088578c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885724.md#insn-0088578c) · [`00885794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885724.md#insn-00885794)
- 新版 `00885830`（命令位置の公開資料なし） · `008857e4`（命令位置の公開資料なし） · `008857ec`（命令位置の公開資料なし）

~~~diff
- 008857d8 ["INT_ADD", "register:40f0:8", ["const:8857d8:8", "const:4:8"]]
- 008857d8 ["CALL", null, ["ram:768e90:8"]]
+ 00885830 ["INT_ADD", "register:40f0:8", ["const:885830:8", "const:4:8"]]
+ 00885830 ["CALL", null, ["ram:768ee8:8"]]
- 008857d8 bytes ae8dfb97
+ 00885830 bytes ae8dfb97
- 0088578c ["INT_ADD", "register:40f0:8", ["const:88578c:8", "const:4:8"]]
- 0088578c ["CALL", null, ["callee:00851550:8"]]
+ 008857e4 ["INT_ADD", "register:40f0:8", ["const:8857e4:8", "const:4:8"]]
+ 008857e4 ["CALL", null, ["callee:00851550:8"]]
- 0088578c bytes 5b2fff97
+ 008857e4 bytes 5b2fff97
- 00885794 ["INT_ADD", "register:40f0:8", ["const:885794:8", "const:4:8"]]
- 00885794 ["CALL", null, ["callee:00768a80:8"]]
+ 008857ec ["INT_ADD", "register:40f0:8", ["const:8857ec:8", "const:4:8"]]
+ 008857ec ["CALL", null, ["callee:00768a80:8"]]
- 00885794 bytes a58cfb97
+ 008857ec bytes a58cfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40ab42281bfed8237bd34dfa23e94c05"></a>

### [`00885b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885b14.md) → [`00885b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885b6c.md) FUN_00885b6c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00885b84",
      "incomplete_value": false,
      "site": "00885b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885b2c",
      "incomplete_value": false,
      "site": "00885b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "00885b90",
      "DATA",
      [
        "storage",
        "00c80d98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885b90",
      "DATA",
      [
        "storage",
        "00c80e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885b14.md#insn-00885b90) · [`00885b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885b14.md#insn-00885b2c) · [`00885b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885b14.md#insn-00885b5c)
- 新版 `00885be8`（命令位置の公開資料なし） · `00885b84`（命令位置の公開資料なし） · `00885bb4`（命令位置の公開資料なし）

~~~diff
- 00885b90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885b90 ["INT_ADD", "register:40f0:8", ["const:885b90:8", "const:4:8"]]
- 00885b90 ["CALLIND", null, ["register:0:8"]]
+ 00885be8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885be8 ["INT_ADD", "register:40f0:8", ["const:885be8:8", "const:4:8"]]
+ 00885be8 ["CALLIND", null, ["register:0:8"]]
- 00885b90 bytes 00013fd6
+ 00885be8 bytes 00013fd6
- 00885b2c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00885b2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885b2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885b2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885b84 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00885b84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885b84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885b84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885b2c bytes 08613691
+ 00885b84 bytes 08a13991
- 00885b5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00885b5c ["INT_ADD", "register:40f0:8", ["const:885b5c:8", "const:4:8"]]
- 00885b5c ["CALLIND", null, ["register:0:8"]]
+ 00885bb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885bb4 ["INT_ADD", "register:40f0:8", ["const:885bb4:8", "const:4:8"]]
+ 00885bb4 ["CALLIND", null, ["register:0:8"]]
- 00885b5c bytes 00013fd6
+ 00885bb4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68ed220f5b02faaecec74b4d0b5c7eaf"></a>

### [`00885ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ba4.md) → [`00885bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885bfc.md) FUN_00885bfc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00885c14",
      "incomplete_value": false,
      "site": "00885c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885bbc",
      "incomplete_value": false,
      "site": "00885bc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "00885c20",
      "DATA",
      [
        "storage",
        "00c80d98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885c20",
      "DATA",
      [
        "storage",
        "00c80e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ba4.md#insn-00885bbc) · [`00885bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ba4.md#insn-00885bec) · [`00885c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ba4.md#insn-00885c00)
- 新版 `00885c14`（命令位置の公開資料なし） · `00885c44`（命令位置の公開資料なし） · `00885c58`（命令位置の公開資料なし）

~~~diff
- 00885bbc ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00885bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885c14 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00885c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885bbc bytes 08613691
+ 00885c14 bytes 08a13991
- 00885bec ["COPY", "register:0:8", ["register:4040:8"]]
- 00885bec ["INT_ADD", "register:40f0:8", ["const:885bec:8", "const:4:8"]]
- 00885bec ["CALLIND", null, ["register:0:8"]]
+ 00885c44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885c44 ["INT_ADD", "register:40f0:8", ["const:885c44:8", "const:4:8"]]
+ 00885c44 ["CALLIND", null, ["register:0:8"]]
- 00885bec bytes 00013fd6
+ 00885c44 bytes 00013fd6
- 00885c00 ["INT_ADD", "register:40f0:8", ["const:885c00:8", "const:4:8"]]
- 00885c00 ["CALL", null, ["callee:00c53da0:8"]]
+ 00885c58 ["INT_ADD", "register:40f0:8", ["const:885c58:8", "const:4:8"]]
+ 00885c58 ["CALL", null, ["callee:00c53da0:8"]]
- 00885c00 bytes 40380f94
+ 00885c58 bytes 52380f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ede0ac63253b1d7ed88fbfd864e6cf44"></a>

### [`00885c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885c30.md) → [`00885c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885c88.md) FUN_00885c88

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885cb0",
      "incomplete_value": false,
      "site": "00885cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885c58",
      "incomplete_value": false,
      "site": "00885c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "00885cb4",
      "DATA",
      [
        "storage",
        "00c80d98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885cb4",
      "DATA",
      [
        "storage",
        "00c80e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885c30.md#insn-00885c44) · [`00885c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885c30.md#insn-00885c58) · [`00885c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885c30.md#insn-00885c74)
- 新版 `00885c9c`（命令位置の公開資料なし） · `00885cb0`（命令位置の公開資料なし） · `00885ccc`（命令位置の公開資料なし）

~~~diff
- 00885c44 ["INT_ADD", "register:40f0:8", ["const:885c44:8", "const:4:8"]]
- 00885c44 ["CALL", null, ["callee:00c57f60:8"]]
+ 00885c9c ["INT_ADD", "register:40f0:8", ["const:885c9c:8", "const:4:8"]]
+ 00885c9c ["CALL", null, ["callee:00c57f60:8"]]
- 00885c44 bytes 93480f94
+ 00885c9c bytes b1480f94
- 00885c58 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00885c58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00885c58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00885c58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00885cb0 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00885cb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00885cb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00885cb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00885c58 bytes 29613691
+ 00885cb0 bytes 29a13991
- 00885c74 ["INT_ADD", "register:40f0:8", ["const:885c74:8", "const:4:8"]]
- 00885c74 ["CALL", null, ["callee:00c53d70:8"]]
+ 00885ccc ["INT_ADD", "register:40f0:8", ["const:885ccc:8", "const:4:8"]]
+ 00885ccc ["CALL", null, ["callee:00c53d70:8"]]
- 00885c74 bytes 17380f94
+ 00885ccc bytes 29380f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac40cd1e0951c81b96d678eaa4003a29"></a>

### [`00885ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ce0.md) → [`00885d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885d38.md) FUN_00885d38

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "00885d54",
      "incomplete_value": false,
      "site": "00885d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885cfc",
      "incomplete_value": false,
      "site": "00885d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "00885d60",
      "DATA",
      [
        "storage",
        "00c80d98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885d60",
      "DATA",
      [
        "storage",
        "00c80e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ce0.md#insn-00885cfc) · [`00885d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ce0.md#insn-00885d1c) · [`00885d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ce0.md#insn-00885d3c)
- 新版 `00885d54`（命令位置の公開資料なし） · `00885d74`（命令位置の公開資料なし） · `00885d94`（命令位置の公開資料なし）

~~~diff
- 00885cfc ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00885cfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00885cfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00885cfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00885d54 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00885d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00885d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00885d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00885cfc bytes 29613691
+ 00885d54 bytes 29a13991
- 00885d1c ["INT_ADD", "register:40f0:8", ["const:885d1c:8", "const:4:8"]]
- 00885d1c ["CALL", null, ["callee:00c53d70:8"]]
+ 00885d74 ["INT_ADD", "register:40f0:8", ["const:885d74:8", "const:4:8"]]
+ 00885d74 ["CALL", null, ["callee:00c53d70:8"]]
- 00885d1c bytes ed370f94
+ 00885d74 bytes ff370f94
- 00885d3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00885d3c ["INT_ADD", "register:40f0:8", ["const:885d3c:8", "const:4:8"]]
- 00885d3c ["CALLIND", null, ["register:0:8"]]
+ 00885d94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885d94 ["INT_ADD", "register:40f0:8", ["const:885d94:8", "const:4:8"]]
+ 00885d94 ["CALLIND", null, ["register:0:8"]]
- 00885d3c bytes 00013fd6
+ 00885d94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-850c84ea848d055a93e8a7c86c075a98"></a>

### [`00885ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ec0.md) → [`00885f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885f18.md) FUN_00885f18

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00885f30",
      "incomplete_value": false,
      "site": "00885f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885ed8",
      "incomplete_value": false,
      "site": "00885ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "00885f3c",
      "DATA",
      [
        "storage",
        "00c80e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885f3c",
      "DATA",
      [
        "storage",
        "00c80ef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ec0.md#insn-00885ed8) · [`00885f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ec0.md#insn-00885f08)
- 新版 `00885f30`（命令位置の公開資料なし） · `00885f60`（命令位置の公開資料なし）

~~~diff
- 00885ed8 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00885ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885f30 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 00885f30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885f30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885f30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885ed8 bytes 08a13891
+ 00885f30 bytes 08e13b91
- 00885f08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885f08 ["INT_ADD", "register:40f0:8", ["const:885f08:8", "const:4:8"]]
- 00885f08 ["CALLIND", null, ["register:0:8"]]
+ 00885f60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885f60 ["INT_ADD", "register:40f0:8", ["const:885f60:8", "const:4:8"]]
+ 00885f60 ["CALLIND", null, ["register:0:8"]]
- 00885f08 bytes 00013fd6
+ 00885f60 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8526638fe3e807b49ef60a12adef1cec"></a>

### [`00885f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885f30.md) → [`00885f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885f88.md) FUN_00885f88

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885fa0",
      "incomplete_value": false,
      "site": "00885fac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885f48",
      "incomplete_value": false,
      "site": "00885f54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "00885fac",
      "DATA",
      [
        "storage",
        "00c80e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885fac",
      "DATA",
      [
        "storage",
        "00c80ef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885f30.md#insn-00885f48) · [`00885f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885f30.md#insn-00885f78) · [`00885f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885f30.md#insn-00885f88)
- 新版 `00885fa0`（命令位置の公開資料なし） · `00885fd0`（命令位置の公開資料なし） · `00885fe0`（命令位置の公開資料なし）

~~~diff
- 00885f48 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00885f48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885f48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885f48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885fa0 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 00885fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885f48 bytes 08a13891
+ 00885fa0 bytes 08e13b91
- 00885f78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885f78 ["INT_ADD", "register:40f0:8", ["const:885f78:8", "const:4:8"]]
- 00885f78 ["CALLIND", null, ["register:0:8"]]
+ 00885fd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885fd0 ["INT_ADD", "register:40f0:8", ["const:885fd0:8", "const:4:8"]]
+ 00885fd0 ["CALLIND", null, ["register:0:8"]]
- 00885f78 bytes 00013fd6
+ 00885fd0 bytes 00013fd6
- 00885f88 ["INT_ADD", "register:40f0:8", ["const:885f88:8", "const:4:8"]]
- 00885f88 ["CALL", null, ["callee:00c57f80:8"]]
+ 00885fe0 ["INT_ADD", "register:40f0:8", ["const:885fe0:8", "const:4:8"]]
+ 00885fe0 ["CALL", null, ["callee:00c57f80:8"]]
- 00885f88 bytes ca470f94
+ 00885fe0 bytes e8470f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dfa7b8462b3853bba8095a2851e52b6"></a>

### [`00885f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885f9c.md) → [`00885ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885ff4.md) FUN_00885ff4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00886028",
      "incomplete_value": false,
      "site": "00886028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885fd0",
      "incomplete_value": false,
      "site": "00885fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "00886028",
      "DATA",
      [
        "storage",
        "00c80e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886028",
      "DATA",
      [
        "storage",
        "00c80ef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885f9c.md#insn-00885fb4) · [`00885fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885f9c.md#insn-00885fc4) · [`00885fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885f9c.md#insn-00885fcc)
- 新版 `0088600c`（命令位置の公開資料なし） · `0088601c`（命令位置の公開資料なし）

~~~diff
- 00885fb4 ["INT_ADD", "register:40f0:8", ["const:885fb4:8", "const:4:8"]]
- 00885fb4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088600c ["INT_ADD", "register:40f0:8", ["const:88600c:8", "const:4:8"]]
+ 0088600c ["CALL", null, ["callee:00c57f60:8"]]
- 00885fb4 bytes b7470f94
+ 0088600c bytes d5470f94
- 00885fc4 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00885fc4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00885fc4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00885fc4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0088601c ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 0088601c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0088601c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0088601c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00885fc4 bytes 4aa13891
+ 0088601c bytes 4ae13b91
- 00885fcc ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00885fcc bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbafd76a624cf05758f84eb83b5a93ef"></a>

### [`00886074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886074.md) → [`008860cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008860cc.md) FUN_008860cc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008860e8",
      "incomplete_value": false,
      "site": "008860e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886090",
      "incomplete_value": false,
      "site": "00886090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "008860e8",
      "DATA",
      [
        "storage",
        "00c80e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008860e8",
      "DATA",
      [
        "storage",
        "00c80ef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886074.md#insn-00886088) · [`0088608c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886074.md#insn-0088608c) · [`008860cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886074.md#insn-008860cc)
- 新版 `008860e0`（命令位置の公開資料なし） · `00886124`（命令位置の公開資料なし）

~~~diff
- 00886088 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00886088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00886088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00886088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008860e0 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 008860e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008860e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008860e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00886088 bytes 08a13891
+ 008860e0 bytes 08e13b91
- 0088608c ["COPY", "register:40a0:8", ["register:4008:8"]]
- 0088608c bytes f40301aa
- 008860cc ["INT_ADD", "register:40f0:8", ["const:8860cc:8", "const:4:8"]]
- 008860cc ["CALL", null, ["callee:0043bb60:8"]]
+ 00886124 ["INT_ADD", "register:40f0:8", ["const:886124:8", "const:4:8"]]
+ 00886124 ["CALL", null, ["callee:0043bb60:8"]]
- 008860cc bytes 95d6ee97
+ 00886124 bytes 8fd6ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a88484b48bd857357bfda9b7a8bae22"></a>

### [`00886200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886200.md) → [`00886258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886258.md) FUN_00886258

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`004557dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`0045581c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/0045581c.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00764f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.52% / 新版 97.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088633c",
      "incomplete_value": false,
      "site": "0088633c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008862e4",
      "incomplete_value": false,
      "site": "008862e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00886298",
      "value": [
        "leaf",
        "ram:764f38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00886240",
      "value": [
        "leaf",
        "ram:764ee0:8"
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
      "00886298",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ],
    [
      "0088633c",
      "DATA",
      [
        "storage",
        "00c80e98",
        null,
        "undefined *"
      ]
    ],
    [
      "008863b8",
      "READ",
      [
        "storage",
        "00c80ec0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886298",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764f38"
      ]
    ],
    [
      "0088633c",
      "DATA",
      [
        "storage",
        "00c80f68",
        null,
        "undefined *"
      ]
    ],
    [
      "008863b8",
      "READ",
      [
        "storage",
        "00c80f90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886200.md#insn-00886240) · [`00886230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886200.md#insn-00886230) · [`00886238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886200.md#insn-00886238)
- 新版 `00886298`（命令位置の公開資料なし） · `00886288`（命令位置の公開資料なし） · `00886290`（命令位置の公開資料なし）

~~~diff
- 00886240 ["INT_ADD", "register:40f0:8", ["const:886240:8", "const:4:8"]]
- 00886240 ["CALL", null, ["ram:764ee0:8"]]
+ 00886298 ["INT_ADD", "register:40f0:8", ["const:886298:8", "const:4:8"]]
+ 00886298 ["CALL", null, ["ram:764f38:8"]]
- 00886240 bytes 287bfb97
+ 00886298 bytes 287bfb97
- 00886230 ["INT_ADD", "register:40f0:8", ["const:886230:8", "const:4:8"]]
- 00886230 ["CALL", null, ["callee:0044f920:8"]]
+ 00886288 ["INT_ADD", "register:40f0:8", ["const:886288:8", "const:4:8"]]
+ 00886288 ["CALL", null, ["callee:0044f920:8"]]
- 00886230 bytes ac25ef97
+ 00886288 bytes a625ef97
- 00886238 ["INT_ADD", "register:40f0:8", ["const:886238:8", "const:4:8"]]
- 00886238 ["CALL", null, ["callee:00851550:8"]]
+ 00886290 ["INT_ADD", "register:40f0:8", ["const:886290:8", "const:4:8"]]
+ 00886290 ["CALL", null, ["callee:00851550:8"]]
- 00886238 bytes b02cff97
+ 00886290 bytes b02cff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2374a4495eb32b1bc22f0f0dd1f77d2"></a>

### [`00886518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886518.md) → [`00886570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886570.md) FUN_00886570

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00886588",
      "incomplete_value": false,
      "site": "00886594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886530",
      "incomplete_value": false,
      "site": "0088653c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "00886594",
      "DATA",
      [
        "storage",
        "00c80e98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886594",
      "DATA",
      [
        "storage",
        "00c80f68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886518.md#insn-00886530) · [`00886560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886518.md#insn-00886560)
- 新版 `00886588`（命令位置の公開資料なし） · `008865b8`（命令位置の公開資料なし）

~~~diff
- 00886530 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 00886530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00886530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00886530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00886588 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00886588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00886588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00886588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00886530 bytes 08613a91
+ 00886588 bytes 08a13d91
- 00886560 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886560 ["INT_ADD", "register:40f0:8", ["const:886560:8", "const:4:8"]]
- 00886560 ["CALLIND", null, ["register:0:8"]]
+ 008865b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008865b8 ["INT_ADD", "register:40f0:8", ["const:8865b8:8", "const:4:8"]]
+ 008865b8 ["CALLIND", null, ["register:0:8"]]
- 00886560 bytes 00013fd6
+ 008865b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2180213507cffcbeef89e0be57960ae3"></a>

### [`008865fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008865fc.md) → [`00886654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886654.md) FUN_00886654

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00886670",
      "incomplete_value": false,
      "site": "00886670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886618",
      "incomplete_value": false,
      "site": "00886618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "00886670",
      "DATA",
      [
        "storage",
        "00c80e98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886670",
      "DATA",
      [
        "storage",
        "00c80f68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008865fc.md#insn-00886614) · [`00886638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008865fc.md#insn-00886638)
- 新版 `0088666c`（命令位置の公開資料なし） · `00886690`（命令位置の公開資料なし）

~~~diff
- 00886614 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 00886614 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00886614 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00886614 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088666c ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 0088666c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088666c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088666c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00886614 bytes 29613a91
+ 0088666c bytes 29a13d91
- 00886638 ["COPY", "register:0:8", ["register:4048:8"]]
- 00886638 ["INT_ADD", "register:40f0:8", ["const:886638:8", "const:4:8"]]
- 00886638 ["CALLIND", null, ["register:0:8"]]
+ 00886690 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00886690 ["INT_ADD", "register:40f0:8", ["const:886690:8", "const:4:8"]]
+ 00886690 ["CALLIND", null, ["register:0:8"]]
- 00886638 bytes 20013fd6
+ 00886690 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-309233488dbfe8516b796383b52fb373"></a>

### [`008868b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008868b8.md) → [`00886910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886910.md) FUN_00886910

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
      "definition_site": "00886924",
      "incomplete_value": false,
      "site": "00886928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008868cc",
      "incomplete_value": false,
      "site": "008868d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "00886928",
      "DATA",
      [
        "storage",
        "00c80f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886928",
      "DATA",
      [
        "storage",
        "00c81008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008868c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008868b8.md#insn-008868c8) · [`008868cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008868b8.md#insn-008868cc) · [`008868e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008868b8.md#insn-008868e0)
- 新版 `00886920`（命令位置の公開資料なし） · `00886924`（命令位置の公開資料なし） · `00886938`（命令位置の公開資料なし）

~~~diff
- 008868c8 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00886920 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 008868c8 bytes c81f00d0
+ 00886920 bytes c81f00f0
- 008868cc ["COPY", "tmp:0:8", ["const:f38:8"]]
- 008868cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008868cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008868cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00886924 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 00886924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00886924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00886924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008868cc bytes 08e13c91
+ 00886924 bytes 08210091
- 008868e0 ["INT_ADD", "register:40f0:8", ["const:8868e0:8", "const:4:8"]]
- 008868e0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00886938 ["INT_ADD", "register:40f0:8", ["const:886938:8", "const:4:8"]]
+ 00886938 ["CALL", null, ["callee:00c53da0:8"]]
- 008868e0 bytes 08350f94
+ 00886938 bytes 1a350f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

