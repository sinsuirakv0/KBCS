# v16.0.0 → v16.0.1 · 最優先の変更候補 (23)

[一覧の目次](README.md)

<a id="compare-9af7c9332e1828cbaada6852cc0a04f1"></a>

### [`005b4a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4a58.md) → [`005b4a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4a98.md) FUN_005b4a98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b490c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b490c.md) · 呼出先 13件 [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md) [`005b8f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8f74.md) [`005b92c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b92c0.md)
- 新版 呼出元 1件 [`005b494c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b494c.md) · 呼出先 13件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md) [`005b8fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8fb4.md) [`005b9300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9300.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4aec",
      "incomplete_value": false,
      "site": "005b4af0",
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
                "const:258:8"
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
      "definition_site": "005b4aac",
      "incomplete_value": false,
      "site": "005b4ab0",
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
                "const:e58:8"
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4b1c",
      "incomplete_value": false,
      "site": "005b4b20",
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
                "const:a10:8"
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
      "definition_site": "005b4adc",
      "incomplete_value": false,
      "site": "005b4ae0",
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
                "const:610:8"
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4bac",
      "incomplete_value": false,
      "site": "005b4bac",
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
    "old": {
      "definition_site": "005b4b6c",
      "incomplete_value": false,
      "site": "005b4b6c",
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
            "const:570:8"
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
      "005b4af0",
      "DATA",
      [
        "storage",
        "00c6de68",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4b20",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4bac",
      "DATA",
      [
        "storage",
        "00c70570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4af0",
      "DATA",
      [
        "storage",
        "00c6e268",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4b20",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4bac",
      "DATA",
      [
        "storage",
        "00c70970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4a58.md#insn-005b4aa0) · [`005b4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4a58.md#insn-005b4a84) · [`005b4a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4a58.md#insn-005b4a9c)
- 新版 `005b4ae0`（命令位置の公開資料なし） · `005b4ac4`（命令位置の公開資料なし） · `005b4adc`（命令位置の公開資料なし）

~~~diff
- 005b4aa0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 005b4ae0 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005b4aa0 bytes c83500b0
+ 005b4ae0 bytes c83500d0
- 005b4a84 ["INT_ADD", "register:40f0:8", ["const:5b4a84:8", "const:4:8"]]
- 005b4a84 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b4ac4 ["INT_ADD", "register:40f0:8", ["const:5b4ac4:8", "const:4:8"]]
+ 005b4ac4 ["CALL", null, ["callee:00c57e90:8"]]
- 005b4a84 bytes 038c1a94
+ 005b4ac4 bytes f38c1a94
- 005b4a9c ["INT_ADD", "register:40f0:8", ["const:5b4a9c:8", "const:4:8"]]
- 005b4a9c ["CALL", null, ["callee:0059b908:8"]]
+ 005b4adc ["INT_ADD", "register:40f0:8", ["const:5b4adc:8", "const:4:8"]]
+ 005b4adc ["CALL", null, ["callee:0059b908:8"]]
- 005b4a9c bytes 8b9bff97
+ 005b4adc bytes 8b9bff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2ee179dbf506869cc90cd21e648d8f4"></a>

### [`005b4db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4db0.md) → [`005b4df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4df0.md) FUN_005b4df0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4e14",
      "incomplete_value": true,
      "site": "005b4e18",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "005b4dd4",
      "incomplete_value": true,
      "site": "005b4dd8",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:610:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b4e18",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4e18",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4db0.md#insn-005b4dcc) · [`005b4de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4db0.md#insn-005b4de4) · [`005b4df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4db0.md#insn-005b4df4)
- 新版 `005b4e0c`（命令位置の公開資料なし） · `005b4e24`（命令位置の公開資料なし） · `005b4e34`（命令位置の公開資料なし）

~~~diff
- 005b4dcc ["COPY", "tmp:0:8", ["const:610:8"]]
- 005b4dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4e0c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005b4e0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4e0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4e0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4dcc bytes 08411891
+ 005b4e0c bytes 08412891
- 005b4de4 ["INT_ADD", "register:40f0:8", ["const:5b4de4:8", "const:4:8"]]
- 005b4de4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b4e24 ["INT_ADD", "register:40f0:8", ["const:5b4e24:8", "const:4:8"]]
+ 005b4e24 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b4de4 bytes 338b1a94
+ 005b4e24 bytes 238c1a94
- 005b4df4 ["INT_ADD", "register:40f0:8", ["const:5b4df4:8", "const:4:8"]]
- 005b4df4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b4e34 ["INT_ADD", "register:40f0:8", ["const:5b4e34:8", "const:4:8"]]
+ 005b4e34 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b4df4 bytes 2f8b1a94
+ 005b4e34 bytes 1f8c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ec1649d2a87de2da2adc001bf2b6f2d"></a>

### [`005b4fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4fd4.md) → [`005b5014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5014.md) FUN_005b5014

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b5048",
      "incomplete_value": false,
      "site": "005b504c",
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
                "const:a10:8"
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
      "definition_site": "005b5008",
      "incomplete_value": false,
      "site": "005b500c",
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
                "const:610:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b504c",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b504c",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4fd4.md#insn-005b4ff8) · [`005b5000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4fd4.md#insn-005b5000) · [`005b5018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4fd4.md#insn-005b5018)
- 新版 `005b5038`（命令位置の公開資料なし） · `005b5040`（命令位置の公開資料なし） · `005b5058`（命令位置の公開資料なし）

~~~diff
- 005b4ff8 ["INT_ADD", "register:40f0:8", ["const:5b4ff8:8", "const:4:8"]]
- 005b4ff8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b5038 ["INT_ADD", "register:40f0:8", ["const:5b5038:8", "const:4:8"]]
+ 005b5038 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b4ff8 bytes ae8a1a94
+ 005b5038 bytes 9e8b1a94
- 005b5000 ["COPY", "tmp:0:8", ["const:610:8"]]
- 005b5000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5040 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005b5040 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5040 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5040 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5000 bytes 08411891
+ 005b5040 bytes 08412891
- 005b5018 ["INT_ADD", "register:40f0:8", ["const:5b5018:8", "const:4:8"]]
- 005b5018 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b5058 ["INT_ADD", "register:40f0:8", ["const:5b5058:8", "const:4:8"]]
+ 005b5058 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b5018 bytes a68a1a94
+ 005b5058 bytes 968b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7af432b33dacd2715dcc2fdcbca928f2"></a>

### [`005b5048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5048.md) → [`005b5088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5088.md) FUN_005b5088

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b50bc",
      "incomplete_value": false,
      "site": "005b50c0",
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
                "const:a10:8"
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
      "definition_site": "005b507c",
      "incomplete_value": false,
      "site": "005b5080",
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
                "const:610:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b50c0",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b50c0",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b506c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5048.md#insn-005b506c) · [`005b5074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5048.md#insn-005b5074) · [`005b508c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5048.md#insn-005b508c)
- 新版 `005b50ac`（命令位置の公開資料なし） · `005b50b4`（命令位置の公開資料なし） · `005b50cc`（命令位置の公開資料なし）

~~~diff
- 005b506c ["INT_ADD", "register:40f0:8", ["const:5b506c:8", "const:4:8"]]
- 005b506c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b50ac ["INT_ADD", "register:40f0:8", ["const:5b50ac:8", "const:4:8"]]
+ 005b50ac ["CALL", null, ["callee:00c57eb0:8"]]
- 005b506c bytes 918a1a94
+ 005b50ac bytes 818b1a94
- 005b5074 ["COPY", "tmp:0:8", ["const:610:8"]]
- 005b5074 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5074 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5074 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b50b4 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005b50b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b50b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b50b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5074 bytes 08411891
+ 005b50b4 bytes 08412891
- 005b508c ["INT_ADD", "register:40f0:8", ["const:5b508c:8", "const:4:8"]]
- 005b508c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b50cc ["INT_ADD", "register:40f0:8", ["const:5b50cc:8", "const:4:8"]]
+ 005b50cc ["CALL", null, ["callee:00c57eb0:8"]]
- 005b508c bytes 898a1a94
+ 005b50cc bytes 798b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-918b3f5150117b55f5beac9d67a3648a"></a>

### [`005b50bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b50bc.md) → [`005b50fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b50fc.md) FUN_005b50fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b5130",
      "incomplete_value": false,
      "site": "005b5134",
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
                "const:a10:8"
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
      "definition_site": "005b50f0",
      "incomplete_value": false,
      "site": "005b50f4",
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
                "const:610:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b5134",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5134",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b50e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b50bc.md#insn-005b50e0) · [`005b50e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b50bc.md#insn-005b50e8) · [`005b5100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b50bc.md#insn-005b5100)
- 新版 `005b5120`（命令位置の公開資料なし） · `005b5128`（命令位置の公開資料なし） · `005b5140`（命令位置の公開資料なし）

~~~diff
- 005b50e0 ["INT_ADD", "register:40f0:8", ["const:5b50e0:8", "const:4:8"]]
- 005b50e0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b5120 ["INT_ADD", "register:40f0:8", ["const:5b5120:8", "const:4:8"]]
+ 005b5120 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b50e0 bytes 748a1a94
+ 005b5120 bytes 648b1a94
- 005b50e8 ["COPY", "tmp:0:8", ["const:610:8"]]
- 005b50e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b50e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b50e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5128 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005b5128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b50e8 bytes 08411891
+ 005b5128 bytes 08412891
- 005b5100 ["INT_ADD", "register:40f0:8", ["const:5b5100:8", "const:4:8"]]
- 005b5100 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b5140 ["INT_ADD", "register:40f0:8", ["const:5b5140:8", "const:4:8"]]
+ 005b5140 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b5100 bytes 6c8a1a94
+ 005b5140 bytes 5c8b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29f48fccf7d17d9361af393905558ae3"></a>

### [`005b5130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5130.md) → [`005b5170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5170.md) FUN_005b5170

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b5194",
      "incomplete_value": false,
      "site": "005b5198",
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
                "const:a10:8"
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
      "definition_site": "005b5154",
      "incomplete_value": false,
      "site": "005b5158",
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
                "const:610:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b5198",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5198",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b514c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5130.md#insn-005b514c) · [`005b5164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5130.md#insn-005b5164) · [`005b5174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5130.md#insn-005b5174)
- 新版 `005b518c`（命令位置の公開資料なし） · `005b51a4`（命令位置の公開資料なし） · `005b51b4`（命令位置の公開資料なし）

~~~diff
- 005b514c ["COPY", "tmp:0:8", ["const:610:8"]]
- 005b514c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b514c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b514c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b518c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005b518c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b518c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b518c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b514c bytes 08411891
+ 005b518c bytes 08412891
- 005b5164 ["INT_ADD", "register:40f0:8", ["const:5b5164:8", "const:4:8"]]
- 005b5164 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b51a4 ["INT_ADD", "register:40f0:8", ["const:5b51a4:8", "const:4:8"]]
+ 005b51a4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b5164 bytes 538a1a94
+ 005b51a4 bytes 438b1a94
- 005b5174 ["INT_ADD", "register:40f0:8", ["const:5b5174:8", "const:4:8"]]
- 005b5174 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b51b4 ["INT_ADD", "register:40f0:8", ["const:5b51b4:8", "const:4:8"]]
+ 005b51b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b5174 bytes 4f8a1a94
+ 005b51b4 bytes 3f8b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22f2c4ebf298113d1208d29e7c2f090f"></a>

### [`005b5194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5194.md) → [`005b51d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b51d4.md) FUN_005b51d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "005b51d8",
      "incomplete_value": false,
      "site": "005b51dc",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5198",
      "incomplete_value": false,
      "site": "005b519c",
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
            "const:260:8"
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
      "005b51dc",
      "DATA",
      [
        "storage",
        "00c6f260",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b51dc",
      "DATA",
      [
        "storage",
        "00c6f660",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5194.md#insn-005b5198)
- 新版 `005b51d8`（命令位置の公開資料なし）

~~~diff
- 005b5198 ["COPY", "tmp:0:8", ["const:260:8"]]
- 005b5198 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5198 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5198 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b51d8 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 005b51d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b51d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b51d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5198 bytes 08810991
+ 005b51d8 bytes 08811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66738cdf5f90252045371534973eb4be"></a>

### [`005b51a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51a4.md) → [`005b51e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b51e4.md) FUN_005b51e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b51f4",
      "incomplete_value": false,
      "site": "005b51fc",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b51b4",
      "incomplete_value": false,
      "site": "005b51bc",
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
            "const:260:8"
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
      "005b51fc",
      "DATA",
      [
        "storage",
        "00c6f260",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b51fc",
      "DATA",
      [
        "storage",
        "00c6f660",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b51b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51a4.md#insn-005b51b4) · [`005b51c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51a4.md#insn-005b51c0)
- 新版 `005b51f4`（命令位置の公開資料なし） · `005b5200`（命令位置の公開資料なし）

~~~diff
- 005b51b4 ["COPY", "tmp:0:8", ["const:260:8"]]
- 005b51b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b51b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b51b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b51f4 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 005b51f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b51f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b51f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b51b4 bytes 08810991
+ 005b51f4 bytes 08811991
- 005b51c0 ["INT_ADD", "register:40f0:8", ["const:5b51c0:8", "const:4:8"]]
- 005b51c0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005b5200 ["INT_ADD", "register:40f0:8", ["const:5b5200:8", "const:4:8"]]
+ 005b5200 ["CALL", null, ["callee:00c57ea0:8"]]
- 005b51c0 bytes 388a1a94
+ 005b5200 bytes 288b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-925717e9014d781f4cf78de0a71d111b"></a>

### [`005b52c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b52c4.md) → [`005b5304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5304.md) FUN_005b5304

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b5328",
      "incomplete_value": false,
      "site": "005b5328",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b52e8",
      "incomplete_value": false,
      "site": "005b52e8",
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
      "005b5328",
      "DATA",
      [
        "storage",
        "00c6f2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5328",
      "DATA",
      [
        "storage",
        "00c6f6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b52d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b52c4.md#insn-005b52d8) · [`005b52e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b52c4.md#insn-005b52e4)
- 新版 `005b5318`（命令位置の公開資料なし） · `005b5324`（命令位置の公開資料なし）

~~~diff
- 005b52d8 ["INT_ADD", "register:40f0:8", ["const:5b52d8:8", "const:4:8"]]
- 005b52d8 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b5318 ["INT_ADD", "register:40f0:8", ["const:5b5318:8", "const:4:8"]]
+ 005b5318 ["CALL", null, ["callee:00c57e90:8"]]
- 005b52d8 bytes ee891a94
+ 005b5318 bytes de8a1a94
- 005b52e4 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 005b52e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b52e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b52e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5324 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 005b5324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b52e4 bytes 08c10a91
+ 005b5324 bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef31bebaf9b6bb043001079efe0211de"></a>

### [`005b5348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5348.md) → [`005b5388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5388.md) FUN_005b5388

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b53ac",
      "incomplete_value": true,
      "site": "005b53ac",
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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b536c",
      "incomplete_value": true,
      "site": "005b536c",
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
            "const:340:8"
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
      "005b53ac",
      "DATA",
      [
        "storage",
        "00c6f340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b53ac",
      "DATA",
      [
        "storage",
        "00c6f740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b535c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5348.md#insn-005b535c) · [`005b5368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5348.md#insn-005b5368)
- 新版 `005b539c`（命令位置の公開資料なし） · `005b53a8`（命令位置の公開資料なし）

~~~diff
- 005b535c ["INT_ADD", "register:40f0:8", ["const:5b535c:8", "const:4:8"]]
- 005b535c ["CALL", null, ["callee:00c57e90:8"]]
+ 005b539c ["INT_ADD", "register:40f0:8", ["const:5b539c:8", "const:4:8"]]
+ 005b539c ["CALL", null, ["callee:00c57e90:8"]]
- 005b535c bytes cd891a94
+ 005b539c bytes bd8a1a94
- 005b5368 ["COPY", "tmp:0:8", ["const:340:8"]]
- 005b5368 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5368 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5368 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b53a8 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 005b53a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b53a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b53a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5368 bytes 08010d91
+ 005b53a8 bytes 08011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc2713393cf1ea15f06230d781a7f803"></a>

### [`005b537c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b537c.md) → [`005b53bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b53bc.md) FUN_005b53bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b53c8",
      "incomplete_value": false,
      "site": "005b53c8",
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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5388",
      "incomplete_value": false,
      "site": "005b5388",
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
            "const:340:8"
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
      "005b53c8",
      "DATA",
      [
        "storage",
        "00c6f340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b53c8",
      "DATA",
      [
        "storage",
        "00c6f740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b537c.md#insn-005b5384)
- 新版 `005b53c4`（命令位置の公開資料なし）

~~~diff
- 005b5384 ["COPY", "tmp:0:8", ["const:340:8"]]
- 005b5384 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5384 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5384 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b53c4 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 005b53c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b53c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b53c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5384 bytes 29010d91
+ 005b53c4 bytes 29011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e173cba54829d6c53db800fcfd35f298"></a>

### [`005b5414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5414.md) → [`005b5454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5454.md) FUN_005b5454

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b545c",
      "incomplete_value": false,
      "site": "005b5460",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b541c",
      "incomplete_value": false,
      "site": "005b5420",
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
            "const:3d0:8"
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
      "005b5460",
      "DATA",
      [
        "storage",
        "00c6f3d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5460",
      "DATA",
      [
        "storage",
        "00c6f7d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b541c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5414.md#insn-005b541c) · [`005b5440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5414.md#insn-005b5440)
- 新版 `005b545c`（命令位置の公開資料なし） · `005b5480`（命令位置の公開資料なし）

~~~diff
- 005b541c ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 005b541c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b541c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b541c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b545c ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 005b545c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b545c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b545c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b541c bytes 29410f91
+ 005b545c bytes 29411f91
- 005b5440 ["INT_ADD", "register:40f0:8", ["const:5b5440:8", "const:4:8"]]
- 005b5440 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b5480 ["INT_ADD", "register:40f0:8", ["const:5b5480:8", "const:4:8"]]
+ 005b5480 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b5440 bytes 9c891a94
+ 005b5480 bytes 8c8a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fbd3cf258e76bb476ab4f38a3dcbf47"></a>

### [`005b54d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b54d0.md) → [`005b5510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5510.md) FUN_005b5510

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

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
      "definition_site": "005b551c",
      "incomplete_value": false,
      "site": "005b551c",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b54dc",
      "incomplete_value": false,
      "site": "005b54dc",
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
            "const:3d0:8"
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
      "005b551c",
      "DATA",
      [
        "storage",
        "00c6f3d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b551c",
      "DATA",
      [
        "storage",
        "00c6f7d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b54d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b54d0.md#insn-005b54d8)
- 新版 `005b5518`（命令位置の公開資料なし）

~~~diff
- 005b54d8 ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 005b54d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b54d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b54d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5518 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 005b5518 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5518 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5518 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b54d8 bytes 29410f91
+ 005b5518 bytes 29411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-810dc7d2fb639159291e6c422766fec3"></a>

### [`005b5594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5594.md) → [`005b55d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b55d4.md) FUN_005b55d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b55f8",
      "incomplete_value": false,
      "site": "005b55f8",
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
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b55b8",
      "incomplete_value": false,
      "site": "005b55b8",
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
            "const:460:8"
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
      "005b55f8",
      "DATA",
      [
        "storage",
        "00c6f460",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b55f8",
      "DATA",
      [
        "storage",
        "00c6f860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b55a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5594.md#insn-005b55a8) · [`005b55b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5594.md#insn-005b55b4)
- 新版 `005b55e8`（命令位置の公開資料なし） · `005b55f4`（命令位置の公開資料なし）

~~~diff
- 005b55a8 ["INT_ADD", "register:40f0:8", ["const:5b55a8:8", "const:4:8"]]
- 005b55a8 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b55e8 ["INT_ADD", "register:40f0:8", ["const:5b55e8:8", "const:4:8"]]
+ 005b55e8 ["CALL", null, ["callee:00c57e90:8"]]
- 005b55a8 bytes 3a891a94
+ 005b55e8 bytes 2a8a1a94
- 005b55b4 ["COPY", "tmp:0:8", ["const:460:8"]]
- 005b55b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b55b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b55b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b55f4 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 005b55f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b55f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b55f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b55b4 bytes 08811191
+ 005b55f4 bytes 08812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-284a8fd8a0968f83d517827687396953"></a>

### [`005b55c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b55c8.md) → [`005b5608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5608.md) FUN_005b5608

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5614",
      "incomplete_value": false,
      "site": "005b5614",
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
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b55d4",
      "incomplete_value": false,
      "site": "005b55d4",
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
            "const:460:8"
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
      "005b5614",
      "DATA",
      [
        "storage",
        "00c6f460",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5614",
      "DATA",
      [
        "storage",
        "00c6f860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b55d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b55c8.md#insn-005b55d0)
- 新版 `005b5610`（命令位置の公開資料なし）

~~~diff
- 005b55d0 ["COPY", "tmp:0:8", ["const:460:8"]]
- 005b55d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b55d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b55d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5610 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 005b5610 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5610 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5610 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b55d0 bytes 29811191
+ 005b5610 bytes 29812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-880b1ef14ac5f1cfcfb8ac1588564301"></a>

### [`005b5680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5680.md) → [`005b56c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b56c0.md) FUN_005b56c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b56cc",
      "incomplete_value": false,
      "site": "005b56cc",
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
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b568c",
      "incomplete_value": false,
      "site": "005b568c",
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
            "const:4e0:8"
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
      "005b56cc",
      "DATA",
      [
        "storage",
        "00c6f4e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b56cc",
      "DATA",
      [
        "storage",
        "00c6f8e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5680.md#insn-005b5688)
- 新版 `005b56c8`（命令位置の公開資料なし）

~~~diff
- 005b5688 ["COPY", "tmp:0:8", ["const:4e0:8"]]
- 005b5688 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5688 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5688 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b56c8 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 005b56c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b56c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b56c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5688 bytes 29811391
+ 005b56c8 bytes 29812391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb2c533a4e962ab7accc5e9ac71d199d"></a>

### [`005b56d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b56d0.md) → [`005b5710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5710.md) FUN_005b5710

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b5734",
      "incomplete_value": false,
      "site": "005b5734",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b56f4",
      "incomplete_value": false,
      "site": "005b56f4",
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
      "005b5734",
      "DATA",
      [
        "storage",
        "00c6f560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5734",
      "DATA",
      [
        "storage",
        "00c6f960",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b56e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b56d0.md#insn-005b56e4) · [`005b56f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b56d0.md#insn-005b56f0)
- 新版 `005b5724`（命令位置の公開資料なし） · `005b5730`（命令位置の公開資料なし）

~~~diff
- 005b56e4 ["INT_ADD", "register:40f0:8", ["const:5b56e4:8", "const:4:8"]]
- 005b56e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b5724 ["INT_ADD", "register:40f0:8", ["const:5b5724:8", "const:4:8"]]
+ 005b5724 ["CALL", null, ["callee:00c57e90:8"]]
- 005b56e4 bytes eb881a94
+ 005b5724 bytes db891a94
- 005b56f0 ["COPY", "tmp:0:8", ["const:560:8"]]
- 005b56f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b56f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b56f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5730 ["COPY", "tmp:0:8", ["const:960:8"]]
+ 005b5730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b56f0 bytes 08811591
+ 005b5730 bytes 08812591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8f64dcf828dff92b5a0fac1b82977e6"></a>

### [`005b5704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5704.md) → [`005b5744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5744.md) FUN_005b5744

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5750",
      "incomplete_value": false,
      "site": "005b5750",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5710",
      "incomplete_value": false,
      "site": "005b5710",
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
      "005b5750",
      "DATA",
      [
        "storage",
        "00c6f560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5750",
      "DATA",
      [
        "storage",
        "00c6f960",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b570c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5704.md#insn-005b570c)
- 新版 `005b574c`（命令位置の公開資料なし）

~~~diff
- 005b570c ["COPY", "tmp:0:8", ["const:560:8"]]
- 005b570c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b570c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b570c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b574c ["COPY", "tmp:0:8", ["const:960:8"]]
+ 005b574c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b574c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b574c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b570c bytes 29811591
+ 005b574c bytes 29812591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-031b569d0a0dd31f7dfde0ec1a33379e"></a>

### [`005b57b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b57b8.md) → [`005b57f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b57f8.md) FUN_005b57f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5804",
      "incomplete_value": false,
      "site": "005b5804",
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
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b57c4",
      "incomplete_value": false,
      "site": "005b57c4",
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
            "const:5e0:8"
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
      "005b5804",
      "DATA",
      [
        "storage",
        "00c6f5e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5804",
      "DATA",
      [
        "storage",
        "00c6f9e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b57c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b57b8.md#insn-005b57c0)
- 新版 `005b5800`（命令位置の公開資料なし）

~~~diff
- 005b57c0 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 005b57c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b57c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b57c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5800 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 005b5800 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5800 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5800 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b57c0 bytes 29811791
+ 005b5800 bytes 29812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afaf122d464f1304aec3b41bdc215975"></a>

### [`005b57d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b57d4.md) → [`005b5814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5814.md) FUN_005b5814

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 11件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`005b5a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5a34.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`005b5a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5a74.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.60% / 新版 95.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b5890",
      "incomplete_value": false,
      "site": "005b5898",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5850",
      "incomplete_value": false,
      "site": "005b5858",
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
            "const:650:8"
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
      "site": "005b5840",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b5800",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "005b5840",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "005b5898",
      "DATA",
      [
        "storage",
        "00c6f650",
        null,
        "pointer"
      ]
    ],
    [
      "005b5930",
      "READ",
      [
        "storage",
        "00c6f660",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5840",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "005b5898",
      "DATA",
      [
        "storage",
        "00c6fa50",
        null,
        "pointer"
      ]
    ],
    [
      "005b5930",
      "READ",
      [
        "storage",
        "00c6fa60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b57d4.md#insn-005b5800) · [`005b5804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b57d4.md#insn-005b5804) · [`005b5848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b57d4.md#insn-005b5848)
- 新版 `005b5840`（命令位置の公開資料なし） · `005b5844`（命令位置の公開資料なし） · `005b5888`（命令位置の公開資料なし）

~~~diff
- 005b5800 ["INT_ADD", "register:40f0:8", ["const:5b5800:8", "const:4:8"]]
- 005b5800 ["CALL", null, ["ram:48ccb8:8"]]
+ 005b5840 ["INT_ADD", "register:40f0:8", ["const:5b5840:8", "const:4:8"]]
+ 005b5840 ["CALL", null, ["ram:48ccf8:8"]]
- 005b5800 bytes 2e5dfb97
+ 005b5840 bytes 2e5dfb97
- 005b5804 ["INT_ADD", "register:40f0:8", ["const:5b5804:8", "const:4:8"]]
- 005b5804 ["CALL", null, ["callee:0048e7e0:8"]]
+ 005b5844 ["INT_ADD", "register:40f0:8", ["const:5b5844:8", "const:4:8"]]
+ 005b5844 ["CALL", null, ["callee:0048e7e0:8"]]
- 005b5804 bytes e763fb97
+ 005b5844 bytes e763fb97
- 005b5848 ["INT_ADD", "register:40f0:8", ["const:5b5848:8", "const:4:8"]]
- 005b5848 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b5888 ["INT_ADD", "register:40f0:8", ["const:5b5888:8", "const:4:8"]]
+ 005b5888 ["CALL", null, ["callee:00c57e90:8"]]
- 005b5848 bytes 92881a94
+ 005b5888 bytes 82891a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaed6567e5e1ed8a5538ee6d81743363"></a>

### [`005b59f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b59f4.md) → [`005b5a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5a34.md) FUN_005b5a34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "005b5a38",
      "incomplete_value": false,
      "site": "005b5a3c",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b59f8",
      "incomplete_value": false,
      "site": "005b59fc",
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
            "const:650:8"
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
      "005b5a3c",
      "DATA",
      [
        "storage",
        "00c6f650",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b5a3c",
      "DATA",
      [
        "storage",
        "00c6fa50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b59f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b59f4.md#insn-005b59f8)
- 新版 `005b5a38`（命令位置の公開資料なし）

~~~diff
- 005b59f8 ["COPY", "tmp:0:8", ["const:650:8"]]
- 005b59f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b59f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b59f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5a38 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 005b5a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b59f8 bytes 08411991
+ 005b5a38 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19adc1fe61fee403b277b5449658d7b2"></a>

### [`005b5a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5a04.md) → [`005b5a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5a44.md) FUN_005b5a44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b5a54",
      "incomplete_value": false,
      "site": "005b5a5c",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5a14",
      "incomplete_value": false,
      "site": "005b5a1c",
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
            "const:650:8"
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
      "005b5a5c",
      "DATA",
      [
        "storage",
        "00c6f650",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b5a5c",
      "DATA",
      [
        "storage",
        "00c6fa50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5a04.md#insn-005b5a14) · [`005b5a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5a04.md#insn-005b5a20)
- 新版 `005b5a54`（命令位置の公開資料なし） · `005b5a60`（命令位置の公開資料なし）

~~~diff
- 005b5a14 ["COPY", "tmp:0:8", ["const:650:8"]]
- 005b5a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5a54 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 005b5a54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5a54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5a54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5a14 bytes 08411991
+ 005b5a54 bytes 08412991
- 005b5a20 ["INT_ADD", "register:40f0:8", ["const:5b5a20:8", "const:4:8"]]
- 005b5a20 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005b5a60 ["INT_ADD", "register:40f0:8", ["const:5b5a60:8", "const:4:8"]]
+ 005b5a60 ["CALL", null, ["callee:00c57ea0:8"]]
- 005b5a20 bytes 20881a94
+ 005b5a60 bytes 10891a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c88b1f893b2bcb2decafbee0a1589165"></a>

### [`005b5a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5a50.md) → [`005b5a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5a90.md) FUN_005b5a90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b5ab4",
      "incomplete_value": false,
      "site": "005b5ab4",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5a74",
      "incomplete_value": false,
      "site": "005b5a74",
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
      "005b5ab4",
      "DATA",
      [
        "storage",
        "00c6f6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5ab4",
      "DATA",
      [
        "storage",
        "00c6fab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5a50.md#insn-005b5a64) · [`005b5a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5a50.md#insn-005b5a70)
- 新版 `005b5aa4`（命令位置の公開資料なし） · `005b5ab0`（命令位置の公開資料なし）

~~~diff
- 005b5a64 ["INT_ADD", "register:40f0:8", ["const:5b5a64:8", "const:4:8"]]
- 005b5a64 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b5aa4 ["INT_ADD", "register:40f0:8", ["const:5b5aa4:8", "const:4:8"]]
+ 005b5aa4 ["CALL", null, ["callee:00c57e90:8"]]
- 005b5a64 bytes 0b881a94
+ 005b5aa4 bytes fb881a94
- 005b5a70 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 005b5a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5ab0 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 005b5ab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5ab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5ab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5a70 bytes 08c11a91
+ 005b5ab0 bytes 08c12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4158fa17cb18b0e21ea4c439a63d3730"></a>

### [`005b5aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5aa0.md) → [`005b5ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ae0.md) FUN_005b5ae0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`005b22b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b22b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`005b22f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22f0.md)

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
      "site": "005b5afc",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b5abc",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "005b5afc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "005b5afc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5aa0.md#insn-005b5abc) · [`005b5ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5aa0.md#insn-005b5ac0)
- 新版 `005b5afc`（命令位置の公開資料なし） · `005b5b00`（命令位置の公開資料なし）

~~~diff
- 005b5abc ["INT_ADD", "register:40f0:8", ["const:5b5abc:8", "const:4:8"]]
- 005b5abc ["CALL", null, ["ram:48ccb8:8"]]
+ 005b5afc ["INT_ADD", "register:40f0:8", ["const:5b5afc:8", "const:4:8"]]
+ 005b5afc ["CALL", null, ["ram:48ccf8:8"]]
- 005b5abc bytes 7f5cfb97
+ 005b5afc bytes 7f5cfb97
- 005b5ac0 ["INT_ADD", "register:40f0:8", ["const:5b5ac0:8", "const:4:8"]]
- 005b5ac0 ["CALL", null, ["callee:0048e7e0:8"]]
+ 005b5b00 ["INT_ADD", "register:40f0:8", ["const:5b5b00:8", "const:4:8"]]
+ 005b5b00 ["CALL", null, ["callee:0048e7e0:8"]]
- 005b5ac0 bytes 3863fb97
+ 005b5b00 bytes 3863fb97
~~~


<a id="compare-6d6676baf3db620cf77cb830594bb32a"></a>

### [`005b5b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b14.md) → [`005b5b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5b54.md) FUN_005b5b54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b5b74",
      "incomplete_value": false,
      "site": "005b5b78",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5b34",
      "incomplete_value": false,
      "site": "005b5b38",
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
            "const:740:8"
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
      "005b5b78",
      "DATA",
      [
        "storage",
        "00c6f740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5b78",
      "DATA",
      [
        "storage",
        "00c6fb40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b14.md#insn-005b5b28) · [`005b5b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b14.md#insn-005b5b34)
- 新版 `005b5b68`（命令位置の公開資料なし） · `005b5b74`（命令位置の公開資料なし）

~~~diff
- 005b5b28 ["INT_ADD", "register:40f0:8", ["const:5b5b28:8", "const:4:8"]]
- 005b5b28 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b5b68 ["INT_ADD", "register:40f0:8", ["const:5b5b68:8", "const:4:8"]]
+ 005b5b68 ["CALL", null, ["callee:00c57e90:8"]]
- 005b5b28 bytes da871a94
+ 005b5b68 bytes ca881a94
- 005b5b34 ["COPY", "tmp:0:8", ["const:740:8"]]
- 005b5b34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5b34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5b34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5b74 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 005b5b74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5b74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5b74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5b34 bytes 08011d91
+ 005b5b74 bytes 08012d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58f9ea86fb1366f9558fe9bc224b3da3"></a>

### [`005b5b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b4c.md) → [`005b5b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5b8c.md) FUN_005b5b8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5b90",
      "incomplete_value": false,
      "site": "005b5b94",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5b50",
      "incomplete_value": false,
      "site": "005b5b54",
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
            "const:740:8"
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
      "005b5b94",
      "DATA",
      [
        "storage",
        "00c6f740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5b94",
      "DATA",
      [
        "storage",
        "00c6fb40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b4c.md#insn-005b5b50)
- 新版 `005b5b90`（命令位置の公開資料なし）

~~~diff
- 005b5b50 ["COPY", "tmp:0:8", ["const:740:8"]]
- 005b5b50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5b50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5b50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5b90 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 005b5b90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5b90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5b90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5b50 bytes 08011d91
+ 005b5b90 bytes 08012d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d7a32c26f678979831ae473e4eb9ea2"></a>

### [`005b5bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5bbc.md) → [`005b5bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5bfc.md) FUN_005b5bfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b5c20",
      "incomplete_value": false,
      "site": "005b5c20",
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
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5be0",
      "incomplete_value": false,
      "site": "005b5be0",
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
            "const:7c0:8"
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
      "005b5c20",
      "DATA",
      [
        "storage",
        "00c6f7c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5c20",
      "DATA",
      [
        "storage",
        "00c6fbc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5bbc.md#insn-005b5bd0) · [`005b5bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5bbc.md#insn-005b5bdc)
- 新版 `005b5c10`（命令位置の公開資料なし） · `005b5c1c`（命令位置の公開資料なし）

~~~diff
- 005b5bd0 ["INT_ADD", "register:40f0:8", ["const:5b5bd0:8", "const:4:8"]]
- 005b5bd0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b5c10 ["INT_ADD", "register:40f0:8", ["const:5b5c10:8", "const:4:8"]]
+ 005b5c10 ["CALL", null, ["callee:00c57e90:8"]]
- 005b5bd0 bytes b0871a94
+ 005b5c10 bytes a0881a94
- 005b5bdc ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 005b5bdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5bdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5bdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5c1c ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 005b5c1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5c1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5c1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5bdc bytes 08011f91
+ 005b5c1c bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ee5bface8e33333ac9db569e0fc97ca"></a>

### [`005b5bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5bf0.md) → [`005b5c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5c30.md) FUN_005b5c30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5c3c",
      "incomplete_value": false,
      "site": "005b5c3c",
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
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5bfc",
      "incomplete_value": false,
      "site": "005b5bfc",
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
            "const:7c0:8"
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
      "005b5c3c",
      "DATA",
      [
        "storage",
        "00c6f7c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5c3c",
      "DATA",
      [
        "storage",
        "00c6fbc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5bf0.md#insn-005b5bf8)
- 新版 `005b5c38`（命令位置の公開資料なし）

~~~diff
- 005b5bf8 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 005b5bf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5bf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5bf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5c38 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 005b5c38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5c38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5c38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5bf8 bytes 29011f91
+ 005b5c38 bytes 29012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acb0e99f2f89bea8fabfd582d99a38f2"></a>

### [`005b5c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c50.md) → [`005b5c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5c90.md) FUN_005b5c90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b5cb4",
      "incomplete_value": false,
      "site": "005b5cb4",
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
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5c74",
      "incomplete_value": false,
      "site": "005b5c74",
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
            "const:840:8"
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
      "005b5cb4",
      "DATA",
      [
        "storage",
        "00c6f840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5cb4",
      "DATA",
      [
        "storage",
        "00c6fc40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c50.md#insn-005b5c64) · [`005b5c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c50.md#insn-005b5c70)
- 新版 `005b5ca4`（命令位置の公開資料なし） · `005b5cb0`（命令位置の公開資料なし）

~~~diff
- 005b5c64 ["INT_ADD", "register:40f0:8", ["const:5b5c64:8", "const:4:8"]]
- 005b5c64 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b5ca4 ["INT_ADD", "register:40f0:8", ["const:5b5ca4:8", "const:4:8"]]
+ 005b5ca4 ["CALL", null, ["callee:00c57e90:8"]]
- 005b5c64 bytes 8b871a94
+ 005b5ca4 bytes 7b881a94
- 005b5c70 ["COPY", "tmp:0:8", ["const:840:8"]]
- 005b5c70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5c70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5c70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5cb0 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 005b5cb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5cb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5cb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5c70 bytes 08012191
+ 005b5cb0 bytes 08013191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-507938b5fa1ba27c789319ea4239a725"></a>

### [`005b5c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c84.md) → [`005b5cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5cc4.md) FUN_005b5cc4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5cd0",
      "incomplete_value": false,
      "site": "005b5cd0",
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
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5c90",
      "incomplete_value": false,
      "site": "005b5c90",
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
            "const:840:8"
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
      "005b5cd0",
      "DATA",
      [
        "storage",
        "00c6f840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5cd0",
      "DATA",
      [
        "storage",
        "00c6fc40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c84.md#insn-005b5c8c)
- 新版 `005b5ccc`（命令位置の公開資料なし）

~~~diff
- 005b5c8c ["COPY", "tmp:0:8", ["const:840:8"]]
- 005b5c8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5c8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5c8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5ccc ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 005b5ccc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5ccc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5ccc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5c8c bytes 29012191
+ 005b5ccc bytes 29013191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d00e5a0bcefdad8b6289274d3ad68ca1"></a>

### [`005b5d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5d78.md) → [`005b5db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5db8.md) FUN_005b5db8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b5ddc",
      "incomplete_value": false,
      "site": "005b5ddc",
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
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5d9c",
      "incomplete_value": false,
      "site": "005b5d9c",
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
            "const:8c0:8"
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
      "005b5ddc",
      "DATA",
      [
        "storage",
        "00c6f8c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5ddc",
      "DATA",
      [
        "storage",
        "00c6fcc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5d78.md#insn-005b5d8c) · [`005b5d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5d78.md#insn-005b5d98)
- 新版 `005b5dcc`（命令位置の公開資料なし） · `005b5dd8`（命令位置の公開資料なし）

~~~diff
- 005b5d8c ["INT_ADD", "register:40f0:8", ["const:5b5d8c:8", "const:4:8"]]
- 005b5d8c ["CALL", null, ["callee:00c57e90:8"]]
+ 005b5dcc ["INT_ADD", "register:40f0:8", ["const:5b5dcc:8", "const:4:8"]]
+ 005b5dcc ["CALL", null, ["callee:00c57e90:8"]]
- 005b5d8c bytes 41871a94
+ 005b5dcc bytes 31881a94
- 005b5d98 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 005b5d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5dd8 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 005b5dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5d98 bytes 08012391
+ 005b5dd8 bytes 08013391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a11c3dd6d10329ae5d76eb730332ac50"></a>

### [`005b5dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5dac.md) → [`005b5dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5dec.md) FUN_005b5dec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5df8",
      "incomplete_value": false,
      "site": "005b5df8",
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
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5db8",
      "incomplete_value": false,
      "site": "005b5db8",
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
            "const:8c0:8"
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
      "005b5df8",
      "DATA",
      [
        "storage",
        "00c6f8c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5df8",
      "DATA",
      [
        "storage",
        "00c6fcc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5dac.md#insn-005b5db4)
- 新版 `005b5df4`（命令位置の公開資料なし）

~~~diff
- 005b5db4 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 005b5db4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5db4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5db4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5df4 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 005b5df4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5df4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5df4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5db4 bytes 29012391
+ 005b5df4 bytes 29013391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2c554587f0151d3cf6c9e3b4cfc6171"></a>

### [`005b5e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e10.md) → [`005b5e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5e50.md) FUN_005b5e50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b5e70",
      "incomplete_value": false,
      "site": "005b5e74",
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
            "const:d40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5e30",
      "incomplete_value": false,
      "site": "005b5e34",
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
      "005b5e74",
      "DATA",
      [
        "storage",
        "00c6f940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5e74",
      "DATA",
      [
        "storage",
        "00c6fd40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e10.md#insn-005b5e24) · [`005b5e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e10.md#insn-005b5e30)
- 新版 `005b5e64`（命令位置の公開資料なし） · `005b5e70`（命令位置の公開資料なし）

~~~diff
- 005b5e24 ["INT_ADD", "register:40f0:8", ["const:5b5e24:8", "const:4:8"]]
- 005b5e24 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b5e64 ["INT_ADD", "register:40f0:8", ["const:5b5e64:8", "const:4:8"]]
+ 005b5e64 ["CALL", null, ["callee:00c57e90:8"]]
- 005b5e24 bytes 1b871a94
+ 005b5e64 bytes 0b881a94
- 005b5e30 ["COPY", "tmp:0:8", ["const:940:8"]]
- 005b5e30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5e30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5e30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5e70 ["COPY", "tmp:0:8", ["const:d40:8"]]
+ 005b5e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5e30 bytes 08012591
+ 005b5e70 bytes 08013591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a62cd973d6e5586dbba2a5af039d446e"></a>

### [`005b5e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e48.md) → [`005b5e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5e88.md) FUN_005b5e88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5e8c",
      "incomplete_value": false,
      "site": "005b5e90",
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
            "const:d40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5e4c",
      "incomplete_value": false,
      "site": "005b5e50",
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
      "005b5e90",
      "DATA",
      [
        "storage",
        "00c6f940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5e90",
      "DATA",
      [
        "storage",
        "00c6fd40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e48.md#insn-005b5e4c)
- 新版 `005b5e8c`（命令位置の公開資料なし）

~~~diff
- 005b5e4c ["COPY", "tmp:0:8", ["const:940:8"]]
- 005b5e4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5e4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5e4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5e8c ["COPY", "tmp:0:8", ["const:d40:8"]]
+ 005b5e8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5e8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5e8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5e4c bytes 08012591
+ 005b5e8c bytes 08013591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33ec3765f5070e5ccf8071ffc3a7514d"></a>

### [`005b5f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5f64.md) → [`005b5fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5fa4.md) FUN_005b5fa4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b5fc4",
      "incomplete_value": false,
      "site": "005b5fc8",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5f84",
      "incomplete_value": false,
      "site": "005b5f88",
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
            "const:9d0:8"
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
      "005b5fc8",
      "DATA",
      [
        "storage",
        "00c6f9d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5fc8",
      "DATA",
      [
        "storage",
        "00c6fdd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5f64.md#insn-005b5f78) · [`005b5f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5f64.md#insn-005b5f84)
- 新版 `005b5fb8`（命令位置の公開資料なし） · `005b5fc4`（命令位置の公開資料なし）

~~~diff
- 005b5f78 ["INT_ADD", "register:40f0:8", ["const:5b5f78:8", "const:4:8"]]
- 005b5f78 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b5fb8 ["INT_ADD", "register:40f0:8", ["const:5b5fb8:8", "const:4:8"]]
+ 005b5fb8 ["CALL", null, ["callee:00c57e90:8"]]
- 005b5f78 bytes c6861a94
+ 005b5fb8 bytes b6871a94
- 005b5f84 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 005b5f84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5f84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5f84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5fc4 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 005b5fc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5fc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5fc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5f84 bytes 08412791
+ 005b5fc4 bytes 08413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d886b4c37f9ac1912dd8bea37d5eae49"></a>

### [`005b60cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b60cc.md) → [`005b610c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b610c.md) FUN_005b610c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b612c",
      "incomplete_value": false,
      "site": "005b6130",
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
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b60ec",
      "incomplete_value": false,
      "site": "005b60f0",
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
            "const:a60:8"
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
      "005b6130",
      "DATA",
      [
        "storage",
        "00c6fa60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6130",
      "DATA",
      [
        "storage",
        "00c6fe60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b60e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b60cc.md#insn-005b60e0) · [`005b60ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b60cc.md#insn-005b60ec)
- 新版 `005b6120`（命令位置の公開資料なし） · `005b612c`（命令位置の公開資料なし）

~~~diff
- 005b60e0 ["INT_ADD", "register:40f0:8", ["const:5b60e0:8", "const:4:8"]]
- 005b60e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b6120 ["INT_ADD", "register:40f0:8", ["const:5b6120:8", "const:4:8"]]
+ 005b6120 ["CALL", null, ["callee:00c57e90:8"]]
- 005b60e0 bytes 6c861a94
+ 005b6120 bytes 5c871a94
- 005b60ec ["COPY", "tmp:0:8", ["const:a60:8"]]
- 005b60ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b60ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b60ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b612c ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 005b612c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b612c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b612c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b60ec bytes 08812991
+ 005b612c bytes 08813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53ceab3303aa6c130b7777be7ca52a9f"></a>

### [`005b6104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6104.md) → [`005b6144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6144.md) FUN_005b6144

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6148",
      "incomplete_value": false,
      "site": "005b614c",
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
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6108",
      "incomplete_value": false,
      "site": "005b610c",
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
            "const:a60:8"
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
      "005b614c",
      "DATA",
      [
        "storage",
        "00c6fa60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b614c",
      "DATA",
      [
        "storage",
        "00c6fe60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6104.md#insn-005b6108)
- 新版 `005b6148`（命令位置の公開資料なし）

~~~diff
- 005b6108 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 005b6108 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6108 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6108 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6148 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 005b6148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6108 bytes 08812991
+ 005b6148 bytes 08813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e09287ec9ee578f09342008e8dda8f00"></a>

### [`005b6164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6164.md) → [`005b61a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b61a4.md) FUN_005b61a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b61c8",
      "incomplete_value": false,
      "site": "005b61c8",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6188",
      "incomplete_value": false,
      "site": "005b6188",
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
            "const:ae0:8"
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
      "005b61c8",
      "DATA",
      [
        "storage",
        "00c6fae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b61c8",
      "DATA",
      [
        "storage",
        "00c6fee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6164.md#insn-005b6178) · [`005b6184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6164.md#insn-005b6184)
- 新版 `005b61b8`（命令位置の公開資料なし） · `005b61c4`（命令位置の公開資料なし）

~~~diff
- 005b6178 ["INT_ADD", "register:40f0:8", ["const:5b6178:8", "const:4:8"]]
- 005b6178 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b61b8 ["INT_ADD", "register:40f0:8", ["const:5b61b8:8", "const:4:8"]]
+ 005b61b8 ["CALL", null, ["callee:00c57e90:8"]]
- 005b6178 bytes 46861a94
+ 005b61b8 bytes 36871a94
- 005b6184 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 005b6184 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6184 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b61c4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 005b61c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b61c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b61c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6184 bytes 08812b91
+ 005b61c4 bytes 08813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4497541d4cde572a22db91f9dbe456a2"></a>

### [`005b6198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6198.md) → [`005b61d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b61d8.md) FUN_005b61d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b61e4",
      "incomplete_value": false,
      "site": "005b61e4",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b61a4",
      "incomplete_value": false,
      "site": "005b61a4",
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
            "const:ae0:8"
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
      "005b61e4",
      "DATA",
      [
        "storage",
        "00c6fae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b61e4",
      "DATA",
      [
        "storage",
        "00c6fee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b61a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6198.md#insn-005b61a0)
- 新版 `005b61e0`（命令位置の公開資料なし）

~~~diff
- 005b61a0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 005b61a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b61a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b61a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b61e0 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 005b61e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b61e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b61e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b61a0 bytes 29812b91
+ 005b61e0 bytes 29813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc87864113747d9e6d42fea9e368fd22"></a>

### [`005b6218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6218.md) → [`005b6258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6258.md) FUN_005b6258

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b627c",
      "incomplete_value": false,
      "site": "005b627c",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b623c",
      "incomplete_value": false,
      "site": "005b623c",
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
            "const:b60:8"
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
      "005b627c",
      "DATA",
      [
        "storage",
        "00c6fb60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b627c",
      "DATA",
      [
        "storage",
        "00c6ff60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b622c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6218.md#insn-005b622c) · [`005b6238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6218.md#insn-005b6238)
- 新版 `005b626c`（命令位置の公開資料なし） · `005b6278`（命令位置の公開資料なし）

~~~diff
- 005b622c ["INT_ADD", "register:40f0:8", ["const:5b622c:8", "const:4:8"]]
- 005b622c ["CALL", null, ["callee:00c57e90:8"]]
+ 005b626c ["INT_ADD", "register:40f0:8", ["const:5b626c:8", "const:4:8"]]
+ 005b626c ["CALL", null, ["callee:00c57e90:8"]]
- 005b622c bytes 19861a94
+ 005b626c bytes 09871a94
- 005b6238 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 005b6238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6278 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 005b6278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6238 bytes 08812d91
+ 005b6278 bytes 08813d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b7083fa8fc601b49e481110f4500e78"></a>

### [`005b6340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6340.md) → [`005b6380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6380.md) FUN_005b6380

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b63a4",
      "incomplete_value": false,
      "site": "005b63a4",
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
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6364",
      "incomplete_value": false,
      "site": "005b6364",
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
            "const:be0:8"
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
      "005b63a4",
      "DATA",
      [
        "storage",
        "00c6fbe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b63a4",
      "DATA",
      [
        "storage",
        "00c6ffe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6340.md#insn-005b6354) · [`005b6360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6340.md#insn-005b6360)
- 新版 `005b6394`（命令位置の公開資料なし） · `005b63a0`（命令位置の公開資料なし）

~~~diff
- 005b6354 ["INT_ADD", "register:40f0:8", ["const:5b6354:8", "const:4:8"]]
- 005b6354 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b6394 ["INT_ADD", "register:40f0:8", ["const:5b6394:8", "const:4:8"]]
+ 005b6394 ["CALL", null, ["callee:00c57e90:8"]]
- 005b6354 bytes cf851a94
+ 005b6394 bytes bf861a94
- 005b6360 ["COPY", "tmp:0:8", ["const:be0:8"]]
- 005b6360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b63a0 ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 005b63a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b63a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b63a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6360 bytes 08812f91
+ 005b63a0 bytes 08813f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f90db9f82b6a2f50cd940c7dadb34d3"></a>

### [`005b6374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6374.md) → [`005b63b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b63b4.md) FUN_005b63b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b63c0",
      "incomplete_value": false,
      "site": "005b63c0",
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
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6380",
      "incomplete_value": false,
      "site": "005b6380",
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
            "const:be0:8"
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
      "005b63c0",
      "DATA",
      [
        "storage",
        "00c6fbe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b63c0",
      "DATA",
      [
        "storage",
        "00c6ffe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b637c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6374.md#insn-005b637c)
- 新版 `005b63bc`（命令位置の公開資料なし）

~~~diff
- 005b637c ["COPY", "tmp:0:8", ["const:be0:8"]]
- 005b637c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b637c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b637c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b63bc ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 005b63bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b63bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b63bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b637c bytes 29812f91
+ 005b63bc bytes 29813f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df903438b6ac5abc8de9ae5af3398cfd"></a>

### [`005b63d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b63d8.md) → [`005b6418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6418.md) FUN_005b6418

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b643c",
      "incomplete_value": false,
      "site": "005b643c",
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
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b63fc",
      "incomplete_value": false,
      "site": "005b63fc",
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
            "const:c60:8"
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
      "005b643c",
      "DATA",
      [
        "storage",
        "00c6fc60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b643c",
      "DATA",
      [
        "storage",
        "00c70060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b63ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b63d8.md#insn-005b63ec) · [`005b63f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b63d8.md#insn-005b63f4) · [`005b63f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b63d8.md#insn-005b63f8)
- 新版 `005b642c`（命令位置の公開資料なし） · `005b6434`（命令位置の公開資料なし） · `005b6438`（命令位置の公開資料なし）

~~~diff
- 005b63ec ["INT_ADD", "register:40f0:8", ["const:5b63ec:8", "const:4:8"]]
- 005b63ec ["CALL", null, ["callee:00c57e90:8"]]
+ 005b642c ["INT_ADD", "register:40f0:8", ["const:5b642c:8", "const:4:8"]]
+ 005b642c ["CALL", null, ["callee:00c57e90:8"]]
- 005b63ec bytes a9851a94
+ 005b642c bytes 99861a94
- 005b63f4 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b6434 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b63f4 bytes c83500b0
+ 005b6434 bytes c83500d0
- 005b63f8 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 005b63f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b63f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b63f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6438 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 005b6438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b63f8 bytes 08813191
+ 005b6438 bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2a9033235302f5b16775bda86f68794"></a>

### [`005b640c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b640c.md) → [`005b644c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b644c.md) FUN_005b644c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6458",
      "incomplete_value": false,
      "site": "005b6458",
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
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6418",
      "incomplete_value": false,
      "site": "005b6418",
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
            "const:c60:8"
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
      "005b6458",
      "DATA",
      [
        "storage",
        "00c6fc60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6458",
      "DATA",
      [
        "storage",
        "00c70060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b640c.md#insn-005b6410) · [`005b6414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b640c.md#insn-005b6414)
- 新版 `005b6450`（命令位置の公開資料なし） · `005b6454`（命令位置の公開資料なし）

~~~diff
- 005b6410 ["COPY", "register:4048:8", ["const:c6f000:8"]]
+ 005b6450 ["COPY", "register:4048:8", ["const:c70000:8"]]
- 005b6410 bytes c93500b0
+ 005b6450 bytes c93500d0
- 005b6414 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 005b6414 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6414 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6414 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6454 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 005b6454 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6454 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6454 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6414 bytes 29813191
+ 005b6454 bytes 29810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-998ffa371b9b2cebf2e820517a77e9b8"></a>

### [`005b6428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6428.md) → [`005b6468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6468.md) FUN_005b6468

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0053efd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efd8.md) [`005b664c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b664c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0053f018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f018.md) [`005b668c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b668c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b64e4",
      "incomplete_value": false,
      "site": "005b64fc",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b64a4",
      "incomplete_value": false,
      "site": "005b64bc",
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
            "const:ce0:8"
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
      "005b64fc",
      "DATA",
      [
        "storage",
        "00c6fce0",
        null,
        "pointer"
      ]
    ],
    [
      "005b6560",
      "READ",
      [
        "storage",
        "00c6fcf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b64fc",
      "DATA",
      [
        "storage",
        "00c700e0",
        null,
        "pointer"
      ]
    ],
    [
      "005b6560",
      "READ",
      [
        "storage",
        "00c700f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6428.md#insn-005b6490) · [`005b64a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6428.md#insn-005b64a0) · [`005b64a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6428.md#insn-005b64a4)
- 新版 `005b64d0`（命令位置の公開資料なし） · `005b64e0`（命令位置の公開資料なし） · `005b64e4`（命令位置の公開資料なし）

~~~diff
- 005b6490 ["INT_ADD", "register:40f0:8", ["const:5b6490:8", "const:4:8"]]
- 005b6490 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b64d0 ["INT_ADD", "register:40f0:8", ["const:5b64d0:8", "const:4:8"]]
+ 005b64d0 ["CALL", null, ["callee:00c57e90:8"]]
- 005b6490 bytes 80851a94
+ 005b64d0 bytes 70861a94
- 005b64a0 ["COPY", "register:4048:8", ["const:c6f000:8"]]
+ 005b64e0 ["COPY", "register:4048:8", ["const:c70000:8"]]
- 005b64a0 bytes c93500b0
+ 005b64e0 bytes c93500d0
- 005b64a4 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 005b64a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b64a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b64a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b64e4 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 005b64e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b64e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b64e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b64a4 bytes 29813391
+ 005b64e4 bytes 29810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcd098f4dc1713dcc7e6126386e77cc2"></a>

### [`005b660c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b660c.md) → [`005b664c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b664c.md) FUN_005b664c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "005b6650",
      "incomplete_value": false,
      "site": "005b6654",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6610",
      "incomplete_value": false,
      "site": "005b6614",
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
            "const:ce0:8"
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
      "005b6654",
      "DATA",
      [
        "storage",
        "00c6fce0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b6654",
      "DATA",
      [
        "storage",
        "00c700e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b660c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b660c.md#insn-005b660c) · [`005b6610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b660c.md#insn-005b6610)
- 新版 `005b664c`（命令位置の公開資料なし） · `005b6650`（命令位置の公開資料なし）

~~~diff
- 005b660c ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b664c ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b660c bytes c83500b0
+ 005b664c bytes c83500d0
- 005b6610 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 005b6610 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6610 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6610 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6650 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 005b6650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6610 bytes 08813391
+ 005b6650 bytes 08810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28d9ac8de6bbdcce75d7cbed60b5171c"></a>

### [`005b661c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b661c.md) → [`005b665c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b665c.md) FUN_005b665c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b666c",
      "incomplete_value": false,
      "site": "005b6674",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b662c",
      "incomplete_value": false,
      "site": "005b6634",
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
            "const:ce0:8"
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
      "005b6674",
      "DATA",
      [
        "storage",
        "00c6fce0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b6674",
      "DATA",
      [
        "storage",
        "00c700e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b661c.md#insn-005b6628) · [`005b662c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b661c.md#insn-005b662c) · [`005b6638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b661c.md#insn-005b6638)
- 新版 `005b6668`（命令位置の公開資料なし） · `005b666c`（命令位置の公開資料なし） · `005b6678`（命令位置の公開資料なし）

~~~diff
- 005b6628 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b6668 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b6628 bytes c83500b0
+ 005b6668 bytes c83500d0
- 005b662c ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 005b662c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b662c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b662c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b666c ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 005b666c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b666c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b666c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b662c bytes 08813391
+ 005b666c bytes 08810391
- 005b6638 ["INT_ADD", "register:40f0:8", ["const:5b6638:8", "const:4:8"]]
- 005b6638 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005b6678 ["INT_ADD", "register:40f0:8", ["const:5b6678:8", "const:4:8"]]
+ 005b6678 ["CALL", null, ["callee:00c57ea0:8"]]
- 005b6638 bytes 1a851a94
+ 005b6678 bytes 0a861a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38136b351d4be2d09248bed7025bf9cd"></a>

### [`005b66d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b66d0.md) → [`005b6710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6710.md) FUN_005b6710

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b6734",
      "incomplete_value": false,
      "site": "005b6734",
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
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b66f4",
      "incomplete_value": false,
      "site": "005b66f4",
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
            "const:d40:8"
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
      "005b6734",
      "DATA",
      [
        "storage",
        "00c6fd40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6734",
      "DATA",
      [
        "storage",
        "00c70140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b66e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b66d0.md#insn-005b66e4) · [`005b66ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b66d0.md#insn-005b66ec) · [`005b66f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b66d0.md#insn-005b66f0)
- 新版 `005b6724`（命令位置の公開資料なし） · `005b672c`（命令位置の公開資料なし） · `005b6730`（命令位置の公開資料なし）

~~~diff
- 005b66e4 ["INT_ADD", "register:40f0:8", ["const:5b66e4:8", "const:4:8"]]
- 005b66e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b6724 ["INT_ADD", "register:40f0:8", ["const:5b6724:8", "const:4:8"]]
+ 005b6724 ["CALL", null, ["callee:00c57e90:8"]]
- 005b66e4 bytes eb841a94
+ 005b6724 bytes db851a94
- 005b66ec ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b672c ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b66ec bytes c83500b0
+ 005b672c bytes c83500d0
- 005b66f0 ["COPY", "tmp:0:8", ["const:d40:8"]]
- 005b66f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b66f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b66f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6730 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 005b6730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b66f0 bytes 08013591
+ 005b6730 bytes 08010591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38a65bf682b9381ac5aa79b738deaf66"></a>

### [`005b6704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6704.md) → [`005b6744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6744.md) FUN_005b6744

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6750",
      "incomplete_value": false,
      "site": "005b6750",
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
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6710",
      "incomplete_value": false,
      "site": "005b6710",
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
            "const:d40:8"
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
      "005b6750",
      "DATA",
      [
        "storage",
        "00c6fd40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6750",
      "DATA",
      [
        "storage",
        "00c70140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6704.md#insn-005b6708) · [`005b670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6704.md#insn-005b670c)
- 新版 `005b6748`（命令位置の公開資料なし） · `005b674c`（命令位置の公開資料なし）

~~~diff
- 005b6708 ["COPY", "register:4048:8", ["const:c6f000:8"]]
+ 005b6748 ["COPY", "register:4048:8", ["const:c70000:8"]]
- 005b6708 bytes c93500b0
+ 005b6748 bytes c93500d0
- 005b670c ["COPY", "tmp:0:8", ["const:d40:8"]]
- 005b670c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b670c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b670c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b674c ["COPY", "tmp:0:8", ["const:140:8"]]
+ 005b674c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b674c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b674c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b670c bytes 29013591
+ 005b674c bytes 29010591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6af6dffae1703d5fb2791363f26aa589"></a>

### [`005b6768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6768.md) → [`005b67a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b67a8.md) FUN_005b67a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b67cc",
      "incomplete_value": false,
      "site": "005b67cc",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b678c",
      "incomplete_value": false,
      "site": "005b678c",
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
            "const:dc0:8"
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
      "005b67cc",
      "DATA",
      [
        "storage",
        "00c6fdc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b67cc",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b677c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6768.md#insn-005b677c) · [`005b6784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6768.md#insn-005b6784) · [`005b6788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6768.md#insn-005b6788)
- 新版 `005b67bc`（命令位置の公開資料なし） · `005b67c4`（命令位置の公開資料なし） · `005b67c8`（命令位置の公開資料なし）

~~~diff
- 005b677c ["INT_ADD", "register:40f0:8", ["const:5b677c:8", "const:4:8"]]
- 005b677c ["CALL", null, ["callee:00c57e90:8"]]
+ 005b67bc ["INT_ADD", "register:40f0:8", ["const:5b67bc:8", "const:4:8"]]
+ 005b67bc ["CALL", null, ["callee:00c57e90:8"]]
- 005b677c bytes c5841a94
+ 005b67bc bytes b5851a94
- 005b6784 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b67c4 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b6784 bytes c83500b0
+ 005b67c4 bytes c83500d0
- 005b6788 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 005b6788 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6788 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6788 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b67c8 ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 005b67c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b67c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b67c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6788 bytes 08013791
+ 005b67c8 bytes 08010791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a67c5a51663b94e03988b201195bcb56"></a>

### [`005b679c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b679c.md) → [`005b67dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b67dc.md) FUN_005b67dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b67e8",
      "incomplete_value": false,
      "site": "005b67e8",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b67a8",
      "incomplete_value": false,
      "site": "005b67a8",
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
            "const:dc0:8"
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
      "005b67e8",
      "DATA",
      [
        "storage",
        "00c6fdc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b67e8",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b67a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b679c.md#insn-005b67a0) · [`005b67a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b679c.md#insn-005b67a4)
- 新版 `005b67e0`（命令位置の公開資料なし） · `005b67e4`（命令位置の公開資料なし）

~~~diff
- 005b67a0 ["COPY", "register:4048:8", ["const:c6f000:8"]]
+ 005b67e0 ["COPY", "register:4048:8", ["const:c70000:8"]]
- 005b67a0 bytes c93500b0
+ 005b67e0 bytes c93500d0
- 005b67a4 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 005b67a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b67a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b67a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b67e4 ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 005b67e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b67e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b67e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b67a4 bytes 29013791
+ 005b67e4 bytes 29010791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2b1c45b72857ac5c3484651feaa9458"></a>

### [`005b67f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b67f0.md) → [`005b6830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6830.md) FUN_005b6830

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b6854",
      "incomplete_value": false,
      "site": "005b6854",
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
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6814",
      "incomplete_value": false,
      "site": "005b6814",
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
            "const:e50:8"
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
      "005b6854",
      "DATA",
      [
        "storage",
        "00c6fe50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6854",
      "DATA",
      [
        "storage",
        "00c70250",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b67f0.md#insn-005b6804) · [`005b680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b67f0.md#insn-005b680c) · [`005b6810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b67f0.md#insn-005b6810)
- 新版 `005b6844`（命令位置の公開資料なし） · `005b684c`（命令位置の公開資料なし） · `005b6850`（命令位置の公開資料なし）

~~~diff
- 005b6804 ["INT_ADD", "register:40f0:8", ["const:5b6804:8", "const:4:8"]]
- 005b6804 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b6844 ["INT_ADD", "register:40f0:8", ["const:5b6844:8", "const:4:8"]]
+ 005b6844 ["CALL", null, ["callee:00c57e90:8"]]
- 005b6804 bytes a3841a94
+ 005b6844 bytes 93851a94
- 005b680c ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b684c ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b680c bytes c83500b0
+ 005b684c bytes c83500d0
- 005b6810 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 005b6810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6850 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 005b6850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6810 bytes 08413991
+ 005b6850 bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba0f6e85673eed646e233cebfbe397c7"></a>

### [`005b6824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6824.md) → [`005b6864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6864.md) FUN_005b6864

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6870",
      "incomplete_value": false,
      "site": "005b6870",
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
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6830",
      "incomplete_value": false,
      "site": "005b6830",
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
            "const:e50:8"
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
      "005b6870",
      "DATA",
      [
        "storage",
        "00c6fe50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6870",
      "DATA",
      [
        "storage",
        "00c70250",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6824.md#insn-005b6828) · [`005b682c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6824.md#insn-005b682c)
- 新版 `005b6868`（命令位置の公開資料なし） · `005b686c`（命令位置の公開資料なし）

~~~diff
- 005b6828 ["COPY", "register:4048:8", ["const:c6f000:8"]]
+ 005b6868 ["COPY", "register:4048:8", ["const:c70000:8"]]
- 005b6828 bytes c93500b0
+ 005b6868 bytes c93500d0
- 005b682c ["COPY", "tmp:0:8", ["const:e50:8"]]
- 005b682c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b682c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b682c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b686c ["COPY", "tmp:0:8", ["const:250:8"]]
+ 005b686c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b686c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b686c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b682c bytes 29413991
+ 005b686c bytes 29410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4fb018b7342dbcc964b99acfce22272"></a>

### [`005b6888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6888.md) → [`005b68c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b68c8.md) FUN_005b68c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b68ec",
      "incomplete_value": false,
      "site": "005b68ec",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b68ac",
      "incomplete_value": false,
      "site": "005b68ac",
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
            "const:ed0:8"
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
      "005b68ec",
      "DATA",
      [
        "storage",
        "00c6fed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b68ec",
      "DATA",
      [
        "storage",
        "00c702d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b689c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6888.md#insn-005b689c) · [`005b68a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6888.md#insn-005b68a4) · [`005b68a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6888.md#insn-005b68a8)
- 新版 `005b68dc`（命令位置の公開資料なし） · `005b68e4`（命令位置の公開資料なし） · `005b68e8`（命令位置の公開資料なし）

~~~diff
- 005b689c ["INT_ADD", "register:40f0:8", ["const:5b689c:8", "const:4:8"]]
- 005b689c ["CALL", null, ["callee:00c57e90:8"]]
+ 005b68dc ["INT_ADD", "register:40f0:8", ["const:5b68dc:8", "const:4:8"]]
+ 005b68dc ["CALL", null, ["callee:00c57e90:8"]]
- 005b689c bytes 7d841a94
+ 005b68dc bytes 6d851a94
- 005b68a4 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b68e4 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b68a4 bytes c83500b0
+ 005b68e4 bytes c83500d0
- 005b68a8 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 005b68a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b68a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b68a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b68e8 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 005b68e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b68e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b68e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b68a8 bytes 08413b91
+ 005b68e8 bytes 08410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5bd28dc858f6077056d426c791637a5"></a>

### [`005b68bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b68bc.md) → [`005b68fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b68fc.md) FUN_005b68fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6908",
      "incomplete_value": false,
      "site": "005b6908",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b68c8",
      "incomplete_value": false,
      "site": "005b68c8",
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
            "const:ed0:8"
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
      "005b6908",
      "DATA",
      [
        "storage",
        "00c6fed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6908",
      "DATA",
      [
        "storage",
        "00c702d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b68c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b68bc.md#insn-005b68c0) · [`005b68c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b68bc.md#insn-005b68c4)
- 新版 `005b6900`（命令位置の公開資料なし） · `005b6904`（命令位置の公開資料なし）

~~~diff
- 005b68c0 ["COPY", "register:4048:8", ["const:c6f000:8"]]
+ 005b6900 ["COPY", "register:4048:8", ["const:c70000:8"]]
- 005b68c0 bytes c93500b0
+ 005b6900 bytes c93500d0
- 005b68c4 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 005b68c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b68c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b68c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6904 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 005b6904 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6904 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6904 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b68c4 bytes 29413b91
+ 005b6904 bytes 29410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fcbdad32064bd1f673936efc04422cd"></a>

### [`005b68d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b68d8.md) → [`005b6918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6918.md) FUN_005b6918

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`005b0b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0b9c.md) [`005b51d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51d4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005b0bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0bdc.md) [`005b5214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5214.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.95% / 新版 87.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b6964",
      "incomplete_value": true,
      "site": "005b6970",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6924",
      "incomplete_value": true,
      "site": "005b6930",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e80:8"
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
      "definition_site": "005b6960",
      "incomplete_value": true,
      "site": "005b6974",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:dbf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6920",
      "incomplete_value": true,
      "site": "005b6934",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:cf2:8"
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
      "definition_site": "005b6960",
      "incomplete_value": true,
      "site": "005b6974",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "005b6920",
      "incomplete_value": true,
      "site": "005b6934",
      "value": [
        "LOAD",
        "16",
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
      "005b6960",
      "READ",
      [
        "storage",
        "002a8cf2",
        null,
        null
      ]
    ],
    [
      "005b6960",
      "READ",
      [
        "storage",
        "002a8d02",
        null,
        null
      ]
    ],
    [
      "005b6964",
      "READ",
      [
        "storage",
        "002c2e80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005b6960",
      "READ",
      [
        "storage",
        "002a8dbf",
        null,
        null
      ]
    ],
    [
      "005b6960",
      "READ",
      [
        "storage",
        "002a8dcf",
        null,
        null
      ]
    ],
    [
      "005b6964",
      "READ",
      [
        "storage",
        "002c2ec0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b68d8.md#insn-005b6924) · [`005b6978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b68d8.md#insn-005b6978) · [`005b6910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b68d8.md#insn-005b6910)
- 新版 `005b6964`（命令位置の公開資料なし） · `005b69b8`（命令位置の公開資料なし） · `005b6950`（命令位置の公開資料なし）

~~~diff
- 005b6924 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e80:8"]]
- 005b6924 ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
- 005b6924 ["COPY", "register:5050:8", ["const:0:8"]]
- 005b6924 ["COPY", "register:5058:8", ["const:0:8"]]
+ 005b6964 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ec0:8"]]
+ 005b6964 ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
+ 005b6964 ["COPY", "register:5050:8", ["const:0:8"]]
+ 005b6964 ["COPY", "register:5058:8", ["const:0:8"]]
- 005b6924 bytes 22a1c33d
+ 005b6964 bytes 22b1c33d
- 005b6978 ["INT_ADD", "register:40f0:8", ["const:5b6978:8", "const:4:8"]]
- 005b6978 ["CALL", null, ["callee:005b0bdc:8"]]
+ 005b69b8 ["INT_ADD", "register:40f0:8", ["const:5b69b8:8", "const:4:8"]]
+ 005b69b8 ["CALL", null, ["callee:005b0bdc:8"]]
- 005b6978 bytes 89e8ff97
+ 005b69b8 bytes 89e8ff97
- 005b6910 ["INT_ADD", "register:40f0:8", ["const:5b6910:8", "const:4:8"]]
- 005b6910 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b6950 ["INT_ADD", "register:40f0:8", ["const:5b6950:8", "const:4:8"]]
+ 005b6950 ["CALL", null, ["callee:00c57e90:8"]]
- 005b6910 bytes 60841a94
+ 005b6950 bytes 50851a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2874af951bb6bd7ed39aa48f5211b421"></a>

### [`005b6aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6aa8.md) → [`005b6ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6ae8.md) FUN_005b6ae8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b6b0c",
      "incomplete_value": false,
      "site": "005b6b0c",
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
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6acc",
      "incomplete_value": false,
      "site": "005b6acc",
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
            "const:f60:8"
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
      "005b6b0c",
      "DATA",
      [
        "storage",
        "00c6ff60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6b0c",
      "DATA",
      [
        "storage",
        "00c70360",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6aa8.md#insn-005b6abc) · [`005b6ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6aa8.md#insn-005b6ac4) · [`005b6ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6aa8.md#insn-005b6ac8)
- 新版 `005b6afc`（命令位置の公開資料なし） · `005b6b04`（命令位置の公開資料なし） · `005b6b08`（命令位置の公開資料なし）

~~~diff
- 005b6abc ["INT_ADD", "register:40f0:8", ["const:5b6abc:8", "const:4:8"]]
- 005b6abc ["CALL", null, ["callee:00c57e90:8"]]
+ 005b6afc ["INT_ADD", "register:40f0:8", ["const:5b6afc:8", "const:4:8"]]
+ 005b6afc ["CALL", null, ["callee:00c57e90:8"]]
- 005b6abc bytes f5831a94
+ 005b6afc bytes e5841a94
- 005b6ac4 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b6b04 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b6ac4 bytes c83500b0
+ 005b6b04 bytes c83500d0
- 005b6ac8 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 005b6ac8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6ac8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6ac8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6b08 ["COPY", "tmp:0:8", ["const:360:8"]]
+ 005b6b08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6b08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6b08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6ac8 bytes 08813d91
+ 005b6b08 bytes 08810d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4646898bad6edfee969cb1237af20ea"></a>

### [`005b6af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6af8.md) → [`005b6b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6b38.md) FUN_005b6b38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`005b6dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6dac.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005b6dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6dec.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.46% / 新版 97.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b6bbc",
      "incomplete_value": false,
      "site": "005b6bc4",
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
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6b7c",
      "incomplete_value": false,
      "site": "005b6b84",
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
            "const:fe0:8"
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
      "005b6bc4",
      "DATA",
      [
        "storage",
        "00c6ffe0",
        null,
        "pointer"
      ]
    ],
    [
      "005b6cbc",
      "READ",
      [
        "storage",
        "00c6fff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6bc4",
      "DATA",
      [
        "storage",
        "00c703e0",
        null,
        "pointer"
      ]
    ],
    [
      "005b6cbc",
      "READ",
      [
        "storage",
        "00c703f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6af8.md#insn-005b6b6c) · [`005b6b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6af8.md#insn-005b6b78) · [`005b6b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6af8.md#insn-005b6b7c)
- 新版 `005b6bac`（命令位置の公開資料なし） · `005b6bb8`（命令位置の公開資料なし） · `005b6bbc`（命令位置の公開資料なし）

~~~diff
- 005b6b6c ["INT_ADD", "register:40f0:8", ["const:5b6b6c:8", "const:4:8"]]
- 005b6b6c ["CALL", null, ["callee:00c57e90:8"]]
+ 005b6bac ["INT_ADD", "register:40f0:8", ["const:5b6bac:8", "const:4:8"]]
+ 005b6bac ["CALL", null, ["callee:00c57e90:8"]]
- 005b6b6c bytes c9831a94
+ 005b6bac bytes b9841a94
- 005b6b78 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b6bb8 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b6b78 bytes c83500b0
+ 005b6bb8 bytes c83500d0
- 005b6b7c ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 005b6b7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6b7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6b7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6bbc ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 005b6bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6b7c bytes 08813f91
+ 005b6bbc bytes 08810f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e340c5646f182eb124e605e2e205ce27"></a>

### [`005b6d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6d6c.md) → [`005b6dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6dac.md) FUN_005b6dac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "005b6db0",
      "incomplete_value": false,
      "site": "005b6db4",
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
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6d70",
      "incomplete_value": false,
      "site": "005b6d74",
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
            "const:fe0:8"
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
      "005b6db4",
      "DATA",
      [
        "storage",
        "00c6ffe0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b6db4",
      "DATA",
      [
        "storage",
        "00c703e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6d6c.md#insn-005b6d6c) · [`005b6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6d6c.md#insn-005b6d70)
- 新版 `005b6dac`（命令位置の公開資料なし） · `005b6db0`（命令位置の公開資料なし）

~~~diff
- 005b6d6c ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b6dac ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b6d6c bytes c83500b0
+ 005b6dac bytes c83500d0
- 005b6d70 ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 005b6d70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6d70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6d70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6db0 ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 005b6db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6d70 bytes 08813f91
+ 005b6db0 bytes 08810f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad0ec4b1eba49743282514b70d60b341"></a>

### [`005b6d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6d7c.md) → [`005b6dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6dbc.md) FUN_005b6dbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b6dcc",
      "incomplete_value": false,
      "site": "005b6dd4",
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
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6d8c",
      "incomplete_value": false,
      "site": "005b6d94",
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
            "const:fe0:8"
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
      "005b6dd4",
      "DATA",
      [
        "storage",
        "00c6ffe0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b6dd4",
      "DATA",
      [
        "storage",
        "00c703e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6d7c.md#insn-005b6d88) · [`005b6d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6d7c.md#insn-005b6d8c) · [`005b6d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6d7c.md#insn-005b6d98)
- 新版 `005b6dc8`（命令位置の公開資料なし） · `005b6dcc`（命令位置の公開資料なし） · `005b6dd8`（命令位置の公開資料なし）

~~~diff
- 005b6d88 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b6dc8 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b6d88 bytes c83500b0
+ 005b6dc8 bytes c83500d0
- 005b6d8c ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 005b6d8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6d8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6d8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6dcc ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 005b6dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6d8c bytes 08813f91
+ 005b6dcc bytes 08810f91
- 005b6d98 ["INT_ADD", "register:40f0:8", ["const:5b6d98:8", "const:4:8"]]
- 005b6d98 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005b6dd8 ["INT_ADD", "register:40f0:8", ["const:5b6dd8:8", "const:4:8"]]
+ 005b6dd8 ["CALL", null, ["callee:00c57ea0:8"]]
- 005b6d98 bytes 42831a94
+ 005b6dd8 bytes 32841a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-513f11e2167d2e820fe9347cf888a0d0"></a>

### [`005b6e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6e3c.md) → [`005b6e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6e7c.md) FUN_005b6e7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b6ea0",
      "incomplete_value": false,
      "site": "005b6ea0",
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
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6e60",
      "incomplete_value": false,
      "site": "005b6e60",
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
            "const:40:8"
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
      "005b6ea0",
      "DATA",
      [
        "storage",
        "00c70040",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6ea0",
      "DATA",
      [
        "storage",
        "00c70440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6e3c.md#insn-005b6e50) · [`005b6e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6e3c.md#insn-005b6e5c)
- 新版 `005b6e90`（命令位置の公開資料なし） · `005b6e9c`（命令位置の公開資料なし）

~~~diff
- 005b6e50 ["INT_ADD", "register:40f0:8", ["const:5b6e50:8", "const:4:8"]]
- 005b6e50 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b6e90 ["INT_ADD", "register:40f0:8", ["const:5b6e90:8", "const:4:8"]]
+ 005b6e90 ["CALL", null, ["callee:00c57e90:8"]]
- 005b6e50 bytes 10831a94
+ 005b6e90 bytes 00841a94
- 005b6e5c ["COPY", "tmp:0:8", ["const:40:8"]]
- 005b6e5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6e5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6e5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6e9c ["COPY", "tmp:0:8", ["const:440:8"]]
+ 005b6e9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6e9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6e9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6e5c bytes 08010191
+ 005b6e9c bytes 08011191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f30ce142cf4dce14e3addb327bc5fad"></a>

### [`005b6e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6e70.md) → [`005b6eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6eb0.md) FUN_005b6eb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6ebc",
      "incomplete_value": false,
      "site": "005b6ebc",
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
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6e7c",
      "incomplete_value": false,
      "site": "005b6e7c",
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
            "const:40:8"
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
      "005b6ebc",
      "DATA",
      [
        "storage",
        "00c70040",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6ebc",
      "DATA",
      [
        "storage",
        "00c70440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6e70.md#insn-005b6e78)
- 新版 `005b6eb8`（命令位置の公開資料なし）

~~~diff
- 005b6e78 ["COPY", "tmp:0:8", ["const:40:8"]]
- 005b6e78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6e78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6e78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6eb8 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 005b6eb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6eb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6eb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6e78 bytes 29010191
+ 005b6eb8 bytes 29011191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e145ae19b3648287875fed94d3446c2"></a>

### [`005b6f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6f88.md) → [`005b6fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6fc8.md) FUN_005b6fc8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b6fec",
      "incomplete_value": false,
      "site": "005b6fec",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6fac",
      "incomplete_value": false,
      "site": "005b6fac",
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
            "const:c0:8"
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
      "005b6fec",
      "DATA",
      [
        "storage",
        "00c700c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6fec",
      "DATA",
      [
        "storage",
        "00c704c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6f88.md#insn-005b6f9c) · [`005b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6f88.md#insn-005b6fa8)
- 新版 `005b6fdc`（命令位置の公開資料なし） · `005b6fe8`（命令位置の公開資料なし）

~~~diff
- 005b6f9c ["INT_ADD", "register:40f0:8", ["const:5b6f9c:8", "const:4:8"]]
- 005b6f9c ["CALL", null, ["callee:00c57e90:8"]]
+ 005b6fdc ["INT_ADD", "register:40f0:8", ["const:5b6fdc:8", "const:4:8"]]
+ 005b6fdc ["CALL", null, ["callee:00c57e90:8"]]
- 005b6f9c bytes bd821a94
+ 005b6fdc bytes ad831a94
- 005b6fa8 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 005b6fa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6fa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6fa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6fe8 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 005b6fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6fa8 bytes 08010391
+ 005b6fe8 bytes 08011391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4132bb06a3fe4d4ef99691d14cbad56f"></a>

### [`005b6fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6fbc.md) → [`005b6ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6ffc.md) FUN_005b6ffc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b7008",
      "incomplete_value": false,
      "site": "005b7008",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6fc8",
      "incomplete_value": false,
      "site": "005b6fc8",
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
            "const:c0:8"
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
      "005b7008",
      "DATA",
      [
        "storage",
        "00c700c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7008",
      "DATA",
      [
        "storage",
        "00c704c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6fbc.md#insn-005b6fc4)
- 新版 `005b7004`（命令位置の公開資料なし）

~~~diff
- 005b6fc4 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 005b6fc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6fc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6fc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b7004 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 005b7004 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7004 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7004 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6fc4 bytes 29010391
+ 005b7004 bytes 29011391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbf2bc756e31e72a24bdd01b5821a614"></a>

### [`005b70b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b70b4.md) → [`005b70f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b70f4.md) FUN_005b70f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b7118",
      "incomplete_value": false,
      "site": "005b7118",
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
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b70d8",
      "incomplete_value": false,
      "site": "005b70d8",
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
            "const:140:8"
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
      "005b7118",
      "DATA",
      [
        "storage",
        "00c70140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7118",
      "DATA",
      [
        "storage",
        "00c70540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b70c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b70b4.md#insn-005b70c8) · [`005b70d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b70b4.md#insn-005b70d4)
- 新版 `005b7108`（命令位置の公開資料なし） · `005b7114`（命令位置の公開資料なし）

~~~diff
- 005b70c8 ["INT_ADD", "register:40f0:8", ["const:5b70c8:8", "const:4:8"]]
- 005b70c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b7108 ["INT_ADD", "register:40f0:8", ["const:5b7108:8", "const:4:8"]]
+ 005b7108 ["CALL", null, ["callee:00c57e90:8"]]
- 005b70c8 bytes 72821a94
+ 005b7108 bytes 62831a94
- 005b70d4 ["COPY", "tmp:0:8", ["const:140:8"]]
- 005b70d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b70d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b70d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7114 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 005b7114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b70d4 bytes 08010591
+ 005b7114 bytes 08011591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b75f80b642e37e4837d464c7d6ff4422"></a>

### [`005b70e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b70e8.md) → [`005b7128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7128.md) FUN_005b7128

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b7134",
      "incomplete_value": false,
      "site": "005b7134",
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
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b70f4",
      "incomplete_value": false,
      "site": "005b70f4",
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
            "const:140:8"
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
      "005b7134",
      "DATA",
      [
        "storage",
        "00c70140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7134",
      "DATA",
      [
        "storage",
        "00c70540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b70f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b70e8.md#insn-005b70f0)
- 新版 `005b7130`（命令位置の公開資料なし）

~~~diff
- 005b70f0 ["COPY", "tmp:0:8", ["const:140:8"]]
- 005b70f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b70f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b70f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b7130 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 005b7130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b70f0 bytes 29010591
+ 005b7130 bytes 29011591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c10a6e818e48fb26a2e476139dc210e"></a>

### [`005b7144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7144.md) → [`005b7184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7184.md) FUN_005b7184

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b3b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3b34.md) · 呼出先 7件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) [`005b72fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72fc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`005b3b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.40% / 新版 97.40%

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
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b717c",
      "incomplete_value": false,
      "site": "005b7184",
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
            "const:1c0:8"
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
      "005b71c4",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b727c",
      "READ",
      [
        "storage",
        "00c701d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b71c4",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b727c",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b71c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7144.md#insn-005b71c4) · [`005b7174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7144.md#insn-005b7174) · [`005b717c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7144.md#insn-005b717c)
- 新版 `005b7204`（命令位置の公開資料なし） · `005b71b4`（命令位置の公開資料なし） · `005b71bc`（命令位置の公開資料なし）

~~~diff
- 005b71c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b71c4 ["INT_ADD", "register:40f0:8", ["const:5b71c4:8", "const:4:8"]]
- 005b71c4 ["CALLIND", null, ["register:0:8"]]
+ 005b7204 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7204 ["INT_ADD", "register:40f0:8", ["const:5b7204:8", "const:4:8"]]
+ 005b7204 ["CALLIND", null, ["register:0:8"]]
- 005b71c4 bytes 00013fd6
+ 005b7204 bytes 00013fd6
- 005b7174 ["INT_ADD", "register:40f0:8", ["const:5b7174:8", "const:4:8"]]
- 005b7174 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b71b4 ["INT_ADD", "register:40f0:8", ["const:5b71b4:8", "const:4:8"]]
+ 005b71b4 ["CALL", null, ["callee:00c57e90:8"]]
- 005b7174 bytes 47821a94
+ 005b71b4 bytes 37831a94
- 005b717c ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 005b717c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b717c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b717c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b71bc ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 005b71bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b71bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b71bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b717c bytes 08010791
+ 005b71bc bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b29b2c28ff5e7b06e7874ddab0b74672"></a>

### [`005b72bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72bc.md) → [`005b72fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b72fc.md) FUN_005b72fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "005b7300",
      "incomplete_value": false,
      "site": "005b7304",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b72c0",
      "incomplete_value": false,
      "site": "005b72c4",
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
            "const:1c0:8"
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
      "005b7304",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b7304",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b72c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72bc.md#insn-005b72c0)
- 新版 `005b7300`（命令位置の公開資料なし）

~~~diff
- 005b72c0 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 005b72c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b72c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b72c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7300 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 005b7300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b72c0 bytes 08010791
+ 005b7300 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-294f745995a577779ca2d0fa8edc9ec3"></a>

### [`005b72cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72cc.md) → [`005b730c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b730c.md) FUN_005b730c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b731c",
      "incomplete_value": false,
      "site": "005b7324",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b72dc",
      "incomplete_value": false,
      "site": "005b72e4",
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
            "const:1c0:8"
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
      "005b7324",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b7324",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b72dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72cc.md#insn-005b72dc) · [`005b72e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72cc.md#insn-005b72e8)
- 新版 `005b731c`（命令位置の公開資料なし） · `005b7328`（命令位置の公開資料なし）

~~~diff
- 005b72dc ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 005b72dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b72dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b72dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b731c ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 005b731c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b731c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b731c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b72dc bytes 08010791
+ 005b731c bytes 08011791
- 005b72e8 ["INT_ADD", "register:40f0:8", ["const:5b72e8:8", "const:4:8"]]
- 005b72e8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005b7328 ["INT_ADD", "register:40f0:8", ["const:5b7328:8", "const:4:8"]]
+ 005b7328 ["CALL", null, ["callee:00c57ea0:8"]]
- 005b72e8 bytes ee811a94
+ 005b7328 bytes de821a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-114be2c4f15904138b69e3d36b28bc2d"></a>

### [`005b730c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b730c.md) → [`005b734c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b734c.md) FUN_005b734c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b7358",
      "incomplete_value": false,
      "site": "005b7364",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7318",
      "incomplete_value": false,
      "site": "005b7324",
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
      "005b7364",
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
      "005b7364",
      "DATA",
      [
        "storage",
        "00c70610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b730c.md#insn-005b7318)
- 新版 `005b7358`（命令位置の公開資料なし）

~~~diff
- 005b7318 ["COPY", "tmp:0:8", ["const:210:8"]]
- 005b7318 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b7318 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b7318 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b7358 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 005b7358 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b7358 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b7358 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b7318 bytes 4a410891
+ 005b7358 bytes 4a411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24d53afee8bd1ce51d0e7a725514d483"></a>

### [`005b7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7350.md) → [`005b7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7390.md) FUN_005b7390

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b73a8",
      "incomplete_value": false,
      "site": "005b73b4",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7368",
      "incomplete_value": false,
      "site": "005b7374",
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
      "005b73b4",
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
      "005b73b4",
      "DATA",
      [
        "storage",
        "00c70610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7350.md#insn-005b7368) · [`005b7398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7350.md#insn-005b7398)
- 新版 `005b73a8`（命令位置の公開資料なし） · `005b73d8`（命令位置の公開資料なし）

~~~diff
- 005b7368 ["COPY", "tmp:0:8", ["const:210:8"]]
- 005b7368 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7368 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7368 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b73a8 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 005b73a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b73a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b73a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7368 bytes 08410891
+ 005b73a8 bytes 08411891
- 005b7398 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7398 ["INT_ADD", "register:40f0:8", ["const:5b7398:8", "const:4:8"]]
- 005b7398 ["CALLIND", null, ["register:0:8"]]
+ 005b73d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b73d8 ["INT_ADD", "register:40f0:8", ["const:5b73d8:8", "const:4:8"]]
+ 005b73d8 ["CALLIND", null, ["register:0:8"]]
- 005b7398 bytes 00013fd6
+ 005b73d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-071e63155ed41d7e4fc60550388a6a17"></a>

### [`005b73ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b73ac.md) → [`005b73ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b73ec.md) FUN_005b73ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b7418",
      "incomplete_value": false,
      "site": "005b7418",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b73d8",
      "incomplete_value": false,
      "site": "005b73d8",
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
      "005b7418",
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
      "005b7418",
      "DATA",
      [
        "storage",
        "00c70610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b73c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b73ac.md#insn-005b73c0) · [`005b73d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b73ac.md#insn-005b73d0) · [`005b73f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b73ac.md#insn-005b73f4)
- 新版 `005b7400`（命令位置の公開資料なし） · `005b7410`（命令位置の公開資料なし） · `005b7434`（命令位置の公開資料なし）

~~~diff
- 005b73c0 ["INT_ADD", "register:40f0:8", ["const:5b73c0:8", "const:4:8"]]
- 005b73c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b7400 ["INT_ADD", "register:40f0:8", ["const:5b7400:8", "const:4:8"]]
+ 005b7400 ["CALL", null, ["callee:00c57e90:8"]]
- 005b73c0 bytes b4811a94
+ 005b7400 bytes a4821a94
- 005b73d0 ["COPY", "tmp:0:8", ["const:210:8"]]
- 005b73d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b73d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b73d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7410 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 005b7410 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7410 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7410 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b73d0 bytes 08410891
+ 005b7410 bytes 08411891
- 005b73f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b73f4 ["INT_ADD", "register:40f0:8", ["const:5b73f4:8", "const:4:8"]]
- 005b73f4 ["CALLIND", null, ["register:0:8"]]
+ 005b7434 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7434 ["INT_ADD", "register:40f0:8", ["const:5b7434:8", "const:4:8"]]
+ 005b7434 ["CALLIND", null, ["register:0:8"]]
- 005b73f4 bytes 00013fd6
+ 005b7434 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db2662b40055f207e6c0d452a9d0ea56"></a>

### [`005b7434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7434.md) → [`005b7474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7474.md) FUN_005b7474

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b7490",
      "incomplete_value": false,
      "site": "005b7490",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7450",
      "incomplete_value": false,
      "site": "005b7450",
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
      "005b7490",
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
      "005b7490",
      "DATA",
      [
        "storage",
        "00c70610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b744c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7434.md#insn-005b744c) · [`005b7470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7434.md#insn-005b7470)
- 新版 `005b748c`（命令位置の公開資料なし） · `005b74b0`（命令位置の公開資料なし）

~~~diff
- 005b744c ["COPY", "tmp:0:8", ["const:210:8"]]
- 005b744c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b744c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b744c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b748c ["COPY", "tmp:0:8", ["const:610:8"]]
+ 005b748c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b748c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b748c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b744c bytes 29410891
+ 005b748c bytes 29411891
- 005b7470 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b7470 ["INT_ADD", "register:40f0:8", ["const:5b7470:8", "const:4:8"]]
- 005b7470 ["CALLIND", null, ["register:0:8"]]
+ 005b74b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b74b0 ["INT_ADD", "register:40f0:8", ["const:5b74b0:8", "const:4:8"]]
+ 005b74b0 ["CALLIND", null, ["register:0:8"]]
- 005b7470 bytes 20013fd6
+ 005b74b0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c60aa4f1c03d3d58d4f12c3fa54e66d6"></a>

### [`005b76f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b76f4.md) → [`005b7734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7734.md) FUN_005b7734

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b1de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1de4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005b1e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1e24.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b7774",
      "incomplete_value": false,
      "site": "005b7778",
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
                "const:a10:8"
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
      "definition_site": "005b7734",
      "incomplete_value": false,
      "site": "005b7738",
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
                "const:610:8"
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
      "005b7778",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7778",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b76f4.md#insn-005b7714) · [`005b7724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b76f4.md#insn-005b7724) · [`005b772c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b76f4.md#insn-005b772c)
- 新版 `005b7754`（命令位置の公開資料なし） · `005b7764`（命令位置の公開資料なし） · `005b776c`（命令位置の公開資料なし）

~~~diff
- 005b7714 ["INT_ADD", "register:40f0:8", ["const:5b7714:8", "const:4:8"]]
- 005b7714 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b7754 ["INT_ADD", "register:40f0:8", ["const:5b7754:8", "const:4:8"]]
+ 005b7754 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b7714 bytes e7801a94
+ 005b7754 bytes d7811a94
- 005b7724 ["INT_ADD", "register:40f0:8", ["const:5b7724:8", "const:4:8"]]
- 005b7724 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b7764 ["INT_ADD", "register:40f0:8", ["const:5b7764:8", "const:4:8"]]
+ 005b7764 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b7724 bytes e3801a94
+ 005b7764 bytes d3811a94
- 005b772c ["COPY", "tmp:0:8", ["const:610:8"]]
- 005b772c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b772c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b772c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b776c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005b776c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b776c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b776c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b772c bytes 08411891
+ 005b776c bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-525a6c0d7084aa3399d4dc250eb243e8"></a>

### [`005b776c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b776c.md) → [`005b77ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b77ac.md) FUN_005b77ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b1de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1de4.md) · 呼出先 7件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) [`005b72fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72fc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`005b1e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1e24.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "005b77e4",
      "incomplete_value": false,
      "site": "005b77ec",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b77a4",
      "incomplete_value": false,
      "site": "005b77ac",
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
            "const:1c0:8"
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
      "005b77ec",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b78a4",
      "READ",
      [
        "storage",
        "00c701d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b77ec",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b78a4",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b77ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b776c.md#insn-005b77ec) · [`005b779c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b776c.md#insn-005b779c) · [`005b77a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b776c.md#insn-005b77a4)
- 新版 `005b782c`（命令位置の公開資料なし） · `005b77dc`（命令位置の公開資料なし） · `005b77e4`（命令位置の公開資料なし）

~~~diff
- 005b77ec ["COPY", "register:0:8", ["register:4040:8"]]
- 005b77ec ["INT_ADD", "register:40f0:8", ["const:5b77ec:8", "const:4:8"]]
- 005b77ec ["CALLIND", null, ["register:0:8"]]
+ 005b782c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b782c ["INT_ADD", "register:40f0:8", ["const:5b782c:8", "const:4:8"]]
+ 005b782c ["CALLIND", null, ["register:0:8"]]
- 005b77ec bytes 00013fd6
+ 005b782c bytes 00013fd6
- 005b779c ["INT_ADD", "register:40f0:8", ["const:5b779c:8", "const:4:8"]]
- 005b779c ["CALL", null, ["callee:00c57e90:8"]]
+ 005b77dc ["INT_ADD", "register:40f0:8", ["const:5b77dc:8", "const:4:8"]]
+ 005b77dc ["CALL", null, ["callee:00c57e90:8"]]
- 005b779c bytes bd801a94
+ 005b77dc bytes ad811a94
- 005b77a4 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 005b77a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b77a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b77a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b77e4 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 005b77e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b77e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b77e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b77a4 bytes 08010791
+ 005b77e4 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-270d2b8940dade6e9eaef323df0f720c"></a>

### [`005b78e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b78e4.md) → [`005b7924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7924.md) FUN_005b7924

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b7930",
      "incomplete_value": false,
      "site": "005b793c",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b78f0",
      "incomplete_value": false,
      "site": "005b78fc",
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
      "005b793c",
      "DATA",
      [
        "storage",
        "00c702a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b793c",
      "DATA",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b78f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b78e4.md#insn-005b78f0)
- 新版 `005b7930`（命令位置の公開資料なし）

~~~diff
- 005b78f0 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 005b78f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b78f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b78f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b7930 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 005b7930 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b7930 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b7930 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b78f0 bytes 4a810a91
+ 005b7930 bytes 4a811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-331b08809e74e4fa1e1e57f5b6be6c6f"></a>

### [`005b7928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7928.md) → [`005b7968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7968.md) FUN_005b7968

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b7980",
      "incomplete_value": false,
      "site": "005b798c",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7940",
      "incomplete_value": false,
      "site": "005b794c",
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
      "005b798c",
      "DATA",
      [
        "storage",
        "00c702a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b798c",
      "DATA",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7928.md#insn-005b7940) · [`005b7970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7928.md#insn-005b7970)
- 新版 `005b7980`（命令位置の公開資料なし） · `005b79b0`（命令位置の公開資料なし）

~~~diff
- 005b7940 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 005b7940 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7940 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7940 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7980 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 005b7980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7940 bytes 08810a91
+ 005b7980 bytes 08811a91
- 005b7970 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7970 ["INT_ADD", "register:40f0:8", ["const:5b7970:8", "const:4:8"]]
- 005b7970 ["CALLIND", null, ["register:0:8"]]
+ 005b79b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b79b0 ["INT_ADD", "register:40f0:8", ["const:5b79b0:8", "const:4:8"]]
+ 005b79b0 ["CALLIND", null, ["register:0:8"]]
- 005b7970 bytes 00013fd6
+ 005b79b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79c24539eeb03b9b4884e09c1a49a1db"></a>

### [`005b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7984.md) → [`005b79c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b79c4.md) FUN_005b79c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b79f0",
      "incomplete_value": false,
      "site": "005b79f0",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b79b0",
      "incomplete_value": false,
      "site": "005b79b0",
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
            "const:2a0:8"
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
      "005b79f0",
      "DATA",
      [
        "storage",
        "00c702a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b79f0",
      "DATA",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7984.md#insn-005b7998) · [`005b79a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7984.md#insn-005b79a8) · [`005b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7984.md#insn-005b79cc)
- 新版 `005b79d8`（命令位置の公開資料なし） · `005b79e8`（命令位置の公開資料なし） · `005b7a0c`（命令位置の公開資料なし）

~~~diff
- 005b7998 ["INT_ADD", "register:40f0:8", ["const:5b7998:8", "const:4:8"]]
- 005b7998 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b79d8 ["INT_ADD", "register:40f0:8", ["const:5b79d8:8", "const:4:8"]]
+ 005b79d8 ["CALL", null, ["callee:00c57e90:8"]]
- 005b7998 bytes 3e801a94
+ 005b79d8 bytes 2e811a94
- 005b79a8 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 005b79a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b79a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b79a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b79e8 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 005b79e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b79e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b79e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b79a8 bytes 08810a91
+ 005b79e8 bytes 08811a91
- 005b79cc ["COPY", "register:0:8", ["register:4040:8"]]
- 005b79cc ["INT_ADD", "register:40f0:8", ["const:5b79cc:8", "const:4:8"]]
- 005b79cc ["CALLIND", null, ["register:0:8"]]
+ 005b7a0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7a0c ["INT_ADD", "register:40f0:8", ["const:5b7a0c:8", "const:4:8"]]
+ 005b7a0c ["CALLIND", null, ["register:0:8"]]
- 005b79cc bytes 00013fd6
+ 005b7a0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84b47060de2346ade95e064625bb9f8f"></a>

### [`005b7a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7a0c.md) → [`005b7a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7a4c.md) FUN_005b7a4c

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b7a68",
      "incomplete_value": false,
      "site": "005b7a68",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7a28",
      "incomplete_value": false,
      "site": "005b7a28",
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
      "005b7a68",
      "DATA",
      [
        "storage",
        "00c702a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7a68",
      "DATA",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7a0c.md#insn-005b7a24) · [`005b7a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7a0c.md#insn-005b7a48)
- 新版 `005b7a64`（命令位置の公開資料なし） · `005b7a88`（命令位置の公開資料なし）

~~~diff
- 005b7a24 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 005b7a24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b7a24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b7a24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b7a64 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 005b7a64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7a64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7a64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b7a24 bytes 29810a91
+ 005b7a64 bytes 29811a91
- 005b7a48 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b7a48 ["INT_ADD", "register:40f0:8", ["const:5b7a48:8", "const:4:8"]]
- 005b7a48 ["CALLIND", null, ["register:0:8"]]
+ 005b7a88 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b7a88 ["INT_ADD", "register:40f0:8", ["const:5b7a88:8", "const:4:8"]]
+ 005b7a88 ["CALLIND", null, ["register:0:8"]]
- 005b7a48 bytes 20013fd6
+ 005b7a88 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0071797fcc4506df3af1da24368d974"></a>

### [`005b7cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7cb8.md) → [`005b7cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7cf8.md) FUN_005b7cf8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b35b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b35b8.md) · 呼出先 7件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) [`005b72fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72fc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`005b35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "005b7d30",
      "incomplete_value": false,
      "site": "005b7d38",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7cf0",
      "incomplete_value": false,
      "site": "005b7cf8",
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
            "const:1c0:8"
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
      "005b7d38",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b7df0",
      "READ",
      [
        "storage",
        "00c701d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7d38",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b7df0",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7cb8.md#insn-005b7d38) · [`005b7ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7cb8.md#insn-005b7ce8) · [`005b7cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7cb8.md#insn-005b7cf0)
- 新版 `005b7d78`（命令位置の公開資料なし） · `005b7d28`（命令位置の公開資料なし） · `005b7d30`（命令位置の公開資料なし）

~~~diff
- 005b7d38 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7d38 ["INT_ADD", "register:40f0:8", ["const:5b7d38:8", "const:4:8"]]
- 005b7d38 ["CALLIND", null, ["register:0:8"]]
+ 005b7d78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7d78 ["INT_ADD", "register:40f0:8", ["const:5b7d78:8", "const:4:8"]]
+ 005b7d78 ["CALLIND", null, ["register:0:8"]]
- 005b7d38 bytes 00013fd6
+ 005b7d78 bytes 00013fd6
- 005b7ce8 ["INT_ADD", "register:40f0:8", ["const:5b7ce8:8", "const:4:8"]]
- 005b7ce8 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b7d28 ["INT_ADD", "register:40f0:8", ["const:5b7d28:8", "const:4:8"]]
+ 005b7d28 ["CALL", null, ["callee:00c57e90:8"]]
- 005b7ce8 bytes 6a7f1a94
+ 005b7d28 bytes 5a801a94
- 005b7cf0 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 005b7cf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7cf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7cf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7d30 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 005b7d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7cf0 bytes 08010791
+ 005b7d30 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b755b79028f0820e371aa73a2a4810b7"></a>

### [`005b7e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7e74.md) → [`005b7eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7eb4.md) FUN_005b7eb4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b7ecc",
      "incomplete_value": false,
      "site": "005b7ed8",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7e8c",
      "incomplete_value": false,
      "site": "005b7e98",
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
      "005b7ed8",
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
      "005b7ed8",
      "DATA",
      [
        "storage",
        "00c70720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7e74.md#insn-005b7e8c) · [`005b7ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7e74.md#insn-005b7ebc)
- 新版 `005b7ecc`（命令位置の公開資料なし） · `005b7efc`（命令位置の公開資料なし）

~~~diff
- 005b7e8c ["COPY", "tmp:0:8", ["const:320:8"]]
- 005b7e8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7e8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7e8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7ecc ["COPY", "tmp:0:8", ["const:720:8"]]
+ 005b7ecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7ecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7ecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7e8c bytes 08810c91
+ 005b7ecc bytes 08811c91
- 005b7ebc ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7ebc ["INT_ADD", "register:40f0:8", ["const:5b7ebc:8", "const:4:8"]]
- 005b7ebc ["CALLIND", null, ["register:0:8"]]
+ 005b7efc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7efc ["INT_ADD", "register:40f0:8", ["const:5b7efc:8", "const:4:8"]]
+ 005b7efc ["CALLIND", null, ["register:0:8"]]
- 005b7ebc bytes 00013fd6
+ 005b7efc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90513f1dc5555b040b012481795010e5"></a>

### [`005b7ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7ed0.md) → [`005b7f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7f10.md) FUN_005b7f10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b7f3c",
      "incomplete_value": false,
      "site": "005b7f3c",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7efc",
      "incomplete_value": false,
      "site": "005b7efc",
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
      "005b7f3c",
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
      "005b7f3c",
      "DATA",
      [
        "storage",
        "00c70720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7ed0.md#insn-005b7ee4) · [`005b7ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7ed0.md#insn-005b7ef4) · [`005b7f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7ed0.md#insn-005b7f18)
- 新版 `005b7f24`（命令位置の公開資料なし） · `005b7f34`（命令位置の公開資料なし） · `005b7f58`（命令位置の公開資料なし）

~~~diff
- 005b7ee4 ["INT_ADD", "register:40f0:8", ["const:5b7ee4:8", "const:4:8"]]
- 005b7ee4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b7f24 ["INT_ADD", "register:40f0:8", ["const:5b7f24:8", "const:4:8"]]
+ 005b7f24 ["CALL", null, ["callee:00c57e90:8"]]
- 005b7ee4 bytes eb7e1a94
+ 005b7f24 bytes db7f1a94
- 005b7ef4 ["COPY", "tmp:0:8", ["const:320:8"]]
- 005b7ef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7ef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7ef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7f34 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 005b7f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7ef4 bytes 08810c91
+ 005b7f34 bytes 08811c91
- 005b7f18 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7f18 ["INT_ADD", "register:40f0:8", ["const:5b7f18:8", "const:4:8"]]
- 005b7f18 ["CALLIND", null, ["register:0:8"]]
+ 005b7f58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7f58 ["INT_ADD", "register:40f0:8", ["const:5b7f58:8", "const:4:8"]]
+ 005b7f58 ["CALLIND", null, ["register:0:8"]]
- 005b7f18 bytes 00013fd6
+ 005b7f58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fa70d39dbabf962ab5e56adff9be434"></a>

### [`005b7f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7f58.md) → [`005b7f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7f98.md) FUN_005b7f98

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b7fb4",
      "incomplete_value": false,
      "site": "005b7fb4",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7f74",
      "incomplete_value": false,
      "site": "005b7f74",
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
      "005b7fb4",
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
      "005b7fb4",
      "DATA",
      [
        "storage",
        "00c70720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7f58.md#insn-005b7f70) · [`005b7f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7f58.md#insn-005b7f94)
- 新版 `005b7fb0`（命令位置の公開資料なし） · `005b7fd4`（命令位置の公開資料なし）

~~~diff
- 005b7f70 ["COPY", "tmp:0:8", ["const:320:8"]]
- 005b7f70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b7f70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b7f70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b7fb0 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 005b7fb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7fb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7fb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b7f70 bytes 29810c91
+ 005b7fb0 bytes 29811c91
- 005b7f94 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b7f94 ["INT_ADD", "register:40f0:8", ["const:5b7f94:8", "const:4:8"]]
- 005b7f94 ["CALLIND", null, ["register:0:8"]]
+ 005b7fd4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b7fd4 ["INT_ADD", "register:40f0:8", ["const:5b7fd4:8", "const:4:8"]]
+ 005b7fd4 ["CALLIND", null, ["register:0:8"]]
- 005b7f94 bytes 20013fd6
+ 005b7fd4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20c00283044f62e2d3c66b46ec5c5f33"></a>

### [`005b809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b809c.md) → [`005b80dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b80dc.md) FUN_005b80dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b271c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b271c.md) · 呼出先 7件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) [`005b72fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72fc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`005b275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b8114",
      "incomplete_value": false,
      "site": "005b811c",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b80d4",
      "incomplete_value": false,
      "site": "005b80dc",
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
            "const:1c0:8"
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
      "005b811c",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b81d4",
      "READ",
      [
        "storage",
        "00c701d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b811c",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b81d4",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b811c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b809c.md#insn-005b811c) · [`005b80cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b809c.md#insn-005b80cc) · [`005b80d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b809c.md#insn-005b80d4)
- 新版 `005b815c`（命令位置の公開資料なし） · `005b810c`（命令位置の公開資料なし） · `005b8114`（命令位置の公開資料なし）

~~~diff
- 005b811c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b811c ["INT_ADD", "register:40f0:8", ["const:5b811c:8", "const:4:8"]]
- 005b811c ["CALLIND", null, ["register:0:8"]]
+ 005b815c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b815c ["INT_ADD", "register:40f0:8", ["const:5b815c:8", "const:4:8"]]
+ 005b815c ["CALLIND", null, ["register:0:8"]]
- 005b811c bytes 00013fd6
+ 005b815c bytes 00013fd6
- 005b80cc ["INT_ADD", "register:40f0:8", ["const:5b80cc:8", "const:4:8"]]
- 005b80cc ["CALL", null, ["callee:00c57e90:8"]]
+ 005b810c ["INT_ADD", "register:40f0:8", ["const:5b810c:8", "const:4:8"]]
+ 005b810c ["CALL", null, ["callee:00c57e90:8"]]
- 005b80cc bytes 717e1a94
+ 005b810c bytes 617f1a94
- 005b80d4 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 005b80d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b80d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b80d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8114 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 005b8114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b80d4 bytes 08010791
+ 005b8114 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b0ebaab4031e8acb7c8ab95c559a45b"></a>

### [`005b8214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8214.md) → [`005b8254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8254.md) FUN_005b8254

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b8260",
      "incomplete_value": false,
      "site": "005b826c",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8220",
      "incomplete_value": false,
      "site": "005b822c",
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
      "005b826c",
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
      "005b826c",
      "DATA",
      [
        "storage",
        "00c707a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8214.md#insn-005b8220)
- 新版 `005b8260`（命令位置の公開資料なし）

~~~diff
- 005b8220 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 005b8220 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b8220 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b8220 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b8260 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 005b8260 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b8260 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b8260 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b8220 bytes 4a810e91
+ 005b8260 bytes 4a811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-114194bdbddee76916a707f2e46c9afb"></a>

### [`005b8258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8258.md) → [`005b8298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8298.md) FUN_005b8298

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b82b0",
      "incomplete_value": false,
      "site": "005b82bc",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8270",
      "incomplete_value": false,
      "site": "005b827c",
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
      "005b82bc",
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
      "005b82bc",
      "DATA",
      [
        "storage",
        "00c707a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8258.md#insn-005b8270) · [`005b82a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8258.md#insn-005b82a0)
- 新版 `005b82b0`（命令位置の公開資料なし） · `005b82e0`（命令位置の公開資料なし）

~~~diff
- 005b8270 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 005b8270 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8270 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b82b0 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 005b82b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b82b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b82b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8270 bytes 08810e91
+ 005b82b0 bytes 08811e91
- 005b82a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b82a0 ["INT_ADD", "register:40f0:8", ["const:5b82a0:8", "const:4:8"]]
- 005b82a0 ["CALLIND", null, ["register:0:8"]]
+ 005b82e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b82e0 ["INT_ADD", "register:40f0:8", ["const:5b82e0:8", "const:4:8"]]
+ 005b82e0 ["CALLIND", null, ["register:0:8"]]
- 005b82a0 bytes 00013fd6
+ 005b82e0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d56039a0b7589a763752b138474d9a6"></a>

### [`005b82b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b82b4.md) → [`005b82f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b82f4.md) FUN_005b82f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b8320",
      "incomplete_value": false,
      "site": "005b8320",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b82e0",
      "incomplete_value": false,
      "site": "005b82e0",
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
      "005b8320",
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
      "005b8320",
      "DATA",
      [
        "storage",
        "00c707a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b82c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b82b4.md#insn-005b82c8) · [`005b82d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b82b4.md#insn-005b82d8) · [`005b82fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b82b4.md#insn-005b82fc)
- 新版 `005b8308`（命令位置の公開資料なし） · `005b8318`（命令位置の公開資料なし） · `005b833c`（命令位置の公開資料なし）

~~~diff
- 005b82c8 ["INT_ADD", "register:40f0:8", ["const:5b82c8:8", "const:4:8"]]
- 005b82c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b8308 ["INT_ADD", "register:40f0:8", ["const:5b8308:8", "const:4:8"]]
+ 005b8308 ["CALL", null, ["callee:00c57e90:8"]]
- 005b82c8 bytes f27d1a94
+ 005b8308 bytes e27e1a94
- 005b82d8 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 005b82d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b82d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b82d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8318 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 005b8318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b82d8 bytes 08810e91
+ 005b8318 bytes 08811e91
- 005b82fc ["COPY", "register:0:8", ["register:4040:8"]]
- 005b82fc ["INT_ADD", "register:40f0:8", ["const:5b82fc:8", "const:4:8"]]
- 005b82fc ["CALLIND", null, ["register:0:8"]]
+ 005b833c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b833c ["INT_ADD", "register:40f0:8", ["const:5b833c:8", "const:4:8"]]
+ 005b833c ["CALLIND", null, ["register:0:8"]]
- 005b82fc bytes 00013fd6
+ 005b833c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6ecad6c64a7ee5b847d2e222d3942c3"></a>

### [`005b833c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b833c.md) → [`005b837c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b837c.md) FUN_005b837c

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b8398",
      "incomplete_value": false,
      "site": "005b8398",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8358",
      "incomplete_value": false,
      "site": "005b8358",
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
      "005b8398",
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
      "005b8398",
      "DATA",
      [
        "storage",
        "00c707a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b833c.md#insn-005b8354) · [`005b8378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b833c.md#insn-005b8378)
- 新版 `005b8394`（命令位置の公開資料なし） · `005b83b8`（命令位置の公開資料なし）

~~~diff
- 005b8354 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 005b8354 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b8354 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b8354 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b8394 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 005b8394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b8394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b8394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b8354 bytes 29810e91
+ 005b8394 bytes 29811e91
- 005b8378 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b8378 ["INT_ADD", "register:40f0:8", ["const:5b8378:8", "const:4:8"]]
- 005b8378 ["CALLIND", null, ["register:0:8"]]
+ 005b83b8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b83b8 ["INT_ADD", "register:40f0:8", ["const:5b83b8:8", "const:4:8"]]
+ 005b83b8 ["CALLIND", null, ["register:0:8"]]
- 005b8378 bytes 20013fd6
+ 005b83b8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da8e7d81695a898d03f8efcf5060f2f9"></a>

### [`005b8480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8480.md) → [`005b84c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b84c0.md) FUN_005b84c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b3fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3fe0.md) · 呼出先 7件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) [`005b72fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72fc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`005b4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b84f8",
      "incomplete_value": true,
      "site": "005b8500",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b84b8",
      "incomplete_value": true,
      "site": "005b84c0",
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
            "const:1c0:8"
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
      "005b8500",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b85b8",
      "READ",
      [
        "storage",
        "00c701d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8500",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b85b8",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8480.md#insn-005b8500) · [`005b84b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8480.md#insn-005b84b0) · [`005b84b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8480.md#insn-005b84b8)
- 新版 `005b8540`（命令位置の公開資料なし） · `005b84f0`（命令位置の公開資料なし） · `005b84f8`（命令位置の公開資料なし）

~~~diff
- 005b8500 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8500 ["INT_ADD", "register:40f0:8", ["const:5b8500:8", "const:4:8"]]
- 005b8500 ["CALLIND", null, ["register:0:8"]]
+ 005b8540 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8540 ["INT_ADD", "register:40f0:8", ["const:5b8540:8", "const:4:8"]]
+ 005b8540 ["CALLIND", null, ["register:0:8"]]
- 005b8500 bytes 00013fd6
+ 005b8540 bytes 00013fd6
- 005b84b0 ["INT_ADD", "register:40f0:8", ["const:5b84b0:8", "const:4:8"]]
- 005b84b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b84f0 ["INT_ADD", "register:40f0:8", ["const:5b84f0:8", "const:4:8"]]
+ 005b84f0 ["CALL", null, ["callee:00c57e90:8"]]
- 005b84b0 bytes 787d1a94
+ 005b84f0 bytes 687e1a94
- 005b84b8 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 005b84b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b84b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b84b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b84f8 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 005b84f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b84f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b84f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b84b8 bytes 08010791
+ 005b84f8 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7255fe07fa44e2b2b8de0e4d34f9b0ef"></a>

### [`005b863c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b863c.md) → [`005b867c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b867c.md) FUN_005b867c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b8694",
      "incomplete_value": false,
      "site": "005b86a0",
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
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8654",
      "incomplete_value": false,
      "site": "005b8660",
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
            "const:420:8"
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
      "005b86a0",
      "DATA",
      [
        "storage",
        "00c70420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b86a0",
      "DATA",
      [
        "storage",
        "00c70820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b863c.md#insn-005b8654) · [`005b8684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b863c.md#insn-005b8684)
- 新版 `005b8694`（命令位置の公開資料なし） · `005b86c4`（命令位置の公開資料なし）

~~~diff
- 005b8654 ["COPY", "tmp:0:8", ["const:420:8"]]
- 005b8654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8694 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 005b8694 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8694 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8694 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8654 bytes 08811091
+ 005b8694 bytes 08812091
- 005b8684 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8684 ["INT_ADD", "register:40f0:8", ["const:5b8684:8", "const:4:8"]]
- 005b8684 ["CALLIND", null, ["register:0:8"]]
+ 005b86c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b86c4 ["INT_ADD", "register:40f0:8", ["const:5b86c4:8", "const:4:8"]]
+ 005b86c4 ["CALLIND", null, ["register:0:8"]]
- 005b8684 bytes 00013fd6
+ 005b86c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf09ca2e7e917e69e2bc74654b355959"></a>

### [`005b8698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8698.md) → [`005b86d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b86d8.md) FUN_005b86d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b8704",
      "incomplete_value": false,
      "site": "005b8704",
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
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b86c4",
      "incomplete_value": false,
      "site": "005b86c4",
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
            "const:420:8"
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
      "005b8704",
      "DATA",
      [
        "storage",
        "00c70420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8704",
      "DATA",
      [
        "storage",
        "00c70820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b86ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8698.md#insn-005b86ac) · [`005b86bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8698.md#insn-005b86bc) · [`005b86e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8698.md#insn-005b86e0)
- 新版 `005b86ec`（命令位置の公開資料なし） · `005b86fc`（命令位置の公開資料なし） · `005b8720`（命令位置の公開資料なし）

~~~diff
- 005b86ac ["INT_ADD", "register:40f0:8", ["const:5b86ac:8", "const:4:8"]]
- 005b86ac ["CALL", null, ["callee:00c57e90:8"]]
+ 005b86ec ["INT_ADD", "register:40f0:8", ["const:5b86ec:8", "const:4:8"]]
+ 005b86ec ["CALL", null, ["callee:00c57e90:8"]]
- 005b86ac bytes f97c1a94
+ 005b86ec bytes e97d1a94
- 005b86bc ["COPY", "tmp:0:8", ["const:420:8"]]
- 005b86bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b86bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b86bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b86fc ["COPY", "tmp:0:8", ["const:820:8"]]
+ 005b86fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b86fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b86fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b86bc bytes 08811091
+ 005b86fc bytes 08812091
- 005b86e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b86e0 ["INT_ADD", "register:40f0:8", ["const:5b86e0:8", "const:4:8"]]
- 005b86e0 ["CALLIND", null, ["register:0:8"]]
+ 005b8720 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8720 ["INT_ADD", "register:40f0:8", ["const:5b8720:8", "const:4:8"]]
+ 005b8720 ["CALLIND", null, ["register:0:8"]]
- 005b86e0 bytes 00013fd6
+ 005b8720 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee6e22ccef58b34c4ab0e2489d9bf4b1"></a>

### [`005b8720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8720.md) → [`005b8760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8760.md) FUN_005b8760

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b877c",
      "incomplete_value": false,
      "site": "005b877c",
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
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b873c",
      "incomplete_value": false,
      "site": "005b873c",
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
            "const:420:8"
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
      "005b877c",
      "DATA",
      [
        "storage",
        "00c70420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b877c",
      "DATA",
      [
        "storage",
        "00c70820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8720.md#insn-005b8738) · [`005b875c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8720.md#insn-005b875c)
- 新版 `005b8778`（命令位置の公開資料なし） · `005b879c`（命令位置の公開資料なし）

~~~diff
- 005b8738 ["COPY", "tmp:0:8", ["const:420:8"]]
- 005b8738 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b8738 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b8738 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b8778 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 005b8778 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b8778 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b8778 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b8738 bytes 29811091
+ 005b8778 bytes 29812091
- 005b875c ["COPY", "register:0:8", ["register:4048:8"]]
- 005b875c ["INT_ADD", "register:40f0:8", ["const:5b875c:8", "const:4:8"]]
- 005b875c ["CALLIND", null, ["register:0:8"]]
+ 005b879c ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b879c ["INT_ADD", "register:40f0:8", ["const:5b879c:8", "const:4:8"]]
+ 005b879c ["CALLIND", null, ["register:0:8"]]
- 005b875c bytes 20013fd6
+ 005b879c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e19a5c1df427aa152494e24dd3d9026"></a>

### [`005b8a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8a24.md) → [`005b8a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8a64.md) FUN_005b8a64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b4550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4550.md) · 呼出先 7件 [`005ac9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac9d0.md) [`005b8bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8bdc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`005b4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md) · 呼出先 7件 [`005aca10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca10.md) [`005b8c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8c1c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "005b8a9c",
      "incomplete_value": false,
      "site": "005b8aa4",
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
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8a5c",
      "incomplete_value": false,
      "site": "005b8a64",
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
            "const:4a0:8"
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
      "005b8aa4",
      "DATA",
      [
        "storage",
        "00c704a0",
        null,
        "pointer"
      ]
    ],
    [
      "005b8b5c",
      "READ",
      [
        "storage",
        "00c704b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8aa4",
      "DATA",
      [
        "storage",
        "00c708a0",
        null,
        "pointer"
      ]
    ],
    [
      "005b8b5c",
      "READ",
      [
        "storage",
        "00c708b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8a24.md#insn-005b8aa4) · [`005b8a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8a24.md#insn-005b8a54) · [`005b8a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8a24.md#insn-005b8a5c)
- 新版 `005b8ae4`（命令位置の公開資料なし） · `005b8a94`（命令位置の公開資料なし） · `005b8a9c`（命令位置の公開資料なし）

~~~diff
- 005b8aa4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8aa4 ["INT_ADD", "register:40f0:8", ["const:5b8aa4:8", "const:4:8"]]
- 005b8aa4 ["CALLIND", null, ["register:0:8"]]
+ 005b8ae4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8ae4 ["INT_ADD", "register:40f0:8", ["const:5b8ae4:8", "const:4:8"]]
+ 005b8ae4 ["CALLIND", null, ["register:0:8"]]
- 005b8aa4 bytes 00013fd6
+ 005b8ae4 bytes 00013fd6
- 005b8a54 ["INT_ADD", "register:40f0:8", ["const:5b8a54:8", "const:4:8"]]
- 005b8a54 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b8a94 ["INT_ADD", "register:40f0:8", ["const:5b8a94:8", "const:4:8"]]
+ 005b8a94 ["CALL", null, ["callee:00c57e90:8"]]
- 005b8a54 bytes 0f7c1a94
+ 005b8a94 bytes ff7c1a94
- 005b8a5c ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 005b8a5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8a5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8a5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8a9c ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 005b8a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8a5c bytes 08811291
+ 005b8a9c bytes 08812291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09a4a177021132aa0fc4e591b6dd03de"></a>

### [`005b8b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8b9c.md) → [`005b8bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8bdc.md) FUN_005b8bdc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "005b8be0",
      "incomplete_value": false,
      "site": "005b8be4",
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
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8ba0",
      "incomplete_value": false,
      "site": "005b8ba4",
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
      "005b8be4",
      "DATA",
      [
        "storage",
        "00c704a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b8be4",
      "DATA",
      [
        "storage",
        "00c708a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8b9c.md#insn-005b8ba0)
- 新版 `005b8be0`（命令位置の公開資料なし）

~~~diff
- 005b8ba0 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 005b8ba0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8ba0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8ba0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8be0 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 005b8be0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8be0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8be0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8ba0 bytes 08811291
+ 005b8be0 bytes 08812291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e68160ae15f9c5f34a6f35b30f5a17f0"></a>

### [`005b8bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8bac.md) → [`005b8bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8bec.md) FUN_005b8bec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b8bfc",
      "incomplete_value": false,
      "site": "005b8c04",
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
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8bbc",
      "incomplete_value": false,
      "site": "005b8bc4",
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
      "005b8c04",
      "DATA",
      [
        "storage",
        "00c704a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b8c04",
      "DATA",
      [
        "storage",
        "00c708a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8bac.md#insn-005b8bbc) · [`005b8bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8bac.md#insn-005b8bc8)
- 新版 `005b8bfc`（命令位置の公開資料なし） · `005b8c08`（命令位置の公開資料なし）

~~~diff
- 005b8bbc ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 005b8bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8bfc ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 005b8bfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8bfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8bfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8bbc bytes 08811291
+ 005b8bfc bytes 08812291
- 005b8bc8 ["INT_ADD", "register:40f0:8", ["const:5b8bc8:8", "const:4:8"]]
- 005b8bc8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005b8c08 ["INT_ADD", "register:40f0:8", ["const:5b8c08:8", "const:4:8"]]
+ 005b8c08 ["CALL", null, ["callee:00c57ea0:8"]]
- 005b8bc8 bytes b67b1a94
+ 005b8c08 bytes a67c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5748c526f4b613fa7cb13d879fe98859"></a>

### [`005b8bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8bec.md) → [`005b8c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8c2c.md) FUN_005b8c2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b8c38",
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
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8bf8",
      "incomplete_value": false,
      "site": "005b8c04",
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
            "const:4f0:8"
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
      "005b8c44",
      "DATA",
      [
        "storage",
        "00c704f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8c44",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8bec.md#insn-005b8bf8)
- 新版 `005b8c38`（命令位置の公開資料なし）

~~~diff
- 005b8bf8 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 005b8bf8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b8bf8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b8bf8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b8c38 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 005b8c38 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b8c38 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b8c38 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b8bf8 bytes 4ac11391
+ 005b8c38 bytes 4ac12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-005c9db7ba0d5991356ac6b7f906c617"></a>

### [`005b8c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8c30.md) → [`005b8c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8c70.md) FUN_005b8c70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b8c88",
      "incomplete_value": false,
      "site": "005b8c94",
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
    "old": {
      "definition_site": "005b8c48",
      "incomplete_value": false,
      "site": "005b8c54",
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
            "const:4f0:8"
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
      "005b8c94",
      "DATA",
      [
        "storage",
        "00c704f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8c94",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8c30.md#insn-005b8c48) · [`005b8c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8c30.md#insn-005b8c78)
- 新版 `005b8c88`（命令位置の公開資料なし） · `005b8cb8`（命令位置の公開資料なし）

~~~diff
- 005b8c48 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 005b8c48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8c48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8c48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8c88 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 005b8c88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8c88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8c88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8c48 bytes 08c11391
+ 005b8c88 bytes 08c12391
- 005b8c78 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8c78 ["INT_ADD", "register:40f0:8", ["const:5b8c78:8", "const:4:8"]]
- 005b8c78 ["CALLIND", null, ["register:0:8"]]
+ 005b8cb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8cb8 ["INT_ADD", "register:40f0:8", ["const:5b8cb8:8", "const:4:8"]]
+ 005b8cb8 ["CALLIND", null, ["register:0:8"]]
- 005b8c78 bytes 00013fd6
+ 005b8cb8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55ce9aa418c4ac5af5824adb8f5bed4f"></a>

### [`005b8c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8c8c.md) → [`005b8ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8ccc.md) FUN_005b8ccc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b8cf8",
      "incomplete_value": false,
      "site": "005b8cf8",
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
    "old": {
      "definition_site": "005b8cb8",
      "incomplete_value": false,
      "site": "005b8cb8",
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
            "const:4f0:8"
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
      "005b8cf8",
      "DATA",
      [
        "storage",
        "00c704f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8cf8",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8c8c.md#insn-005b8ca0) · [`005b8cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8c8c.md#insn-005b8cb0) · [`005b8cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8c8c.md#insn-005b8cd4)
- 新版 `005b8ce0`（命令位置の公開資料なし） · `005b8cf0`（命令位置の公開資料なし） · `005b8d14`（命令位置の公開資料なし）

~~~diff
- 005b8ca0 ["INT_ADD", "register:40f0:8", ["const:5b8ca0:8", "const:4:8"]]
- 005b8ca0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b8ce0 ["INT_ADD", "register:40f0:8", ["const:5b8ce0:8", "const:4:8"]]
+ 005b8ce0 ["CALL", null, ["callee:00c57e90:8"]]
- 005b8ca0 bytes 7c7b1a94
+ 005b8ce0 bytes 6c7c1a94
- 005b8cb0 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 005b8cb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8cb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8cb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8cf0 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 005b8cf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8cf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8cf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8cb0 bytes 08c11391
+ 005b8cf0 bytes 08c12391
- 005b8cd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8cd4 ["INT_ADD", "register:40f0:8", ["const:5b8cd4:8", "const:4:8"]]
- 005b8cd4 ["CALLIND", null, ["register:0:8"]]
+ 005b8d14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8d14 ["INT_ADD", "register:40f0:8", ["const:5b8d14:8", "const:4:8"]]
+ 005b8d14 ["CALLIND", null, ["register:0:8"]]
- 005b8cd4 bytes 00013fd6
+ 005b8d14 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b576a9acfce496cf51428aca60346d06"></a>

### [`005b8d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8d14.md) → [`005b8d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8d54.md) FUN_005b8d54

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b8d70",
      "incomplete_value": false,
      "site": "005b8d70",
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
    "old": {
      "definition_site": "005b8d30",
      "incomplete_value": false,
      "site": "005b8d30",
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
            "const:4f0:8"
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
      "005b8d70",
      "DATA",
      [
        "storage",
        "00c704f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8d70",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8d14.md#insn-005b8d2c) · [`005b8d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8d14.md#insn-005b8d50)
- 新版 `005b8d6c`（命令位置の公開資料なし） · `005b8d90`（命令位置の公開資料なし）

~~~diff
- 005b8d2c ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 005b8d2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b8d2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b8d2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b8d6c ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 005b8d6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b8d6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b8d6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b8d2c bytes 29c11391
+ 005b8d6c bytes 29c12391
- 005b8d50 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b8d50 ["INT_ADD", "register:40f0:8", ["const:5b8d50:8", "const:4:8"]]
- 005b8d50 ["CALLIND", null, ["register:0:8"]]
+ 005b8d90 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b8d90 ["INT_ADD", "register:40f0:8", ["const:5b8d90:8", "const:4:8"]]
+ 005b8d90 ["CALLIND", null, ["register:0:8"]]
- 005b8d50 bytes 20013fd6
+ 005b8d90 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abbb28b05f9a97eae2f08b8ea6171997"></a>

### [`005b8f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8f74.md) → [`005b8fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8fb4.md) FUN_005b8fb4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b4a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4a58.md) · 呼出先 7件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) [`005b72fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72fc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`005b4a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4a98.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "005b8fec",
      "incomplete_value": false,
      "site": "005b8ff4",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8fac",
      "incomplete_value": false,
      "site": "005b8fb4",
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
            "const:1c0:8"
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
      "005b8ff4",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b90ac",
      "READ",
      [
        "storage",
        "00c701d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8ff4",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b90ac",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8f74.md#insn-005b8ff4) · [`005b8fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8f74.md#insn-005b8fa4) · [`005b8fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8f74.md#insn-005b8fac)
- 新版 `005b9034`（命令位置の公開資料なし） · `005b8fe4`（命令位置の公開資料なし） · `005b8fec`（命令位置の公開資料なし）

~~~diff
- 005b8ff4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8ff4 ["INT_ADD", "register:40f0:8", ["const:5b8ff4:8", "const:4:8"]]
- 005b8ff4 ["CALLIND", null, ["register:0:8"]]
+ 005b9034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b9034 ["INT_ADD", "register:40f0:8", ["const:5b9034:8", "const:4:8"]]
+ 005b9034 ["CALLIND", null, ["register:0:8"]]
- 005b8ff4 bytes 00013fd6
+ 005b9034 bytes 00013fd6
- 005b8fa4 ["INT_ADD", "register:40f0:8", ["const:5b8fa4:8", "const:4:8"]]
- 005b8fa4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b8fe4 ["INT_ADD", "register:40f0:8", ["const:5b8fe4:8", "const:4:8"]]
+ 005b8fe4 ["CALL", null, ["callee:00c57e90:8"]]
- 005b8fa4 bytes bb7a1a94
+ 005b8fe4 bytes ab7b1a94
- 005b8fac ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 005b8fac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8fac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8fac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8fec ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 005b8fec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8fec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8fec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8fac bytes 08010791
+ 005b8fec bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

