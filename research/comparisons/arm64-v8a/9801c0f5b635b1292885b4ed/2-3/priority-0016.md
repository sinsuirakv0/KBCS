# v16.0.1 → v16.0.2 · 最優先の変更候補 (16)

[一覧の目次](README.md)

<a id="compare-5e8c08061059c6a3af1eba342be55bbb"></a>

### [`0056085c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056085c.md) → [`0056089c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/0056089c.md) FUN_0056089c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 12件 [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00881098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md) [`00930a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930a40.md) [`0093155c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/0093155c.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 12件 [`004737bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004737bc.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`008810f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008810f0.md) [`00930a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00930/00930a94.md) [`009315b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00931/009315b0.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005608b8",
      "incomplete_value": false,
      "site": "005608c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560878",
      "incomplete_value": false,
      "site": "00560880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
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
      "definition_site": "005608d0",
      "incomplete_value": false,
      "site": "005608d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560890",
      "incomplete_value": false,
      "site": "00560890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "005608c0",
      "DATA",
      [
        "storage",
        "00c6b2d0",
        null,
        "undefined *"
      ]
    ],
    [
      "005608d0",
      "DATA",
      [
        "storage",
        "00c6b320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005608c0",
      "DATA",
      [
        "storage",
        "00c6b3a0",
        null,
        "undefined *"
      ]
    ],
    [
      "005608d0",
      "DATA",
      [
        "storage",
        "00c6b3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056085c.md#insn-00560870) · [`00560878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056085c.md#insn-00560878) · [`00560884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056085c.md#insn-00560884)
- 新版 `005608b0`（命令位置の公開資料なし） · `005608b8`（命令位置の公開資料なし）

~~~diff
- 00560870 ["INT_ADD", "register:40f0:8", ["const:560870:8", "const:4:8"]]
- 00560870 ["CALL", null, ["callee:00c57f60:8"]]
+ 005608b0 ["INT_ADD", "register:40f0:8", ["const:5608b0:8", "const:4:8"]]
+ 005608b0 ["CALL", null, ["callee:00c57f60:8"]]
- 00560870 bytes 88dd1b94
+ 005608b0 bytes acdd1b94
- 00560878 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 00560878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005608b8 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 005608b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005608b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005608b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560878 bytes 08410b91
+ 005608b8 bytes 08810e91
- 00560884 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00560884 bytes 483800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecae0a0b1ebea46fc6422ce8c790a025"></a>

### [`005608a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005608a4.md) → [`005608e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005608e4.md) FUN_005608e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00550a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a14.md) [`00560e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560e48.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00550a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a54.md) [`00560e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560e88.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056097c",
      "incomplete_value": false,
      "site": "0056097c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056093c",
      "incomplete_value": false,
      "site": "0056093c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "0056097c",
      "DATA",
      [
        "storage",
        "00c6b370",
        null,
        "undefined *"
      ]
    ],
    [
      "005609fc",
      "READ",
      [
        "storage",
        "00c6b398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056097c",
      "DATA",
      [
        "storage",
        "00c6b440",
        null,
        "undefined *"
      ]
    ],
    [
      "005609fc",
      "READ",
      [
        "storage",
        "00c6b468",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005608d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005608a4.md#insn-005608d4) · [`005608f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005608a4.md#insn-005608f4) · [`00560918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005608a4.md#insn-00560918)
- 新版 `00560914`（命令位置の公開資料なし） · `00560934`（命令位置の公開資料なし） · `00560958`（命令位置の公開資料なし）

~~~diff
- 005608d4 ["INT_ADD", "register:40f0:8", ["const:5608d4:8", "const:4:8"]]
- 005608d4 ["CALL", null, ["callee:00550a54:8"]]
+ 00560914 ["INT_ADD", "register:40f0:8", ["const:560914:8", "const:4:8"]]
+ 00560914 ["CALL", null, ["callee:00550a54:8"]]
- 005608d4 bytes 50c0ff97
+ 00560914 bytes 50c0ff97
- 005608f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005608f4 ["INT_ADD", "register:40f0:8", ["const:5608f4:8", "const:4:8"]]
- 005608f4 ["CALLIND", null, ["register:0:8"]]
+ 00560934 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00560934 ["INT_ADD", "register:40f0:8", ["const:560934:8", "const:4:8"]]
+ 00560934 ["CALLIND", null, ["register:0:8"]]
- 005608f4 bytes 00013fd6
+ 00560934 bytes 00013fd6
- 00560918 ["COPY", "register:0:8", ["register:4040:8"]]
- 00560918 ["INT_ADD", "register:40f0:8", ["const:560918:8", "const:4:8"]]
- 00560918 ["CALLIND", null, ["register:0:8"]]
+ 00560958 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00560958 ["INT_ADD", "register:40f0:8", ["const:560958:8", "const:4:8"]]
+ 00560958 ["CALLIND", null, ["register:0:8"]]
- 00560918 bytes 00013fd6
+ 00560958 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a88b2af0a5ad4d0b331cf2bc9c9de17"></a>

### [`00560b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b68.md) → [`00560ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560ba8.md) FUN_00560ba8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00560bc0",
      "incomplete_value": false,
      "site": "00560bc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560b80",
      "incomplete_value": false,
      "site": "00560b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "00560bc4",
      "DATA",
      [
        "storage",
        "00c6b270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560bc4",
      "DATA",
      [
        "storage",
        "00c6b340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b68.md#insn-00560b80) · [`00560b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b68.md#insn-00560b90)
- 新版 `00560bc0`（命令位置の公開資料なし） · `00560bd0`（命令位置の公開資料なし）

~~~diff
- 00560b80 ["COPY", "tmp:0:8", ["const:270:8"]]
- 00560b80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560b80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560b80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560bc0 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 00560bc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560bc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560bc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560b80 bytes 29c10991
+ 00560bc0 bytes 29010d91
- 00560b90 ["INT_ADD", "register:40f0:8", ["const:560b90:8", "const:4:8"]]
- 00560b90 ["CALL", null, ["callee:00c57f80:8"]]
+ 00560bd0 ["INT_ADD", "register:40f0:8", ["const:560bd0:8", "const:4:8"]]
+ 00560bd0 ["CALL", null, ["callee:00c57f80:8"]]
- 00560b90 bytes c8dc1b94
+ 00560bd0 bytes ecdc1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a416247c34929007194fa4475e138efb"></a>

### [`00560bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560bb8.md) → [`00560bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560bf8.md) FUN_00560bf8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00560c10",
      "incomplete_value": false,
      "site": "00560c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560bd0",
      "incomplete_value": false,
      "site": "00560bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "00560c14",
      "DATA",
      [
        "storage",
        "00c6b270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560c14",
      "DATA",
      [
        "storage",
        "00c6b340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560bb8.md#insn-00560bd0) · [`00560be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560bb8.md#insn-00560be0) · [`00560bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560bb8.md#insn-00560bf0)
- 新版 `00560c10`（命令位置の公開資料なし） · `00560c20`（命令位置の公開資料なし） · `00560c30`（命令位置の公開資料なし）

~~~diff
- 00560bd0 ["COPY", "tmp:0:8", ["const:270:8"]]
- 00560bd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560bd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560bd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560c10 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 00560c10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560c10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560c10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560bd0 bytes 29c10991
+ 00560c10 bytes 29010d91
- 00560be0 ["INT_ADD", "register:40f0:8", ["const:560be0:8", "const:4:8"]]
- 00560be0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00560c20 ["INT_ADD", "register:40f0:8", ["const:560c20:8", "const:4:8"]]
+ 00560c20 ["CALL", null, ["callee:00c57f80:8"]]
- 00560be0 bytes b4dc1b94
+ 00560c20 bytes d8dc1b94
- 00560bf0 ["INT_ADD", "register:40f0:8", ["const:560bf0:8", "const:4:8"]]
- 00560bf0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00560c30 ["INT_ADD", "register:40f0:8", ["const:560c30:8", "const:4:8"]]
+ 00560c30 ["CALL", null, ["callee:00c57f80:8"]]
- 00560bf0 bytes b0dc1b94
+ 00560c30 bytes d4dc1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-583e4213937de955221c5379f39104d0"></a>

### [`00560c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560c0c.md) → [`00560c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560c4c.md) FUN_00560c4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00560c50",
      "incomplete_value": false,
      "site": "00560c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560c10",
      "incomplete_value": false,
      "site": "00560c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
      "00560c54",
      "DATA",
      [
        "storage",
        "00c6b2d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560c54",
      "DATA",
      [
        "storage",
        "00c6b3a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560c0c.md#insn-00560c10)
- 新版 `00560c50`（命令位置の公開資料なし）

~~~diff
- 00560c10 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 00560c10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560c10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560c10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560c50 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 00560c50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560c50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560c50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560c10 bytes 08410b91
+ 00560c50 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-961e160ba71f01a23b59ebf53d809dcb"></a>

### [`00560c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560c1c.md) → [`00560c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560c5c.md) FUN_00560c5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00560c6c",
      "incomplete_value": false,
      "site": "00560c74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560c2c",
      "incomplete_value": false,
      "site": "00560c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
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
      "00560c74",
      "DATA",
      [
        "storage",
        "00c6b2d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560c74",
      "DATA",
      [
        "storage",
        "00c6b3a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560c1c.md#insn-00560c2c) · [`00560c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560c1c.md#insn-00560c38)
- 新版 `00560c6c`（命令位置の公開資料なし） · `00560c78`（命令位置の公開資料なし）

~~~diff
- 00560c2c ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 00560c2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560c2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560c2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560c6c ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 00560c6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560c6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560c6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560c2c bytes 08410b91
+ 00560c6c bytes 08810e91
- 00560c38 ["INT_ADD", "register:40f0:8", ["const:560c38:8", "const:4:8"]]
- 00560c38 ["CALL", null, ["callee:00c57f70:8"]]
+ 00560c78 ["INT_ADD", "register:40f0:8", ["const:560c78:8", "const:4:8"]]
+ 00560c78 ["CALL", null, ["callee:00c57f70:8"]]
- 00560c38 bytes 9adc1b94
+ 00560c78 bytes bedc1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13cccbcb0294c1eaff5d253d0ed9f932"></a>

### [`00560cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560cb8.md) → [`00560cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560cf8.md) FUN_00560cf8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00560d10",
      "incomplete_value": false,
      "site": "00560d1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560cd0",
      "incomplete_value": false,
      "site": "00560cdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "00560d1c",
      "DATA",
      [
        "storage",
        "00c6b370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560d1c",
      "DATA",
      [
        "storage",
        "00c6b440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560cb8.md#insn-00560cd0) · [`00560d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560cb8.md#insn-00560d00)
- 新版 `00560d10`（命令位置の公開資料なし） · `00560d40`（命令位置の公開資料なし）

~~~diff
- 00560cd0 ["COPY", "tmp:0:8", ["const:370:8"]]
- 00560cd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560cd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560cd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560d10 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00560d10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560d10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560d10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560cd0 bytes 08c10d91
+ 00560d10 bytes 08011191
- 00560d00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00560d00 ["INT_ADD", "register:40f0:8", ["const:560d00:8", "const:4:8"]]
- 00560d00 ["CALLIND", null, ["register:0:8"]]
+ 00560d40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00560d40 ["INT_ADD", "register:40f0:8", ["const:560d40:8", "const:4:8"]]
+ 00560d40 ["CALLIND", null, ["register:0:8"]]
- 00560d00 bytes 00013fd6
+ 00560d40 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4352d9d66505aed8a468dea182d1158"></a>

### [`00560d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d14.md) → [`00560d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560d54.md) FUN_00560d54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00560d80",
      "incomplete_value": false,
      "site": "00560d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560d40",
      "incomplete_value": false,
      "site": "00560d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "00560d80",
      "DATA",
      [
        "storage",
        "00c6b370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560d80",
      "DATA",
      [
        "storage",
        "00c6b440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d14.md#insn-00560d28) · [`00560d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d14.md#insn-00560d38) · [`00560d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d14.md#insn-00560d5c)
- 新版 `00560d68`（命令位置の公開資料なし） · `00560d78`（命令位置の公開資料なし） · `00560d9c`（命令位置の公開資料なし）

~~~diff
- 00560d28 ["INT_ADD", "register:40f0:8", ["const:560d28:8", "const:4:8"]]
- 00560d28 ["CALL", null, ["callee:00c57f60:8"]]
+ 00560d68 ["INT_ADD", "register:40f0:8", ["const:560d68:8", "const:4:8"]]
+ 00560d68 ["CALL", null, ["callee:00c57f60:8"]]
- 00560d28 bytes 5adc1b94
+ 00560d68 bytes 7edc1b94
- 00560d38 ["COPY", "tmp:0:8", ["const:370:8"]]
- 00560d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560d78 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00560d78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560d78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560d78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560d38 bytes 08c10d91
+ 00560d78 bytes 08011191
- 00560d5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00560d5c ["INT_ADD", "register:40f0:8", ["const:560d5c:8", "const:4:8"]]
- 00560d5c ["CALLIND", null, ["register:0:8"]]
+ 00560d9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00560d9c ["INT_ADD", "register:40f0:8", ["const:560d9c:8", "const:4:8"]]
+ 00560d9c ["CALLIND", null, ["register:0:8"]]
- 00560d5c bytes 00013fd6
+ 00560d9c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09a69cceaca175ebaafc00828208c872"></a>

### [`00560d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d9c.md) → [`00560ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560ddc.md) FUN_00560ddc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00560df8",
      "incomplete_value": true,
      "site": "00560df8",
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
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560db8",
      "incomplete_value": true,
      "site": "00560db8",
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
            "const:370:8"
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
      "00560df8",
      "DATA",
      [
        "storage",
        "00c6b370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560df8",
      "DATA",
      [
        "storage",
        "00c6b440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d9c.md#insn-00560db4) · [`00560dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d9c.md#insn-00560dd8)
- 新版 `00560df4`（命令位置の公開資料なし） · `00560e18`（命令位置の公開資料なし）

~~~diff
- 00560db4 ["COPY", "tmp:0:8", ["const:370:8"]]
- 00560db4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560db4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560db4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560df4 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00560df4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560df4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560df4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560db4 bytes 29c10d91
+ 00560df4 bytes 29011191
- 00560dd8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00560dd8 ["INT_ADD", "register:40f0:8", ["const:560dd8:8", "const:4:8"]]
- 00560dd8 ["CALLIND", null, ["register:0:8"]]
+ 00560e18 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00560e18 ["INT_ADD", "register:40f0:8", ["const:560e18:8", "const:4:8"]]
+ 00560e18 ["CALLIND", null, ["register:0:8"]]
- 00560dd8 bytes 20013fd6
+ 00560e18 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1d82aa508859cb9d623c5b75f2d5712"></a>

### [`00560ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560ee0.md) → [`00560f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560f20.md) FUN_00560f20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00560b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b08.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 1件 [`00560b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560b48.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.29% / 新版 85.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00560f38",
      "incomplete_value": false,
      "site": "00560f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560ef8",
      "incomplete_value": false,
      "site": "00560ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      "definition_site": "00560f44",
      "incomplete_value": false,
      "site": "00560f44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560f04",
      "incomplete_value": false,
      "site": "00560f04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "00560f38",
      "DATA",
      [
        "storage",
        "00c6b3f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00560f44",
      "DATA",
      [
        "storage",
        "00c6b270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560f38",
      "DATA",
      [
        "storage",
        "00c6b4c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00560f44",
      "DATA",
      [
        "storage",
        "00c6b340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560ee0.md#insn-00560ef0) · [`00560efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560ee0.md#insn-00560efc) · [`00560f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560ee0.md#insn-00560f00)
- 新版 `00560f30`（命令位置の公開資料なし） · `00560f40`（命令位置の公開資料なし）

~~~diff
- 00560ef0 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 00560ef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560ef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560ef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560f30 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00560f30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560f30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560f30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560ef0 bytes 08c10f91
+ 00560f30 bytes 08011391
- 00560efc ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00560efc bytes 483800f0
- 00560f00 ["COPY", "tmp:0:8", ["const:270:8"]]
- 00560f00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560f00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560f00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560f40 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 00560f40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560f40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560f40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560f00 bytes 08c10991
+ 00560f40 bytes 08010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fa45b083f6288835e428b82d0c7c458"></a>

### [`00560f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560f94.md) → [`00560fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560fd4.md) FUN_00560fd4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00560fd8",
      "incomplete_value": false,
      "site": "00560fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560f98",
      "incomplete_value": false,
      "site": "00560f9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      "00560fdc",
      "DATA",
      [
        "storage",
        "00c6b3f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560fdc",
      "DATA",
      [
        "storage",
        "00c6b4c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560f94.md#insn-00560f98)
- 新版 `00560fd8`（命令位置の公開資料なし）

~~~diff
- 00560f98 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 00560f98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560f98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560f98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560fd8 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00560fd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560fd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560fd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560f98 bytes 08c10f91
+ 00560fd8 bytes 08011391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7827980e7d69249c554ee9b93654ce3c"></a>

### [`00560fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560fa4.md) → [`00560fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560fe4.md) FUN_00560fe4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00560ff4",
      "incomplete_value": false,
      "site": "00560ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560fb4",
      "incomplete_value": false,
      "site": "00560fbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      "00560ffc",
      "DATA",
      [
        "storage",
        "00c6b3f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560ffc",
      "DATA",
      [
        "storage",
        "00c6b4c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560fa4.md#insn-00560fb4) · [`00560fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560fa4.md#insn-00560fc0)
- 新版 `00560ff4`（命令位置の公開資料なし） · `00561000`（命令位置の公開資料なし）

~~~diff
- 00560fb4 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 00560fb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560fb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560fb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560ff4 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00560ff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560ff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560ff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560fb4 bytes 08c10f91
+ 00560ff4 bytes 08011391
- 00560fc0 ["INT_ADD", "register:40f0:8", ["const:560fc0:8", "const:4:8"]]
- 00560fc0 ["CALL", null, ["callee:00c57f70:8"]]
+ 00561000 ["INT_ADD", "register:40f0:8", ["const:561000:8", "const:4:8"]]
+ 00561000 ["CALL", null, ["callee:00c57f70:8"]]
- 00560fc0 bytes b8db1b94
+ 00561000 bytes dcdb1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3440b12c6f8d76233e189a07d37bdc7d"></a>

### [`005610b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005610b4.md) → [`005610f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610f4.md) FUN_005610f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0045440c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md) [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) · 呼出先 14件 [`0055f578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f578.md) [`00597610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597610.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`0045444c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/0045444c.md) [`00456848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456848.md) · 呼出先 14件 [`0055f5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f5b8.md) [`00597650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597650.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.39% / 新版 96.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056114c",
      "incomplete_value": false,
      "site": "00561158",
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
            "const:46c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056110c",
      "incomplete_value": false,
      "site": "00561118",
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
            "const:42c:8"
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
      "definition_site": "005613dc",
      "incomplete_value": false,
      "site": "005613e4",
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
            "const:ce9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056139c",
      "incomplete_value": false,
      "site": "005613a4",
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
            "const:d45:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056147c",
      "incomplete_value": false,
      "site": "00561480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:209:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056143c",
      "incomplete_value": false,
      "site": "00561440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:1c9:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056114c",
      "PARAM",
      [
        "storage",
        "002b742c",
        null,
        "string"
      ]
    ],
    [
      "00561214",
      "PARAM",
      [
        "storage",
        "002bb4c2",
        null,
        "string"
      ]
    ],
    [
      "00561230",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056114c",
      "PARAM",
      [
        "storage",
        "002b746c",
        null,
        "string"
      ]
    ],
    [
      "00561214",
      "PARAM",
      [
        "storage",
        "002bb46e",
        null,
        "string"
      ]
    ],
    [
      "00561230",
      "READ",
      [
        "storage",
        "002b393f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005610b4.md#insn-00561118) · [`005613a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005610b4.md#insn-005613a4) · [`00561440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005610b4.md#insn-00561440)
- 新版 `00561158`（命令位置の公開資料なし） · `005613e4`（命令位置の公開資料なし） · `00561480`（命令位置の公開資料なし）

~~~diff
- 00561118 ["INT_ADD", "register:40f0:8", ["const:561118:8", "const:4:8"]]
- 00561118 ["CALL", null, ["callee:00c58030:8"]]
+ 00561158 ["INT_ADD", "register:40f0:8", ["const:561158:8", "const:4:8"]]
+ 00561158 ["CALL", null, ["callee:00c58030:8"]]
- 00561118 bytes 92db1b94
+ 00561158 bytes b6db1b94
- 005613a4 ["INT_ADD", "register:40f0:8", ["const:5613a4:8", "const:4:8"]]
- 005613a4 ["CALL", null, ["callee:00c58180:8"]]
+ 005613e4 ["INT_ADD", "register:40f0:8", ["const:5613e4:8", "const:4:8"]]
+ 005613e4 ["CALL", null, ["callee:00c58180:8"]]
- 005613a4 bytes 43db1b94
+ 005613e4 bytes 67db1b94
- 00561440 ["INT_ADD", "register:40f0:8", ["const:561440:8", "const:4:8"]]
- 00561440 ["CALL", null, ["callee:00c58180:8"]]
+ 00561480 ["INT_ADD", "register:40f0:8", ["const:561480:8", "const:4:8"]]
+ 00561480 ["CALL", null, ["callee:00c58180:8"]]
- 00561440 bytes 1cdb1b94
+ 00561480 bytes 40db1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee706394b5a96571244ac020fc0fc612"></a>

### [`005618a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618a8.md) → [`005618e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005618e8.md) FUN_005618e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`0045440c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md) [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`0045444c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/0045444c.md) [`00456848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456848.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00561904",
      "incomplete_value": false,
      "site": "0056190c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005618c4",
      "incomplete_value": false,
      "site": "005618cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:440:8"
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
      "0056190c",
      "DATA",
      [
        "storage",
        "00c6b440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056190c",
      "DATA",
      [
        "storage",
        "00c6b510",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005618bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618a8.md#insn-005618bc) · [`005618c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618a8.md#insn-005618c4)
- 新版 `005618fc`（命令位置の公開資料なし） · `00561904`（命令位置の公開資料なし）

~~~diff
- 005618bc ["INT_ADD", "register:40f0:8", ["const:5618bc:8", "const:4:8"]]
- 005618bc ["CALL", null, ["callee:00c57f60:8"]]
+ 005618fc ["INT_ADD", "register:40f0:8", ["const:5618fc:8", "const:4:8"]]
+ 005618fc ["CALL", null, ["callee:00c57f60:8"]]
- 005618bc bytes 75d91b94
+ 005618fc bytes 99d91b94
- 005618c4 ["COPY", "tmp:0:8", ["const:440:8"]]
- 005618c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005618c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005618c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561904 ["COPY", "tmp:0:8", ["const:510:8"]]
+ 00561904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005618c4 bytes 08011191
+ 00561904 bytes 08411491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a10055e1f41f0ca2f54fe6254ada65c"></a>

### [`005618ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618ec.md) → [`0056192c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/0056192c.md) FUN_0056192c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008d548c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md) [`008d6ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6ce0.md) · 呼出先 5件 [`00560460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560460.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`008d54e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d54e0.md) [`008d6d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6d34.md) · 呼出先 5件 [`005604a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005604a0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005619a8",
      "incomplete_value": false,
      "site": "005619b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:f3a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561968",
      "incomplete_value": false,
      "site": "00561970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:f09:8"
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
      "0056198c",
      "PARAM",
      [
        "storage",
        "002a8ad9",
        null,
        null
      ]
    ],
    [
      "005619a8",
      "PARAM",
      [
        "storage",
        "002b4f09",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0056198c",
      "PARAM",
      [
        "storage",
        "002a8a7d",
        null,
        null
      ]
    ],
    [
      "005619a8",
      "PARAM",
      [
        "storage",
        "002b4f3a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618ec.md#insn-00561970) · [`0056194c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618ec.md#insn-0056194c) · [`00561954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618ec.md#insn-00561954)
- 新版 `005619b0`（命令位置の公開資料なし） · `0056198c`（命令位置の公開資料なし） · `00561994`（命令位置の公開資料なし）

~~~diff
- 00561970 ["INT_ADD", "register:40f0:8", ["const:561970:8", "const:4:8"]]
- 00561970 ["CALL", null, ["callee:00c58040:8"]]
+ 005619b0 ["INT_ADD", "register:40f0:8", ["const:5619b0:8", "const:4:8"]]
+ 005619b0 ["CALL", null, ["callee:00c58040:8"]]
- 00561970 bytes 80d91b94
+ 005619b0 bytes a4d91b94
- 0056194c ["COPY", "tmp:0:8", ["const:ad9:8"]]
- 0056194c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056194c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056194c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056198c ["COPY", "tmp:0:8", ["const:a7d:8"]]
+ 0056198c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056198c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056198c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056194c bytes 21642b91
+ 0056198c bytes 21f42991
- 00561954 ["INT_ADD", "register:40f0:8", ["const:561954:8", "const:4:8"]]
- 00561954 ["CALL", null, ["callee:00c58040:8"]]
+ 00561994 ["INT_ADD", "register:40f0:8", ["const:561994:8", "const:4:8"]]
+ 00561994 ["CALL", null, ["callee:00c58040:8"]]
- 00561954 bytes 87d91b94
+ 00561994 bytes abd91b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3d97e52699b1992606bef673ba542f9"></a>

### [`00561b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561b24.md) → [`00561b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561b64.md) FUN_00561b64

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008d548c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md) [`008d6ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6ce0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58160.md)
- 新版 呼出元 2件 [`008d54e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d54e0.md) [`008d6d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6d34.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58230.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.37% / 新版 87.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00561bb0",
      "incomplete_value": true,
      "site": "00561bb0",
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
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:93f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561b70",
      "incomplete_value": true,
      "site": "00561b70",
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
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:90e:8"
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
      "definition_site": "00561bd0",
      "incomplete_value": true,
      "site": "00561be0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00561b90",
      "incomplete_value": true,
      "site": "00561ba0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00561bcc",
      "incomplete_value": true,
      "site": "00561be4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e11:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561b8c",
      "incomplete_value": true,
      "site": "00561ba4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e65:8"
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
      "00561b88",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ],
    [
      "00561bcc",
      "READ",
      [
        "storage",
        "002bee65",
        null,
        "string"
      ]
    ],
    [
      "00561bcc",
      "READ",
      [
        "storage",
        "002bee75",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00561b88",
      "READ",
      [
        "storage",
        "002b393f",
        null,
        "string"
      ]
    ],
    [
      "00561bcc",
      "READ",
      [
        "storage",
        "002bee11",
        null,
        "string"
      ]
    ],
    [
      "00561bcc",
      "READ",
      [
        "storage",
        "002bee21",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561b24.md#insn-00561b40) · [`00561b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561b24.md#insn-00561b7c) · [`00561b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561b24.md#insn-00561b84)
- 新版 `00561b80`（命令位置の公開資料なし） · `00561bbc`（命令位置の公開資料なし） · `00561bc4`（命令位置の公開資料なし）

~~~diff
- 00561b40 ["COPY", "tmp:0:8", ["const:90e:8"]]
- 00561b40 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00561b40 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00561b40 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00561b80 ["COPY", "tmp:0:8", ["const:93f:8"]]
+ 00561b80 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00561b80 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00561b80 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00561b40 bytes 4a392491
+ 00561b80 bytes 4afd2491
- 00561b7c ["INT_ADD", "register:40f0:8", ["const:561b7c:8", "const:4:8"]]
- 00561b7c ["CALL", null, ["callee:00c57f60:8"]]
+ 00561bbc ["INT_ADD", "register:40f0:8", ["const:561bbc:8", "const:4:8"]]
+ 00561bbc ["CALL", null, ["callee:00c57f60:8"]]
- 00561b7c bytes c5d81b94
+ 00561bbc bytes e9d81b94
- 00561b84 ["COPY", "tmp:0:8", ["const:e65:8"]]
- 00561b84 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00561b84 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00561b84 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00561bc4 ["COPY", "tmp:0:8", ["const:e11:8"]]
+ 00561bc4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00561bc4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00561bc4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00561b84 bytes 4a953991
+ 00561bc4 bytes 4a453891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f97bfec1c4d696bc463003c7f6345b78"></a>

### [`00561cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561cec.md) → [`00561d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d2c.md) FUN_00561d2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`008d548c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md) [`008d6ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6ce0.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`008d54e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d54e0.md) [`008d6d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6d34.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00561d48",
      "incomplete_value": false,
      "site": "00561d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561d08",
      "incomplete_value": false,
      "site": "00561d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "00561d50",
      "DATA",
      [
        "storage",
        "00c6b490",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00561d50",
      "DATA",
      [
        "storage",
        "00c6b560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561cec.md#insn-00561d00) · [`00561d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561cec.md#insn-00561d08)
- 新版 `00561d40`（命令位置の公開資料なし） · `00561d48`（命令位置の公開資料なし）

~~~diff
- 00561d00 ["INT_ADD", "register:40f0:8", ["const:561d00:8", "const:4:8"]]
- 00561d00 ["CALL", null, ["callee:00c57f60:8"]]
+ 00561d40 ["INT_ADD", "register:40f0:8", ["const:561d40:8", "const:4:8"]]
+ 00561d40 ["CALL", null, ["callee:00c57f60:8"]]
- 00561d00 bytes 64d81b94
+ 00561d40 bytes 88d81b94
- 00561d08 ["COPY", "tmp:0:8", ["const:490:8"]]
- 00561d08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561d08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561d08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561d48 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 00561d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561d08 bytes 08411291
+ 00561d48 bytes 08811591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-738c6cb844d41a45cc4cdc306b006126"></a>

### [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) → [`00561d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md) FUN_00561d74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 21件 [`0043dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dfb0.md) [`0043e578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e578.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`0044f948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f948.md) [`0044fd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fd0c.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00563750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563750.md) [`00585324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585324.md) [`00597644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597644.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 21件 [`0043dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md) [`0043e5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e5b8.md) [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`0044f988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f988.md) [`0044fd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fd4c.md) · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00563790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563790.md) [`00585364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585364.md) [`00597684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597684.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00561e34",
      "incomplete_value": false,
      "site": "00561e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561df4",
      "incomplete_value": false,
      "site": "00561df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00561db8",
      "incomplete_value": true,
      "site": "00561db8",
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
      "definition_site": "00561d78",
      "incomplete_value": true,
      "site": "00561d78",
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
      "00561db4",
      "READ",
      [
        "storage",
        "00ca5cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00561e34",
      "DATA",
      [
        "storage",
        "00c6b4e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00561ec0",
      "READ",
      [
        "storage",
        "00c6b508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00561db4",
      "READ",
      [
        "storage",
        "00ca5dc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00561e34",
      "DATA",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00561ec0",
      "READ",
      [
        "storage",
        "00c6b5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md#insn-00561d74) · [`00561da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md#insn-00561da0) · [`00561dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md#insn-00561dcc)
- 新版 `00561db4`（命令位置の公開資料なし） · `00561de0`（命令位置の公開資料なし） · `00561e0c`（命令位置の公開資料なし）

~~~diff
- 00561d74 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cc0:8"]]
- 00561d74 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00561db4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dc0:8"]]
+ 00561db4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00561d74 bytes 296146f9
+ 00561db4 bytes 29e146f9
- 00561da0 ["INT_ADD", "register:40f0:8", ["const:561da0:8", "const:4:8"]]
- 00561da0 ["CALL", null, ["callee:0043bb60:8"]]
+ 00561de0 ["INT_ADD", "register:40f0:8", ["const:561de0:8", "const:4:8"]]
+ 00561de0 ["CALL", null, ["callee:0043bb60:8"]]
- 00561da0 bytes 6067fb97
+ 00561de0 bytes 6067fb97
- 00561dcc ["INT_ADD", "register:40f0:8", ["const:561dcc:8", "const:4:8"]]
- 00561dcc ["CALL", null, ["callee:0043bb60:8"]]
+ 00561e0c ["INT_ADD", "register:40f0:8", ["const:561e0c:8", "const:4:8"]]
+ 00561e0c ["CALL", null, ["callee:0043bb60:8"]]
- 00561dcc bytes 5567fb97
+ 00561e0c bytes 5567fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0fe38db270c50132f53fc3ad6893141"></a>

### [`00561fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561fd0.md) → [`00562010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562010.md) FUN_00562010

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0043dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dfb0.md) [`00458af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md) [`0097f894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f894.md) · 呼出先 10件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`005626f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/005626f4.md) [`005647e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647e0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`0043dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md) [`00458b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458b30.md) [`0097f8e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097f/0097f8e8.md) · 呼出先 10件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00562734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562734.md) [`00564820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564820.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.46% / 新版 99.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00562428",
      "incomplete_value": false,
      "site": "00562434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005623e8",
      "incomplete_value": false,
      "site": "005623f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00562434",
      "DATA",
      [
        "storage",
        "00c6b620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00562434",
      "DATA",
      [
        "storage",
        "00c6b6f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056203c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561fd0.md#insn-0056203c) · [`0056204c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561fd0.md#insn-0056204c) · [`00562078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561fd0.md#insn-00562078)
- 新版 `0056207c`（命令位置の公開資料なし） · `0056208c`（命令位置の公開資料なし） · `005620b8`（命令位置の公開資料なし）

~~~diff
- 0056203c ["INT_ADD", "register:40f0:8", ["const:56203c:8", "const:4:8"]]
- 0056203c ["CALL", null, ["callee:00562734:8"]]
+ 0056207c ["INT_ADD", "register:40f0:8", ["const:56207c:8", "const:4:8"]]
+ 0056207c ["CALL", null, ["callee:00562734:8"]]
- 0056203c bytes ae010094
+ 0056207c bytes ae010094
- 0056204c ["INT_ADD", "register:40f0:8", ["const:56204c:8", "const:4:8"]]
- 0056204c ["CALL", null, ["callee:00c57f80:8"]]
+ 0056208c ["INT_ADD", "register:40f0:8", ["const:56208c:8", "const:4:8"]]
+ 0056208c ["CALL", null, ["callee:00c57f80:8"]]
- 0056204c bytes 99d71b94
+ 0056208c bytes bdd71b94
- 00562078 ["INT_ADD", "register:40f0:8", ["const:562078:8", "const:4:8"]]
- 00562078 ["CALL", null, ["callee:00c58500:8"]]
+ 005620b8 ["INT_ADD", "register:40f0:8", ["const:5620b8:8", "const:4:8"]]
+ 005620b8 ["CALL", null, ["callee:00c58500:8"]]
- 00562078 bytes eed81b94
+ 005620b8 bytes 12d91b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3f63683d39781a96c9ca442b4137bdb"></a>

### [`00562cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cdc.md) → [`00562d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d1c.md) FUN_00562d1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00562d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562d90.md) [`00563098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563098.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`00562dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562dd0.md) [`005630d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005630d8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00562d28",
      "incomplete_value": false,
      "site": "00562d2c",
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
      "definition_site": "00562ce8",
      "incomplete_value": false,
      "site": "00562cec",
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
      "00562d28",
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
      "00562d28",
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

- 旧版 [`00562cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cdc.md#insn-00562cec) · [`00562ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cdc.md#insn-00562ce8)
- 新版 `00562d2c`（命令位置の公開資料なし） · `00562d28`（命令位置の公開資料なし）

~~~diff
- 00562cec ["INT_ADD", "register:40f0:8", ["const:562cec:8", "const:4:8"]]
- 00562cec ["CALL", null, ["callee:0043b7b8:8"]]
+ 00562d2c ["INT_ADD", "register:40f0:8", ["const:562d2c:8", "const:4:8"]]
+ 00562d2c ["CALL", null, ["callee:0043b7b8:8"]]
- 00562cec bytes a362fb97
+ 00562d2c bytes a362fb97
- 00562ce8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00562ce8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00562ce8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00562ce8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00562d28 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00562d28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00562d28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00562d28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00562ce8 bytes 00303d91
+ 00562d28 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-051cd1f01d7cbdb0b00611d6ffbcaaaf"></a>

### [`005633e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005633e4.md) → [`00563424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563424.md) FUN_00563424

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00563428",
      "incomplete_value": false,
      "site": "0056342c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005633e8",
      "incomplete_value": false,
      "site": "005633ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:440:8"
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
      "0056342c",
      "DATA",
      [
        "storage",
        "00c6b440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056342c",
      "DATA",
      [
        "storage",
        "00c6b510",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005633e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005633e4.md#insn-005633e8)
- 新版 `00563428`（命令位置の公開資料なし）

~~~diff
- 005633e8 ["COPY", "tmp:0:8", ["const:440:8"]]
- 005633e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005633e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005633e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563428 ["COPY", "tmp:0:8", ["const:510:8"]]
+ 00563428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005633e8 bytes 08011191
+ 00563428 bytes 08411491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f69179eb3b1646e793e2db14fb00cf19"></a>

### [`005633f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005633f4.md) → [`00563434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563434.md) FUN_00563434

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00563444",
      "incomplete_value": false,
      "site": "0056344c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563404",
      "incomplete_value": false,
      "site": "0056340c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:440:8"
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
      "0056344c",
      "DATA",
      [
        "storage",
        "00c6b440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056344c",
      "DATA",
      [
        "storage",
        "00c6b510",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005633f4.md#insn-00563404) · [`00563410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005633f4.md#insn-00563410)
- 新版 `00563444`（命令位置の公開資料なし） · `00563450`（命令位置の公開資料なし）

~~~diff
- 00563404 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00563404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563444 ["COPY", "tmp:0:8", ["const:510:8"]]
+ 00563444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563404 bytes 08011191
+ 00563444 bytes 08411491
- 00563410 ["INT_ADD", "register:40f0:8", ["const:563410:8", "const:4:8"]]
- 00563410 ["CALL", null, ["callee:00c57f70:8"]]
+ 00563450 ["INT_ADD", "register:40f0:8", ["const:563450:8", "const:4:8"]]
+ 00563450 ["CALL", null, ["callee:00c57f70:8"]]
- 00563410 bytes a4d21b94
+ 00563450 bytes c8d21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da4204cf181d3dd5ec2db114c126209d"></a>

### [`00563494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563494.md) → [`005634d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005634d4.md) FUN_005634d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005634d8",
      "incomplete_value": false,
      "site": "005634dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563498",
      "incomplete_value": false,
      "site": "0056349c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "005634dc",
      "DATA",
      [
        "storage",
        "00c6b490",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005634dc",
      "DATA",
      [
        "storage",
        "00c6b560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563494.md#insn-00563498)
- 新版 `005634d8`（命令位置の公開資料なし）

~~~diff
- 00563498 ["COPY", "tmp:0:8", ["const:490:8"]]
- 00563498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005634d8 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 005634d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005634d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005634d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563498 bytes 08411291
+ 005634d8 bytes 08811591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b76f1e9e54f0f67b03ab59a240ff9fab"></a>

### [`005634a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005634a4.md) → [`005634e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005634e4.md) FUN_005634e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005634f4",
      "incomplete_value": false,
      "site": "005634fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005634b4",
      "incomplete_value": false,
      "site": "005634bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "005634fc",
      "DATA",
      [
        "storage",
        "00c6b490",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005634fc",
      "DATA",
      [
        "storage",
        "00c6b560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005634b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005634a4.md#insn-005634b4) · [`005634c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005634a4.md#insn-005634c0)
- 新版 `005634f4`（命令位置の公開資料なし） · `00563500`（命令位置の公開資料なし）

~~~diff
- 005634b4 ["COPY", "tmp:0:8", ["const:490:8"]]
- 005634b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005634b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005634b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005634f4 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 005634f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005634f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005634f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005634b4 bytes 08411291
+ 005634f4 bytes 08811591
- 005634c0 ["INT_ADD", "register:40f0:8", ["const:5634c0:8", "const:4:8"]]
- 005634c0 ["CALL", null, ["callee:00c57f70:8"]]
+ 00563500 ["INT_ADD", "register:40f0:8", ["const:563500:8", "const:4:8"]]
+ 00563500 ["CALL", null, ["callee:00c57f70:8"]]
- 005634c0 bytes 78d21b94
+ 00563500 bytes 9cd21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-820d93ba7d536428d667b42f897b96ad"></a>

### [`005634ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005634ec.md) → [`0056352c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056352c.md) FUN_0056352c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00563544",
      "incomplete_value": false,
      "site": "00563548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563504",
      "incomplete_value": false,
      "site": "00563508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
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
      "00563548",
      "DATA",
      [
        "storage",
        "00c6b4e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563548",
      "DATA",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005634ec.md#insn-00563504) · [`00563514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005634ec.md#insn-00563514)
- 新版 `00563544`（命令位置の公開資料なし） · `00563554`（命令位置の公開資料なし）

~~~diff
- 00563504 ["COPY", "tmp:0:8", ["const:4e0:8"]]
- 00563504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00563504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00563504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00563544 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 00563544 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00563544 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00563544 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00563504 bytes 29811391
+ 00563544 bytes 29c11691
- 00563514 ["INT_ADD", "register:40f0:8", ["const:563514:8", "const:4:8"]]
- 00563514 ["CALL", null, ["callee:00c57f80:8"]]
+ 00563554 ["INT_ADD", "register:40f0:8", ["const:563554:8", "const:4:8"]]
+ 00563554 ["CALL", null, ["callee:00c57f80:8"]]
- 00563514 bytes 67d21b94
+ 00563554 bytes 8bd21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af00324d509443be39384fcbffbded7c"></a>

### [`0056353c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056353c.md) → [`0056357c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056357c.md) FUN_0056357c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00563594",
      "incomplete_value": false,
      "site": "00563598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563554",
      "incomplete_value": false,
      "site": "00563558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
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
      "00563598",
      "DATA",
      [
        "storage",
        "00c6b4e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563598",
      "DATA",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056353c.md#insn-00563554) · [`00563564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056353c.md#insn-00563564) · [`00563574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056353c.md#insn-00563574)
- 新版 `00563594`（命令位置の公開資料なし） · `005635a4`（命令位置の公開資料なし） · `005635b4`（命令位置の公開資料なし）

~~~diff
- 00563554 ["COPY", "tmp:0:8", ["const:4e0:8"]]
- 00563554 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00563554 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00563554 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00563594 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 00563594 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00563594 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00563594 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00563554 bytes 29811391
+ 00563594 bytes 29c11691
- 00563564 ["INT_ADD", "register:40f0:8", ["const:563564:8", "const:4:8"]]
- 00563564 ["CALL", null, ["callee:00c57f80:8"]]
+ 005635a4 ["INT_ADD", "register:40f0:8", ["const:5635a4:8", "const:4:8"]]
+ 005635a4 ["CALL", null, ["callee:00c57f80:8"]]
- 00563564 bytes 53d21b94
+ 005635a4 bytes 77d21b94
- 00563574 ["INT_ADD", "register:40f0:8", ["const:563574:8", "const:4:8"]]
- 00563574 ["CALL", null, ["callee:00c57f80:8"]]
+ 005635b4 ["INT_ADD", "register:40f0:8", ["const:5635b4:8", "const:4:8"]]
+ 005635b4 ["CALL", null, ["callee:00c57f80:8"]]
- 00563574 bytes 4fd21b94
+ 005635b4 bytes 73d21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcf080136b5e884d2f23b75a494469aa"></a>

### [`00563588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563588.md) → [`005635c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005635c8.md) FUN_005635c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005635fc",
      "incomplete_value": false,
      "site": "005635fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005635bc",
      "incomplete_value": false,
      "site": "005635bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
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
      "005635fc",
      "DATA",
      [
        "storage",
        "00c6b4e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005635fc",
      "DATA",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005635a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563588.md#insn-005635a0) · [`005635b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563588.md#insn-005635b0) · [`005635b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563588.md#insn-005635b8)
- 新版 `005635e0`（命令位置の公開資料なし） · `005635f0`（命令位置の公開資料なし）

~~~diff
- 005635a0 ["INT_ADD", "register:40f0:8", ["const:5635a0:8", "const:4:8"]]
- 005635a0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005635e0 ["INT_ADD", "register:40f0:8", ["const:5635e0:8", "const:4:8"]]
+ 005635e0 ["CALL", null, ["callee:00c57f60:8"]]
- 005635a0 bytes 3cd21b94
+ 005635e0 bytes 60d21b94
- 005635b0 ["COPY", "tmp:0:8", ["const:4e0:8"]]
- 005635b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005635b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005635b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005635f0 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 005635f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005635f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005635f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005635b0 bytes 4a811391
+ 005635f0 bytes 4ac11691
- 005635b8 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 005635b8 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13e32bb6bb4a1ca5fea2382130d6ac90"></a>

### [`00563790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563790.md) → [`005637d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005637d0.md) FUN_005637d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005637fc",
      "incomplete_value": true,
      "site": "005637fc",
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
      "definition_site": "005637bc",
      "incomplete_value": true,
      "site": "005637bc",
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
      "005637f4",
      "READ",
      [
        "storage",
        "00ca5cc0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005637f4",
      "READ",
      [
        "storage",
        "00ca5dc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005637b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563790.md#insn-005637b4) · [`005637d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563790.md#insn-005637d8) · [`0056380c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563790.md#insn-0056380c)
- 新版 `005637f4`（命令位置の公開資料なし） · `00563818`（命令位置の公開資料なし） · `0056384c`（命令位置の公開資料なし）

~~~diff
- 005637b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 005637b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005637f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 005637f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005637b4 bytes 086146f9
+ 005637f4 bytes 08e146f9
- 005637d8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005637d8 ["INT_ADD", "register:40f0:8", ["const:5637d8:8", "const:4:8"]]
- 005637d8 ["CALLIND", null, ["register:0:8"]]
+ 00563818 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00563818 ["INT_ADD", "register:40f0:8", ["const:563818:8", "const:4:8"]]
+ 00563818 ["CALLIND", null, ["register:0:8"]]
- 005637d8 bytes 20013fd6
+ 00563818 bytes 20013fd6
- 0056380c ["INT_ADD", "register:40f0:8", ["const:56380c:8", "const:4:8"]]
- 0056380c ["CALL", null, ["callee:00459db4:8"]]
+ 0056384c ["INT_ADD", "register:40f0:8", ["const:56384c:8", "const:4:8"]]
+ 0056384c ["CALL", null, ["callee:00459db4:8"]]
- 0056380c bytes 5ad9fb97
+ 0056384c bytes 5ad9fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f14205ffa3be7148c3a4126c3c428812"></a>

### [`0056383c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056383c.md) → [`0056387c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056387c.md) FUN_0056387c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00563880",
      "incomplete_value": false,
      "site": "00563884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563840",
      "incomplete_value": false,
      "site": "00563844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:560:8"
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
      "00563884",
      "DATA",
      [
        "storage",
        "00c6b560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563884",
      "DATA",
      [
        "storage",
        "00c6b630",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056383c.md#insn-00563840)
- 新版 `00563880`（命令位置の公開資料なし）

~~~diff
- 00563840 ["COPY", "tmp:0:8", ["const:560:8"]]
- 00563840 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563840 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563840 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563880 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00563880 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563880 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563880 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563840 bytes 08811591
+ 00563880 bytes 08c11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ac11c223f966ed912b2d2f99f25c598"></a>

### [`0056384c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056384c.md) → [`0056388c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056388c.md) FUN_0056388c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0056389c",
      "incomplete_value": false,
      "site": "005638a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056385c",
      "incomplete_value": false,
      "site": "00563864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:560:8"
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
      "005638a4",
      "DATA",
      [
        "storage",
        "00c6b560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005638a4",
      "DATA",
      [
        "storage",
        "00c6b630",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056385c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056384c.md#insn-0056385c) · [`00563868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056384c.md#insn-00563868)
- 新版 `0056389c`（命令位置の公開資料なし） · `005638a8`（命令位置の公開資料なし）

~~~diff
- 0056385c ["COPY", "tmp:0:8", ["const:560:8"]]
- 0056385c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056385c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056385c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056389c ["COPY", "tmp:0:8", ["const:630:8"]]
+ 0056389c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056389c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056389c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056385c bytes 08811591
+ 0056389c bytes 08c11891
- 00563868 ["INT_ADD", "register:40f0:8", ["const:563868:8", "const:4:8"]]
- 00563868 ["CALL", null, ["callee:00c57f70:8"]]
+ 005638a8 ["INT_ADD", "register:40f0:8", ["const:5638a8:8", "const:4:8"]]
+ 005638a8 ["CALL", null, ["callee:00c57f70:8"]]
- 00563868 bytes 8ed11b94
+ 005638a8 bytes b2d11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bef0a13767ad1d0e7862f631d3927bf"></a>

### [`0056387c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056387c.md) → [`005638bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005638bc.md) FUN_005638bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005638cc",
      "incomplete_value": false,
      "site": "005638d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056388c",
      "incomplete_value": false,
      "site": "00563890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
      "005638d0",
      "DATA",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005638d0",
      "DATA",
      [
        "storage",
        "00c6b680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056388c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056387c.md#insn-0056388c)
- 新版 `005638cc`（命令位置の公開資料なし）

~~~diff
- 0056388c ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 0056388c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056388c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056388c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005638cc ["COPY", "tmp:0:8", ["const:680:8"]]
+ 005638cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005638cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005638cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056388c bytes 29c11691
+ 005638cc bytes 29011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15963ab9fa426b0a5d15efcce70e70a8"></a>

### [`0056389c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056389c.md) → [`005638dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005638dc.md) FUN_005638dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00565314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565314.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005626f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/005626f4.md) [`00563b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563b04.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00565354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565354.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00562734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562734.md) [`00563b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563b44.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00563908",
      "incomplete_value": false,
      "site": "00563924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005638c8",
      "incomplete_value": false,
      "site": "005638e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "00563924",
      "DATA",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005639d4",
      "READ",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563924",
      "DATA",
      [
        "storage",
        "00c6b680",
        null,
        "undefined *"
      ]
    ],
    [
      "005639d4",
      "READ",
      [
        "storage",
        "00c6b680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005638c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056389c.md#insn-005638c8) · [`00563908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056389c.md#insn-00563908) · [`00563918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056389c.md#insn-00563918)
- 新版 `00563908`（命令位置の公開資料なし） · `00563948`（命令位置の公開資料なし） · `00563958`（命令位置の公開資料なし）

~~~diff
- 005638c8 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 005638c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005638c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005638c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00563908 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 00563908 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00563908 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00563908 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005638c8 bytes 4ac11691
+ 00563908 bytes 4a011a91
- 00563908 ["INT_ADD", "register:40f0:8", ["const:563908:8", "const:4:8"]]
- 00563908 ["CALL", null, ["callee:00562734:8"]]
+ 00563948 ["INT_ADD", "register:40f0:8", ["const:563948:8", "const:4:8"]]
+ 00563948 ["CALL", null, ["callee:00562734:8"]]
- 00563908 bytes 7bfbff97
+ 00563948 bytes 7bfbff97
- 00563918 ["INT_ADD", "register:40f0:8", ["const:563918:8", "const:4:8"]]
- 00563918 ["CALL", null, ["callee:00c57f80:8"]]
+ 00563958 ["INT_ADD", "register:40f0:8", ["const:563958:8", "const:4:8"]]
+ 00563958 ["CALL", null, ["callee:00c57f80:8"]]
- 00563918 bytes 66d11b94
+ 00563958 bytes 8ad11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-253d185d8ea3a5a2758d3729a7f98e69"></a>

### [`00564588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564588.md) → [`005645c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005645c8.md) FUN_005645c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00563e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563e30.md) [`00864ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864ce0.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) [`0091a294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0091a/0091a294.md) [`00a43138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a43/00a43138.md) · 呼出先 9件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md)
- 新版 呼出元 5件 [`00563e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563e70.md) [`00864d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864d38.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) [`0091a2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0091a/0091a2e8.md) [`00a4318c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a43/00a4318c.md) · 呼出先 9件 [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md)

変更の種類 constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.96% / 新版 91.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00564610",
      "incomplete_value": true,
      "site": "00564620",
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
      "definition_site": "005645d0",
      "incomplete_value": true,
      "site": "005645e0",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00564618",
      "incomplete_value": true,
      "site": "00564624",
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
              "LOAD",
              [
                "leaf",
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005645d8",
      "incomplete_value": true,
      "site": "005645e4",
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
              "LOAD",
              [
                "leaf",
                "const:8:8"
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
      "definition_site": "00564678",
      "incomplete_value": true,
      "site": "0056467c",
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
      "definition_site": "00564638",
      "incomplete_value": true,
      "site": "0056463c",
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
      "unmatched:005645c0",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00564618",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00564618",
      "READ",
      [
        "storage",
        "00c93210",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "005645fc",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00564618",
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00564618",
      "READ",
      [
        "storage",
        "00c932e0",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564588.md#insn-00564624) · [`005645bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564588.md#insn-005645bc) · [`005645c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564588.md#insn-005645c0)
- 新版 `00564664`（命令位置の公開資料なし） · `00564600`（命令位置の公開資料なし）

~~~diff
- 00564624 ["INT_ADD", "register:40f0:8", ["const:564624:8", "const:4:8"]]
- 00564624 ["CALL", null, ["callee:00c582c0:8"]]
+ 00564664 ["INT_ADD", "register:40f0:8", ["const:564664:8", "const:4:8"]]
+ 00564664 ["CALL", null, ["callee:00c582c0:8"]]
- 00564624 bytes f3ce1b94
+ 00564664 bytes 17cf1b94
- 005645bc ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c88:8"]]
- 005645bc ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00564600 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:c88:8"]]
+ 00564600 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 005645bc bytes 5a4746f9
+ 00564600 bytes 394746f9
- 005645c0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:bb8:8"]]
- 005645c0 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 005645c0 bytes 39df45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39fb33f7ad75422c7855db8a6763f2f2"></a>

### [`00564794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564794.md) → [`005647d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005647d4.md) FUN_005647d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005647d8",
      "incomplete_value": false,
      "site": "005647dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564798",
      "incomplete_value": false,
      "site": "0056479c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
      "005647dc",
      "DATA",
      [
        "storage",
        "00c6b620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005647dc",
      "DATA",
      [
        "storage",
        "00c6b6f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564794.md#insn-00564798)
- 新版 `005647d8`（命令位置の公開資料なし）

~~~diff
- 00564798 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00564798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005647d8 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 005647d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005647d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005647d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564798 bytes 08811891
+ 005647d8 bytes 08c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7ad8d596aed31ca51bf035183d7a7a2"></a>

### [`005647a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647a4.md) → [`005647e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005647e4.md) FUN_005647e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005647f4",
      "incomplete_value": false,
      "site": "005647fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005647b4",
      "incomplete_value": false,
      "site": "005647bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
      "005647fc",
      "DATA",
      [
        "storage",
        "00c6b620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005647fc",
      "DATA",
      [
        "storage",
        "00c6b6f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005647b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647a4.md#insn-005647b4) · [`005647c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647a4.md#insn-005647c0)
- 新版 `005647f4`（命令位置の公開資料なし） · `00564800`（命令位置の公開資料なし）

~~~diff
- 005647b4 ["COPY", "tmp:0:8", ["const:620:8"]]
- 005647b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005647b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005647b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005647f4 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 005647f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005647f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005647f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005647b4 bytes 08811891
+ 005647f4 bytes 08c11b91
- 005647c0 ["INT_ADD", "register:40f0:8", ["const:5647c0:8", "const:4:8"]]
- 005647c0 ["CALL", null, ["callee:00c57f70:8"]]
+ 00564800 ["INT_ADD", "register:40f0:8", ["const:564800:8", "const:4:8"]]
+ 00564800 ["CALL", null, ["callee:00c57f70:8"]]
- 005647c0 bytes b8cd1b94
+ 00564800 bytes dccd1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17ce9532b68b686a77d770616ff4c5a6"></a>

### [`005647e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647e0.md) → [`00564820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564820.md) FUN_00564820

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00561fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561fd0.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 1件 [`00562010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562010.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00564844",
      "incomplete_value": false,
      "site": "00564844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564804",
      "incomplete_value": false,
      "site": "00564804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "00564844",
      "DATA",
      [
        "storage",
        "00c6b670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564844",
      "DATA",
      [
        "storage",
        "00c6b740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005647fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647e0.md#insn-005647fc) · [`00564800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647e0.md#insn-00564800)
- 新版 `0056483c`（命令位置の公開資料なし） · `00564840`（命令位置の公開資料なし）

~~~diff
- 005647fc ["COPY", "tmp:0:8", ["const:670:8"]]
- 005647fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005647fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005647fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056483c ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0056483c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056483c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056483c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005647fc bytes 08c11991
+ 0056483c bytes 08011d91
- 00564800 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00564800 bytes f40300aa
+ 00564840 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 00564840 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25dbfa153396a98ff0bc5d16551f4682"></a>

### [`00564d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564d4c.md) → [`00564d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564d8c.md) FUN_00564d8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00564e0c",
      "incomplete_value": false,
      "site": "00564e14",
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
            "const:cfe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564dcc",
      "incomplete_value": false,
      "site": "00564dd4",
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
            "const:ccd:8"
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
      "definition_site": "00564fe4",
      "incomplete_value": false,
      "site": "00564ff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a7000:8"
          ],
          [
            "leaf",
            "const:8ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564fa4",
      "incomplete_value": false,
      "site": "00564fb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a7000:8"
          ],
          [
            "leaf",
            "const:94a:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00564e0c",
      "PARAM",
      [
        "storage",
        "002b2ccd",
        null,
        null
      ]
    ],
    [
      "00564f48",
      "PARAM",
      [
        "storage",
        "002a20cd",
        null,
        null
      ]
    ],
    [
      "00564fe4",
      "PARAM",
      [
        "storage",
        "002a794a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00564e0c",
      "PARAM",
      [
        "storage",
        "002b2cfe",
        null,
        null
      ]
    ],
    [
      "00564f48",
      "PARAM",
      [
        "storage",
        "002a2080",
        null,
        null
      ]
    ],
    [
      "00564fe4",
      "PARAM",
      [
        "storage",
        "002a78ee",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564d4c.md#insn-00564dd4) · [`00564f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564d4c.md#insn-00564f70) · [`00564fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564d4c.md#insn-00564fb0)
- 新版 `00564e14`（命令位置の公開資料なし） · `00564fb0`（命令位置の公開資料なし） · `00564ff0`（命令位置の公開資料なし）

~~~diff
- 00564dd4 ["INT_ADD", "register:40f0:8", ["const:564dd4:8", "const:4:8"]]
- 00564dd4 ["CALL", null, ["callee:00c58040:8"]]
+ 00564e14 ["INT_ADD", "register:40f0:8", ["const:564e14:8", "const:4:8"]]
+ 00564e14 ["CALL", null, ["callee:00c58040:8"]]
- 00564dd4 bytes 67cc1b94
+ 00564e14 bytes 8bcc1b94
- 00564f70 ["INT_ADD", "register:40f0:8", ["const:564f70:8", "const:4:8"]]
- 00564f70 ["CALL", null, ["callee:00c57f80:8"]]
+ 00564fb0 ["INT_ADD", "register:40f0:8", ["const:564fb0:8", "const:4:8"]]
+ 00564fb0 ["CALL", null, ["callee:00c57f80:8"]]
- 00564f70 bytes d0cb1b94
+ 00564fb0 bytes f4cb1b94
- 00564fb0 ["INT_ADD", "register:40f0:8", ["const:564fb0:8", "const:4:8"]]
- 00564fb0 ["CALL", null, ["callee:00c58030:8"]]
+ 00564ff0 ["INT_ADD", "register:40f0:8", ["const:564ff0:8", "const:4:8"]]
+ 00564ff0 ["CALL", null, ["callee:00c58030:8"]]
- 00564fb0 bytes eccb1b94
+ 00564ff0 bytes 10cc1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b54be327a15e4406a2f8a3c4e869f47"></a>

### [`005653e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005653e4.md) → [`00565424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565424.md) FUN_00565424

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005647d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647d4.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00564814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564814.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0056543c",
      "incomplete_value": false,
      "site": "00565440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005653fc",
      "incomplete_value": false,
      "site": "00565400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "00565440",
      "DATA",
      [
        "storage",
        "00c6b670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565440",
      "DATA",
      [
        "storage",
        "00c6b740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005653fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005653e4.md#insn-005653fc) · [`00565410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005653e4.md#insn-00565410) · [`00565458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005653e4.md#insn-00565458)
- 新版 `0056543c`（命令位置の公開資料なし） · `00565450`（命令位置の公開資料なし） · `00565498`（命令位置の公開資料なし）

~~~diff
- 005653fc ["COPY", "tmp:0:8", ["const:670:8"]]
- 005653fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005653fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005653fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056543c ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0056543c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056543c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056543c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005653fc bytes 08c11991
+ 0056543c bytes 08011d91
- 00565410 ["INT_ADD", "register:40f0:8", ["const:565410:8", "const:4:8"]]
- 00565410 ["CALL", null, ["callee:00c53da0:8"]]
+ 00565450 ["INT_ADD", "register:40f0:8", ["const:565450:8", "const:4:8"]]
+ 00565450 ["CALL", null, ["callee:00c53da0:8"]]
- 00565410 bytes 3cba1b94
+ 00565450 bytes 54ba1b94
- 00565458 ["COPY", "register:0:8", ["register:4040:8"]]
- 00565458 ["INT_ADD", "register:40f0:8", ["const:565458:8", "const:4:8"]]
- 00565458 ["CALLIND", null, ["register:0:8"]]
+ 00565498 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00565498 ["INT_ADD", "register:40f0:8", ["const:565498:8", "const:4:8"]]
+ 00565498 ["CALLIND", null, ["register:0:8"]]
- 00565458 bytes 00013fd6
+ 00565498 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03fa241994ef859542e86e8bdf80efea"></a>

### [`005654bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005654bc.md) → [`005654fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005654fc.md) _INIT_27

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00560fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560fe4.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00561024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561024.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 52.00% / 新版 52.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 10件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00565524",
      "incomplete_value": false,
      "site": "00565524",
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
                "const:da0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005654e4",
      "incomplete_value": false,
      "site": "005654e4",
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
                "const:ca0:8"
              ]
            ]
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00565544",
      "incomplete_value": false,
      "site": "00565544",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565504",
      "incomplete_value": false,
      "site": "00565504",
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
            "const:cd0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056554c",
      "incomplete_value": false,
      "site": "0056554c",
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
                "const:dd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056550c",
      "incomplete_value": false,
      "site": "0056550c",
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
                "const:cd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:1:8"
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
      "00565514",
      "PARAM",
      [
        "storage",
        "00ca5ca0",
        null,
        null
      ]
    ],
    [
      "0056551c",
      "PARAM",
      [
        "storage",
        "00560fe4",
        null,
        null
      ]
    ],
    [
      "00565520",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00565514",
      "PARAM",
      [
        "storage",
        "00ca5da0",
        null,
        null
      ]
    ],
    [
      "0056551c",
      "PARAM",
      [
        "storage",
        "00561024",
        null,
        null
      ]
    ],
    [
      "00565520",
      "PARAM",
      [
        "storage",
        "00c63060",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005654cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005654bc.md#insn-005654cc) · [`005654e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005654bc.md#insn-005654e8) · [`00565518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005654bc.md#insn-00565518)
- 新版 `0056550c`（命令位置の公開資料なし） · `00565528`（命令位置の公開資料なし） · `00565558`（命令位置の公開資料なし）

~~~diff
- 005654cc ["COPY", "tmp:0:8", ["const:f90:8"]]
- 005654cc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005654cc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005654cc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0056550c ["COPY", "tmp:0:8", ["const:60:8"]]
+ 0056550c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0056550c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0056550c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005654cc bytes 73423e91
+ 0056550c bytes 73820191
- 005654e8 ["INT_ADD", "register:40f0:8", ["const:5654e8:8", "const:4:8"]]
- 005654e8 ["CALL", null, ["callee:00c57f00:8"]]
+ 00565528 ["INT_ADD", "register:40f0:8", ["const:565528:8", "const:4:8"]]
+ 00565528 ["CALL", null, ["callee:00c57f00:8"]]
- 005654e8 bytes 52ca1b94
+ 00565528 bytes 76ca1b94
- 00565518 ["INT_ADD", "register:40f0:8", ["const:565518:8", "const:4:8"]]
- 00565518 ["CALL", null, ["callee:00c57f00:8"]]
+ 00565558 ["INT_ADD", "register:40f0:8", ["const:565558:8", "const:4:8"]]
+ 00565558 ["CALL", null, ["callee:00c57f00:8"]]
- 00565518 bytes 46ca1b94
+ 00565558 bytes 6aca1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b97fb9076009d4a60c6373614dfb0834"></a>

### [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) → [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) FUN_00565a98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`005692bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005692bc.md) [`005694e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005694e0.md) [`0056a174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a174.md) [`0056a914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a914.md) · 呼出先 9件 [`0056ca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ca60.md) [`0056ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md) [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md) [`0056d7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d7d4.md) [`0056d97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md)
- 新版 呼出元 5件 [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) [`005692fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/005692fc.md) [`00569520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569520.md) [`0056a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a1b4.md) [`0056a954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a954.md) · 呼出先 9件 [`0056caa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056caa0.md) [`0056ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md) [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md) [`0056d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d814.md) [`0056d9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d9bc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00565c7c",
      "incomplete_value": true,
      "site": "00565c7c",
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
      "definition_site": "00565c3c",
      "incomplete_value": true,
      "site": "00565c3c",
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
    "ordinal": 34,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00565c6c",
      "DATA",
      [
        "storage",
        "002c21ac",
        null,
        null
      ]
    ],
    [
      "00565c84",
      "DATA",
      [
        "storage",
        "002c30e0",
        null,
        "string"
      ]
    ],
    [
      "00566694",
      "DATA",
      [
        "storage",
        "002d1528",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00565c6c",
      "DATA",
      [
        "storage",
        "002c21ec",
        null,
        null
      ]
    ],
    [
      "00565c84",
      "DATA",
      [
        "storage",
        "002c3120",
        null,
        "string"
      ]
    ],
    [
      "00566694",
      "DATA",
      [
        "storage",
        "002d1568",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md#insn-00565aa4) · [`00565bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md#insn-00565bb4) · [`00565c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md#insn-00565c14)
- 新版 `00565ae4`（命令位置の公開資料なし） · `00565bf4`（命令位置の公開資料なし） · `00565c54`（命令位置の公開資料なし）

~~~diff
- 00565aa4 ["INT_ADD", "register:40f0:8", ["const:565aa4:8", "const:4:8"]]
- 00565aa4 ["CALL", null, ["callee:0056caa0:8"]]
+ 00565ae4 ["INT_ADD", "register:40f0:8", ["const:565ae4:8", "const:4:8"]]
+ 00565ae4 ["CALL", null, ["callee:0056caa0:8"]]
- 00565aa4 bytes ef1b0094
+ 00565ae4 bytes ef1b0094
- 00565bb4 ["INT_ADD", "register:40f0:8", ["const:565bb4:8", "const:4:8"]]
- 00565bb4 ["CALL", null, ["callee:0056d0ac:8"]]
+ 00565bf4 ["INT_ADD", "register:40f0:8", ["const:565bf4:8", "const:4:8"]]
+ 00565bf4 ["CALL", null, ["callee:0056d0ac:8"]]
- 00565bb4 bytes 2e1d0094
+ 00565bf4 bytes 2e1d0094
- 00565c14 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 00565c14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00565c14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00565c14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00565c54 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00565c54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00565c54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00565c54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00565c14 bytes 29c10691
+ 00565c54 bytes 29c10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc0c42e9c5ed6519ee7b6cfa99396068"></a>

### [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) → [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) FUN_00566c40

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056a174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a174.md) · 呼出先 28件 [`0056591c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/0056591c.md) [`00568928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/00568928.md) [`00569f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569f74.md) [`0056a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a010.md) [`0056ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md)
- 新版 呼出元 1件 [`0056a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a1b4.md) · 呼出先 28件 [`0056595c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/0056595c.md) [`00568968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/00568968.md) [`00569fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569fb4.md) [`0056a050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a050.md) [`0056ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.73% / 新版 99.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00567af8",
      "incomplete_value": true,
      "site": "00567b08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567ab8",
      "incomplete_value": true,
      "site": "00567ac8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:700:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 113,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005670ac",
      "value": [
        "leaf",
        "ram:56f6f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0056706c",
      "value": [
        "leaf",
        "ram:56f6b0:8"
      ]
    },
    "ordinal": 39,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00567680",
      "value": [
        "leaf",
        "ram:56f7b4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00567640",
      "value": [
        "leaf",
        "ram:56f774:8"
      ]
    },
    "ordinal": 75,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00566d64",
      "READ",
      [
        "storage",
        "00ca3df4",
        null,
        "string"
      ]
    ],
    [
      "00566d6c",
      "READ",
      [
        "storage",
        "00ca3df8",
        null,
        "string"
      ]
    ],
    [
      "00566f10",
      "READ",
      [
        "storage",
        "00ca3df4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00566d64",
      "READ",
      [
        "storage",
        "00ca3ec4",
        null,
        "string"
      ]
    ],
    [
      "00566d6c",
      "READ",
      [
        "storage",
        "00ca3ec8",
        null,
        "string"
      ]
    ],
    [
      "00566f10",
      "READ",
      [
        "storage",
        "00ca3ec4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056706c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md#insn-0056706c) · [`00567640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md#insn-00567640) · [`00567d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md#insn-00567d64)
- 新版 `005670ac`（命令位置の公開資料なし） · `00567680`（命令位置の公開資料なし） · `00567da4`（命令位置の公開資料なし）

~~~diff
- 0056706c ["INT_ADD", "register:40f0:8", ["const:56706c:8", "const:4:8"]]
- 0056706c ["CALL", null, ["ram:56f6b0:8"]]
+ 005670ac ["INT_ADD", "register:40f0:8", ["const:5670ac:8", "const:4:8"]]
+ 005670ac ["CALL", null, ["ram:56f6f0:8"]]
- 0056706c bytes 91210094
+ 005670ac bytes 91210094
- 00567640 ["INT_ADD", "register:40f0:8", ["const:567640:8", "const:4:8"]]
- 00567640 ["CALL", null, ["ram:56f774:8"]]
+ 00567680 ["INT_ADD", "register:40f0:8", ["const:567680:8", "const:4:8"]]
+ 00567680 ["CALL", null, ["ram:56f7b4:8"]]
- 00567640 bytes 4d200094
+ 00567680 bytes 4d200094
- 00567d64 ["INT_ADD", "register:40f0:8", ["const:567d64:8", "const:4:8"]]
- 00567d64 ["CALL", null, ["callee:00c5a110:8"]]
+ 00567da4 ["INT_ADD", "register:40f0:8", ["const:567da4:8", "const:4:8"]]
+ 00567da4 ["CALL", null, ["callee:00c5a110:8"]]
- 00567d64 bytes b7c81b94
+ 00567da4 bytes dbc81b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c058448351a2aa73a102ab952b4838d2"></a>

### [`0056ab68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md) → [`0056aba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056aba8.md) FUN_0056aba8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043af2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043af2c.md) · 呼出先 11件 [`0056af6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056af6c.md) [`0056afdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056afdc.md) [`0056b2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b2f4.md) [`00570e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e38.md) [`00570e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e44.md)
- 新版 呼出元 1件 [`0043af6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043af6c.md) · 呼出先 11件 [`0056afac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056afac.md) [`0056b01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b01c.md) [`0056b334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b334.md) [`00570e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e78.md) [`00570e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e84.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 82.63% / 新版 82.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 12件, `call_target` 4件, `store_condition` 5件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056acf0",
      "incomplete_value": false,
      "site": "0056acfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056acb0",
      "incomplete_value": false,
      "site": "0056acbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056ad6c",
      "incomplete_value": false,
      "site": "0056ad6c",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ad2c",
      "incomplete_value": false,
      "site": "0056ad2c",
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
            "const:d38:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056ae20",
      "incomplete_value": false,
      "site": "0056ae20",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ade0",
      "incomplete_value": false,
      "site": "0056ade0",
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
            "const:d38:8"
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
      "0056abd8",
      "READ",
      [
        "storage",
        "00ca5d48",
        null,
        "undefined8"
      ]
    ],
    [
      "0056abf0",
      "PARAM",
      [
        "storage",
        "00ca5d48",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ac14",
      "READ",
      [
        "storage",
        "00ca5d48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056abd8",
      "READ",
      [
        "storage",
        "00ca5e48",
        null,
        "undefined8"
      ]
    ],
    [
      "0056abf0",
      "PARAM",
      [
        "storage",
        "00ca5e48",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ac14",
      "READ",
      [
        "storage",
        "00ca5e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056abcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md#insn-0056abcc) · [`0056abe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md#insn-0056abe4) · [`0056abf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md#insn-0056abf8)
- 新版 `0056ac0c`（命令位置の公開資料なし） · `0056ac24`（命令位置の公開資料なし） · `0056ac38`（命令位置の公開資料なし）

~~~diff
- 0056abcc ["INT_ADD", "register:40f0:8", ["const:56abcc:8", "const:4:8"]]
- 0056abcc ["CALL", null, ["callee:00c5a180:8"]]
+ 0056ac0c ["INT_ADD", "register:40f0:8", ["const:56ac0c:8", "const:4:8"]]
+ 0056ac0c ["CALL", null, ["callee:00c5a180:8"]]
- 0056abcc bytes 39bd1b94
+ 0056ac0c bytes 5dbd1b94
- 0056abe4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056abe4 ["INT_ADD", "register:40f0:8", ["const:56abe4:8", "const:4:8"]]
- 0056abe4 ["CALLIND", null, ["register:0:8"]]
+ 0056ac24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056ac24 ["INT_ADD", "register:40f0:8", ["const:56ac24:8", "const:4:8"]]
+ 0056ac24 ["CALLIND", null, ["register:0:8"]]
- 0056abe4 bytes 00013fd6
+ 0056ac24 bytes 00013fd6
- 0056abf8 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 0056abf8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0056abf8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0056abf8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0056ac38 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 0056ac38 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0056ac38 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0056ac38 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0056abf8 bytes 42403591
+ 0056ac38 bytes 42403991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3550df1014b250fd82a7cb9b3303663e"></a>

### [`0056b23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b23c.md) → [`0056b27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b27c.md) FUN_0056b27c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047bde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0047be20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047be20.md) · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0056b298",
      "incomplete_value": true,
      "site": "0056b29c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "LOAD"
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
      "definition_site": "0056b258",
      "incomplete_value": true,
      "site": "0056b25c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "LOAD"
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
      "0056b294",
      "READ",
      [
        "storage",
        "00ca5d18",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b294",
      "READ",
      [
        "storage",
        "00ca5d20",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b2e0",
      "READ",
      [
        "storage",
        "00ca5d30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056b294",
      "READ",
      [
        "storage",
        "00ca5e18",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b294",
      "READ",
      [
        "storage",
        "00ca5e20",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b2e0",
      "READ",
      [
        "storage",
        "00ca5e30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b23c.md#insn-0056b29c) · [`0056b250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b23c.md#insn-0056b250) · [`0056b284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b23c.md#insn-0056b284)
- 新版 `0056b2dc`（命令位置の公開資料なし） · `0056b290`（命令位置の公開資料なし） · `0056b2c4`（命令位置の公開資料なし）

~~~diff
- 0056b29c ["COPY", "tmp:0:8", ["const:d30:8"]]
- 0056b29c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056b29c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056b29c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056b2dc ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 0056b2dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b2dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b2dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056b29c bytes 08c13491
+ 0056b2dc bytes 08c13891
- 0056b250 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 0056b250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056b250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056b250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056b290 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 0056b290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056b250 bytes 08613491
+ 0056b290 bytes 08613891
- 0056b284 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b284 ["INT_ADD", "register:40f0:8", ["const:56b284:8", "const:4:8"]]
- 0056b284 ["CALLIND", null, ["register:0:8"]]
+ 0056b2c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b2c4 ["INT_ADD", "register:40f0:8", ["const:56b2c4:8", "const:4:8"]]
+ 0056b2c4 ["CALLIND", null, ["register:0:8"]]
- 0056b284 bytes 00013fd6
+ 0056b2c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcd0db745ea42ed91c43db97a4e15c1b"></a>

### [`0056b2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b2f4.md) → [`0056b334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b334.md) FUN_0056b334

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0056ab68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md) · 呼出先 3件 [`0056b614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b614.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0c0.md)
- 新版 呼出元 1件 [`0056aba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056aba8.md) · 呼出先 3件 [`0056b654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b654.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a190.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.78% / 新版 82.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 10件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056b370",
      "incomplete_value": false,
      "site": "0056b374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b330",
      "incomplete_value": false,
      "site": "0056b334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "definition_site": "0056b3ec",
      "incomplete_value": true,
      "site": "0056b3f4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2d1000:8"
              ],
              [
                "leaf",
                "const:50c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b3ac",
      "incomplete_value": true,
      "site": "0056b3b4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2d1000:8"
              ],
              [
                "leaf",
                "const:4cc:8"
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
      "definition_site": "0056b3f8",
      "incomplete_value": true,
      "site": "0056b410",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056b3b8",
      "incomplete_value": true,
      "site": "0056b3d0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 35,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056b374",
      "DATA",
      [
        "storage",
        "00c6b6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b3a0",
      "READ",
      [
        "storage",
        "00ca5d58",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b3ec",
      "READ",
      [
        "storage",
        "002d14cc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0056b374",
      "DATA",
      [
        "storage",
        "00c6b7c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b3a0",
      "READ",
      [
        "storage",
        "00ca5e58",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b3ec",
      "READ",
      [
        "storage",
        "002d150c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b2f4.md#insn-0056b3f4) · [`0056b40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b2f4.md#insn-0056b40c) · [`0056b410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b2f4.md#insn-0056b410)
- 新版 `0056b434`（命令位置の公開資料なし） · `0056b44c`（命令位置の公開資料なし） · `0056b450`（命令位置の公開資料なし）

~~~diff
- 0056b3f4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:2b0:8"]]
- 0056b3f4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056b434 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:380:8"]]
+ 0056b434 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 0056b3f4 bytes 4a5941f9
+ 0056b434 bytes 4ac141f9
- 0056b40c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b8:8"]]
- 0056b40c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056b44c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:388:8"]]
+ 0056b44c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0056b40c bytes 085d41f9
+ 0056b44c bytes 08c541f9
- 0056b410 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2c0:8"]]
- 0056b410 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056b450 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:390:8"]]
+ 0056b450 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0056b410 bytes 296141f9
+ 0056b450 bytes 29c941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0265c45a46bcffbafdef64cc80667903"></a>

### [`0056b79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b79c.md) → [`0056b7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b7dc.md) FUN_0056b7dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00570e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e38.md) · 呼出先 8件 [`00565584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565584.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 1件 [`00570e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e78.md) · 呼出先 8件 [`005655c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005655c4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056b7f4",
      "incomplete_value": false,
      "site": "0056b7f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b7b4",
      "incomplete_value": false,
      "site": "0056b7b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056b848",
      "incomplete_value": false,
      "site": "0056b848",
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
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b808",
      "incomplete_value": false,
      "site": "0056b808",
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
            "const:d60:8"
          ]
        ]
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
      "0056b7f8",
      "DATA",
      [
        "storage",
        "00c6b6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b840",
      "READ",
      [
        "storage",
        "00ca5d60",
        null,
        "undefined4"
      ]
    ],
    [
      "0056b848",
      "WRITE",
      [
        "storage",
        "00ca5d60",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0056b7f8",
      "DATA",
      [
        "storage",
        "00c6b7c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b840",
      "READ",
      [
        "storage",
        "00ca5e60",
        null,
        "undefined4"
      ]
    ],
    [
      "0056b848",
      "WRITE",
      [
        "storage",
        "00ca5e60",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b79c.md#insn-0056b7f8) · [`0056b808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b79c.md#insn-0056b808) · [`0056b7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b79c.md#insn-0056b7b4)
- 新版 `0056b838`（命令位置の公開資料なし） · `0056b848`（命令位置の公開資料なし） · `0056b7f4`（命令位置の公開資料なし）

~~~diff
- 0056b7f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b7f8 ["INT_ADD", "register:40f0:8", ["const:56b7f8:8", "const:4:8"]]
- 0056b7f8 ["CALLIND", null, ["register:0:8"]]
+ 0056b838 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b838 ["INT_ADD", "register:40f0:8", ["const:56b838:8", "const:4:8"]]
+ 0056b838 ["CALLIND", null, ["register:0:8"]]
- 0056b7f8 bytes 00013fd6
+ 0056b838 bytes 00013fd6
- 0056b808 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d60:8"]]
- 0056b808 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 0056b848 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 0056b848 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0056b808 bytes 09610db9
+ 0056b848 bytes 09610eb9
- 0056b7b4 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 0056b7b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056b7b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056b7b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056b7f4 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 0056b7f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056b7f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056b7f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056b7b4 bytes 29c11b91
+ 0056b7f4 bytes 29011f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43f77637cdbc62427f59eab1eab133b9"></a>

### [`0056c4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c4fc.md) → [`0056c53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c53c.md) FUN_0056c53c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0056c73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c73c.md) [`0056c740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c740.md) · 呼出先 8件 [`0056bcf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056bcf4.md) [`00c537f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c537f0.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`0056c77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c77c.md) [`0056c780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c780.md) · 呼出先 8件 [`0056bd34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056bd34.md) [`00c53890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53890.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.08% / 新版 92.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056c6ac",
      "incomplete_value": false,
      "site": "0056c6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c66c",
      "incomplete_value": false,
      "site": "0056c66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0056c578",
      "incomplete_value": true,
      "site": "0056c57c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "LOAD"
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
      "definition_site": "0056c538",
      "incomplete_value": true,
      "site": "0056c53c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "LOAD"
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
      "definition_site": "0056c5e0",
      "incomplete_value": false,
      "site": "0056c5ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c5a0",
      "incomplete_value": false,
      "site": "0056c5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:878:8"
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
      "0056c574",
      "READ",
      [
        "storage",
        "00ca5d18",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c574",
      "READ",
      [
        "storage",
        "00ca5d20",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c5e0",
      "PARAM",
      [
        "storage",
        "00c6b878",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0056c574",
      "READ",
      [
        "storage",
        "00ca5e18",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c574",
      "READ",
      [
        "storage",
        "00ca5e20",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c5e0",
      "PARAM",
      [
        "storage",
        "00c6b948",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056c5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c4fc.md#insn-0056c5ac) · [`0056c530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c4fc.md#insn-0056c530) · [`0056c580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c4fc.md#insn-0056c580)
- 新版 `0056c5ec`（命令位置の公開資料なし） · `0056c570`（命令位置の公開資料なし） · `0056c5c0`（命令位置の公開資料なし）

~~~diff
- 0056c5ac ["INT_ADD", "register:40f0:8", ["const:56c5ac:8", "const:4:8"]]
- 0056c5ac ["CALL", null, ["callee:00c586e0:8"]]
+ 0056c5ec ["INT_ADD", "register:40f0:8", ["const:56c5ec:8", "const:4:8"]]
+ 0056c5ec ["CALL", null, ["callee:00c586e0:8"]]
- 0056c5ac bytes 19b01b94
+ 0056c5ec bytes 3db01b94
- 0056c530 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 0056c530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056c530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056c530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056c570 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 0056c570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056c530 bytes 08613491
+ 0056c570 bytes 08613891
- 0056c580 ["INT_ADD", "register:40f0:8", ["const:56c580:8", "const:4:8"]]
- 0056c580 ["CALL", null, ["callee:00c53890:8"]]
+ 0056c5c0 ["INT_ADD", "register:40f0:8", ["const:56c5c0:8", "const:4:8"]]
+ 0056c5c0 ["CALL", null, ["callee:00c53890:8"]]
- 0056c580 bytes 9c9c1b94
+ 0056c5c0 bytes b49c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7527934fcc850b1b55d7cdef0851012"></a>

### [`0056cf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056cf78.md) → [`0056cfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056cfb8.md) FUN_0056cfb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 77.05% / 新版 77.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0056cfd4",
      "incomplete_value": true,
      "site": "0056cfd8",
      "value": [
        "INT_SEXT",
        "8",
        [
          [
            "LOAD",
            "1",
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
      "definition_site": "0056cf94",
      "incomplete_value": true,
      "site": "0056cf98",
      "value": [
        "INT_SEXT",
        "8",
        [
          [
            "LOAD",
            "1",
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
      "0056cfd4",
      "DATA",
      [
        "storage",
        "002c30e0",
        null,
        "string"
      ]
    ],
    [
      "0056d004",
      "DATA",
      [
        "storage",
        "002c30e0",
        null,
        "string"
      ]
    ],
    [
      "0056d028",
      "DATA",
      [
        "storage",
        "002c30e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056cfd4",
      "DATA",
      [
        "storage",
        "002c3120",
        null,
        "string"
      ]
    ],
    [
      "0056d004",
      "DATA",
      [
        "storage",
        "002c3120",
        null,
        "string"
      ]
    ],
    [
      "0056d028",
      "DATA",
      [
        "storage",
        "002c3120",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056cf90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056cf78.md#insn-0056cf90) · [`0056cfbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056cf78.md#insn-0056cfbc) · [`0056cfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056cf78.md#insn-0056cfe0)
- 新版 `0056cfd0`（命令位置の公開資料なし） · `0056cffc`（命令位置の公開資料なし） · `0056d020`（命令位置の公開資料なし）

~~~diff
- 0056cf90 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 0056cf90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056cf90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056cf90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056cfd0 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 0056cfd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056cfd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056cfd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056cf90 bytes 08810391
+ 0056cfd0 bytes 08810491
- 0056cfbc ["COPY", "tmp:0:8", ["const:e0:8"]]
- 0056cfbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056cfbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056cfbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056cffc ["COPY", "tmp:0:8", ["const:120:8"]]
+ 0056cffc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056cffc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056cffc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056cfbc bytes 29810391
+ 0056cffc bytes 29810491
- 0056cfe0 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 0056cfe0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056cfe0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056cfe0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056d020 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 0056d020 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056d020 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056d020 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056cfe0 bytes 29810391
+ 0056d020 bytes 29810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e892155badcf9f26de242fd7efe6c3d"></a>

### [`0056d438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md) → [`0056d478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d478.md) FUN_0056d478

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00569334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569334.md) [`0056d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md) · 呼出先 5件 [`0056a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a010.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a050.md) [`00c5a070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a070.md) [`00c5a080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a080.md)
- 新版 呼出元 2件 [`00569374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569374.md) [`0056d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md) · 呼出先 5件 [`0056a050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a050.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a120.md) [`00c5a140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a140.md) [`00c5a150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a150.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.13% / 新版 99.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056d6bc",
      "incomplete_value": true,
      "site": "0056d6c0",
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
                "const:58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056d67c",
      "incomplete_value": true,
      "site": "0056d680",
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
                "const:18:8"
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
      "0056d6bc",
      "READ",
      [
        "storage",
        "002c4018",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056d6bc",
      "READ",
      [
        "storage",
        "002c4058",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056d4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md#insn-0056d4c0) · [`0056d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md#insn-0056d4e0) · [`0056d518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md#insn-0056d518)
- 新版 `0056d500`（命令位置の公開資料なし） · `0056d520`（命令位置の公開資料なし） · `0056d558`（命令位置の公開資料なし）

~~~diff
- 0056d4c0 ["INT_ADD", "register:40f0:8", ["const:56d4c0:8", "const:4:8"]]
- 0056d4c0 ["CALL", null, ["callee:00c5a120:8"]]
+ 0056d500 ["INT_ADD", "register:40f0:8", ["const:56d500:8", "const:4:8"]]
+ 0056d500 ["CALL", null, ["callee:00c5a120:8"]]
- 0056d4c0 bytes e4b21b94
+ 0056d500 bytes 08b31b94
- 0056d4e0 ["INT_ADD", "register:40f0:8", ["const:56d4e0:8", "const:4:8"]]
- 0056d4e0 ["CALL", null, ["callee:00c5a140:8"]]
+ 0056d520 ["INT_ADD", "register:40f0:8", ["const:56d520:8", "const:4:8"]]
+ 0056d520 ["CALL", null, ["callee:00c5a140:8"]]
- 0056d4e0 bytes e4b21b94
+ 0056d520 bytes 08b31b94
- 0056d518 ["INT_ADD", "register:40f0:8", ["const:56d518:8", "const:4:8"]]
- 0056d518 ["CALL", null, ["callee:00c5a140:8"]]
+ 0056d558 ["INT_ADD", "register:40f0:8", ["const:56d558:8", "const:4:8"]]
+ 0056d558 ["CALL", null, ["callee:00c5a140:8"]]
- 0056d518 bytes d6b21b94
+ 0056d558 bytes fab21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1eafcdce819c6501ee5f5271ec12f2be"></a>

### [`0056fda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fda0.md) → [`0056fde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056fde0.md) FUN_0056fde0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 3件 [`00c583e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583e0.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a120.md)
- 新版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 3件 [`00c584b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c584b0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5a1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005700c0",
      "incomplete_value": true,
      "site": "005700c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570080",
      "incomplete_value": true,
      "site": "00570084",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:390:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005700c8",
      "incomplete_value": true,
      "site": "005700cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570088",
      "incomplete_value": true,
      "site": "0057008c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:170:8"
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
      "definition_site": "0057030c",
      "incomplete_value": true,
      "site": "00570310",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005702cc",
      "incomplete_value": true,
      "site": "005702d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:390:8"
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
      "0056ffc0",
      "READ",
      [
        "storage",
        "002c43f0",
        null,
        "undefined8"
      ]
    ],
    [
      "005700c0",
      "READ",
      [
        "storage",
        "002c2390",
        null,
        null
      ]
    ],
    [
      "005700c8",
      "READ",
      [
        "storage",
        "002c3170",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0056ffc0",
      "READ",
      [
        "storage",
        "002c4430",
        null,
        "undefined8"
      ]
    ],
    [
      "005700c0",
      "READ",
      [
        "storage",
        "002c23d0",
        null,
        null
      ]
    ],
    [
      "005700c8",
      "READ",
      [
        "storage",
        "002c31b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056fe24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fda0.md#insn-0056fe24) · [`0056fe40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fda0.md#insn-0056fe40) · [`0056fef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fda0.md#insn-0056fef0)
- 新版 `0056fe64`（命令位置の公開資料なし） · `0056fe80`（命令位置の公開資料なし） · `0056ff30`（命令位置の公開資料なし）

~~~diff
- 0056fe24 ["INT_ADD", "register:40f0:8", ["const:56fe24:8", "const:4:8"]]
- 0056fe24 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 0056fe64 ["INT_ADD", "register:40f0:8", ["const:56fe64:8", "const:4:8"]]
+ 0056fe64 ["CALL", null, ["callee:00c5a0f0:8"]]
- 0056fe24 bytes 7fa81b94
+ 0056fe64 bytes a3a81b94
- 0056fe40 ["INT_ADD", "register:40f0:8", ["const:56fe40:8", "const:4:8"]]
- 0056fe40 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 0056fe80 ["INT_ADD", "register:40f0:8", ["const:56fe80:8", "const:4:8"]]
+ 0056fe80 ["CALL", null, ["callee:00c5a0f0:8"]]
- 0056fe40 bytes 78a81b94
+ 0056fe80 bytes 9ca81b94
- 0056fef0 ["INT_ADD", "register:40f0:8", ["const:56fef0:8", "const:4:8"]]
- 0056fef0 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 0056ff30 ["INT_ADD", "register:40f0:8", ["const:56ff30:8", "const:4:8"]]
+ 0056ff30 ["CALL", null, ["callee:00c5a0f0:8"]]
- 0056fef0 bytes 4ca81b94
+ 0056ff30 bytes 70a81b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acc1ebf38606745d3f66e1ca3a6c3968"></a>

### [`00570df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570df8.md) → [`00570e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e38.md) FUN_00570e38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00570e3c",
      "incomplete_value": false,
      "site": "00570e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570dfc",
      "incomplete_value": false,
      "site": "00570e00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:838:8"
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
      "00570e40",
      "DATA",
      [
        "storage",
        "00c6b838",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00570e40",
      "DATA",
      [
        "storage",
        "00c6b908",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570df8.md#insn-00570dfc)
- 新版 `00570e3c`（命令位置の公開資料なし）

~~~diff
- 00570dfc ["COPY", "tmp:0:8", ["const:838:8"]]
- 00570dfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00570dfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00570dfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00570e3c ["COPY", "tmp:0:8", ["const:908:8"]]
+ 00570e3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00570e3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00570e3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00570dfc bytes 08e12091
+ 00570e3c bytes 08212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22d2a77f697c0bd426fd0da08a72f40a"></a>

### [`00570e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e08.md) → [`00570e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e48.md) FUN_00570e48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00570e58",
      "incomplete_value": false,
      "site": "00570e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570e18",
      "incomplete_value": false,
      "site": "00570e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:838:8"
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
      "00570e60",
      "DATA",
      [
        "storage",
        "00c6b838",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00570e60",
      "DATA",
      [
        "storage",
        "00c6b908",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e08.md#insn-00570e18) · [`00570e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e08.md#insn-00570e24)
- 新版 `00570e58`（命令位置の公開資料なし） · `00570e64`（命令位置の公開資料なし）

~~~diff
- 00570e18 ["COPY", "tmp:0:8", ["const:838:8"]]
- 00570e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00570e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00570e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00570e58 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 00570e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00570e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00570e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00570e18 bytes 08e12091
+ 00570e58 bytes 08212491
- 00570e24 ["INT_ADD", "register:40f0:8", ["const:570e24:8", "const:4:8"]]
- 00570e24 ["CALL", null, ["callee:00c57f70:8"]]
+ 00570e64 ["INT_ADD", "register:40f0:8", ["const:570e64:8", "const:4:8"]]
+ 00570e64 ["CALL", null, ["callee:00c57f70:8"]]
- 00570e24 bytes 1f9c1b94
+ 00570e64 bytes 439c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a92d35264afaa1144cd7fe75eb6c424"></a>

### [`00570fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fa0.md) → [`00570fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570fe0.md) FUN_00570fe0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00570e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e44.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00570e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e84.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00570fec",
      "incomplete_value": true,
      "site": "00570ff0",
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
    "old": {
      "definition_site": "00570fac",
      "incomplete_value": true,
      "site": "00570fb0",
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
      "00570fec",
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
      "00570fec",
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

- 旧版 [`00570fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fa0.md#insn-00570fb0) · [`00570fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fa0.md#insn-00570fac)
- 新版 `00570ff0`（命令位置の公開資料なし） · `00570fec`（命令位置の公開資料なし）

~~~diff
- 00570fb0 ["INT_ADD", "register:40f0:8", ["const:570fb0:8", "const:4:8"]]
- 00570fb0 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00570ff0 ["INT_ADD", "register:40f0:8", ["const:570ff0:8", "const:4:8"]]
+ 00570ff0 ["CALL", null, ["callee:0043b7b8:8"]]
- 00570fb0 bytes f229fb97
+ 00570ff0 bytes f229fb97
- 00570fac ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00570fac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00570fac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00570fac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00570fec ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00570fec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00570fec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00570fec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00570fac bytes 00303d91
+ 00570fec bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-394fb8a242f6db3aafb244449c993719"></a>

### [`00570fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fb4.md) → [`00570ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570ff4.md) FUN_00570ff4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "0057100c",
      "incomplete_value": false,
      "site": "00571010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570fcc",
      "incomplete_value": false,
      "site": "00570fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "00571010",
      "DATA",
      [
        "storage",
        "00c6b8a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00571010",
      "DATA",
      [
        "storage",
        "00c6b970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fb4.md#insn-00570fcc) · [`00570fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fb4.md#insn-00570fe0) · [`00570ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fb4.md#insn-00570ff4)
- 新版 `0057100c`（命令位置の公開資料なし） · `00571020`（命令位置の公開資料なし） · `00571034`（命令位置の公開資料なし）

~~~diff
- 00570fcc ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00570fcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00570fcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00570fcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057100c ["COPY", "tmp:0:8", ["const:970:8"]]
+ 0057100c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057100c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057100c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00570fcc bytes 08812291
+ 0057100c bytes 08c12591
- 00570fe0 ["INT_ADD", "register:40f0:8", ["const:570fe0:8", "const:4:8"]]
- 00570fe0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00571020 ["INT_ADD", "register:40f0:8", ["const:571020:8", "const:4:8"]]
+ 00571020 ["CALL", null, ["callee:00c53da0:8"]]
- 00570fe0 bytes 488b1b94
+ 00571020 bytes 608b1b94
- 00570ff4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00570ff4 ["INT_ADD", "register:40f0:8", ["const:570ff4:8", "const:4:8"]]
- 00570ff4 ["CALLIND", null, ["register:0:8"]]
+ 00571034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00571034 ["INT_ADD", "register:40f0:8", ["const:571034:8", "const:4:8"]]
+ 00571034 ["CALLIND", null, ["register:0:8"]]
- 00570ff4 bytes 00013fd6
+ 00571034 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27dec255d4d44f75bfa85af8e6f78341"></a>

### [`00571010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571010.md) → [`00571050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571050.md) FUN_00571050

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00571068",
      "incomplete_value": false,
      "site": "0057106c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571028",
      "incomplete_value": false,
      "site": "0057102c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "0057106c",
      "DATA",
      [
        "storage",
        "00c6b8a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057106c",
      "DATA",
      [
        "storage",
        "00c6b970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571010.md#insn-00571028) · [`0057103c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571010.md#insn-0057103c) · [`00571050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571010.md#insn-00571050)
- 新版 `00571068`（命令位置の公開資料なし） · `0057107c`（命令位置の公開資料なし） · `00571090`（命令位置の公開資料なし）

~~~diff
- 00571028 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00571028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00571028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00571028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00571068 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00571068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00571068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00571068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00571028 bytes 08812291
+ 00571068 bytes 08c12591
- 0057103c ["INT_ADD", "register:40f0:8", ["const:57103c:8", "const:4:8"]]
- 0057103c ["CALL", null, ["callee:00c53da0:8"]]
+ 0057107c ["INT_ADD", "register:40f0:8", ["const:57107c:8", "const:4:8"]]
+ 0057107c ["CALL", null, ["callee:00c53da0:8"]]
- 0057103c bytes 318b1b94
+ 0057107c bytes 498b1b94
- 00571050 ["COPY", "register:0:8", ["register:4040:8"]]
- 00571050 ["INT_ADD", "register:40f0:8", ["const:571050:8", "const:4:8"]]
- 00571050 ["CALLIND", null, ["register:0:8"]]
+ 00571090 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00571090 ["INT_ADD", "register:40f0:8", ["const:571090:8", "const:4:8"]]
+ 00571090 ["CALLIND", null, ["register:0:8"]]
- 00571050 bytes 00013fd6
+ 00571090 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3088d895c108d68fddca268bad4bc024"></a>

### [`005710f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005710f4.md) → [`00571134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571134.md) FUN_00571134

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "0057114c",
      "incomplete_value": false,
      "site": "00571150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057110c",
      "incomplete_value": false,
      "site": "00571110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "00571150",
      "DATA",
      [
        "storage",
        "00c6b8f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00571150",
      "DATA",
      [
        "storage",
        "00c6b9c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057110c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005710f4.md#insn-0057110c) · [`00571120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005710f4.md#insn-00571120) · [`00571134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005710f4.md#insn-00571134)
- 新版 `0057114c`（命令位置の公開資料なし） · `00571160`（命令位置の公開資料なし） · `00571174`（命令位置の公開資料なし）

~~~diff
- 0057110c ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 0057110c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057110c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057110c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057114c ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 0057114c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057114c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057114c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057110c bytes 08c12391
+ 0057114c bytes 08012791
- 00571120 ["INT_ADD", "register:40f0:8", ["const:571120:8", "const:4:8"]]
- 00571120 ["CALL", null, ["callee:00c53da0:8"]]
+ 00571160 ["INT_ADD", "register:40f0:8", ["const:571160:8", "const:4:8"]]
+ 00571160 ["CALL", null, ["callee:00c53da0:8"]]
- 00571120 bytes f88a1b94
+ 00571160 bytes 108b1b94
- 00571134 ["COPY", "register:0:8", ["register:4040:8"]]
- 00571134 ["INT_ADD", "register:40f0:8", ["const:571134:8", "const:4:8"]]
- 00571134 ["CALLIND", null, ["register:0:8"]]
+ 00571174 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00571174 ["INT_ADD", "register:40f0:8", ["const:571174:8", "const:4:8"]]
+ 00571174 ["CALLIND", null, ["register:0:8"]]
- 00571134 bytes 00013fd6
+ 00571174 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6380004b4952c361e4de23b840b59ca7"></a>

### [`00571150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571150.md) → [`00571190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571190.md) FUN_00571190

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005711a8",
      "incomplete_value": false,
      "site": "005711ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571168",
      "incomplete_value": false,
      "site": "0057116c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "005711ac",
      "DATA",
      [
        "storage",
        "00c6b8f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005711ac",
      "DATA",
      [
        "storage",
        "00c6b9c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571150.md#insn-00571168) · [`0057117c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571150.md#insn-0057117c) · [`00571190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571150.md#insn-00571190)
- 新版 `005711a8`（命令位置の公開資料なし） · `005711bc`（命令位置の公開資料なし） · `005711d0`（命令位置の公開資料なし）

~~~diff
- 00571168 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00571168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00571168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00571168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005711a8 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 005711a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005711a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005711a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00571168 bytes 08c12391
+ 005711a8 bytes 08012791
- 0057117c ["INT_ADD", "register:40f0:8", ["const:57117c:8", "const:4:8"]]
- 0057117c ["CALL", null, ["callee:00c53da0:8"]]
+ 005711bc ["INT_ADD", "register:40f0:8", ["const:5711bc:8", "const:4:8"]]
+ 005711bc ["CALL", null, ["callee:00c53da0:8"]]
- 0057117c bytes e18a1b94
+ 005711bc bytes f98a1b94
- 00571190 ["COPY", "register:0:8", ["register:4040:8"]]
- 00571190 ["INT_ADD", "register:40f0:8", ["const:571190:8", "const:4:8"]]
- 00571190 ["CALLIND", null, ["register:0:8"]]
+ 005711d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005711d0 ["INT_ADD", "register:40f0:8", ["const:5711d0:8", "const:4:8"]]
+ 005711d0 ["CALLIND", null, ["register:0:8"]]
- 00571190 bytes 00013fd6
+ 005711d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d3b0c4756e1231f90e0bb80aa1abdea"></a>

### [`00571234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571234.md) → [`00571274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571274.md) FUN_00571274

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00571278",
      "incomplete_value": false,
      "site": "0057127c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571238",
      "incomplete_value": false,
      "site": "0057123c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "0057127c",
      "DATA",
      [
        "storage",
        "00c6b940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057127c",
      "DATA",
      [
        "storage",
        "00c6ba10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571234.md#insn-00571238)
- 新版 `00571278`（命令位置の公開資料なし）

~~~diff
- 00571238 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00571238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00571238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00571238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00571278 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 00571278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00571278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00571278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00571238 bytes 08012591
+ 00571278 bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8d48b1120cb5d381e2800ac592a351e"></a>

### [`00571244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571244.md) → [`00571284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571284.md) FUN_00571284

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00571294",
      "incomplete_value": false,
      "site": "0057129c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571254",
      "incomplete_value": false,
      "site": "0057125c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "0057129c",
      "DATA",
      [
        "storage",
        "00c6b940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057129c",
      "DATA",
      [
        "storage",
        "00c6ba10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571244.md#insn-00571254) · [`00571260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571244.md#insn-00571260)
- 新版 `00571294`（命令位置の公開資料なし） · `005712a0`（命令位置の公開資料なし）

~~~diff
- 00571254 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00571254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00571254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00571254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00571294 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 00571294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00571294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00571294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00571254 bytes 08012591
+ 00571294 bytes 08412891
- 00571260 ["INT_ADD", "register:40f0:8", ["const:571260:8", "const:4:8"]]
- 00571260 ["CALL", null, ["callee:00c57f70:8"]]
+ 005712a0 ["INT_ADD", "register:40f0:8", ["const:5712a0:8", "const:4:8"]]
+ 005712a0 ["CALL", null, ["callee:00c57f70:8"]]
- 00571260 bytes 109b1b94
+ 005712a0 bytes 349b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3edec2683e40f2e1f831497b32491e84"></a>

### [`00571284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571284.md) → [`005712c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005712c4.md) _INIT_28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056aad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056aad0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0056ab10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056ab10.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 56.52% / 新版 56.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005712f0",
      "incomplete_value": false,
      "site": "005712f0",
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
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005712b0",
      "incomplete_value": false,
      "site": "005712b0",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005712f0",
      "incomplete_value": false,
      "site": "005712f0",
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
                "const:e18:8"
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
      "definition_site": "005712b0",
      "incomplete_value": false,
      "site": "005712b0",
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
                "const:d18:8"
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005712f4",
      "incomplete_value": false,
      "site": "005712f4",
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
                "const:e18:8"
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
      "definition_site": "005712b4",
      "incomplete_value": false,
      "site": "005712b4",
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
                "const:d18:8"
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
      "005712e4",
      "PARAM",
      [
        "storage",
        "00ca5d18",
        null,
        "undefined8"
      ]
    ],
    [
      "005712e8",
      "PARAM",
      [
        "storage",
        "0056aad0",
        null,
        null
      ]
    ],
    [
      "005712ec",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005712e4",
      "PARAM",
      [
        "storage",
        "00ca5e18",
        null,
        "undefined8"
      ]
    ],
    [
      "005712e8",
      "PARAM",
      [
        "storage",
        "0056ab10",
        null,
        null
      ]
    ],
    [
      "005712ec",
      "PARAM",
      [
        "storage",
        "00c63060",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005712b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571284.md#insn-005712b8) · [`00571294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571284.md#insn-00571294) · [`00571298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571284.md#insn-00571298)
- 新版 `005712f8`（命令位置の公開資料なし） · `005712d4`（命令位置の公開資料なし） · `005712d8`（命令位置の公開資料なし）

~~~diff
- 005712b8 ["INT_ADD", "register:40f0:8", ["const:5712b8:8", "const:4:8"]]
- 005712b8 ["CALL", null, ["callee:00c57f00:8"]]
+ 005712f8 ["INT_ADD", "register:40f0:8", ["const:5712f8:8", "const:4:8"]]
+ 005712f8 ["CALL", null, ["callee:00c57f00:8"]]
- 005712b8 bytes de9a1b94
+ 005712f8 bytes 029b1b94
- 00571294 ["COPY", "register:4098:8", ["const:56aad0:8"]]
+ 005712d4 ["COPY", "register:4098:8", ["const:56ab10:8"]]
- 00571294 bytes f3c1fc10
+ 005712d4 bytes f3c1fc10
- 00571298 ["COPY", "register:40a0:8", ["const:c62000:8"]]
+ 005712d8 ["COPY", "register:40a0:8", ["const:c63000:8"]]
- 00571298 bytes 943700b0
+ 005712d8 bytes 943700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ddfca831aab77ea62098695e0c5fcc1"></a>

### [`005712e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md) → [`00571320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md) FUN_00571320

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00573b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573b60.md) [`00573e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md) [`005740e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md) · 呼出先 10件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0057485c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/0057485c.md) [`00596f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md)
- 新版 呼出元 3件 [`00573ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ba0.md) [`00573ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ec0.md) [`00574120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574120.md) · 呼出先 10件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0057489c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/0057489c.md) [`00596f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md) [`00597648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597648.md) [`00597728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597728.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.21% / 新版 94.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005713a8",
      "incomplete_value": true,
      "site": "005713a8",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:250:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571368",
      "incomplete_value": true,
      "site": "00571368",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:29d:8"
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
      "definition_site": "00571410",
      "incomplete_value": true,
      "site": "00571410",
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
                "const:d02:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005713d0",
      "incomplete_value": true,
      "site": "005713d0",
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
                "const:cd1:8"
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
      "definition_site": "005714dc",
      "incomplete_value": true,
      "site": "005714dc",
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
                "const:e1b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057149c",
      "incomplete_value": true,
      "site": "0057149c",
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
                "const:dea:8"
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
      "00571398",
      "READ",
      [
        "storage",
        "002a329d",
        null,
        "string"
      ]
    ],
    [
      "005713f8",
      "READ",
      [
        "storage",
        "002b2cd1",
        null,
        "string"
      ]
    ],
    [
      "005714cc",
      "READ",
      [
        "storage",
        "002b1dea",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00571398",
      "READ",
      [
        "storage",
        "002a3250",
        null,
        "string"
      ]
    ],
    [
      "005713f8",
      "READ",
      [
        "storage",
        "002b2d02",
        null,
        "string"
      ]
    ],
    [
      "005714cc",
      "READ",
      [
        "storage",
        "002b1e1b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md#insn-00571328) · [`005713a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md#insn-005713a8) · [`00571410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md#insn-00571410)
- 新版 `00571368`（命令位置の公開資料なし） · `005713e8`（命令位置の公開資料なし） · `00571450`（命令位置の公開資料なし）

~~~diff
- 00571328 ["INT_ADD", "register:40f0:8", ["const:571328:8", "const:4:8"]]
- 00571328 ["CALL", null, ["callee:00596f6c:8"]]
+ 00571368 ["INT_ADD", "register:40f0:8", ["const:571368:8", "const:4:8"]]
+ 00571368 ["CALL", null, ["callee:00596f6c:8"]]
- 00571328 bytes 01970094
+ 00571368 bytes 01970094
- 005713a8 ["INT_ADD", "register:40f0:8", ["const:5713a8:8", "const:4:8"]]
- 005713a8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005713e8 ["INT_ADD", "register:40f0:8", ["const:5713e8:8", "const:4:8"]]
+ 005713e8 ["CALL", null, ["callee:00c57f80:8"]]
- 005713a8 bytes c29a1b94
+ 005713e8 bytes e69a1b94
- 00571410 ["COPY", "register:0:8", ["register:4040:8"]]
- 00571410 ["INT_ADD", "register:40f0:8", ["const:571410:8", "const:4:8"]]
- 00571410 ["CALLIND", null, ["register:0:8"]]
+ 00571450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00571450 ["INT_ADD", "register:40f0:8", ["const:571450:8", "const:4:8"]]
+ 00571450 ["CALLIND", null, ["register:0:8"]]
- 00571410 bytes 00013fd6
+ 00571450 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a6bd9c4e7b07594f38057604c8744b9"></a>

### [`00571af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md) → [`00571b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571b34.md) FUN_00571b34

採用 · 移動量 `+0x40` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550990.md) · 呼出先 15件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 1件 [`005509d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509d0.md) · 呼出先 15件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.03% / 新版 95.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00571cec",
      "incomplete_value": true,
      "site": "00571cec",
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
      "definition_site": "00571cac",
      "incomplete_value": true,
      "site": "00571cac",
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00571d1c",
      "incomplete_value": true,
      "site": "00571d1c",
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
      "definition_site": "00571cdc",
      "incomplete_value": true,
      "site": "00571cdc",
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
      "00571bb0",
      "READ",
      [
        "storage",
        "002bda7e",
        null,
        "string"
      ]
    ],
    [
      "00571bb0",
      "READ",
      [
        "storage",
        "002bda8e",
        null,
        "string"
      ]
    ],
    [
      "00571bb4",
      "READ",
      [
        "storage",
        "002c2570",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00571bb0",
      "READ",
      [
        "storage",
        "002bda2a",
        null,
        "string"
      ]
    ],
    [
      "00571bb0",
      "READ",
      [
        "storage",
        "002bda3a",
        null,
        "string"
      ]
    ],
    [
      "00571bb4",
      "READ",
      [
        "storage",
        "002c25b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md#insn-00571b2c) · [`00571b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md#insn-00571b34) · [`00571b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md#insn-00571b60)
- 新版 `00571b6c`（命令位置の公開資料なし） · `00571b74`（命令位置の公開資料なし） · `00571ba0`（命令位置の公開資料なし）

~~~diff
- 00571b2c ["INT_ADD", "register:40f0:8", ["const:571b2c:8", "const:4:8"]]
- 00571b2c ["CALL", null, ["callee:00588eac:8"]]
+ 00571b6c ["INT_ADD", "register:40f0:8", ["const:571b6c:8", "const:4:8"]]
+ 00571b6c ["CALL", null, ["callee:00588eac:8"]]
- 00571b2c bytes d05c0094
+ 00571b6c bytes d05c0094
- 00571b34 ["INT_ADD", "register:40f0:8", ["const:571b34:8", "const:4:8"]]
- 00571b34 ["CALL", null, ["callee:0058919c:8"]]
+ 00571b74 ["INT_ADD", "register:40f0:8", ["const:571b74:8", "const:4:8"]]
+ 00571b74 ["CALL", null, ["callee:0058919c:8"]]
- 00571b34 bytes 8a5d0094
+ 00571b74 bytes 8a5d0094
- 00571b60 ["INT_ADD", "register:40f0:8", ["const:571b60:8", "const:4:8"]]
- 00571b60 ["CALL", null, ["callee:00c57f60:8"]]
+ 00571ba0 ["INT_ADD", "register:40f0:8", ["const:571ba0:8", "const:4:8"]]
+ 00571ba0 ["CALL", null, ["callee:00c57f60:8"]]
- 00571b60 bytes cc981b94
+ 00571ba0 bytes f0981b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bc4a0cb450de9da39e48d60fdd145c7"></a>

### [`005720f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md) → [`00572138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572138.md) FUN_00572138

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00550998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550998.md) · 呼出先 11件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`005509d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509d8.md) · 呼出先 11件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057219c",
      "incomplete_value": true,
      "site": "005721ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057215c",
      "incomplete_value": true,
      "site": "0057216c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ec:8"
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
      "definition_site": "005721b0",
      "incomplete_value": true,
      "site": "005721b0",
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
      "definition_site": "00572170",
      "incomplete_value": true,
      "site": "00572170",
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
      "0057217c",
      "READ",
      [
        "storage",
        "002bfee3",
        null,
        "string"
      ]
    ],
    [
      "0057219c",
      "READ",
      [
        "storage",
        "002a20ec",
        null,
        "string"
      ]
    ],
    [
      "005721a4",
      "READ",
      [
        "storage",
        "002a20fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057217c",
      "READ",
      [
        "storage",
        "002bff23",
        null,
        "string"
      ]
    ],
    [
      "0057219c",
      "READ",
      [
        "storage",
        "002a209f",
        null,
        "string"
      ]
    ],
    [
      "005721a4",
      "READ",
      [
        "storage",
        "002a20ad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057212c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md#insn-0057212c) · [`005721ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md#insn-005721ac) · [`00572124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md#insn-00572124)
- 新版 `0057216c`（命令位置の公開資料なし） · `005721ec`（命令位置の公開資料なし） · `00572164`（命令位置の公開資料なし）

~~~diff
- 0057212c ["INT_ADD", "register:40f0:8", ["const:57212c:8", "const:4:8"]]
- 0057212c ["CALL", null, ["callee:0058919c:8"]]
+ 0057216c ["INT_ADD", "register:40f0:8", ["const:57216c:8", "const:4:8"]]
+ 0057216c ["CALL", null, ["callee:0058919c:8"]]
- 0057212c bytes 0c5c0094
+ 0057216c bytes 0c5c0094
- 005721ac ["INT_ADD", "register:40f0:8", ["const:5721ac:8", "const:4:8"]]
- 005721ac ["CALL", null, ["callee:00589184:8"]]
+ 005721ec ["INT_ADD", "register:40f0:8", ["const:5721ec:8", "const:4:8"]]
+ 005721ec ["CALL", null, ["callee:00589184:8"]]
- 005721ac bytes e65b0094
+ 005721ec bytes e65b0094
- 00572124 ["INT_ADD", "register:40f0:8", ["const:572124:8", "const:4:8"]]
- 00572124 ["CALL", null, ["callee:00588eac:8"]]
+ 00572164 ["INT_ADD", "register:40f0:8", ["const:572164:8", "const:4:8"]]
+ 00572164 ["CALL", null, ["callee:00588eac:8"]]
- 00572124 bytes 525b0094
+ 00572164 bytes 525b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee6fdf17debc7ec46065bd75eed1080d"></a>

### [`005722ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md) → [`005722ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005722ec.md) FUN_005722ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055099c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/0055099c.md) · 呼出先 11件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`005509dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509dc.md) · 呼出先 11件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00572344",
      "incomplete_value": true,
      "site": "00572344",
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
                "const:f23:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572304",
      "incomplete_value": true,
      "site": "00572304",
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
                "const:ee3:8"
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
      "definition_site": "00572350",
      "incomplete_value": true,
      "site": "00572360",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572310",
      "incomplete_value": true,
      "site": "00572320",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ec:8"
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
      "definition_site": "00572364",
      "incomplete_value": true,
      "site": "00572364",
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
      "definition_site": "00572324",
      "incomplete_value": true,
      "site": "00572324",
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
      "00572330",
      "READ",
      [
        "storage",
        "002bfee3",
        null,
        "string"
      ]
    ],
    [
      "00572350",
      "READ",
      [
        "storage",
        "002a20ec",
        null,
        "string"
      ]
    ],
    [
      "00572358",
      "READ",
      [
        "storage",
        "002a20fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00572330",
      "READ",
      [
        "storage",
        "002bff23",
        null,
        "string"
      ]
    ],
    [
      "00572350",
      "READ",
      [
        "storage",
        "002a209f",
        null,
        "string"
      ]
    ],
    [
      "00572358",
      "READ",
      [
        "storage",
        "002a20ad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005722e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md#insn-005722e0) · [`00572360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md#insn-00572360) · [`005722d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md#insn-005722d8)
- 新版 `00572320`（命令位置の公開資料なし） · `005723a0`（命令位置の公開資料なし） · `00572318`（命令位置の公開資料なし）

~~~diff
- 005722e0 ["INT_ADD", "register:40f0:8", ["const:5722e0:8", "const:4:8"]]
- 005722e0 ["CALL", null, ["callee:0058919c:8"]]
+ 00572320 ["INT_ADD", "register:40f0:8", ["const:572320:8", "const:4:8"]]
+ 00572320 ["CALL", null, ["callee:0058919c:8"]]
- 005722e0 bytes 9f5b0094
+ 00572320 bytes 9f5b0094
- 00572360 ["INT_ADD", "register:40f0:8", ["const:572360:8", "const:4:8"]]
- 00572360 ["CALL", null, ["callee:00589184:8"]]
+ 005723a0 ["INT_ADD", "register:40f0:8", ["const:5723a0:8", "const:4:8"]]
+ 005723a0 ["CALL", null, ["callee:00589184:8"]]
- 00572360 bytes 795b0094
+ 005723a0 bytes 795b0094
- 005722d8 ["INT_ADD", "register:40f0:8", ["const:5722d8:8", "const:4:8"]]
- 005722d8 ["CALL", null, ["callee:00588eac:8"]]
+ 00572318 ["INT_ADD", "register:40f0:8", ["const:572318:8", "const:4:8"]]
+ 00572318 ["CALL", null, ["callee:00588eac:8"]]
- 005722d8 bytes e55a0094
+ 00572318 bytes e55a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b601a2f7af8cf4d7aeca66a54bd3c4b"></a>

### [`00572460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md) → [`005724a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005724a0.md) FUN_005724a0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509a0.md) · 呼出先 19件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00574d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574d88.md)
- 新版 呼出元 1件 [`005509e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509e0.md) · 呼出先 19件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00574dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574dc8.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 92.44% / 新版 92.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057251c",
      "incomplete_value": true,
      "site": "0057252c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:36:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005724dc",
      "incomplete_value": true,
      "site": "005724ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8a:8"
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
      "definition_site": "00572530",
      "incomplete_value": true,
      "site": "00572530",
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
      "definition_site": "005724f0",
      "incomplete_value": true,
      "site": "005724f0",
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
      "definition_site": "00572524",
      "incomplete_value": true,
      "site": "00572534",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005724e4",
      "incomplete_value": true,
      "site": "005724f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057251c",
      "READ",
      [
        "storage",
        "002b908a",
        null,
        "string"
      ]
    ],
    [
      "00572520",
      "READ",
      [
        "storage",
        "002b9099",
        null,
        "string"
      ]
    ],
    [
      "00572524",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057251c",
      "READ",
      [
        "storage",
        "002b9036",
        null,
        "string"
      ]
    ],
    [
      "00572520",
      "READ",
      [
        "storage",
        "002b9045",
        null,
        "string"
      ]
    ],
    [
      "00572524",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md#insn-00572530) · [`00572558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md#insn-00572558) · [`005725d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md#insn-005725d4)
- 新版 `00572570`（命令位置の公開資料なし） · `00572598`（命令位置の公開資料なし） · `00572614`（命令位置の公開資料なし）

~~~diff
- 00572530 ["INT_ADD", "register:40f0:8", ["const:572530:8", "const:4:8"]]
- 00572530 ["CALL", null, ["callee:00c57f80:8"]]
+ 00572570 ["INT_ADD", "register:40f0:8", ["const:572570:8", "const:4:8"]]
+ 00572570 ["CALL", null, ["callee:00c57f80:8"]]
- 00572530 bytes 60961b94
+ 00572570 bytes 84961b94
- 00572558 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:1b8:8"]]
- 00572558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
+ 00572598 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:2b8:8"]]
+ 00572598 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00572558 bytes 54b901b9
+ 00572598 bytes 54b902b9
- 005725d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a0:8"]]
- 005725d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00572614 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
+ 00572614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005725d4 bytes 09d100f9
+ 00572614 bytes 095101f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48441bc6b75291608f79eaea100578ad"></a>

### [`005728b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005728b4.md) → [`005728f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005728f4.md) FUN_005728f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005509a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509a4.md) · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`005509e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509e4.md) · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00572940",
      "incomplete_value": true,
      "site": "00572940",
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
                "const:d0d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572900",
      "incomplete_value": true,
      "site": "00572900",
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
                "const:d69:8"
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
      "00572930",
      "READ",
      [
        "storage",
        "002a9d69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00572930",
      "READ",
      [
        "storage",
        "002a9d0d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005728d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005728b4.md#insn-005728d4) · [`005728dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005728b4.md#insn-005728dc) · [`005728e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005728b4.md#insn-005728e8)
- 新版 `00572914`（命令位置の公開資料なし） · `0057291c`（命令位置の公開資料なし） · `00572928`（命令位置の公開資料なし）

~~~diff
- 005728d4 ["INT_ADD", "register:40f0:8", ["const:5728d4:8", "const:4:8"]]
- 005728d4 ["CALL", null, ["callee:00588eac:8"]]
+ 00572914 ["INT_ADD", "register:40f0:8", ["const:572914:8", "const:4:8"]]
+ 00572914 ["CALL", null, ["callee:00588eac:8"]]
- 005728d4 bytes 66590094
+ 00572914 bytes 66590094
- 005728dc ["INT_ADD", "register:40f0:8", ["const:5728dc:8", "const:4:8"]]
- 005728dc ["CALL", null, ["callee:0058919c:8"]]
+ 0057291c ["INT_ADD", "register:40f0:8", ["const:57291c:8", "const:4:8"]]
+ 0057291c ["CALL", null, ["callee:0058919c:8"]]
- 005728dc bytes 205a0094
+ 0057291c bytes 205a0094
- 005728e8 ["COPY", "tmp:0:8", ["const:d69:8"]]
- 005728e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005728e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005728e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00572928 ["COPY", "tmp:0:8", ["const:d0d:8"]]
+ 00572928 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00572928 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00572928 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005728e8 bytes 29a53591
+ 00572928 bytes 29353491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7984982820129f43aa09b7c786960f8"></a>

### [`005729e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005729e4.md) → [`00572a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572a24.md) FUN_00572a24

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005509a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509a8.md) · 呼出先 11件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`005509e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509e8.md) · 呼出先 11件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00572a60",
      "incomplete_value": true,
      "site": "00572a78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f2d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572a20",
      "incomplete_value": true,
      "site": "00572a38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:eed:8"
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
      "definition_site": "00572a7c",
      "incomplete_value": true,
      "site": "00572a88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cc5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572a3c",
      "incomplete_value": true,
      "site": "00572a48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c94:8"
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
      "definition_site": "00572a8c",
      "incomplete_value": true,
      "site": "00572a8c",
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
      "definition_site": "00572a4c",
      "incomplete_value": true,
      "site": "00572a4c",
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
      "00572a60",
      "READ",
      [
        "storage",
        "002bfeed",
        null,
        "string"
      ]
    ],
    [
      "00572a7c",
      "READ",
      [
        "storage",
        "002b3c94",
        null,
        "string"
      ]
    ],
    [
      "00572a80",
      "READ",
      [
        "storage",
        "002b3ca1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00572a60",
      "READ",
      [
        "storage",
        "002bff2d",
        null,
        "string"
      ]
    ],
    [
      "00572a7c",
      "READ",
      [
        "storage",
        "002b3cc5",
        null,
        "string"
      ]
    ],
    [
      "00572a80",
      "READ",
      [
        "storage",
        "002b3cd2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005729e4.md#insn-00572a08) · [`00572a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005729e4.md#insn-00572a8c) · [`00572a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005729e4.md#insn-00572a10)
- 新版 `00572a48`（命令位置の公開資料なし） · `00572acc`（命令位置の公開資料なし） · `00572a50`（命令位置の公開資料なし）

~~~diff
- 00572a08 ["INT_ADD", "register:40f0:8", ["const:572a08:8", "const:4:8"]]
- 00572a08 ["CALL", null, ["callee:00588eac:8"]]
+ 00572a48 ["INT_ADD", "register:40f0:8", ["const:572a48:8", "const:4:8"]]
+ 00572a48 ["CALL", null, ["callee:00588eac:8"]]
- 00572a08 bytes 19590094
+ 00572a48 bytes 19590094
- 00572a8c ["INT_ADD", "register:40f0:8", ["const:572a8c:8", "const:4:8"]]
- 00572a8c ["CALL", null, ["callee:00589184:8"]]
+ 00572acc ["INT_ADD", "register:40f0:8", ["const:572acc:8", "const:4:8"]]
+ 00572acc ["CALL", null, ["callee:00589184:8"]]
- 00572a8c bytes ae590094
+ 00572acc bytes ae590094
- 00572a10 ["INT_ADD", "register:40f0:8", ["const:572a10:8", "const:4:8"]]
- 00572a10 ["CALL", null, ["callee:0058919c:8"]]
+ 00572a50 ["INT_ADD", "register:40f0:8", ["const:572a50:8", "const:4:8"]]
+ 00572a50 ["CALL", null, ["callee:0058919c:8"]]
- 00572a10 bytes d3590094
+ 00572a50 bytes d3590094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24fde7c8cda0a2b4829c9957cbdc990b"></a>

### [`00572ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572ba0.md) → [`00572be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572be0.md) FUN_00572be0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005509ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509ac.md) · 呼出先 2件 [`00574ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ef0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005509ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509ec.md) · 呼出先 2件 [`00574f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574f30.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00572c48",
      "incomplete_value": false,
      "site": "00572c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572c08",
      "incomplete_value": false,
      "site": "00572c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "00572c48",
      "PARAM",
      [
        "storage",
        "00ca6170",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00572c48",
      "PARAM",
      [
        "storage",
        "00ca6270",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572ba0.md#insn-00572c14) · [`00572bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572ba0.md#insn-00572bd8) · [`00572c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572ba0.md#insn-00572c00)
- 新版 `00572c54`（命令位置の公開資料なし） · `00572c18`（命令位置の公開資料なし） · `00572c40`（命令位置の公開資料なし）

~~~diff
- 00572c14 ["INT_ADD", "register:40f0:8", ["const:572c14:8", "const:4:8"]]
- 00572c14 ["CALL", null, ["callee:00574f30:8"]]
+ 00572c54 ["INT_ADD", "register:40f0:8", ["const:572c54:8", "const:4:8"]]
+ 00572c54 ["CALL", null, ["callee:00574f30:8"]]
- 00572c14 bytes b7080094
+ 00572c54 bytes b7080094
- 00572bd8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00572bd8 ["INT_ADD", "register:40f0:8", ["const:572bd8:8", "const:4:8"]]
- 00572bd8 ["CALLIND", null, ["register:0:8"]]
+ 00572c18 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00572c18 ["INT_ADD", "register:40f0:8", ["const:572c18:8", "const:4:8"]]
+ 00572c18 ["CALLIND", null, ["register:0:8"]]
- 00572bd8 bytes 20013fd6
+ 00572c18 bytes 20013fd6
- 00572c00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00572c00 ["INT_ADD", "register:40f0:8", ["const:572c00:8", "const:4:8"]]
- 00572c00 ["CALLIND", null, ["register:0:8"]]
+ 00572c40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00572c40 ["INT_ADD", "register:40f0:8", ["const:572c40:8", "const:4:8"]]
+ 00572c40 ["CALLIND", null, ["register:0:8"]]
- 00572c00 bytes 00013fd6
+ 00572c40 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6c393f6cf7f7594f0b7ece22db9dd5e"></a>

### [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) → [`00572ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md) Java_jp_co_ponos_battlecats_MyActivity_onIapList

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0057196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/0057196c.md) [`00574478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574478.md) [`00575124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575124.md)
- 新版 呼出元 0件  · 呼出先 18件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`005719ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005719ac.md) [`005744b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/005744b8.md) [`00575164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575164.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.32% / 新版 95.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00572d7c",
      "incomplete_value": false,
      "site": "00572d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572d3c",
      "incomplete_value": false,
      "site": "00572d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "definition_site": "00572e28",
      "incomplete_value": true,
      "site": "00572e2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572de8",
      "incomplete_value": true,
      "site": "00572dec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00572eb8",
      "incomplete_value": true,
      "site": "00572ec4",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:250:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572e78",
      "incomplete_value": true,
      "site": "00572e84",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:29d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00572ce4",
      "READ",
      [
        "storage",
        "00ca61a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00572d7c",
      "DATA",
      [
        "storage",
        "00c6bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00572e28",
      "READ",
      [
        "storage",
        "002c2a00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00572ce4",
      "READ",
      [
        "storage",
        "00ca62a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00572d7c",
      "DATA",
      [
        "storage",
        "00c6bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00572e28",
      "READ",
      [
        "storage",
        "002c2a40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00573000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md#insn-00573000) · [`005730e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md#insn-005730e0) · [`00573128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md#insn-00573128)
- 新版 `00573040`（命令位置の公開資料なし） · `00573120`（命令位置の公開資料なし） · `00573168`（命令位置の公開資料なし）

~~~diff
- 00573000 ["INT_ADD", "register:40f0:8", ["const:573000:8", "const:4:8"]]
- 00573000 ["CALL", null, ["callee:00c57f80:8"]]
+ 00573040 ["INT_ADD", "register:40f0:8", ["const:573040:8", "const:4:8"]]
+ 00573040 ["CALL", null, ["callee:00c57f80:8"]]
- 00573000 bytes ac931b94
+ 00573040 bytes d0931b94
- 005730e0 ["COPY", "tmp:0:8", ["const:b12:8"]]
- 005730e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005730e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005730e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00573120 ["COPY", "tmp:0:8", ["const:ab6:8"]]
+ 00573120 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00573120 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00573120 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005730e0 bytes 29492c91
+ 00573120 bytes 29d92a91
- 00573128 ["COPY", "register:0:8", ["register:4048:8"]]
- 00573128 ["INT_ADD", "register:40f0:8", ["const:573128:8", "const:4:8"]]
- 00573128 ["CALLIND", null, ["register:0:8"]]
+ 00573168 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00573168 ["INT_ADD", "register:40f0:8", ["const:573168:8", "const:4:8"]]
+ 00573168 ["CALLIND", null, ["register:0:8"]]
- 00573128 bytes 20013fd6
+ 00573168 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35b2f617199a4ba1a6ee52e70fde1c1e"></a>

### [`00573e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md) → [`00573ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ec0.md) Java_jp_co_ponos_battlecats_MyActivity_onIapPurchases

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`005712e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md) [`0058a624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a624.md) [`0058a720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a720.md) [`0058a7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a7d8.md) [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00571320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md) [`0058a664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a664.md) [`0058a760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a760.md) [`0058a818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a818.md) [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 98.37% / 新版 98.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00573ffc",
      "incomplete_value": true,
      "site": "00573ffc",
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
      "definition_site": "00573fbc",
      "incomplete_value": true,
      "site": "00573fbc",
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00573fbc"
      ],
      [
        "FALL_THROUGH",
        "00573ffc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00573ffc",
      "incomplete_value": true,
      "site": "00574000",
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
      "definition_site": "00573fbc",
      "incomplete_value": true,
      "site": "00573fc0",
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
      "00573ff8",
      "READ",
      [
        "storage",
        "00ca6190",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00573ff8",
      "READ",
      [
        "storage",
        "00ca6290",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00573ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md#insn-00573ec0) · [`00573ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md#insn-00573ecc) · [`00573edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md#insn-00573edc)
- 新版 `00573f00`（命令位置の公開資料なし） · `00573f0c`（命令位置の公開資料なし） · `00573f1c`（命令位置の公開資料なし）

~~~diff
- 00573ec0 ["INT_ADD", "register:40f0:8", ["const:573ec0:8", "const:4:8"]]
- 00573ec0 ["CALL", null, ["callee:0058a664:8"]]
+ 00573f00 ["INT_ADD", "register:40f0:8", ["const:573f00:8", "const:4:8"]]
+ 00573f00 ["CALL", null, ["callee:0058a664:8"]]
- 00573ec0 bytes d9590094
+ 00573f00 bytes d9590094
- 00573ecc ["INT_ADD", "register:40f0:8", ["const:573ecc:8", "const:4:8"]]
- 00573ecc ["CALL", null, ["callee:0058a664:8"]]
+ 00573f0c ["INT_ADD", "register:40f0:8", ["const:573f0c:8", "const:4:8"]]
+ 00573f0c ["CALL", null, ["callee:0058a664:8"]]
- 00573ecc bytes d6590094
+ 00573f0c bytes d6590094
- 00573edc ["INT_ADD", "register:40f0:8", ["const:573edc:8", "const:4:8"]]
- 00573edc ["CALL", null, ["callee:0058a818:8"]]
+ 00573f1c ["INT_ADD", "register:40f0:8", ["const:573f1c:8", "const:4:8"]]
+ 00573f1c ["CALL", null, ["callee:0058a818:8"]]
- 00573edc bytes 3f5a0094
+ 00573f1c bytes 3f5a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6595408f2d127892a0fae0b961069e9a"></a>

### [`005740e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md) → [`00574120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574120.md) Java_jp_co_ponos_battlecats_MyActivity_onIapPurchases2

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`005712e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md) [`0058a624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a624.md) [`0058a720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a720.md) [`0058a7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a7d8.md) [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00571320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md) [`0058a664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a664.md) [`0058a760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a760.md) [`0058a818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a818.md) [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 98.74% / 新版 98.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005742b8",
      "incomplete_value": true,
      "site": "005742b8",
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
      "definition_site": "00574278",
      "incomplete_value": true,
      "site": "00574278",
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00574278"
      ],
      [
        "FALL_THROUGH",
        "005742b8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "005742b8",
      "incomplete_value": true,
      "site": "005742bc",
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
      "definition_site": "00574278",
      "incomplete_value": true,
      "site": "0057427c",
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
      "005742b4",
      "READ",
      [
        "storage",
        "00ca6190",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005742b4",
      "READ",
      [
        "storage",
        "00ca6290",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md#insn-00574128) · [`00574134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md#insn-00574134) · [`0057414c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md#insn-0057414c)
- 新版 `00574168`（命令位置の公開資料なし） · `00574174`（命令位置の公開資料なし） · `0057418c`（命令位置の公開資料なし）

~~~diff
- 00574128 ["INT_ADD", "register:40f0:8", ["const:574128:8", "const:4:8"]]
- 00574128 ["CALL", null, ["callee:0058a664:8"]]
+ 00574168 ["INT_ADD", "register:40f0:8", ["const:574168:8", "const:4:8"]]
+ 00574168 ["CALL", null, ["callee:0058a664:8"]]
- 00574128 bytes 3f590094
+ 00574168 bytes 3f590094
- 00574134 ["INT_ADD", "register:40f0:8", ["const:574134:8", "const:4:8"]]
- 00574134 ["CALL", null, ["callee:0058a664:8"]]
+ 00574174 ["INT_ADD", "register:40f0:8", ["const:574174:8", "const:4:8"]]
+ 00574174 ["CALL", null, ["callee:0058a664:8"]]
- 00574134 bytes 3c590094
+ 00574174 bytes 3c590094
- 0057414c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057414c ["INT_ADD", "register:40f0:8", ["const:57414c:8", "const:4:8"]]
- 0057414c ["CALLIND", null, ["register:0:8"]]
+ 0057418c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057418c ["INT_ADD", "register:40f0:8", ["const:57418c:8", "const:4:8"]]
+ 0057418c ["CALLIND", null, ["register:0:8"]]
- 0057414c bytes 00013fd6
+ 0057418c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3c64eb9e77ceb30c4ac0013d96ceff5"></a>

### [`005743e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005743e4.md) → [`00574424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574424.md) FUN_00574424

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00574428",
      "incomplete_value": false,
      "site": "0057442c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005743e8",
      "incomplete_value": false,
      "site": "005743ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "0057442c",
      "DATA",
      [
        "storage",
        "00c6b990",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057442c",
      "DATA",
      [
        "storage",
        "00c6ba60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005743e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005743e4.md#insn-005743e8)
- 新版 `00574428`（命令位置の公開資料なし）

~~~diff
- 005743e8 ["COPY", "tmp:0:8", ["const:990:8"]]
- 005743e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005743e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005743e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574428 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 00574428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005743e8 bytes 08412691
+ 00574428 bytes 08812991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c94fb070b8aae92b934f84c6fdd343a3"></a>

### [`005743f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005743f4.md) → [`00574434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574434.md) FUN_00574434

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00574444",
      "incomplete_value": false,
      "site": "0057444c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574404",
      "incomplete_value": false,
      "site": "0057440c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "0057444c",
      "DATA",
      [
        "storage",
        "00c6b990",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057444c",
      "DATA",
      [
        "storage",
        "00c6ba60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005743f4.md#insn-00574404) · [`00574410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005743f4.md#insn-00574410)
- 新版 `00574444`（命令位置の公開資料なし） · `00574450`（命令位置の公開資料なし）

~~~diff
- 00574404 ["COPY", "tmp:0:8", ["const:990:8"]]
- 00574404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574444 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 00574444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574404 bytes 08412691
+ 00574444 bytes 08812991
- 00574410 ["INT_ADD", "register:40f0:8", ["const:574410:8", "const:4:8"]]
- 00574410 ["CALL", null, ["callee:00c57f70:8"]]
+ 00574450 ["INT_ADD", "register:40f0:8", ["const:574450:8", "const:4:8"]]
+ 00574450 ["CALL", null, ["callee:00c57f70:8"]]
- 00574410 bytes a48e1b94
+ 00574450 bytes c88e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77e751c593e17b8e265001488b5ecf4a"></a>

### [`00574478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574478.md) → [`005744b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/005744b8.md) FUN_005744b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 1件 [`00572ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005744e8",
      "incomplete_value": true,
      "site": "005744e8",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005744a8",
      "incomplete_value": true,
      "site": "005744a8",
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
            "const:9e0:8"
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
      "005744e8",
      "DATA",
      [
        "storage",
        "00c6b9e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005744e8",
      "DATA",
      [
        "storage",
        "00c6bab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574478.md#insn-00574498) · [`005744e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574478.md#insn-005744e0) · [`0057450c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574478.md#insn-0057450c)
- 新版 `005744d8`（命令位置の公開資料なし） · `00574520`（命令位置の公開資料なし） · `0057454c`（命令位置の公開資料なし）

~~~diff
- 00574498 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 00574498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005744d8 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 005744d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005744d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005744d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574498 bytes 08812791
+ 005744d8 bytes 08c12a91
- 005744e0 ["INT_ADD", "register:40f0:8", ["const:5744e0:8", "const:4:8"]]
- 005744e0 ["CALL", null, ["callee:0043bb60:8"]]
+ 00574520 ["INT_ADD", "register:40f0:8", ["const:574520:8", "const:4:8"]]
+ 00574520 ["CALL", null, ["callee:0043bb60:8"]]
- 005744e0 bytes 901dfb97
+ 00574520 bytes 901dfb97
- 0057450c ["INT_ADD", "register:40f0:8", ["const:57450c:8", "const:4:8"]]
- 0057450c ["CALL", null, ["callee:0043bb60:8"]]
+ 0057454c ["INT_ADD", "register:40f0:8", ["const:57454c:8", "const:4:8"]]
+ 0057454c ["CALL", null, ["callee:0043bb60:8"]]
- 0057450c bytes 851dfb97
+ 0057454c bytes 851dfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a2787857e74baa0ee60c176d643505f"></a>

### [`00574728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574728.md) → [`00574768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574768.md) FUN_00574768

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00574424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574424.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00574464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574464.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00574780",
      "incomplete_value": false,
      "site": "00574784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574740",
      "incomplete_value": false,
      "site": "00574744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "00574784",
      "DATA",
      [
        "storage",
        "00c6b9e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574784",
      "DATA",
      [
        "storage",
        "00c6bab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574728.md#insn-00574740) · [`0057477c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574728.md#insn-0057477c) · [`0057478c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574728.md#insn-0057478c)
- 新版 `00574780`（命令位置の公開資料なし） · `005747bc`（命令位置の公開資料なし） · `005747cc`（命令位置の公開資料なし）

~~~diff
- 00574740 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 00574740 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00574740 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00574740 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00574780 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 00574780 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00574780 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00574780 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00574740 bytes 29812791
+ 00574780 bytes 29c12a91
- 0057477c ["INT_ADD", "register:40f0:8", ["const:57477c:8", "const:4:8"]]
- 0057477c ["CALL", null, ["callee:00c57f80:8"]]
+ 005747bc ["INT_ADD", "register:40f0:8", ["const:5747bc:8", "const:4:8"]]
+ 005747bc ["CALL", null, ["callee:00c57f80:8"]]
- 0057477c bytes cd8d1b94
+ 005747bc bytes f18d1b94
- 0057478c ["INT_ADD", "register:40f0:8", ["const:57478c:8", "const:4:8"]]
- 0057478c ["CALL", null, ["callee:00c57f80:8"]]
+ 005747cc ["INT_ADD", "register:40f0:8", ["const:5747cc:8", "const:4:8"]]
+ 005747cc ["CALL", null, ["callee:00c57f80:8"]]
- 0057478c bytes c98d1b94
+ 005747cc bytes ed8d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d63ea2ab396cc4f892bf97289624577"></a>

### [`005747c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005747c8.md) → [`00574808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574808.md) FUN_00574808

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057480c",
      "incomplete_value": true,
      "site": "00574810",
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
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005747cc",
      "incomplete_value": true,
      "site": "005747d0",
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
            "const:a48:8"
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
      "00574810",
      "DATA",
      [
        "storage",
        "00c6ba48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574810",
      "DATA",
      [
        "storage",
        "00c6bb18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005747cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005747c8.md#insn-005747cc)
- 新版 `0057480c`（命令位置の公開資料なし）

~~~diff
- 005747cc ["COPY", "tmp:0:8", ["const:a48:8"]]
- 005747cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005747cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005747cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057480c ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 0057480c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057480c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057480c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005747cc bytes 08212991
+ 0057480c bytes 08612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9163e4e85a056acb00a6871396f7bcb"></a>

### [`005747d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005747d8.md) → [`00574818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574818.md) FUN_00574818

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00574828",
      "incomplete_value": false,
      "site": "00574830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005747e8",
      "incomplete_value": false,
      "site": "005747f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "00574830",
      "DATA",
      [
        "storage",
        "00c6ba48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574830",
      "DATA",
      [
        "storage",
        "00c6bb18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005747e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005747d8.md#insn-005747e8) · [`005747f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005747d8.md#insn-005747f4)
- 新版 `00574828`（命令位置の公開資料なし） · `00574834`（命令位置の公開資料なし）

~~~diff
- 005747e8 ["COPY", "tmp:0:8", ["const:a48:8"]]
- 005747e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005747e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005747e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574828 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 00574828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005747e8 bytes 08212991
+ 00574828 bytes 08612c91
- 005747f4 ["INT_ADD", "register:40f0:8", ["const:5747f4:8", "const:4:8"]]
- 005747f4 ["CALL", null, ["callee:00c57f70:8"]]
+ 00574834 ["INT_ADD", "register:40f0:8", ["const:574834:8", "const:4:8"]]
+ 00574834 ["CALL", null, ["callee:00c57f70:8"]]
- 005747f4 bytes ab8d1b94
+ 00574834 bytes cf8d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0c2db6239204e6799d441cbd683d206"></a>

### [`0057485c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/0057485c.md) → [`0057489c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/0057489c.md) FUN_0057489c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005712e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 1件 [`00571320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005748c0",
      "incomplete_value": false,
      "site": "005748c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574880",
      "incomplete_value": false,
      "site": "00574880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "005748c0",
      "DATA",
      [
        "storage",
        "00c6ba98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005748c0",
      "DATA",
      [
        "storage",
        "00c6bb68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/0057485c.md#insn-00574878) · [`0057487c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/0057485c.md#insn-0057487c)
- 新版 `005748b8`（命令位置の公開資料なし） · `005748bc`（命令位置の公開資料なし）

~~~diff
- 00574878 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 00574878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005748b8 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 005748b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005748b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005748b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574878 bytes 08612a91
+ 005748b8 bytes 08a12d91
- 0057487c ["COPY", "register:40a8:8", ["register:4000:8"]]
- 0057487c bytes f50300aa
+ 005748bc ["COPY", "register:40a8:8", ["register:4000:8"]]
+ 005748bc bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19ba52577011c03dfd000de188510a8e"></a>

### [`00574acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574acc.md) → [`00574b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574b0c.md) FUN_00574b0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574808.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00574848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574848.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00574b24",
      "incomplete_value": false,
      "site": "00574b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574ae4",
      "incomplete_value": false,
      "site": "00574ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
      "00574b28",
      "DATA",
      [
        "storage",
        "00c6ba98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574b28",
      "DATA",
      [
        "storage",
        "00c6bb68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574acc.md#insn-00574b28) · [`00574ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574acc.md#insn-00574ae4) · [`00574af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574acc.md#insn-00574af8)
- 新版 `00574b68`（命令位置の公開資料なし） · `00574b24`（命令位置の公開資料なし） · `00574b38`（命令位置の公開資料なし）

~~~diff
- 00574b28 ["INT_ADD", "register:40f0:8", ["const:574b28:8", "const:4:8"]]
- 00574b28 ["CALL", null, ["callee:00c53da0:8"]]
+ 00574b68 ["INT_ADD", "register:40f0:8", ["const:574b68:8", "const:4:8"]]
+ 00574b68 ["CALL", null, ["callee:00c53da0:8"]]
- 00574b28 bytes 767c1b94
+ 00574b68 bytes 8e7c1b94
- 00574ae4 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 00574ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574b24 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 00574b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574ae4 bytes 08612a91
+ 00574b24 bytes 08a12d91
- 00574af8 ["INT_ADD", "register:40f0:8", ["const:574af8:8", "const:4:8"]]
- 00574af8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00574b38 ["INT_ADD", "register:40f0:8", ["const:574b38:8", "const:4:8"]]
+ 00574b38 ["CALL", null, ["callee:00c53da0:8"]]
- 00574af8 bytes 827c1b94
+ 00574b38 bytes 9a7c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f5fd9f2d4c536e1b62b897f15c99210"></a>

### [`00574ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ba4.md) → [`00574be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574be4.md) FUN_00574be4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00573b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573b60.md) · 呼出先 2件 [`0059765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00573ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ba0.md) · 呼出先 2件 [`0059769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059769c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00574c0c",
      "incomplete_value": false,
      "site": "00574c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574bcc",
      "incomplete_value": false,
      "site": "00574bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "definition_site": "00574c20",
      "incomplete_value": false,
      "site": "00574c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574be0",
      "incomplete_value": false,
      "site": "00574be0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "00574c14",
      "DATA",
      [
        "storage",
        "00c6ba48",
        null,
        "undefined *"
      ]
    ],
    [
      "00574c20",
      "DATA",
      [
        "storage",
        "00c6ba98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574c14",
      "DATA",
      [
        "storage",
        "00c6bb18",
        null,
        "undefined *"
      ]
    ],
    [
      "00574c20",
      "DATA",
      [
        "storage",
        "00c6bb68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ba4.md#insn-00574bc4) · [`00574bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ba4.md#insn-00574bcc) · [`00574bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ba4.md#insn-00574bd0)
- 新版 `00574c04`（命令位置の公開資料なし） · `00574c0c`（命令位置の公開資料なし）

~~~diff
- 00574bc4 ["INT_ADD", "register:40f0:8", ["const:574bc4:8", "const:4:8"]]
- 00574bc4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00574c04 ["INT_ADD", "register:40f0:8", ["const:574c04:8", "const:4:8"]]
+ 00574c04 ["CALL", null, ["callee:00c57f60:8"]]
- 00574bc4 bytes b38c1b94
+ 00574c04 bytes d78c1b94
- 00574bcc ["COPY", "tmp:0:8", ["const:a48:8"]]
- 00574bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574c0c ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 00574c0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574c0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574c0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574bcc bytes 08212991
+ 00574c0c bytes 08612c91
- 00574bd0 ["COPY", "register:40b8:8", ["register:4000:8"]]
- 00574bd0 bytes f70300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba2ed3703e0ceba4c12472eacd7c0185"></a>

### [`00575344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575344.md) → [`00575384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575384.md) FUN_00575384

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005751e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005751e8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00575228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575228.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00575390",
      "incomplete_value": false,
      "site": "00575394",
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
      "definition_site": "00575350",
      "incomplete_value": false,
      "site": "00575354",
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
      "00575390",
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
      "00575390",
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

- 旧版 [`00575354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575344.md#insn-00575354) · [`00575350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575344.md#insn-00575350)
- 新版 `00575394`（命令位置の公開資料なし） · `00575390`（命令位置の公開資料なし）

~~~diff
- 00575354 ["INT_ADD", "register:40f0:8", ["const:575354:8", "const:4:8"]]
- 00575354 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00575394 ["INT_ADD", "register:40f0:8", ["const:575394:8", "const:4:8"]]
+ 00575394 ["CALL", null, ["callee:0043b7b8:8"]]
- 00575354 bytes 0919fb97
+ 00575394 bytes 0919fb97
- 00575350 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00575350 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00575350 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00575350 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00575390 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00575390 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00575390 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00575390 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00575350 bytes 00303d91
+ 00575390 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e5c3160366b9af1ad1a324d189fd614"></a>

### [`00575358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575358.md) → [`00575398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575398.md) _INIT_29

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`005717c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005717c8.md) [`005717f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005717f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00571808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571808.md) [`00571838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 45.83% / 新版 45.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005753c0",
      "incomplete_value": false,
      "site": "005753c0",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:270:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00575380",
      "incomplete_value": false,
      "site": "00575380",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:170:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005753dc",
      "incomplete_value": false,
      "site": "005753dc",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:2a0:8"
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
      "definition_site": "0057539c",
      "incomplete_value": false,
      "site": "0057539c",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:1a0:8"
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005753e0",
      "incomplete_value": false,
      "site": "005753e0",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:2a0:8"
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
      "definition_site": "005753a0",
      "incomplete_value": false,
      "site": "005753a0",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:1a0:8"
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
      "005753b0",
      "PARAM",
      [
        "storage",
        "00ca6170",
        null,
        null
      ]
    ],
    [
      "005753b8",
      "PARAM",
      [
        "storage",
        "005717c8",
        null,
        null
      ]
    ],
    [
      "005753bc",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005753b0",
      "PARAM",
      [
        "storage",
        "00ca6270",
        null,
        null
      ]
    ],
    [
      "005753b8",
      "PARAM",
      [
        "storage",
        "00571808",
        null,
        null
      ]
    ],
    [
      "005753bc",
      "PARAM",
      [
        "storage",
        "00c63060",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00575368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575358.md#insn-00575368) · [`00575384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575358.md#insn-00575384) · [`00575364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575358.md#insn-00575364)
- 新版 `005753a8`（命令位置の公開資料なし） · `005753c4`（命令位置の公開資料なし） · `005753a4`（命令位置の公開資料なし）

~~~diff
- 00575368 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 00575368 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00575368 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00575368 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005753a8 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 005753a8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005753a8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005753a8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00575368 bytes 73423e91
+ 005753a8 bytes 73820191
- 00575384 ["INT_ADD", "register:40f0:8", ["const:575384:8", "const:4:8"]]
- 00575384 ["CALL", null, ["callee:00c57f00:8"]]
+ 005753c4 ["INT_ADD", "register:40f0:8", ["const:5753c4:8", "const:4:8"]]
+ 005753c4 ["CALL", null, ["callee:00c57f00:8"]]
- 00575384 bytes ab8a1b94
+ 005753c4 bytes cf8a1b94
- 00575364 ["COPY", "register:4098:8", ["const:c62000:8"]]
+ 005753a4 ["COPY", "register:4098:8", ["const:c63000:8"]]
- 00575364 bytes 733700b0
+ 005753a4 bytes 733700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f417b692519a52e5c180aa06d7849261"></a>

### [`00575418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575418.md) → [`00575458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575458.md) FUN_00575458

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b0.md) · 呼出先 11件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`005509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509f0.md) · 呼出先 11件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057549c",
      "incomplete_value": true,
      "site": "005754b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:645:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057545c",
      "incomplete_value": true,
      "site": "00575474",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6a1:8"
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
      "definition_site": "005754b8",
      "incomplete_value": true,
      "site": "005754c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:48d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00575478",
      "incomplete_value": true,
      "site": "00575484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e1:8"
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
      "definition_site": "005754c8",
      "incomplete_value": true,
      "site": "005754c8",
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
      "definition_site": "00575488",
      "incomplete_value": true,
      "site": "00575488",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057549c",
      "READ",
      [
        "storage",
        "002a56a1",
        null,
        "string"
      ]
    ],
    [
      "005754b8",
      "READ",
      [
        "storage",
        "002bb4e1",
        null,
        "string"
      ]
    ],
    [
      "005754bc",
      "READ",
      [
        "storage",
        "002bb4ee",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057549c",
      "READ",
      [
        "storage",
        "002a5645",
        null,
        "string"
      ]
    ],
    [
      "005754b8",
      "READ",
      [
        "storage",
        "002bb48d",
        null,
        "string"
      ]
    ],
    [
      "005754bc",
      "READ",
      [
        "storage",
        "002bb49a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00575444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575418.md#insn-00575444) · [`005754c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575418.md#insn-005754c8) · [`0057543c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575418.md#insn-0057543c)
- 新版 `00575484`（命令位置の公開資料なし） · `00575508`（命令位置の公開資料なし） · `0057547c`（命令位置の公開資料なし）

~~~diff
- 00575444 ["INT_ADD", "register:40f0:8", ["const:575444:8", "const:4:8"]]
- 00575444 ["CALL", null, ["callee:0058919c:8"]]
+ 00575484 ["INT_ADD", "register:40f0:8", ["const:575484:8", "const:4:8"]]
+ 00575484 ["CALL", null, ["callee:0058919c:8"]]
- 00575444 bytes 464f0094
+ 00575484 bytes 464f0094
- 005754c8 ["INT_ADD", "register:40f0:8", ["const:5754c8:8", "const:4:8"]]
- 005754c8 ["CALL", null, ["callee:00589184:8"]]
+ 00575508 ["INT_ADD", "register:40f0:8", ["const:575508:8", "const:4:8"]]
+ 00575508 ["CALL", null, ["callee:00589184:8"]]
- 005754c8 bytes 1f4f0094
+ 00575508 bytes 1f4f0094
- 0057543c ["INT_ADD", "register:40f0:8", ["const:57543c:8", "const:4:8"]]
- 0057543c ["CALL", null, ["callee:00588eac:8"]]
+ 0057547c ["INT_ADD", "register:40f0:8", ["const:57547c:8", "const:4:8"]]
+ 0057547c ["CALL", null, ["callee:00588eac:8"]]
- 0057543c bytes 8c4e0094
+ 0057547c bytes 8c4e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-528fce98e5a8b7a74037b3db0c11937c"></a>

### [`00575588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575588.md) → [`005755c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005755c8.md) FUN_005755c8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b4.md) · 呼出先 14件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00575d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575d8c.md) [`00575f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575f98.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md)
- 新版 呼出元 1件 [`005509f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509f4.md) · 呼出先 14件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00575dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575dcc.md) [`00575fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575fd8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.40% / 新版 82.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00575618",
      "incomplete_value": true,
      "site": "00575628",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2fa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005755d8",
      "incomplete_value": true,
      "site": "005755e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:347:8"
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
      "definition_site": "00575638",
      "incomplete_value": true,
      "site": "00575638",
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
      "definition_site": "005755f8",
      "incomplete_value": true,
      "site": "005755f8",
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
      "definition_site": "0057562c",
      "incomplete_value": true,
      "site": "00575640",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005755ec",
      "incomplete_value": true,
      "site": "00575600",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00575618",
      "READ",
      [
        "storage",
        "002a4347",
        null,
        "string"
      ]
    ],
    [
      "0057561c",
      "READ",
      [
        "storage",
        "002a4356",
        null,
        "string"
      ]
    ],
    [
      "0057562c",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00575618",
      "READ",
      [
        "storage",
        "002a42fa",
        null,
        "string"
      ]
    ],
    [
      "0057561c",
      "READ",
      [
        "storage",
        "002a4309",
        null,
        "string"
      ]
    ],
    [
      "0057562c",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005755d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575588.md#insn-005755d0) · [`00575640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575588.md#insn-00575640)
- 新版 `00575610`（命令位置の公開資料なし） · `00575614`（命令位置の公開資料なし） · `00575680`（命令位置の公開資料なし）

~~~diff
- 005755d0 ["COPY", "tmp:0:8", ["const:347:8"]]
- 005755d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005755d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005755d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00575610 ["COPY", "tmp:0:8", ["const:2fa:8"]]
+ 00575610 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00575610 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00575610 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005755d0 bytes 081d0d91
+ 00575610 bytes 08e90b91
+ 00575614 ["COPY", "register:4048:8", ["const:2c2000:8"]]
+ 00575614 bytes 69eaffb0
- 00575640 ["INT_ADD", "register:40f0:8", ["const:575640:8", "const:4:8"]]
- 00575640 ["CALL", null, ["callee:00c57f80:8"]]
+ 00575680 ["INT_ADD", "register:40f0:8", ["const:575680:8", "const:4:8"]]
+ 00575680 ["CALL", null, ["callee:00c57f80:8"]]
- 00575640 bytes 1c8a1b94
+ 00575680 bytes 408a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6dec2f4a81b0c93a9b842d439ad7158"></a>

### [`005757d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005757d0.md) → [`00575810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575810.md) FUN_00575810

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b8.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00576150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576150.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 1件 [`005509f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509f8.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00576190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576190.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.72% / 新版 90.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00575858",
      "incomplete_value": true,
      "site": "00575868",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4a3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00575818",
      "incomplete_value": true,
      "site": "00575828",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4f7:8"
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
      "definition_site": "0057585c",
      "incomplete_value": true,
      "site": "00575880",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0057581c",
      "incomplete_value": true,
      "site": "00575840",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057586c",
      "incomplete_value": true,
      "site": "00575884",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057582c",
      "incomplete_value": true,
      "site": "00575844",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b50:8"
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
      "00575858",
      "READ",
      [
        "storage",
        "002bb4f7",
        null,
        "string"
      ]
    ],
    [
      "0057585c",
      "READ",
      [
        "storage",
        "002bb504",
        null,
        "string"
      ]
    ],
    [
      "0057586c",
      "READ",
      [
        "storage",
        "002c2b50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00575858",
      "READ",
      [
        "storage",
        "002bb4a3",
        null,
        "string"
      ]
    ],
    [
      "0057585c",
      "READ",
      [
        "storage",
        "002bb4b0",
        null,
        "string"
      ]
    ],
    [
      "0057586c",
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

- 旧版 [`00575880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005757d0.md#insn-00575880) · [`005757f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005757d0.md#insn-005757f4) · [`005757fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005757d0.md#insn-005757fc)
- 新版 `005758c0`（命令位置の公開資料なし） · `00575834`（命令位置の公開資料なし） · `0057583c`（命令位置の公開資料なし）

~~~diff
- 00575880 ["INT_ADD", "register:40f0:8", ["const:575880:8", "const:4:8"]]
- 00575880 ["CALL", null, ["callee:00c57f80:8"]]
+ 005758c0 ["INT_ADD", "register:40f0:8", ["const:5758c0:8", "const:4:8"]]
+ 005758c0 ["CALL", null, ["callee:00c57f80:8"]]
- 00575880 bytes 8c891b94
+ 005758c0 bytes b0891b94
- 005757f4 ["INT_ADD", "register:40f0:8", ["const:5757f4:8", "const:4:8"]]
- 005757f4 ["CALL", null, ["callee:00588eac:8"]]
+ 00575834 ["INT_ADD", "register:40f0:8", ["const:575834:8", "const:4:8"]]
+ 00575834 ["CALL", null, ["callee:00588eac:8"]]
- 005757f4 bytes 9e4d0094
+ 00575834 bytes 9e4d0094
- 005757fc ["INT_ADD", "register:40f0:8", ["const:5757fc:8", "const:4:8"]]
- 005757fc ["CALL", null, ["callee:0058919c:8"]]
+ 0057583c ["INT_ADD", "register:40f0:8", ["const:57583c:8", "const:4:8"]]
+ 0057583c ["CALL", null, ["callee:0058919c:8"]]
- 005757fc bytes 584e0094
+ 0057583c bytes 584e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5e261f1c2c475b3866be289ca4e1dfd"></a>

### [`00575990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575990.md) → [`005759d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005759d0.md) FUN_005759d0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509bc.md) · 呼出先 13件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 1件 [`005509fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509fc.md) · 呼出先 13件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.54% / 新版 95.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00575a34",
      "incomplete_value": true,
      "site": "00575a4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:312:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005759f4",
      "incomplete_value": true,
      "site": "00575a0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:35f:8"
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
      "00575a34",
      "READ",
      [
        "storage",
        "002a435f",
        null,
        "string"
      ]
    ],
    [
      "00575a68",
      "READ",
      [
        "storage",
        "002bff32",
        null,
        "string"
      ]
    ],
    [
      "00575a68",
      "READ",
      [
        "storage",
        "002bff42",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00575a34",
      "READ",
      [
        "storage",
        "002a4312",
        null,
        "string"
      ]
    ],
    [
      "00575a68",
      "READ",
      [
        "storage",
        "002bff72",
        null,
        "string"
      ]
    ],
    [
      "00575a68",
      "READ",
      [
        "storage",
        "002bff82",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005759dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575990.md#insn-005759dc) · [`005759e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575990.md#insn-005759e4) · [`005759ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575990.md#insn-005759ec)
- 新版 `00575a1c`（命令位置の公開資料なし） · `00575a24`（命令位置の公開資料なし） · `00575a2c`（命令位置の公開資料なし）

~~~diff
- 005759dc ["INT_ADD", "register:40f0:8", ["const:5759dc:8", "const:4:8"]]
- 005759dc ["CALL", null, ["callee:00588eac:8"]]
+ 00575a1c ["INT_ADD", "register:40f0:8", ["const:575a1c:8", "const:4:8"]]
+ 00575a1c ["CALL", null, ["callee:00588eac:8"]]
- 005759dc bytes 244d0094
+ 00575a1c bytes 244d0094
- 005759e4 ["INT_ADD", "register:40f0:8", ["const:5759e4:8", "const:4:8"]]
- 005759e4 ["CALL", null, ["callee:0058919c:8"]]
+ 00575a24 ["INT_ADD", "register:40f0:8", ["const:575a24:8", "const:4:8"]]
+ 00575a24 ["CALL", null, ["callee:0058919c:8"]]
- 005759e4 bytes de4d0094
+ 00575a24 bytes de4d0094
- 005759ec ["COPY", "tmp:0:8", ["const:35f:8"]]
- 005759ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005759ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005759ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00575a2c ["COPY", "tmp:0:8", ["const:312:8"]]
+ 00575a2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00575a2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00575a2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005759ec bytes 297d0d91
+ 00575a2c bytes 29490c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98418a0ee1aff90375c0de90f4a050a5"></a>

### [`00576354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576354.md) → [`00576394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576394.md) _INIT_30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`005753b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005753b8.md) [`005753e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005753e8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005753f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005753f8.md) [`00575428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575428.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005763bc",
      "incomplete_value": false,
      "site": "005763bc",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:2c0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057637c",
      "incomplete_value": false,
      "site": "0057637c",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:1c0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005763d8",
      "incomplete_value": false,
      "site": "005763d8",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:2f0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576398",
      "incomplete_value": false,
      "site": "00576398",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:1f0:8"
              ]
            ]
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
    "new": {
      "definition_site": "005763b4",
      "incomplete_value": false,
      "site": "005763c0",
      "value": [
        "leaf",
        "const:5753f8:8"
      ]
    },
    "old": {
      "definition_site": "00576374",
      "incomplete_value": false,
      "site": "00576380",
      "value": [
        "leaf",
        "const:5753b8:8"
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
      "005763ac",
      "PARAM",
      [
        "storage",
        "00ca61c0",
        null,
        null
      ]
    ],
    [
      "005763b4",
      "PARAM",
      [
        "storage",
        "005753b8",
        null,
        null
      ]
    ],
    [
      "005763b8",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005763ac",
      "PARAM",
      [
        "storage",
        "00ca62c0",
        null,
        null
      ]
    ],
    [
      "005763b4",
      "PARAM",
      [
        "storage",
        "005753f8",
        null,
        null
      ]
    ],
    [
      "005763b8",
      "PARAM",
      [
        "storage",
        "00c63060",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576354.md#insn-00576380) · [`00576360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576354.md#insn-00576360) · [`00576364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576354.md#insn-00576364)
- 新版 `005763c0`（命令位置の公開資料なし） · `005763a0`（命令位置の公開資料なし） · `005763a4`（命令位置の公開資料なし）

~~~diff
- 00576380 ["INT_ADD", "register:40f0:8", ["const:576380:8", "const:4:8"]]
- 00576380 ["CALL", null, ["callee:00c57f00:8"]]
+ 005763c0 ["INT_ADD", "register:40f0:8", ["const:5763c0:8", "const:4:8"]]
+ 005763c0 ["CALL", null, ["callee:00c57f00:8"]]
- 00576380 bytes ac861b94
+ 005763c0 bytes d0861b94
- 00576360 ["COPY", "register:4098:8", ["const:c62000:8"]]
+ 005763a0 ["COPY", "register:4098:8", ["const:c63000:8"]]
- 00576360 bytes 73370090
+ 005763a0 bytes 733700b0
- 00576364 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 00576364 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00576364 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00576364 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005763a4 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 005763a4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005763a4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005763a4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00576364 bytes 73423e91
+ 005763a4 bytes 73820191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-336dcdd552811e6f89272169fd36c2d3"></a>

### [`005763ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005763ac.md) → [`005763ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005763ec.md) FUN_005763ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005509c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509c8.md) · 呼出先 4件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 1件 [`00550a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a08.md) · 呼出先 4件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00576430",
      "incomplete_value": false,
      "site": "00576448",
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
            "const:25a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005763f0",
      "incomplete_value": false,
      "site": "00576408",
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
            "const:2a7:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00576438",
      "incomplete_value": false,
      "site": "00576448",
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
            "const:26a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005763f8",
      "incomplete_value": false,
      "site": "00576408",
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
            "const:2b7:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00576430",
      "PARAM",
      [
        "storage",
        "002a32a7",
        null,
        "string"
      ]
    ],
    [
      "00576438",
      "PARAM",
      [
        "storage",
        "002a32b7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00576430",
      "PARAM",
      [
        "storage",
        "002a325a",
        null,
        "string"
      ]
    ],
    [
      "00576438",
      "PARAM",
      [
        "storage",
        "002a326a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005763c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005763ac.md#insn-005763c8) · [`00576408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005763ac.md#insn-00576408) · [`005763bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005763ac.md#insn-005763bc)
- 新版 `00576408`（命令位置の公開資料なし） · `00576448`（命令位置の公開資料なし） · `005763fc`（命令位置の公開資料なし）

~~~diff
- 005763c8 ["INT_ADD", "register:40f0:8", ["const:5763c8:8", "const:4:8"]]
- 005763c8 ["CALL", null, ["callee:00589890:8"]]
+ 00576408 ["INT_ADD", "register:40f0:8", ["const:576408:8", "const:4:8"]]
+ 00576408 ["CALL", null, ["callee:00589890:8"]]
- 005763c8 bytes 224d0094
+ 00576408 bytes 224d0094
- 00576408 ["COPY", "register:0:8", ["register:4040:8"]]
- 00576408 ["INT_ADD", "register:40f0:8", ["const:576408:8", "const:4:8"]]
- 00576408 ["CALLIND", null, ["register:0:8"]]
+ 00576448 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00576448 ["INT_ADD", "register:40f0:8", ["const:576448:8", "const:4:8"]]
+ 00576448 ["CALLIND", null, ["register:0:8"]]
- 00576408 bytes 00013fd6
+ 00576448 bytes 00013fd6
- 005763bc ["INT_ADD", "register:40f0:8", ["const:5763bc:8", "const:4:8"]]
- 005763bc ["CALL", null, ["callee:00588eac:8"]]
+ 005763fc ["INT_ADD", "register:40f0:8", ["const:5763fc:8", "const:4:8"]]
+ 005763fc ["CALL", null, ["callee:00588eac:8"]]
- 005763bc bytes ac4a0094
+ 005763fc bytes ac4a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e0a971ade5f35810716b506a5cd2aab"></a>

### [`00576440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576440.md) → [`00576480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576480.md) FUN_00576480

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005509cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509cc.md) · 呼出先 4件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 1件 [`00550a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a0c.md) · 呼出先 4件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005764d0",
      "incomplete_value": false,
      "site": "005764e8",
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
            "const:cf6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576490",
      "incomplete_value": false,
      "site": "005764a8",
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
            "const:d52:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005764d8",
      "incomplete_value": false,
      "site": "005764e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:854:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576498",
      "incomplete_value": false,
      "site": "005764a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005764d0",
      "PARAM",
      [
        "storage",
        "002b0d52",
        null,
        "string"
      ]
    ],
    [
      "005764d8",
      "PARAM",
      [
        "storage",
        "002ad8b0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005764d0",
      "PARAM",
      [
        "storage",
        "002b0cf6",
        null,
        "string"
      ]
    ],
    [
      "005764d8",
      "PARAM",
      [
        "storage",
        "002ad854",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576440.md#insn-00576468) · [`005764a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576440.md#insn-005764a8) · [`0057645c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576440.md#insn-0057645c)
- 新版 `005764a8`（命令位置の公開資料なし） · `005764e8`（命令位置の公開資料なし） · `0057649c`（命令位置の公開資料なし）

~~~diff
- 00576468 ["INT_ADD", "register:40f0:8", ["const:576468:8", "const:4:8"]]
- 00576468 ["CALL", null, ["callee:00589890:8"]]
+ 005764a8 ["INT_ADD", "register:40f0:8", ["const:5764a8:8", "const:4:8"]]
+ 005764a8 ["CALL", null, ["callee:00589890:8"]]
- 00576468 bytes fa4c0094
+ 005764a8 bytes fa4c0094
- 005764a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005764a8 ["INT_ADD", "register:40f0:8", ["const:5764a8:8", "const:4:8"]]
- 005764a8 ["CALLIND", null, ["register:0:8"]]
+ 005764e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005764e8 ["INT_ADD", "register:40f0:8", ["const:5764e8:8", "const:4:8"]]
+ 005764e8 ["CALLIND", null, ["register:0:8"]]
- 005764a8 bytes 00013fd6
+ 005764e8 bytes 00013fd6
- 0057645c ["INT_ADD", "register:40f0:8", ["const:57645c:8", "const:4:8"]]
- 0057645c ["CALL", null, ["callee:00588eac:8"]]
+ 0057649c ["INT_ADD", "register:40f0:8", ["const:57649c:8", "const:4:8"]]
+ 0057649c ["CALL", null, ["callee:00588eac:8"]]
- 0057645c bytes 844a0094
+ 0057649c bytes 844a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec805c76a5f367e3c06830bbb12da934"></a>

### [`00576500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576500.md) → [`00576540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576540.md) FUN_00576540

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005509f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509f8.md) · 呼出先 4件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 1件 [`00550a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a38.md) · 呼出先 4件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00576584",
      "incomplete_value": false,
      "site": "0057659c",
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
            "const:3d7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576544",
      "incomplete_value": false,
      "site": "0057655c",
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
            "const:42b:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0057658c",
      "incomplete_value": false,
      "site": "0057659c",
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
            "const:a33:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057654c",
      "incomplete_value": false,
      "site": "0057655c",
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
            "const:a8f:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00576584",
      "PARAM",
      [
        "storage",
        "002ba42b",
        null,
        "string"
      ]
    ],
    [
      "0057658c",
      "PARAM",
      [
        "storage",
        "002aea8f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00576584",
      "PARAM",
      [
        "storage",
        "002ba3d7",
        null,
        "string"
      ]
    ],
    [
      "0057658c",
      "PARAM",
      [
        "storage",
        "002aea33",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057651c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576500.md#insn-0057651c) · [`0057655c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576500.md#insn-0057655c) · [`00576510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576500.md#insn-00576510)
- 新版 `0057655c`（命令位置の公開資料なし） · `0057659c`（命令位置の公開資料なし） · `00576550`（命令位置の公開資料なし）

~~~diff
- 0057651c ["INT_ADD", "register:40f0:8", ["const:57651c:8", "const:4:8"]]
- 0057651c ["CALL", null, ["callee:00589890:8"]]
+ 0057655c ["INT_ADD", "register:40f0:8", ["const:57655c:8", "const:4:8"]]
+ 0057655c ["CALL", null, ["callee:00589890:8"]]
- 0057651c bytes cd4c0094
+ 0057655c bytes cd4c0094
- 0057655c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057655c ["INT_ADD", "register:40f0:8", ["const:57655c:8", "const:4:8"]]
- 0057655c ["CALLIND", null, ["register:0:8"]]
+ 0057659c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057659c ["INT_ADD", "register:40f0:8", ["const:57659c:8", "const:4:8"]]
+ 0057659c ["CALLIND", null, ["register:0:8"]]
- 0057655c bytes 00013fd6
+ 0057659c bytes 00013fd6
- 00576510 ["INT_ADD", "register:40f0:8", ["const:576510:8", "const:4:8"]]
- 00576510 ["CALL", null, ["callee:00588eac:8"]]
+ 00576550 ["INT_ADD", "register:40f0:8", ["const:576550:8", "const:4:8"]]
+ 00576550 ["CALL", null, ["callee:00588eac:8"]]
- 00576510 bytes 574a0094
+ 00576550 bytes 574a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f95a88b651c9e8f892b25de4c426f7c8"></a>

### [`005765bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765bc.md) → [`005765fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005765fc.md) FUN_005765fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005509fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509fc.md) · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00550a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a3c.md) · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00576638",
      "incomplete_value": true,
      "site": "00576650",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f3c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005765f8",
      "incomplete_value": true,
      "site": "00576610",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f0b:8"
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
      "00576638",
      "READ",
      [
        "storage",
        "002b4f0b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00576638",
      "READ",
      [
        "storage",
        "002b4f3c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765bc.md#insn-00576650) · [`005765d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765bc.md#insn-005765d8) · [`005765e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765bc.md#insn-005765e0)
- 新版 `00576690`（命令位置の公開資料なし） · `00576618`（命令位置の公開資料なし） · `00576620`（命令位置の公開資料なし）

~~~diff
- 00576650 ["INT_ADD", "register:40f0:8", ["const:576650:8", "const:4:8"]]
- 00576650 ["CALL", null, ["callee:00589184:8"]]
+ 00576690 ["INT_ADD", "register:40f0:8", ["const:576690:8", "const:4:8"]]
+ 00576690 ["CALL", null, ["callee:00589184:8"]]
- 00576650 bytes bd4a0094
+ 00576690 bytes bd4a0094
- 005765d8 ["INT_ADD", "register:40f0:8", ["const:5765d8:8", "const:4:8"]]
- 005765d8 ["CALL", null, ["callee:00588eac:8"]]
+ 00576618 ["INT_ADD", "register:40f0:8", ["const:576618:8", "const:4:8"]]
+ 00576618 ["CALL", null, ["callee:00588eac:8"]]
- 005765d8 bytes 254a0094
+ 00576618 bytes 254a0094
- 005765e0 ["INT_ADD", "register:40f0:8", ["const:5765e0:8", "const:4:8"]]
- 005765e0 ["CALL", null, ["callee:0058919c:8"]]
+ 00576620 ["INT_ADD", "register:40f0:8", ["const:576620:8", "const:4:8"]]
+ 00576620 ["CALL", null, ["callee:0058919c:8"]]
- 005765e0 bytes df4a0094
+ 00576620 bytes df4a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ccd0ef796bd7f637a264a9c724a61d7"></a>

### [`00576700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576700.md) → [`00576740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576740.md) FUN_00576740

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00576828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576828.md) · 呼出先 7件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 1件 [`00576868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576868.md) · 呼出先 7件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00576768",
      "incomplete_value": true,
      "site": "0057676c",
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
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576728",
      "incomplete_value": true,
      "site": "0057672c",
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
            "const:b60:8"
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
      "0057676c",
      "DATA",
      [
        "storage",
        "00c6bb60",
        null,
        "undefined *"
      ]
    ],
    [
      "00576790",
      "READ",
      [
        "storage",
        "002a32bb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057676c",
      "DATA",
      [
        "storage",
        "00c6bc30",
        null,
        "undefined *"
      ]
    ],
    [
      "00576790",
      "READ",
      [
        "storage",
        "002a326e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576700.md#insn-00576728) · [`00576730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576700.md#insn-00576730) · [`00576738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576700.md#insn-00576738)
- 新版 `00576768`（命令位置の公開資料なし） · `00576770`（命令位置の公開資料なし） · `00576778`（命令位置の公開資料なし）

~~~diff
- 00576728 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 00576728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00576728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00576728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00576768 ["COPY", "tmp:0:8", ["const:c30:8"]]
+ 00576768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00576768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00576768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00576728 bytes 08812d91
+ 00576768 bytes 08c13091
- 00576730 ["INT_ADD", "register:40f0:8", ["const:576730:8", "const:4:8"]]
- 00576730 ["CALL", null, ["callee:00588eac:8"]]
+ 00576770 ["INT_ADD", "register:40f0:8", ["const:576770:8", "const:4:8"]]
+ 00576770 ["CALL", null, ["callee:00588eac:8"]]
- 00576730 bytes cf490094
+ 00576770 bytes cf490094
- 00576738 ["INT_ADD", "register:40f0:8", ["const:576738:8", "const:4:8"]]
- 00576738 ["CALL", null, ["callee:0058919c:8"]]
+ 00576778 ["INT_ADD", "register:40f0:8", ["const:576778:8", "const:4:8"]]
+ 00576778 ["CALL", null, ["callee:0058919c:8"]]
- 00576738 bytes 894a0094
+ 00576778 bytes 894a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-036ea2a29924bd7c954b17e0299cc01e"></a>

### [`0057699c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md) → [`005769dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md) FUN_005769dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00577318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md) [`005778e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md) [`00577c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md)
- 新版 呼出元 3件 [`00577358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577358.md) [`00577920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md) [`00577cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.81% / 新版 96.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00576a50",
      "incomplete_value": true,
      "site": "00576a50",
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:4c1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576a10",
      "incomplete_value": true,
      "site": "00576a10",
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:515:8"
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
      "definition_site": "00576a54",
      "incomplete_value": true,
      "site": "00576a54",
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
      "definition_site": "00576a14",
      "incomplete_value": true,
      "site": "00576a14",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00576a40",
      "READ",
      [
        "storage",
        "002bb515",
        null,
        "string"
      ]
    ],
    [
      "00576a48",
      "READ",
      [
        "storage",
        "002bb51b",
        null,
        "string"
      ]
    ],
    [
      "00576ab8",
      "READ",
      [
        "storage",
        "002c12bb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00576a40",
      "READ",
      [
        "storage",
        "002bb4c1",
        null,
        "string"
      ]
    ],
    [
      "00576a48",
      "READ",
      [
        "storage",
        "002bb4c7",
        null,
        "string"
      ]
    ],
    [
      "00576ab8",
      "READ",
      [
        "storage",
        "002c12fb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005769e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md#insn-005769e0) · [`005769f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md#insn-005769f0) · [`005769fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md#insn-005769fc)
- 新版 `00576a20`（命令位置の公開資料なし） · `00576a30`（命令位置の公開資料なし） · `00576a3c`（命令位置の公開資料なし）

~~~diff
- 005769e0 ["INT_ADD", "register:40f0:8", ["const:5769e0:8", "const:4:8"]]
- 005769e0 ["CALL", null, ["callee:00588eac:8"]]
+ 00576a20 ["INT_ADD", "register:40f0:8", ["const:576a20:8", "const:4:8"]]
+ 00576a20 ["CALL", null, ["callee:00588eac:8"]]
- 005769e0 bytes 23490094
+ 00576a20 bytes 23490094
- 005769f0 ["INT_ADD", "register:40f0:8", ["const:5769f0:8", "const:4:8"]]
- 005769f0 ["CALL", null, ["callee:0058919c:8"]]
+ 00576a30 ["INT_ADD", "register:40f0:8", ["const:576a30:8", "const:4:8"]]
+ 00576a30 ["CALL", null, ["callee:0058919c:8"]]
- 005769f0 bytes db490094
+ 00576a30 bytes db490094
- 005769fc ["COPY", "tmp:0:8", ["const:515:8"]]
- 005769fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005769fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005769fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00576a3c ["COPY", "tmp:0:8", ["const:4c1:8"]]
+ 00576a3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00576a3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00576a3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005769fc bytes 29551491
+ 00576a3c bytes 29051391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4324af62fd06abbb788cedd023983d67"></a>

### [`00576f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576f08.md) → [`00576f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576f48.md) FUN_00576f48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00577318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md) [`00577c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 2件 [`00577358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577358.md) [`00577cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00576fa8",
      "incomplete_value": true,
      "site": "00576fbc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:767:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576f68",
      "incomplete_value": true,
      "site": "00576f7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c3:8"
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
      "definition_site": "00576fc0",
      "incomplete_value": true,
      "site": "00576fc0",
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
      "definition_site": "00576f80",
      "incomplete_value": true,
      "site": "00576f80",
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
      "00576f8c",
      "READ",
      [
        "storage",
        "002a4374",
        null,
        "string"
      ]
    ],
    [
      "00576f94",
      "READ",
      [
        "storage",
        "002a437a",
        null,
        "string"
      ]
    ],
    [
      "00576fa8",
      "READ",
      [
        "storage",
        "002a67c3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00576f8c",
      "READ",
      [
        "storage",
        "002a4327",
        null,
        "string"
      ]
    ],
    [
      "00576f94",
      "READ",
      [
        "storage",
        "002a432d",
        null,
        "string"
      ]
    ],
    [
      "00576fa8",
      "READ",
      [
        "storage",
        "002a6767",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576f08.md#insn-00576f3c) · [`00576f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576f08.md#insn-00576f34) · [`00576f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576f08.md#insn-00576f48)
- 新版 `00576f7c`（命令位置の公開資料なし） · `00576f74`（命令位置の公開資料なし） · `00576f88`（命令位置の公開資料なし）

~~~diff
- 00576f3c ["INT_ADD", "register:40f0:8", ["const:576f3c:8", "const:4:8"]]
- 00576f3c ["CALL", null, ["callee:0058919c:8"]]
+ 00576f7c ["INT_ADD", "register:40f0:8", ["const:576f7c:8", "const:4:8"]]
+ 00576f7c ["CALL", null, ["callee:0058919c:8"]]
- 00576f3c bytes 88480094
+ 00576f7c bytes 88480094
- 00576f34 ["INT_ADD", "register:40f0:8", ["const:576f34:8", "const:4:8"]]
- 00576f34 ["CALL", null, ["callee:00588eac:8"]]
+ 00576f74 ["INT_ADD", "register:40f0:8", ["const:576f74:8", "const:4:8"]]
+ 00576f74 ["CALL", null, ["callee:00588eac:8"]]
- 00576f34 bytes ce470094
+ 00576f74 bytes ce470094
- 00576f48 ["COPY", "tmp:0:8", ["const:374:8"]]
- 00576f48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00576f48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00576f48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00576f88 ["COPY", "tmp:0:8", ["const:327:8"]]
+ 00576f88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00576f88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00576f88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00576f48 bytes 29d10d91
+ 00576f88 bytes 299d0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ab40ab2840b207a1d0574baf39f8466"></a>

### [`0057714c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/0057714c.md) → [`0057718c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/0057718c.md) FUN_0057718c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005778e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 1件 [`00577920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005771e8",
      "incomplete_value": true,
      "site": "005771e8",
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
                "const:701:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005771a8",
      "incomplete_value": true,
      "site": "005771a8",
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
                "const:755:8"
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
      "definition_site": "005771f0",
      "incomplete_value": true,
      "site": "005771f0",
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
      "definition_site": "005771b0",
      "incomplete_value": true,
      "site": "005771b0",
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
      "005771d0",
      "READ",
      [
        "storage",
        "002bc755",
        null,
        "string"
      ]
    ],
    [
      "005771d8",
      "READ",
      [
        "storage",
        "002bc75a",
        null,
        "string"
      ]
    ],
    [
      "005771ec",
      "READ",
      [
        "storage",
        "002a67c3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005771d0",
      "READ",
      [
        "storage",
        "002bc701",
        null,
        "string"
      ]
    ],
    [
      "005771d8",
      "READ",
      [
        "storage",
        "002bc706",
        null,
        "string"
      ]
    ],
    [
      "005771ec",
      "READ",
      [
        "storage",
        "002a6767",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/0057714c.md#insn-00577178) · [`00577180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/0057714c.md#insn-00577180) · [`0057718c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/0057714c.md#insn-0057718c)
- 新版 `005771b8`（命令位置の公開資料なし） · `005771c0`（命令位置の公開資料なし） · `005771cc`（命令位置の公開資料なし）

~~~diff
- 00577178 ["INT_ADD", "register:40f0:8", ["const:577178:8", "const:4:8"]]
- 00577178 ["CALL", null, ["callee:00588eac:8"]]
+ 005771b8 ["INT_ADD", "register:40f0:8", ["const:5771b8:8", "const:4:8"]]
+ 005771b8 ["CALL", null, ["callee:00588eac:8"]]
- 00577178 bytes 3d470094
+ 005771b8 bytes 3d470094
- 00577180 ["INT_ADD", "register:40f0:8", ["const:577180:8", "const:4:8"]]
- 00577180 ["CALL", null, ["callee:0058919c:8"]]
+ 005771c0 ["INT_ADD", "register:40f0:8", ["const:5771c0:8", "const:4:8"]]
+ 005771c0 ["CALL", null, ["callee:0058919c:8"]]
- 00577180 bytes f7470094
+ 005771c0 bytes f7470094
- 0057718c ["COPY", "tmp:0:8", ["const:755:8"]]
- 0057718c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057718c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057718c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005771cc ["COPY", "tmp:0:8", ["const:701:8"]]
+ 005771cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005771cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005771cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057718c bytes 29551d91
+ 005771cc bytes 29051c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a48175bcee4bb9984aa2da15cd0b668"></a>

### [`00577318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md) → [`00577358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577358.md) FUN_00577358

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a04.md) · 呼出先 15件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0057699c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md) [`00576f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576f08.md) [`00577080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md)
- 新版 呼出元 1件 [`00550a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a44.md) · 呼出先 15件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`005769dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md) [`00576f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576f48.md) [`005770c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005770c0.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577494",
      "incomplete_value": false,
      "site": "0057749c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577454",
      "incomplete_value": false,
      "site": "0057745c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e80:8"
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
      "definition_site": "005774ac",
      "incomplete_value": false,
      "site": "005774ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057746c",
      "incomplete_value": false,
      "site": "0057746c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00577558",
      "incomplete_value": true,
      "site": "00577558",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577518",
      "incomplete_value": true,
      "site": "00577518",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005773c0",
      "READ",
      [
        "storage",
        "002ba437",
        null,
        "string"
      ]
    ],
    [
      "0057749c",
      "DATA",
      [
        "storage",
        "00c6be80",
        null,
        "undefined *"
      ]
    ],
    [
      "005774ac",
      "DATA",
      [
        "storage",
        "00c6bb60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005773c0",
      "READ",
      [
        "storage",
        "002ba3e3",
        null,
        "string"
      ]
    ],
    [
      "0057749c",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ],
    [
      "005774ac",
      "DATA",
      [
        "storage",
        "00c6bc30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md#insn-00577464) · [`00577518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md#insn-00577518) · [`00577360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md#insn-00577360)
- 新版 `005774a4`（命令位置の公開資料なし） · `00577558`（命令位置の公開資料なし） · `005773a0`（命令位置の公開資料なし）

~~~diff
- 00577464 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 00577464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00577464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00577464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005774a4 ["COPY", "tmp:0:8", ["const:c30:8"]]
+ 005774a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005774a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005774a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00577464 bytes 08812d91
+ 005774a4 bytes 08c13091
- 00577518 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:270:8"]]
- 00577518 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00577558 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 00577558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00577518 bytes 093901f9
+ 00577558 bytes 09b901f9
- 00577360 ["INT_ADD", "register:40f0:8", ["const:577360:8", "const:4:8"]]
- 00577360 ["CALL", null, ["callee:00588eac:8"]]
+ 005773a0 ["INT_ADD", "register:40f0:8", ["const:5773a0:8", "const:4:8"]]
+ 005773a0 ["CALL", null, ["callee:00588eac:8"]]
- 00577360 bytes c3460094
+ 005773a0 bytes c3460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21849fdbd9361939b305b20ec333ae97"></a>

### [`00577678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577678.md) → [`005776b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005776b8.md) FUN_005776b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005777ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005777ec.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 1件 [`0057782c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/0057782c.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005776d8",
      "incomplete_value": false,
      "site": "005776d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577698",
      "incomplete_value": false,
      "site": "00577698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "005776d8",
      "DATA",
      [
        "storage",
        "00c6bbe8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005776d8",
      "DATA",
      [
        "storage",
        "00c6bcb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005776d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577678.md#insn-005776d8) · [`00577690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577678.md#insn-00577690) · [`00577694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577678.md#insn-00577694)
- 新版 `00577718`（命令位置の公開資料なし） · `005776d0`（命令位置の公開資料なし）

~~~diff
- 005776d8 ["INT_ADD", "register:40f0:8", ["const:5776d8:8", "const:4:8"]]
- 005776d8 ["CALL", null, ["callee:0043bb60:8"]]
+ 00577718 ["INT_ADD", "register:40f0:8", ["const:577718:8", "const:4:8"]]
+ 00577718 ["CALL", null, ["callee:0043bb60:8"]]
- 005776d8 bytes 1211fb97
+ 00577718 bytes 1211fb97
- 00577690 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 00577690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00577690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00577690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005776d0 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 005776d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005776d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005776d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00577690 bytes 08a12f91
+ 005776d0 bytes 08e13291
- 00577694 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00577694 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-401c4cc245f6b3c99ecb311dde317c94"></a>

### [`005778e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md) → [`00577920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md) FUN_00577920

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0057699c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md) [`00577080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md) [`0057714c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/0057714c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`005769dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md) [`005770c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005770c0.md) [`0057718c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/0057718c.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 95.67% / 新版 95.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577a60",
      "incomplete_value": false,
      "site": "00577a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577a20",
      "incomplete_value": false,
      "site": "00577a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00577b24",
      "incomplete_value": true,
      "site": "00577b24",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577ae4",
      "incomplete_value": true,
      "site": "00577ae4",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00577b20",
      "incomplete_value": true,
      "site": "00577b20",
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
              "LOAD"
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
      "definition_site": "00577ae0",
      "incomplete_value": true,
      "site": "00577ae0",
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
              "LOAD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057798c",
      "READ",
      [
        "storage",
        "002ba437",
        null,
        "string"
      ]
    ],
    [
      "00577a68",
      "DATA",
      [
        "storage",
        "00c6be80",
        null,
        "undefined *"
      ]
    ],
    [
      "00577a78",
      "DATA",
      [
        "storage",
        "00c6bb60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057798c",
      "READ",
      [
        "storage",
        "002ba3e3",
        null,
        "string"
      ]
    ],
    [
      "00577a68",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ],
    [
      "00577a78",
      "DATA",
      [
        "storage",
        "00c6bc30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md#insn-00577ae4) · [`0057792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md#insn-0057792c) · [`00577934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md#insn-00577934)
- 新版 `00577b24`（命令位置の公開資料なし） · `0057796c`（命令位置の公開資料なし） · `00577974`（命令位置の公開資料なし）

~~~diff
- 00577ae4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:270:8"]]
- 00577ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00577b24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 00577b24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00577ae4 bytes 093901f9
+ 00577b24 bytes 09b901f9
- 0057792c ["INT_ADD", "register:40f0:8", ["const:57792c:8", "const:4:8"]]
- 0057792c ["CALL", null, ["callee:00588eac:8"]]
+ 0057796c ["INT_ADD", "register:40f0:8", ["const:57796c:8", "const:4:8"]]
+ 0057796c ["CALL", null, ["callee:00588eac:8"]]
- 0057792c bytes 50450094
+ 0057796c bytes 50450094
- 00577934 ["INT_ADD", "register:40f0:8", ["const:577934:8", "const:4:8"]]
- 00577934 ["CALL", null, ["callee:0058919c:8"]]
+ 00577974 ["INT_ADD", "register:40f0:8", ["const:577974:8", "const:4:8"]]
+ 00577974 ["CALL", null, ["callee:0058919c:8"]]
- 00577934 bytes 0a460094
+ 00577974 bytes 0a460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5da92ebf7656072dd4818f3b8087205e"></a>

### [`00577c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md) → [`00577cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md) FUN_00577cc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 16件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0057699c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md) [`00576f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576f08.md) [`00577080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`005769dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md) [`00576f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576f48.md) [`005770c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005770c0.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 94.71% / 新版 94.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577e18",
      "incomplete_value": false,
      "site": "00577e18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577dd8",
      "incomplete_value": false,
      "site": "00577dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00577ec4",
      "incomplete_value": true,
      "site": "00577ec4",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577e84",
      "incomplete_value": true,
      "site": "00577e84",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00577ec0",
      "incomplete_value": true,
      "site": "00577ec0",
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
              "LOAD"
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
      "definition_site": "00577e80",
      "incomplete_value": true,
      "site": "00577e80",
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
              "LOAD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00577d2c",
      "READ",
      [
        "storage",
        "002ba437",
        null,
        "string"
      ]
    ],
    [
      "00577e08",
      "DATA",
      [
        "storage",
        "00c6be80",
        null,
        "undefined *"
      ]
    ],
    [
      "00577e18",
      "DATA",
      [
        "storage",
        "00c6bb60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00577d2c",
      "READ",
      [
        "storage",
        "002ba3e3",
        null,
        "string"
      ]
    ],
    [
      "00577e08",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ],
    [
      "00577e18",
      "DATA",
      [
        "storage",
        "00c6bc30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md#insn-00577d98) · [`00577e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md#insn-00577e84) · [`00577ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md#insn-00577ccc)
- 新版 `00577dd8`（命令位置の公開資料なし） · `00577ec4`（命令位置の公開資料なし） · `00577d0c`（命令位置の公開資料なし）

~~~diff
- 00577d98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00577d98 ["INT_ADD", "register:40f0:8", ["const:577d98:8", "const:4:8"]]
- 00577d98 ["CALLIND", null, ["register:0:8"]]
+ 00577dd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00577dd8 ["INT_ADD", "register:40f0:8", ["const:577dd8:8", "const:4:8"]]
+ 00577dd8 ["CALLIND", null, ["register:0:8"]]
- 00577d98 bytes 00013fd6
+ 00577dd8 bytes 00013fd6
- 00577e84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:270:8"]]
- 00577e84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00577ec4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 00577ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00577e84 bytes 093901f9
+ 00577ec4 bytes 09b901f9
- 00577ccc ["INT_ADD", "register:40f0:8", ["const:577ccc:8", "const:4:8"]]
- 00577ccc ["CALL", null, ["callee:00588eac:8"]]
+ 00577d0c ["INT_ADD", "register:40f0:8", ["const:577d0c:8", "const:4:8"]]
+ 00577d0c ["CALL", null, ["callee:00588eac:8"]]
- 00577ccc bytes 68440094
+ 00577d0c bytes 68440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecbd062a5febf42abe34b0caec06a028"></a>

### [`00578020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578020.md) → [`00578060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578060.md) FUN_00578060

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005781c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/005781c4.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`0057c220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c220.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00578204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578204.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`0057c260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c260.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.15% / 新版 95.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057808c",
      "incomplete_value": false,
      "site": "00578090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057804c",
      "incomplete_value": false,
      "site": "00578050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:c08:8"
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
      "00578090",
      "DATA",
      [
        "storage",
        "00c6bc08",
        null,
        "undefined *"
      ]
    ],
    [
      "005780b4",
      "READ",
      [
        "storage",
        "002a32bb",
        null,
        "string"
      ]
    ],
    [
      "00578154",
      "PARAM",
      [
        "storage",
        "00ca6270",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00578090",
      "DATA",
      [
        "storage",
        "00c6bcd8",
        null,
        "undefined *"
      ]
    ],
    [
      "005780b4",
      "READ",
      [
        "storage",
        "002a326e",
        null,
        "string"
      ]
    ],
    [
      "00578154",
      "PARAM",
      [
        "storage",
        "00ca6370",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057804c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578020.md#insn-0057804c) · [`00578054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578020.md#insn-00578054) · [`0057805c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578020.md#insn-0057805c)
- 新版 `0057808c`（命令位置の公開資料なし） · `00578094`（命令位置の公開資料なし） · `0057809c`（命令位置の公開資料なし）

~~~diff
- 0057804c ["COPY", "tmp:0:8", ["const:c08:8"]]
- 0057804c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057804c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057804c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057808c ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 0057808c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057808c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057808c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057804c bytes 08213091
+ 0057808c bytes 08613391
- 00578054 ["INT_ADD", "register:40f0:8", ["const:578054:8", "const:4:8"]]
- 00578054 ["CALL", null, ["callee:00588eac:8"]]
+ 00578094 ["INT_ADD", "register:40f0:8", ["const:578094:8", "const:4:8"]]
+ 00578094 ["CALL", null, ["callee:00588eac:8"]]
- 00578054 bytes 86430094
+ 00578094 bytes 86430094
- 0057805c ["INT_ADD", "register:40f0:8", ["const:57805c:8", "const:4:8"]]
- 0057805c ["CALL", null, ["callee:0058919c:8"]]
+ 0057809c ["INT_ADD", "register:40f0:8", ["const:57809c:8", "const:4:8"]]
+ 0057809c ["CALL", null, ["callee:0058919c:8"]]
- 0057805c bytes 40440094
+ 0057809c bytes 40440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37df548c1145cc523cacb64fa3688185"></a>

### [`0057835c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/0057835c.md) → [`0057839c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/0057839c.md) FUN_0057839c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578408",
      "incomplete_value": true,
      "site": "00578408",
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:85a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005783c8",
      "incomplete_value": true,
      "site": "005783c8",
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:8b6:8"
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
      "definition_site": "00578420",
      "incomplete_value": true,
      "site": "00578430",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:218:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005783e0",
      "incomplete_value": true,
      "site": "005783f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1d8:8"
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
      "definition_site": "00578434",
      "incomplete_value": true,
      "site": "00578434",
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
      "definition_site": "005783f4",
      "incomplete_value": true,
      "site": "005783f4",
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
      "005783f4",
      "READ",
      [
        "storage",
        "002ad8b6",
        null,
        "string"
      ]
    ],
    [
      "00578420",
      "READ",
      [
        "storage",
        "002b61d8",
        null,
        "string"
      ]
    ],
    [
      "00578424",
      "READ",
      [
        "storage",
        "002b61e7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005783f4",
      "READ",
      [
        "storage",
        "002ad85a",
        null,
        "string"
      ]
    ],
    [
      "00578420",
      "READ",
      [
        "storage",
        "002b6218",
        null,
        "string"
      ]
    ],
    [
      "00578424",
      "READ",
      [
        "storage",
        "002b6227",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/0057835c.md#insn-00578434) · [`00578454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/0057835c.md#insn-00578454) · [`005784ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/0057835c.md#insn-005784ac)
- 新版 `00578474`（命令位置の公開資料なし） · `00578494`（命令位置の公開資料なし） · `005784ec`（命令位置の公開資料なし）

~~~diff
- 00578434 ["INT_ADD", "register:40f0:8", ["const:578434:8", "const:4:8"]]
- 00578434 ["CALL", null, ["callee:00c57f80:8"]]
+ 00578474 ["INT_ADD", "register:40f0:8", ["const:578474:8", "const:4:8"]]
+ 00578474 ["CALL", null, ["callee:00c57f80:8"]]
- 00578434 bytes 9f7e1b94
+ 00578474 bytes c37e1b94
- 00578454 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
- 00578454 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:4"]]
+ 00578494 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 00578494 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:4"]]
- 00578454 bytes 166902b9
+ 00578494 bytes 166903b9
- 005784ac ["INT_ADD", "register:40f0:8", ["const:5784ac:8", "const:4:8"]]
- 005784ac ["CALL", null, ["callee:00c57f80:8"]]
+ 005784ec ["INT_ADD", "register:40f0:8", ["const:5784ec:8", "const:4:8"]]
+ 005784ec ["CALL", null, ["callee:00c57f80:8"]]
- 005784ac bytes 817e1b94
+ 005784ec bytes a57e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

