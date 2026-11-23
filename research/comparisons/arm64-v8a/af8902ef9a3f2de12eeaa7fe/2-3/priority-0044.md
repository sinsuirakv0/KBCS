# v16.0.0 → v16.0.1 · 最優先の変更候補 (44)

[一覧の目次](README.md)

<a id="compare-19ceefdcf046e4e0d4ec49e2ddaf6e67"></a>

### [`00865910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865910.md) → [`00865950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865950.md) FUN_00865950

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00865668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865668.md) · 呼出先 7件 [`004796d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004796d0.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00936428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936428.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`008656a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/008656a8.md) · 呼出先 6件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`009365c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/009365c4.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00865998",
      "incomplete_value": true,
      "site": "008659b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00865958",
      "incomplete_value": true,
      "site": "00865970",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c70:8"
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
      "definition_site": "008659a4",
      "incomplete_value": true,
      "site": "008659b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:185:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00865964",
      "incomplete_value": true,
      "site": "00865974",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:145:8"
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
      "definition_site": "008659a4",
      "incomplete_value": true,
      "site": "008659b4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00865964",
      "incomplete_value": true,
      "site": "00865974",
      "value": [
        "LOAD",
        "16",
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
      "00865998",
      "READ",
      [
        "storage",
        "002c2c70",
        null,
        null
      ]
    ],
    [
      "008659a4",
      "READ",
      [
        "storage",
        "002b1145",
        null,
        "string"
      ]
    ],
    [
      "008659a4",
      "READ",
      [
        "storage",
        "002b1155",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00865998",
      "READ",
      [
        "storage",
        "002c2cb0",
        null,
        null
      ]
    ],
    [
      "008659a4",
      "READ",
      [
        "storage",
        "002b1185",
        null,
        "string"
      ]
    ],
    [
      "008659a4",
      "READ",
      [
        "storage",
        "002b1195",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00865938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865910.md#insn-00865938) · [`00865948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865910.md#insn-00865948) · [`00865958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865910.md#insn-00865958)
- 新版 `00865978`（命令位置の公開資料なし） · `00865988`（命令位置の公開資料なし） · `00865998`（命令位置の公開資料なし）

~~~diff
- 00865938 ["INT_ADD", "register:40f0:8", ["const:865938:8", "const:4:8"]]
- 00865938 ["CALL", null, ["callee:0048ce84:8"]]
+ 00865978 ["INT_ADD", "register:40f0:8", ["const:865978:8", "const:4:8"]]
+ 00865978 ["CALL", null, ["callee:0048ce84:8"]]
- 00865938 bytes 439df097
+ 00865978 bytes 439df097
- 00865948 ["INT_ADD", "register:40f0:8", ["const:865948:8", "const:4:8"]]
- 00865948 ["CALL", null, ["callee:00c57e90:8"]]
+ 00865988 ["INT_ADD", "register:40f0:8", ["const:865988:8", "const:4:8"]]
+ 00865988 ["CALL", null, ["callee:00c57e90:8"]]
- 00865948 bytes 52c80f94
+ 00865988 bytes 42c90f94
- 00865958 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c70:8"]]
- 00865958 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00865958 ["COPY", "register:5010:8", ["const:0:8"]]
- 00865958 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00865998 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb0:8"]]
+ 00865998 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00865998 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00865998 ["COPY", "register:5018:8", ["const:0:8"]]
- 00865958 bytes 001dc33d
+ 00865998 bytes 002dc33d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28c42fe05ed596bd0ca503ca41d0012f"></a>

