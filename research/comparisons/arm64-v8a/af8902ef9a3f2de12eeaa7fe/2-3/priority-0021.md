# v16.0.0 → v16.0.1 · 最優先の変更候補 (21)

[一覧の目次](README.md)

<a id="compare-29967e2670d8ef4699d2a7401da14cfc"></a>

### [`0059ff60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff60.md) → [`0059ffa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059ffa0.md) FUN_0059ffa0

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
      "definition_site": "0059ffa4",
      "incomplete_value": false,
      "site": "0059ffa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ff64",
      "incomplete_value": false,
      "site": "0059ff68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "0059ffa8",
      "DATA",
      [
        "storage",
        "00c6df28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059ffa8",
      "DATA",
      [
        "storage",
        "00c6e328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ff60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff60.md#insn-0059ff60) · [`0059ff64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff60.md#insn-0059ff64)
- 新版 `0059ffa0`（命令位置の公開資料なし） · `0059ffa4`（命令位置の公開資料なし）

~~~diff
- 0059ff60 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059ffa0 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059ff60 bytes 683600d0
+ 0059ffa0 bytes 683600f0
- 0059ff64 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 0059ff64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059ff64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059ff64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059ffa4 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 0059ffa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ffa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ffa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059ff64 bytes 08a13c91
+ 0059ffa4 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-815d3ae678838d082d2dd4f7d38ede77"></a>

### [`0059ff70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff70.md) → [`0059ffb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059ffb0.md) FUN_0059ffb0

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
      "definition_site": "0059ffc0",
      "incomplete_value": false,
      "site": "0059ffc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ff80",
      "incomplete_value": false,
      "site": "0059ff88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "0059ffc8",
      "DATA",
      [
        "storage",
        "00c6df28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059ffc8",
      "DATA",
      [
        "storage",
        "00c6e328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ff7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff70.md#insn-0059ff7c) · [`0059ff80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff70.md#insn-0059ff80) · [`0059ff8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff70.md#insn-0059ff8c)
- 新版 `0059ffbc`（命令位置の公開資料なし） · `0059ffc0`（命令位置の公開資料なし） · `0059ffcc`（命令位置の公開資料なし）

~~~diff
- 0059ff7c ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059ffbc ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059ff7c bytes 683600d0
+ 0059ffbc bytes 683600f0
- 0059ff80 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 0059ff80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059ff80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059ff80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059ffc0 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 0059ffc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ffc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ffc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059ff80 bytes 08a13c91
+ 0059ffc0 bytes 08a10c91
- 0059ff8c ["INT_ADD", "register:40f0:8", ["const:59ff8c:8", "const:4:8"]]
- 0059ff8c ["CALL", null, ["callee:00c57ea0:8"]]
+ 0059ffcc ["INT_ADD", "register:40f0:8", ["const:59ffcc:8", "const:4:8"]]
+ 0059ffcc ["CALL", null, ["callee:00c57ea0:8"]]
- 0059ff8c bytes c5de1a94
+ 0059ffcc bytes b5df1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc2390561e1e66068b290595648c0559"></a>

### [`0059ffa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ffa8.md) → [`0059ffe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059ffe8.md) _INIT_43

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a0024",
      "incomplete_value": true,
      "site": "005a0040",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0059ffe4",
      "incomplete_value": true,
      "site": "005a0000",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "005a0048",
      "incomplete_value": true,
      "site": "005a0064",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "005a0008",
      "incomplete_value": true,
      "site": "005a0024",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
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
      "definition_site": "005a0088",
      "incomplete_value": true,
      "site": "005a00a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "005a0048",
      "incomplete_value": true,
      "site": "005a0060",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e95:8"
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
      "005a0024",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005a0048",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005a0068",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a0024",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a0048",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a0068",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ffa8.md#insn-005a0020) · [`005a0040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ffa8.md#insn-005a0040) · [`005a01dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ffa8.md#insn-005a01dc)
- 新版 `005a0060`（命令位置の公開資料なし） · `005a0080`（命令位置の公開資料なし） · `005a021c`（命令位置の公開資料なし）

~~~diff
- 005a0020 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005a0020 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a0020 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a0020 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a0060 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005a0060 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0060 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0060 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a0020 bytes 4a093691
+ 005a0060 bytes 4a093791
- 005a0040 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005a0040 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a0040 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a0040 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a0080 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005a0080 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0080 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0080 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a0040 bytes 4a553a91
+ 005a0080 bytes 4a893d91
- 005a01dc ["INT_ADD", "register:40f0:8", ["const:5a01dc:8", "const:4:8"]]
- 005a01dc ["CALL", null, ["callee:00c57e30:8"]]
+ 005a021c ["INT_ADD", "register:40f0:8", ["const:5a021c:8", "const:4:8"]]
+ 005a021c ["CALL", null, ["callee:00c57e30:8"]]
- 005a01dc bytes 15de1a94
+ 005a021c bytes 05df1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-981bd95593ccac4f1b939d8fd56a5839"></a>

### [`005a0338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0338.md) → [`005a0378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0378.md) FUN_005a0378

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a03c4",
      "incomplete_value": true,
      "site": "005a03c4",
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0384",
      "incomplete_value": true,
      "site": "005a0384",
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
                "const:165:8"
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
      "definition_site": "005a04e4",
      "incomplete_value": true,
      "site": "005a04e4",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:24b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a04a4",
      "incomplete_value": true,
      "site": "005a04a4",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:20b:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a0538",
      "incomplete_value": false,
      "site": "005a0544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a04f8",
      "incomplete_value": false,
      "site": "005a0504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a03a8",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "005a04d4",
      "READ",
      [
        "storage",
        "002b620b",
        null,
        "string"
      ]
    ],
    [
      "005a0544",
      "DATA",
      [
        "storage",
        "00c6e050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a03a8",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005a04d4",
      "READ",
      [
        "storage",
        "002b624b",
        null,
        "string"
      ]
    ],
    [
      "005a0544",
      "DATA",
      [
        "storage",
        "00c6e450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a03c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0338.md#insn-005a03c4) · [`005a04e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0338.md#insn-005a04e4) · [`005a035c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0338.md#insn-005a035c)
- 新版 `005a0404`（命令位置の公開資料なし） · `005a0524`（命令位置の公開資料なし） · `005a039c`（命令位置の公開資料なし）

~~~diff
- 005a03c4 ["INT_ADD", "register:40f0:8", ["const:5a03c4:8", "const:4:8"]]
- 005a03c4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a0404 ["INT_ADD", "register:40f0:8", ["const:5a0404:8", "const:4:8"]]
+ 005a0404 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a03c4 bytes bbdd1a94
+ 005a0404 bytes abde1a94
- 005a04e4 ["INT_ADD", "register:40f0:8", ["const:5a04e4:8", "const:4:8"]]
- 005a04e4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a0524 ["INT_ADD", "register:40f0:8", ["const:5a0524:8", "const:4:8"]]
+ 005a0524 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a04e4 bytes 73dd1a94
+ 005a0524 bytes 63de1a94
- 005a035c ["COPY", "tmp:0:8", ["const:165:8"]]
- 005a035c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a035c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a035c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a039c ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 005a039c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a039c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a039c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a035c bytes 4a950591
+ 005a039c bytes 4a950691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b5d2bd387e303e147ce90cc220f5918"></a>

### [`005a0628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0628.md) → [`005a0668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0668.md) FUN_005a0668

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b4550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4550.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)
- 新版 呼出元 1件 [`005b4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)

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
      "definition_site": "005a0684",
      "incomplete_value": false,
      "site": "005a0688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0644",
      "incomplete_value": false,
      "site": "005a0648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "005a0688",
      "DATA",
      [
        "storage",
        "00c6df98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a0688",
      "DATA",
      [
        "storage",
        "00c6e398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a063c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0628.md#insn-005a063c) · [`005a0640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0628.md#insn-005a0640) · [`005a0644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0628.md#insn-005a0644)
- 新版 `005a067c`（命令位置の公開資料なし） · `005a0680`（命令位置の公開資料なし） · `005a0684`（命令位置の公開資料なし）

~~~diff
- 005a063c ["INT_ADD", "register:40f0:8", ["const:5a063c:8", "const:4:8"]]
- 005a063c ["CALL", null, ["callee:0059b908:8"]]
+ 005a067c ["INT_ADD", "register:40f0:8", ["const:5a067c:8", "const:4:8"]]
+ 005a067c ["CALL", null, ["callee:0059b908:8"]]
- 005a063c bytes a3ecff97
+ 005a067c bytes a3ecff97
- 005a0640 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 005a0680 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005a0640 bytes 683600b0
+ 005a0680 bytes 683600d0
- 005a0644 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 005a0644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a0644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a0644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a0684 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 005a0684 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0684 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0684 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a0644 bytes 08613e91
+ 005a0684 bytes 08610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18fc40cceb72a0116403e697ce9a5a51"></a>

### [`005a06c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a06c4.md) → [`005a0704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0704.md) FUN_005a0704

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`005970d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`00597110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597110.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.18% / 新版 82.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a073c",
      "incomplete_value": false,
      "site": "005a0744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a06fc",
      "incomplete_value": false,
      "site": "005a0704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a0764",
      "incomplete_value": false,
      "site": "005a0764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0724",
      "incomplete_value": false,
      "site": "005a0724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "005a0798",
      "incomplete_value": true,
      "site": "005a0798",
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
    "old": {
      "definition_site": "005a0758",
      "incomplete_value": true,
      "site": "005a0758",
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
                "const:8ce:8"
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
      "005a0744",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ],
    [
      "005a0764",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ],
    [
      "005a0780",
      "READ",
      [
        "storage",
        "002b38ce",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a0744",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "005a0764",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "005a0780",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a06c4.md#insn-005a0718) · [`005a0764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a06c4.md#insn-005a0764) · [`005a0798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a06c4.md#insn-005a0798)
- 新版 `005a0758`（命令位置の公開資料なし） · `005a07a4`（命令位置の公開資料なし） · `005a07d8`（命令位置の公開資料なし）

~~~diff
- 005a0718 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 005a0718 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a0718 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a0718 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a0758 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005a0758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a0718 bytes 08811b91
+ 005a0758 bytes 08812b91
- 005a0764 ["INT_ADD", "register:40f0:8", ["const:5a0764:8", "const:4:8"]]
- 005a0764 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a07a4 ["INT_ADD", "register:40f0:8", ["const:5a07a4:8", "const:4:8"]]
+ 005a07a4 ["CALL", null, ["callee:00c57e90:8"]]
- 005a0764 bytes cbdc1a94
+ 005a07a4 bytes bbdd1a94
- 005a0798 ["INT_ADD", "register:40f0:8", ["const:5a0798:8", "const:4:8"]]
- 005a0798 ["CALL", null, ["callee:0045982c:8"]]
+ 005a07d8 ["INT_ADD", "register:40f0:8", ["const:5a07d8:8", "const:4:8"]]
+ 005a07d8 ["CALL", null, ["callee:0045982c:8"]]
- 005a0798 bytes 15e4fa97
+ 005a07d8 bytes 15e4fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f12381c18c3667a0aa5e2758592983e2"></a>

### [`005a08cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a08cc.md) → [`005a090c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a090c.md) FUN_005a090c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005a0928",
      "incomplete_value": false,
      "site": "005a0930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a08e8",
      "incomplete_value": false,
      "site": "005a08f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a0:8"
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
      "definition_site": "005a0940",
      "incomplete_value": false,
      "site": "005a0940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0900",
      "incomplete_value": false,
      "site": "005a0900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
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
      "005a0930",
      "DATA",
      [
        "storage",
        "00c6e0a0",
        null,
        "undefined *"
      ]
    ],
    [
      "005a0940",
      "DATA",
      [
        "storage",
        "00c6dff0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a0930",
      "DATA",
      [
        "storage",
        "00c6e4a0",
        null,
        "undefined *"
      ]
    ],
    [
      "005a0940",
      "DATA",
      [
        "storage",
        "00c6e3f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a08e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a08cc.md#insn-005a08e0) · [`005a08e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a08cc.md#insn-005a08e8) · [`005a08f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a08cc.md#insn-005a08f4)
- 新版 `005a0920`（命令位置の公開資料なし） · `005a0928`（命令位置の公開資料なし）

~~~diff
- 005a08e0 ["INT_ADD", "register:40f0:8", ["const:5a08e0:8", "const:4:8"]]
- 005a08e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a0920 ["INT_ADD", "register:40f0:8", ["const:5a0920:8", "const:4:8"]]
+ 005a0920 ["CALL", null, ["callee:00c57e90:8"]]
- 005a08e0 bytes 6cdc1a94
+ 005a0920 bytes 5cdd1a94
- 005a08e8 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 005a08e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a08e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a08e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a0928 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 005a0928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a08e8 bytes 08810291
+ 005a0928 bytes 08811291
- 005a08f4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005a08f4 bytes 683600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f57472ee8fa1a1473873884663bed5c"></a>

### [`005a0914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0914.md) → [`005a0954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0954.md) FUN_005a0954

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
      "definition_site": "005a0980",
      "incomplete_value": false,
      "site": "005a0984",
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
      "definition_site": "005a0940",
      "incomplete_value": false,
      "site": "005a0944",
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
      "005a0984",
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
      "005a0984",
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

- 旧版 [`005a0930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0914.md#insn-005a0930) · [`005a0938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0914.md#insn-005a0938) · [`005a0950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0914.md#insn-005a0950)
- 新版 `005a0970`（命令位置の公開資料なし） · `005a0978`（命令位置の公開資料なし） · `005a0990`（命令位置の公開資料なし）

~~~diff
- 005a0930 ["INT_ADD", "register:40f0:8", ["const:5a0930:8", "const:4:8"]]
- 005a0930 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a0970 ["INT_ADD", "register:40f0:8", ["const:5a0970:8", "const:4:8"]]
+ 005a0970 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a0930 bytes 60dc1a94
+ 005a0970 bytes 50dd1a94
- 005a0938 ["COPY", "tmp:0:8", ["const:610:8"]]
- 005a0938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a0938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a0938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a0978 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005a0978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a0938 bytes 08411891
+ 005a0978 bytes 08412891
- 005a0950 ["INT_ADD", "register:40f0:8", ["const:5a0950:8", "const:4:8"]]
- 005a0950 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a0990 ["INT_ADD", "register:40f0:8", ["const:5a0990:8", "const:4:8"]]
+ 005a0990 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a0950 bytes 58dc1a94
+ 005a0990 bytes 48dd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c65a697bb054d0617b8fa4670bebd45"></a>

### [`005a0978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0978.md) → [`005a09b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a09b8.md) FUN_005a09b8

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
      "definition_site": "005a09e4",
      "incomplete_value": false,
      "site": "005a09e8",
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
      "definition_site": "005a09a4",
      "incomplete_value": false,
      "site": "005a09a8",
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
      "005a09e8",
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
      "005a09e8",
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

- 旧版 [`005a0994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0978.md#insn-005a0994) · [`005a099c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0978.md#insn-005a099c) · [`005a09b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0978.md#insn-005a09b4)
- 新版 `005a09d4`（命令位置の公開資料なし） · `005a09dc`（命令位置の公開資料なし） · `005a09f4`（命令位置の公開資料なし）

~~~diff
- 005a0994 ["INT_ADD", "register:40f0:8", ["const:5a0994:8", "const:4:8"]]
- 005a0994 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a09d4 ["INT_ADD", "register:40f0:8", ["const:5a09d4:8", "const:4:8"]]
+ 005a09d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a0994 bytes 47dc1a94
+ 005a09d4 bytes 37dd1a94
- 005a099c ["COPY", "tmp:0:8", ["const:610:8"]]
- 005a099c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a099c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a099c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a09dc ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005a09dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a09dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a09dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a099c bytes 08411891
+ 005a09dc bytes 08412891
- 005a09b4 ["INT_ADD", "register:40f0:8", ["const:5a09b4:8", "const:4:8"]]
- 005a09b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a09f4 ["INT_ADD", "register:40f0:8", ["const:5a09f4:8", "const:4:8"]]
+ 005a09f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a09b4 bytes 3fdc1a94
+ 005a09f4 bytes 2fdd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f443e8d1883190fa805196201f778c9a"></a>

### [`005a09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a09d8.md) → [`005a0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a18.md) FUN_005a0a18

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
      "definition_site": "005a0a20",
      "incomplete_value": false,
      "site": "005a0a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a09e0",
      "incomplete_value": false,
      "site": "005a09e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a0a24",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a0a24",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a09e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a09d8.md#insn-005a09e0) · [`005a0a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a09d8.md#insn-005a0a04)
- 新版 `005a0a20`（命令位置の公開資料なし） · `005a0a44`（命令位置の公開資料なし）

~~~diff
- 005a09e0 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a09e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a09e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a09e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a0a20 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a0a20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a0a20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a0a20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a09e0 bytes 29011891
+ 005a0a20 bytes 29012891
- 005a0a04 ["INT_ADD", "register:40f0:8", ["const:5a0a04:8", "const:4:8"]]
- 005a0a04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a0a44 ["INT_ADD", "register:40f0:8", ["const:5a0a44:8", "const:4:8"]]
+ 005a0a44 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a0a04 bytes 2bdc1a94
+ 005a0a44 bytes 1bdd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-517b3f48d1b23a3608e487ad8ab6fddf"></a>

### [`005a0a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a18.md) → [`005a0a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a58.md) FUN_005a0a58

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
      "definition_site": "005a0a5c",
      "incomplete_value": false,
      "site": "005a0a60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0a1c",
      "incomplete_value": false,
      "site": "005a0a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:50:8"
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
      "005a0a60",
      "DATA",
      [
        "storage",
        "00c6e050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a0a60",
      "DATA",
      [
        "storage",
        "00c6e450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a18.md#insn-005a0a1c)
- 新版 `005a0a5c`（命令位置の公開資料なし）

~~~diff
- 005a0a1c ["COPY", "tmp:0:8", ["const:50:8"]]
- 005a0a1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a0a1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a0a1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a0a5c ["COPY", "tmp:0:8", ["const:450:8"]]
+ 005a0a5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0a5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0a5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a0a1c bytes 08410191
+ 005a0a5c bytes 08411191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0aadefe7159ccb713e1df113f33c877"></a>

### [`005a0a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a28.md) → [`005a0a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a68.md) FUN_005a0a68

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
      "definition_site": "005a0a78",
      "incomplete_value": false,
      "site": "005a0a80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0a38",
      "incomplete_value": false,
      "site": "005a0a40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:50:8"
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
      "005a0a80",
      "DATA",
      [
        "storage",
        "00c6e050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a0a80",
      "DATA",
      [
        "storage",
        "00c6e450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a28.md#insn-005a0a38) · [`005a0a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a28.md#insn-005a0a44)
- 新版 `005a0a78`（命令位置の公開資料なし） · `005a0a84`（命令位置の公開資料なし）

~~~diff
- 005a0a38 ["COPY", "tmp:0:8", ["const:50:8"]]
- 005a0a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a0a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a0a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a0a78 ["COPY", "tmp:0:8", ["const:450:8"]]
+ 005a0a78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0a78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0a78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a0a38 bytes 08410191
+ 005a0a78 bytes 08411191
- 005a0a44 ["INT_ADD", "register:40f0:8", ["const:5a0a44:8", "const:4:8"]]
- 005a0a44 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a0a84 ["INT_ADD", "register:40f0:8", ["const:5a0a84:8", "const:4:8"]]
+ 005a0a84 ["CALL", null, ["callee:00c57ea0:8"]]
- 005a0a44 bytes 17dc1a94
+ 005a0a84 bytes 07dd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4e5166ca67ef98b492240c3e49f7c9f"></a>

### [`005a0a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a58.md) → [`005a0a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a98.md) FUN_005a0a98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005a0aa0",
      "incomplete_value": false,
      "site": "005a0aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0a60",
      "incomplete_value": false,
      "site": "005a0a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a0aa4",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a0aa4",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a58.md#insn-005a0a60)
- 新版 `005a0aa0`（命令位置の公開資料なし）

~~~diff
- 005a0a60 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a0a60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a0a60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a0a60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a0aa0 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a0aa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a0aa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a0aa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a0a60 bytes 29011891
+ 005a0aa0 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4a3a600c155ebfeef1f2228c1b0ad6b"></a>

### [`005a0a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a7c.md) → [`005a0abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0abc.md) FUN_005a0abc

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
      "definition_site": "005a0ac0",
      "incomplete_value": false,
      "site": "005a0ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0a80",
      "incomplete_value": false,
      "site": "005a0a84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a0ac4",
      "DATA",
      [
        "storage",
        "00c6e0a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a0ac4",
      "DATA",
      [
        "storage",
        "00c6e4a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a7c.md#insn-005a0a80)
- 新版 `005a0ac0`（命令位置の公開資料なし）

~~~diff
- 005a0a80 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 005a0a80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a0a80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a0a80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a0ac0 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 005a0ac0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0ac0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0ac0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a0a80 bytes 08810291
+ 005a0ac0 bytes 08811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcbd2308522d576292d1a2e99f994a76"></a>

### [`005a0a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a8c.md) → [`005a0acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0acc.md) FUN_005a0acc

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
      "definition_site": "005a0adc",
      "incomplete_value": false,
      "site": "005a0ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0a9c",
      "incomplete_value": false,
      "site": "005a0aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a0ae4",
      "DATA",
      [
        "storage",
        "00c6e0a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a0ae4",
      "DATA",
      [
        "storage",
        "00c6e4a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a8c.md#insn-005a0a9c) · [`005a0aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a8c.md#insn-005a0aa8)
- 新版 `005a0adc`（命令位置の公開資料なし） · `005a0ae8`（命令位置の公開資料なし）

~~~diff
- 005a0a9c ["COPY", "tmp:0:8", ["const:a0:8"]]
- 005a0a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a0a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a0a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a0adc ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 005a0adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a0a9c bytes 08810291
+ 005a0adc bytes 08811291
- 005a0aa8 ["INT_ADD", "register:40f0:8", ["const:5a0aa8:8", "const:4:8"]]
- 005a0aa8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a0ae8 ["INT_ADD", "register:40f0:8", ["const:5a0ae8:8", "const:4:8"]]
+ 005a0ae8 ["CALL", null, ["callee:00c57ea0:8"]]
- 005a0aa8 bytes fedb1a94
+ 005a0ae8 bytes eedc1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e45c134ae6eada0d7dfcb40814404b84"></a>

### [`005a0ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0ac4.md) → [`005a0b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0b04.md) _INIT_44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a0b40",
      "incomplete_value": true,
      "site": "005a0b5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "005a0b00",
      "incomplete_value": true,
      "site": "005a0b1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "005a0b64",
      "incomplete_value": true,
      "site": "005a0b80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "005a0b24",
      "incomplete_value": true,
      "site": "005a0b40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
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
      "definition_site": "005a0b84",
      "incomplete_value": true,
      "site": "005a0ba0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "005a0b44",
      "incomplete_value": true,
      "site": "005a0b60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d82:8"
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
      "005a0b40",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005a0b64",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005a0b84",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a0b40",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a0b64",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a0b84",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0ac4.md#insn-005a0b3c) · [`005a0b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0ac4.md#insn-005a0b5c) · [`005a0cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0ac4.md#insn-005a0cf8)
- 新版 `005a0b7c`（命令位置の公開資料なし） · `005a0b9c`（命令位置の公開資料なし） · `005a0d38`（命令位置の公開資料なし）

~~~diff
- 005a0b3c ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005a0b3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a0b3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a0b3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a0b7c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005a0b7c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0b7c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0b7c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a0b3c bytes 4a093691
+ 005a0b7c bytes 4a093791
- 005a0b5c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005a0b5c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a0b5c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a0b5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a0b9c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005a0b9c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0b9c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0b9c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a0b5c bytes 4a553a91
+ 005a0b9c bytes 4a893d91
- 005a0cf8 ["INT_ADD", "register:40f0:8", ["const:5a0cf8:8", "const:4:8"]]
- 005a0cf8 ["CALL", null, ["callee:00c57e30:8"]]
+ 005a0d38 ["INT_ADD", "register:40f0:8", ["const:5a0d38:8", "const:4:8"]]
+ 005a0d38 ["CALL", null, ["callee:00c57e30:8"]]
- 005a0cf8 bytes 4edb1a94
+ 005a0d38 bytes 3edc1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-440a2c0bcdeeeb8b5ce59c8ac5a54068"></a>

### [`005a0e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0e54.md) → [`005a0e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0e94.md) FUN_005a0e94

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005a1b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1b40.md) [`005a1da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1da0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005a1b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b80.md) [`005a1de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1de0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.66% / 新版 97.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a0ee8",
      "incomplete_value": true,
      "site": "005a0ee8",
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0ea8",
      "incomplete_value": true,
      "site": "005a0ea8",
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
                "const:165:8"
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
      "definition_site": "005a1004",
      "incomplete_value": true,
      "site": "005a1010",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0fc4",
      "incomplete_value": true,
      "site": "005a0fd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4b0:8"
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
      "005a0ecc",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "005a1004",
      "READ",
      [
        "storage",
        "002b74b0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a0ecc",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005a1004",
      "READ",
      [
        "storage",
        "002b74f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0e54.md#insn-005a0ee8) · [`005a0e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0e54.md#insn-005a0e80) · [`005a0eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0e54.md#insn-005a0eb8)
- 新版 `005a0f28`（命令位置の公開資料なし） · `005a0ec0`（命令位置の公開資料なし） · `005a0ef8`（命令位置の公開資料なし）

~~~diff
- 005a0ee8 ["INT_ADD", "register:40f0:8", ["const:5a0ee8:8", "const:4:8"]]
- 005a0ee8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a0f28 ["INT_ADD", "register:40f0:8", ["const:5a0f28:8", "const:4:8"]]
+ 005a0f28 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a0ee8 bytes f2da1a94
+ 005a0f28 bytes e2db1a94
- 005a0e80 ["COPY", "tmp:0:8", ["const:165:8"]]
- 005a0e80 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a0e80 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a0e80 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a0ec0 ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 005a0ec0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0ec0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0ec0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a0e80 bytes 4a950591
+ 005a0ec0 bytes 4a950691
- 005a0eb8 ["INT_ADD", "register:40f0:8", ["const:5a0eb8:8", "const:4:8"]]
- 005a0eb8 ["CALL", null, ["callee:0044108c:8"]]
+ 005a0ef8 ["INT_ADD", "register:40f0:8", ["const:5a0ef8:8", "const:4:8"]]
+ 005a0ef8 ["CALL", null, ["callee:0044108c:8"]]
- 005a0eb8 bytes 6580fa97
+ 005a0ef8 bytes 6580fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e06c5d3d5dca64c33e15ecd234c3bba"></a>

### [`005a138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a138c.md) → [`005a13cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a13cc.md) FUN_005a13cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0079c82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079c82c.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)
- 新版 呼出元 1件 [`0079c86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c86c.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)

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
      "definition_site": "005a13ec",
      "incomplete_value": false,
      "site": "005a13f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a13ac",
      "incomplete_value": false,
      "site": "005a13b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "005a13f8",
      "DATA",
      [
        "storage",
        "00c6e110",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a13f8",
      "DATA",
      [
        "storage",
        "00c6e510",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a13a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a138c.md#insn-005a13a0) · [`005a13ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a138c.md#insn-005a13ac)
- 新版 `005a13e0`（命令位置の公開資料なし） · `005a13ec`（命令位置の公開資料なし）

~~~diff
- 005a13a0 ["INT_ADD", "register:40f0:8", ["const:5a13a0:8", "const:4:8"]]
- 005a13a0 ["CALL", null, ["callee:0059b908:8"]]
+ 005a13e0 ["INT_ADD", "register:40f0:8", ["const:5a13e0:8", "const:4:8"]]
+ 005a13e0 ["CALL", null, ["callee:0059b908:8"]]
- 005a13a0 bytes 4ae9ff97
+ 005a13e0 bytes 4ae9ff97
- 005a13ac ["COPY", "tmp:0:8", ["const:110:8"]]
- 005a13ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a13ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a13ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a13ec ["COPY", "tmp:0:8", ["const:510:8"]]
+ 005a13ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a13ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a13ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a13ac bytes 29410491
+ 005a13ec bytes 29411491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb53fb9cd699f920969519d644118624"></a>

### [`005a1430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1430.md) → [`005a1470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1470.md) FUN_005a1470

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004593b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md) [`00459a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459a90.md) [`0059715c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059715c.md) [`005974c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005974c4.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004593f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md) [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md) [`0059719c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059719c.md) [`00597504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597504.md)

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
      "definition_site": "005a14c0",
      "incomplete_value": false,
      "site": "005a14c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1480",
      "incomplete_value": false,
      "site": "005a1484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "005a14c4",
      "DATA",
      [
        "storage",
        "00c6d278",
        null,
        "pointer"
      ]
    ],
    [
      "005a1534",
      "DATA",
      [
        "storage",
        "00c63360",
        null,
        "pointer"
      ]
    ],
    [
      "005a157c",
      "READ",
      [
        "storage",
        "00c63368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a14c4",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ],
    [
      "005a1534",
      "DATA",
      [
        "storage",
        "00c63760",
        null,
        "pointer"
      ]
    ],
    [
      "005a157c",
      "READ",
      [
        "storage",
        "00c63768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1430.md#insn-005a1464) · [`005a146c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1430.md#insn-005a146c) · [`005a1480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1430.md#insn-005a1480)
- 新版 `005a14a4`（命令位置の公開資料なし） · `005a14ac`（命令位置の公開資料なし） · `005a14c0`（命令位置の公開資料なし）

~~~diff
- 005a1464 ["INT_ADD", "register:40f0:8", ["const:5a1464:8", "const:4:8"]]
- 005a1464 ["CALL", null, ["callee:0059bf44:8"]]
+ 005a14a4 ["INT_ADD", "register:40f0:8", ["const:5a14a4:8", "const:4:8"]]
+ 005a14a4 ["CALL", null, ["callee:0059bf44:8"]]
- 005a1464 bytes a8eaff97
+ 005a14a4 bytes a8eaff97
- 005a146c ["INT_ADD", "register:40f0:8", ["const:5a146c:8", "const:4:8"]]
- 005a146c ["CALL", null, ["callee:00c57e90:8"]]
+ 005a14ac ["INT_ADD", "register:40f0:8", ["const:5a14ac:8", "const:4:8"]]
+ 005a14ac ["CALL", null, ["callee:00c57e90:8"]]
- 005a146c bytes 89d91a94
+ 005a14ac bytes 79da1a94
- 005a1480 ["COPY", "tmp:0:8", ["const:278:8"]]
- 005a1480 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a1480 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a1480 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a14c0 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 005a14c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a14c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a14c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a1480 bytes 29e10991
+ 005a14c0 bytes 29e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f8a76cd43ef97760573cadff86b0d99"></a>

### [`005a16a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a16a0.md) → [`005a16e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a16e0.md) FUN_005a16e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005a16fc",
      "incomplete_value": false,
      "site": "005a1704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a16bc",
      "incomplete_value": false,
      "site": "005a16c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      "definition_site": "005a1714",
      "incomplete_value": false,
      "site": "005a1714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a16d4",
      "incomplete_value": false,
      "site": "005a16d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:168:8"
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
      "005a1704",
      "DATA",
      [
        "storage",
        "00c6e218",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1714",
      "DATA",
      [
        "storage",
        "00c6e168",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a1704",
      "DATA",
      [
        "storage",
        "00c6e618",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1714",
      "DATA",
      [
        "storage",
        "00c6e568",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a16b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a16a0.md#insn-005a16b4) · [`005a16bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a16a0.md#insn-005a16bc) · [`005a16c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a16a0.md#insn-005a16c8)
- 新版 `005a16f4`（命令位置の公開資料なし） · `005a16fc`（命令位置の公開資料なし）

~~~diff
- 005a16b4 ["INT_ADD", "register:40f0:8", ["const:5a16b4:8", "const:4:8"]]
- 005a16b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a16f4 ["INT_ADD", "register:40f0:8", ["const:5a16f4:8", "const:4:8"]]
+ 005a16f4 ["CALL", null, ["callee:00c57e90:8"]]
- 005a16b4 bytes f7d81a94
+ 005a16f4 bytes e7d91a94
- 005a16bc ["COPY", "tmp:0:8", ["const:218:8"]]
- 005a16bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a16bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a16bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a16fc ["COPY", "tmp:0:8", ["const:618:8"]]
+ 005a16fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a16fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a16fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a16bc bytes 08610891
+ 005a16fc bytes 08611891
- 005a16c8 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005a16c8 bytes 683600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5de6417e575fde1f2835908731b18dd5"></a>

### [`005a16e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a16e8.md) → [`005a1728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1728.md) FUN_005a1728

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`005a1794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1794.md) [`0079bdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079bdc8.md) [`0079c940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079c940.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`005a17d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a17d4.md) [`0079be08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079be08.md) [`0079c980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c980.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "005a1794",
      "incomplete_value": false,
      "site": "005a1798",
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
      "definition_site": "005a1754",
      "incomplete_value": false,
      "site": "005a1758",
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
      "005a1798",
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
      "005a1798",
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

- 旧版 [`005a1734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a16e8.md#insn-005a1734) · [`005a1744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a16e8.md#insn-005a1744) · [`005a174c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a16e8.md#insn-005a174c)
- 新版 `005a1774`（命令位置の公開資料なし） · `005a1784`（命令位置の公開資料なし） · `005a178c`（命令位置の公開資料なし）

~~~diff
- 005a1734 ["INT_ADD", "register:40f0:8", ["const:5a1734:8", "const:4:8"]]
- 005a1734 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a1774 ["INT_ADD", "register:40f0:8", ["const:5a1774:8", "const:4:8"]]
+ 005a1774 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a1734 bytes dfd81a94
+ 005a1774 bytes cfd91a94
- 005a1744 ["INT_ADD", "register:40f0:8", ["const:5a1744:8", "const:4:8"]]
- 005a1744 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a1784 ["INT_ADD", "register:40f0:8", ["const:5a1784:8", "const:4:8"]]
+ 005a1784 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a1744 bytes dbd81a94
+ 005a1784 bytes cbd91a94
- 005a174c ["COPY", "tmp:0:8", ["const:610:8"]]
- 005a174c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a174c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a174c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a178c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005a178c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a178c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a178c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a174c bytes 08411891
+ 005a178c bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3042c49ac4b4b53932a71f4555828ec7"></a>

### [`005a17b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a17b8.md) → [`005a17f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a17f8.md) FUN_005a17f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a1860",
      "incomplete_value": false,
      "site": "005a1864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1820",
      "incomplete_value": false,
      "site": "005a1824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "005a1864",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a1864",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a17b8.md#insn-005a1804) · [`005a1814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a17b8.md#insn-005a1814) · [`005a1820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a17b8.md#insn-005a1820)
- 新版 `005a1844`（命令位置の公開資料なし） · `005a1854`（命令位置の公開資料なし） · `005a1860`（命令位置の公開資料なし）

~~~diff
- 005a1804 ["INT_ADD", "register:40f0:8", ["const:5a1804:8", "const:4:8"]]
- 005a1804 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a1844 ["INT_ADD", "register:40f0:8", ["const:5a1844:8", "const:4:8"]]
+ 005a1844 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a1804 bytes abd81a94
+ 005a1844 bytes 9bd91a94
- 005a1814 ["INT_ADD", "register:40f0:8", ["const:5a1814:8", "const:4:8"]]
- 005a1814 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a1854 ["INT_ADD", "register:40f0:8", ["const:5a1854:8", "const:4:8"]]
+ 005a1854 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a1814 bytes a7d81a94
+ 005a1854 bytes 97d91a94
- 005a1820 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a1820 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a1820 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a1820 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a1860 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a1860 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1860 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1860 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a1820 bytes 29011891
+ 005a1860 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1295a2d0eb34da5f1d6983fc4c470fb8"></a>

### [`005a1850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1850.md) → [`005a1890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1890.md) FUN_005a1890

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005a18f8",
      "incomplete_value": false,
      "site": "005a18fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a18b8",
      "incomplete_value": false,
      "site": "005a18bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "005a18fc",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a18fc",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a189c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1850.md#insn-005a189c) · [`005a18ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1850.md#insn-005a18ac) · [`005a18b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1850.md#insn-005a18b8)
- 新版 `005a18dc`（命令位置の公開資料なし） · `005a18ec`（命令位置の公開資料なし） · `005a18f8`（命令位置の公開資料なし）

~~~diff
- 005a189c ["INT_ADD", "register:40f0:8", ["const:5a189c:8", "const:4:8"]]
- 005a189c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a18dc ["INT_ADD", "register:40f0:8", ["const:5a18dc:8", "const:4:8"]]
+ 005a18dc ["CALL", null, ["callee:00c57eb0:8"]]
- 005a189c bytes 85d81a94
+ 005a18dc bytes 75d91a94
- 005a18ac ["INT_ADD", "register:40f0:8", ["const:5a18ac:8", "const:4:8"]]
- 005a18ac ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a18ec ["INT_ADD", "register:40f0:8", ["const:5a18ec:8", "const:4:8"]]
+ 005a18ec ["CALL", null, ["callee:00c57eb0:8"]]
- 005a18ac bytes 81d81a94
+ 005a18ec bytes 71d91a94
- 005a18b8 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a18b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a18b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a18b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a18f8 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a18f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a18f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a18f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a18b8 bytes 29011891
+ 005a18f8 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d02d2b9a7daa626e4c0f398b5b528ad1"></a>

### [`005a1acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1acc.md) → [`005a1b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b0c.md) FUN_005a1b0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a18e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a18e0.md) [`005a1b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1b40.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`005a1920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1920.md) [`005a1b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b80.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005a1b18",
      "incomplete_value": false,
      "site": "005a1b1c",
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
    "old": {
      "definition_site": "005a1ad8",
      "incomplete_value": false,
      "site": "005a1adc",
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
            "const:f0c:8"
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
      "005a1b18",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a1b18",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1acc.md#insn-005a1adc) · [`005a1ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1acc.md#insn-005a1ad8)
- 新版 `005a1b1c`（命令位置の公開資料なし） · `005a1b18`（命令位置の公開資料なし）

~~~diff
- 005a1adc ["INT_ADD", "register:40f0:8", ["const:5a1adc:8", "const:4:8"]]
- 005a1adc ["CALL", null, ["callee:0043b778:8"]]
+ 005a1b1c ["INT_ADD", "register:40f0:8", ["const:5a1b1c:8", "const:4:8"]]
+ 005a1b1c ["CALL", null, ["callee:0043b778:8"]]
- 005a1adc bytes 1767fa97
+ 005a1b1c bytes 1767fa97
- 005a1ad8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005a1ad8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005a1ad8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005a1ad8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005a1b18 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005a1b18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005a1b18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005a1b18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005a1ad8 bytes 00303c91
+ 005a1b18 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f47ebe749f3ac9144276fc1b3cb52cf"></a>

### [`005a1da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1da0.md) → [`005a1de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1de0.md) FUN_005a1de0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005a0e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0e54.md) · 呼出先 3件 [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`005a18e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a18e0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005a0e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0e94.md) · 呼出先 3件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`005a1920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1920.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a1e18",
      "incomplete_value": false,
      "site": "005a1e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1dd8",
      "incomplete_value": false,
      "site": "005a1de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a1e60",
      "incomplete_value": false,
      "site": "005a1e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1e20",
      "incomplete_value": false,
      "site": "005a1e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
      "005a1e24",
      "DATA",
      [
        "storage",
        "00c6e1c8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1e60",
      "DATA",
      [
        "storage",
        "00c6e0f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a1e24",
      "DATA",
      [
        "storage",
        "00c6e5c8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1e60",
      "DATA",
      [
        "storage",
        "00c6e4f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1da0.md#insn-005a1e24) · [`005a1dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1da0.md#insn-005a1dc8) · [`005a1dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1da0.md#insn-005a1dd8)
- 新版 `005a1e64`（命令位置の公開資料なし） · `005a1e08`（命令位置の公開資料なし） · `005a1e18`（命令位置の公開資料なし）

~~~diff
- 005a1e24 ["INT_ADD", "register:40f0:8", ["const:5a1e24:8", "const:4:8"]]
- 005a1e24 ["CALL", null, ["callee:005a1920:8"]]
+ 005a1e64 ["INT_ADD", "register:40f0:8", ["const:5a1e64:8", "const:4:8"]]
+ 005a1e64 ["CALL", null, ["callee:005a1920:8"]]
- 005a1e24 bytes affeff97
+ 005a1e64 bytes affeff97
- 005a1dc8 ["INT_ADD", "register:40f0:8", ["const:5a1dc8:8", "const:4:8"]]
- 005a1dc8 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a1e08 ["INT_ADD", "register:40f0:8", ["const:5a1e08:8", "const:4:8"]]
+ 005a1e08 ["CALL", null, ["callee:00c57e90:8"]]
- 005a1dc8 bytes 32d71a94
+ 005a1e08 bytes 22d81a94
- 005a1dd8 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 005a1dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1e18 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 005a1e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1dd8 bytes 08210791
+ 005a1e18 bytes 08211791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2efdbf6a568a75e7cec06e227684995b"></a>

### [`005a1e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1e80.md) → [`005a1ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1ec0.md) FUN_005a1ec0

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
      "definition_site": "005a1ec4",
      "incomplete_value": false,
      "site": "005a1ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1e84",
      "incomplete_value": false,
      "site": "005a1e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
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
      "005a1ec8",
      "DATA",
      [
        "storage",
        "00c6e1c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a1ec8",
      "DATA",
      [
        "storage",
        "00c6e5c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1e80.md#insn-005a1e84)
- 新版 `005a1ec4`（命令位置の公開資料なし）

~~~diff
- 005a1e84 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 005a1e84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1e84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1e84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1ec4 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 005a1ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1e84 bytes 08210791
+ 005a1ec4 bytes 08211791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-170186d230e64f0a114e1b58361f51b1"></a>

### [`005a1e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1e90.md) → [`005a1ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1ed0.md) FUN_005a1ed0

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
      "definition_site": "005a1ee0",
      "incomplete_value": false,
      "site": "005a1ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1ea0",
      "incomplete_value": false,
      "site": "005a1ea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
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
      "005a1ee8",
      "DATA",
      [
        "storage",
        "00c6e1c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a1ee8",
      "DATA",
      [
        "storage",
        "00c6e5c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1e90.md#insn-005a1ea0) · [`005a1eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1e90.md#insn-005a1eac)
- 新版 `005a1ee0`（命令位置の公開資料なし） · `005a1eec`（命令位置の公開資料なし）

~~~diff
- 005a1ea0 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 005a1ea0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1ea0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1ea0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1ee0 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 005a1ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1ea0 bytes 08210791
+ 005a1ee0 bytes 08211791
- 005a1eac ["INT_ADD", "register:40f0:8", ["const:5a1eac:8", "const:4:8"]]
- 005a1eac ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a1eec ["INT_ADD", "register:40f0:8", ["const:5a1eec:8", "const:4:8"]]
+ 005a1eec ["CALL", null, ["callee:00c57ea0:8"]]
- 005a1eac bytes fdd61a94
+ 005a1eec bytes edd71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df8af4bc791e0601adcab3fc6b723d69"></a>

### [`005a1ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1ec0.md) → [`005a1f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1f00.md) FUN_005a1f00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a1f68",
      "incomplete_value": false,
      "site": "005a1f6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1f28",
      "incomplete_value": false,
      "site": "005a1f2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "005a1f6c",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a1f6c",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1ec0.md#insn-005a1f0c) · [`005a1f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1ec0.md#insn-005a1f1c) · [`005a1f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1ec0.md#insn-005a1f28)
- 新版 `005a1f4c`（命令位置の公開資料なし） · `005a1f5c`（命令位置の公開資料なし） · `005a1f68`（命令位置の公開資料なし）

~~~diff
- 005a1f0c ["INT_ADD", "register:40f0:8", ["const:5a1f0c:8", "const:4:8"]]
- 005a1f0c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a1f4c ["INT_ADD", "register:40f0:8", ["const:5a1f4c:8", "const:4:8"]]
+ 005a1f4c ["CALL", null, ["callee:00c57eb0:8"]]
- 005a1f0c bytes e9d61a94
+ 005a1f4c bytes d9d71a94
- 005a1f1c ["INT_ADD", "register:40f0:8", ["const:5a1f1c:8", "const:4:8"]]
- 005a1f1c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a1f5c ["INT_ADD", "register:40f0:8", ["const:5a1f5c:8", "const:4:8"]]
+ 005a1f5c ["CALL", null, ["callee:00c57eb0:8"]]
- 005a1f1c bytes e5d61a94
+ 005a1f5c bytes d5d71a94
- 005a1f28 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a1f28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a1f28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a1f28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a1f68 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a1f68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1f68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1f68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a1f28 bytes 29011891
+ 005a1f68 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2adb29ce98bcafdc51fc689766582fa8"></a>

### [`005a1f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1f5c.md) → [`005a1f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1f9c.md) FUN_005a1f9c

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
      "definition_site": "005a1fa0",
      "incomplete_value": false,
      "site": "005a1fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1f60",
      "incomplete_value": false,
      "site": "005a1f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      "005a1fa4",
      "DATA",
      [
        "storage",
        "00c6e218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a1fa4",
      "DATA",
      [
        "storage",
        "00c6e618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1f5c.md#insn-005a1f60)
- 新版 `005a1fa0`（命令位置の公開資料なし）

~~~diff
- 005a1f60 ["COPY", "tmp:0:8", ["const:218:8"]]
- 005a1f60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1f60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1f60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1fa0 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 005a1fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1f60 bytes 08610891
+ 005a1fa0 bytes 08611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e6bfa799462346dd9c7413eaa9bd162"></a>

### [`005a1f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1f6c.md) → [`005a1fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1fac.md) FUN_005a1fac

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
      "definition_site": "005a1fbc",
      "incomplete_value": false,
      "site": "005a1fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1f7c",
      "incomplete_value": false,
      "site": "005a1f84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      "005a1fc4",
      "DATA",
      [
        "storage",
        "00c6e218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a1fc4",
      "DATA",
      [
        "storage",
        "00c6e618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1f6c.md#insn-005a1f7c) · [`005a1f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1f6c.md#insn-005a1f88)
- 新版 `005a1fbc`（命令位置の公開資料なし） · `005a1fc8`（命令位置の公開資料なし）

~~~diff
- 005a1f7c ["COPY", "tmp:0:8", ["const:218:8"]]
- 005a1f7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1f7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1f7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1fbc ["COPY", "tmp:0:8", ["const:618:8"]]
+ 005a1fbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1fbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1fbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1f7c bytes 08610891
+ 005a1fbc bytes 08611891
- 005a1f88 ["INT_ADD", "register:40f0:8", ["const:5a1f88:8", "const:4:8"]]
- 005a1f88 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a1fc8 ["INT_ADD", "register:40f0:8", ["const:5a1fc8:8", "const:4:8"]]
+ 005a1fc8 ["CALL", null, ["callee:00c57ea0:8"]]
- 005a1f88 bytes c6d61a94
+ 005a1fc8 bytes b6d71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daf23f830eff1dae982323518d442397"></a>

### [`005a1fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1fa4.md) → [`005a1fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1fe4.md) _INIT_45

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a2084",
      "incomplete_value": true,
      "site": "005a209c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a2044",
      "incomplete_value": true,
      "site": "005a205c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:e95:8"
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
      "definition_site": "005a20c0",
      "incomplete_value": true,
      "site": "005a20dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "005a2080",
      "incomplete_value": true,
      "site": "005a209c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e90:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005a20e0",
      "incomplete_value": true,
      "site": "005a2124",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f09:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a20a0",
      "incomplete_value": true,
      "site": "005a20e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e3c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a2020",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005a2044",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005a2064",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a2020",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a2044",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a2064",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a201c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1fa4.md#insn-005a201c) · [`005a21d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1fa4.md#insn-005a21d8) · [`005a1fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1fa4.md#insn-005a1fd0)
- 新版 `005a205c`（命令位置の公開資料なし） · `005a2218`（命令位置の公開資料なし） · `005a2010`（命令位置の公開資料なし）

~~~diff
- 005a201c ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005a201c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a201c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a201c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a205c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005a205c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a205c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a205c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a201c bytes 4a093691
+ 005a205c bytes 4a093791
- 005a21d8 ["INT_ADD", "register:40f0:8", ["const:5a21d8:8", "const:4:8"]]
- 005a21d8 ["CALL", null, ["callee:00c57e30:8"]]
+ 005a2218 ["INT_ADD", "register:40f0:8", ["const:5a2218:8", "const:4:8"]]
+ 005a2218 ["CALL", null, ["callee:00c57e30:8"]]
- 005a21d8 bytes 16d61a94
+ 005a2218 bytes 06d71a94
- 005a1fd0 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 005a1fd0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005a1fd0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005a1fd0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005a2010 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 005a2010 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005a2010 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005a2010 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005a1fd0 bytes 73020b91
+ 005a2010 bytes 73021b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4bbbce6aa6c3868425f1911ebaeb515"></a>

### [`005a2334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2334.md) → [`005a2374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2374.md) FUN_005a2374

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.90% / 新版 94.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a24e4",
      "incomplete_value": true,
      "site": "005a24e4",
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
                "const:2bb000:8"
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
      "definition_site": "005a24a4",
      "incomplete_value": true,
      "site": "005a24a4",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:536:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a259c",
      "incomplete_value": false,
      "site": "005a25a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a255c",
      "incomplete_value": false,
      "site": "005a2564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a23a4",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "005a24d0",
      "READ",
      [
        "storage",
        "002bb536",
        null,
        "string"
      ]
    ],
    [
      "005a2584",
      "DATA",
      [
        "storage",
        "00c6e340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a23a4",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005a24d0",
      "READ",
      [
        "storage",
        "002bb576",
        null,
        "string"
      ]
    ],
    [
      "005a2584",
      "DATA",
      [
        "storage",
        "00c6e740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a2524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2334.md#insn-005a2524) · [`005a2358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2334.md#insn-005a2358) · [`005a2390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2334.md#insn-005a2390)
- 新版 `005a2564`（命令位置の公開資料なし） · `005a2398`（命令位置の公開資料なし） · `005a23d0`（命令位置の公開資料なし）

~~~diff
- 005a2524 ["INT_ADD", "register:40f0:8", ["const:5a2524:8", "const:4:8"]]
- 005a2524 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a2564 ["INT_ADD", "register:40f0:8", ["const:5a2564:8", "const:4:8"]]
+ 005a2564 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a2524 bytes 63d51a94
+ 005a2564 bytes 53d61a94
- 005a2358 ["COPY", "tmp:0:8", ["const:165:8"]]
- 005a2358 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a2358 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a2358 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a2398 ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 005a2398 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a2398 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a2398 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a2358 bytes 4a950591
+ 005a2398 bytes 4a950691
- 005a2390 ["INT_ADD", "register:40f0:8", ["const:5a2390:8", "const:4:8"]]
- 005a2390 ["CALL", null, ["callee:0044108c:8"]]
+ 005a23d0 ["INT_ADD", "register:40f0:8", ["const:5a23d0:8", "const:4:8"]]
+ 005a23d0 ["CALL", null, ["callee:0044108c:8"]]
- 005a2390 bytes 2f7bfa97
+ 005a23d0 bytes 2f7bfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e1ed59df2dbdb4d6c4b4b8b63c70636"></a>

### [`005a26f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a26f4.md) → [`005a2734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2734.md) FUN_005a2734

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a2750",
      "incomplete_value": true,
      "site": "005a2754",
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
      "definition_site": "005a2710",
      "incomplete_value": true,
      "site": "005a2714",
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
      "005a2748",
      "READ",
      [
        "storage",
        "00c9af20",
        null,
        "pointer"
      ]
    ],
    [
      "005a2754",
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
      "005a2748",
      "READ",
      [
        "storage",
        "00c9b320",
        null,
        "pointer"
      ]
    ],
    [
      "005a2754",
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

- 旧版 [`005a2700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a26f4.md#insn-005a2700) · [`005a2708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a26f4.md#insn-005a2708) · [`005a2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a26f4.md#insn-005a2720)
- 新版 `005a2740`（命令位置の公開資料なし） · `005a2748`（命令位置の公開資料なし） · `005a2760`（命令位置の公開資料なし）

~~~diff
- 005a2700 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005a2740 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005a2700 bytes c8370090
+ 005a2740 bytes c83700b0
- 005a2708 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
- 005a2708 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a2748 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:320:8"]]
+ 005a2748 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a2708 bytes 089147f9
+ 005a2748 bytes 089141f9
- 005a2720 ["INT_ADD", "register:40f0:8", ["const:5a2720:8", "const:4:8"]]
- 005a2720 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a2760 ["INT_ADD", "register:40f0:8", ["const:5a2760:8", "const:4:8"]]
+ 005a2760 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a2720 bytes e4d41a94
+ 005a2760 bytes d4d51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13ce489f389dccbd494a37899127a62b"></a>

### [`005a2744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2744.md) → [`005a2784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2784.md) FUN_005a2784

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
      "definition_site": "005a278c",
      "incomplete_value": false,
      "site": "005a2790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a274c",
      "incomplete_value": false,
      "site": "005a2750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a2790",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a2790",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a274c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2744.md#insn-005a274c) · [`005a2770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2744.md#insn-005a2770)
- 新版 `005a278c`（命令位置の公開資料なし） · `005a27b0`（命令位置の公開資料なし）

~~~diff
- 005a274c ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a274c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a274c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a274c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a278c ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a278c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a278c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a278c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a274c bytes 29011891
+ 005a278c bytes 29012891
- 005a2770 ["INT_ADD", "register:40f0:8", ["const:5a2770:8", "const:4:8"]]
- 005a2770 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a27b0 ["INT_ADD", "register:40f0:8", ["const:5a27b0:8", "const:4:8"]]
+ 005a27b0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a2770 bytes d0d41a94
+ 005a27b0 bytes c0d51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cba9ea813df9c990371c3159a26f82b"></a>

### [`005a2794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2794.md) → [`005a27d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a27d4.md) FUN_005a27d4

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
      "definition_site": "005a27e4",
      "incomplete_value": false,
      "site": "005a27ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a27a4",
      "incomplete_value": false,
      "site": "005a27ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a27ec",
      "DATA",
      [
        "storage",
        "00c6e340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a27ec",
      "DATA",
      [
        "storage",
        "00c6e740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a27a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2794.md#insn-005a27a4) · [`005a27b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2794.md#insn-005a27b0)
- 新版 `005a27e4`（命令位置の公開資料なし） · `005a27f0`（命令位置の公開資料なし）

~~~diff
- 005a27a4 ["COPY", "tmp:0:8", ["const:340:8"]]
- 005a27a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a27a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a27a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a27e4 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 005a27e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a27e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a27e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a27a4 bytes 08010d91
+ 005a27e4 bytes 08011d91
- 005a27b0 ["INT_ADD", "register:40f0:8", ["const:5a27b0:8", "const:4:8"]]
- 005a27b0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a27f0 ["INT_ADD", "register:40f0:8", ["const:5a27f0:8", "const:4:8"]]
+ 005a27f0 ["CALL", null, ["callee:00c57ea0:8"]]
- 005a27b0 bytes bcd41a94
+ 005a27f0 bytes acd51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5f8d254ed6f0305cf40acb4a44a38ec"></a>

### [`005a27c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a27c4.md) → [`005a2804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2804.md) FUN_005a2804

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a280c",
      "incomplete_value": true,
      "site": "005a2810",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a27cc",
      "incomplete_value": true,
      "site": "005a27d0",
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
      "005a2810",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a2810",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a27cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a27c4.md#insn-005a27cc)
- 新版 `005a280c`（命令位置の公開資料なし）

~~~diff
- 005a27cc ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a27cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a27cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a27cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a280c ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a280c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a280c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a280c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a27cc bytes 29011891
+ 005a280c bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c014774c656d90af3de11201163d59b3"></a>

### [`005a27e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a27e8.md) → [`005a2828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2828.md) FUN_005a2828

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
      "definition_site": "005a282c",
      "incomplete_value": false,
      "site": "005a2830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a27ec",
      "incomplete_value": false,
      "site": "005a27f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a2830",
      "DATA",
      [
        "storage",
        "00c6e390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a2830",
      "DATA",
      [
        "storage",
        "00c6e790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a27ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a27e8.md#insn-005a27ec)
- 新版 `005a282c`（命令位置の公開資料なし）

~~~diff
- 005a27ec ["COPY", "tmp:0:8", ["const:390:8"]]
- 005a27ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a27ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a27ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a282c ["COPY", "tmp:0:8", ["const:790:8"]]
+ 005a282c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a282c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a282c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a27ec bytes 08410e91
+ 005a282c bytes 08411e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de70b3eba412b8ab095e7e2d7212a254"></a>

### [`005a27f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a27f8.md) → [`005a2838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2838.md) FUN_005a2838

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
      "definition_site": "005a2848",
      "incomplete_value": false,
      "site": "005a2850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a2808",
      "incomplete_value": false,
      "site": "005a2810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a2850",
      "DATA",
      [
        "storage",
        "00c6e390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a2850",
      "DATA",
      [
        "storage",
        "00c6e790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a2808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a27f8.md#insn-005a2808) · [`005a2814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a27f8.md#insn-005a2814)
- 新版 `005a2848`（命令位置の公開資料なし） · `005a2854`（命令位置の公開資料なし）

~~~diff
- 005a2808 ["COPY", "tmp:0:8", ["const:390:8"]]
- 005a2808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a2808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a2808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a2848 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 005a2848 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a2848 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a2848 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a2808 bytes 08410e91
+ 005a2848 bytes 08411e91
- 005a2814 ["INT_ADD", "register:40f0:8", ["const:5a2814:8", "const:4:8"]]
- 005a2814 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a2854 ["INT_ADD", "register:40f0:8", ["const:5a2854:8", "const:4:8"]]
+ 005a2854 ["CALL", null, ["callee:00c57ea0:8"]]
- 005a2814 bytes a3d41a94
+ 005a2854 bytes 93d51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd346df4819180f086362c9beaa7af8b"></a>

### [`005a2830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2830.md) → [`005a2870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2870.md) _INIT_46

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.40% / 新版 90.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a28ac",
      "incomplete_value": true,
      "site": "005a28c8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a286c",
      "incomplete_value": true,
      "site": "005a2888",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:ee6:8"
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
      "definition_site": "005a294c",
      "incomplete_value": true,
      "site": "005a2968",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f5d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a290c",
      "incomplete_value": true,
      "site": "005a2928",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:e90:8"
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
      "005a28ac",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005a28d0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005a28f0",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a28ac",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a28d0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a28f0",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a28c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2830.md#insn-005a28c8) · [`005a285c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2830.md#insn-005a285c) · [`005a2868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2830.md#insn-005a2868)
- 新版 `005a2908`（命令位置の公開資料なし） · `005a289c`（命令位置の公開資料なし） · `005a28a8`（命令位置の公開資料なし）

~~~diff
- 005a28c8 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005a28c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a28c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a28c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a2908 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005a2908 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a2908 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a2908 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a28c8 bytes 4a553a91
+ 005a2908 bytes 4a893d91
- 005a285c ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 005a285c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005a285c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005a285c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005a289c ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 005a289c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005a289c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005a289c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005a285c bytes 73620b91
+ 005a289c bytes 73621b91
- 005a2868 ["COPY", "tmp:0:8", ["const:ee6:8"]]
- 005a2868 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a2868 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a2868 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a28a8 ["COPY", "tmp:0:8", ["const:f26:8"]]
+ 005a28a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a28a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a28a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a2868 bytes 29993b91
+ 005a28a8 bytes 29993c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb990610346c1522bdd49b0c05315ebc"></a>

### [`005a2bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2bc0.md) → [`005a2c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2c00.md) _INIT_47

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a2e28",
      "incomplete_value": false,
      "site": "005a2e34",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a2de8",
      "incomplete_value": false,
      "site": "005a2df4",
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
            "const:2f0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a2e30",
      "incomplete_value": false,
      "site": "005a2e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a2df0",
      "incomplete_value": false,
      "site": "005a2df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "005a2c3c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005a2c60",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005a2c80",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a2c3c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a2c60",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a2c80",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a2df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2bc0.md#insn-005a2df4) · [`005a2bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2bc0.md#insn-005a2bec) · [`005a2bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2bc0.md#insn-005a2bf4)
- 新版 `005a2e34`（命令位置の公開資料なし） · `005a2c2c`（命令位置の公開資料なし）

~~~diff
- 005a2df4 ["INT_ADD", "register:40f0:8", ["const:5a2df4:8", "const:4:8"]]
- 005a2df4 ["CALL", null, ["callee:00c57e30:8"]]
+ 005a2e34 ["INT_ADD", "register:40f0:8", ["const:5a2e34:8", "const:4:8"]]
+ 005a2e34 ["CALL", null, ["callee:00c57e30:8"]]
- 005a2df4 bytes 0fd31a94
+ 005a2e34 bytes ffd31a94
- 005a2bec ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 005a2bec ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005a2bec ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005a2bec ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005a2c2c ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 005a2c2c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005a2c2c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005a2c2c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005a2bec bytes 73c20b91
+ 005a2c2c bytes 73c21b91
- 005a2bf4 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 005a2bf4 bytes a9e8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fc9eb74da31c2bd9bbd9ba9f3ff229f"></a>

### [`005a2f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2f50.md) → [`005a2f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2f90.md) _INIT_48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.40% / 新版 90.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a2fcc",
      "incomplete_value": true,
      "site": "005a2fe8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "005a2f8c",
      "incomplete_value": true,
      "site": "005a2fa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a31c0",
      "incomplete_value": true,
      "site": "005a31c4",
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
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a3180",
      "incomplete_value": true,
      "site": "005a3184",
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
            "const:b90:8"
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
      "005a2fcc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005a2ff0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005a3010",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a2fcc",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a2ff0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a3010",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a2fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2f50.md#insn-005a2fe8) · [`005a3184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2f50.md#insn-005a3184) · [`005a2f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2f50.md#insn-005a2f7c)
- 新版 `005a3028`（命令位置の公開資料なし） · `005a31c4`（命令位置の公開資料なし） · `005a2fbc`（命令位置の公開資料なし）

~~~diff
- 005a2fe8 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005a2fe8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a2fe8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a2fe8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a3028 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005a3028 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a3028 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a3028 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a2fe8 bytes 4a553a91
+ 005a3028 bytes 4a893d91
- 005a3184 ["INT_ADD", "register:40f0:8", ["const:5a3184:8", "const:4:8"]]
- 005a3184 ["CALL", null, ["callee:00c57e30:8"]]
+ 005a31c4 ["INT_ADD", "register:40f0:8", ["const:5a31c4:8", "const:4:8"]]
+ 005a31c4 ["CALL", null, ["callee:00c57e30:8"]]
- 005a3184 bytes 2bd21a94
+ 005a31c4 bytes 1bd31a94
- 005a2f7c ["COPY", "tmp:0:8", ["const:308:8"]]
- 005a2f7c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005a2f7c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005a2f7c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005a2fbc ["COPY", "tmp:0:8", ["const:708:8"]]
+ 005a2fbc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005a2fbc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005a2fbc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005a2f7c bytes 73220c91
+ 005a2fbc bytes 73221c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9ccb9d7cf1f1bc588a85a7b7d7a7e44"></a>

### [`005a32e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a32e0.md) → [`005a3320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3320.md) FUN_005a3320

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005a4260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4260.md) [`005a4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4418.md) [`005a4554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4554.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005a42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`005a4594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4594.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a372c",
      "incomplete_value": true,
      "site": "005a3738",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:34b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a36ec",
      "incomplete_value": true,
      "site": "005a36f8",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:30b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 74,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a3358",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "005a34c0",
      "READ",
      [
        "storage",
        "002a9d85",
        null,
        "string"
      ]
    ],
    [
      "005a362c",
      "READ",
      [
        "storage",
        "002b7178",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a3358",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005a34c0",
      "READ",
      [
        "storage",
        "002a9e52",
        null,
        "string"
      ]
    ],
    [
      "005a362c",
      "READ",
      [
        "storage",
        "002b71b8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a36b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a32e0.md#insn-005a36b8) · [`005a330c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a32e0.md#insn-005a330c) · [`005a3344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a32e0.md#insn-005a3344)
- 新版 `005a36f8`（命令位置の公開資料なし） · `005a334c`（命令位置の公開資料なし） · `005a3384`（命令位置の公開資料なし）

~~~diff
- 005a36b8 ["INT_ADD", "register:40f0:8", ["const:5a36b8:8", "const:4:8"]]
- 005a36b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a36f8 ["INT_ADD", "register:40f0:8", ["const:5a36f8:8", "const:4:8"]]
+ 005a36f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a36b8 bytes fed01a94
+ 005a36f8 bytes eed11a94
- 005a330c ["COPY", "tmp:0:8", ["const:165:8"]]
- 005a330c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a330c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a330c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a334c ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 005a334c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a334c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a334c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a330c bytes 4a950591
+ 005a334c bytes 4a950691
- 005a3344 ["INT_ADD", "register:40f0:8", ["const:5a3344:8", "const:4:8"]]
- 005a3344 ["CALL", null, ["callee:0044108c:8"]]
+ 005a3384 ["INT_ADD", "register:40f0:8", ["const:5a3384:8", "const:4:8"]]
+ 005a3384 ["CALL", null, ["callee:0044108c:8"]]
- 005a3344 bytes 4277fa97
+ 005a3384 bytes 4277fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a661235f7ad89f2d2d4b4b6a5de4e25"></a>

### [`005a3f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3f58.md) → [`005a3f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3f98.md) FUN_005a3f98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005a3fb4",
      "incomplete_value": false,
      "site": "005a3fbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a3f74",
      "incomplete_value": false,
      "site": "005a3f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a3fcc",
      "incomplete_value": true,
      "site": "005a3fcc",
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
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a3f8c",
      "incomplete_value": true,
      "site": "005a3f8c",
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
            "const:400:8"
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
      "005a3fbc",
      "DATA",
      [
        "storage",
        "00c6e508",
        null,
        "undefined *"
      ]
    ],
    [
      "005a3fcc",
      "DATA",
      [
        "storage",
        "00c6e400",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a3fbc",
      "DATA",
      [
        "storage",
        "00c6e908",
        null,
        "undefined *"
      ]
    ],
    [
      "005a3fcc",
      "DATA",
      [
        "storage",
        "00c6e800",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a3f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3f58.md#insn-005a3f6c) · [`005a3f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3f58.md#insn-005a3f74) · [`005a3f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3f58.md#insn-005a3f80)
- 新版 `005a3fac`（命令位置の公開資料なし） · `005a3fb4`（命令位置の公開資料なし）

~~~diff
- 005a3f6c ["INT_ADD", "register:40f0:8", ["const:5a3f6c:8", "const:4:8"]]
- 005a3f6c ["CALL", null, ["callee:00c57e90:8"]]
+ 005a3fac ["INT_ADD", "register:40f0:8", ["const:5a3fac:8", "const:4:8"]]
+ 005a3fac ["CALL", null, ["callee:00c57e90:8"]]
- 005a3f6c bytes c9ce1a94
+ 005a3fac bytes b9cf1a94
- 005a3f74 ["COPY", "tmp:0:8", ["const:508:8"]]
- 005a3f74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a3f74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a3f74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a3fb4 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 005a3fb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a3fb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a3fb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a3f74 bytes 08211491
+ 005a3fb4 bytes 08212491
- 005a3f80 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005a3f80 bytes 483600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31f59d5992434ebe18e7714c9da27c56"></a>

### [`005a3ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3ff0.md) → [`005a4030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4030.md) FUN_005a4030

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a44c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a44c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005a4064",
      "incomplete_value": false,
      "site": "005a4068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4024",
      "incomplete_value": false,
      "site": "005a4028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "005a4068",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a4068",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3ff0.md#insn-005a4010) · [`005a4018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3ff0.md#insn-005a4018) · [`005a4024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3ff0.md#insn-005a4024)
- 新版 `005a4050`（命令位置の公開資料なし） · `005a4058`（命令位置の公開資料なし） · `005a4064`（命令位置の公開資料なし）

~~~diff
- 005a4010 ["INT_ADD", "register:40f0:8", ["const:5a4010:8", "const:4:8"]]
- 005a4010 ["CALL", null, ["callee:005a4508:8"]]
+ 005a4050 ["INT_ADD", "register:40f0:8", ["const:5a4050:8", "const:4:8"]]
+ 005a4050 ["CALL", null, ["callee:005a4508:8"]]
- 005a4010 bytes 2e010094
+ 005a4050 bytes 2e010094
- 005a4018 ["INT_ADD", "register:40f0:8", ["const:5a4018:8", "const:4:8"]]
- 005a4018 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a4058 ["INT_ADD", "register:40f0:8", ["const:5a4058:8", "const:4:8"]]
+ 005a4058 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a4018 bytes a6ce1a94
+ 005a4058 bytes 96cf1a94
- 005a4024 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a4024 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a4024 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a4024 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a4064 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a4064 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a4064 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a4064 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a4024 bytes 29011891
+ 005a4064 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0eff2124430d414aa976aae08e0a883"></a>

### [`005a404c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a404c.md) → [`005a408c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a408c.md) FUN_005a408c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a44c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a44c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005a40c0",
      "incomplete_value": false,
      "site": "005a40c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4080",
      "incomplete_value": false,
      "site": "005a4084",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "005a40c4",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a40c4",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a406c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a404c.md#insn-005a406c) · [`005a4074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a404c.md#insn-005a4074) · [`005a4080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a404c.md#insn-005a4080)
- 新版 `005a40ac`（命令位置の公開資料なし） · `005a40b4`（命令位置の公開資料なし） · `005a40c0`（命令位置の公開資料なし）

~~~diff
- 005a406c ["INT_ADD", "register:40f0:8", ["const:5a406c:8", "const:4:8"]]
- 005a406c ["CALL", null, ["callee:005a4508:8"]]
+ 005a40ac ["INT_ADD", "register:40f0:8", ["const:5a40ac:8", "const:4:8"]]
+ 005a40ac ["CALL", null, ["callee:005a4508:8"]]
- 005a406c bytes 17010094
+ 005a40ac bytes 17010094
- 005a4074 ["INT_ADD", "register:40f0:8", ["const:5a4074:8", "const:4:8"]]
- 005a4074 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a40b4 ["INT_ADD", "register:40f0:8", ["const:5a40b4:8", "const:4:8"]]
+ 005a40b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a4074 bytes 8fce1a94
+ 005a40b4 bytes 7fcf1a94
- 005a4080 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a4080 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a4080 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a4080 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a40c0 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a40c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a40c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a40c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a4080 bytes 29011891
+ 005a40c0 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93cbf622095d7741913c0d59f5aaf80f"></a>

### [`005a422c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a422c.md) → [`005a426c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a426c.md) FUN_005a426c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005a40a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a40a4.md) [`005a4554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4554.md) [`0079cbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079cbd0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`005a40e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md) [`005a4594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4594.md) [`0079cc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cc10.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005a4278",
      "incomplete_value": false,
      "site": "005a427c",
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
    "old": {
      "definition_site": "005a4238",
      "incomplete_value": false,
      "site": "005a423c",
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
            "const:f0c:8"
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
      "005a4278",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a4278",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a423c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a422c.md#insn-005a423c) · [`005a4238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a422c.md#insn-005a4238)
- 新版 `005a427c`（命令位置の公開資料なし） · `005a4278`（命令位置の公開資料なし）

~~~diff
- 005a423c ["INT_ADD", "register:40f0:8", ["const:5a423c:8", "const:4:8"]]
- 005a423c ["CALL", null, ["callee:0043b778:8"]]
+ 005a427c ["INT_ADD", "register:40f0:8", ["const:5a427c:8", "const:4:8"]]
+ 005a427c ["CALL", null, ["callee:0043b778:8"]]
- 005a423c bytes 3f5dfa97
+ 005a427c bytes 3f5dfa97
- 005a4238 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005a4238 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005a4238 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005a4238 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005a4278 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005a4278 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005a4278 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005a4278 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005a4238 bytes 00303c91
+ 005a4278 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e28a687bfaf2b90560da7a2b8046ae9"></a>

### [`005a4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4418.md) → [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) FUN_005a4458

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 19件 [`005a32e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a32e0.md) [`005a4260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4260.md) [`0079cf34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079cf34.md) [`0079d58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d58c.md) [`0079fff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fff4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 19件 [`005a3320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3320.md) [`005a42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md) [`0079cf74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cf74.md) [`0079d5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d5cc.md) [`007a0034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005a4464",
      "incomplete_value": false,
      "site": "005a4468",
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
    "old": {
      "definition_site": "005a4424",
      "incomplete_value": false,
      "site": "005a4428",
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
            "const:f0c:8"
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
      "005a4464",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a4464",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4418.md#insn-005a4428) · [`005a4424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4418.md#insn-005a4424)
- 新版 `005a4468`（命令位置の公開資料なし） · `005a4464`（命令位置の公開資料なし）

~~~diff
- 005a4428 ["INT_ADD", "register:40f0:8", ["const:5a4428:8", "const:4:8"]]
- 005a4428 ["CALL", null, ["callee:0043b778:8"]]
+ 005a4468 ["INT_ADD", "register:40f0:8", ["const:5a4468:8", "const:4:8"]]
+ 005a4468 ["CALL", null, ["callee:0043b778:8"]]
- 005a4428 bytes c45cfa97
+ 005a4468 bytes c45cfa97
- 005a4424 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005a4424 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005a4424 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005a4424 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005a4464 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005a4464 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005a4464 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005a4464 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005a4424 bytes 00303c91
+ 005a4464 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e5c31fb16d062d679f1b6ce99aab4e2"></a>

### [`005a48dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a48dc.md) → [`005a491c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a491c.md) FUN_005a491c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005a32e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a32e0.md) · 呼出先 3件 [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`005a40a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a40a4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005a3320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3320.md) · 呼出先 3件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`005a40e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a499c",
      "incomplete_value": false,
      "site": "005a499c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a495c",
      "incomplete_value": false,
      "site": "005a495c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "005a4960",
      "DATA",
      [
        "storage",
        "00c6e4b8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a499c",
      "DATA",
      [
        "storage",
        "00c6e3e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a4960",
      "DATA",
      [
        "storage",
        "00c6e8b8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a499c",
      "DATA",
      [
        "storage",
        "00c6e7e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a48dc.md#insn-005a4904) · [`005a4914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a48dc.md#insn-005a4914) · [`005a492c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a48dc.md#insn-005a492c)
- 新版 `005a4944`（命令位置の公開資料なし） · `005a4954`（命令位置の公開資料なし） · `005a496c`（命令位置の公開資料なし）

~~~diff
- 005a4904 ["INT_ADD", "register:40f0:8", ["const:5a4904:8", "const:4:8"]]
- 005a4904 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a4944 ["INT_ADD", "register:40f0:8", ["const:5a4944:8", "const:4:8"]]
+ 005a4944 ["CALL", null, ["callee:00c57e90:8"]]
- 005a4904 bytes 63cc1a94
+ 005a4944 bytes 53cd1a94
- 005a4914 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 005a4914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a4914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a4914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a4954 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 005a4954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a4914 bytes 08e11291
+ 005a4954 bytes 08e12291
- 005a492c ["INT_ADD", "register:40f0:8", ["const:5a492c:8", "const:4:8"]]
- 005a492c ["CALL", null, ["callee:0059b8dc:8"]]
+ 005a496c ["INT_ADD", "register:40f0:8", ["const:5a496c:8", "const:4:8"]]
+ 005a496c ["CALL", null, ["callee:0059b8dc:8"]]
- 005a492c bytes dcdbff97
+ 005a496c bytes dcdbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7f40f13b12198db71a0882de19598d8"></a>

### [`005a49bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a49bc.md) → [`005a49fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a49fc.md) FUN_005a49fc

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
      "definition_site": "005a4a00",
      "incomplete_value": false,
      "site": "005a4a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a49c0",
      "incomplete_value": false,
      "site": "005a49c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
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
      "005a4a04",
      "DATA",
      [
        "storage",
        "00c6e4b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a4a04",
      "DATA",
      [
        "storage",
        "00c6e8b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a49c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a49bc.md#insn-005a49c0)
- 新版 `005a4a00`（命令位置の公開資料なし）

~~~diff
- 005a49c0 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 005a49c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a49c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a49c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a4a00 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 005a4a00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4a00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4a00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a49c0 bytes 08e11291
+ 005a4a00 bytes 08e12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e620d34ae00ca40c623f5f74fb5e95f6"></a>

### [`005a49fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a49fc.md) → [`005a4a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4a3c.md) FUN_005a4a3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a44c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a44c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005a4a70",
      "incomplete_value": false,
      "site": "005a4a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4a30",
      "incomplete_value": false,
      "site": "005a4a34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "005a4a74",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a4a74",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a49fc.md#insn-005a4a1c) · [`005a4a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a49fc.md#insn-005a4a24) · [`005a4a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a49fc.md#insn-005a4a30)
- 新版 `005a4a5c`（命令位置の公開資料なし） · `005a4a64`（命令位置の公開資料なし） · `005a4a70`（命令位置の公開資料なし）

~~~diff
- 005a4a1c ["INT_ADD", "register:40f0:8", ["const:5a4a1c:8", "const:4:8"]]
- 005a4a1c ["CALL", null, ["callee:005a4508:8"]]
+ 005a4a5c ["INT_ADD", "register:40f0:8", ["const:5a4a5c:8", "const:4:8"]]
+ 005a4a5c ["CALL", null, ["callee:005a4508:8"]]
- 005a4a1c bytes abfeff97
+ 005a4a5c bytes abfeff97
- 005a4a24 ["INT_ADD", "register:40f0:8", ["const:5a4a24:8", "const:4:8"]]
- 005a4a24 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a4a64 ["INT_ADD", "register:40f0:8", ["const:5a4a64:8", "const:4:8"]]
+ 005a4a64 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a4a24 bytes 23cc1a94
+ 005a4a64 bytes 13cd1a94
- 005a4a30 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a4a30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a4a30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a4a30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a4a70 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a4a70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a4a70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a4a70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a4a30 bytes 29011891
+ 005a4a70 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90fca2b3bda10e2e553a0a3d5fa6c954"></a>

### [`005a4a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4a5c.md) → [`005a4a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4a9c.md) FUN_005a4a9c

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
      "definition_site": "005a4aa0",
      "incomplete_value": false,
      "site": "005a4aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4a60",
      "incomplete_value": false,
      "site": "005a4a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "005a4aa4",
      "DATA",
      [
        "storage",
        "00c6e508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a4aa4",
      "DATA",
      [
        "storage",
        "00c6e908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4a5c.md#insn-005a4a60)
- 新版 `005a4aa0`（命令位置の公開資料なし）

~~~diff
- 005a4a60 ["COPY", "tmp:0:8", ["const:508:8"]]
- 005a4a60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a4a60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a4a60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a4aa0 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 005a4aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a4a60 bytes 08211491
+ 005a4aa0 bytes 08212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9b86540213d283110ccd2d34f5952db"></a>

### [`005a4a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4a6c.md) → [`005a4aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4aac.md) FUN_005a4aac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a4abc",
      "incomplete_value": true,
      "site": "005a4ac4",
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
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4a7c",
      "incomplete_value": true,
      "site": "005a4a84",
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
            "const:508:8"
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
      "005a4ac4",
      "DATA",
      [
        "storage",
        "00c6e508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a4ac4",
      "DATA",
      [
        "storage",
        "00c6e908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4a6c.md#insn-005a4a7c) · [`005a4a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4a6c.md#insn-005a4a88)
- 新版 `005a4abc`（命令位置の公開資料なし） · `005a4ac8`（命令位置の公開資料なし）

~~~diff
- 005a4a7c ["COPY", "tmp:0:8", ["const:508:8"]]
- 005a4a7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a4a7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a4a7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a4abc ["COPY", "tmp:0:8", ["const:908:8"]]
+ 005a4abc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4abc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4abc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a4a7c bytes 08211491
+ 005a4abc bytes 08212491
- 005a4a88 ["INT_ADD", "register:40f0:8", ["const:5a4a88:8", "const:4:8"]]
- 005a4a88 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a4ac8 ["INT_ADD", "register:40f0:8", ["const:5a4ac8:8", "const:4:8"]]
+ 005a4ac8 ["CALL", null, ["callee:00c57ea0:8"]]
- 005a4a88 bytes 06cc1a94
+ 005a4ac8 bytes f6cc1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ad9cf9d4feadd49e4af2f9639f45bd7"></a>

### [`005a4aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4aa4.md) → [`005a4ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4ae4.md) _INIT_49

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a4ba0",
      "incomplete_value": true,
      "site": "005a4bbc",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4b60",
      "incomplete_value": true,
      "site": "005a4b7c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:592:8"
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
      "005a4b20",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005a4b44",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005a4b64",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a4b20",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a4b44",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a4b64",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4aa4.md#insn-005a4b3c) · [`005a4ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4aa4.md#insn-005a4ad0) · [`005a4ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4aa4.md#insn-005a4ad8)
- 新版 `005a4b7c`（命令位置の公開資料なし） · `005a4b10`（命令位置の公開資料なし）

~~~diff
- 005a4b3c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005a4b3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a4b3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a4b3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a4b7c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005a4b7c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a4b7c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a4b7c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a4b3c bytes 4a553a91
+ 005a4b7c bytes 4a893d91
- 005a4ad0 ["COPY", "tmp:0:8", ["const:320:8"]]
- 005a4ad0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005a4ad0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005a4ad0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005a4b10 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 005a4b10 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005a4b10 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005a4b10 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005a4ad0 bytes 73820c91
+ 005a4b10 bytes 73821c91
- 005a4ad8 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 005a4ad8 bytes 89e8fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe8a1b0710cd058f758ce12812c9676d"></a>

### [`005a4fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4fd8.md) → [`005a5018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5018.md) FUN_005a5018

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`007adedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007adedc.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)
- 新版 呼出元 1件 [`007adf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)

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
      "definition_site": "005a5034",
      "incomplete_value": false,
      "site": "005a5038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4ff4",
      "incomplete_value": false,
      "site": "005a4ff8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "005a5038",
      "DATA",
      [
        "storage",
        "00c6e578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5038",
      "DATA",
      [
        "storage",
        "00c6e978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4fd8.md#insn-005a4fec) · [`005a4ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4fd8.md#insn-005a4ff4)
- 新版 `005a502c`（命令位置の公開資料なし） · `005a5034`（命令位置の公開資料なし）

~~~diff
- 005a4fec ["INT_ADD", "register:40f0:8", ["const:5a4fec:8", "const:4:8"]]
- 005a4fec ["CALL", null, ["callee:0059b908:8"]]
+ 005a502c ["INT_ADD", "register:40f0:8", ["const:5a502c:8", "const:4:8"]]
+ 005a502c ["CALL", null, ["callee:0059b908:8"]]
- 005a4fec bytes 37daff97
+ 005a502c bytes 37daff97
- 005a4ff4 ["COPY", "tmp:0:8", ["const:578:8"]]
- 005a4ff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a4ff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a4ff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5034 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 005a5034 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5034 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5034 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a4ff4 bytes 08e11591
+ 005a5034 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da416c54921ce530f8b2a2d08c77a486"></a>

### [`005a5024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5024.md) → [`005a5064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5064.md) FUN_005a5064

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "005a5070",
      "incomplete_value": true,
      "site": "005a5080",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ff2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5030",
      "incomplete_value": true,
      "site": "005a5040",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fb2:8"
              ]
            ]
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
      "005a5070",
      "READ",
      [
        "storage",
        "002b4fb2",
        null,
        "string"
      ]
    ],
    [
      "005a5078",
      "READ",
      [
        "storage",
        "002b4fc0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a5070",
      "READ",
      [
        "storage",
        "002b4ff2",
        null,
        "string"
      ]
    ],
    [
      "005a5078",
      "READ",
      [
        "storage",
        "002b5000",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a502c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5024.md#insn-005a502c)
- 新版 `005a506c`（命令位置の公開資料なし）

~~~diff
- 005a502c ["COPY", "tmp:0:8", ["const:fb2:8"]]
- 005a502c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a502c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a502c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a506c ["COPY", "tmp:0:8", ["const:ff2:8"]]
+ 005a506c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a506c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a506c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a502c bytes 4ac93e91
+ 005a506c bytes 4ac93f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-913e88e57039df68eee50abff9c75123"></a>

### [`005a5150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5150.md) → [`005a5190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5190.md) FUN_005a5190

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005a51ac",
      "incomplete_value": false,
      "site": "005a51b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a516c",
      "incomplete_value": false,
      "site": "005a5174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "definition_site": "005a51c4",
      "incomplete_value": false,
      "site": "005a51c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5184",
      "incomplete_value": false,
      "site": "005a5184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
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
      "005a51b4",
      "DATA",
      [
        "storage",
        "00c6e680",
        null,
        "undefined *"
      ]
    ],
    [
      "005a51c4",
      "DATA",
      [
        "storage",
        "00c6e5d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a51b4",
      "DATA",
      [
        "storage",
        "00c6ea80",
        null,
        "undefined *"
      ]
    ],
    [
      "005a51c4",
      "DATA",
      [
        "storage",
        "00c6e9d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5150.md#insn-005a5164) · [`005a516c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5150.md#insn-005a516c) · [`005a5178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5150.md#insn-005a5178)
- 新版 `005a51a4`（命令位置の公開資料なし） · `005a51ac`（命令位置の公開資料なし）

~~~diff
- 005a5164 ["INT_ADD", "register:40f0:8", ["const:5a5164:8", "const:4:8"]]
- 005a5164 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a51a4 ["INT_ADD", "register:40f0:8", ["const:5a51a4:8", "const:4:8"]]
+ 005a51a4 ["CALL", null, ["callee:00c57e90:8"]]
- 005a5164 bytes 4bca1a94
+ 005a51a4 bytes 3bcb1a94
- 005a516c ["COPY", "tmp:0:8", ["const:680:8"]]
- 005a516c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a516c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a516c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a51ac ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 005a51ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a51ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a51ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a516c bytes 08011a91
+ 005a51ac bytes 08012a91
- 005a5178 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005a5178 bytes 483600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98d40bd05957299478c91aeea6f1b807"></a>

### [`005a5198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5198.md) → [`005a51d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a51d8.md) FUN_005a51d8

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
      "definition_site": "005a5204",
      "incomplete_value": false,
      "site": "005a5208",
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
      "definition_site": "005a51c4",
      "incomplete_value": false,
      "site": "005a51c8",
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
      "005a5208",
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
      "005a5208",
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

- 旧版 [`005a51b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5198.md#insn-005a51b4) · [`005a51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5198.md#insn-005a51bc) · [`005a51d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5198.md#insn-005a51d4)
- 新版 `005a51f4`（命令位置の公開資料なし） · `005a51fc`（命令位置の公開資料なし） · `005a5214`（命令位置の公開資料なし）

~~~diff
- 005a51b4 ["INT_ADD", "register:40f0:8", ["const:5a51b4:8", "const:4:8"]]
- 005a51b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a51f4 ["INT_ADD", "register:40f0:8", ["const:5a51f4:8", "const:4:8"]]
+ 005a51f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a51b4 bytes 3fca1a94
+ 005a51f4 bytes 2fcb1a94
- 005a51bc ["COPY", "tmp:0:8", ["const:610:8"]]
- 005a51bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a51bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a51bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a51fc ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005a51fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a51fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a51fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a51bc bytes 08411891
+ 005a51fc bytes 08412891
- 005a51d4 ["INT_ADD", "register:40f0:8", ["const:5a51d4:8", "const:4:8"]]
- 005a51d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a5214 ["INT_ADD", "register:40f0:8", ["const:5a5214:8", "const:4:8"]]
+ 005a5214 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a51d4 bytes 37ca1a94
+ 005a5214 bytes 27cb1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c56ea25e18e68605db9611fbcfe49254"></a>

### [`005a51fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a51fc.md) → [`005a523c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a523c.md) FUN_005a523c

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
      "definition_site": "005a5268",
      "incomplete_value": false,
      "site": "005a526c",
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
      "definition_site": "005a5228",
      "incomplete_value": false,
      "site": "005a522c",
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
      "005a526c",
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
      "005a526c",
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

- 旧版 [`005a5218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a51fc.md#insn-005a5218) · [`005a5220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a51fc.md#insn-005a5220) · [`005a5238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a51fc.md#insn-005a5238)
- 新版 `005a5258`（命令位置の公開資料なし） · `005a5260`（命令位置の公開資料なし） · `005a5278`（命令位置の公開資料なし）

~~~diff
- 005a5218 ["INT_ADD", "register:40f0:8", ["const:5a5218:8", "const:4:8"]]
- 005a5218 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a5258 ["INT_ADD", "register:40f0:8", ["const:5a5258:8", "const:4:8"]]
+ 005a5258 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a5218 bytes 26ca1a94
+ 005a5258 bytes 16cb1a94
- 005a5220 ["COPY", "tmp:0:8", ["const:610:8"]]
- 005a5220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5260 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005a5260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5220 bytes 08411891
+ 005a5260 bytes 08412891
- 005a5238 ["INT_ADD", "register:40f0:8", ["const:5a5238:8", "const:4:8"]]
- 005a5238 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a5278 ["INT_ADD", "register:40f0:8", ["const:5a5278:8", "const:4:8"]]
+ 005a5278 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a5238 bytes 1eca1a94
+ 005a5278 bytes 0ecb1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e52eb8e0c871e5dfe328c9e1be90f298"></a>

### [`005a525c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a525c.md) → [`005a529c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a529c.md) FUN_005a529c

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
      "definition_site": "005a52a4",
      "incomplete_value": false,
      "site": "005a52a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5264",
      "incomplete_value": false,
      "site": "005a5268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a52a8",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a52a8",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a525c.md#insn-005a5264) · [`005a5288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a525c.md#insn-005a5288)
- 新版 `005a52a4`（命令位置の公開資料なし） · `005a52c8`（命令位置の公開資料なし）

~~~diff
- 005a5264 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a5264 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a5264 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a5264 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a52a4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a52a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a52a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a52a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a5264 bytes 29011891
+ 005a52a4 bytes 29012891
- 005a5288 ["INT_ADD", "register:40f0:8", ["const:5a5288:8", "const:4:8"]]
- 005a5288 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a52c8 ["INT_ADD", "register:40f0:8", ["const:5a52c8:8", "const:4:8"]]
+ 005a52c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a5288 bytes 0aca1a94
+ 005a52c8 bytes faca1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7df6ccfaba7b45fb6aa6430b10f92291"></a>

### [`005a529c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a529c.md) → [`005a52dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a52dc.md) FUN_005a52dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005a4e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4e34.md) · 呼出先 4件 [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005a4e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4e74.md) · 呼出先 4件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5318",
      "incomplete_value": false,
      "site": "005a5320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a52d8",
      "incomplete_value": false,
      "site": "005a52e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:630:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a535c",
      "incomplete_value": false,
      "site": "005a5360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a531c",
      "incomplete_value": false,
      "site": "005a5320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "005a5320",
      "DATA",
      [
        "storage",
        "00c6e630",
        null,
        "undefined *"
      ]
    ],
    [
      "005a5360",
      "DATA",
      [
        "storage",
        "00c6e558",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a5320",
      "DATA",
      [
        "storage",
        "00c6ea30",
        null,
        "undefined *"
      ]
    ],
    [
      "005a5360",
      "DATA",
      [
        "storage",
        "00c6e958",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a52d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a529c.md#insn-005a52d0) · [`005a52d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a529c.md#insn-005a52d8) · [`005a5310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a529c.md#insn-005a5310)
- 新版 `005a5310`（命令位置の公開資料なし） · `005a5318`（命令位置の公開資料なし） · `005a5350`（命令位置の公開資料なし）

~~~diff
- 005a52d0 ["INT_ADD", "register:40f0:8", ["const:5a52d0:8", "const:4:8"]]
- 005a52d0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a5310 ["INT_ADD", "register:40f0:8", ["const:5a5310:8", "const:4:8"]]
+ 005a5310 ["CALL", null, ["callee:00c57e90:8"]]
- 005a52d0 bytes f0c91a94
+ 005a5310 bytes e0ca1a94
- 005a52d8 ["COPY", "tmp:0:8", ["const:630:8"]]
- 005a52d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a52d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a52d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5318 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 005a5318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a52d8 bytes 08c11891
+ 005a5318 bytes 08c12891
- 005a5310 ["INT_ADD", "register:40f0:8", ["const:5a5310:8", "const:4:8"]]
- 005a5310 ["CALL", null, ["callee:0059b8dc:8"]]
+ 005a5350 ["INT_ADD", "register:40f0:8", ["const:5a5350:8", "const:4:8"]]
+ 005a5350 ["CALL", null, ["callee:0059b8dc:8"]]
- 005a5310 bytes 63d9ff97
+ 005a5350 bytes 63d9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ff34d7c810403995a2d31255d743deb"></a>

### [`005a539c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a539c.md) → [`005a53dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a53dc.md) FUN_005a53dc

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
      "definition_site": "005a53e0",
      "incomplete_value": false,
      "site": "005a53e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a53a0",
      "incomplete_value": false,
      "site": "005a53a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a53e4",
      "DATA",
      [
        "storage",
        "00c6e630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a53e4",
      "DATA",
      [
        "storage",
        "00c6ea30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a53a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a539c.md#insn-005a53a0)
- 新版 `005a53e0`（命令位置の公開資料なし）

~~~diff
- 005a53a0 ["COPY", "tmp:0:8", ["const:630:8"]]
- 005a53a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a53a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a53a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a53e0 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 005a53e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a53e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a53e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a53a0 bytes 08c11891
+ 005a53e0 bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55a38878ea1cb583f2132b9c938de4e5"></a>

### [`005a53ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a53ac.md) → [`005a53ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a53ec.md) FUN_005a53ec

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
      "definition_site": "005a53fc",
      "incomplete_value": false,
      "site": "005a5404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a53bc",
      "incomplete_value": false,
      "site": "005a53c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a5404",
      "DATA",
      [
        "storage",
        "00c6e630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5404",
      "DATA",
      [
        "storage",
        "00c6ea30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a53bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a53ac.md#insn-005a53bc) · [`005a53c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a53ac.md#insn-005a53c8)
- 新版 `005a53fc`（命令位置の公開資料なし） · `005a5408`（命令位置の公開資料なし）

~~~diff
- 005a53bc ["COPY", "tmp:0:8", ["const:630:8"]]
- 005a53bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a53bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a53bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a53fc ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 005a53fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a53fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a53fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a53bc bytes 08c11891
+ 005a53fc bytes 08c12891
- 005a53c8 ["INT_ADD", "register:40f0:8", ["const:5a53c8:8", "const:4:8"]]
- 005a53c8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a5408 ["INT_ADD", "register:40f0:8", ["const:5a5408:8", "const:4:8"]]
+ 005a5408 ["CALL", null, ["callee:00c57ea0:8"]]
- 005a53c8 bytes b6c91a94
+ 005a5408 bytes a6ca1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fe2f75b08717baf868984e5883ae263"></a>

### [`005a53dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a53dc.md) → [`005a541c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a541c.md) FUN_005a541c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005a5424",
      "incomplete_value": false,
      "site": "005a5428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a53e4",
      "incomplete_value": false,
      "site": "005a53e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a5428",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a5428",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a53e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a53dc.md#insn-005a53e4)
- 新版 `005a5424`（命令位置の公開資料なし）

~~~diff
- 005a53e4 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a53e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a53e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a53e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a5424 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a5424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a53e4 bytes 29011891
+ 005a5424 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dad1d4dfdfe10cd5f385f7ff77027fdc"></a>

### [`005a5400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5400.md) → [`005a5440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5440.md) FUN_005a5440

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
      "definition_site": "005a5444",
      "incomplete_value": false,
      "site": "005a5448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5404",
      "incomplete_value": false,
      "site": "005a5408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "005a5448",
      "DATA",
      [
        "storage",
        "00c6e680",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5448",
      "DATA",
      [
        "storage",
        "00c6ea80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5400.md#insn-005a5404)
- 新版 `005a5444`（命令位置の公開資料なし）

~~~diff
- 005a5404 ["COPY", "tmp:0:8", ["const:680:8"]]
- 005a5404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5444 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 005a5444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5404 bytes 08011a91
+ 005a5444 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea2919e8d8f2ad779b85d645efcc315a"></a>

### [`005a5410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5410.md) → [`005a5450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5450.md) FUN_005a5450

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5460",
      "incomplete_value": true,
      "site": "005a5468",
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
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5420",
      "incomplete_value": true,
      "site": "005a5428",
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
            "const:680:8"
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
      "005a5468",
      "DATA",
      [
        "storage",
        "00c6e680",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5468",
      "DATA",
      [
        "storage",
        "00c6ea80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5410.md#insn-005a5420) · [`005a542c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5410.md#insn-005a542c)
- 新版 `005a5460`（命令位置の公開資料なし） · `005a546c`（命令位置の公開資料なし）

~~~diff
- 005a5420 ["COPY", "tmp:0:8", ["const:680:8"]]
- 005a5420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5460 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 005a5460 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5460 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5460 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5420 bytes 08011a91
+ 005a5460 bytes 08012a91
- 005a542c ["INT_ADD", "register:40f0:8", ["const:5a542c:8", "const:4:8"]]
- 005a542c ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a546c ["INT_ADD", "register:40f0:8", ["const:5a546c:8", "const:4:8"]]
+ 005a546c ["CALL", null, ["callee:00c57ea0:8"]]
- 005a542c bytes 9dc91a94
+ 005a546c bytes 8dca1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca28bb735c7599ad08453221f4926b21"></a>

### [`005a5448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5448.md) → [`005a5488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5488.md) _INIT_50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a54c4",
      "incomplete_value": true,
      "site": "005a54e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "005a5484",
      "incomplete_value": true,
      "site": "005a54a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a56a8",
      "incomplete_value": false,
      "site": "005a56bc",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5668",
      "incomplete_value": false,
      "site": "005a567c",
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
            "const:e30:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a56b0",
      "incomplete_value": false,
      "site": "005a56bc",
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
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5670",
      "incomplete_value": false,
      "site": "005a567c",
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
            "const:338:8"
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
      "005a54c4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005a54e8",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005a5508",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a54c4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a54e8",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a5508",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a54e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5448.md#insn-005a54e0) · [`005a567c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5448.md#insn-005a567c) · [`005a5474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5448.md#insn-005a5474)
- 新版 `005a5520`（命令位置の公開資料なし） · `005a56bc`（命令位置の公開資料なし） · `005a54b4`（命令位置の公開資料なし）

~~~diff
- 005a54e0 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005a54e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a54e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a54e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a5520 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005a5520 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5520 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5520 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a54e0 bytes 4a553a91
+ 005a5520 bytes 4a893d91
- 005a567c ["INT_ADD", "register:40f0:8", ["const:5a567c:8", "const:4:8"]]
- 005a567c ["CALL", null, ["callee:00c57e30:8"]]
+ 005a56bc ["INT_ADD", "register:40f0:8", ["const:5a56bc:8", "const:4:8"]]
+ 005a56bc ["CALL", null, ["callee:00c57e30:8"]]
- 005a567c bytes edc81a94
+ 005a56bc bytes ddc91a94
- 005a5474 ["COPY", "tmp:0:8", ["const:338:8"]]
- 005a5474 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005a5474 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005a5474 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005a54b4 ["COPY", "tmp:0:8", ["const:738:8"]]
+ 005a54b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005a54b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005a54b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005a5474 bytes 73e20c91
+ 005a54b4 bytes 73e21c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e497703b649ef9dbd519d2a2f7e4e2e"></a>

### [`005a597c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a597c.md) → [`005a59bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a59bc.md) FUN_005a59bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`007ad2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad2e4.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)
- 新版 呼出元 1件 [`007ad324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)

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
      "definition_site": "005a59d8",
      "incomplete_value": false,
      "site": "005a59dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5998",
      "incomplete_value": false,
      "site": "005a599c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a59dc",
      "DATA",
      [
        "storage",
        "00c6e6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a59dc",
      "DATA",
      [
        "storage",
        "00c6eaf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a597c.md#insn-005a5990) · [`005a5998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a597c.md#insn-005a5998)
- 新版 `005a59d0`（命令位置の公開資料なし） · `005a59d8`（命令位置の公開資料なし）

~~~diff
- 005a5990 ["INT_ADD", "register:40f0:8", ["const:5a5990:8", "const:4:8"]]
- 005a5990 ["CALL", null, ["callee:0059b908:8"]]
+ 005a59d0 ["INT_ADD", "register:40f0:8", ["const:5a59d0:8", "const:4:8"]]
+ 005a59d0 ["CALL", null, ["callee:0059b908:8"]]
- 005a5990 bytes ced7ff97
+ 005a59d0 bytes ced7ff97
- 005a5998 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 005a5998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a59d8 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 005a59d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a59d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a59d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5998 bytes 08c11b91
+ 005a59d8 bytes 08c12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a13a8eac31ff31f4623e21093e341c84"></a>

### [`005a59c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a59c8.md) → [`005a5a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5a08.md) FUN_005a5a08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5a24",
      "incomplete_value": true,
      "site": "005a5a24",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:714:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a59e4",
      "incomplete_value": true,
      "site": "005a59e4",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:638:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005a5a28",
      "incomplete_value": true,
      "site": "005a5a28",
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
      "definition_site": "005a59e8",
      "incomplete_value": true,
      "site": "005a59e8",
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
      "005a5a14",
      "READ",
      [
        "storage",
        "002a5638",
        null,
        "string"
      ]
    ],
    [
      "005a5a1c",
      "READ",
      [
        "storage",
        "002a563d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a5a14",
      "READ",
      [
        "storage",
        "002a5714",
        null,
        "string"
      ]
    ],
    [
      "005a5a1c",
      "READ",
      [
        "storage",
        "002a5719",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a59d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a59c8.md#insn-005a59d0)
- 新版 `005a5a10`（命令位置の公開資料なし）

~~~diff
- 005a59d0 ["COPY", "tmp:0:8", ["const:638:8"]]
- 005a59d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a59d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a59d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a5a10 ["COPY", "tmp:0:8", ["const:714:8"]]
+ 005a5a10 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5a10 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5a10 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a59d0 bytes 4ae11891
+ 005a5a10 bytes 4a511c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-197e9cbf712954b8736998bf40008fe8"></a>

### [`005a5a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5a20.md) → [`005a5a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5a60.md) FUN_005a5a60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`0059bf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059bf04.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bf44.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5ab0",
      "incomplete_value": true,
      "site": "005a5ab0",
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
                "const:b88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5a70",
      "incomplete_value": true,
      "site": "005a5a70",
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
                "const:b48:8"
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
      "005a5a9c",
      "READ",
      [
        "storage",
        "002afb48",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a5a9c",
      "READ",
      [
        "storage",
        "002afb88",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5a20.md#insn-005a5a4c) · [`005a5a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5a20.md#insn-005a5a54) · [`005a5a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5a20.md#insn-005a5a80)
- 新版 `005a5a8c`（命令位置の公開資料なし） · `005a5a94`（命令位置の公開資料なし） · `005a5ac0`（命令位置の公開資料なし）

~~~diff
- 005a5a4c ["INT_ADD", "register:40f0:8", ["const:5a5a4c:8", "const:4:8"]]
- 005a5a4c ["CALL", null, ["callee:0059bf44:8"]]
+ 005a5a8c ["INT_ADD", "register:40f0:8", ["const:5a5a8c:8", "const:4:8"]]
+ 005a5a8c ["CALL", null, ["callee:0059bf44:8"]]
- 005a5a4c bytes 2ed9ff97
+ 005a5a8c bytes 2ed9ff97
- 005a5a54 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 005a5a54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a5a54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a5a54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a5a94 ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 005a5a94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5a94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5a94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a5a54 bytes 29212d91
+ 005a5a94 bytes 29212e91
- 005a5a80 ["INT_ADD", "register:40f0:8", ["const:5a5a80:8", "const:4:8"]]
- 005a5a80 ["CALL", null, ["callee:0045179c:8"]]
+ 005a5ac0 ["INT_ADD", "register:40f0:8", ["const:5a5ac0:8", "const:4:8"]]
+ 005a5ac0 ["CALL", null, ["callee:0045179c:8"]]
- 005a5a80 bytes 37affa97
+ 005a5ac0 bytes 37affa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b915875d45ce14eba540027e8a412840"></a>

### [`005a5af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5af0.md) → [`005a5b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5b30.md) FUN_005a5b30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5b4c",
      "incomplete_value": false,
      "site": "005a5b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5b0c",
      "incomplete_value": false,
      "site": "005a5b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "definition_site": "005a5b64",
      "incomplete_value": false,
      "site": "005a5b64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5b24",
      "incomplete_value": false,
      "site": "005a5b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:748:8"
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
      "005a5b54",
      "DATA",
      [
        "storage",
        "00c6e7f8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a5b64",
      "DATA",
      [
        "storage",
        "00c6e748",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a5b54",
      "DATA",
      [
        "storage",
        "00c6ebf8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a5b64",
      "DATA",
      [
        "storage",
        "00c6eb48",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5af0.md#insn-005a5b04) · [`005a5b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5af0.md#insn-005a5b0c) · [`005a5b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5af0.md#insn-005a5b1c)
- 新版 `005a5b44`（命令位置の公開資料なし） · `005a5b4c`（命令位置の公開資料なし） · `005a5b5c`（命令位置の公開資料なし）

~~~diff
- 005a5b04 ["INT_ADD", "register:40f0:8", ["const:5a5b04:8", "const:4:8"]]
- 005a5b04 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a5b44 ["INT_ADD", "register:40f0:8", ["const:5a5b44:8", "const:4:8"]]
+ 005a5b44 ["CALL", null, ["callee:00c57e90:8"]]
- 005a5b04 bytes e3c71a94
+ 005a5b44 bytes d3c81a94
- 005a5b0c ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 005a5b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5b4c ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 005a5b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5b0c bytes 08e11f91
+ 005a5b4c bytes 08e12f91
- 005a5b1c ["COPY", "tmp:0:8", ["const:748:8"]]
- 005a5b1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5b1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5b1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5b5c ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 005a5b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5b1c bytes 08211d91
+ 005a5b5c bytes 08212d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e8185271699f76e222cfd2713394e9c"></a>

### [`005a5bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5bfc.md) → [`005a5c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5c3c.md) FUN_005a5c3c

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
      "definition_site": "005a5c44",
      "incomplete_value": false,
      "site": "005a5c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5c04",
      "incomplete_value": false,
      "site": "005a5c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a5c48",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a5c48",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5bfc.md#insn-005a5c04) · [`005a5c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5bfc.md#insn-005a5c28)
- 新版 `005a5c44`（命令位置の公開資料なし） · `005a5c68`（命令位置の公開資料なし）

~~~diff
- 005a5c04 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a5c04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a5c04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a5c04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a5c44 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a5c44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5c44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5c44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a5c04 bytes 29011891
+ 005a5c44 bytes 29012891
- 005a5c28 ["INT_ADD", "register:40f0:8", ["const:5a5c28:8", "const:4:8"]]
- 005a5c28 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a5c68 ["INT_ADD", "register:40f0:8", ["const:5a5c68:8", "const:4:8"]]
+ 005a5c68 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a5c28 bytes a2c71a94
+ 005a5c68 bytes 92c81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8de7a14e35346ef5783fd75bf1777de2"></a>

### [`005a5c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5c3c.md) → [`005a5c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5c7c.md) FUN_005a5c7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005a57d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a57d8.md) · 呼出先 4件 [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005a5818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5818.md) · 呼出先 4件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5cb8",
      "incomplete_value": false,
      "site": "005a5cc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5c78",
      "incomplete_value": false,
      "site": "005a5c80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5cfc",
      "incomplete_value": false,
      "site": "005a5d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5cbc",
      "incomplete_value": false,
      "site": "005a5cc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "005a5cc0",
      "DATA",
      [
        "storage",
        "00c6e7a8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a5d00",
      "DATA",
      [
        "storage",
        "00c6e6d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a5cc0",
      "DATA",
      [
        "storage",
        "00c6eba8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a5d00",
      "DATA",
      [
        "storage",
        "00c6ead0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5c3c.md#insn-005a5c70) · [`005a5c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5c3c.md#insn-005a5c78) · [`005a5cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5c3c.md#insn-005a5cb0)
- 新版 `005a5cb0`（命令位置の公開資料なし） · `005a5cb8`（命令位置の公開資料なし） · `005a5cf0`（命令位置の公開資料なし）

~~~diff
- 005a5c70 ["INT_ADD", "register:40f0:8", ["const:5a5c70:8", "const:4:8"]]
- 005a5c70 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a5cb0 ["INT_ADD", "register:40f0:8", ["const:5a5cb0:8", "const:4:8"]]
+ 005a5cb0 ["CALL", null, ["callee:00c57e90:8"]]
- 005a5c70 bytes 88c71a94
+ 005a5cb0 bytes 78c81a94
- 005a5c78 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 005a5c78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5c78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5c78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5cb8 ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 005a5cb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5cb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5cb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5c78 bytes 08a11e91
+ 005a5cb8 bytes 08a12e91
- 005a5cb0 ["INT_ADD", "register:40f0:8", ["const:5a5cb0:8", "const:4:8"]]
- 005a5cb0 ["CALL", null, ["callee:0059b8dc:8"]]
+ 005a5cf0 ["INT_ADD", "register:40f0:8", ["const:5a5cf0:8", "const:4:8"]]
+ 005a5cf0 ["CALL", null, ["callee:0059b8dc:8"]]
- 005a5cb0 bytes fbd6ff97
+ 005a5cf0 bytes fbd6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b3ef158f62f6762b7e82185274c8254"></a>

### [`005a5d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5d3c.md) → [`005a5d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5d7c.md) FUN_005a5d7c

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
      "definition_site": "005a5d80",
      "incomplete_value": false,
      "site": "005a5d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5d40",
      "incomplete_value": false,
      "site": "005a5d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "005a5d84",
      "DATA",
      [
        "storage",
        "00c6e7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5d84",
      "DATA",
      [
        "storage",
        "00c6eba8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5d3c.md#insn-005a5d40)
- 新版 `005a5d80`（命令位置の公開資料なし）

~~~diff
- 005a5d40 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 005a5d40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5d40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5d40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5d80 ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 005a5d80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5d80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5d80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5d40 bytes 08a11e91
+ 005a5d80 bytes 08a12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ce7301dab7f74a205535996515cdcbe"></a>

### [`005a5d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5d7c.md) → [`005a5dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5dbc.md) FUN_005a5dbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005a5dc4",
      "incomplete_value": false,
      "site": "005a5dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5d84",
      "incomplete_value": false,
      "site": "005a5d88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a5dc8",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a5dc8",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5d7c.md#insn-005a5d84)
- 新版 `005a5dc4`（命令位置の公開資料なし）

~~~diff
- 005a5d84 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a5d84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a5d84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a5d84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a5dc4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a5dc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5dc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5dc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a5d84 bytes 29011891
+ 005a5dc4 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d5e148d96aa704eb9e6c70d042f3337"></a>

### [`005a5da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5da0.md) → [`005a5de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5de0.md) FUN_005a5de0

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
      "definition_site": "005a5de4",
      "incomplete_value": false,
      "site": "005a5de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5da4",
      "incomplete_value": false,
      "site": "005a5da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "005a5de8",
      "DATA",
      [
        "storage",
        "00c6e7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5de8",
      "DATA",
      [
        "storage",
        "00c6ebf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5da0.md#insn-005a5da4)
- 新版 `005a5de4`（命令位置の公開資料なし）

~~~diff
- 005a5da4 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 005a5da4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5da4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5da4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5de4 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 005a5de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5da4 bytes 08e11f91
+ 005a5de4 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5e2fc36185533e5e9fac714f6dec5fb"></a>

### [`005a5db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5db0.md) → [`005a5df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5df0.md) FUN_005a5df0

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
      "definition_site": "005a5e00",
      "incomplete_value": false,
      "site": "005a5e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5dc0",
      "incomplete_value": false,
      "site": "005a5dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "005a5e08",
      "DATA",
      [
        "storage",
        "00c6e7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5e08",
      "DATA",
      [
        "storage",
        "00c6ebf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5db0.md#insn-005a5dc0) · [`005a5dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5db0.md#insn-005a5dcc)
- 新版 `005a5e00`（命令位置の公開資料なし） · `005a5e0c`（命令位置の公開資料なし）

~~~diff
- 005a5dc0 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 005a5dc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5dc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5dc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5e00 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 005a5e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5dc0 bytes 08e11f91
+ 005a5e00 bytes 08e12f91
- 005a5dcc ["INT_ADD", "register:40f0:8", ["const:5a5dcc:8", "const:4:8"]]
- 005a5dcc ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a5e0c ["INT_ADD", "register:40f0:8", ["const:5a5e0c:8", "const:4:8"]]
+ 005a5e0c ["CALL", null, ["callee:00c57ea0:8"]]
- 005a5dcc bytes 35c71a94
+ 005a5e0c bytes 25c81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daadc7a35eaabb83d763aa7516f9b726"></a>

### [`005a5de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5de8.md) → [`005a5e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5e28.md) _INIT_51

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.88% / 新版 85.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5e88",
      "incomplete_value": true,
      "site": "005a5ea4",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5e48",
      "incomplete_value": true,
      "site": "005a5e64",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:ef9:8"
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
      "definition_site": "005a5ea8",
      "incomplete_value": true,
      "site": "005a5ec4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "005a5e68",
      "incomplete_value": true,
      "site": "005a5e84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d82:8"
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
      "definition_site": "005a5ec8",
      "incomplete_value": true,
      "site": "005a5ee0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "005a5e88",
      "incomplete_value": true,
      "site": "005a5ea0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e95:8"
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
      "005a5e64",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005a5e88",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005a5ea8",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a5e64",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a5e88",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a5ea8",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5de8.md#insn-005a5e60) · [`005a5e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5de8.md#insn-005a5e80) · [`005a601c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5de8.md#insn-005a601c)
- 新版 `005a5ea0`（命令位置の公開資料なし） · `005a5ec0`（命令位置の公開資料なし） · `005a605c`（命令位置の公開資料なし）

~~~diff
- 005a5e60 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005a5e60 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a5e60 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a5e60 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a5ea0 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005a5ea0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5ea0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5ea0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a5e60 bytes 4a093691
+ 005a5ea0 bytes 4a093791
- 005a5e80 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005a5e80 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a5e80 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a5e80 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a5ec0 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005a5ec0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5ec0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5ec0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a5e80 bytes 4a553a91
+ 005a5ec0 bytes 4a893d91
- 005a601c ["INT_ADD", "register:40f0:8", ["const:5a601c:8", "const:4:8"]]
- 005a601c ["CALL", null, ["callee:00c57e30:8"]]
+ 005a605c ["INT_ADD", "register:40f0:8", ["const:5a605c:8", "const:4:8"]]
+ 005a605c ["CALL", null, ["callee:00c57e30:8"]]
- 005a601c bytes 85c61a94
+ 005a605c bytes 75c71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0f4fb2fc54e80ca25b2d5b96047ceea"></a>

### [`005a6178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6178.md) → [`005a61b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a61b8.md) FUN_005a61b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005a6658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6658.md) [`005a69dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a69dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005a6698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6698.md) [`005a6a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6a1c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.21% / 新版 96.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a6204",
      "incomplete_value": true,
      "site": "005a6204",
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a61c4",
      "incomplete_value": true,
      "site": "005a61c4",
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
                "const:165:8"
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
      "definition_site": "005a633c",
      "incomplete_value": true,
      "site": "005a633c",
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
                "const:b88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a62fc",
      "incomplete_value": true,
      "site": "005a62fc",
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
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a63c0",
      "incomplete_value": true,
      "site": "005a63c0",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:686:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6380",
      "incomplete_value": true,
      "site": "005a6380",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:5aa:8"
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
      "005a61e8",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "005a632c",
      "READ",
      [
        "storage",
        "002afb48",
        null,
        "string"
      ]
    ],
    [
      "005a63b0",
      "READ",
      [
        "storage",
        "002a75aa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a61e8",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005a632c",
      "READ",
      [
        "storage",
        "002afb88",
        null,
        "string"
      ]
    ],
    [
      "005a63b0",
      "READ",
      [
        "storage",
        "002a7686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6178.md#insn-005a6204) · [`005a633c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6178.md#insn-005a633c) · [`005a619c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6178.md#insn-005a619c)
- 新版 `005a6244`（命令位置の公開資料なし） · `005a637c`（命令位置の公開資料なし） · `005a61dc`（命令位置の公開資料なし）

~~~diff
- 005a6204 ["INT_ADD", "register:40f0:8", ["const:5a6204:8", "const:4:8"]]
- 005a6204 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a6244 ["INT_ADD", "register:40f0:8", ["const:5a6244:8", "const:4:8"]]
+ 005a6244 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a6204 bytes 2bc61a94
+ 005a6244 bytes 1bc71a94
- 005a633c ["INT_ADD", "register:40f0:8", ["const:5a633c:8", "const:4:8"]]
- 005a633c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a637c ["INT_ADD", "register:40f0:8", ["const:5a637c:8", "const:4:8"]]
+ 005a637c ["CALL", null, ["callee:00c57eb0:8"]]
- 005a633c bytes ddc51a94
+ 005a637c bytes cdc61a94
- 005a619c ["COPY", "tmp:0:8", ["const:165:8"]]
- 005a619c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a619c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a619c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a61dc ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 005a61dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a61dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a61dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a619c bytes 4a950591
+ 005a61dc bytes 4a950691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea300fc60b595295b63d45b692a7abe7"></a>

### [`005a6658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6658.md) → [`005a6698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6698.md) FUN_005a6698

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005a6178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6178.md) · 呼出先 3件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005a61b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a61b8.md) · 呼出先 3件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.21% / 新版 92.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a66d4",
      "incomplete_value": true,
      "site": "005a66d4",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:2e1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6694",
      "incomplete_value": true,
      "site": "005a6694",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:2a1:8"
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
      "005a66bc",
      "READ",
      [
        "storage",
        "002c12a1",
        null,
        "string"
      ]
    ],
    [
      "005a66cc",
      "READ",
      [
        "storage",
        "002c12a6",
        null,
        "string"
      ]
    ],
    [
      "005a6728",
      "READ",
      [
        "storage",
        "002a43cf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a66bc",
      "READ",
      [
        "storage",
        "002c12e1",
        null,
        "string"
      ]
    ],
    [
      "005a66cc",
      "READ",
      [
        "storage",
        "002c12e6",
        null,
        "string"
      ]
    ],
    [
      "005a6728",
      "READ",
      [
        "storage",
        "002a449c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6658.md#insn-005a6674) · [`005a66a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6658.md#insn-005a66a8) · [`005a66c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6658.md#insn-005a66c4)
- 新版 `005a66b4`（命令位置の公開資料なし） · `005a66e8`（命令位置の公開資料なし） · `005a6704`（命令位置の公開資料なし）

~~~diff
- 005a6674 ["COPY", "tmp:0:8", ["const:2a1:8"]]
- 005a6674 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a6674 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a6674 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a66b4 ["COPY", "tmp:0:8", ["const:2e1:8"]]
+ 005a66b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a66b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a66b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a6674 bytes 29850a91
+ 005a66b4 bytes 29850b91
- 005a66a8 ["INT_ADD", "register:40f0:8", ["const:5a66a8:8", "const:4:8"]]
- 005a66a8 ["CALL", null, ["callee:0044108c:8"]]
+ 005a66e8 ["INT_ADD", "register:40f0:8", ["const:5a66e8:8", "const:4:8"]]
+ 005a66e8 ["CALL", null, ["callee:0044108c:8"]]
- 005a66a8 bytes 696afa97
+ 005a66e8 bytes 696afa97
- 005a66c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005a66c4 ["INT_ADD", "register:40f0:8", ["const:5a66c4:8", "const:4:8"]]
- 005a66c4 ["CALLIND", null, ["register:0:8"]]
+ 005a6704 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005a6704 ["INT_ADD", "register:40f0:8", ["const:5a6704:8", "const:4:8"]]
+ 005a6704 ["CALLIND", null, ["register:0:8"]]
- 005a66c4 bytes 00013fd6
+ 005a6704 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87f1d557a1c78662bc7f9089ba3f36f3"></a>

### [`005a6814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6814.md) → [`005a6854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6854.md) FUN_005a6854

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005a6870",
      "incomplete_value": false,
      "site": "005a6878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6830",
      "incomplete_value": false,
      "site": "005a6838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "definition_site": "005a6888",
      "incomplete_value": false,
      "site": "005a6888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6848",
      "incomplete_value": false,
      "site": "005a6848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:868:8"
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
      "005a6878",
      "DATA",
      [
        "storage",
        "00c6e970",
        null,
        "undefined *"
      ]
    ],
    [
      "005a6888",
      "DATA",
      [
        "storage",
        "00c6e868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a6878",
      "DATA",
      [
        "storage",
        "00c6ed70",
        null,
        "undefined *"
      ]
    ],
    [
      "005a6888",
      "DATA",
      [
        "storage",
        "00c6ec68",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6814.md#insn-005a6828) · [`005a6830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6814.md#insn-005a6830) · [`005a683c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6814.md#insn-005a683c)
- 新版 `005a6868`（命令位置の公開資料なし） · `005a6870`（命令位置の公開資料なし）

~~~diff
- 005a6828 ["INT_ADD", "register:40f0:8", ["const:5a6828:8", "const:4:8"]]
- 005a6828 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a6868 ["INT_ADD", "register:40f0:8", ["const:5a6868:8", "const:4:8"]]
+ 005a6868 ["CALL", null, ["callee:00c57e90:8"]]
- 005a6828 bytes 9ac41a94
+ 005a6868 bytes 8ac51a94
- 005a6830 ["COPY", "tmp:0:8", ["const:970:8"]]
- 005a6830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a6830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a6830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a6870 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 005a6870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a6830 bytes 08c12591
+ 005a6870 bytes 08c13591
- 005a683c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005a683c bytes 48360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ffe720edbc224e42c0b298b0585fa77"></a>

### [`005a685c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a685c.md) → [`005a689c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a689c.md) FUN_005a689c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a68b8",
      "incomplete_value": true,
      "site": "005a68bc",
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
      "definition_site": "005a6878",
      "incomplete_value": true,
      "site": "005a687c",
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
      "005a68b0",
      "READ",
      [
        "storage",
        "00c9af20",
        null,
        "pointer"
      ]
    ],
    [
      "005a68bc",
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
      "005a68b0",
      "READ",
      [
        "storage",
        "00c9b320",
        null,
        "pointer"
      ]
    ],
    [
      "005a68bc",
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

- 旧版 [`005a6868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a685c.md#insn-005a6868) · [`005a6870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a685c.md#insn-005a6870) · [`005a6888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a685c.md#insn-005a6888)
- 新版 `005a68a8`（命令位置の公開資料なし） · `005a68b0`（命令位置の公開資料なし） · `005a68c8`（命令位置の公開資料なし）

~~~diff
- 005a6868 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005a68a8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005a6868 bytes a8370090
+ 005a68a8 bytes a83700b0
- 005a6870 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
- 005a6870 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a68b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:320:8"]]
+ 005a68b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a6870 bytes 089147f9
+ 005a68b0 bytes 089141f9
- 005a6888 ["INT_ADD", "register:40f0:8", ["const:5a6888:8", "const:4:8"]]
- 005a6888 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a68c8 ["INT_ADD", "register:40f0:8", ["const:5a68c8:8", "const:4:8"]]
+ 005a68c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a6888 bytes 8ac41a94
+ 005a68c8 bytes 7ac51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ded109a1248ef9cb24748bc51cb2d601"></a>

### [`005a68ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a68ac.md) → [`005a68ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a68ec.md) FUN_005a68ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005a6914",
      "incomplete_value": false,
      "site": "005a6918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a68d4",
      "incomplete_value": false,
      "site": "005a68d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a6918",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a6918",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a68c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a68ac.md#insn-005a68c8) · [`005a68d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a68ac.md#insn-005a68d4)
- 新版 `005a6908`（命令位置の公開資料なし） · `005a6914`（命令位置の公開資料なし）

~~~diff
- 005a68c8 ["INT_ADD", "register:40f0:8", ["const:5a68c8:8", "const:4:8"]]
- 005a68c8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a6908 ["INT_ADD", "register:40f0:8", ["const:5a6908:8", "const:4:8"]]
+ 005a6908 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a68c8 bytes 7ac41a94
+ 005a6908 bytes 6ac51a94
- 005a68d4 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a68d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a68d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a68d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a6914 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a6914 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a6914 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a6914 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a68d4 bytes 29011891
+ 005a6914 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e23e978dc7d08bc1f65837263962a64"></a>

### [`005a68fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a68fc.md) → [`005a693c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a693c.md) FUN_005a693c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005a6964",
      "incomplete_value": false,
      "site": "005a6968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6924",
      "incomplete_value": false,
      "site": "005a6928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a6968",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a6968",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a68fc.md#insn-005a6918) · [`005a6924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a68fc.md#insn-005a6924) · [`005a6934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a68fc.md#insn-005a6934)
- 新版 `005a6958`（命令位置の公開資料なし） · `005a6964`（命令位置の公開資料なし） · `005a6974`（命令位置の公開資料なし）

~~~diff
- 005a6918 ["INT_ADD", "register:40f0:8", ["const:5a6918:8", "const:4:8"]]
- 005a6918 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a6958 ["INT_ADD", "register:40f0:8", ["const:5a6958:8", "const:4:8"]]
+ 005a6958 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a6918 bytes 66c41a94
+ 005a6958 bytes 56c51a94
- 005a6924 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a6924 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a6924 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a6924 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a6964 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a6964 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a6964 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a6964 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a6924 bytes 29011891
+ 005a6964 bytes 29012891
- 005a6934 ["INT_ADD", "register:40f0:8", ["const:5a6934:8", "const:4:8"]]
- 005a6934 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a6974 ["INT_ADD", "register:40f0:8", ["const:5a6974:8", "const:4:8"]]
+ 005a6974 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a6934 bytes 5fc41a94
+ 005a6974 bytes 4fc51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cf563cb9f502c7e2cba781ae9101990"></a>

### [`005a6948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6948.md) → [`005a6988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6988.md) FUN_005a6988

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
      "definition_site": "005a698c",
      "incomplete_value": false,
      "site": "005a6990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a694c",
      "incomplete_value": false,
      "site": "005a6950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a6990",
      "DATA",
      [
        "storage",
        "00c6e920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a6990",
      "DATA",
      [
        "storage",
        "00c6ed20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6948.md#insn-005a694c)
- 新版 `005a698c`（命令位置の公開資料なし）

~~~diff
- 005a694c ["COPY", "tmp:0:8", ["const:920:8"]]
- 005a694c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a694c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a694c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a698c ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 005a698c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a698c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a698c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a694c bytes 08812491
+ 005a698c bytes 08813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c237dbe957b3cbffc1b491e041bf7f65"></a>

### [`005a6958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6958.md) → [`005a6998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6998.md) FUN_005a6998

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
      "definition_site": "005a69a8",
      "incomplete_value": false,
      "site": "005a69b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6968",
      "incomplete_value": false,
      "site": "005a6970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "005a69b0",
      "DATA",
      [
        "storage",
        "00c6e920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a69b0",
      "DATA",
      [
        "storage",
        "00c6ed20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6958.md#insn-005a6968) · [`005a6974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6958.md#insn-005a6974)
- 新版 `005a69a8`（命令位置の公開資料なし） · `005a69b4`（命令位置の公開資料なし）

~~~diff
- 005a6968 ["COPY", "tmp:0:8", ["const:920:8"]]
- 005a6968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a6968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a6968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a69a8 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 005a69a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a69a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a69a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a6968 bytes 08812491
+ 005a69a8 bytes 08813491
- 005a6974 ["INT_ADD", "register:40f0:8", ["const:5a6974:8", "const:4:8"]]
- 005a6974 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a69b4 ["INT_ADD", "register:40f0:8", ["const:5a69b4:8", "const:4:8"]]
+ 005a69b4 ["CALL", null, ["callee:00c57ea0:8"]]
- 005a6974 bytes 4bc41a94
+ 005a69b4 bytes 3bc51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc7ed1e365788b4cc2942578fea8cd47"></a>

### [`005a6988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6988.md) → [`005a69c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a69c8.md) FUN_005a69c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005a69f0",
      "incomplete_value": false,
      "site": "005a69f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a69b0",
      "incomplete_value": false,
      "site": "005a69b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a69f4",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a69f4",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a69a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6988.md#insn-005a69a4) · [`005a69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6988.md#insn-005a69b0)
- 新版 `005a69e4`（命令位置の公開資料なし） · `005a69f0`（命令位置の公開資料なし）

~~~diff
- 005a69a4 ["INT_ADD", "register:40f0:8", ["const:5a69a4:8", "const:4:8"]]
- 005a69a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a69e4 ["INT_ADD", "register:40f0:8", ["const:5a69e4:8", "const:4:8"]]
+ 005a69e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a69a4 bytes 43c41a94
+ 005a69e4 bytes 33c51a94
- 005a69b0 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a69b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a69b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a69b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a69f0 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a69f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a69f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a69f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a69b0 bytes 29011891
+ 005a69f0 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31687f8b11565e1a088cbdcbcfd78f35"></a>

### [`005a69dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a69dc.md) → [`005a6a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6a1c.md) FUN_005a6a1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005a6178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6178.md) · 呼出先 3件 [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005a61b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a61b8.md) · 呼出先 3件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a6a98",
      "incomplete_value": false,
      "site": "005a6aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6a58",
      "incomplete_value": false,
      "site": "005a6a60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "005a6aa0",
      "DATA",
      [
        "storage",
        "00c6e848",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a6aa0",
      "DATA",
      [
        "storage",
        "00c6ec48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a69dc.md#insn-005a6a50) · [`005a6a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a69dc.md#insn-005a6a58) · [`005a6a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a69dc.md#insn-005a6a88)
- 新版 `005a6a90`（命令位置の公開資料なし） · `005a6a98`（命令位置の公開資料なし） · `005a6ac8`（命令位置の公開資料なし）

~~~diff
- 005a6a50 ["INT_ADD", "register:40f0:8", ["const:5a6a50:8", "const:4:8"]]
- 005a6a50 ["CALL", null, ["callee:0059b8dc:8"]]
+ 005a6a90 ["INT_ADD", "register:40f0:8", ["const:5a6a90:8", "const:4:8"]]
+ 005a6a90 ["CALL", null, ["callee:0059b8dc:8"]]
- 005a6a50 bytes 93d3ff97
+ 005a6a90 bytes 93d3ff97
- 005a6a58 ["COPY", "tmp:0:8", ["const:848:8"]]
- 005a6a58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a6a58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a6a58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a6a98 ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 005a6a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a6a58 bytes 08212191
+ 005a6a98 bytes 08213191
- 005a6a88 ["INT_ADD", "register:40f0:8", ["const:5a6a88:8", "const:4:8"]]
- 005a6a88 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a6ac8 ["INT_ADD", "register:40f0:8", ["const:5a6ac8:8", "const:4:8"]]
+ 005a6ac8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a6a88 bytes 0ac41a94
+ 005a6ac8 bytes fac41a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8610a0f6e1a10e3fdcd843f70a6339d"></a>

### [`005a6af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6af4.md) → [`005a6b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6b34.md) FUN_005a6b34

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
      "definition_site": "005a6b38",
      "incomplete_value": false,
      "site": "005a6b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6af8",
      "incomplete_value": false,
      "site": "005a6afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "005a6b3c",
      "DATA",
      [
        "storage",
        "00c6e970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a6b3c",
      "DATA",
      [
        "storage",
        "00c6ed70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6af4.md#insn-005a6af8)
- 新版 `005a6b38`（命令位置の公開資料なし）

~~~diff
- 005a6af8 ["COPY", "tmp:0:8", ["const:970:8"]]
- 005a6af8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a6af8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a6af8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a6b38 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 005a6b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a6af8 bytes 08c12591
+ 005a6b38 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9226c3e440aaac3da8f2e29fa3b9afd"></a>

### [`005a6b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6b04.md) → [`005a6b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6b44.md) FUN_005a6b44

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
      "definition_site": "005a6b54",
      "incomplete_value": false,
      "site": "005a6b5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6b14",
      "incomplete_value": false,
      "site": "005a6b1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "005a6b5c",
      "DATA",
      [
        "storage",
        "00c6e970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a6b5c",
      "DATA",
      [
        "storage",
        "00c6ed70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6b04.md#insn-005a6b14) · [`005a6b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6b04.md#insn-005a6b20)
- 新版 `005a6b54`（命令位置の公開資料なし） · `005a6b60`（命令位置の公開資料なし）

~~~diff
- 005a6b14 ["COPY", "tmp:0:8", ["const:970:8"]]
- 005a6b14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a6b14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a6b14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a6b54 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 005a6b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a6b14 bytes 08c12591
+ 005a6b54 bytes 08c13591
- 005a6b20 ["INT_ADD", "register:40f0:8", ["const:5a6b20:8", "const:4:8"]]
- 005a6b20 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a6b60 ["INT_ADD", "register:40f0:8", ["const:5a6b60:8", "const:4:8"]]
+ 005a6b60 ["CALL", null, ["callee:00c57ea0:8"]]
- 005a6b20 bytes e0c31a94
+ 005a6b60 bytes d0c41a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1f9eda02a08e44554e7aefe8b0b5867"></a>

### [`005a6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6ecc.md) → [`005a6f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6f0c.md) FUN_005a6f0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005a7a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7a18.md) [`005a7c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7c74.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005a7a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7a58.md) [`005a7cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7cb4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.03% / 新版 99.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a6f60",
      "incomplete_value": true,
      "site": "005a6f60",
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6f20",
      "incomplete_value": true,
      "site": "005a6f20",
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
                "const:165:8"
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
      "005a6f44",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a6f44",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6ecc.md#insn-005a6f60) · [`005a6ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6ecc.md#insn-005a6ef8) · [`005a6f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6ecc.md#insn-005a6f30)
- 新版 `005a6fa0`（命令位置の公開資料なし） · `005a6f38`（命令位置の公開資料なし） · `005a6f70`（命令位置の公開資料なし）

~~~diff
- 005a6f60 ["INT_ADD", "register:40f0:8", ["const:5a6f60:8", "const:4:8"]]
- 005a6f60 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a6fa0 ["INT_ADD", "register:40f0:8", ["const:5a6fa0:8", "const:4:8"]]
+ 005a6fa0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a6f60 bytes d4c21a94
+ 005a6fa0 bytes c4c31a94
- 005a6ef8 ["COPY", "tmp:0:8", ["const:165:8"]]
- 005a6ef8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a6ef8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a6ef8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a6f38 ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 005a6f38 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a6f38 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a6f38 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a6ef8 bytes 4a950591
+ 005a6f38 bytes 4a950691
- 005a6f30 ["INT_ADD", "register:40f0:8", ["const:5a6f30:8", "const:4:8"]]
- 005a6f30 ["CALL", null, ["callee:0044108c:8"]]
+ 005a6f70 ["INT_ADD", "register:40f0:8", ["const:5a6f70:8", "const:4:8"]]
+ 005a6f70 ["CALL", null, ["callee:0044108c:8"]]
- 005a6f30 bytes 4768fa97
+ 005a6f70 bytes 4768fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b5ef03971cbb02bbdc5b1cbfa2c17bf"></a>

### [`005a74f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a74f4.md) → [`005a7534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7534.md) FUN_005a7534

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009a4f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a4/009a4f24.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)
- 新版 呼出元 1件 [`009a50c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a5/009a50c0.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)

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
      "definition_site": "005a7550",
      "incomplete_value": false,
      "site": "005a7554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7510",
      "incomplete_value": false,
      "site": "005a7514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "005a7554",
      "DATA",
      [
        "storage",
        "00c6e9e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a7554",
      "DATA",
      [
        "storage",
        "00c6ede0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a74f4.md#insn-005a7508) · [`005a7510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a74f4.md#insn-005a7510)
- 新版 `005a7548`（命令位置の公開資料なし） · `005a7550`（命令位置の公開資料なし）

~~~diff
- 005a7508 ["INT_ADD", "register:40f0:8", ["const:5a7508:8", "const:4:8"]]
- 005a7508 ["CALL", null, ["callee:0059b908:8"]]
+ 005a7548 ["INT_ADD", "register:40f0:8", ["const:5a7548:8", "const:4:8"]]
+ 005a7548 ["CALL", null, ["callee:0059b908:8"]]
- 005a7508 bytes f0d0ff97
+ 005a7548 bytes f0d0ff97
- 005a7510 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 005a7510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7550 ["COPY", "tmp:0:8", ["const:de0:8"]]
+ 005a7550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7510 bytes 08812791
+ 005a7550 bytes 08813791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15204ae4674b0526ae5ce285e581e592"></a>

### [`005a752c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a752c.md) → [`005a756c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a756c.md) FUN_005a756c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57dd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c581d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a759c",
      "incomplete_value": true,
      "site": "005a75a8",
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
            "const:fd1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a755c",
      "incomplete_value": true,
      "site": "005a7568",
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
            "const:f91:8"
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
      "005a759c",
      "PARAM",
      [
        "storage",
        "002bff91",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a759c",
      "PARAM",
      [
        "storage",
        "002bffd1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a752c.md#insn-005a7568) · [`005a7554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a752c.md#insn-005a7554) · [`005a755c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a752c.md#insn-005a755c)
- 新版 `005a75a8`（命令位置の公開資料なし） · `005a7594`（命令位置の公開資料なし） · `005a759c`（命令位置の公開資料なし）

~~~diff
- 005a7568 ["INT_ADD", "register:40f0:8", ["const:5a7568:8", "const:4:8"]]
- 005a7568 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a75a8 ["INT_ADD", "register:40f0:8", ["const:5a75a8:8", "const:4:8"]]
+ 005a75a8 ["CALL", null, ["callee:00c57f60:8"]]
- 005a7568 bytes 7ec11a94
+ 005a75a8 bytes 6ec21a94
- 005a7554 ["INT_ADD", "register:40f0:8", ["const:5a7554:8", "const:4:8"]]
- 005a7554 ["CALL", null, ["callee:00c581d0:8"]]
+ 005a7594 ["INT_ADD", "register:40f0:8", ["const:5a7594:8", "const:4:8"]]
+ 005a7594 ["CALL", null, ["callee:00c581d0:8"]]
- 005a7554 bytes 1fc21a94
+ 005a7594 bytes 0fc31a94
- 005a755c ["COPY", "tmp:0:8", ["const:f91:8"]]
- 005a755c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005a755c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005a755c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005a759c ["COPY", "tmp:0:8", ["const:fd1:8"]]
+ 005a759c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005a759c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005a759c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005a755c bytes 42443e91
+ 005a759c bytes 42443f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28d3ebc5c9dda95ea482e2bb616c2b28"></a>

### [`005a7614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7614.md) → [`005a7654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7654.md) FUN_005a7654

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005a7670",
      "incomplete_value": false,
      "site": "005a7678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7630",
      "incomplete_value": false,
      "site": "005a7638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "definition_site": "005a7688",
      "incomplete_value": false,
      "site": "005a7688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7648",
      "incomplete_value": false,
      "site": "005a7648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a38:8"
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
      "005a7678",
      "DATA",
      [
        "storage",
        "00c6eae8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a7688",
      "DATA",
      [
        "storage",
        "00c6ea38",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a7678",
      "DATA",
      [
        "storage",
        "00c6eee8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a7688",
      "DATA",
      [
        "storage",
        "00c6ee38",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7614.md#insn-005a7628) · [`005a7630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7614.md#insn-005a7630) · [`005a763c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7614.md#insn-005a763c)
- 新版 `005a7668`（命令位置の公開資料なし） · `005a7670`（命令位置の公開資料なし）

~~~diff
- 005a7628 ["INT_ADD", "register:40f0:8", ["const:5a7628:8", "const:4:8"]]
- 005a7628 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a7668 ["INT_ADD", "register:40f0:8", ["const:5a7668:8", "const:4:8"]]
+ 005a7668 ["CALL", null, ["callee:00c57e90:8"]]
- 005a7628 bytes 1ac11a94
+ 005a7668 bytes 0ac21a94
- 005a7630 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 005a7630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7670 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 005a7670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7630 bytes 08a12b91
+ 005a7670 bytes 08a13b91
- 005a763c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005a763c bytes 283600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-740e78a5c402cba04b3426212b3bff79"></a>

### [`005a765c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a765c.md) → [`005a769c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a769c.md) FUN_005a769c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a76b8",
      "incomplete_value": true,
      "site": "005a76bc",
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
      "definition_site": "005a7678",
      "incomplete_value": true,
      "site": "005a767c",
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
      "005a76b0",
      "READ",
      [
        "storage",
        "00c9af20",
        null,
        "pointer"
      ]
    ],
    [
      "005a76bc",
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
      "005a76b0",
      "READ",
      [
        "storage",
        "00c9b320",
        null,
        "pointer"
      ]
    ],
    [
      "005a76bc",
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

- 旧版 [`005a7668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a765c.md#insn-005a7668) · [`005a7670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a765c.md#insn-005a7670) · [`005a7688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a765c.md#insn-005a7688)
- 新版 `005a76a8`（命令位置の公開資料なし） · `005a76b0`（命令位置の公開資料なし） · `005a76c8`（命令位置の公開資料なし）

~~~diff
- 005a7668 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005a76a8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005a7668 bytes 883700f0
+ 005a76a8 bytes a8370090
- 005a7670 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
- 005a7670 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a76b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:320:8"]]
+ 005a76b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a7670 bytes 089147f9
+ 005a76b0 bytes 089141f9
- 005a7688 ["INT_ADD", "register:40f0:8", ["const:5a7688:8", "const:4:8"]]
- 005a7688 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a76c8 ["INT_ADD", "register:40f0:8", ["const:5a76c8:8", "const:4:8"]]
+ 005a76c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a7688 bytes 0ac11a94
+ 005a76c8 bytes fac11a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2eb1302ff53f4ed23b110c4a579c203"></a>

### [`005a76ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a76ac.md) → [`005a76ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a76ec.md) FUN_005a76ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005a7750",
      "incomplete_value": false,
      "site": "005a7754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7710",
      "incomplete_value": false,
      "site": "005a7714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "005a7754",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a7754",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a76f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a76ac.md#insn-005a76f4) · [`005a7704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a76ac.md#insn-005a7704) · [`005a7710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a76ac.md#insn-005a7710)
- 新版 `005a7734`（命令位置の公開資料なし） · `005a7744`（命令位置の公開資料なし） · `005a7750`（命令位置の公開資料なし）

~~~diff
- 005a76f4 ["INT_ADD", "register:40f0:8", ["const:5a76f4:8", "const:4:8"]]
- 005a76f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a7734 ["INT_ADD", "register:40f0:8", ["const:5a7734:8", "const:4:8"]]
+ 005a7734 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a76f4 bytes efc01a94
+ 005a7734 bytes dfc11a94
- 005a7704 ["INT_ADD", "register:40f0:8", ["const:5a7704:8", "const:4:8"]]
- 005a7704 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a7744 ["INT_ADD", "register:40f0:8", ["const:5a7744:8", "const:4:8"]]
+ 005a7744 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a7704 bytes ebc01a94
+ 005a7744 bytes dbc11a94
- 005a7710 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a7710 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a7710 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a7710 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a7750 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a7750 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a7750 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a7750 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a7710 bytes 29011891
+ 005a7750 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67a180970b38cc1f98dfb1a3c4208651"></a>

### [`005a7740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7740.md) → [`005a7780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7780.md) FUN_005a7780

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a77e4",
      "incomplete_value": true,
      "site": "005a77e8",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a77a4",
      "incomplete_value": true,
      "site": "005a77a8",
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
            "const:600:8"
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
      "005a77e8",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a77e8",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7740.md#insn-005a7788) · [`005a7798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7740.md#insn-005a7798) · [`005a77a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7740.md#insn-005a77a4)
- 新版 `005a77c8`（命令位置の公開資料なし） · `005a77d8`（命令位置の公開資料なし） · `005a77e4`（命令位置の公開資料なし）

~~~diff
- 005a7788 ["INT_ADD", "register:40f0:8", ["const:5a7788:8", "const:4:8"]]
- 005a7788 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a77c8 ["INT_ADD", "register:40f0:8", ["const:5a77c8:8", "const:4:8"]]
+ 005a77c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a7788 bytes cac01a94
+ 005a77c8 bytes bac11a94
- 005a7798 ["INT_ADD", "register:40f0:8", ["const:5a7798:8", "const:4:8"]]
- 005a7798 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a77d8 ["INT_ADD", "register:40f0:8", ["const:5a77d8:8", "const:4:8"]]
+ 005a77d8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a7798 bytes c6c01a94
+ 005a77d8 bytes b6c11a94
- 005a77a4 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a77a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a77a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a77a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a77e4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a77e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a77e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a77e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a77a4 bytes 29011891
+ 005a77e4 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d1a8fa21beb13b4bd29e97d736b1724"></a>

### [`005a79b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a79b0.md) → [`005a79f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a79f0.md) FUN_005a79f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a77cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a77cc.md) [`005a7a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7a18.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`005a780c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a780c.md) [`005a7a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7a58.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005a79fc",
      "incomplete_value": true,
      "site": "005a7a00",
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
    "old": {
      "definition_site": "005a79bc",
      "incomplete_value": true,
      "site": "005a79c0",
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
            "const:f0c:8"
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
      "005a79fc",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a79fc",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a79c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a79b0.md#insn-005a79c0) · [`005a79bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a79b0.md#insn-005a79bc)
- 新版 `005a7a00`（命令位置の公開資料なし） · `005a79fc`（命令位置の公開資料なし）

~~~diff
- 005a79c0 ["INT_ADD", "register:40f0:8", ["const:5a79c0:8", "const:4:8"]]
- 005a79c0 ["CALL", null, ["callee:0043b778:8"]]
+ 005a7a00 ["INT_ADD", "register:40f0:8", ["const:5a7a00:8", "const:4:8"]]
+ 005a7a00 ["CALL", null, ["callee:0043b778:8"]]
- 005a79c0 bytes 5e4ffa97
+ 005a7a00 bytes 5e4ffa97
- 005a79bc ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005a79bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005a79bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005a79bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005a79fc ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005a79fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005a79fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005a79fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005a79bc bytes 00303c91
+ 005a79fc bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d54cb0e01d6e8870869cdcb465b89004"></a>

### [`005a7c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7c74.md) → [`005a7cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7cb4.md) FUN_005a7cb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005a6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6ecc.md) · 呼出先 3件 [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`005a77cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a77cc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005a6f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6f0c.md) · 呼出先 3件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`005a780c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a780c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a7cf4",
      "incomplete_value": true,
      "site": "005a7d00",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7cb4",
      "incomplete_value": true,
      "site": "005a7cc0",
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
            "const:a98:8"
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
      "definition_site": "005a7d24",
      "incomplete_value": false,
      "site": "005a7d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7ce4",
      "incomplete_value": false,
      "site": "005a7ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "005a7d00",
      "DATA",
      [
        "storage",
        "00c6ea98",
        null,
        "undefined *"
      ]
    ],
    [
      "005a7d24",
      "DATA",
      [
        "storage",
        "00c6e9c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a7d00",
      "DATA",
      [
        "storage",
        "00c6ee98",
        null,
        "undefined *"
      ]
    ],
    [
      "005a7d24",
      "DATA",
      [
        "storage",
        "00c6edc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7c74.md#insn-005a7ca0) · [`005a7cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7c74.md#insn-005a7cb4) · [`005a7ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7c74.md#insn-005a7ccc)
- 新版 `005a7ce0`（命令位置の公開資料なし） · `005a7cf4`（命令位置の公開資料なし） · `005a7d0c`（命令位置の公開資料なし）

~~~diff
- 005a7ca0 ["INT_ADD", "register:40f0:8", ["const:5a7ca0:8", "const:4:8"]]
- 005a7ca0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a7ce0 ["INT_ADD", "register:40f0:8", ["const:5a7ce0:8", "const:4:8"]]
+ 005a7ce0 ["CALL", null, ["callee:00c57e90:8"]]
- 005a7ca0 bytes 7cbf1a94
+ 005a7ce0 bytes 6cc01a94
- 005a7cb4 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 005a7cb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7cb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7cb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7cf4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005a7cf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7cf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7cf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7cb4 bytes 08612a91
+ 005a7cf4 bytes 08613a91
- 005a7ccc ["INT_ADD", "register:40f0:8", ["const:5a7ccc:8", "const:4:8"]]
- 005a7ccc ["CALL", null, ["callee:0059b8dc:8"]]
+ 005a7d0c ["INT_ADD", "register:40f0:8", ["const:5a7d0c:8", "const:4:8"]]
+ 005a7d0c ["CALL", null, ["callee:0059b8dc:8"]]
- 005a7ccc bytes f4ceff97
+ 005a7d0c bytes f4ceff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-774c4eba69245715070e2e99876ed458"></a>

### [`005a7d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7d54.md) → [`005a7d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7d94.md) FUN_005a7d94

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
      "definition_site": "005a7d98",
      "incomplete_value": false,
      "site": "005a7d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7d58",
      "incomplete_value": false,
      "site": "005a7d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "005a7d9c",
      "DATA",
      [
        "storage",
        "00c6ea98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a7d9c",
      "DATA",
      [
        "storage",
        "00c6ee98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7d54.md#insn-005a7d58)
- 新版 `005a7d98`（命令位置の公開資料なし）

~~~diff
- 005a7d58 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 005a7d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7d98 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005a7d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7d58 bytes 08612a91
+ 005a7d98 bytes 08613a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a143b41c18212d1634b988a211d6f7bb"></a>

### [`005a7d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7d64.md) → [`005a7da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7da4.md) FUN_005a7da4

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
      "definition_site": "005a7db4",
      "incomplete_value": false,
      "site": "005a7dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7d74",
      "incomplete_value": false,
      "site": "005a7d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a7dbc",
      "DATA",
      [
        "storage",
        "00c6ea98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a7dbc",
      "DATA",
      [
        "storage",
        "00c6ee98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7d64.md#insn-005a7d74) · [`005a7d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7d64.md#insn-005a7d80)
- 新版 `005a7db4`（命令位置の公開資料なし） · `005a7dc0`（命令位置の公開資料なし）

~~~diff
- 005a7d74 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 005a7d74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7d74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7d74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7db4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005a7db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7d74 bytes 08612a91
+ 005a7db4 bytes 08613a91
- 005a7d80 ["INT_ADD", "register:40f0:8", ["const:5a7d80:8", "const:4:8"]]
- 005a7d80 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a7dc0 ["INT_ADD", "register:40f0:8", ["const:5a7dc0:8", "const:4:8"]]
+ 005a7dc0 ["CALL", null, ["callee:00c57ea0:8"]]
- 005a7d80 bytes 48bf1a94
+ 005a7dc0 bytes 38c01a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