### [`00865ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865ab4.md) → [`00865af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865af4.md) FUN_00865af4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) [`008d3454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3454.md) [`008d58e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d58e0.md) [`008da608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da608.md) [`008dad0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dad0c.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)
- 新版 呼出元 5件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) [`008d35f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d35f0.md) [`008d5a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5a7c.md) [`008da7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da7a4.md) [`008daea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008daea8.md) · 呼出先 6件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md) [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00865bb4",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00865b74",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "site": "00865bc8",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00865b88",
      "value": [
        "leaf",
        "ram:46dac0:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00865bdc",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00865b9c",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "00865b1c",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "00865bb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ],
    [
      "00865bc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ],
  "added": [
    [
      "00865b1c",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "00865bb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ],
    [
      "00865bc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00865b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865ab4.md#insn-00865b74) · [`00865b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865ab4.md#insn-00865b88) · [`00865b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865ab4.md#insn-00865b9c)
- 新版 `00865bb4`（命令位置の公開資料なし） · `00865bc8`（命令位置の公開資料なし） · `00865bdc`（命令位置の公開資料なし）

~~~diff
- 00865b74 ["INT_ADD", "register:40f0:8", ["const:865b74:8", "const:4:8"]]
- 00865b74 ["CALL", null, ["ram:46dac0:8"]]
+ 00865bb4 ["INT_ADD", "register:40f0:8", ["const:865bb4:8", "const:4:8"]]
+ 00865bb4 ["CALL", null, ["ram:46db00:8"]]
- 00865b74 bytes d31ff097
+ 00865bb4 bytes d31ff097
- 00865b88 ["INT_ADD", "register:40f0:8", ["const:865b88:8", "const:4:8"]]
- 00865b88 ["CALL", null, ["ram:46dac0:8"]]
+ 00865bc8 ["INT_ADD", "register:40f0:8", ["const:865bc8:8", "const:4:8"]]
+ 00865bc8 ["CALL", null, ["ram:46db00:8"]]
- 00865b88 bytes ce1ff097
+ 00865bc8 bytes ce1ff097
- 00865b9c ["INT_ADD", "register:40f0:8", ["const:865b9c:8", "const:4:8"]]
- 00865b9c ["CALL", null, ["ram:46dac0:8"]]
+ 00865bdc ["INT_ADD", "register:40f0:8", ["const:865bdc:8", "const:4:8"]]
+ 00865bdc ["CALL", null, ["ram:46db00:8"]]
- 00865b9c bytes c91ff097
+ 00865bdc bytes c91ff097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35bbdce2ab80147568841a1a4472c8ec"></a>

### [`00869a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869a34.md) → [`00869a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869a74.md) FUN_00869a74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00869a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869a34.md) [`008b7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7950.md) · 呼出先 3件 [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00869a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869a34.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00869a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869a74.md) [`008b7994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7994.md) · 呼出先 3件 [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00869a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869a74.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00869b10",
      "incomplete_value": true,
      "site": "00869b10",
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
      "definition_site": "00869ad0",
      "incomplete_value": true,
      "site": "00869ad0",
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
      "00869b08",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ],
    [
      "00869b10",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00869b08",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "00869b10",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00869a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869a34.md#insn-00869a54) · [`00869a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869a34.md#insn-00869a60) · [`00869a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869a34.md#insn-00869a7c)
- 新版 `00869a94`（命令位置の公開資料なし） · `00869aa0`（命令位置の公開資料なし） · `00869abc`（命令位置の公開資料なし）

~~~diff
- 00869a54 ["INT_ADD", "register:40f0:8", ["const:869a54:8", "const:4:8"]]
- 00869a54 ["CALL", null, ["local:b0:8"]]
+ 00869a94 ["INT_ADD", "register:40f0:8", ["const:869a94:8", "const:4:8"]]
+ 00869a94 ["CALL", null, ["local:b0:8"]]
- 00869a54 bytes f8ffff97
+ 00869a94 bytes f8ffff97
- 00869a60 ["INT_ADD", "register:40f0:8", ["const:869a60:8", "const:4:8"]]
- 00869a60 ["CALL", null, ["local:b0:8"]]
+ 00869aa0 ["INT_ADD", "register:40f0:8", ["const:869aa0:8", "const:4:8"]]
+ 00869aa0 ["CALL", null, ["local:b0:8"]]
- 00869a60 bytes f5ffff97
+ 00869aa0 bytes f5ffff97
- 00869a7c ["INT_ADD", "register:40f0:8", ["const:869a7c:8", "const:4:8"]]
- 00869a7c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869abc ["INT_ADD", "register:40f0:8", ["const:869abc:8", "const:4:8"]]
+ 00869abc ["CALL", null, ["callee:00c57eb0:8"]]
- 00869a7c bytes 0db80f94
+ 00869abc bytes fdb80f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c570f05d23be7c9b0dbef66738762aa0"></a>

### [`0086adc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086adc4.md) → [`0086ae04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ae04.md) FUN_0086ae04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "0086ae10",
      "incomplete_value": false,
      "site": "0086ae14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086add0",
      "incomplete_value": false,
      "site": "0086add4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
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
      "0086ae14",
      "DATA",
      [
        "storage",
        "00c7ebd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086ae14",
      "DATA",
      [
        "storage",
        "00c7efd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086add0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086adc4.md#insn-0086add0)
- 新版 `0086ae10`（命令位置の公開資料なし）

~~~diff
- 0086add0 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 0086add0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086add0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086add0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086ae10 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 0086ae10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086ae10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086ae10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086add0 bytes 29412f91
+ 0086ae10 bytes 29413f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf2416871368bc4e9b1c4c2b853ab0ea"></a>

### [`0086ade4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ade4.md) → [`0086ae24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ae24.md) FUN_0086ae24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086ae2c",
      "incomplete_value": true,
      "site": "0086ae30",
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
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086adec",
      "incomplete_value": true,
      "site": "0086adf0",
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
            "const:bd0:8"
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
      "0086ae30",
      "DATA",
      [
        "storage",
        "00c7ebd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086ae30",
      "DATA",
      [
        "storage",
        "00c7efd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086adec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ade4.md#insn-0086adec) · [`0086ae0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ade4.md#insn-0086ae0c)
- 新版 `0086ae2c`（命令位置の公開資料なし） · `0086ae4c`（命令位置の公開資料なし）

~~~diff
- 0086adec ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 0086adec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086adec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086adec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086ae2c ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 0086ae2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086ae2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086ae2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086adec bytes 29412f91
+ 0086ae2c bytes 29413f91
- 0086ae0c ["INT_ADD", "register:40f0:8", ["const:86ae0c:8", "const:4:8"]]
- 0086ae0c ["CALL", null, ["callee:00c57e80:8"]]
+ 0086ae4c ["INT_ADD", "register:40f0:8", ["const:86ae4c:8", "const:4:8"]]
+ 0086ae4c ["CALL", null, ["callee:00c57e80:8"]]
- 0086ae0c bytes 1db30f94
+ 0086ae4c bytes 0db40f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aedbcc8bc2221f402b3d33646ec0fcf"></a>

### [`0086ae20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ae20.md) → [`0086ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ae60.md) FUN_0086ae60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0086ae84",
      "incomplete_value": false,
      "site": "0086ae84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086ae44",
      "incomplete_value": false,
      "site": "0086ae44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
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
      "0086ae84",
      "DATA",
      [
        "storage",
        "00c7ebd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086ae84",
      "DATA",
      [
        "storage",
        "00c7efd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086ae34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ae20.md#insn-0086ae34) · [`0086ae40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ae20.md#insn-0086ae40) · [`0086ae5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ae20.md#insn-0086ae5c)
- 新版 `0086ae74`（命令位置の公開資料なし） · `0086ae80`（命令位置の公開資料なし） · `0086ae9c`（命令位置の公開資料なし）

~~~diff
- 0086ae34 ["INT_ADD", "register:40f0:8", ["const:86ae34:8", "const:4:8"]]
- 0086ae34 ["CALL", null, ["callee:00c57e90:8"]]
+ 0086ae74 ["INT_ADD", "register:40f0:8", ["const:86ae74:8", "const:4:8"]]
+ 0086ae74 ["CALL", null, ["callee:00c57e90:8"]]
- 0086ae34 bytes 17b30f94
+ 0086ae74 bytes 07b40f94
- 0086ae40 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 0086ae40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086ae40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086ae40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086ae80 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 0086ae80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086ae80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086ae80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086ae40 bytes 29412f91
+ 0086ae80 bytes 29413f91
- 0086ae5c ["INT_ADD", "register:40f0:8", ["const:86ae5c:8", "const:4:8"]]
- 0086ae5c ["CALL", null, ["callee:00c53cd0:8"]]
+ 0086ae9c ["INT_ADD", "register:40f0:8", ["const:86ae9c:8", "const:4:8"]]
+ 0086ae9c ["CALL", null, ["callee:00c53cd0:8"]]
- 0086ae5c bytes 95a20f94
+ 0086ae9c bytes 8da30f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a89b5c24c2a837e364507f8893af2d22"></a>

### [`0086af14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086af14.md) → [`0086af54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086af54.md) FUN_0086af54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0086aee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aee4.md) · 呼出先 7件 [`0048965c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/0048965c.md) [`004986a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0086af24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086af24.md) · 呼出先 7件 [`0048969c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/0048969c.md) [`004986e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004986e4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.41% / 新版 98.41%

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
      "site": "0086afa8",
      "value": [
        "leaf",
        "ram:48969c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086af68",
      "value": [
        "leaf",
        "ram:48965c:8"
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
      "0086afa8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048965c"
      ]
    ]
  ],
  "added": [
    [
      "0086afa8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048969c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086af68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086af14.md#insn-0086af68) · [`0086af48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086af14.md#insn-0086af48) · [`0086af78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086af14.md#insn-0086af78)
- 新版 `0086afa8`（命令位置の公開資料なし） · `0086af88`（命令位置の公開資料なし） · `0086afb8`（命令位置の公開資料なし）

~~~diff
- 0086af68 ["INT_ADD", "register:40f0:8", ["const:86af68:8", "const:4:8"]]
- 0086af68 ["CALL", null, ["ram:48965c:8"]]
+ 0086afa8 ["INT_ADD", "register:40f0:8", ["const:86afa8:8", "const:4:8"]]
+ 0086afa8 ["CALL", null, ["ram:48969c:8"]]
- 0086af68 bytes bd79f097
+ 0086afa8 bytes bd79f097
- 0086af48 ["INT_ADD", "register:40f0:8", ["const:86af48:8", "const:4:8"]]
- 0086af48 ["CALL", null, ["callee:00c584f0:8"]]
+ 0086af88 ["INT_ADD", "register:40f0:8", ["const:86af88:8", "const:4:8"]]
+ 0086af88 ["CALL", null, ["callee:00c584f0:8"]]
- 0086af48 bytes 6ab40f94
+ 0086af88 bytes 5ab50f94
- 0086af78 ["INT_ADD", "register:40f0:8", ["const:86af78:8", "const:4:8"]]
- 0086af78 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0086afb8 ["INT_ADD", "register:40f0:8", ["const:86afb8:8", "const:4:8"]]
+ 0086afb8 ["CALL", null, ["callee:00c53cd0:8"]]
- 0086af78 bytes 4ea20f94
+ 0086afb8 bytes 46a30f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d349c44bf6df1d8359143d67ffa1df8c"></a>

### [`0086b044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b044.md) → [`0086b084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b084.md) FUN_0086b084

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "0086b090",
      "incomplete_value": false,
      "site": "0086b094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086b050",
      "incomplete_value": false,
      "site": "0086b054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      "0086b094",
      "DATA",
      [
        "storage",
        "00c7ec50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086b094",
      "DATA",
      [
        "storage",
        "00c7f050",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086b04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b044.md#insn-0086b04c) · [`0086b050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b044.md#insn-0086b050)
- 新版 `0086b08c`（命令位置の公開資料なし） · `0086b090`（命令位置の公開資料なし）

~~~diff
- 0086b04c ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 0086b08c ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0086b04c bytes 892000f0
+ 0086b08c bytes a9200090
- 0086b050 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 0086b050 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086b050 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086b050 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086b090 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 0086b090 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b090 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b090 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086b050 bytes 29413191
+ 0086b090 bytes 29410191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2b7c2e1b16eebf20c915b9d7eab6c68"></a>

### [`0086b064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b064.md) → [`0086b0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b0a4.md) FUN_0086b0a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0086b0ac",
      "incomplete_value": false,
      "site": "0086b0b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086b06c",
      "incomplete_value": false,
      "site": "0086b070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      "0086b0b0",
      "DATA",
      [
        "storage",
        "00c7ec50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086b0b0",
      "DATA",
      [
        "storage",
        "00c7f050",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086b068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b064.md#insn-0086b068) · [`0086b06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b064.md#insn-0086b06c) · [`0086b08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b064.md#insn-0086b08c)
- 新版 `0086b0a8`（命令位置の公開資料なし） · `0086b0ac`（命令位置の公開資料なし） · `0086b0cc`（命令位置の公開資料なし）

~~~diff
- 0086b068 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 0086b0a8 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0086b068 bytes 892000f0
+ 0086b0a8 bytes a9200090
- 0086b06c ["COPY", "tmp:0:8", ["const:c50:8"]]
- 0086b06c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086b06c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086b06c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086b0ac ["COPY", "tmp:0:8", ["const:50:8"]]
+ 0086b0ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b0ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b0ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086b06c bytes 29413191
+ 0086b0ac bytes 29410191
- 0086b08c ["INT_ADD", "register:40f0:8", ["const:86b08c:8", "const:4:8"]]
- 0086b08c ["CALL", null, ["callee:00c57e80:8"]]
+ 0086b0cc ["INT_ADD", "register:40f0:8", ["const:86b0cc:8", "const:4:8"]]
+ 0086b0cc ["CALL", null, ["callee:00c57e80:8"]]
- 0086b08c bytes 7db20f94
+ 0086b0cc bytes 6db30f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06bd90a05bbff28f7f1198c759020a19"></a>

### [`0086b0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b0a0.md) → [`0086b0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b0e0.md) FUN_0086b0e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0086b104",
      "incomplete_value": false,
      "site": "0086b104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086b0c4",
      "incomplete_value": false,
      "site": "0086b0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      "0086b104",
      "DATA",
      [
        "storage",
        "00c7ec50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086b104",
      "DATA",
      [
        "storage",
        "00c7f050",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086b0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b0a0.md#insn-0086b0b4) · [`0086b0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b0a0.md#insn-0086b0bc) · [`0086b0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b0a0.md#insn-0086b0c0)
- 新版 `0086b0f4`（命令位置の公開資料なし） · `0086b0fc`（命令位置の公開資料なし） · `0086b100`（命令位置の公開資料なし）

~~~diff
- 0086b0b4 ["INT_ADD", "register:40f0:8", ["const:86b0b4:8", "const:4:8"]]
- 0086b0b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0086b0f4 ["INT_ADD", "register:40f0:8", ["const:86b0f4:8", "const:4:8"]]
+ 0086b0f4 ["CALL", null, ["callee:00c57e90:8"]]
- 0086b0b4 bytes 77b20f94
+ 0086b0f4 bytes 67b30f94
- 0086b0bc ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 0086b0fc ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0086b0bc bytes 892000f0
+ 0086b0fc bytes a9200090
- 0086b0c0 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 0086b0c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086b0c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086b0c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086b100 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 0086b100 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b100 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b100 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086b0c0 bytes 29413191
+ 0086b100 bytes 29410191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8f8a0b836f622f294a204071b8315db"></a>

### [`0086b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b0f0.md) → [`0086b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b130.md) FUN_0086b130

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "0086b13c",
      "incomplete_value": false,
      "site": "0086b13c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086b0fc",
      "incomplete_value": false,
      "site": "0086b0fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      "0086b13c",
      "DATA",
      [
        "storage",
        "00c7ec50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086b13c",
      "DATA",
      [
        "storage",
        "00c7f050",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086b0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b0f0.md#insn-0086b0f4) · [`0086b0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b0f0.md#insn-0086b0f8) · [`0086b118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b0f0.md#insn-0086b118)
- 新版 `0086b134`（命令位置の公開資料なし） · `0086b138`（命令位置の公開資料なし） · `0086b158`（命令位置の公開資料なし）

~~~diff
- 0086b0f4 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 0086b134 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0086b0f4 bytes 892000f0
+ 0086b134 bytes a9200090
- 0086b0f8 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 0086b0f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086b0f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086b0f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086b138 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 0086b138 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b138 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b138 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086b0f8 bytes 29413191
+ 0086b138 bytes 29410191
- 0086b118 ["INT_ADD", "register:40f0:8", ["const:86b118:8", "const:4:8"]]
- 0086b118 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0086b158 ["INT_ADD", "register:40f0:8", ["const:86b158:8", "const:4:8"]]
+ 0086b158 ["CALL", null, ["callee:00c53cd0:8"]]
- 0086b118 bytes e6a10f94
+ 0086b158 bytes dea20f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-057b00cb93fb76f4976abd37fae688d3"></a>

### [`0086b2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b2c4.md) → [`0086b304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b304.md) FUN_0086b304

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
      "definition_site": "0086b308",
      "incomplete_value": false,
      "site": "0086b30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086b2c8",
      "incomplete_value": false,
      "site": "0086b2cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "0086b30c",
      "DATA",
      [
        "storage",
        "00c7ecd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086b30c",
      "DATA",
      [
        "storage",
        "00c7f0d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086b2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b2c4.md#insn-0086b2c4) · [`0086b2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b2c4.md#insn-0086b2c8)
- 新版 `0086b304`（命令位置の公開資料なし） · `0086b308`（命令位置の公開資料なし）

~~~diff
- 0086b2c4 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 0086b304 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0086b2c4 bytes 882000f0
+ 0086b304 bytes a8200090
- 0086b2c8 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0086b2c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086b2c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086b2c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086b308 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 0086b308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086b308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086b308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086b2c8 bytes 08413391
+ 0086b308 bytes 08410391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31655773089308af7030cd0df27aae04"></a>

### [`0086b2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b2d4.md) → [`0086b314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b314.md) FUN_0086b314

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
      "definition_site": "0086b324",
      "incomplete_value": false,
      "site": "0086b32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086b2e4",
      "incomplete_value": false,
      "site": "0086b2ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "0086b32c",
      "DATA",
      [
        "storage",
        "00c7ecd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086b32c",
      "DATA",
      [
        "storage",
        "00c7f0d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086b2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b2d4.md#insn-0086b2e0) · [`0086b2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b2d4.md#insn-0086b2e4) · [`0086b2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b2d4.md#insn-0086b2f0)
- 新版 `0086b320`（命令位置の公開資料なし） · `0086b324`（命令位置の公開資料なし） · `0086b330`（命令位置の公開資料なし）

~~~diff
- 0086b2e0 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 0086b320 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0086b2e0 bytes 882000f0
+ 0086b320 bytes a8200090
- 0086b2e4 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0086b2e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086b2e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086b2e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086b324 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 0086b324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086b324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086b324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086b2e4 bytes 08413391
+ 0086b324 bytes 08410391
- 0086b2f0 ["INT_ADD", "register:40f0:8", ["const:86b2f0:8", "const:4:8"]]
- 0086b2f0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0086b330 ["INT_ADD", "register:40f0:8", ["const:86b330:8", "const:4:8"]]
+ 0086b330 ["CALL", null, ["callee:00c57ea0:8"]]
- 0086b2f0 bytes ecb10f94
+ 0086b330 bytes dcb20f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0a7005a5e07aab5d148f9e63d362e98"></a>

### [`0086b314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b314.md) → [`0086b354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b354.md) FUN_0086b354

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00853660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853660.md) · 呼出先 3件 [`0049883c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049883c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 1件 [`008536a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/008536a0.md) · 呼出先 3件 [`0049887c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049887c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

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
      "definition_site": "0086b374",
      "incomplete_value": false,
      "site": "0086b374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086b334",
      "incomplete_value": false,
      "site": "0086b334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "0086b374",
      "DATA",
      [
        "storage",
        "00c7ed20",
        null,
        "undefined *"
      ]
    ],
    [
      "0086b3cc",
      "PARAM",
      [
        "storage",
        "002ede3e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0086b374",
      "DATA",
      [
        "storage",
        "00c7f120",
        null,
        "undefined *"
      ]
    ],
    [
      "0086b3cc",
      "PARAM",
      [
        "storage",
        "002ede7e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086b324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b314.md#insn-0086b324) · [`0086b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b314.md#insn-0086b328) · [`0086b35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b314.md#insn-0086b35c)
- 新版 `0086b364`（命令位置の公開資料なし） · `0086b368`（命令位置の公開資料なし） · `0086b39c`（命令位置の公開資料なし）

~~~diff
- 0086b324 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 0086b364 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0086b324 bytes 882000f0
+ 0086b364 bytes a8200090
- 0086b328 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 0086b328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086b328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086b328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086b368 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 0086b368 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086b368 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086b368 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086b328 bytes 08813491
+ 0086b368 bytes 08810491
- 0086b35c ["INT_ADD", "register:40f0:8", ["const:86b35c:8", "const:4:8"]]
- 0086b35c ["CALL", null, ["callee:00c53cd0:8"]]
+ 0086b39c ["INT_ADD", "register:40f0:8", ["const:86b39c:8", "const:4:8"]]
+ 0086b39c ["CALL", null, ["callee:00c53cd0:8"]]
- 0086b35c bytes 55a10f94
+ 0086b39c bytes 4da20f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03e0167a7cf522b1c1862376f8819a30"></a>

### [`0086b3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b3e0.md) → [`0086b420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b420.md) FUN_0086b420

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0086b438",
      "incomplete_value": false,
      "site": "0086b43c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086b3f8",
      "incomplete_value": false,
      "site": "0086b3fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "0086b43c",
      "DATA",
      [
        "storage",
        "00c7ed20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086b43c",
      "DATA",
      [
        "storage",
        "00c7f120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086b3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b3e0.md#insn-0086b3f4) · [`0086b3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b3e0.md#insn-0086b3f8) · [`0086b408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b3e0.md#insn-0086b408)
- 新版 `0086b434`（命令位置の公開資料なし） · `0086b438`（命令位置の公開資料なし） · `0086b448`（命令位置の公開資料なし）

~~~diff
- 0086b3f4 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 0086b434 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0086b3f4 bytes 892000f0
+ 0086b434 bytes a9200090
- 0086b3f8 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 0086b3f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086b3f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086b3f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086b438 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 0086b438 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b438 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b438 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086b3f8 bytes 29813491
+ 0086b438 bytes 29810491
- 0086b408 ["INT_ADD", "register:40f0:8", ["const:86b408:8", "const:4:8"]]
- 0086b408 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086b448 ["INT_ADD", "register:40f0:8", ["const:86b448:8", "const:4:8"]]
+ 0086b448 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086b408 bytes aab10f94
+ 0086b448 bytes 9ab20f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b793d6a480e9c00fbf8c335151f4697"></a>

### [`0086b48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b48c.md) → [`0086b4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b4cc.md) FUN_0086b4cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0086b4e4",
      "incomplete_value": false,
      "site": "0086b4e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086b4a4",
      "incomplete_value": false,
      "site": "0086b4a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "0086b4e8",
      "DATA",
      [
        "storage",
        "00c7ed20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086b4e8",
      "DATA",
      [
        "storage",
        "00c7f120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086b4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b48c.md#insn-0086b4a0) · [`0086b4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b48c.md#insn-0086b4a4) · [`0086b4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b48c.md#insn-0086b4b4)
- 新版 `0086b4e0`（命令位置の公開資料なし） · `0086b4e4`（命令位置の公開資料なし） · `0086b4f4`（命令位置の公開資料なし）

~~~diff
- 0086b4a0 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 0086b4e0 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0086b4a0 bytes 892000f0
+ 0086b4e0 bytes a9200090
- 0086b4a4 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 0086b4a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086b4a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086b4a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086b4e4 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 0086b4e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b4e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b4e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086b4a4 bytes 29813491
+ 0086b4e4 bytes 29810491
- 0086b4b4 ["INT_ADD", "register:40f0:8", ["const:86b4b4:8", "const:4:8"]]
- 0086b4b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086b4f4 ["INT_ADD", "register:40f0:8", ["const:86b4f4:8", "const:4:8"]]
+ 0086b4f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086b4b4 bytes 7fb10f94
+ 0086b4f4 bytes 6fb20f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ddfcfb8a04f17674ee46d5f76513430"></a>

### [`0086c55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c55c.md) → [`0086c59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c59c.md) FUN_0086c59c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 6件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md) [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086c65c",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086c61c",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "site": "0086c670",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086c630",
      "value": [
        "leaf",
        "ram:46dac0:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086c684",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086c644",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "0086c5c4",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086c65c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ],
    [
      "0086c670",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ],
  "added": [
    [
      "0086c5c4",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "0086c65c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ],
    [
      "0086c670",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086c61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c55c.md#insn-0086c61c) · [`0086c630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c55c.md#insn-0086c630) · [`0086c644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c55c.md#insn-0086c644)
- 新版 `0086c65c`（命令位置の公開資料なし） · `0086c670`（命令位置の公開資料なし） · `0086c684`（命令位置の公開資料なし）

~~~diff
- 0086c61c ["INT_ADD", "register:40f0:8", ["const:86c61c:8", "const:4:8"]]
- 0086c61c ["CALL", null, ["ram:46dac0:8"]]
+ 0086c65c ["INT_ADD", "register:40f0:8", ["const:86c65c:8", "const:4:8"]]
+ 0086c65c ["CALL", null, ["ram:46db00:8"]]
- 0086c61c bytes 2905f097
+ 0086c65c bytes 2905f097
- 0086c630 ["INT_ADD", "register:40f0:8", ["const:86c630:8", "const:4:8"]]
- 0086c630 ["CALL", null, ["ram:46dac0:8"]]
+ 0086c670 ["INT_ADD", "register:40f0:8", ["const:86c670:8", "const:4:8"]]
+ 0086c670 ["CALL", null, ["ram:46db00:8"]]
- 0086c630 bytes 2405f097
+ 0086c670 bytes 2405f097
- 0086c644 ["INT_ADD", "register:40f0:8", ["const:86c644:8", "const:4:8"]]
- 0086c644 ["CALL", null, ["ram:46dac0:8"]]
+ 0086c684 ["INT_ADD", "register:40f0:8", ["const:86c684:8", "const:4:8"]]
+ 0086c684 ["CALL", null, ["ram:46db00:8"]]
- 0086c644 bytes 1f05f097
+ 0086c684 bytes 1f05f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da7b8d2b6669a07efc2cc6735c5e710e"></a>

### [`0086c6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c6e4.md) → [`0086c724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c724.md) FUN_0086c724

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 6件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md) [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086c76c",
      "incomplete_value": true,
      "site": "0086c76c",
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
                "const:e1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086c72c",
      "incomplete_value": true,
      "site": "0086c72c",
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
                "const:ddd:8"
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
      "site": "0086c7e4",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086c7a4",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "site": "0086c7f8",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086c7b8",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "0086c74c",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086c7e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ],
    [
      "0086c7f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ],
  "added": [
    [
      "0086c74c",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "0086c7e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ],
    [
      "0086c7f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086c7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c6e4.md#insn-0086c7a4) · [`0086c7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c6e4.md#insn-0086c7b8) · [`0086c7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c6e4.md#insn-0086c7cc)
- 新版 `0086c7e4`（命令位置の公開資料なし） · `0086c7f8`（命令位置の公開資料なし） · `0086c80c`（命令位置の公開資料なし）

~~~diff
- 0086c7a4 ["INT_ADD", "register:40f0:8", ["const:86c7a4:8", "const:4:8"]]
- 0086c7a4 ["CALL", null, ["ram:46dac0:8"]]
+ 0086c7e4 ["INT_ADD", "register:40f0:8", ["const:86c7e4:8", "const:4:8"]]
+ 0086c7e4 ["CALL", null, ["ram:46db00:8"]]
- 0086c7a4 bytes c704f097
+ 0086c7e4 bytes c704f097
- 0086c7b8 ["INT_ADD", "register:40f0:8", ["const:86c7b8:8", "const:4:8"]]
- 0086c7b8 ["CALL", null, ["ram:46dac0:8"]]
+ 0086c7f8 ["INT_ADD", "register:40f0:8", ["const:86c7f8:8", "const:4:8"]]
+ 0086c7f8 ["CALL", null, ["ram:46db00:8"]]
- 0086c7b8 bytes c204f097
+ 0086c7f8 bytes c204f097
- 0086c7cc ["INT_ADD", "register:40f0:8", ["const:86c7cc:8", "const:4:8"]]
- 0086c7cc ["CALL", null, ["ram:46dac0:8"]]
+ 0086c80c ["INT_ADD", "register:40f0:8", ["const:86c80c:8", "const:4:8"]]
+ 0086c80c ["CALL", null, ["ram:46db00:8"]]
- 0086c7cc bytes bd04f097
+ 0086c80c bytes bd04f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d0e6c235eec785ed8d99c554799737e"></a>

### [`0086c874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c874.md) → [`0086c8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c8b4.md) FUN_0086c8b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 6件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md) [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086c8fc",
      "incomplete_value": true,
      "site": "0086c8fc",
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
                "const:e1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086c8bc",
      "incomplete_value": true,
      "site": "0086c8bc",
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
                "const:ddd:8"
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
      "site": "0086c974",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086c934",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "site": "0086c988",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086c948",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "0086c8dc",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086c974",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ],
    [
      "0086c988",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ],
  "added": [
    [
      "0086c8dc",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "0086c974",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ],
    [
      "0086c988",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086c934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c874.md#insn-0086c934) · [`0086c948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c874.md#insn-0086c948) · [`0086c95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c874.md#insn-0086c95c)
- 新版 `0086c974`（命令位置の公開資料なし） · `0086c988`（命令位置の公開資料なし） · `0086c99c`（命令位置の公開資料なし）

~~~diff
- 0086c934 ["INT_ADD", "register:40f0:8", ["const:86c934:8", "const:4:8"]]
- 0086c934 ["CALL", null, ["ram:46dac0:8"]]
+ 0086c974 ["INT_ADD", "register:40f0:8", ["const:86c974:8", "const:4:8"]]
+ 0086c974 ["CALL", null, ["ram:46db00:8"]]
- 0086c934 bytes 6304f097
+ 0086c974 bytes 6304f097
- 0086c948 ["INT_ADD", "register:40f0:8", ["const:86c948:8", "const:4:8"]]
- 0086c948 ["CALL", null, ["ram:46dac0:8"]]
+ 0086c988 ["INT_ADD", "register:40f0:8", ["const:86c988:8", "const:4:8"]]
+ 0086c988 ["CALL", null, ["ram:46db00:8"]]
- 0086c948 bytes 5e04f097
+ 0086c988 bytes 5e04f097
- 0086c95c ["INT_ADD", "register:40f0:8", ["const:86c95c:8", "const:4:8"]]
- 0086c95c ["CALL", null, ["ram:46dac0:8"]]
+ 0086c99c ["INT_ADD", "register:40f0:8", ["const:86c99c:8", "const:4:8"]]
+ 0086c99c ["CALL", null, ["ram:46db00:8"]]
- 0086c95c bytes 5904f097
+ 0086c99c bytes 5904f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ac0bbd64692e83f0e1835af55b18a29"></a>

### [`0086ca04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086ca04.md) → [`0086ca44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086ca44.md) FUN_0086ca44

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 6件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md) [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086ca8c",
      "incomplete_value": true,
      "site": "0086ca8c",
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
                "const:e1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086ca4c",
      "incomplete_value": true,
      "site": "0086ca4c",
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
                "const:ddd:8"
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
      "site": "0086cb04",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086cac4",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "site": "0086cb18",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086cad8",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "0086ca6c",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086cb04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ],
    [
      "0086cb18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ],
  "added": [
    [
      "0086ca6c",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "0086cb04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ],
    [
      "0086cb18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086cac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086ca04.md#insn-0086cac4) · [`0086cad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086ca04.md#insn-0086cad8) · [`0086caec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086ca04.md#insn-0086caec)
- 新版 `0086cb04`（命令位置の公開資料なし） · `0086cb18`（命令位置の公開資料なし） · `0086cb2c`（命令位置の公開資料なし）

~~~diff
- 0086cac4 ["INT_ADD", "register:40f0:8", ["const:86cac4:8", "const:4:8"]]
- 0086cac4 ["CALL", null, ["ram:46dac0:8"]]
+ 0086cb04 ["INT_ADD", "register:40f0:8", ["const:86cb04:8", "const:4:8"]]
+ 0086cb04 ["CALL", null, ["ram:46db00:8"]]
- 0086cac4 bytes ff03f097
+ 0086cb04 bytes ff03f097
- 0086cad8 ["INT_ADD", "register:40f0:8", ["const:86cad8:8", "const:4:8"]]
- 0086cad8 ["CALL", null, ["ram:46dac0:8"]]
+ 0086cb18 ["INT_ADD", "register:40f0:8", ["const:86cb18:8", "const:4:8"]]
+ 0086cb18 ["CALL", null, ["ram:46db00:8"]]
- 0086cad8 bytes fa03f097
+ 0086cb18 bytes fa03f097
- 0086caec ["INT_ADD", "register:40f0:8", ["const:86caec:8", "const:4:8"]]
- 0086caec ["CALL", null, ["ram:46dac0:8"]]
+ 0086cb2c ["INT_ADD", "register:40f0:8", ["const:86cb2c:8", "const:4:8"]]
+ 0086cb2c ["CALL", null, ["ram:46db00:8"]]
- 0086caec bytes f503f097
+ 0086cb2c bytes f503f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fa29346baa73f86e3f46c27bcd1b312"></a>

### [`0086cb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086cb94.md) → [`0086cbd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086cbd4.md) FUN_0086cbd4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 6件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md) [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086cc1c",
      "incomplete_value": true,
      "site": "0086cc1c",
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
                "const:e1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086cbdc",
      "incomplete_value": true,
      "site": "0086cbdc",
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
                "const:ddd:8"
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
      "site": "0086cc94",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086cc54",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "site": "0086cca8",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086cc68",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "0086cbfc",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086cc94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ],
    [
      "0086cca8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ],
  "added": [
    [
      "0086cbfc",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "0086cc94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ],
    [
      "0086cca8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086cc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086cb94.md#insn-0086cc54) · [`0086cc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086cb94.md#insn-0086cc68) · [`0086cc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086cb94.md#insn-0086cc7c)
- 新版 `0086cc94`（命令位置の公開資料なし） · `0086cca8`（命令位置の公開資料なし） · `0086ccbc`（命令位置の公開資料なし）

~~~diff
- 0086cc54 ["INT_ADD", "register:40f0:8", ["const:86cc54:8", "const:4:8"]]
- 0086cc54 ["CALL", null, ["ram:46dac0:8"]]
+ 0086cc94 ["INT_ADD", "register:40f0:8", ["const:86cc94:8", "const:4:8"]]
+ 0086cc94 ["CALL", null, ["ram:46db00:8"]]
- 0086cc54 bytes 9b03f097
+ 0086cc94 bytes 9b03f097
- 0086cc68 ["INT_ADD", "register:40f0:8", ["const:86cc68:8", "const:4:8"]]
- 0086cc68 ["CALL", null, ["ram:46dac0:8"]]
+ 0086cca8 ["INT_ADD", "register:40f0:8", ["const:86cca8:8", "const:4:8"]]
+ 0086cca8 ["CALL", null, ["ram:46db00:8"]]
- 0086cc68 bytes 9603f097
+ 0086cca8 bytes 9603f097
- 0086cc7c ["INT_ADD", "register:40f0:8", ["const:86cc7c:8", "const:4:8"]]
- 0086cc7c ["CALL", null, ["ram:46dac0:8"]]
+ 0086ccbc ["INT_ADD", "register:40f0:8", ["const:86ccbc:8", "const:4:8"]]
+ 0086ccbc ["CALL", null, ["ram:46db00:8"]]
- 0086cc7c bytes 9103f097
+ 0086ccbc bytes 9103f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27716d021482ff1943d12e10424b1ec7"></a>

### [`0086cd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086cd24.md) → [`0086cd64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086cd64.md) FUN_0086cd64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) [`00a39208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39208.md) [`00a39330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39330.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)
- 新版 呼出元 3件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) [`00a39400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39400.md) [`00a39528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39528.md) · 呼出先 6件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md) [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.46% / 新版 91.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086cdac",
      "incomplete_value": true,
      "site": "0086cdac",
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
                "const:e1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086cd6c",
      "incomplete_value": true,
      "site": "0086cd6c",
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
                "const:ddd:8"
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
      "site": "0086ce24",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086cde4",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "site": "0086ce38",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086cdf8",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "0086cd8c",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086ce24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ],
    [
      "0086ce38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ],
  "added": [
    [
      "0086cd8c",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "0086ce24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ],
    [
      "0086ce38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086cde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086cd24.md#insn-0086cde4) · [`0086cdf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086cd24.md#insn-0086cdf8) · [`0086ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086cd24.md#insn-0086ce0c)
- 新版 `0086ce24`（命令位置の公開資料なし） · `0086ce38`（命令位置の公開資料なし） · `0086ce4c`（命令位置の公開資料なし）

~~~diff
- 0086cde4 ["INT_ADD", "register:40f0:8", ["const:86cde4:8", "const:4:8"]]
- 0086cde4 ["CALL", null, ["ram:46dac0:8"]]
+ 0086ce24 ["INT_ADD", "register:40f0:8", ["const:86ce24:8", "const:4:8"]]
+ 0086ce24 ["CALL", null, ["ram:46db00:8"]]
- 0086cde4 bytes 3703f097
+ 0086ce24 bytes 3703f097
- 0086cdf8 ["INT_ADD", "register:40f0:8", ["const:86cdf8:8", "const:4:8"]]
- 0086cdf8 ["CALL", null, ["ram:46dac0:8"]]
+ 0086ce38 ["INT_ADD", "register:40f0:8", ["const:86ce38:8", "const:4:8"]]
+ 0086ce38 ["CALL", null, ["ram:46db00:8"]]
- 0086cdf8 bytes 3203f097
+ 0086ce38 bytes 3203f097
- 0086ce0c ["INT_ADD", "register:40f0:8", ["const:86ce0c:8", "const:4:8"]]
- 0086ce0c ["CALL", null, ["ram:46dac0:8"]]
+ 0086ce4c ["INT_ADD", "register:40f0:8", ["const:86ce4c:8", "const:4:8"]]
+ 0086ce4c ["CALL", null, ["ram:46db00:8"]]
- 0086ce0c bytes 2d03f097
+ 0086ce4c bytes 2d03f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e76fc5d5fc952c886c017dec98021c7"></a>

### [`0086ceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086ceac.md) → [`0086ceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086ceec.md) FUN_0086ceec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 6件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md) [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.46% / 新版 91.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086cf34",
      "incomplete_value": true,
      "site": "0086cf34",
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
                "const:e1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086cef4",
      "incomplete_value": true,
      "site": "0086cef4",
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
                "const:ddd:8"
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
      "site": "0086cfac",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086cf6c",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "site": "0086cfc0",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086cf80",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "0086cf14",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086cfac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ],
    [
      "0086cfc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ],
  "added": [
    [
      "0086cf14",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "0086cfac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ],
    [
      "0086cfc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086cf6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086ceac.md#insn-0086cf6c) · [`0086cf80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086ceac.md#insn-0086cf80) · [`0086cf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086ceac.md#insn-0086cf94)
- 新版 `0086cfac`（命令位置の公開資料なし） · `0086cfc0`（命令位置の公開資料なし） · `0086cfd4`（命令位置の公開資料なし）

~~~diff
- 0086cf6c ["INT_ADD", "register:40f0:8", ["const:86cf6c:8", "const:4:8"]]
- 0086cf6c ["CALL", null, ["ram:46dac0:8"]]
+ 0086cfac ["INT_ADD", "register:40f0:8", ["const:86cfac:8", "const:4:8"]]
+ 0086cfac ["CALL", null, ["ram:46db00:8"]]
- 0086cf6c bytes d502f097
+ 0086cfac bytes d502f097
- 0086cf80 ["INT_ADD", "register:40f0:8", ["const:86cf80:8", "const:4:8"]]
- 0086cf80 ["CALL", null, ["ram:46dac0:8"]]
+ 0086cfc0 ["INT_ADD", "register:40f0:8", ["const:86cfc0:8", "const:4:8"]]
+ 0086cfc0 ["CALL", null, ["ram:46db00:8"]]
- 0086cf80 bytes d002f097
+ 0086cfc0 bytes d002f097
- 0086cf94 ["INT_ADD", "register:40f0:8", ["const:86cf94:8", "const:4:8"]]
- 0086cf94 ["CALL", null, ["ram:46dac0:8"]]
+ 0086cfd4 ["INT_ADD", "register:40f0:8", ["const:86cfd4:8", "const:4:8"]]
+ 0086cfd4 ["CALL", null, ["ram:46db00:8"]]
- 0086cf94 bytes cb02f097
+ 0086cfd4 bytes cb02f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3604a0b78ac3a6a182ac4d98bd2d7235"></a>

### [`0086d034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d034.md) → [`0086d074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d074.md) FUN_0086d074

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 6件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md) [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086d0bc",
      "incomplete_value": true,
      "site": "0086d0bc",
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
                "const:e1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d07c",
      "incomplete_value": true,
      "site": "0086d07c",
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
                "const:ddd:8"
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
      "site": "0086d134",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086d0f4",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "site": "0086d148",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086d108",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "0086d09c",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086d134",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ],
    [
      "0086d148",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ],
  "added": [
    [
      "0086d09c",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "0086d134",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ],
    [
      "0086d148",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d034.md#insn-0086d0f4) · [`0086d108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d034.md#insn-0086d108) · [`0086d11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d034.md#insn-0086d11c)
- 新版 `0086d134`（命令位置の公開資料なし） · `0086d148`（命令位置の公開資料なし） · `0086d15c`（命令位置の公開資料なし）

~~~diff
- 0086d0f4 ["INT_ADD", "register:40f0:8", ["const:86d0f4:8", "const:4:8"]]
- 0086d0f4 ["CALL", null, ["ram:46dac0:8"]]
+ 0086d134 ["INT_ADD", "register:40f0:8", ["const:86d134:8", "const:4:8"]]
+ 0086d134 ["CALL", null, ["ram:46db00:8"]]
- 0086d0f4 bytes 7302f097
+ 0086d134 bytes 7302f097
- 0086d108 ["INT_ADD", "register:40f0:8", ["const:86d108:8", "const:4:8"]]
- 0086d108 ["CALL", null, ["ram:46dac0:8"]]
+ 0086d148 ["INT_ADD", "register:40f0:8", ["const:86d148:8", "const:4:8"]]
+ 0086d148 ["CALL", null, ["ram:46db00:8"]]
- 0086d108 bytes 6e02f097
+ 0086d148 bytes 6e02f097
- 0086d11c ["INT_ADD", "register:40f0:8", ["const:86d11c:8", "const:4:8"]]
- 0086d11c ["CALL", null, ["ram:46dac0:8"]]
+ 0086d15c ["INT_ADD", "register:40f0:8", ["const:86d15c:8", "const:4:8"]]
+ 0086d15c ["CALL", null, ["ram:46db00:8"]]
- 0086d11c bytes 6902f097
+ 0086d15c bytes 6902f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fd9381e94df4fd35b6caa30abc395fb"></a>

### [`0086d1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d1c4.md) → [`0086d204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d204.md) FUN_0086d204

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
      "definition_site": "0086d208",
      "incomplete_value": false,
      "site": "0086d20c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d1c8",
      "incomplete_value": false,
      "site": "0086d1cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
      "0086d20c",
      "DATA",
      [
        "storage",
        "00c7ed80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d20c",
      "DATA",
      [
        "storage",
        "00c7f180",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d1c4.md#insn-0086d1c4) · [`0086d1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d1c4.md#insn-0086d1c8)
- 新版 `0086d204`（命令位置の公開資料なし） · `0086d208`（命令位置の公開資料なし）

~~~diff
- 0086d1c4 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 0086d204 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0086d1c4 bytes 882000b0
+ 0086d204 bytes 882000d0
- 0086d1c8 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 0086d1c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086d1c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086d1c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086d208 ["COPY", "tmp:0:8", ["const:180:8"]]
+ 0086d208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086d1c8 bytes 08013691
+ 0086d208 bytes 08010691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c02fb7814e4268082232bc8f1bb80942"></a>

### [`0086d1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d1d4.md) → [`0086d214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d214.md) FUN_0086d214

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
      "definition_site": "0086d224",
      "incomplete_value": false,
      "site": "0086d22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d1e4",
      "incomplete_value": false,
      "site": "0086d1ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
      "0086d22c",
      "DATA",
      [
        "storage",
        "00c7ed80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d22c",
      "DATA",
      [
        "storage",
        "00c7f180",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d1d4.md#insn-0086d1e0) · [`0086d1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d1d4.md#insn-0086d1e4) · [`0086d1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d1d4.md#insn-0086d1f0)
- 新版 `0086d220`（命令位置の公開資料なし） · `0086d224`（命令位置の公開資料なし） · `0086d230`（命令位置の公開資料なし）

~~~diff
- 0086d1e0 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 0086d220 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0086d1e0 bytes 882000b0
+ 0086d220 bytes 882000d0
- 0086d1e4 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 0086d1e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086d1e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086d1e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086d224 ["COPY", "tmp:0:8", ["const:180:8"]]
+ 0086d224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086d1e4 bytes 08013691
+ 0086d224 bytes 08010691
- 0086d1f0 ["INT_ADD", "register:40f0:8", ["const:86d1f0:8", "const:4:8"]]
- 0086d1f0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0086d230 ["INT_ADD", "register:40f0:8", ["const:86d230:8", "const:4:8"]]
+ 0086d230 ["CALL", null, ["callee:00c57ea0:8"]]
- 0086d1f0 bytes 2caa0f94
+ 0086d230 bytes 1cab0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e68572da3fa8f7508ca89deda3a63fe1"></a>

### [`0086d214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d214.md) → [`0086d254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d254.md) FUN_0086d254

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
      "definition_site": "0086d278",
      "incomplete_value": false,
      "site": "0086d278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d238",
      "incomplete_value": false,
      "site": "0086d238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
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
      "0086d278",
      "DATA",
      [
        "storage",
        "00c7edd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d278",
      "DATA",
      [
        "storage",
        "00c7f1d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d214.md#insn-0086d228) · [`0086d230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d214.md#insn-0086d230) · [`0086d234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d214.md#insn-0086d234)
- 新版 `0086d268`（命令位置の公開資料なし） · `0086d270`（命令位置の公開資料なし） · `0086d274`（命令位置の公開資料なし）

~~~diff
- 0086d228 ["INT_ADD", "register:40f0:8", ["const:86d228:8", "const:4:8"]]
- 0086d228 ["CALL", null, ["callee:00c57e90:8"]]
+ 0086d268 ["INT_ADD", "register:40f0:8", ["const:86d268:8", "const:4:8"]]
+ 0086d268 ["CALL", null, ["callee:00c57e90:8"]]
- 0086d228 bytes 1aaa0f94
+ 0086d268 bytes 0aab0f94
- 0086d230 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 0086d270 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0086d230 bytes 882000b0
+ 0086d270 bytes 882000d0
- 0086d234 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 0086d234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086d234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086d234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086d274 ["COPY", "tmp:0:8", ["const:1d0:8"]]
+ 0086d274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086d234 bytes 08413791
+ 0086d274 bytes 08410791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4bf3edbbc5cd6a372db249bf62a16be"></a>

### [`0086d248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d248.md) → [`0086d288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d288.md) FUN_0086d288

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
      "definition_site": "0086d294",
      "incomplete_value": false,
      "site": "0086d294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d254",
      "incomplete_value": false,
      "site": "0086d254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
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
      "0086d294",
      "DATA",
      [
        "storage",
        "00c7edd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d294",
      "DATA",
      [
        "storage",
        "00c7f1d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d248.md#insn-0086d24c) · [`0086d250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d248.md#insn-0086d250)
- 新版 `0086d28c`（命令位置の公開資料なし） · `0086d290`（命令位置の公開資料なし）

~~~diff
- 0086d24c ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 0086d28c ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0086d24c bytes 892000b0
+ 0086d28c bytes 892000d0
- 0086d250 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 0086d250 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086d250 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086d250 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086d290 ["COPY", "tmp:0:8", ["const:1d0:8"]]
+ 0086d290 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d290 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d290 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086d250 bytes 29413791
+ 0086d290 bytes 29410791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af76825bb89366c584eb2b566405cbcb"></a>

### [`0086d264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d264.md) → [`0086d2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d2a4.md) FUN_0086d2a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "0086d2c8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086d288",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "0086d2c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0086d2c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d264.md#insn-0086d288) · [`0086d294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d264.md#insn-0086d294)
- 新版 `0086d2c8`（命令位置の公開資料なし） · `0086d2d4`（命令位置の公開資料なし）

~~~diff
- 0086d288 ["INT_ADD", "register:40f0:8", ["const:86d288:8", "const:4:8"]]
- 0086d288 ["CALL", null, ["ram:47acb4:8"]]
+ 0086d2c8 ["INT_ADD", "register:40f0:8", ["const:86d2c8:8", "const:4:8"]]
+ 0086d2c8 ["CALL", null, ["ram:47acf4:8"]]
- 0086d288 bytes 8b36f097
+ 0086d2c8 bytes 8b36f097
- 0086d294 ["INT_ADD", "register:40f0:8", ["const:86d294:8", "const:4:8"]]
- 0086d294 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0086d2d4 ["INT_ADD", "register:40f0:8", ["const:86d2d4:8", "const:4:8"]]
+ 0086d2d4 ["CALL", null, ["callee:0047cdd4:8"]]
- 0086d294 bytes c03ef097
+ 0086d2d4 bytes c03ef097
~~~


<a id="compare-0e79ca06062a349f1869049b13cd2251"></a>

### [`0086d2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d2d8.md) → [`0086d318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d318.md) FUN_0086d318

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
      "definition_site": "0086d33c",
      "incomplete_value": false,
      "site": "0086d33c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d2fc",
      "incomplete_value": false,
      "site": "0086d2fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
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
      "0086d33c",
      "DATA",
      [
        "storage",
        "00c7ee50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d33c",
      "DATA",
      [
        "storage",
        "00c7f250",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d2d8.md#insn-0086d2ec) · [`0086d2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d2d8.md#insn-0086d2f4) · [`0086d2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d2d8.md#insn-0086d2f8)
- 新版 `0086d32c`（命令位置の公開資料なし） · `0086d334`（命令位置の公開資料なし） · `0086d338`（命令位置の公開資料なし）

~~~diff
- 0086d2ec ["INT_ADD", "register:40f0:8", ["const:86d2ec:8", "const:4:8"]]
- 0086d2ec ["CALL", null, ["callee:00c57e90:8"]]
+ 0086d32c ["INT_ADD", "register:40f0:8", ["const:86d32c:8", "const:4:8"]]
+ 0086d32c ["CALL", null, ["callee:00c57e90:8"]]
- 0086d2ec bytes e9a90f94
+ 0086d32c bytes d9aa0f94
- 0086d2f4 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 0086d334 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0086d2f4 bytes 882000b0
+ 0086d334 bytes 882000d0
- 0086d2f8 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 0086d2f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086d2f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086d2f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086d338 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 0086d338 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d338 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d338 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086d2f8 bytes 08413991
+ 0086d338 bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c04fc9c388ce892a9b314431aab3f78c"></a>

### [`0086d30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d30c.md) → [`0086d34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d34c.md) FUN_0086d34c

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
      "definition_site": "0086d358",
      "incomplete_value": false,
      "site": "0086d358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d318",
      "incomplete_value": false,
      "site": "0086d318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
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
      "0086d358",
      "DATA",
      [
        "storage",
        "00c7ee50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d358",
      "DATA",
      [
        "storage",
        "00c7f250",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d30c.md#insn-0086d310) · [`0086d314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d30c.md#insn-0086d314)
- 新版 `0086d350`（命令位置の公開資料なし） · `0086d354`（命令位置の公開資料なし）

~~~diff
- 0086d310 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 0086d350 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0086d310 bytes 892000b0
+ 0086d350 bytes 892000d0
- 0086d314 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 0086d314 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086d314 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086d314 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086d354 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 0086d354 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d354 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d354 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086d314 bytes 29413991
+ 0086d354 bytes 29410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90f10cdc14c7186cfcfc32c97845f6a6"></a>

### [`0086d328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d328.md) → [`0086d368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d368.md) FUN_0086d368

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "0086d38c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086d34c",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "0086d38c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0086d38c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d328.md#insn-0086d34c) · [`0086d358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d328.md#insn-0086d358)
- 新版 `0086d38c`（命令位置の公開資料なし） · `0086d398`（命令位置の公開資料なし）

~~~diff
- 0086d34c ["INT_ADD", "register:40f0:8", ["const:86d34c:8", "const:4:8"]]
- 0086d34c ["CALL", null, ["ram:47acb4:8"]]
+ 0086d38c ["INT_ADD", "register:40f0:8", ["const:86d38c:8", "const:4:8"]]
+ 0086d38c ["CALL", null, ["ram:47acf4:8"]]
- 0086d34c bytes 5a36f097
+ 0086d38c bytes 5a36f097
- 0086d358 ["INT_ADD", "register:40f0:8", ["const:86d358:8", "const:4:8"]]
- 0086d358 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0086d398 ["INT_ADD", "register:40f0:8", ["const:86d398:8", "const:4:8"]]
+ 0086d398 ["CALL", null, ["callee:0047cdd4:8"]]
- 0086d358 bytes 8f3ef097
+ 0086d398 bytes 8f3ef097
~~~


<a id="compare-568bc438afc4f0b92e1e5553d9be4ecd"></a>

### [`0086d39c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d39c.md) → [`0086d3dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d3dc.md) FUN_0086d3dc

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
      "definition_site": "0086d400",
      "incomplete_value": false,
      "site": "0086d400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d3c0",
      "incomplete_value": false,
      "site": "0086d3c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
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
      "0086d400",
      "DATA",
      [
        "storage",
        "00c7eed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d400",
      "DATA",
      [
        "storage",
        "00c7f2d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d39c.md#insn-0086d3b0) · [`0086d3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d39c.md#insn-0086d3b8) · [`0086d3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d39c.md#insn-0086d3bc)
- 新版 `0086d3f0`（命令位置の公開資料なし） · `0086d3f8`（命令位置の公開資料なし） · `0086d3fc`（命令位置の公開資料なし）

~~~diff
- 0086d3b0 ["INT_ADD", "register:40f0:8", ["const:86d3b0:8", "const:4:8"]]
- 0086d3b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0086d3f0 ["INT_ADD", "register:40f0:8", ["const:86d3f0:8", "const:4:8"]]
+ 0086d3f0 ["CALL", null, ["callee:00c57e90:8"]]
- 0086d3b0 bytes b8a90f94
+ 0086d3f0 bytes a8aa0f94
- 0086d3b8 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 0086d3f8 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0086d3b8 bytes 882000b0
+ 0086d3f8 bytes 882000d0
- 0086d3bc ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 0086d3bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086d3bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086d3bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086d3fc ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 0086d3fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d3fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d3fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086d3bc bytes 08413b91
+ 0086d3fc bytes 08410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35919f1a544c5b5d3cfe7b0ff4ba23a7"></a>

### [`0086d3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d3d0.md) → [`0086d410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d410.md) FUN_0086d410

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
      "definition_site": "0086d41c",
      "incomplete_value": false,
      "site": "0086d41c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d3dc",
      "incomplete_value": false,
      "site": "0086d3dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
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
      "0086d41c",
      "DATA",
      [
        "storage",
        "00c7eed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d41c",
      "DATA",
      [
        "storage",
        "00c7f2d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d3d0.md#insn-0086d3d4) · [`0086d3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d3d0.md#insn-0086d3d8)
- 新版 `0086d414`（命令位置の公開資料なし） · `0086d418`（命令位置の公開資料なし）

~~~diff
- 0086d3d4 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 0086d414 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0086d3d4 bytes 892000b0
+ 0086d414 bytes 892000d0
- 0086d3d8 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 0086d3d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086d3d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086d3d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086d418 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 0086d418 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d418 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d418 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086d3d8 bytes 29413b91
+ 0086d418 bytes 29410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae9b0d89e6dda792956ff2265aa69f1c"></a>

### [`0086d3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d3ec.md) → [`0086d42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d42c.md) FUN_0086d42c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "0086d450",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086d410",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "0086d450",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0086d450",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d3ec.md#insn-0086d410) · [`0086d41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d3ec.md#insn-0086d41c)
- 新版 `0086d450`（命令位置の公開資料なし） · `0086d45c`（命令位置の公開資料なし）

~~~diff
- 0086d410 ["INT_ADD", "register:40f0:8", ["const:86d410:8", "const:4:8"]]
- 0086d410 ["CALL", null, ["ram:47acb4:8"]]
+ 0086d450 ["INT_ADD", "register:40f0:8", ["const:86d450:8", "const:4:8"]]
+ 0086d450 ["CALL", null, ["ram:47acf4:8"]]
- 0086d410 bytes 2936f097
+ 0086d450 bytes 2936f097
- 0086d41c ["INT_ADD", "register:40f0:8", ["const:86d41c:8", "const:4:8"]]
- 0086d41c ["CALL", null, ["callee:0047cdd4:8"]]
+ 0086d45c ["INT_ADD", "register:40f0:8", ["const:86d45c:8", "const:4:8"]]
+ 0086d45c ["CALL", null, ["callee:0047cdd4:8"]]
- 0086d41c bytes 5e3ef097
+ 0086d45c bytes 5e3ef097
~~~


<a id="compare-0bd841e934a48df52ff4a8022ea63dc9"></a>

### [`0086d460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d460.md) → [`0086d4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d4a0.md) FUN_0086d4a0

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
      "definition_site": "0086d4c4",
      "incomplete_value": false,
      "site": "0086d4c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d484",
      "incomplete_value": false,
      "site": "0086d484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "0086d4c4",
      "DATA",
      [
        "storage",
        "00c7ef50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d4c4",
      "DATA",
      [
        "storage",
        "00c7f350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d460.md#insn-0086d474) · [`0086d47c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d460.md#insn-0086d47c) · [`0086d480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d460.md#insn-0086d480)
- 新版 `0086d4b4`（命令位置の公開資料なし） · `0086d4bc`（命令位置の公開資料なし） · `0086d4c0`（命令位置の公開資料なし）

~~~diff
- 0086d474 ["INT_ADD", "register:40f0:8", ["const:86d474:8", "const:4:8"]]
- 0086d474 ["CALL", null, ["callee:00c57e90:8"]]
+ 0086d4b4 ["INT_ADD", "register:40f0:8", ["const:86d4b4:8", "const:4:8"]]
+ 0086d4b4 ["CALL", null, ["callee:00c57e90:8"]]
- 0086d474 bytes 87a90f94
+ 0086d4b4 bytes 77aa0f94
- 0086d47c ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 0086d4bc ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0086d47c bytes 882000b0
+ 0086d4bc bytes 882000d0
- 0086d480 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 0086d480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086d480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086d480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086d4c0 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 0086d4c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d4c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d4c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086d480 bytes 08413d91
+ 0086d4c0 bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b965ec82bffc7ffaa909cc816553db02"></a>

### [`0086d494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d494.md) → [`0086d4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d4d4.md) FUN_0086d4d4

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
      "definition_site": "0086d4e0",
      "incomplete_value": false,
      "site": "0086d4e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d4a0",
      "incomplete_value": false,
      "site": "0086d4a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "0086d4e0",
      "DATA",
      [
        "storage",
        "00c7ef50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d4e0",
      "DATA",
      [
        "storage",
        "00c7f350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d494.md#insn-0086d498) · [`0086d49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d494.md#insn-0086d49c)
- 新版 `0086d4d8`（命令位置の公開資料なし） · `0086d4dc`（命令位置の公開資料なし）

~~~diff
- 0086d498 ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 0086d4d8 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0086d498 bytes 892000b0
+ 0086d4d8 bytes 892000d0
- 0086d49c ["COPY", "tmp:0:8", ["const:f50:8"]]
- 0086d49c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086d49c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086d49c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086d4dc ["COPY", "tmp:0:8", ["const:350:8"]]
+ 0086d4dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d4dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d4dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086d49c bytes 29413d91
+ 0086d4dc bytes 29410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53b4a9268eb750b5fbc1fd5841088664"></a>

### [`0086d4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d4b0.md) → [`0086d4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d4f0.md) FUN_0086d4f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "0086d514",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086d4d4",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "0086d514",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0086d514",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d4b0.md#insn-0086d4d4) · [`0086d4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d4b0.md#insn-0086d4e0)
- 新版 `0086d514`（命令位置の公開資料なし） · `0086d520`（命令位置の公開資料なし）

~~~diff
- 0086d4d4 ["INT_ADD", "register:40f0:8", ["const:86d4d4:8", "const:4:8"]]
- 0086d4d4 ["CALL", null, ["ram:47acb4:8"]]
+ 0086d514 ["INT_ADD", "register:40f0:8", ["const:86d514:8", "const:4:8"]]
+ 0086d514 ["CALL", null, ["ram:47acf4:8"]]
- 0086d4d4 bytes f835f097
+ 0086d514 bytes f835f097
- 0086d4e0 ["INT_ADD", "register:40f0:8", ["const:86d4e0:8", "const:4:8"]]
- 0086d4e0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0086d520 ["INT_ADD", "register:40f0:8", ["const:86d520:8", "const:4:8"]]
+ 0086d520 ["CALL", null, ["callee:0047cdd4:8"]]
- 0086d4e0 bytes 2d3ef097
+ 0086d520 bytes 2d3ef097
~~~


<a id="compare-62794491bbdaac4bb8452d4a1cbacdea"></a>

### [`0086d524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d524.md) → [`0086d564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d564.md) FUN_0086d564

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
      "definition_site": "0086d588",
      "incomplete_value": false,
      "site": "0086d588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d548",
      "incomplete_value": false,
      "site": "0086d548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
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
      "0086d588",
      "DATA",
      [
        "storage",
        "00c7efd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d588",
      "DATA",
      [
        "storage",
        "00c7f3d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d524.md#insn-0086d538) · [`0086d540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d524.md#insn-0086d540) · [`0086d544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d524.md#insn-0086d544)
- 新版 `0086d578`（命令位置の公開資料なし） · `0086d580`（命令位置の公開資料なし） · `0086d584`（命令位置の公開資料なし）

~~~diff
- 0086d538 ["INT_ADD", "register:40f0:8", ["const:86d538:8", "const:4:8"]]
- 0086d538 ["CALL", null, ["callee:00c57e90:8"]]
+ 0086d578 ["INT_ADD", "register:40f0:8", ["const:86d578:8", "const:4:8"]]
+ 0086d578 ["CALL", null, ["callee:00c57e90:8"]]
- 0086d538 bytes 56a90f94
+ 0086d578 bytes 46aa0f94
- 0086d540 ["COPY", "register:4040:8", ["const:c7e000:8"]]
+ 0086d580 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0086d540 bytes 882000b0
+ 0086d580 bytes 882000d0
- 0086d544 ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 0086d544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086d544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086d544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086d584 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 0086d584 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d584 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d584 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086d544 bytes 08413f91
+ 0086d584 bytes 08410f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65d1c6979d48cd56daa4d37b487d0a14"></a>

### [`0086d558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d558.md) → [`0086d598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d598.md) FUN_0086d598

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
      "definition_site": "0086d5a4",
      "incomplete_value": false,
      "site": "0086d5a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d564",
      "incomplete_value": false,
      "site": "0086d564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
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
      "0086d5a4",
      "DATA",
      [
        "storage",
        "00c7efd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d5a4",
      "DATA",
      [
        "storage",
        "00c7f3d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d558.md#insn-0086d55c) · [`0086d560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d558.md#insn-0086d560)
- 新版 `0086d59c`（命令位置の公開資料なし） · `0086d5a0`（命令位置の公開資料なし）

~~~diff
- 0086d55c ["COPY", "register:4048:8", ["const:c7e000:8"]]
+ 0086d59c ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0086d55c bytes 892000b0
+ 0086d59c bytes 892000d0
- 0086d560 ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 0086d560 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086d560 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086d560 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086d5a0 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 0086d5a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d5a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d5a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086d560 bytes 29413f91
+ 0086d5a0 bytes 29410f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4769fe642de278aa41da0bdcdcc20350"></a>

### [`0086d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d574.md) → [`0086d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d5b4.md) FUN_0086d5b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "0086d5d8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086d598",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "0086d5d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0086d5d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d574.md#insn-0086d598) · [`0086d5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d574.md#insn-0086d5a4)
- 新版 `0086d5d8`（命令位置の公開資料なし） · `0086d5e4`（命令位置の公開資料なし）

~~~diff
- 0086d598 ["INT_ADD", "register:40f0:8", ["const:86d598:8", "const:4:8"]]
- 0086d598 ["CALL", null, ["ram:47acb4:8"]]
+ 0086d5d8 ["INT_ADD", "register:40f0:8", ["const:86d5d8:8", "const:4:8"]]
+ 0086d5d8 ["CALL", null, ["ram:47acf4:8"]]
- 0086d598 bytes c735f097
+ 0086d5d8 bytes c735f097
- 0086d5a4 ["INT_ADD", "register:40f0:8", ["const:86d5a4:8", "const:4:8"]]
- 0086d5a4 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0086d5e4 ["INT_ADD", "register:40f0:8", ["const:86d5e4:8", "const:4:8"]]
+ 0086d5e4 ["CALL", null, ["callee:0047cdd4:8"]]
- 0086d5a4 bytes fc3df097
+ 0086d5e4 bytes fc3df097
~~~


<a id="compare-6a90a498541b4d1f3344054ff43a9ab1"></a>

### [`0086d5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d5ec.md) → [`0086d62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d62c.md) FUN_0086d62c

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
      "definition_site": "0086d650",
      "incomplete_value": false,
      "site": "0086d650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d610",
      "incomplete_value": false,
      "site": "0086d610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "0086d650",
      "DATA",
      [
        "storage",
        "00c7f050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d650",
      "DATA",
      [
        "storage",
        "00c7f450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d5ec.md#insn-0086d600) · [`0086d60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d5ec.md#insn-0086d60c)
- 新版 `0086d640`（命令位置の公開資料なし） · `0086d64c`（命令位置の公開資料なし）

~~~diff
- 0086d600 ["INT_ADD", "register:40f0:8", ["const:86d600:8", "const:4:8"]]
- 0086d600 ["CALL", null, ["callee:00c57e90:8"]]
+ 0086d640 ["INT_ADD", "register:40f0:8", ["const:86d640:8", "const:4:8"]]
+ 0086d640 ["CALL", null, ["callee:00c57e90:8"]]
- 0086d600 bytes 24a90f94
+ 0086d640 bytes 14aa0f94
- 0086d60c ["COPY", "tmp:0:8", ["const:50:8"]]
- 0086d60c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086d60c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086d60c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086d64c ["COPY", "tmp:0:8", ["const:450:8"]]
+ 0086d64c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d64c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d64c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086d60c bytes 08410191
+ 0086d64c bytes 08411191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d93220b709ec9616966170ae20a2c37"></a>

### [`0086d68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d68c.md) → [`0086d6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d6cc.md) FUN_0086d6cc

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
      "definition_site": "0086d6f0",
      "incomplete_value": false,
      "site": "0086d6f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d6b0",
      "incomplete_value": false,
      "site": "0086d6b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d0:8"
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
      "0086d6f0",
      "DATA",
      [
        "storage",
        "00c7f0d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d6f0",
      "DATA",
      [
        "storage",
        "00c7f4d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d68c.md#insn-0086d6a0) · [`0086d6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d68c.md#insn-0086d6ac)
- 新版 `0086d6e0`（命令位置の公開資料なし） · `0086d6ec`（命令位置の公開資料なし）

~~~diff
- 0086d6a0 ["INT_ADD", "register:40f0:8", ["const:86d6a0:8", "const:4:8"]]
- 0086d6a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0086d6e0 ["INT_ADD", "register:40f0:8", ["const:86d6e0:8", "const:4:8"]]
+ 0086d6e0 ["CALL", null, ["callee:00c57e90:8"]]
- 0086d6a0 bytes fca80f94
+ 0086d6e0 bytes eca90f94
- 0086d6ac ["COPY", "tmp:0:8", ["const:d0:8"]]
- 0086d6ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086d6ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086d6ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086d6ec ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 0086d6ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d6ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d6ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086d6ac bytes 08410391
+ 0086d6ec bytes 08411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5711aa3e89304397d73c6443b7eae06b"></a>

### [`0086d6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6c0.md) → [`0086d700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d700.md) FUN_0086d700

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
      "definition_site": "0086d70c",
      "incomplete_value": false,
      "site": "0086d70c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d6cc",
      "incomplete_value": false,
      "site": "0086d6cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d0:8"
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
      "0086d70c",
      "DATA",
      [
        "storage",
        "00c7f0d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d70c",
      "DATA",
      [
        "storage",
        "00c7f4d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6c0.md#insn-0086d6c8)
- 新版 `0086d708`（命令位置の公開資料なし）

~~~diff
- 0086d6c8 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 0086d6c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086d6c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086d6c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086d708 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 0086d708 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d708 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d708 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086d6c8 bytes 29410391
+ 0086d708 bytes 29411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffbf31545910a8d7f6b2f9f6f5164822"></a>

### [`0086d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md) → [`0086d71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d71c.md) FUN_0086d71c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0044f858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f858.md) [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md) [`00464838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464838.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0044f898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f898.md) [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) [`0046479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md) [`00464878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464878.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.13% / 新版 97.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086d824",
      "incomplete_value": true,
      "site": "0086d834",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:183:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d7e4",
      "incomplete_value": true,
      "site": "0086d7f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:143:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0086d8cc",
      "incomplete_value": false,
      "site": "0086d8cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086d88c",
      "incomplete_value": false,
      "site": "0086d88c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 61,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0086da80",
      "incomplete_value": false,
      "site": "0086da84",
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
    "old": {
      "definition_site": "0086da40",
      "incomplete_value": false,
      "site": "0086da44",
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
                "const:130:8"
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
    "ordinal": 109,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0086d824",
      "READ",
      [
        "storage",
        "002bf143",
        null,
        "string"
      ]
    ],
    [
      "0086d8cc",
      "DATA",
      [
        "storage",
        "00c7f150",
        null,
        "undefined *"
      ]
    ],
    [
      "0086da2c",
      "READ",
      [
        "storage",
        "00c7f178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d824",
      "READ",
      [
        "storage",
        "002bf183",
        null,
        "string"
      ]
    ],
    [
      "0086d8cc",
      "DATA",
      [
        "storage",
        "00c7f550",
        null,
        "undefined *"
      ]
    ],
    [
      "0086da2c",
      "READ",
      [
        "storage",
        "00c7f578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086da84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md#insn-0086da84) · [`0086d7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md#insn-0086d7d4) · [`0086d7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md#insn-0086d7dc)
- 新版 `0086dac4`（命令位置の公開資料なし） · `0086d814`（命令位置の公開資料なし） · `0086d81c`（命令位置の公開資料なし）

~~~diff
- 0086da84 ["COPY", "register:0:8", ["register:4040:8"]]
- 0086da84 ["INT_ADD", "register:40f0:8", ["const:86da84:8", "const:4:8"]]
- 0086da84 ["CALLIND", null, ["register:0:8"]]
+ 0086dac4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0086dac4 ["INT_ADD", "register:40f0:8", ["const:86dac4:8", "const:4:8"]]
+ 0086dac4 ["CALLIND", null, ["register:0:8"]]
- 0086da84 bytes 00013fd6
+ 0086dac4 bytes 00013fd6
- 0086d7d4 ["INT_ADD", "register:40f0:8", ["const:86d7d4:8", "const:4:8"]]
- 0086d7d4 ["CALL", null, ["callee:00481430:8"]]
+ 0086d814 ["INT_ADD", "register:40f0:8", ["const:86d814:8", "const:4:8"]]
+ 0086d814 ["CALL", null, ["callee:00481430:8"]]
- 0086d7d4 bytes 074ff097
+ 0086d814 bytes 074ff097
- 0086d7dc ["COPY", "tmp:0:8", ["const:143:8"]]
- 0086d7dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086d7dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086d7dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086d81c ["COPY", "tmp:0:8", ["const:183:8"]]
+ 0086d81c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d81c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086d81c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086d7dc bytes 290d0591
+ 0086d81c bytes 290d0691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96bedc803f3ca46a870501d5c472a416"></a>

### [`0086dc24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc24.md) → [`0086dc64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dc64.md) FUN_0086dc64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md)

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
      "definition_site": "0086dc6c",
      "incomplete_value": false,
      "site": "0086dc70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086dc2c",
      "incomplete_value": false,
      "site": "0086dc30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "0086dc70",
      "DATA",
      [
        "storage",
        "00c7f150",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086dc70",
      "DATA",
      [
        "storage",
        "00c7f550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086dc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc24.md#insn-0086dc2c)
- 新版 `0086dc6c`（命令位置の公開資料なし）

~~~diff
- 0086dc2c ["COPY", "tmp:0:8", ["const:150:8"]]
- 0086dc2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086dc2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086dc2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086dc6c ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0086dc6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086dc6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086dc6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086dc2c bytes 29410591
+ 0086dc6c bytes 29411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-251e0f400537640c1d0123a9303823aa"></a>

### [`0086dc44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc44.md) → [`0086dc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dc84.md) FUN_0086dc84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0086dc8c",
      "incomplete_value": false,
      "site": "0086dc90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086dc4c",
      "incomplete_value": false,
      "site": "0086dc50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "0086dc90",
      "DATA",
      [
        "storage",
        "00c7f150",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086dc90",
      "DATA",
      [
        "storage",
        "00c7f550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086dc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc44.md#insn-0086dc4c) · [`0086dc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc44.md#insn-0086dc6c)
- 新版 `0086dc8c`（命令位置の公開資料なし） · `0086dcac`（命令位置の公開資料なし）

~~~diff
- 0086dc4c ["COPY", "tmp:0:8", ["const:150:8"]]
- 0086dc4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086dc4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086dc4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086dc8c ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0086dc8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086dc8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086dc8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086dc4c bytes 29410591
+ 0086dc8c bytes 29411591
- 0086dc6c ["INT_ADD", "register:40f0:8", ["const:86dc6c:8", "const:4:8"]]
- 0086dc6c ["CALL", null, ["callee:0046479c:8"]]
+ 0086dcac ["INT_ADD", "register:40f0:8", ["const:86dcac:8", "const:4:8"]]
+ 0086dcac ["CALL", null, ["callee:0046479c:8"]]
- 0086dc6c bytes bcdaef97
+ 0086dcac bytes bcdaef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a061e7fbc6c46b056a0f07f8c6e2e1ba"></a>

### [`0086dc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc80.md) → [`0086dcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dcc0.md) FUN_0086dcc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00464838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464838.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00464878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464878.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0086dcf4",
      "incomplete_value": false,
      "site": "0086dcf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086dcb4",
      "incomplete_value": false,
      "site": "0086dcb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "0086dcf4",
      "DATA",
      [
        "storage",
        "00c7f150",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086dcf4",
      "DATA",
      [
        "storage",
        "00c7f550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086dc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc80.md#insn-0086dc98) · [`0086dca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc80.md#insn-0086dca4) · [`0086dccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc80.md#insn-0086dccc)
- 新版 `0086dcd8`（命令位置の公開資料なし） · `0086dce4`（命令位置の公開資料なし） · `0086dd0c`（命令位置の公開資料なし）

~~~diff
- 0086dc98 ["INT_ADD", "register:40f0:8", ["const:86dc98:8", "const:4:8"]]
- 0086dc98 ["CALL", null, ["callee:00c57e90:8"]]
+ 0086dcd8 ["INT_ADD", "register:40f0:8", ["const:86dcd8:8", "const:4:8"]]
+ 0086dcd8 ["CALL", null, ["callee:00c57e90:8"]]
- 0086dc98 bytes 7ea70f94
+ 0086dcd8 bytes 6ea80f94
- 0086dca4 ["COPY", "tmp:0:8", ["const:150:8"]]
- 0086dca4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086dca4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086dca4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086dce4 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0086dce4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086dce4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086dce4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086dca4 bytes 29410591
+ 0086dce4 bytes 29411591
- 0086dccc ["INT_ADD", "register:40f0:8", ["const:86dccc:8", "const:4:8"]]
- 0086dccc ["CALL", null, ["callee:00464878:8"]]
+ 0086dd0c ["INT_ADD", "register:40f0:8", ["const:86dd0c:8", "const:4:8"]]
+ 0086dd0c ["CALL", null, ["callee:00464878:8"]]
- 0086dccc bytes dbdaef97
+ 0086dd0c bytes dbdaef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8556d0f2e7850a4157c1abf51da44c2"></a>

### [`0086dd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dd10.md) → [`0086dd50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dd50.md) FUN_0086dd50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00464838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464838.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00464878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464878.md)

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
      "definition_site": "0086dd78",
      "incomplete_value": false,
      "site": "0086dd78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086dd38",
      "incomplete_value": false,
      "site": "0086dd38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "0086dd78",
      "DATA",
      [
        "storage",
        "00c7f150",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086dd78",
      "DATA",
      [
        "storage",
        "00c7f550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086dd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dd10.md#insn-0086dd30) · [`0086dd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dd10.md#insn-0086dd4c)
- 新版 `0086dd70`（命令位置の公開資料なし） · `0086dd8c`（命令位置の公開資料なし）

~~~diff
- 0086dd30 ["COPY", "tmp:0:8", ["const:150:8"]]
- 0086dd30 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0086dd30 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0086dd30 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0086dd70 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0086dd70 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0086dd70 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0086dd70 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0086dd30 bytes 4a410591
+ 0086dd70 bytes 4a411591
- 0086dd4c ["INT_ADD", "register:40f0:8", ["const:86dd4c:8", "const:4:8"]]
- 0086dd4c ["CALL", null, ["callee:00464878:8"]]
+ 0086dd8c ["INT_ADD", "register:40f0:8", ["const:86dd8c:8", "const:4:8"]]
+ 0086dd8c ["CALL", null, ["callee:00464878:8"]]
- 0086dd4c bytes bbdaef97
+ 0086dd8c bytes bbdaef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f9372a42ad2c585348c3097dc4f1c5f"></a>

### [`0086de64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086de64.md) → [`0086dea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dea4.md) FUN_0086dea4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0085b2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b2b8.md) [`0086de64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086de64.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0085b2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2f8.md) [`0086dea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dea4.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.66% / 新版 98.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0086e014",
      "incomplete_value": false,
      "site": "0086e01c",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086dfd4",
      "incomplete_value": false,
      "site": "0086dfdc",
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
            "const:f13:8"
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
      "definition_site": "0086e0d4",
      "incomplete_value": true,
      "site": "0086e0dc",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086e094",
      "incomplete_value": true,
      "site": "0086e09c",
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
            "const:da7:8"
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
      "definition_site": "0086e1a0",
      "incomplete_value": false,
      "site": "0086e1ac",
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
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086e160",
      "incomplete_value": false,
      "site": "0086e16c",
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
            "const:ea9:8"
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
      "0086e014",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0086e0d4",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0086e0f0",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0086e014",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0086e0d4",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0086e0f0",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086dfdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086de64.md#insn-0086dfdc) · [`0086e09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086de64.md#insn-0086e09c) · [`0086e16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086de64.md#insn-0086e16c)
- 新版 `0086e01c`（命令位置の公開資料なし） · `0086e0dc`（命令位置の公開資料なし） · `0086e1ac`（命令位置の公開資料なし）

~~~diff
- 0086dfdc ["INT_ADD", "register:40f0:8", ["const:86dfdc:8", "const:4:8"]]
- 0086dfdc ["CALL", null, ["callee:00441e94:8"]]
+ 0086e01c ["INT_ADD", "register:40f0:8", ["const:86e01c:8", "const:4:8"]]
+ 0086e01c ["CALL", null, ["callee:00441e94:8"]]
- 0086dfdc bytes 9e4fef97
+ 0086e01c bytes 9e4fef97
- 0086e09c ["INT_ADD", "register:40f0:8", ["const:86e09c:8", "const:4:8"]]
- 0086e09c ["CALL", null, ["callee:00441e94:8"]]
+ 0086e0dc ["INT_ADD", "register:40f0:8", ["const:86e0dc:8", "const:4:8"]]
+ 0086e0dc ["CALL", null, ["callee:00441e94:8"]]
- 0086e09c bytes 6e4fef97
+ 0086e0dc bytes 6e4fef97
- 0086e16c ["INT_ADD", "register:40f0:8", ["const:86e16c:8", "const:4:8"]]
- 0086e16c ["CALL", null, ["callee:004427f4:8"]]
+ 0086e1ac ["INT_ADD", "register:40f0:8", ["const:86e1ac:8", "const:4:8"]]
+ 0086e1ac ["CALL", null, ["callee:004427f4:8"]]
- 0086e16c bytes 9251ef97
+ 0086e1ac bytes 9251ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04d512b5f30c621303324612a907c994"></a>

### [`0086e764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086e/0086e764.md) → [`0086e7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086e/0086e7a4.md) FUN_0086e7a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0086de64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086de64.md) [`0086e764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086e/0086e764.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0086dea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dea4.md) [`0086e7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086e/0086e7a4.md) · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

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
      "definition_site": "0086e8fc",
      "incomplete_value": false,
      "site": "0086e904",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086e8bc",
      "incomplete_value": false,
      "site": "0086e8c4",
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
            "const:f13:8"
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
      "definition_site": "0086e9b8",
      "incomplete_value": false,
      "site": "0086e9c0",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086e978",
      "incomplete_value": false,
      "site": "0086e980",
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
            "const:da7:8"
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
      "definition_site": "0086e9d0",
      "incomplete_value": false,
      "site": "0086e9dc",
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
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086e990",
      "incomplete_value": false,
      "site": "0086e99c",
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
            "const:ea9:8"
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
      "0086e8fc",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0086e9b8",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0086e9d0",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0086e8fc",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0086e9b8",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0086e9d0",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086e8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086e/0086e764.md#insn-0086e8c4) · [`0086e980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086e/0086e764.md#insn-0086e980) · [`0086e99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086e/0086e764.md#insn-0086e99c)
- 新版 `0086e904`（命令位置の公開資料なし） · `0086e9c0`（命令位置の公開資料なし） · `0086e9dc`（命令位置の公開資料なし）

~~~diff
- 0086e8c4 ["INT_ADD", "register:40f0:8", ["const:86e8c4:8", "const:4:8"]]
- 0086e8c4 ["CALL", null, ["callee:00441e94:8"]]
+ 0086e904 ["INT_ADD", "register:40f0:8", ["const:86e904:8", "const:4:8"]]
+ 0086e904 ["CALL", null, ["callee:00441e94:8"]]
- 0086e8c4 bytes 644def97
+ 0086e904 bytes 644def97
- 0086e980 ["INT_ADD", "register:40f0:8", ["const:86e980:8", "const:4:8"]]
- 0086e980 ["CALL", null, ["callee:00441e94:8"]]
+ 0086e9c0 ["INT_ADD", "register:40f0:8", ["const:86e9c0:8", "const:4:8"]]
+ 0086e9c0 ["CALL", null, ["callee:00441e94:8"]]
- 0086e980 bytes 354def97
+ 0086e9c0 bytes 354def97
- 0086e99c ["INT_ADD", "register:40f0:8", ["const:86e99c:8", "const:4:8"]]
- 0086e99c ["CALL", null, ["callee:004427f4:8"]]
+ 0086e9dc ["INT_ADD", "register:40f0:8", ["const:86e9dc:8", "const:4:8"]]
+ 0086e9dc ["CALL", null, ["callee:004427f4:8"]]
- 0086e99c bytes 864fef97
+ 0086e9dc bytes 864fef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a5dd492516f2c18a457363cf3cd663c"></a>

### [`0086f09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f09c.md) → [`0086f0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086f0dc.md) FUN_0086f0dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0086e764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086e/0086e764.md) [`0086f09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f09c.md) [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 3件 [`0086e7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086e/0086e7a4.md) [`0086f0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086f0dc.md) [`0089788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/0089788c.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

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
      "definition_site": "0086f22c",
      "incomplete_value": false,
      "site": "0086f234",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086f1ec",
      "incomplete_value": false,
      "site": "0086f1f4",
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
            "const:f13:8"
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
      "definition_site": "0086f250",
      "incomplete_value": false,
      "site": "0086f25c",
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
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086f210",
      "incomplete_value": false,
      "site": "0086f21c",
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
            "const:ea9:8"
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
      "definition_site": "0086f384",
      "incomplete_value": false,
      "site": "0086f38c",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086f344",
      "incomplete_value": false,
      "site": "0086f34c",
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
            "const:da7:8"
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
      "0086f22c",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0086f250",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0086f384",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0086f22c",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0086f250",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "0086f384",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086f1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f09c.md#insn-0086f1f4) · [`0086f21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f09c.md#insn-0086f21c) · [`0086f34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f09c.md#insn-0086f34c)
- 新版 `0086f234`（命令位置の公開資料なし） · `0086f25c`（命令位置の公開資料なし） · `0086f38c`（命令位置の公開資料なし）

~~~diff
- 0086f1f4 ["INT_ADD", "register:40f0:8", ["const:86f1f4:8", "const:4:8"]]
- 0086f1f4 ["CALL", null, ["callee:00441e94:8"]]
+ 0086f234 ["INT_ADD", "register:40f0:8", ["const:86f234:8", "const:4:8"]]
+ 0086f234 ["CALL", null, ["callee:00441e94:8"]]
- 0086f1f4 bytes 184bef97
+ 0086f234 bytes 184bef97
- 0086f21c ["INT_ADD", "register:40f0:8", ["const:86f21c:8", "const:4:8"]]
- 0086f21c ["CALL", null, ["callee:004427f4:8"]]
+ 0086f25c ["INT_ADD", "register:40f0:8", ["const:86f25c:8", "const:4:8"]]
+ 0086f25c ["CALL", null, ["callee:004427f4:8"]]
- 0086f21c bytes 664def97
+ 0086f25c bytes 664def97
- 0086f34c ["INT_ADD", "register:40f0:8", ["const:86f34c:8", "const:4:8"]]
- 0086f34c ["CALL", null, ["callee:00441e94:8"]]
+ 0086f38c ["INT_ADD", "register:40f0:8", ["const:86f38c:8", "const:4:8"]]
+ 0086f38c ["CALL", null, ["callee:00441e94:8"]]
- 0086f34c bytes c24aef97
+ 0086f38c bytes c24aef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6140b46b8b4e25b4fe6a795028ea18d"></a>

### [`0086f88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f88c.md) → [`0086f8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086f8cc.md) FUN_0086f8cc

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
      "definition_site": "0086f8f0",
      "incomplete_value": false,
      "site": "0086f8f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086f8b0",
      "incomplete_value": false,
      "site": "0086f8b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "0086f8f0",
      "DATA",
      [
        "storage",
        "00c7f1f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086f8f0",
      "DATA",
      [
        "storage",
        "00c7f5f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f88c.md#insn-0086f8a0) · [`0086f8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f88c.md#insn-0086f8ac)
- 新版 `0086f8e0`（命令位置の公開資料なし） · `0086f8ec`（命令位置の公開資料なし）

~~~diff
- 0086f8a0 ["INT_ADD", "register:40f0:8", ["const:86f8a0:8", "const:4:8"]]
- 0086f8a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0086f8e0 ["INT_ADD", "register:40f0:8", ["const:86f8e0:8", "const:4:8"]]
+ 0086f8e0 ["CALL", null, ["callee:00c57e90:8"]]
- 0086f8a0 bytes 7ca00f94
+ 0086f8e0 bytes 6ca10f94
- 0086f8ac ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 0086f8ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086f8ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086f8ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086f8ec ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 0086f8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086f8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086f8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086f8ac bytes 08c10791
+ 0086f8ec bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35bd954681fe8c7be0d4858d25163766"></a>

### [`0086f8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f8c0.md) → [`0086f900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086f900.md) FUN_0086f900

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
      "definition_site": "0086f90c",
      "incomplete_value": false,
      "site": "0086f90c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086f8cc",
      "incomplete_value": false,
      "site": "0086f8cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "0086f90c",
      "DATA",
      [
        "storage",
        "00c7f1f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086f90c",
      "DATA",
      [
        "storage",
        "00c7f5f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086f8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f8c0.md#insn-0086f8c8)
- 新版 `0086f908`（命令位置の公開資料なし）

~~~diff
- 0086f8c8 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 0086f8c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086f8c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086f8c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086f908 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 0086f908 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086f908 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086f908 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086f8c8 bytes 29c10791
+ 0086f908 bytes 29c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c6899ede4749a5da684a8ec846a978a"></a>

### [`0086f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f8dc.md) → [`0086f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086f91c.md) FUN_0086f91c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0044dd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dd40.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0044dd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dd80.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.98% / 新版 95.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086f9fc",
      "incomplete_value": true,
      "site": "0086fa0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:537:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086f9bc",
      "incomplete_value": true,
      "site": "0086f9cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46a:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0086facc",
      "incomplete_value": false,
      "site": "0086facc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086fa8c",
      "incomplete_value": false,
      "site": "0086fa8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086f958",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086f918",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "0086f958",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0086f96c",
      "PARAM",
      [
        "storage",
        "002c1730",
        null,
        "string"
      ]
    ],
    [
      "0086f9ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "0086f958",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0086f96c",
      "PARAM",
      [
        "storage",
        "002c1770",
        null,
        "string"
      ]
    ],
    [
      "0086f9ec",
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

- 旧版 [`0086f918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f8dc.md#insn-0086f918) · [`0086f934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f8dc.md#insn-0086f934) · [`0086f9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f8dc.md#insn-0086f9ac)
- 新版 `0086f958`（命令位置の公開資料なし） · `0086f974`（命令位置の公開資料なし） · `0086f9ec`（命令位置の公開資料なし）

~~~diff
- 0086f918 ["INT_ADD", "register:40f0:8", ["const:86f918:8", "const:4:8"]]
- 0086f918 ["CALL", null, ["ram:48ccb8:8"]]
+ 0086f958 ["INT_ADD", "register:40f0:8", ["const:86f958:8", "const:4:8"]]
+ 0086f958 ["CALL", null, ["ram:48ccf8:8"]]
- 0086f918 bytes e874f097
+ 0086f958 bytes e874f097
- 0086f934 ["INT_ADD", "register:40f0:8", ["const:86f934:8", "const:4:8"]]
- 0086f934 ["CALL", null, ["callee:00c57f70:8"]]
+ 0086f974 ["INT_ADD", "register:40f0:8", ["const:86f974:8", "const:4:8"]]
+ 0086f974 ["CALL", null, ["callee:00c57f70:8"]]
- 0086f934 bytes 8fa00f94
+ 0086f974 bytes 7fa10f94
- 0086f9ac ["INT_ADD", "register:40f0:8", ["const:86f9ac:8", "const:4:8"]]
- 0086f9ac ["CALL", null, ["ram:48ccb8:8"]]
+ 0086f9ec ["INT_ADD", "register:40f0:8", ["const:86f9ec:8", "const:4:8"]]
+ 0086f9ec ["CALL", null, ["ram:48ccf8:8"]]
- 0086f9ac bytes c374f097
+ 0086f9ec bytes c374f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b3716051ee0f9e1ea7839858e634b7b"></a>

### [`0086fd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fd60.md) → [`0086fda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086fda0.md) FUN_0086fda0

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
      "definition_site": "0086fdc4",
      "incomplete_value": false,
      "site": "0086fdc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086fd84",
      "incomplete_value": false,
      "site": "0086fd84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "0086fdc4",
      "DATA",
      [
        "storage",
        "00c7f260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086fdc4",
      "DATA",
      [
        "storage",
        "00c7f660",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086fd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fd60.md#insn-0086fd74) · [`0086fd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fd60.md#insn-0086fd80)
- 新版 `0086fdb4`（命令位置の公開資料なし） · `0086fdc0`（命令位置の公開資料なし）

~~~diff
- 0086fd74 ["INT_ADD", "register:40f0:8", ["const:86fd74:8", "const:4:8"]]
- 0086fd74 ["CALL", null, ["callee:00c57e90:8"]]
+ 0086fdb4 ["INT_ADD", "register:40f0:8", ["const:86fdb4:8", "const:4:8"]]
+ 0086fdb4 ["CALL", null, ["callee:00c57e90:8"]]
- 0086fd74 bytes 479f0f94
+ 0086fdb4 bytes 37a00f94
- 0086fd80 ["COPY", "tmp:0:8", ["const:260:8"]]
- 0086fd80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086fd80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086fd80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086fdc0 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 0086fdc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086fdc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086fdc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086fd80 bytes 08810991
+ 0086fdc0 bytes 08811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00ac36506180790e2aaaf8b9cacf7728"></a>

### [`0086fd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fd94.md) → [`0086fdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086fdd4.md) FUN_0086fdd4

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
      "definition_site": "0086fde0",
      "incomplete_value": false,
      "site": "0086fde0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086fda0",
      "incomplete_value": false,
      "site": "0086fda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "0086fde0",
      "DATA",
      [
        "storage",
        "00c7f260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086fde0",
      "DATA",
      [
        "storage",
        "00c7f660",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086fd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fd94.md#insn-0086fd9c)
- 新版 `0086fddc`（命令位置の公開資料なし）

~~~diff
- 0086fd9c ["COPY", "tmp:0:8", ["const:260:8"]]
- 0086fd9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086fd9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086fd9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086fddc ["COPY", "tmp:0:8", ["const:660:8"]]
+ 0086fddc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086fddc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086fddc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086fd9c bytes 29810991
+ 0086fddc bytes 29811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88f4d60ff0dfccaa188fc1e1f9ca730b"></a>

### [`0086fdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fdf0.md) → [`0086fe30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086fe30.md) FUN_0086fe30

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
      "definition_site": "0086fe34",
      "incomplete_value": false,
      "site": "0086fe38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086fdf4",
      "incomplete_value": false,
      "site": "0086fdf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "0086fe38",
      "DATA",
      [
        "storage",
        "00c7f2f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0086fe38",
      "DATA",
      [
        "storage",
        "00c7f6f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086fdf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fdf0.md#insn-0086fdf4)
- 新版 `0086fe34`（命令位置の公開資料なし）

~~~diff
- 0086fdf4 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 0086fdf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086fdf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086fdf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086fe34 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 0086fe34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086fe34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086fe34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086fdf4 bytes 08c10b91
+ 0086fe34 bytes 08c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f135c064cdf6bb984f9ebe9a10607802"></a>

### [`0086fe00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fe00.md) → [`0086fe40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086fe40.md) FUN_0086fe40

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
      "definition_site": "0086fe50",
      "incomplete_value": false,
      "site": "0086fe58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086fe10",
      "incomplete_value": false,
      "site": "0086fe18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "0086fe58",
      "DATA",
      [
        "storage",
        "00c7f2f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0086fe58",
      "DATA",
      [
        "storage",
        "00c7f6f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086fe10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fe00.md#insn-0086fe10) · [`0086fe1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fe00.md#insn-0086fe1c)
- 新版 `0086fe50`（命令位置の公開資料なし） · `0086fe5c`（命令位置の公開資料なし）

~~~diff
- 0086fe10 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 0086fe10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086fe10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086fe10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086fe50 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 0086fe50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086fe50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086fe50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086fe10 bytes 08c10b91
+ 0086fe50 bytes 08c11b91
- 0086fe1c ["INT_ADD", "register:40f0:8", ["const:86fe1c:8", "const:4:8"]]
- 0086fe1c ["CALL", null, ["callee:00c57ea0:8"]]
+ 0086fe5c ["INT_ADD", "register:40f0:8", ["const:86fe5c:8", "const:4:8"]]
+ 0086fe5c ["CALL", null, ["callee:00c57ea0:8"]]
- 0086fe1c bytes 219f0f94
+ 0086fe5c bytes 11a00f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad01f333027c45e3f5aee4b2233f0dc4"></a>

### [`0086fe44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fe44.md) → [`0086fe84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086fe84.md) FUN_0086fe84

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
      "definition_site": "0086fea4",
      "incomplete_value": false,
      "site": "0086fea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086fe64",
      "incomplete_value": false,
      "site": "0086fe68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "0086fea8",
      "DATA",
      [
        "storage",
        "00c7f340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086fea8",
      "DATA",
      [
        "storage",
        "00c7f740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086fe58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fe44.md#insn-0086fe58) · [`0086fe64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fe44.md#insn-0086fe64)
- 新版 `0086fe98`（命令位置の公開資料なし） · `0086fea4`（命令位置の公開資料なし）

~~~diff
- 0086fe58 ["INT_ADD", "register:40f0:8", ["const:86fe58:8", "const:4:8"]]
- 0086fe58 ["CALL", null, ["callee:00c57e90:8"]]
+ 0086fe98 ["INT_ADD", "register:40f0:8", ["const:86fe98:8", "const:4:8"]]
+ 0086fe98 ["CALL", null, ["callee:00c57e90:8"]]
- 0086fe58 bytes 0e9f0f94
+ 0086fe98 bytes fe9f0f94
- 0086fe64 ["COPY", "tmp:0:8", ["const:340:8"]]
- 0086fe64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086fe64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086fe64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086fea4 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0086fea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086fea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086fea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086fe64 bytes 08010d91
+ 0086fea4 bytes 08011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4760dc067fed381bd21d39e39aa9b2ea"></a>

### [`0086fe7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fe7c.md) → [`0086febc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086febc.md) FUN_0086febc

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
      "definition_site": "0086fec0",
      "incomplete_value": false,
      "site": "0086fec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086fe80",
      "incomplete_value": false,
      "site": "0086fe84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "0086fec4",
      "DATA",
      [
        "storage",
        "00c7f340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086fec4",
      "DATA",
      [
        "storage",
        "00c7f740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086fe80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fe7c.md#insn-0086fe80)
- 新版 `0086fec0`（命令位置の公開資料なし）

~~~diff
- 0086fe80 ["COPY", "tmp:0:8", ["const:340:8"]]
- 0086fe80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086fe80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086fe80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086fec0 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0086fec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086fec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086fec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086fe80 bytes 08010d91
+ 0086fec0 bytes 08011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-688046e92832dc22de80844b37e06935"></a>

### [`0086fec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fec8.md) → [`0086ff08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086ff08.md) FUN_0086ff08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0086fe9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fe9c.md) [`00870200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870200.md) · 呼出先 7件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00550970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550970.md) [`0055097c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055097c.md) [`00597e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e88.md) [`00a86618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86618.md)
- 新版 呼出元 2件 [`0086fedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086fedc.md) [`00870240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870240.md) · 呼出先 7件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b0.md) [`005509bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509bc.md) [`00597ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec8.md) [`00a86810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a86/00a86810.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.44% / 新版 93.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086ff44",
      "incomplete_value": true,
      "site": "0086ff5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:875:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086ff04",
      "incomplete_value": true,
      "site": "0086ff1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:835:8"
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
      "definition_site": "0086ff44",
      "incomplete_value": true,
      "site": "0086ff60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:875:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086ff04",
      "incomplete_value": true,
      "site": "0086ff20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:835:8"
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
      "definition_site": "0086ffb8",
      "incomplete_value": true,
      "site": "0086ffc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:983:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086ff78",
      "incomplete_value": true,
      "site": "0086ff88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:943:8"
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
      "0086ff20",
      "PARAM",
      [
        "storage",
        "00cb4178",
        null,
        null
      ]
    ],
    [
      "0086ff44",
      "READ",
      [
        "storage",
        "002b7835",
        null,
        "string"
      ]
    ],
    [
      "0086ffb8",
      "READ",
      [
        "storage",
        "002bb943",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0086ff20",
      "PARAM",
      [
        "storage",
        "00cb4578",
        null,
        null
      ]
    ],
    [
      "0086ff44",
      "READ",
      [
        "storage",
        "002b7875",
        null,
        "string"
      ]
    ],
    [
      "0086ffb8",
      "READ",
      [
        "storage",
        "002bb983",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086fee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fec8.md#insn-0086fee0) · [`0086feec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fec8.md#insn-0086feec) · [`0086ff2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fec8.md#insn-0086ff2c)
- 新版 `0086ff20`（命令位置の公開資料なし） · `0086ff2c`（命令位置の公開資料なし） · `0086ff6c`（命令位置の公開資料なし）

~~~diff
- 0086fee0 ["COPY", "tmp:0:8", ["const:178:8"]]
- 0086fee0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0086fee0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0086fee0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0086ff20 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 0086ff20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0086ff20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0086ff20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0086fee0 bytes 00e00591
+ 0086ff20 bytes 00e01591
- 0086feec ["INT_ADD", "register:40f0:8", ["const:86feec:8", "const:4:8"]]
- 0086feec ["CALL", null, ["callee:00a86810:8"]]
+ 0086ff2c ["INT_ADD", "register:40f0:8", ["const:86ff2c:8", "const:4:8"]]
+ 0086ff2c ["CALL", null, ["callee:00a86810:8"]]
- 0086feec bytes cb590894
+ 0086ff2c bytes 395a0894
- 0086ff2c ["INT_ADD", "register:40f0:8", ["const:86ff2c:8", "const:4:8"]]
- 0086ff2c ["CALL", null, ["callee:005509b0:8"]]
+ 0086ff6c ["INT_ADD", "register:40f0:8", ["const:86ff6c:8", "const:4:8"]]
+ 0086ff6c ["CALL", null, ["callee:005509b0:8"]]
- 0086ff2c bytes 9182f397
+ 0086ff6c bytes 9182f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7546031d6ab1885e782802e1f632a4a6"></a>

### [`008701a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/008701a8.md) → [`008701e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008701e8.md) FUN_008701e8

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
      "definition_site": "00870208",
      "incomplete_value": false,
      "site": "0087020c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008701c8",
      "incomplete_value": false,
      "site": "008701cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
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
      "0087020c",
      "DATA",
      [
        "storage",
        "00c7f3c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087020c",
      "DATA",
      [
        "storage",
        "00c7f7c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008701bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/008701a8.md#insn-008701bc) · [`008701c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/008701a8.md#insn-008701c8)
- 新版 `008701fc`（命令位置の公開資料なし） · `00870208`（命令位置の公開資料なし）

~~~diff
- 008701bc ["INT_ADD", "register:40f0:8", ["const:8701bc:8", "const:4:8"]]
- 008701bc ["CALL", null, ["callee:00c57e90:8"]]
+ 008701fc ["INT_ADD", "register:40f0:8", ["const:8701fc:8", "const:4:8"]]
+ 008701fc ["CALL", null, ["callee:00c57e90:8"]]
- 008701bc bytes 359e0f94
+ 008701fc bytes 259f0f94
- 008701c8 ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 008701c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008701c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008701c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00870208 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 00870208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00870208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00870208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008701c8 bytes 08010f91
+ 00870208 bytes 08011f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91704bf895ad505e5aa62f3901e64e26"></a>

### [`008701e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/008701e0.md) → [`00870220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870220.md) FUN_00870220

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
      "definition_site": "00870224",
      "incomplete_value": false,
      "site": "00870228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008701e4",
      "incomplete_value": false,
      "site": "008701e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
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
      "00870228",
      "DATA",
      [
        "storage",
        "00c7f3c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00870228",
      "DATA",
      [
        "storage",
        "00c7f7c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008701e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/008701e0.md#insn-008701e4)
- 新版 `00870224`（命令位置の公開資料なし）

~~~diff
- 008701e4 ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 008701e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008701e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008701e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00870224 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 00870224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00870224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00870224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008701e4 bytes 08010f91
+ 00870224 bytes 08011f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9d41cea9fd9d269d2d5a8336b554d5d"></a>

### [`00870230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870230.md) → [`00870270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870270.md) FUN_00870270

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
      "definition_site": "00870290",
      "incomplete_value": false,
      "site": "00870294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870250",
      "incomplete_value": false,
      "site": "00870254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "00870294",
      "DATA",
      [
        "storage",
        "00c7f440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00870294",
      "DATA",
      [
        "storage",
        "00c7f840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00870244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870230.md#insn-00870244) · [`00870250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870230.md#insn-00870250)
- 新版 `00870284`（命令位置の公開資料なし） · `00870290`（命令位置の公開資料なし）

~~~diff
- 00870244 ["INT_ADD", "register:40f0:8", ["const:870244:8", "const:4:8"]]
- 00870244 ["CALL", null, ["callee:00c57e90:8"]]
+ 00870284 ["INT_ADD", "register:40f0:8", ["const:870284:8", "const:4:8"]]
+ 00870284 ["CALL", null, ["callee:00c57e90:8"]]
- 00870244 bytes 139e0f94
+ 00870284 bytes 039f0f94
- 00870250 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00870250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00870250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00870250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00870290 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00870290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00870290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00870290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00870250 bytes 08011191
+ 00870290 bytes 08012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbc0b03a20b57c020710221e6b452dca"></a>

### [`00870268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870268.md) → [`008702a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008702a8.md) FUN_008702a8

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
      "definition_site": "008702ac",
      "incomplete_value": false,
      "site": "008702b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087026c",
      "incomplete_value": false,
      "site": "00870270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "008702b0",
      "DATA",
      [
        "storage",
        "00c7f440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008702b0",
      "DATA",
      [
        "storage",
        "00c7f840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087026c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870268.md#insn-0087026c)
- 新版 `008702ac`（命令位置の公開資料なし）

~~~diff
- 0087026c ["COPY", "tmp:0:8", ["const:440:8"]]
- 0087026c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087026c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087026c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008702ac ["COPY", "tmp:0:8", ["const:840:8"]]
+ 008702ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008702ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008702ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087026c bytes 08011191
+ 008702ac bytes 08012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72d6064ebfc82bd74ac2949e4bca3752"></a>

### [`008702b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/008702b4.md) → [`008702f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008702f4.md) FUN_008702f4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00870288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870288.md) [`00870c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c3c.md) · 呼出先 16件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00550970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550970.md)
- 新版 呼出元 2件 [`008702c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008702c8.md) [`00870c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870c7c.md) · 呼出先 16件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`005509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.43% / 新版 93.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087033c",
      "incomplete_value": true,
      "site": "0087033c",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:ec9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008702fc",
      "incomplete_value": true,
      "site": "008702fc",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:e89:8"
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
      "definition_site": "00870340",
      "incomplete_value": true,
      "site": "00870340",
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
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870300",
      "incomplete_value": true,
      "site": "00870300",
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
                "const:7:8"
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
      "definition_site": "00870398",
      "incomplete_value": true,
      "site": "008703a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:54f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870358",
      "incomplete_value": true,
      "site": "00870364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:482:8"
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
      "00870324",
      "READ",
      [
        "storage",
        "002aee89",
        null,
        "string"
      ]
    ],
    [
      "00870328",
      "READ",
      [
        "storage",
        "002aee90",
        null,
        "string"
      ]
    ],
    [
      "00870398",
      "READ",
      [
        "storage",
        "0029f482",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00870324",
      "READ",
      [
        "storage",
        "002aeec9",
        null,
        "string"
      ]
    ],
    [
      "00870328",
      "READ",
      [
        "storage",
        "002aeed0",
        null,
        "string"
      ]
    ],
    [
      "00870398",
      "READ",
      [
        "storage",
        "0029f54f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008704d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/008702b4.md#insn-008704d0) · [`008702dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/008702b4.md#insn-008702dc) · [`0087030c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/008702b4.md#insn-0087030c)
- 新版 `00870510`（命令位置の公開資料なし） · `0087031c`（命令位置の公開資料なし） · `0087034c`（命令位置の公開資料なし）

~~~diff
- 008704d0 ["INT_ADD", "register:40f0:8", ["const:8704d0:8", "const:4:8"]]
- 008704d0 ["CALL", null, ["callee:00a38bbc:8"]]
+ 00870510 ["INT_ADD", "register:40f0:8", ["const:870510:8", "const:4:8"]]
+ 00870510 ["CALL", null, ["callee:00a38bbc:8"]]
- 008704d0 bytes 3d210794
+ 00870510 bytes ab210794
- 008702dc ["COPY", "tmp:0:8", ["const:e89:8"]]
- 008702dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008702dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008702dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087031c ["COPY", "tmp:0:8", ["const:ec9:8"]]
+ 0087031c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087031c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087031c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008702dc bytes 29253a91
+ 0087031c bytes 29253b91
- 0087030c ["INT_ADD", "register:40f0:8", ["const:87030c:8", "const:4:8"]]
- 0087030c ["CALL", null, ["callee:005509b0:8"]]
+ 0087034c ["INT_ADD", "register:40f0:8", ["const:87034c:8", "const:4:8"]]
+ 0087034c ["CALL", null, ["callee:005509b0:8"]]
- 0087030c bytes 9981f397
+ 0087034c bytes 9981f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-964b757b56a3eef7d3a1970205363786"></a>

### [`00870be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870be4.md) → [`00870c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870c24.md) FUN_00870c24

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
      "definition_site": "00870c44",
      "incomplete_value": false,
      "site": "00870c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870c04",
      "incomplete_value": false,
      "site": "00870c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
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
      "00870c48",
      "DATA",
      [
        "storage",
        "00c7f4c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00870c48",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00870bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870be4.md#insn-00870bf8) · [`00870c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870be4.md#insn-00870c04)
- 新版 `00870c38`（命令位置の公開資料なし） · `00870c44`（命令位置の公開資料なし）

~~~diff
- 00870bf8 ["INT_ADD", "register:40f0:8", ["const:870bf8:8", "const:4:8"]]
- 00870bf8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00870c38 ["INT_ADD", "register:40f0:8", ["const:870c38:8", "const:4:8"]]
+ 00870c38 ["CALL", null, ["callee:00c57e90:8"]]
- 00870bf8 bytes a69b0f94
+ 00870c38 bytes 969c0f94
- 00870c04 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00870c04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00870c04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00870c04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00870c44 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00870c44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00870c44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00870c44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00870c04 bytes 08011391
+ 00870c44 bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a86affbe81ba0d3d906482ba23f22d0d"></a>

### [`00870c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c1c.md) → [`00870c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870c5c.md) FUN_00870c5c

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
      "definition_site": "00870c60",
      "incomplete_value": false,
      "site": "00870c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870c20",
      "incomplete_value": false,
      "site": "00870c24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
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
      "00870c64",
      "DATA",
      [
        "storage",
        "00c7f4c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00870c64",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00870c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c1c.md#insn-00870c20)
- 新版 `00870c60`（命令位置の公開資料なし）

~~~diff
- 00870c20 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00870c20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00870c20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00870c20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00870c60 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00870c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00870c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00870c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00870c20 bytes 08011391
+ 00870c60 bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57c11fa452c6c95bd640c5b6d4156ca2"></a>

### [`00870c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c68.md) → [`00870ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870ca8.md) FUN_00870ca8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0085d4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085d/0085d4b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0085d4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085d/0085d4f4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00870cb4",
      "incomplete_value": false,
      "site": "00870cb8",
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
      "definition_site": "00870c74",
      "incomplete_value": false,
      "site": "00870c78",
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
      "00870cb4",
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
      "00870cb4",
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

- 旧版 [`00870c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c68.md#insn-00870c78) · [`00870c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c68.md#insn-00870c74)
- 新版 `00870cb8`（命令位置の公開資料なし） · `00870cb4`（命令位置の公開資料なし）

~~~diff
- 00870c78 ["INT_ADD", "register:40f0:8", ["const:870c78:8", "const:4:8"]]
- 00870c78 ["CALL", null, ["callee:0043b778:8"]]
+ 00870cb8 ["INT_ADD", "register:40f0:8", ["const:870cb8:8", "const:4:8"]]
+ 00870cb8 ["CALL", null, ["callee:0043b778:8"]]
- 00870c78 bytes b02aef97
+ 00870cb8 bytes b02aef97
- 00870c74 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00870c74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00870c74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00870c74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00870cb4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00870cb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00870cb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00870cb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00870c74 bytes 00303c91
+ 00870cb4 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a830bdbbd0dd6f931d47ed4c0861a837"></a>

### [`008718f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/008718f8.md) → [`00871938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871938.md) FUN_00871938

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
      "definition_site": "0087195c",
      "incomplete_value": false,
      "site": "0087195c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087191c",
      "incomplete_value": false,
      "site": "0087191c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      "0087195c",
      "DATA",
      [
        "storage",
        "00c7f540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087195c",
      "DATA",
      [
        "storage",
        "00c7f940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087190c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/008718f8.md#insn-0087190c) · [`00871918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/008718f8.md#insn-00871918)
- 新版 `0087194c`（命令位置の公開資料なし） · `00871958`（命令位置の公開資料なし）

~~~diff
- 0087190c ["INT_ADD", "register:40f0:8", ["const:87190c:8", "const:4:8"]]
- 0087190c ["CALL", null, ["callee:00c57e90:8"]]
+ 0087194c ["INT_ADD", "register:40f0:8", ["const:87194c:8", "const:4:8"]]
+ 0087194c ["CALL", null, ["callee:00c57e90:8"]]
- 0087190c bytes 61980f94
+ 0087194c bytes 51990f94
- 00871918 ["COPY", "tmp:0:8", ["const:540:8"]]
- 00871918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871958 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00871958 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871958 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871958 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871918 bytes 08011591
+ 00871958 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b000a8e403f945ffd3975bda1e260d4a"></a>

### [`0087192c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/0087192c.md) → [`0087196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/0087196c.md) FUN_0087196c

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
      "definition_site": "00871978",
      "incomplete_value": false,
      "site": "00871978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871938",
      "incomplete_value": false,
      "site": "00871938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      "00871978",
      "DATA",
      [
        "storage",
        "00c7f540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871978",
      "DATA",
      [
        "storage",
        "00c7f940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/0087192c.md#insn-00871934)
- 新版 `00871974`（命令位置の公開資料なし）

~~~diff
- 00871934 ["COPY", "tmp:0:8", ["const:540:8"]]
- 00871934 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871934 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871934 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871974 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00871974 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871974 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871974 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871934 bytes 29011591
+ 00871974 bytes 29012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b7796356a2d5d8438781e00771b611b"></a>

### [`00871948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871948.md) → [`00871988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871988.md) FUN_00871988

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0085d4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085d/0085d4b4.md) · 呼出先 10件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`00801c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801c04.md) [`00801c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801c50.md) [`008056ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/008056ac.md)
- 新版 呼出元 1件 [`0085d4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085d/0085d4f4.md) · 呼出先 10件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`00801c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801c44.md) [`00801c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801c90.md) [`008056ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/008056ec.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.85% / 新版 94.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00871a08",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008719c8",
      "value": [
        "leaf",
        "ram:a65bf4:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00871a38",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008719f8",
      "value": [
        "leaf",
        "ram:a65bf4:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00871a58",
      "value": [
        "leaf",
        "ram:806614:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00871a18",
      "value": [
        "leaf",
        "ram:8065d4:8"
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
      "00871a08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ],
    [
      "00871a38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ],
    [
      "00871a58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008065d4"
      ]
    ]
  ],
  "added": [
    [
      "00871a08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      "00871a38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      "00871a58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00806614"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008719c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871948.md#insn-008719c8) · [`008719f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871948.md#insn-008719f8) · [`00871a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871948.md#insn-00871a18)
- 新版 `00871a08`（命令位置の公開資料なし） · `00871a38`（命令位置の公開資料なし） · `00871a58`（命令位置の公開資料なし）

~~~diff
- 008719c8 ["INT_ADD", "register:40f0:8", ["const:8719c8:8", "const:4:8"]]
- 008719c8 ["CALL", null, ["ram:a65bf4:8"]]
+ 00871a08 ["INT_ADD", "register:40f0:8", ["const:871a08:8", "const:4:8"]]
+ 00871a08 ["CALL", null, ["ram:a65dec:8"]]
- 008719c8 bytes 8bd00794
+ 00871a08 bytes f9d00794
- 008719f8 ["INT_ADD", "register:40f0:8", ["const:8719f8:8", "const:4:8"]]
- 008719f8 ["CALL", null, ["ram:a65bf4:8"]]
+ 00871a38 ["INT_ADD", "register:40f0:8", ["const:871a38:8", "const:4:8"]]
+ 00871a38 ["CALL", null, ["ram:a65dec:8"]]
- 008719f8 bytes 7fd00794
+ 00871a38 bytes edd00794
- 00871a18 ["INT_ADD", "register:40f0:8", ["const:871a18:8", "const:4:8"]]
- 00871a18 ["CALL", null, ["ram:8065d4:8"]]
+ 00871a58 ["INT_ADD", "register:40f0:8", ["const:871a58:8", "const:4:8"]]
+ 00871a58 ["CALL", null, ["ram:806614:8"]]
- 00871a18 bytes ef52fe97
+ 00871a58 bytes ef52fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b9235896f3843c7a5a847c802e4e5f4"></a>

### [`00871afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871afc.md) → [`00871b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871b3c.md) FUN_00871b3c

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
      "definition_site": "00871b60",
      "incomplete_value": false,
      "site": "00871b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871b20",
      "incomplete_value": false,
      "site": "00871b20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
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
      "00871b60",
      "DATA",
      [
        "storage",
        "00c7f5d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871b60",
      "DATA",
      [
        "storage",
        "00c7f9d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871afc.md#insn-00871b10) · [`00871b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871afc.md#insn-00871b1c)
- 新版 `00871b50`（命令位置の公開資料なし） · `00871b5c`（命令位置の公開資料なし）

~~~diff
- 00871b10 ["INT_ADD", "register:40f0:8", ["const:871b10:8", "const:4:8"]]
- 00871b10 ["CALL", null, ["callee:00c57e90:8"]]
+ 00871b50 ["INT_ADD", "register:40f0:8", ["const:871b50:8", "const:4:8"]]
+ 00871b50 ["CALL", null, ["callee:00c57e90:8"]]
- 00871b10 bytes e0970f94
+ 00871b50 bytes d0980f94
- 00871b1c ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 00871b1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871b1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871b1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871b5c ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 00871b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871b1c bytes 08411791
+ 00871b5c bytes 08412791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3db5794abeb4f175a5a34010d944b3b4"></a>

### [`00871b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871b30.md) → [`00871b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871b70.md) FUN_00871b70

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
      "definition_site": "00871b7c",
      "incomplete_value": false,
      "site": "00871b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871b3c",
      "incomplete_value": false,
      "site": "00871b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
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
      "00871b7c",
      "DATA",
      [
        "storage",
        "00c7f5d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871b7c",
      "DATA",
      [
        "storage",
        "00c7f9d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871b30.md#insn-00871b38)
- 新版 `00871b78`（命令位置の公開資料なし）

~~~diff
- 00871b38 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 00871b38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871b38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871b38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871b78 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 00871b78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871b78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871b78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871b38 bytes 29411791
+ 00871b78 bytes 29412791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31265b048a181a8ce019b57a2986b26c"></a>

### [`00871e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871e88.md) → [`00871ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871ec8.md) FUN_00871ec8

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
      "definition_site": "00871ed0",
      "incomplete_value": false,
      "site": "00871ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871e90",
      "incomplete_value": false,
      "site": "00871e94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "00871ed4",
      "DATA",
      [
        "storage",
        "00c7f660",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871ed4",
      "DATA",
      [
        "storage",
        "00c7fa60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871e88.md#insn-00871e90)
- 新版 `00871ed0`（命令位置の公開資料なし）

~~~diff
- 00871e90 ["COPY", "tmp:0:8", ["const:660:8"]]
- 00871e90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871e90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871e90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871ed0 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 00871ed0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871ed0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871ed0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871e90 bytes 29811991
+ 00871ed0 bytes 29812991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e08bad81ef48d1e677dc454cb9e74fc"></a>

### [`00871ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871ea8.md) → [`00871ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871ee8.md) FUN_00871ee8

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
      "definition_site": "00871ef0",
      "incomplete_value": false,
      "site": "00871ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871eb0",
      "incomplete_value": false,
      "site": "00871eb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "00871ef4",
      "DATA",
      [
        "storage",
        "00c7f660",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871ef4",
      "DATA",
      [
        "storage",
        "00c7fa60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871ea8.md#insn-00871eb0) · [`00871ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871ea8.md#insn-00871ed4)
- 新版 `00871ef0`（命令位置の公開資料なし） · `00871f14`（命令位置の公開資料なし）

~~~diff
- 00871eb0 ["COPY", "tmp:0:8", ["const:660:8"]]
- 00871eb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871eb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871eb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871ef0 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 00871ef0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871ef0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871ef0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871eb0 bytes 29811991
+ 00871ef0 bytes 29812991
- 00871ed4 ["INT_ADD", "register:40f0:8", ["const:871ed4:8", "const:4:8"]]
- 00871ed4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00871f14 ["INT_ADD", "register:40f0:8", ["const:871f14:8", "const:4:8"]]
+ 00871f14 ["CALL", null, ["callee:00c57eb0:8"]]
- 00871ed4 bytes f7960f94
+ 00871f14 bytes e7970f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45b8b4549de51a7fad4d9617147e8b33"></a>

### [`00871ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871ee8.md) → [`00871f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871f28.md) FUN_00871f28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00871f54",
      "incomplete_value": false,
      "site": "00871f54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871f14",
      "incomplete_value": false,
      "site": "00871f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "00871f54",
      "DATA",
      [
        "storage",
        "00c7f660",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871f54",
      "DATA",
      [
        "storage",
        "00c7fa60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871ee8.md#insn-00871efc) · [`00871f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871ee8.md#insn-00871f0c) · [`00871f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871ee8.md#insn-00871f34)
- 新版 `00871f3c`（命令位置の公開資料なし） · `00871f4c`（命令位置の公開資料なし） · `00871f74`（命令位置の公開資料なし）

~~~diff
- 00871efc ["INT_ADD", "register:40f0:8", ["const:871efc:8", "const:4:8"]]
- 00871efc ["CALL", null, ["callee:00c57e90:8"]]
+ 00871f3c ["INT_ADD", "register:40f0:8", ["const:871f3c:8", "const:4:8"]]
+ 00871f3c ["CALL", null, ["callee:00c57e90:8"]]
- 00871efc bytes e5960f94
+ 00871f3c bytes d5970f94
- 00871f0c ["COPY", "tmp:0:8", ["const:660:8"]]
- 00871f0c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00871f0c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00871f0c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00871f4c ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 00871f4c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00871f4c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00871f4c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00871f0c bytes 4a811991
+ 00871f4c bytes 4a812991
- 00871f34 ["INT_ADD", "register:40f0:8", ["const:871f34:8", "const:4:8"]]
- 00871f34 ["CALL", null, ["callee:0043bb20:8"]]
+ 00871f74 ["INT_ADD", "register:40f0:8", ["const:871f74:8", "const:4:8"]]
+ 00871f74 ["CALL", null, ["callee:0043bb20:8"]]
- 00871f34 bytes eb26ef97
+ 00871f74 bytes eb26ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d434cb76312a8523ded6e2087a8b53a"></a>

### [`00871f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871f5c.md) → [`00871f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871f9c.md) FUN_00871f9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

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
      "definition_site": "00871fa4",
      "incomplete_value": false,
      "site": "00871fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871f64",
      "incomplete_value": false,
      "site": "00871f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "00871fa4",
      "DATA",
      [
        "storage",
        "00c7f660",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871fa4",
      "DATA",
      [
        "storage",
        "00c7fa60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871f5c.md#insn-00871f60)
- 新版 `00871fa0`（命令位置の公開資料なし）

~~~diff
- 00871f60 ["COPY", "tmp:0:8", ["const:660:8"]]
- 00871f60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871f60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871f60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871fa0 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 00871fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871f60 bytes 08811991
+ 00871fa0 bytes 08812991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d5cae77085ca31a83db8cc676fa41d6"></a>

### [`00871fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871fe0.md) → [`00872020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872020.md) FUN_00872020

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.94% / 新版 93.94%

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
      "site": "00872044",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00872004",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "site": "0087204c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087200c",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "00872044",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0087204c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "00872044",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0087204c",
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

- 旧版 [`00872004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871fe0.md#insn-00872004) · [`0087200c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871fe0.md#insn-0087200c) · [`00872008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871fe0.md#insn-00872008)
- 新版 `00872044`（命令位置の公開資料なし） · `0087204c`（命令位置の公開資料なし） · `00872048`（命令位置の公開資料なし）

~~~diff
- 00872004 ["INT_ADD", "register:40f0:8", ["const:872004:8", "const:4:8"]]
- 00872004 ["CALL", null, ["ram:48ccb8:8"]]
+ 00872044 ["INT_ADD", "register:40f0:8", ["const:872044:8", "const:4:8"]]
+ 00872044 ["CALL", null, ["ram:48ccf8:8"]]
- 00872004 bytes 2d6bf097
+ 00872044 bytes 2d6bf097
- 0087200c ["INT_ADD", "register:40f0:8", ["const:87200c:8", "const:4:8"]]
- 0087200c ["CALL", null, ["ram:48ccb8:8"]]
+ 0087204c ["INT_ADD", "register:40f0:8", ["const:87204c:8", "const:4:8"]]
+ 0087204c ["CALL", null, ["ram:48ccf8:8"]]
- 0087200c bytes 2b6bf097
+ 0087204c bytes 2b6bf097
- 00872008 ["INT_ADD", "register:40f0:8", ["const:872008:8", "const:4:8"]]
- 00872008 ["CALL", null, ["callee:0048e7e0:8"]]
+ 00872048 ["INT_ADD", "register:40f0:8", ["const:872048:8", "const:4:8"]]
+ 00872048 ["CALL", null, ["callee:0048e7e0:8"]]
- 00872008 bytes e671f097
+ 00872048 bytes e671f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-389915673ceb31de7101f72deca600ef"></a>

### [`008720b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008720b8.md) → [`008720f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008720f8.md) FUN_008720f8

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
      "definition_site": "00872100",
      "incomplete_value": true,
      "site": "00872104",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008720c0",
      "incomplete_value": true,
      "site": "008720c4",
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
            "const:6e0:8"
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
      "00872104",
      "DATA",
      [
        "storage",
        "00c7f6e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872104",
      "DATA",
      [
        "storage",
        "00c7fae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008720c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008720b8.md#insn-008720c0)
- 新版 `00872100`（命令位置の公開資料なし）

~~~diff
- 008720c0 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 008720c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008720c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008720c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00872100 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 00872100 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00872100 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00872100 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008720c0 bytes 29811b91
+ 00872100 bytes 29812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-683d6ab4877b962ae00d57f59db13db9"></a>

### [`008720d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008720d8.md) → [`00872118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872118.md) FUN_00872118

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
      "definition_site": "00872120",
      "incomplete_value": false,
      "site": "00872124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008720e0",
      "incomplete_value": false,
      "site": "008720e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "00872124",
      "DATA",
      [
        "storage",
        "00c7f6e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872124",
      "DATA",
      [
        "storage",
        "00c7fae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008720e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008720d8.md#insn-008720e0) · [`00872104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008720d8.md#insn-00872104)
- 新版 `00872120`（命令位置の公開資料なし） · `00872144`（命令位置の公開資料なし）

~~~diff
- 008720e0 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 008720e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008720e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008720e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00872120 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 00872120 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00872120 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00872120 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008720e0 bytes 29811b91
+ 00872120 bytes 29812b91
- 00872104 ["INT_ADD", "register:40f0:8", ["const:872104:8", "const:4:8"]]
- 00872104 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00872144 ["INT_ADD", "register:40f0:8", ["const:872144:8", "const:4:8"]]
+ 00872144 ["CALL", null, ["callee:00c57eb0:8"]]
- 00872104 bytes 6b960f94
+ 00872144 bytes 5b970f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d1a98186c0e7fc1cfcb972ff56822a3"></a>

### [`0087218c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/0087218c.md) → [`008721cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008721cc.md) FUN_008721cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

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
      "definition_site": "008721d4",
      "incomplete_value": false,
      "site": "008721d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872194",
      "incomplete_value": false,
      "site": "00872194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "008721d4",
      "DATA",
      [
        "storage",
        "00c7f6e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008721d4",
      "DATA",
      [
        "storage",
        "00c7fae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/0087218c.md#insn-00872190)
- 新版 `008721d0`（命令位置の公開資料なし）

~~~diff
- 00872190 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00872190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008721d0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 008721d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008721d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008721d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872190 bytes 08811b91
+ 008721d0 bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aac81d4f0c592fbc2c749c47303bec62"></a>

### [`00872210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872210.md) → [`00872250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872250.md) FUN_00872250

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.94% / 新版 93.94%

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
      "site": "00872274",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00872234",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "site": "0087227c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087223c",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "00872274",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0087227c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "00872274",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0087227c",
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

- 旧版 [`00872234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872210.md#insn-00872234) · [`0087223c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872210.md#insn-0087223c) · [`00872238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872210.md#insn-00872238)
- 新版 `00872274`（命令位置の公開資料なし） · `0087227c`（命令位置の公開資料なし） · `00872278`（命令位置の公開資料なし）

~~~diff
- 00872234 ["INT_ADD", "register:40f0:8", ["const:872234:8", "const:4:8"]]
- 00872234 ["CALL", null, ["ram:48ccb8:8"]]
+ 00872274 ["INT_ADD", "register:40f0:8", ["const:872274:8", "const:4:8"]]
+ 00872274 ["CALL", null, ["ram:48ccf8:8"]]
- 00872234 bytes a16af097
+ 00872274 bytes a16af097
- 0087223c ["INT_ADD", "register:40f0:8", ["const:87223c:8", "const:4:8"]]
- 0087223c ["CALL", null, ["ram:48ccb8:8"]]
+ 0087227c ["INT_ADD", "register:40f0:8", ["const:87227c:8", "const:4:8"]]
+ 0087227c ["CALL", null, ["ram:48ccf8:8"]]
- 0087223c bytes 9f6af097
+ 0087227c bytes 9f6af097
- 00872238 ["INT_ADD", "register:40f0:8", ["const:872238:8", "const:4:8"]]
- 00872238 ["CALL", null, ["callee:0048e7e0:8"]]
+ 00872278 ["INT_ADD", "register:40f0:8", ["const:872278:8", "const:4:8"]]
+ 00872278 ["CALL", null, ["callee:0048e7e0:8"]]
- 00872238 bytes 5a71f097
+ 00872278 bytes 5a71f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb14b2625753c4b71fb2bf3bb0bda169"></a>

### [`008722e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008722e8.md) → [`00872328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872328.md) FUN_00872328

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
      "definition_site": "0087232c",
      "incomplete_value": false,
      "site": "00872330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008722ec",
      "incomplete_value": false,
      "site": "008722f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "00872330",
      "DATA",
      [
        "storage",
        "00c7f778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00872330",
      "DATA",
      [
        "storage",
        "00c7fb78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008722ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008722e8.md#insn-008722ec)
- 新版 `0087232c`（命令位置の公開資料なし）

~~~diff
- 008722ec ["COPY", "tmp:0:8", ["const:778:8"]]
- 008722ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008722ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008722ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087232c ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 0087232c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087232c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087232c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008722ec bytes 08e11d91
+ 0087232c bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cffa9343c604f9b52149ccf67015289"></a>

### [`00872338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872338.md) → [`00872378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872378.md) FUN_00872378

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) · 呼出先 6件 [`004440a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004440a0.md) [`00444640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444640.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0085b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) · 呼出先 6件 [`004440e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/004440e0.md) [`00444680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444680.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.54% / 新版 95.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008723b8",
      "incomplete_value": false,
      "site": "008723b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872378",
      "incomplete_value": false,
      "site": "00872378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008723d0",
      "incomplete_value": false,
      "site": "008723d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ee000:8"
          ],
          [
            "leaf",
            "const:dcc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872390",
      "incomplete_value": false,
      "site": "00872398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ee000:8"
          ],
          [
            "leaf",
            "const:d8c:8"
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
      "008723b8",
      "DATA",
      [
        "storage",
        "00c7f7c8",
        null,
        "undefined *"
      ]
    ],
    [
      "008723d0",
      "PARAM",
      [
        "storage",
        "002eed8c",
        null,
        "string"
      ]
    ],
    [
      "00872430",
      "READ",
      [
        "storage",
        "002a7d2f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008723b8",
      "DATA",
      [
        "storage",
        "00c7fbc8",
        null,
        "undefined *"
      ]
    ],
    [
      "008723d0",
      "PARAM",
      [
        "storage",
        "002eedcc",
        null,
        "string"
      ]
    ],
    [
      "00872430",
      "READ",
      [
        "storage",
        "002a7e0b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872338.md#insn-00872398) · [`00872374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872338.md#insn-00872374) · [`00872390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872338.md#insn-00872390)
- 新版 `008723d8`（命令位置の公開資料なし） · `008723b4`（命令位置の公開資料なし） · `008723d0`（命令位置の公開資料なし）

~~~diff
- 00872398 ["INT_ADD", "register:40f0:8", ["const:872398:8", "const:4:8"]]
- 00872398 ["CALL", null, ["callee:00c58190:8"]]
+ 008723d8 ["INT_ADD", "register:40f0:8", ["const:8723d8:8", "const:4:8"]]
+ 008723d8 ["CALL", null, ["callee:00c58190:8"]]
- 00872398 bytes 7e960f94
+ 008723d8 bytes 6e970f94
- 00872374 ["COPY", "tmp:0:8", ["const:7c8:8"]]
- 00872374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008723b4 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 008723b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008723b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008723b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872374 bytes 08211f91
+ 008723b4 bytes 08212f91
- 00872390 ["COPY", "tmp:0:8", ["const:d8c:8"]]
- 00872390 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00872390 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00872390 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008723d0 ["COPY", "tmp:0:8", ["const:dcc:8"]]
+ 008723d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008723d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008723d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00872390 bytes 21303691
+ 008723d0 bytes 21303791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fda8a95012229b9fa76d647a5b8547f"></a>

### [`00872560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872560.md) → [`008725a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008725a0.md) FUN_008725a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008729ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729ac.md) · 呼出先 5件 [`00484780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md) [`00493958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493958.md) [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`008729ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008729ec.md) · 呼出先 5件 [`004847c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md) [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md) [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.45% / 新版 87.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00872604",
      "incomplete_value": false,
      "site": "0087260c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1121000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008725c4",
      "incomplete_value": false,
      "site": "008725cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1121000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "definition_site": "00872614",
      "incomplete_value": false,
      "site": "0087261c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1122000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008725d4",
      "incomplete_value": false,
      "site": "008725dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1122000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "definition_site": "0087263c",
      "incomplete_value": false,
      "site": "00872644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1121000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008725fc",
      "incomplete_value": false,
      "site": "00872604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1121000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "008725e0",
      "DATA",
      [
        "storage",
        "00c7f7c8",
        null,
        "undefined *"
      ]
    ],
    [
      "008725e8",
      "READ",
      [
        "storage",
        "00fe0478",
        null,
        "undefined1"
      ]
    ],
    [
      "008725f8",
      "READ",
      [
        "storage",
        "01070113",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008725e0",
      "DATA",
      [
        "storage",
        "00c7fbc8",
        null,
        "undefined *"
      ]
    ],
    [
      "008725e8",
      "READ",
      [
        "storage",
        "00fe0878",
        null,
        "undefined1"
      ]
    ],
    [
      "008725f8",
      "READ",
      [
        "storage",
        "01070513",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008725c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872560.md#insn-008725c4) · [`008725cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872560.md#insn-008725cc)
- 新版 `00872604`（命令位置の公開資料なし） · `0087260c`（命令位置の公開資料なし） · `008725cc`（命令位置の公開資料なし）

~~~diff
- 008725c4 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 008725c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008725c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008725c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00872604 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 00872604 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00872604 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00872604 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008725c4 bytes 00601391
+ 00872604 bytes 00602391
- 008725cc ["INT_ADD", "register:40f0:8", ["const:8725cc:8", "const:4:8"]]
- 008725cc ["CALL", null, ["callee:004847c0:8"]]
+ 0087260c ["INT_ADD", "register:40f0:8", ["const:87260c:8", "const:4:8"]]
+ 0087260c ["CALL", null, ["callee:004847c0:8"]]
- 008725cc bytes 6d48f097
+ 0087260c bytes 6d48f097
+ 008725cc ["COPY", "register:40a0:8", ["const:ca8000:8"]]
+ 008725cc bytes b42100d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59b669fee12e167ea4f6aef464b65f13"></a>

### [`008729d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729d0.md) → [`00872a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872a10.md) FUN_00872a10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 17件 [`004440a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004440a0.md) [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md)
- 新版 呼出元 0件  · 呼出先 17件 [`004440e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/004440e0.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.06% / 新版 86.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_destination` 9件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00872c88",
      "incomplete_value": false,
      "site": "00872c88",
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
    "old": {
      "definition_site": "00872c48",
      "incomplete_value": false,
      "site": "00872c48",
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
                "const:b00:8"
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
    "ordinal": 24,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00872c8c",
      "incomplete_value": false,
      "site": "00872c8c",
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
    "old": {
      "definition_site": "00872c4c",
      "incomplete_value": false,
      "site": "00872c4c",
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
            "const:b00:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00872c88",
      "incomplete_value": false,
      "site": "00872c8c",
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
    "old": {
      "definition_site": "00872c48",
      "incomplete_value": false,
      "site": "00872c4c",
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
                "const:b00:8"
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
      "00872a48",
      "PARAM",
      [
        "storage",
        "00ca7d70",
        null,
        null
      ]
    ],
    [
      "00872abc",
      "READ",
      [
        "storage",
        "002a7d3f",
        null,
        "string"
      ]
    ],
    [
      "00872ac0",
      "READ",
      [
        "storage",
        "00c9a890",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00872a48",
      "PARAM",
      [
        "storage",
        "00ca8170",
        null,
        null
      ]
    ],
    [
      "00872abc",
      "READ",
      [
        "storage",
        "002a7e1b",
        null,
        "string"
      ]
    ],
    [
      "00872ac0",
      "READ",
      [
        "storage",
        "00c9ac90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729d0.md#insn-00872a0c) · [`00872a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729d0.md#insn-00872a4c) · [`00872afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729d0.md#insn-00872afc)
- 新版 `00872a4c`（命令位置の公開資料なし） · `00872a8c`（命令位置の公開資料なし） · `00872b3c`（命令位置の公開資料なし）

~~~diff
- 00872a0c ["INT_ADD", "register:40f0:8", ["const:872a0c:8", "const:4:8"]]
- 00872a0c ["CALL", null, ["callee:009ccb7c:8"]]
+ 00872a4c ["INT_ADD", "register:40f0:8", ["const:872a4c:8", "const:4:8"]]
+ 00872a4c ["CALL", null, ["callee:009ccb7c:8"]]
- 00872a0c bytes f5670594
+ 00872a4c bytes 4c680594
- 00872a4c ["COPY", "tmp:0:8", ["const:d70:8"]]
- 00872a4c ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00872a4c ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00872a4c ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00872a8c ["COPY", "tmp:0:8", ["const:170:8"]]
+ 00872a8c ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00872a8c ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00872a8c ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00872a4c bytes 39c33591
+ 00872a8c bytes 39c30591
- 00872afc ["INT_ADD", "register:40f0:8", ["const:872afc:8", "const:4:8"]]
- 00872afc ["CALL", null, ["callee:0048ce54:8"]]
+ 00872b3c ["INT_ADD", "register:40f0:8", ["const:872b3c:8", "const:4:8"]]
+ 00872b3c ["CALL", null, ["callee:0048ce54:8"]]
- 00872afc bytes c668f097
+ 00872b3c bytes c668f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d607edc39b8d05bf845b02b04b76708"></a>

### [`00873008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873008.md) → [`00873048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873048.md) FUN_00873048

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087304c",
      "incomplete_value": true,
      "site": "00873050",
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
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087300c",
      "incomplete_value": true,
      "site": "00873010",
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
      "00873050",
      "DATA",
      [
        "storage",
        "00c7f810",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00873050",
      "DATA",
      [
        "storage",
        "00c7fc10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873008.md#insn-0087300c)
- 新版 `0087304c`（命令位置の公開資料なし）

~~~diff
- 0087300c ["COPY", "tmp:0:8", ["const:810:8"]]
- 0087300c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087300c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087300c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087304c ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0087304c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087304c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087304c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087300c bytes 08412091
+ 0087304c bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7232e2f9e07cb3967378d7af7b9b3550"></a>

### [`00873018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873018.md) → [`00873058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873058.md) FUN_00873058

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
      "definition_site": "00873068",
      "incomplete_value": false,
      "site": "00873070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873028",
      "incomplete_value": false,
      "site": "00873030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      "00873070",
      "DATA",
      [
        "storage",
        "00c7f810",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00873070",
      "DATA",
      [
        "storage",
        "00c7fc10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873018.md#insn-00873028) · [`00873034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873018.md#insn-00873034)
- 新版 `00873068`（命令位置の公開資料なし） · `00873074`（命令位置の公開資料なし）

~~~diff
- 00873028 ["COPY", "tmp:0:8", ["const:810:8"]]
- 00873028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873068 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 00873068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873028 bytes 08412091
+ 00873068 bytes 08413091
- 00873034 ["INT_ADD", "register:40f0:8", ["const:873034:8", "const:4:8"]]
- 00873034 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00873074 ["INT_ADD", "register:40f0:8", ["const:873074:8", "const:4:8"]]
+ 00873074 ["CALL", null, ["callee:00c57ea0:8"]]
- 00873034 bytes 9b920f94
+ 00873074 bytes 8b930f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52f6ec77795d6487243326bc7fec14bd"></a>

### [`00873058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873058.md) → [`00873098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873098.md) FUN_00873098

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) [`008766b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008766b4.md) · 呼出先 12件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00597e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 2件 [`0085b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) [`008766f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766f4.md) · 呼出先 12件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00597ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008730dc",
      "incomplete_value": false,
      "site": "008730dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087309c",
      "incomplete_value": false,
      "site": "0087309c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "definition_site": "00873144",
      "incomplete_value": true,
      "site": "00873144",
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
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:99a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873104",
      "incomplete_value": true,
      "site": "00873104",
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
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:95a:8"
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
      "definition_site": "008730fc",
      "incomplete_value": false,
      "site": "00873104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ee000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008730bc",
      "incomplete_value": false,
      "site": "008730c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ee000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "008730dc",
      "DATA",
      [
        "storage",
        "00c7f860",
        null,
        "undefined *"
      ]
    ],
    [
      "008730fc",
      "PARAM",
      [
        "storage",
        "002eedf0",
        null,
        "string"
      ]
    ],
    [
      "00873110",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008730dc",
      "DATA",
      [
        "storage",
        "00c7fc60",
        null,
        "undefined *"
      ]
    ],
    [
      "008730fc",
      "PARAM",
      [
        "storage",
        "002eee30",
        null,
        "string"
      ]
    ],
    [
      "00873110",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008730c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873058.md#insn-008730c4) · [`00873140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873058.md#insn-00873140) · [`00873318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873058.md#insn-00873318)
- 新版 `00873104`（命令位置の公開資料なし） · `00873180`（命令位置の公開資料なし） · `00873358`（命令位置の公開資料なし）

~~~diff
- 008730c4 ["INT_ADD", "register:40f0:8", ["const:8730c4:8", "const:4:8"]]
- 008730c4 ["CALL", null, ["callee:00c58190:8"]]
+ 00873104 ["INT_ADD", "register:40f0:8", ["const:873104:8", "const:4:8"]]
+ 00873104 ["CALL", null, ["callee:00c58190:8"]]
- 008730c4 bytes 33930f94
+ 00873104 bytes 23940f94
- 00873140 ["INT_ADD", "register:40f0:8", ["const:873140:8", "const:4:8"]]
- 00873140 ["CALL", null, ["callee:0047e60c:8"]]
+ 00873180 ["INT_ADD", "register:40f0:8", ["const:873180:8", "const:4:8"]]
+ 00873180 ["CALL", null, ["callee:0047e60c:8"]]
- 00873140 bytes 232df097
+ 00873180 bytes 232df097
- 00873318 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 00873318 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00873318 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00873318 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00873358 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00873358 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00873358 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00873358 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00873318 bytes 00e02c91
+ 00873358 bytes 00e03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-841cc1b2eb55e0c8696451353bcc39b3"></a>

### [`00873454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873454.md) → [`00873494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873494.md) FUN_00873494

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008734ac",
      "incomplete_value": false,
      "site": "008734b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087346c",
      "incomplete_value": false,
      "site": "00873470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "008734b0",
      "DATA",
      [
        "storage",
        "00c7f860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008734b0",
      "DATA",
      [
        "storage",
        "00c7fc60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087346c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873454.md#insn-0087346c) · [`0087347c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873454.md#insn-0087347c) · [`00873490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873454.md#insn-00873490)
- 新版 `008734ac`（命令位置の公開資料なし） · `008734bc`（命令位置の公開資料なし） · `008734d0`（命令位置の公開資料なし）

~~~diff
- 0087346c ["COPY", "tmp:0:8", ["const:860:8"]]
- 0087346c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087346c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087346c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008734ac ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 008734ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008734ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008734ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087346c bytes 29812191
+ 008734ac bytes 29813191
- 0087347c ["INT_ADD", "register:40f0:8", ["const:87347c:8", "const:4:8"]]
- 0087347c ["CALL", null, ["callee:00c57eb0:8"]]
+ 008734bc ["INT_ADD", "register:40f0:8", ["const:8734bc:8", "const:4:8"]]
+ 008734bc ["CALL", null, ["callee:00c57eb0:8"]]
- 0087347c bytes 8d910f94
+ 008734bc bytes 7d920f94
- 00873490 ["INT_ADD", "register:40f0:8", ["const:873490:8", "const:4:8"]]
- 00873490 ["CALL", null, ["callee:00c53d00:8"]]
+ 008734d0 ["INT_ADD", "register:40f0:8", ["const:8734d0:8", "const:4:8"]]
+ 008734d0 ["CALL", null, ["callee:00c53d00:8"]]
- 00873490 bytes 14810f94
+ 008734d0 bytes 0c820f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-074733b8c23c2c992f0419f683929da4"></a>

### [`00873500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873500.md) → [`00873540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873540.md) FUN_00873540

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00873558",
      "incomplete_value": false,
      "site": "0087355c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873518",
      "incomplete_value": false,
      "site": "0087351c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "0087355c",
      "DATA",
      [
        "storage",
        "00c7f860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087355c",
      "DATA",
      [
        "storage",
        "00c7fc60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873500.md#insn-00873518) · [`00873528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873500.md#insn-00873528) · [`0087353c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873500.md#insn-0087353c)
- 新版 `00873558`（命令位置の公開資料なし） · `00873568`（命令位置の公開資料なし） · `0087357c`（命令位置の公開資料なし）

~~~diff
- 00873518 ["COPY", "tmp:0:8", ["const:860:8"]]
- 00873518 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00873518 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00873518 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00873558 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 00873558 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00873558 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00873558 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00873518 bytes 29812191
+ 00873558 bytes 29813191
- 00873528 ["INT_ADD", "register:40f0:8", ["const:873528:8", "const:4:8"]]
- 00873528 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00873568 ["INT_ADD", "register:40f0:8", ["const:873568:8", "const:4:8"]]
+ 00873568 ["CALL", null, ["callee:00c57eb0:8"]]
- 00873528 bytes 62910f94
+ 00873568 bytes 52920f94
- 0087353c ["INT_ADD", "register:40f0:8", ["const:87353c:8", "const:4:8"]]
- 0087353c ["CALL", null, ["callee:00c53d00:8"]]
+ 0087357c ["INT_ADD", "register:40f0:8", ["const:87357c:8", "const:4:8"]]
+ 0087357c ["CALL", null, ["callee:00c53d00:8"]]
- 0087353c bytes e9800f94
+ 0087357c bytes e1810f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2c9d6aa4e8c7fdda6cb35483e46e077"></a>

### [`0087359c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md) → [`008735dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md) FUN_008735dc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00560ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ac8.md) [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md)
- 新版 呼出元 0件  · 呼出先 17件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00560b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b08.md) [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.02% / 新版 96.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00873604",
      "value": [
        "leaf",
        "ram:7683d8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008735c4",
      "value": [
        "leaf",
        "ram:768398:8"
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
      "site": "0087377c",
      "value": [
        "leaf",
        "ram:7685a4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087373c",
      "value": [
        "leaf",
        "ram:768564:8"
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00873798",
      "value": [
        "leaf",
        "ram:764ee0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00873758",
      "value": [
        "leaf",
        "ram:764ea0:8"
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
      "00873604",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768398"
      ]
    ],
    [
      "00873620",
      "DATA",
      [
        "storage",
        "003c79f8",
        null,
        "byte[15]"
      ]
    ],
    [
      "00873630",
      "READ",
      [
        "storage",
        "002b4b6a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00873604",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683d8"
      ]
    ],
    [
      "00873620",
      "DATA",
      [
        "storage",
        "003c79f8",
        null,
        "qword"
      ]
    ],
    [
      "00873630",
      "READ",
      [
        "storage",
        "002b4baa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008735c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md#insn-008735c4) · [`0087373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md#insn-0087373c) · [`00873758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md#insn-00873758)
- 新版 `00873604`（命令位置の公開資料なし） · `0087377c`（命令位置の公開資料なし） · `00873798`（命令位置の公開資料なし）

~~~diff
- 008735c4 ["INT_ADD", "register:40f0:8", ["const:8735c4:8", "const:4:8"]]
- 008735c4 ["CALL", null, ["ram:768398:8"]]
+ 00873604 ["INT_ADD", "register:40f0:8", ["const:873604:8", "const:4:8"]]
+ 00873604 ["CALL", null, ["ram:7683d8:8"]]
- 008735c4 bytes 75d3fb97
+ 00873604 bytes 75d3fb97
- 0087373c ["INT_ADD", "register:40f0:8", ["const:87373c:8", "const:4:8"]]
- 0087373c ["CALL", null, ["ram:768564:8"]]
+ 0087377c ["INT_ADD", "register:40f0:8", ["const:87377c:8", "const:4:8"]]
+ 0087377c ["CALL", null, ["ram:7685a4:8"]]
- 0087373c bytes 8ad3fb97
+ 0087377c bytes 8ad3fb97
- 00873758 ["INT_ADD", "register:40f0:8", ["const:873758:8", "const:4:8"]]
- 00873758 ["CALL", null, ["ram:764ea0:8"]]
+ 00873798 ["INT_ADD", "register:40f0:8", ["const:873798:8", "const:4:8"]]
+ 00873798 ["CALL", null, ["ram:764ee0:8"]]
- 00873758 bytes d2c5fb97
+ 00873798 bytes d2c5fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97fccd6df8bb35adea9a8494b0ceab25"></a>

### [`00873a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873a68.md) → [`00873aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873aa8.md) FUN_00873aa8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0087359c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md) [`00874a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874a94.md) · 呼出先 9件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`0044f908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md) [`00874538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874538.md) [`00874588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874588.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 2件 [`008735dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md) [`00874ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ad4.md) · 呼出先 9件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`0044f948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f948.md) [`00874578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874578.md) [`008745c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008745c8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.06% / 新版 95.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00873b10",
      "incomplete_value": false,
      "site": "00873b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873ad0",
      "incomplete_value": false,
      "site": "00873ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "definition_site": "00873b30",
      "incomplete_value": false,
      "site": "00873b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873af0",
      "incomplete_value": false,
      "site": "00873af0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "00873b10",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873b30",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873b70",
      "READ",
      [
        "storage",
        "00c7f8e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00873b10",
      "DATA",
      [
        "storage",
        "00c7fcc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873b30",
      "DATA",
      [
        "storage",
        "00c7fcc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873b70",
      "READ",
      [
        "storage",
        "00c7fce0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873a68.md#insn-00873a94) · [`00873ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873a68.md#insn-00873ab8) · [`00873ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873a68.md#insn-00873ac0)
- 新版 `00873ad4`（命令位置の公開資料なし） · `00873af8`（命令位置の公開資料なし） · `00873b00`（命令位置の公開資料なし）

~~~diff
- 00873a94 ["INT_ADD", "register:40f0:8", ["const:873a94:8", "const:4:8"]]
- 00873a94 ["CALL", null, ["callee:0044f8e0:8"]]
+ 00873ad4 ["INT_ADD", "register:40f0:8", ["const:873ad4:8", "const:4:8"]]
+ 00873ad4 ["CALL", null, ["callee:0044f8e0:8"]]
- 00873a94 bytes 836fef97
+ 00873ad4 bytes 836fef97
- 00873ab8 ["INT_ADD", "register:40f0:8", ["const:873ab8:8", "const:4:8"]]
- 00873ab8 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00873af8 ["INT_ADD", "register:40f0:8", ["const:873af8:8", "const:4:8"]]
+ 00873af8 ["CALL", null, ["callee:00c53cd0:8"]]
- 00873ab8 bytes 7e7f0f94
+ 00873af8 bytes 76800f94
- 00873ac0 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00873ac0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873ac0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873ac0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873b00 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 00873b00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873b00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873b00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873ac0 bytes 08012391
+ 00873b00 bytes 08013391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a362e39042fb04befbe010821a328c0d"></a>

### [`00873c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873c10.md) → [`00873c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873c50.md) FUN_00873c50

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0087359c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md) [`008746a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008746a8.md) · 呼出先 7件 [`00874c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874c68.md) [`00874cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874cb8.md) [`00880668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 2件 [`008735dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md) [`008746e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md) · 呼出先 7件 [`00874ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ca8.md) [`00874cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874cf8.md) [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00873cb0",
      "incomplete_value": false,
      "site": "00873cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873c70",
      "incomplete_value": false,
      "site": "00873c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "definition_site": "00873cd0",
      "incomplete_value": false,
      "site": "00873cd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873c90",
      "incomplete_value": false,
      "site": "00873c90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "00873cb0",
      "DATA",
      [
        "storage",
        "00c7f9c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873cd0",
      "DATA",
      [
        "storage",
        "00c7f9c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873d14",
      "READ",
      [
        "storage",
        "00c7f9e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00873cb0",
      "DATA",
      [
        "storage",
        "00c7fdc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873cd0",
      "DATA",
      [
        "storage",
        "00c7fdc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873d14",
      "READ",
      [
        "storage",
        "00c7fde0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873c10.md#insn-00873c58) · [`00873c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873c10.md#insn-00873c60) · [`00873c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873c10.md#insn-00873c78)
- 新版 `00873c98`（命令位置の公開資料なし） · `00873ca0`（命令位置の公開資料なし） · `00873cb8`（命令位置の公開資料なし）

~~~diff
- 00873c58 ["INT_ADD", "register:40f0:8", ["const:873c58:8", "const:4:8"]]
- 00873c58 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00873c98 ["INT_ADD", "register:40f0:8", ["const:873c98:8", "const:4:8"]]
+ 00873c98 ["CALL", null, ["callee:00c53cd0:8"]]
- 00873c58 bytes 167f0f94
+ 00873c98 bytes 0e800f94
- 00873c60 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00873c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873ca0 ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 00873ca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873ca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873ca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873c60 bytes 08012791
+ 00873ca0 bytes 08013791
- 00873c78 ["INT_ADD", "register:40f0:8", ["const:873c78:8", "const:4:8"]]
- 00873c78 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00873cb8 ["INT_ADD", "register:40f0:8", ["const:873cb8:8", "const:4:8"]]
+ 00873cb8 ["CALL", null, ["callee:00c53cd0:8"]]
- 00873c78 bytes 0e7f0f94
+ 00873cb8 bytes 06800f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dde085bf7b0dfafcf394f41fa7f60923"></a>

### [`00873d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873d88.md) → [`00873dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873dc8.md) FUN_00873dc8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087359c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md) · 呼出先 7件 [`008750a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008750a0.md) [`008750f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008750f0.md) [`00880cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`008735dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md) · 呼出先 7件 [`008750e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008750e0.md) [`00875130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875130.md) [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00873e28",
      "incomplete_value": false,
      "site": "00873e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873de8",
      "incomplete_value": false,
      "site": "00873de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      "definition_site": "00873e48",
      "incomplete_value": false,
      "site": "00873e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873e08",
      "incomplete_value": false,
      "site": "00873e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      "00873e28",
      "DATA",
      [
        "storage",
        "00c7fa40",
        null,
        "undefined *"
      ]
    ],
    [
      "00873e48",
      "DATA",
      [
        "storage",
        "00c7fa40",
        null,
        "undefined *"
      ]
    ],
    [
      "00873e8c",
      "READ",
      [
        "storage",
        "00c7fa60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00873e28",
      "DATA",
      [
        "storage",
        "00c7fe40",
        null,
        "undefined *"
      ]
    ],
    [
      "00873e48",
      "DATA",
      [
        "storage",
        "00c7fe40",
        null,
        "undefined *"
      ]
    ],
    [
      "00873e8c",
      "READ",
      [
        "storage",
        "00c7fe60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873d88.md#insn-00873dd0) · [`00873dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873d88.md#insn-00873dd8) · [`00873df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873d88.md#insn-00873df0)
- 新版 `00873e10`（命令位置の公開資料なし） · `00873e18`（命令位置の公開資料なし） · `00873e30`（命令位置の公開資料なし）

~~~diff
- 00873dd0 ["INT_ADD", "register:40f0:8", ["const:873dd0:8", "const:4:8"]]
- 00873dd0 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00873e10 ["INT_ADD", "register:40f0:8", ["const:873e10:8", "const:4:8"]]
+ 00873e10 ["CALL", null, ["callee:00c53cd0:8"]]
- 00873dd0 bytes b87e0f94
+ 00873e10 bytes b07f0f94
- 00873dd8 ["COPY", "tmp:0:8", ["const:a40:8"]]
- 00873dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873e18 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 00873e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873dd8 bytes 08012991
+ 00873e18 bytes 08013991
- 00873df0 ["INT_ADD", "register:40f0:8", ["const:873df0:8", "const:4:8"]]
- 00873df0 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00873e30 ["INT_ADD", "register:40f0:8", ["const:873e30:8", "const:4:8"]]
+ 00873e30 ["CALL", null, ["callee:00c53cd0:8"]]
- 00873df0 bytes b07e0f94
+ 00873e30 bytes a87f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bb6a345f1c0d9f86d4a390fb2bc335f"></a>

### [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) → [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) FUN_00873f40

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0087359c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md) [`00874d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874d3c.md) [`00875174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875174.md) [`00876018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876018.md) · 呼出先 16件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`00453c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453c70.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`0087539c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087539c.md)
- 新版 呼出元 4件 [`008735dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md) [`00874d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874d7c.md) [`008751b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008751b4.md) [`00876058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876058.md) · 呼出先 16件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00453cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`008753dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008753dc.md)

変更の種類 call, call_target, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.05% / 新版 89.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00873f9c",
      "incomplete_value": true,
      "site": "00873f9c",
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
                "const:e27:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873f5c",
      "incomplete_value": true,
      "site": "00873f5c",
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
                "const:d4b:8"
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
      "definition_site": "00873fa4",
      "incomplete_value": true,
      "site": "00873fa4",
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
      "definition_site": "00873f64",
      "incomplete_value": true,
      "site": "00873f64",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00873fe8",
      "incomplete_value": true,
      "site": "00873ff8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:668:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873fa8",
      "incomplete_value": true,
      "site": "00873fb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:59b:8"
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
      "00873f90",
      "READ",
      [
        "storage",
        "002a7d4b",
        null,
        "string"
      ]
    ],
    [
      "00873f94",
      "READ",
      [
        "storage",
        "002a7d50",
        null,
        "string"
      ]
    ],
    [
      "00873fe8",
      "READ",
      [
        "storage",
        "002a359b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00873f90",
      "READ",
      [
        "storage",
        "002a7e27",
        null,
        "string"
      ]
    ],
    [
      "00873f94",
      "READ",
      [
        "storage",
        "002a7e2c",
        null,
        "string"
      ]
    ],
    [
      "00873fe8",
      "READ",
      [
        "storage",
        "002a3668",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008740a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md#insn-008740a0) · [`008740b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md#insn-008740b0) · [`008740bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md#insn-008740bc)
- 新版 `008740e0`（命令位置の公開資料なし） · `008740f0`（命令位置の公開資料なし） · `008740fc`（命令位置の公開資料なし）

~~~diff
- 008740a0 ["INT_ADD", "register:40f0:8", ["const:8740a0:8", "const:4:8"]]
- 008740a0 ["CALL", null, ["callee:0044f8e0:8"]]
+ 008740e0 ["INT_ADD", "register:40f0:8", ["const:8740e0:8", "const:4:8"]]
+ 008740e0 ["CALL", null, ["callee:0044f8e0:8"]]
- 008740a0 bytes 006eef97
+ 008740e0 bytes 006eef97
- 008740b0 ["INT_ADD", "register:40f0:8", ["const:8740b0:8", "const:4:8"]]
- 008740b0 ["CALL", null, ["ram:764344:8"]]
+ 008740f0 ["INT_ADD", "register:40f0:8", ["const:8740f0:8", "const:4:8"]]
+ 008740f0 ["CALL", null, ["ram:764384:8"]]
- 008740b0 bytes a5c0fb97
+ 008740f0 bytes a5c0fb97
- 008740bc ["INT_ADD", "register:40f0:8", ["const:8740bc:8", "const:4:8"]]
- 008740bc ["CALL", null, ["ram:764ea0:8"]]
+ 008740fc ["INT_ADD", "register:40f0:8", ["const:8740fc:8", "const:4:8"]]
+ 008740fc ["CALL", null, ["ram:764ee0:8"]]
- 008740bc bytes 79c3fb97
+ 008740fc bytes 79c3fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a40eaf3dfcd59b593267c63f02ce7021"></a>

### [`008743ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008743ec.md) → [`0087442c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087442c.md) FUN_0087442c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "00874440",
      "incomplete_value": false,
      "site": "00874444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874400",
      "incomplete_value": false,
      "site": "00874404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "00874444",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874444",
      "DATA",
      [
        "storage",
        "00c7fcc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008743ec.md#insn-00874400) · [`00874414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008743ec.md#insn-00874414) · [`00874434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008743ec.md#insn-00874434)
- 新版 `00874440`（命令位置の公開資料なし） · `00874454`（命令位置の公開資料なし） · `00874474`（命令位置の公開資料なし）

~~~diff
- 00874400 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00874400 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874400 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874400 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874440 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 00874440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874400 bytes 08012391
+ 00874440 bytes 08013391
- 00874414 ["INT_ADD", "register:40f0:8", ["const:874414:8", "const:4:8"]]
- 00874414 ["CALL", null, ["callee:00c53d00:8"]]
+ 00874454 ["INT_ADD", "register:40f0:8", ["const:874454:8", "const:4:8"]]
+ 00874454 ["CALL", null, ["callee:00c53d00:8"]]
- 00874414 bytes 337d0f94
+ 00874454 bytes 2b7e0f94
- 00874434 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874434 ["INT_ADD", "register:40f0:8", ["const:874434:8", "const:4:8"]]
- 00874434 ["CALLIND", null, ["register:0:8"]]
+ 00874474 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874474 ["INT_ADD", "register:40f0:8", ["const:874474:8", "const:4:8"]]
+ 00874474 ["CALLIND", null, ["register:0:8"]]
- 00874434 bytes 00013fd6
+ 00874474 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bfc9c56d6fe3ddebb01ad5a39c4e887"></a>

### [`00874448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874448.md) → [`00874488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874488.md) FUN_00874488

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "008744a0",
      "incomplete_value": false,
      "site": "008744a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874460",
      "incomplete_value": false,
      "site": "00874464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "008744a4",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008744a4",
      "DATA",
      [
        "storage",
        "00c7fcc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874448.md#insn-00874460) · [`00874474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874448.md#insn-00874474) · [`00874488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874448.md#insn-00874488)
- 新版 `008744a0`（命令位置の公開資料なし） · `008744b4`（命令位置の公開資料なし） · `008744c8`（命令位置の公開資料なし）

~~~diff
- 00874460 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00874460 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874460 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874460 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008744a0 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 008744a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008744a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008744a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874460 bytes 08012391
+ 008744a0 bytes 08013391
- 00874474 ["INT_ADD", "register:40f0:8", ["const:874474:8", "const:4:8"]]
- 00874474 ["CALL", null, ["callee:00c53d00:8"]]
+ 008744b4 ["INT_ADD", "register:40f0:8", ["const:8744b4:8", "const:4:8"]]
+ 008744b4 ["CALL", null, ["callee:00c53d00:8"]]
- 00874474 bytes 1b7d0f94
+ 008744b4 bytes 137e0f94
- 00874488 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874488 ["INT_ADD", "register:40f0:8", ["const:874488:8", "const:4:8"]]
- 00874488 ["CALLIND", null, ["register:0:8"]]
+ 008744c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008744c8 ["INT_ADD", "register:40f0:8", ["const:8744c8:8", "const:4:8"]]
+ 008744c8 ["CALLIND", null, ["register:0:8"]]
- 00874488 bytes 00013fd6
+ 008744c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

