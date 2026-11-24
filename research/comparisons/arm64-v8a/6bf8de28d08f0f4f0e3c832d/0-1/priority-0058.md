# v16.0.0 → v16.0.1 · 最優先の変更候補 (58)

[一覧の目次](README.md)

<a id="compare-916178224958cbe569f9391f11b6071f"></a>

### [`009ee7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ee/009ee7d4.md) → [`009ee970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee970.md) FUN_009ee970

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009eeb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ee/009eeb14.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`009f2c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2c48.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`009eecb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009eecb0.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009f2de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2de4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "009ee9c8",
      "incomplete_value": true,
      "site": "009ee9c8",
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
                "const:3fb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ee82c",
      "incomplete_value": true,
      "site": "009ee82c",
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
                "const:32e:8"
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
      "009ee9a0",
      "READ",
      [
        "storage",
        "002aa32e",
        null,
        "string"
      ]
    ],
    [
      "009ee9e4",
      "READ",
      [
        "storage",
        "002b55a8",
        null,
        "string"
      ]
    ],
    [
      "009ee9e4",
      "READ",
      [
        "storage",
        "002b55b8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ee9a0",
      "READ",
      [
        "storage",
        "002aa3fb",
        null,
        "string"
      ]
    ],
    [
      "009ee9e4",
      "READ",
      [
        "storage",
        "002b55e8",
        null,
        "string"
      ]
    ],
    [
      "009ee9e4",
      "READ",
      [
        "storage",
        "002b55f8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ee7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ee/009ee7d4.md#insn-009ee7fc) · [`009ee838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ee/009ee7d4.md#insn-009ee838) · [`009ee840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ee/009ee7d4.md#insn-009ee840)
- 新版 [`009ee998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee970.md#insn-009ee998) · [`009ee9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee970.md#insn-009ee9d4) · [`009ee9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee970.md#insn-009ee9dc)

~~~diff
- 009ee7fc ["COPY", "tmp:0:8", ["const:32e:8"]]
- 009ee7fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009ee7fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009ee7fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009ee998 ["COPY", "tmp:0:8", ["const:3fb:8"]]
+ 009ee998 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009ee998 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009ee998 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009ee7fc bytes 4ab90c91
+ 009ee998 bytes 4aed0f91
- 009ee838 ["INT_ADD", "register:40f0:8", ["const:9ee838:8", "const:4:8"]]
- 009ee838 ["CALL", null, ["callee:00c57e90:8"]]
+ 009ee9d4 ["INT_ADD", "register:40f0:8", ["const:9ee9d4:8", "const:4:8"]]
+ 009ee9d4 ["CALL", null, ["callee:00c57e90:8"]]
- 009ee838 bytes 96a40994
+ 009ee9d4 bytes 2fa50994
- 009ee840 ["COPY", "tmp:0:8", ["const:568:8"]]
- 009ee840 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ee840 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ee840 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ee9dc ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 009ee9dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ee9dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ee9dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ee840 bytes 08a11591
+ 009ee9dc bytes 08a11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cc6508354f55bfea794d1331d266bfa"></a>

### [`009eee88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ee/009eee88.md) → [`009ef024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef024.md) FUN_009ef024

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ef/009ef744.md) · 呼出先 20件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`004883f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004883f4.md)
- 新版 呼出元 1件 [`009ef8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef8e0.md) · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md)

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
      "definition_site": "009ef068",
      "incomplete_value": false,
      "site": "009ef06c",
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
    "old": {
      "definition_site": "009eeecc",
      "incomplete_value": false,
      "site": "009eeed0",
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
            "const:938:8"
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
      "definition_site": "009ef084",
      "incomplete_value": true,
      "site": "009ef094",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:408:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eeee8",
      "incomplete_value": true,
      "site": "009eeef8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:33b:8"
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
      "definition_site": "009ef088",
      "incomplete_value": true,
      "site": "009ef098",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "009eeeec",
      "incomplete_value": true,
      "site": "009eeefc",
      "value": [
        "LOAD",
        "16",
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
      "009ef06c",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "009ef084",
      "READ",
      [
        "storage",
        "002aa33b",
        null,
        "string"
      ]
    ],
    [
      "009ef088",
      "READ",
      [
        "storage",
        "002aa347",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ef06c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "009ef084",
      "READ",
      [
        "storage",
        "002aa408",
        null,
        "string"
      ]
    ],
    [
      "009ef088",
      "READ",
      [
        "storage",
        "002aa414",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ef32c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ee/009eee88.md#insn-009ef32c) · [`009ef344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ee/009eee88.md#insn-009ef344) · [`009eeec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ee/009eee88.md#insn-009eeec4)
- 新版 [`009ef4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef024.md#insn-009ef4c8) · [`009ef4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef024.md#insn-009ef4e0) · [`009ef060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef024.md#insn-009ef060)

~~~diff
- 009ef32c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7c0:8"]]
- 009ef32c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 009ef4c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bc0:8"]]
+ 009ef4c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 009ef32c bytes 08e143f9
+ 009ef4c8 bytes 08e145f9
- 009ef344 ["INT_ADD", "register:40f0:8", ["const:9ef344:8", "const:4:8"]]
- 009ef344 ["CALL", null, ["callee:00c57eb0:8"]]
+ 009ef4e0 ["INT_ADD", "register:40f0:8", ["const:9ef4e0:8", "const:4:8"]]
+ 009ef4e0 ["CALL", null, ["callee:00c57eb0:8"]]
- 009ef344 bytes dba10994
+ 009ef4e0 bytes 74a20994
- 009eeec4 ["INT_ADD", "register:40f0:8", ["const:9eeec4:8", "const:4:8"]]
- 009eeec4 ["CALL", null, ["callee:00487e20:8"]]
+ 009ef060 ["INT_ADD", "register:40f0:8", ["const:9ef060:8", "const:4:8"]]
+ 009ef060 ["CALL", null, ["callee:00487e20:8"]]
- 009eeec4 bytes c763ea97
+ 009ef060 bytes 7063ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-845507a48b8037f0d62cab22371b03c7"></a>

### [`009ef4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ef/009ef4d0.md) → [`009ef66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef66c.md) FUN_009ef66c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009f2468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2468.md) · 呼出先 2件 [`009f3748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3748.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`009f2604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2604.md) · 呼出先 2件 [`009f38e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f38e4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "009ef6b8",
      "incomplete_value": false,
      "site": "009ef6bc",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ef51c",
      "incomplete_value": false,
      "site": "009ef520",
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
            "const:a58:8"
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
      "009ef6bc",
      "DATA",
      [
        "storage",
        "00c89a58",
        null,
        "undefined *"
      ]
    ],
    [
      "009ef78c",
      "DATA",
      [
        "storage",
        "00c89fb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ef6bc",
      "DATA",
      [
        "storage",
        "00c89e58",
        null,
        "undefined *"
      ]
    ],
    [
      "009ef78c",
      "DATA",
      [
        "storage",
        "00c8a3b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ef51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ef/009ef4d0.md#insn-009ef51c) · [`009ef5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ef/009ef4d0.md#insn-009ef5d0) · [`009ef5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ef/009ef4d0.md#insn-009ef5dc)
- 新版 [`009ef6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef66c.md#insn-009ef6b8) · [`009ef76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef66c.md#insn-009ef76c) · [`009ef778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef66c.md#insn-009ef778)

~~~diff
- 009ef51c ["COPY", "tmp:0:8", ["const:a58:8"]]
- 009ef51c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ef51c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ef51c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ef6b8 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 009ef6b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ef6b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ef6b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ef51c bytes 08612991
+ 009ef6b8 bytes 08613991
- 009ef5d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 009ef5d0 ["INT_ADD", "register:40f0:8", ["const:9ef5d0:8", "const:4:8"]]
- 009ef5d0 ["CALLIND", null, ["register:0:8"]]
+ 009ef76c ["COPY", "register:0:8", ["register:4048:8"]]
+ 009ef76c ["INT_ADD", "register:40f0:8", ["const:9ef76c:8", "const:4:8"]]
+ 009ef76c ["CALLIND", null, ["register:0:8"]]
- 009ef5d0 bytes 20013fd6
+ 009ef76c bytes 20013fd6
- 009ef5dc ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009ef778 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009ef5dc bytes c81400d0
+ 009ef778 bytes c81400f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4f25992ec1d5e3ceaf945517eb74396"></a>

### [`009efc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ef/009efc4c.md) → [`009efde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md) FUN_009efde8

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009f0370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f0/009f0370.md) [`009f0b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f0/009f0b98.md) · 呼出先 9件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`009f391c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f391c.md) [`009f3930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3930.md)
- 新版 呼出元 2件 [`009f050c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md) [`009f0d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md) · 呼出先 9件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009f3ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3ab8.md) [`009f3acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3acc.md)

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
      "definition_site": "009f01c4",
      "incomplete_value": true,
      "site": "009f01cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "009f0028",
      "incomplete_value": true,
      "site": "009f0030",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:200:8"
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
      "definition_site": "009f01c0",
      "incomplete_value": true,
      "site": "009f01d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:df3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f0024",
      "incomplete_value": true,
      "site": "009f0034",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d17:8"
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
      "definition_site": "009f01c0",
      "incomplete_value": true,
      "site": "009f01d0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "009f0024",
      "incomplete_value": true,
      "site": "009f0034",
      "value": [
        "LOAD",
        "16",
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
      "009f01c0",
      "READ",
      [
        "storage",
        "002a5d17",
        null,
        "string"
      ]
    ],
    [
      "009f01c0",
      "READ",
      [
        "storage",
        "002a5d27",
        null,
        "string"
      ]
    ],
    [
      "009f01c4",
      "READ",
      [
        "storage",
        "002c2200",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009f01c0",
      "READ",
      [
        "storage",
        "002a5df3",
        null,
        "string"
      ]
    ],
    [
      "009f01c0",
      "READ",
      [
        "storage",
        "002a5e03",
        null,
        "string"
      ]
    ],
    [
      "009f01c4",
      "READ",
      [
        "storage",
        "002c2240",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009effe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ef/009efc4c.md#insn-009effe0) · [`009efdfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ef/009efc4c.md#insn-009efdfc) · [`009efe34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ef/009efc4c.md#insn-009efe34)
- 新版 [`009f017c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md#insn-009f017c) · [`009eff98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md#insn-009eff98) · [`009effd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md#insn-009effd0)

~~~diff
- 009effe0 ["INT_ADD", "register:40f0:8", ["const:9effe0:8", "const:4:8"]]
- 009effe0 ["CALL", null, ["callee:009f3acc:8"]]
+ 009f017c ["INT_ADD", "register:40f0:8", ["const:9f017c:8", "const:4:8"]]
+ 009f017c ["CALL", null, ["callee:009f3acc:8"]]
- 009effe0 bytes 540e0094
+ 009f017c bytes 540e0094
- 009efdfc ["INT_ADD", "register:40f0:8", ["const:9efdfc:8", "const:4:8"]]
- 009efdfc ["CALL", null, ["callee:00c57e90:8"]]
+ 009eff98 ["INT_ADD", "register:40f0:8", ["const:9eff98:8", "const:4:8"]]
+ 009eff98 ["CALL", null, ["callee:00c57e90:8"]]
- 009efdfc bytes 259f0994
+ 009eff98 bytes be9f0994
- 009efe34 ["INT_ADD", "register:40f0:8", ["const:9efe34:8", "const:4:8"]]
- 009efe34 ["CALL", null, ["callee:00c58000:8"]]
+ 009effd0 ["INT_ADD", "register:40f0:8", ["const:9effd0:8", "const:4:8"]]
+ 009effd0 ["CALL", null, ["callee:00c58000:8"]]
- 009efe34 bytes 739f0994
+ 009effd0 bytes 0ca00994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f81a23b781966c8db81e5c3419b437a"></a>

### [`009f0370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f0/009f0370.md) → [`009f050c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md) FUN_009f050c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009f2308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2308.md) · 呼出先 11件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`009efc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ef/009efc4c.md) [`009f391c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f391c.md)
- 新版 呼出元 1件 [`009f24a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f24a4.md) · 呼出先 11件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`009efde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md) [`009f3ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3ab8.md)

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
      "definition_site": "009f05f8",
      "incomplete_value": false,
      "site": "009f0608",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f045c",
      "incomplete_value": false,
      "site": "009f046c",
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
            "const:ab8:8"
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
      "definition_site": "009f0600",
      "incomplete_value": false,
      "site": "009f0608",
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
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f0464",
      "incomplete_value": false,
      "site": "009f046c",
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
            "const:b10:8"
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
      "definition_site": "009f066c",
      "incomplete_value": false,
      "site": "009f067c",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f04d0",
      "incomplete_value": false,
      "site": "009f04e0",
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
            "const:ab8:8"
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
      "009f05f8",
      "PARAM",
      [
        "storage",
        "00c89ab8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f0600",
      "PARAM",
      [
        "storage",
        "00c89b10",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f066c",
      "PARAM",
      [
        "storage",
        "00c89ab8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f05f8",
      "PARAM",
      [
        "storage",
        "00c89eb8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f0600",
      "PARAM",
      [
        "storage",
        "00c89f10",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f066c",
      "PARAM",
      [
        "storage",
        "00c89eb8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f046c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f0/009f0370.md#insn-009f046c) · [`009f04e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f0/009f0370.md#insn-009f04e0) · [`009f03bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f0/009f0370.md#insn-009f03bc)
- 新版 [`009f0608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md#insn-009f0608) · [`009f067c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md#insn-009f067c) · [`009f0558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md#insn-009f0558)

~~~diff
- 009f046c ["INT_ADD", "register:40f0:8", ["const:9f046c:8", "const:4:8"]]
- 009f046c ["CALL", null, ["callee:00c58610:8"]]
+ 009f0608 ["INT_ADD", "register:40f0:8", ["const:9f0608:8", "const:4:8"]]
+ 009f0608 ["CALL", null, ["callee:00c58610:8"]]
- 009f046c bytes 699f0994
+ 009f0608 bytes 02a00994
- 009f04e0 ["INT_ADD", "register:40f0:8", ["const:9f04e0:8", "const:4:8"]]
- 009f04e0 ["CALL", null, ["callee:00c58610:8"]]
+ 009f067c ["INT_ADD", "register:40f0:8", ["const:9f067c:8", "const:4:8"]]
+ 009f067c ["CALL", null, ["callee:00c58610:8"]]
- 009f04e0 bytes 4c9f0994
+ 009f067c bytes e59f0994
- 009f03bc ["INT_ADD", "register:40f0:8", ["const:9f03bc:8", "const:4:8"]]
- 009f03bc ["CALL", null, ["callee:009efde8:8"]]
+ 009f0558 ["INT_ADD", "register:40f0:8", ["const:9f0558:8", "const:4:8"]]
+ 009f0558 ["CALL", null, ["callee:009efde8:8"]]
- 009f03bc bytes 24feff97
+ 009f0558 bytes 24feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f52a350e57883635795f48254f325af"></a>

### [`009f0b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f0/009f0b98.md) → [`009f0d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md) FUN_009f0d34

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`009efc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ef/009efc4c.md) [`009f0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f0/009f0eac.md) [`009f3660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3660.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009efde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md) [`009f1048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1048.md) [`009f37fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37fc.md)

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
      "definition_site": "009f0df4",
      "incomplete_value": true,
      "site": "009f0e04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f0c58",
      "incomplete_value": true,
      "site": "009f0c68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:80:8"
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
      "definition_site": "009f0df8",
      "incomplete_value": true,
      "site": "009f0e14",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1e6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f0c5c",
      "incomplete_value": true,
      "site": "009f0c78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1a6:8"
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
      "definition_site": "009f0df8",
      "incomplete_value": true,
      "site": "009f0e14",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "009f0c5c",
      "incomplete_value": true,
      "site": "009f0c78",
      "value": [
        "LOAD",
        "16",
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
      "009f0df4",
      "READ",
      [
        "storage",
        "002c2080",
        null,
        null
      ]
    ],
    [
      "009f0df8",
      "READ",
      [
        "storage",
        "002b31a6",
        null,
        "string"
      ]
    ],
    [
      "009f0df8",
      "READ",
      [
        "storage",
        "002b31b6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009f0df4",
      "READ",
      [
        "storage",
        "002c20c0",
        null,
        null
      ]
    ],
    [
      "009f0df8",
      "READ",
      [
        "storage",
        "002b31e6",
        null,
        "string"
      ]
    ],
    [
      "009f0df8",
      "READ",
      [
        "storage",
        "002b31f6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f0bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f0/009f0b98.md#insn-009f0bf0) · [`009f0c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f0/009f0b98.md#insn-009f0c48) · [`009f0c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f0/009f0b98.md#insn-009f0c54)
- 新版 [`009f0d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md#insn-009f0d8c) · [`009f0de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md#insn-009f0de4) · [`009f0df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md#insn-009f0df0)

~~~diff
- 009f0bf0 ["INT_ADD", "register:40f0:8", ["const:9f0bf0:8", "const:4:8"]]
- 009f0bf0 ["CALL", null, ["callee:009f3f34:8"]]
+ 009f0d8c ["INT_ADD", "register:40f0:8", ["const:9f0d8c:8", "const:4:8"]]
+ 009f0d8c ["CALL", null, ["callee:009f3f34:8"]]
- 009f0bf0 bytes 6a0c0094
+ 009f0d8c bytes 6a0c0094
- 009f0c48 ["INT_ADD", "register:40f0:8", ["const:9f0c48:8", "const:4:8"]]
- 009f0c48 ["CALL", null, ["callee:00c57e90:8"]]
+ 009f0de4 ["INT_ADD", "register:40f0:8", ["const:9f0de4:8", "const:4:8"]]
+ 009f0de4 ["CALL", null, ["callee:00c57e90:8"]]
- 009f0c48 bytes 929b0994
+ 009f0de4 bytes 2b9c0994
- 009f0c54 ["COPY", "tmp:0:8", ["const:1a6:8"]]
- 009f0c54 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009f0c54 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009f0c54 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009f0df0 ["COPY", "tmp:0:8", ["const:1e6:8"]]
+ 009f0df0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009f0df0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009f0df0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009f0c54 bytes 4a990691
+ 009f0df0 bytes 4a990791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca1feff505b735eabdc9005b0ffa8005"></a>

### [`009f17dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f1/009f17dc.md) → [`009f1978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1978.md) FUN_009f1978

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`009f3460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3460.md) [`009f36f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f36f8.md) [`009f3d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3d98.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009f35fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f35fc.md) [`009f3894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3894.md) [`009f3f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3f34.md)

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
      "definition_site": "009f1a3c",
      "incomplete_value": true,
      "site": "009f1a4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f18a0",
      "incomplete_value": true,
      "site": "009f18b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:80:8"
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
      "definition_site": "009f1a40",
      "incomplete_value": true,
      "site": "009f1a5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1e6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f18a4",
      "incomplete_value": true,
      "site": "009f18c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1a6:8"
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
      "definition_site": "009f1a40",
      "incomplete_value": true,
      "site": "009f1a5c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "009f18a4",
      "incomplete_value": true,
      "site": "009f18c0",
      "value": [
        "LOAD",
        "16",
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
      "009f1a3c",
      "READ",
      [
        "storage",
        "002c2080",
        null,
        null
      ]
    ],
    [
      "009f1a40",
      "READ",
      [
        "storage",
        "002b31a6",
        null,
        "string"
      ]
    ],
    [
      "009f1a40",
      "READ",
      [
        "storage",
        "002b31b6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009f1a3c",
      "READ",
      [
        "storage",
        "002c20c0",
        null,
        null
      ]
    ],
    [
      "009f1a40",
      "READ",
      [
        "storage",
        "002b31e6",
        null,
        "string"
      ]
    ],
    [
      "009f1a40",
      "READ",
      [
        "storage",
        "002b31f6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f1a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f1/009f17dc.md#insn-009f1a60) · [`009f1838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f1/009f17dc.md#insn-009f1838) · [`009f1890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f1/009f17dc.md#insn-009f1890)
- 新版 [`009f1bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1978.md#insn-009f1bfc) · [`009f19d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1978.md#insn-009f19d4) · [`009f1a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1978.md#insn-009f1a2c)

~~~diff
- 009f1a60 ["INT_ADD", "register:40f0:8", ["const:9f1a60:8", "const:4:8"]]
- 009f1a60 ["CALL", null, ["callee:00c57eb0:8"]]
+ 009f1bfc ["INT_ADD", "register:40f0:8", ["const:9f1bfc:8", "const:4:8"]]
+ 009f1bfc ["CALL", null, ["callee:00c57eb0:8"]]
- 009f1a60 bytes 14980994
+ 009f1bfc bytes ad980994
- 009f1838 ["INT_ADD", "register:40f0:8", ["const:9f1838:8", "const:4:8"]]
- 009f1838 ["CALL", null, ["callee:009f3f34:8"]]
+ 009f19d4 ["INT_ADD", "register:40f0:8", ["const:9f19d4:8", "const:4:8"]]
+ 009f19d4 ["CALL", null, ["callee:009f3f34:8"]]
- 009f1838 bytes 58090094
+ 009f19d4 bytes 58090094
- 009f1890 ["INT_ADD", "register:40f0:8", ["const:9f1890:8", "const:4:8"]]
- 009f1890 ["CALL", null, ["callee:00c57e90:8"]]
+ 009f1a2c ["INT_ADD", "register:40f0:8", ["const:9f1a2c:8", "const:4:8"]]
+ 009f1a2c ["CALL", null, ["callee:00c57e90:8"]]
- 009f1890 bytes 80980994
+ 009f1a2c bytes 19990994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d9d8f34d46a920b8867f6e96628ff31"></a>

### [`009f1cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f1/009f1cb0.md) → [`009f1e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md) FUN_009f1e4c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`009f3460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3460.md) [`009f35c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f35c8.md) [`009f3660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3660.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009f35fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f35fc.md) [`009f3764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3764.md) [`009f37fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37fc.md)

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
      "definition_site": "009f1f14",
      "incomplete_value": true,
      "site": "009f1f24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f1d78",
      "incomplete_value": true,
      "site": "009f1d88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:80:8"
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
      "definition_site": "009f1f18",
      "incomplete_value": true,
      "site": "009f1f34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1e6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f1d7c",
      "incomplete_value": true,
      "site": "009f1d98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1a6:8"
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
      "definition_site": "009f1f18",
      "incomplete_value": true,
      "site": "009f1f34",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "009f1d7c",
      "incomplete_value": true,
      "site": "009f1d98",
      "value": [
        "LOAD",
        "16",
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
      "009f1f14",
      "READ",
      [
        "storage",
        "002c2080",
        null,
        null
      ]
    ],
    [
      "009f1f18",
      "READ",
      [
        "storage",
        "002b31a6",
        null,
        "string"
      ]
    ],
    [
      "009f1f18",
      "READ",
      [
        "storage",
        "002b31b6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009f1f14",
      "READ",
      [
        "storage",
        "002c20c0",
        null,
        null
      ]
    ],
    [
      "009f1f18",
      "READ",
      [
        "storage",
        "002b31e6",
        null,
        "string"
      ]
    ],
    [
      "009f1f18",
      "READ",
      [
        "storage",
        "002b31f6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f1d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f1/009f1cb0.md#insn-009f1d10) · [`009f1d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f1/009f1cb0.md#insn-009f1d68) · [`009f1d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f1/009f1cb0.md#insn-009f1d74)
- 新版 [`009f1eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md#insn-009f1eac) · [`009f1f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md#insn-009f1f04) · [`009f1f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md#insn-009f1f10)

~~~diff
- 009f1d10 ["INT_ADD", "register:40f0:8", ["const:9f1d10:8", "const:4:8"]]
- 009f1d10 ["CALL", null, ["callee:009f3f34:8"]]
+ 009f1eac ["INT_ADD", "register:40f0:8", ["const:9f1eac:8", "const:4:8"]]
+ 009f1eac ["CALL", null, ["callee:009f3f34:8"]]
- 009f1d10 bytes 22080094
+ 009f1eac bytes 22080094
- 009f1d68 ["INT_ADD", "register:40f0:8", ["const:9f1d68:8", "const:4:8"]]
- 009f1d68 ["CALL", null, ["callee:00c57e90:8"]]
+ 009f1f04 ["INT_ADD", "register:40f0:8", ["const:9f1f04:8", "const:4:8"]]
+ 009f1f04 ["CALL", null, ["callee:00c57e90:8"]]
- 009f1d68 bytes 4a970994
+ 009f1f04 bytes e3970994
- 009f1d74 ["COPY", "tmp:0:8", ["const:1a6:8"]]
- 009f1d74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009f1d74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009f1d74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009f1f10 ["COPY", "tmp:0:8", ["const:1e6:8"]]
+ 009f1f10 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009f1f10 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009f1f10 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009f1d74 bytes 4a990691
+ 009f1f10 bytes 4a990791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e446741ca7bed6d95ea912b991e60afa"></a>

### [`009f2468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2468.md) → [`009f2604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2604.md) FUN_009f2604

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009e0038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0038.md) · 呼出先 2件 [`009ef4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ef/009ef4d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`009e01d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e01d4.md) · 呼出先 2件 [`009ef66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef66c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "009f262c",
      "incomplete_value": false,
      "site": "009f2638",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2490",
      "incomplete_value": false,
      "site": "009f249c",
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
            "const:30:8"
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
      "009f2638",
      "DATA",
      [
        "storage",
        "00c8a030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f2638",
      "DATA",
      [
        "storage",
        "00c8a430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2468.md#insn-009f2484) · [`009f2490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2468.md#insn-009f2490) · [`009f24a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2468.md#insn-009f24a8)
- 新版 [`009f2620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2604.md#insn-009f2620) · [`009f262c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2604.md#insn-009f262c) · [`009f2644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2604.md#insn-009f2644)

~~~diff
- 009f2484 ["INT_ADD", "register:40f0:8", ["const:9f2484:8", "const:4:8"]]
- 009f2484 ["CALL", null, ["callee:00c57e90:8"]]
+ 009f2620 ["INT_ADD", "register:40f0:8", ["const:9f2620:8", "const:4:8"]]
+ 009f2620 ["CALL", null, ["callee:00c57e90:8"]]
- 009f2484 bytes 83950994
+ 009f2620 bytes 1c960994
- 009f2490 ["COPY", "tmp:0:8", ["const:30:8"]]
- 009f2490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f262c ["COPY", "tmp:0:8", ["const:430:8"]]
+ 009f262c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f262c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f262c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2490 bytes 08c10091
+ 009f262c bytes 08c11091
- 009f24a8 ["INT_ADD", "register:40f0:8", ["const:9f24a8:8", "const:4:8"]]
- 009f24a8 ["CALL", null, ["callee:009ef66c:8"]]
+ 009f2644 ["INT_ADD", "register:40f0:8", ["const:9f2644:8", "const:4:8"]]
+ 009f2644 ["CALL", null, ["callee:009ef66c:8"]]
- 009f24a8 bytes 0af4ff97
+ 009f2644 bytes 0af4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c71ded8f8000bba5d5af134ce5bd92a"></a>

### [`009f2510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2510.md) → [`009f26ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f26ac.md) FUN_009f26ac

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "009f26c8",
      "incomplete_value": false,
      "site": "009f26cc",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f252c",
      "incomplete_value": false,
      "site": "009f2530",
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
            "const:bb0:8"
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
      "009f26cc",
      "DATA",
      [
        "storage",
        "00c89bb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f26cc",
      "DATA",
      [
        "storage",
        "00c89fb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f252c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2510.md#insn-009f252c) · [`009f2568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2510.md#insn-009f2568) · [`009f257c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2510.md#insn-009f257c)
- 新版 [`009f26c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f26ac.md#insn-009f26c8) · [`009f2704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f26ac.md#insn-009f2704) · [`009f2718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f26ac.md#insn-009f2718)

~~~diff
- 009f252c ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 009f252c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f252c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f252c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f26c8 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 009f26c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f26c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f26c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f252c bytes 08c12e91
+ 009f26c8 bytes 08c13e91
- 009f2568 ["INT_ADD", "register:40f0:8", ["const:9f2568:8", "const:4:8"]]
- 009f2568 ["CALL", null, ["callee:00c53d00:8"]]
+ 009f2704 ["INT_ADD", "register:40f0:8", ["const:9f2704:8", "const:4:8"]]
+ 009f2704 ["CALL", null, ["callee:00c53d00:8"]]
- 009f2568 bytes de840994
+ 009f2704 bytes 7f850994
- 009f257c ["COPY", "register:0:8", ["register:4040:8"]]
- 009f257c ["INT_ADD", "register:40f0:8", ["const:9f257c:8", "const:4:8"]]
- 009f257c ["CALLIND", null, ["register:0:8"]]
+ 009f2718 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f2718 ["INT_ADD", "register:40f0:8", ["const:9f2718:8", "const:4:8"]]
+ 009f2718 ["CALLIND", null, ["register:0:8"]]
- 009f257c bytes 00013fd6
+ 009f2718 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0e7cc3962d25c8a249065e234720343"></a>

### [`009f2878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2878.md) → [`009f2a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2a14.md) FUN_009f2a14

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009f282c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f282c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009f29c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f29c8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "009f2a30",
      "incomplete_value": false,
      "site": "009f2a34",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2894",
      "incomplete_value": false,
      "site": "009f2898",
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
            "const:bb0:8"
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
      "009f2a34",
      "DATA",
      [
        "storage",
        "00c89bb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f2a34",
      "DATA",
      [
        "storage",
        "00c89fb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2878.md#insn-009f2894) · [`009f28d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2878.md#insn-009f28d0) · [`009f28e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2878.md#insn-009f28e4)
- 新版 [`009f2a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2a14.md#insn-009f2a30) · [`009f2a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2a14.md#insn-009f2a6c) · [`009f2a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2a14.md#insn-009f2a80)

~~~diff
- 009f2894 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 009f2894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f2a30 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 009f2a30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2a30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2a30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2894 bytes 08c12e91
+ 009f2a30 bytes 08c13e91
- 009f28d0 ["INT_ADD", "register:40f0:8", ["const:9f28d0:8", "const:4:8"]]
- 009f28d0 ["CALL", null, ["callee:00c53d00:8"]]
+ 009f2a6c ["INT_ADD", "register:40f0:8", ["const:9f2a6c:8", "const:4:8"]]
+ 009f2a6c ["CALL", null, ["callee:00c53d00:8"]]
- 009f28d0 bytes 04840994
+ 009f2a6c bytes a5840994
- 009f28e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f28e4 ["INT_ADD", "register:40f0:8", ["const:9f28e4:8", "const:4:8"]]
- 009f28e4 ["CALLIND", null, ["register:0:8"]]
+ 009f2a80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f2a80 ["INT_ADD", "register:40f0:8", ["const:9f2a80:8", "const:4:8"]]
+ 009f2a80 ["CALLIND", null, ["register:0:8"]]
- 009f28e4 bytes 00013fd6
+ 009f2a80 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aa4639fc8580ffc0ebbfc18cbe207f2"></a>

### [`009f2c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2c48.md) → [`009f2de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2de4.md) FUN_009f2de4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`009ed9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ed/009ed9a0.md) [`009ee7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ee/009ee7d4.md) [`009f2980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2980.md) [`009f4408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4408.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 4件 [`009edb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009edb3c.md) [`009ee970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee970.md) [`009f2b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2b1c.md) [`009f45a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f45a4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "009f2df0",
      "incomplete_value": false,
      "site": "009f2df4",
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
      "definition_site": "009f2c54",
      "incomplete_value": false,
      "site": "009f2c58",
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
      "009f2df0",
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
      "009f2df0",
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

- 旧版 [`009f2c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2c48.md#insn-009f2c58) · [`009f2c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2c48.md#insn-009f2c54)
- 新版 [`009f2df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2de4.md#insn-009f2df4) · [`009f2df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2de4.md#insn-009f2df0)

~~~diff
- 009f2c58 ["INT_ADD", "register:40f0:8", ["const:9f2c58:8", "const:4:8"]]
- 009f2c58 ["CALL", null, ["callee:0043b778:8"]]
+ 009f2df4 ["INT_ADD", "register:40f0:8", ["const:9f2df4:8", "const:4:8"]]
+ 009f2df4 ["CALL", null, ["callee:0043b778:8"]]
- 009f2c58 bytes b822e997
+ 009f2df4 bytes 6122e997
- 009f2c54 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 009f2c54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f2c54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f2c54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f2df0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 009f2df0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f2df0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f2df0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f2c54 bytes 00303c91
+ 009f2df0 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b068ea538a10403ee4d9298dd09de712"></a>

### [`009f2c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2c5c.md) → [`009f2df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2df8.md) FUN_009f2df8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009f2dfc",
      "incomplete_value": false,
      "site": "009f2e00",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2c60",
      "incomplete_value": false,
      "site": "009f2c64",
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
            "const:c10:8"
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
      "009f2e00",
      "DATA",
      [
        "storage",
        "00c89c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f2e00",
      "DATA",
      [
        "storage",
        "00c8a010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2c5c.md#insn-009f2c5c) · [`009f2c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2c5c.md#insn-009f2c60)
- 新版 [`009f2df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2df8.md#insn-009f2df8) · [`009f2dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2df8.md#insn-009f2dfc)

~~~diff
- 009f2c5c ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f2df8 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f2c5c bytes a81400f0
+ 009f2df8 bytes c8140090
- 009f2c60 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 009f2c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f2dfc ["COPY", "tmp:0:8", ["const:10:8"]]
+ 009f2dfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2dfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2dfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2c60 bytes 08413091
+ 009f2dfc bytes 08410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd7e9c2dc4ebd0e2d02c3d5548000683"></a>

### [`009f2c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2c6c.md) → [`009f2e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e08.md) FUN_009f2e08

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009f2e18",
      "incomplete_value": false,
      "site": "009f2e20",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2c7c",
      "incomplete_value": false,
      "site": "009f2c84",
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
            "const:c10:8"
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
      "009f2e20",
      "DATA",
      [
        "storage",
        "00c89c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f2e20",
      "DATA",
      [
        "storage",
        "00c8a010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2c6c.md#insn-009f2c78) · [`009f2c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2c6c.md#insn-009f2c7c) · [`009f2c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2c6c.md#insn-009f2c88)
- 新版 [`009f2e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e08.md#insn-009f2e14) · [`009f2e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e08.md#insn-009f2e18) · [`009f2e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e08.md#insn-009f2e24)

~~~diff
- 009f2c78 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f2e14 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f2c78 bytes a81400f0
+ 009f2e14 bytes c8140090
- 009f2c7c ["COPY", "tmp:0:8", ["const:c10:8"]]
- 009f2c7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2c7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2c7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f2e18 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 009f2e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2c7c bytes 08413091
+ 009f2e18 bytes 08410091
- 009f2c88 ["INT_ADD", "register:40f0:8", ["const:9f2c88:8", "const:4:8"]]
- 009f2c88 ["CALL", null, ["callee:00c57ea0:8"]]
+ 009f2e24 ["INT_ADD", "register:40f0:8", ["const:9f2e24:8", "const:4:8"]]
+ 009f2e24 ["CALL", null, ["callee:00c57ea0:8"]]
- 009f2c88 bytes 86930994
+ 009f2e24 bytes 1f940994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecf85caab77a39868679f3650fa2b84d"></a>

### [`009f2e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2e08.md) → [`009f2fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2fa4.md) FUN_009f2fa4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009f2cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2cc8.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`009f2e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e64.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "009f2fb0",
      "incomplete_value": false,
      "site": "009f2fb4",
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
      "definition_site": "009f2e14",
      "incomplete_value": false,
      "site": "009f2e18",
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
      "009f2fb0",
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
      "009f2fb0",
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

- 旧版 [`009f2e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2e08.md#insn-009f2e18) · [`009f2e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2e08.md#insn-009f2e14)
- 新版 [`009f2fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2fa4.md#insn-009f2fb4) · [`009f2fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2fa4.md#insn-009f2fb0)

~~~diff
- 009f2e18 ["INT_ADD", "register:40f0:8", ["const:9f2e18:8", "const:4:8"]]
- 009f2e18 ["CALL", null, ["callee:0043b778:8"]]
+ 009f2fb4 ["INT_ADD", "register:40f0:8", ["const:9f2fb4:8", "const:4:8"]]
+ 009f2fb4 ["CALL", null, ["callee:0043b778:8"]]
- 009f2e18 bytes 4822e997
+ 009f2fb4 bytes f121e997
- 009f2e14 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 009f2e14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f2e14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f2e14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f2fb0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 009f2fb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f2fb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f2fb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f2e14 bytes 00303c91
+ 009f2fb0 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9eecdb2e6f702d7c98188edc12b97017"></a>

### [`009f2eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2eec.md) → [`009f3088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3088.md) FUN_009f3088

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009f308c",
      "incomplete_value": false,
      "site": "009f3090",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2ef0",
      "incomplete_value": false,
      "site": "009f2ef4",
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
      "009f3090",
      "DATA",
      [
        "storage",
        "00c89dc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3090",
      "DATA",
      [
        "storage",
        "00c8a1c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2eec.md#insn-009f2eec) · [`009f2ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2eec.md#insn-009f2ef0)
- 新版 [`009f3088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3088.md#insn-009f3088) · [`009f308c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3088.md#insn-009f308c)

~~~diff
- 009f2eec ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f3088 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f2eec bytes a81400f0
+ 009f3088 bytes a81400f0
- 009f2ef0 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 009f2ef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2ef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2ef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f308c ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 009f308c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f308c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f308c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2ef0 bytes 08013791
+ 009f308c bytes 08010791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5d689c0760ece5ab6f2a5882c59f69d"></a>

### [`009f2efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2efc.md) → [`009f3098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3098.md) FUN_009f3098

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009f30a8",
      "incomplete_value": false,
      "site": "009f30b0",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2f0c",
      "incomplete_value": false,
      "site": "009f2f14",
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
      "009f30b0",
      "DATA",
      [
        "storage",
        "00c89dc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f30b0",
      "DATA",
      [
        "storage",
        "00c8a1c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2efc.md#insn-009f2f08) · [`009f2f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2efc.md#insn-009f2f0c) · [`009f2f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2efc.md#insn-009f2f18)
- 新版 [`009f30a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3098.md#insn-009f30a4) · [`009f30a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3098.md#insn-009f30a8) · [`009f30b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3098.md#insn-009f30b4)

~~~diff
- 009f2f08 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f30a4 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f2f08 bytes a81400f0
+ 009f30a4 bytes a81400f0
- 009f2f0c ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 009f2f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f30a8 ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 009f30a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f30a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f30a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2f0c bytes 08013791
+ 009f30a8 bytes 08010791
- 009f2f18 ["INT_ADD", "register:40f0:8", ["const:9f2f18:8", "const:4:8"]]
- 009f2f18 ["CALL", null, ["callee:00c57ea0:8"]]
+ 009f30b4 ["INT_ADD", "register:40f0:8", ["const:9f30b4:8", "const:4:8"]]
+ 009f30b4 ["CALL", null, ["callee:00c57ea0:8"]]
- 009f2f18 bytes e2920994
+ 009f30b4 bytes 7b930994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ee71d8c76426acbdc553494ced4e4d7"></a>

### [`009f2f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2f58.md) → [`009f30f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f30f4.md) FUN_009f30f4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009f30f8",
      "incomplete_value": false,
      "site": "009f30fc",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2f5c",
      "incomplete_value": false,
      "site": "009f2f60",
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
            "const:e78:8"
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
      "009f30fc",
      "DATA",
      [
        "storage",
        "00c89e78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f30fc",
      "DATA",
      [
        "storage",
        "00c8a278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2f58.md#insn-009f2f58) · [`009f2f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2f58.md#insn-009f2f5c)
- 新版 [`009f30f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f30f4.md#insn-009f30f4) · [`009f30f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f30f4.md#insn-009f30f8)

~~~diff
- 009f2f58 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f30f4 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f2f58 bytes a81400f0
+ 009f30f4 bytes a81400f0
- 009f2f5c ["COPY", "tmp:0:8", ["const:e78:8"]]
- 009f2f5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2f5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2f5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f30f8 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 009f30f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f30f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f30f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2f5c bytes 08e13991
+ 009f30f8 bytes 08e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed62fdb25e42fe6036e7844eef2a12e0"></a>

### [`009f2f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2f68.md) → [`009f3104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3104.md) FUN_009f3104

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009f3114",
      "incomplete_value": false,
      "site": "009f311c",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2f78",
      "incomplete_value": false,
      "site": "009f2f80",
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
            "const:e78:8"
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
      "009f311c",
      "DATA",
      [
        "storage",
        "00c89e78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f311c",
      "DATA",
      [
        "storage",
        "00c8a278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2f68.md#insn-009f2f74) · [`009f2f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2f68.md#insn-009f2f78) · [`009f2f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2f68.md#insn-009f2f84)
- 新版 [`009f3110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3104.md#insn-009f3110) · [`009f3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3104.md#insn-009f3114) · [`009f3120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3104.md#insn-009f3120)

~~~diff
- 009f2f74 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f3110 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f2f74 bytes a81400f0
+ 009f3110 bytes a81400f0
- 009f2f78 ["COPY", "tmp:0:8", ["const:e78:8"]]
- 009f2f78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2f78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2f78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f3114 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 009f3114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2f78 bytes 08e13991
+ 009f3114 bytes 08e10991
- 009f2f84 ["INT_ADD", "register:40f0:8", ["const:9f2f84:8", "const:4:8"]]
- 009f2f84 ["CALL", null, ["callee:00c57ea0:8"]]
+ 009f3120 ["INT_ADD", "register:40f0:8", ["const:9f3120:8", "const:4:8"]]
+ 009f3120 ["CALL", null, ["callee:00c57ea0:8"]]
- 009f2f84 bytes c7920994
+ 009f3120 bytes 60930994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9659c8e236c55ea4d11857c85127ae2"></a>

### [`009f2fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2fc8.md) → [`009f3164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3164.md) FUN_009f3164

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009ec0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ec/009ec0b4.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`009ec250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec250.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "009f31f0",
      "incomplete_value": false,
      "site": "009f3258",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3054",
      "incomplete_value": false,
      "site": "009f30bc",
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
            "const:bb0:8"
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
      "009f3258",
      "DATA",
      [
        "storage",
        "00c89bb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3258",
      "DATA",
      [
        "storage",
        "00c89fb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f303c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2fc8.md#insn-009f303c) · [`009f3054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2fc8.md#insn-009f3054) · [`009f30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2fc8.md#insn-009f30d4)
- 新版 [`009f31d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3164.md#insn-009f31d8) · [`009f31f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3164.md#insn-009f31f0) · [`009f3270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3164.md#insn-009f3270)

~~~diff
- 009f303c ["INT_ADD", "register:40f0:8", ["const:9f303c:8", "const:4:8"]]
- 009f303c ["CALL", null, ["callee:00c57e90:8"]]
+ 009f31d8 ["INT_ADD", "register:40f0:8", ["const:9f31d8:8", "const:4:8"]]
+ 009f31d8 ["CALL", null, ["callee:00c57e90:8"]]
- 009f303c bytes 95920994
+ 009f31d8 bytes 2e930994
- 009f3054 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 009f3054 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009f3054 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009f3054 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009f31f0 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 009f31f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009f31f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009f31f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009f3054 bytes 29c12e91
+ 009f31f0 bytes 29c13e91
- 009f30d4 ["INT_ADD", "register:40f0:8", ["const:9f30d4:8", "const:4:8"]]
- 009f30d4 ["CALL", null, ["callee:0043bba4:8"]]
+ 009f3270 ["INT_ADD", "register:40f0:8", ["const:9f3270:8", "const:4:8"]]
+ 009f3270 ["CALL", null, ["callee:0043bba4:8"]]
- 009f30d4 bytes a422e997
+ 009f3270 bytes 4d22e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11d1506ad9661375814ddf4269a35c72"></a>

### [`009f3108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3108.md) → [`009f32a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f32a4.md) FUN_009f32a4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ec7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ec/009ec7c0.md) · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 1件 [`009ec95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec95c.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "009f32c0",
      "incomplete_value": false,
      "site": "009f32c0",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3124",
      "incomplete_value": false,
      "site": "009f3124",
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
            "const:f30:8"
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
      "definition_site": "009f32cc",
      "incomplete_value": false,
      "site": "009f32cc",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3130",
      "incomplete_value": false,
      "site": "009f3130",
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
            "const:f80:8"
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
      "009f32c0",
      "DATA",
      [
        "storage",
        "00c89f30",
        null,
        "undefined *"
      ]
    ],
    [
      "009f32cc",
      "DATA",
      [
        "storage",
        "00c89f80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f32c0",
      "DATA",
      [
        "storage",
        "00c8a330",
        null,
        "undefined *"
      ]
    ],
    [
      "009f32cc",
      "DATA",
      [
        "storage",
        "00c8a380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3108.md#insn-009f3118) · [`009f311c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3108.md#insn-009f311c) · [`009f3128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3108.md#insn-009f3128)
- 新版 [`009f32b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f32a4.md#insn-009f32b4) · [`009f32b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f32a4.md#insn-009f32b8)

~~~diff
- 009f3118 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f32b4 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f3118 bytes a81400d0
+ 009f32b4 bytes a81400f0
- 009f311c ["COPY", "tmp:0:8", ["const:f30:8"]]
- 009f311c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f311c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f311c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f32b8 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 009f32b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f32b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f32b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f311c bytes 08c13c91
+ 009f32b8 bytes 08c10c91
- 009f3128 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009f3128 bytes a81400d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-746745d9f711e748c90a3f49711f9924"></a>

### [`009f3208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3208.md) → [`009f33a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33a4.md) FUN_009f33a4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009f33a8",
      "incomplete_value": false,
      "site": "009f33ac",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f320c",
      "incomplete_value": false,
      "site": "009f3210",
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
      "009f33ac",
      "DATA",
      [
        "storage",
        "00c89f30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f33ac",
      "DATA",
      [
        "storage",
        "00c8a330",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3208.md#insn-009f3208) · [`009f320c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3208.md#insn-009f320c)
- 新版 [`009f33a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33a4.md#insn-009f33a4) · [`009f33a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33a4.md#insn-009f33a8)

~~~diff
- 009f3208 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f33a4 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f3208 bytes a81400d0
+ 009f33a4 bytes a81400f0
- 009f320c ["COPY", "tmp:0:8", ["const:f30:8"]]
- 009f320c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f320c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f320c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f33a8 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 009f33a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f33a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f33a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f320c bytes 08c13c91
+ 009f33a8 bytes 08c10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29976e17247ec5b2cfb588f879a384d5"></a>

### [`009f3218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3218.md) → [`009f33b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33b4.md) FUN_009f33b4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009f33c4",
      "incomplete_value": false,
      "site": "009f33cc",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3228",
      "incomplete_value": false,
      "site": "009f3230",
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
      "009f33cc",
      "DATA",
      [
        "storage",
        "00c89f30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f33cc",
      "DATA",
      [
        "storage",
        "00c8a330",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3218.md#insn-009f3224) · [`009f3228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3218.md#insn-009f3228) · [`009f3234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3218.md#insn-009f3234)
- 新版 [`009f33c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33b4.md#insn-009f33c0) · [`009f33c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33b4.md#insn-009f33c4) · [`009f33d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33b4.md#insn-009f33d0)

~~~diff
- 009f3224 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f33c0 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f3224 bytes a81400d0
+ 009f33c0 bytes a81400f0
- 009f3228 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 009f3228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f3228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f3228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f33c4 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 009f33c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f33c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f33c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f3228 bytes 08c13c91
+ 009f33c4 bytes 08c10c91
- 009f3234 ["INT_ADD", "register:40f0:8", ["const:9f3234:8", "const:4:8"]]
- 009f3234 ["CALL", null, ["callee:00c57ea0:8"]]
+ 009f33d0 ["INT_ADD", "register:40f0:8", ["const:9f33d0:8", "const:4:8"]]
+ 009f33d0 ["CALL", null, ["callee:00c57ea0:8"]]
- 009f3234 bytes 1b920994
+ 009f33d0 bytes b4920994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39eb4604e70eb80a39ccaf9af44081d5"></a>

### [`009f3258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3258.md) → [`009f33f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33f4.md) FUN_009f33f4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009f3408",
      "incomplete_value": false,
      "site": "009f340c",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f326c",
      "incomplete_value": false,
      "site": "009f3270",
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
            "const:f80:8"
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
      "009f340c",
      "DATA",
      [
        "storage",
        "00c89f80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f340c",
      "DATA",
      [
        "storage",
        "00c8a380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3258.md#insn-009f3268) · [`009f326c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3258.md#insn-009f326c) · [`009f3280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3258.md#insn-009f3280)
- 新版 [`009f3404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33f4.md#insn-009f3404) · [`009f3408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33f4.md#insn-009f3408) · [`009f341c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33f4.md#insn-009f341c)

~~~diff
- 009f3268 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f3404 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f3268 bytes a81400d0
+ 009f3404 bytes a81400f0
- 009f326c ["COPY", "tmp:0:8", ["const:f80:8"]]
- 009f326c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f326c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f326c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f3408 ["COPY", "tmp:0:8", ["const:380:8"]]
+ 009f3408 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3408 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f326c bytes 08013e91
+ 009f3408 bytes 08010e91
- 009f3280 ["INT_ADD", "register:40f0:8", ["const:9f3280:8", "const:4:8"]]
- 009f3280 ["CALL", null, ["callee:00c53d00:8"]]
+ 009f341c ["INT_ADD", "register:40f0:8", ["const:9f341c:8", "const:4:8"]]
+ 009f341c ["CALL", null, ["callee:00c53d00:8"]]
- 009f3280 bytes 98810994
+ 009f341c bytes 39820994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06debd7d6b6d219e1fb39345681ae466"></a>

### [`009f32b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f32b4.md) → [`009f3450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3450.md) FUN_009f3450

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009f3468",
      "incomplete_value": false,
      "site": "009f346c",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f32cc",
      "incomplete_value": false,
      "site": "009f32d0",
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
            "const:f80:8"
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
      "009f346c",
      "DATA",
      [
        "storage",
        "00c89f80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f346c",
      "DATA",
      [
        "storage",
        "00c8a380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f32c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f32b4.md#insn-009f32c8) · [`009f32cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f32b4.md#insn-009f32cc) · [`009f32e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f32b4.md#insn-009f32e0)
- 新版 [`009f3464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3450.md#insn-009f3464) · [`009f3468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3450.md#insn-009f3468) · [`009f347c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3450.md#insn-009f347c)

~~~diff
- 009f32c8 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f3464 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f32c8 bytes a81400d0
+ 009f3464 bytes a81400f0
- 009f32cc ["COPY", "tmp:0:8", ["const:f80:8"]]
- 009f32cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f32cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f32cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f3468 ["COPY", "tmp:0:8", ["const:380:8"]]
+ 009f3468 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3468 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3468 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f32cc bytes 08013e91
+ 009f3468 bytes 08010e91
- 009f32e0 ["INT_ADD", "register:40f0:8", ["const:9f32e0:8", "const:4:8"]]
- 009f32e0 ["CALL", null, ["callee:00c53d00:8"]]
+ 009f347c ["INT_ADD", "register:40f0:8", ["const:9f347c:8", "const:4:8"]]
+ 009f347c ["CALL", null, ["callee:00c53d00:8"]]
- 009f32e0 bytes 80810994
+ 009f347c bytes 21820994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-278227d9f7b64392e10191e6f29132a3"></a>

### [`009f3460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3460.md) → [`009f35fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f35fc.md) FUN_009f35fc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009ecf7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ec/009ecf7c.md) [`009f17dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f1/009f17dc.md) [`009f1cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f1/009f1cb0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`009ed118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed118.md) [`009f1978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1978.md) [`009f1e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "009f3608",
      "incomplete_value": false,
      "site": "009f360c",
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
      "definition_site": "009f346c",
      "incomplete_value": false,
      "site": "009f3470",
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
      "009f3608",
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
      "009f3608",
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

- 旧版 [`009f3470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3460.md#insn-009f3470) · [`009f346c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3460.md#insn-009f346c)
- 新版 [`009f360c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f35fc.md#insn-009f360c) · [`009f3608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f35fc.md#insn-009f3608)

~~~diff
- 009f3470 ["INT_ADD", "register:40f0:8", ["const:9f3470:8", "const:4:8"]]
- 009f3470 ["CALL", null, ["callee:0043b778:8"]]
+ 009f360c ["INT_ADD", "register:40f0:8", ["const:9f360c:8", "const:4:8"]]
+ 009f360c ["CALL", null, ["callee:0043b778:8"]]
- 009f3470 bytes b220e997
+ 009f360c bytes 5b20e997
- 009f346c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 009f346c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f346c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f346c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f3608 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 009f3608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f346c bytes 00303c91
+ 009f3608 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11d6d7cedaf68083fd03e901a03de80e"></a>

### [`009f38d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f38d8.md) → [`009f3a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3a74.md) FUN_009f3a74

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009f3a78",
      "incomplete_value": false,
      "site": "009f3a7c",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f38dc",
      "incomplete_value": false,
      "site": "009f38e0",
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
      "009f3a7c",
      "DATA",
      [
        "storage",
        "00c89fb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3a7c",
      "DATA",
      [
        "storage",
        "00c8a3b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f38d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f38d8.md#insn-009f38d8) · [`009f38dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f38d8.md#insn-009f38dc)
- 新版 [`009f3a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3a74.md#insn-009f3a74) · [`009f3a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3a74.md#insn-009f3a78)

~~~diff
- 009f38d8 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f3a74 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f38d8 bytes a81400d0
+ 009f3a74 bytes a81400f0
- 009f38dc ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 009f38dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f38dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f38dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f3a78 ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 009f3a78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3a78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3a78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f38dc bytes 08c13e91
+ 009f3a78 bytes 08c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-292fb296bebf0c44ea3944a3b2416373"></a>

### [`009f391c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f391c.md) → [`009f3ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3ab8.md) FUN_009f3ab8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`009efc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ef/009efc4c.md) [`009f0370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f0/009f0370.md) [`009f1064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f1/009f1064.md) [`009f3ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3ad0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 4件 [`009efde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md) [`009f050c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md) [`009f1200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1200.md) [`009f3c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c6c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "009f3ac4",
      "incomplete_value": false,
      "site": "009f3ac8",
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
      "definition_site": "009f3928",
      "incomplete_value": false,
      "site": "009f392c",
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
      "009f3ac4",
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
      "009f3ac4",
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

- 旧版 [`009f392c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f391c.md#insn-009f392c) · [`009f3928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f391c.md#insn-009f3928)
- 新版 [`009f3ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3ab8.md#insn-009f3ac8) · [`009f3ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3ab8.md#insn-009f3ac4)

~~~diff
- 009f392c ["INT_ADD", "register:40f0:8", ["const:9f392c:8", "const:4:8"]]
- 009f392c ["CALL", null, ["callee:0043b778:8"]]
+ 009f3ac8 ["INT_ADD", "register:40f0:8", ["const:9f3ac8:8", "const:4:8"]]
+ 009f3ac8 ["CALL", null, ["callee:0043b778:8"]]
- 009f392c bytes 831fe997
+ 009f3ac8 bytes 2c1fe997
- 009f3928 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 009f3928 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f3928 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f3928 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f3ac4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 009f3ac4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3ac4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3ac4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f3928 bytes 00303c91
+ 009f3ac4 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d52fb07a2c74bec69d00d87385eb22dc"></a>

### [`009f3abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3abc.md) → [`009f3c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c58.md) FUN_009f3c58

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009f3930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3930.md) [`009f47b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f47b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`009f3acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3acc.md) [`009f4950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4950.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "009f3c64",
      "incomplete_value": false,
      "site": "009f3c68",
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
      "definition_site": "009f3ac8",
      "incomplete_value": false,
      "site": "009f3acc",
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
      "009f3c64",
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
      "009f3c64",
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

- 旧版 [`009f3acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3abc.md#insn-009f3acc) · [`009f3ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f3/009f3abc.md#insn-009f3ac8)
- 新版 [`009f3c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c58.md#insn-009f3c68) · [`009f3c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c58.md#insn-009f3c64)

~~~diff
- 009f3acc ["INT_ADD", "register:40f0:8", ["const:9f3acc:8", "const:4:8"]]
- 009f3acc ["CALL", null, ["callee:0043b778:8"]]
+ 009f3c68 ["INT_ADD", "register:40f0:8", ["const:9f3c68:8", "const:4:8"]]
+ 009f3c68 ["CALL", null, ["callee:0043b778:8"]]
- 009f3acc bytes 1b1fe997
+ 009f3c68 bytes c41ee997
- 009f3ac8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 009f3ac8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f3ac8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f3ac8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f3c64 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 009f3c64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3c64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3c64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f3ac8 bytes 00303c91
+ 009f3c64 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fa43de04cfe185a6bd5df93328a2dc0"></a>

### [`009f4940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4940.md) → [`009f4adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4adc.md) FUN_009f4adc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009f1420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f1/009f1420.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`009f15bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f15bc.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "009f4ae8",
      "incomplete_value": false,
      "site": "009f4aec",
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
      "definition_site": "009f494c",
      "incomplete_value": false,
      "site": "009f4950",
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
      "009f4ae8",
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
      "009f4ae8",
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

- 旧版 [`009f4950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4940.md#insn-009f4950) · [`009f494c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4940.md#insn-009f494c)
- 新版 [`009f4aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4adc.md#insn-009f4aec) · [`009f4ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4adc.md#insn-009f4ae8)

~~~diff
- 009f4950 ["INT_ADD", "register:40f0:8", ["const:9f4950:8", "const:4:8"]]
- 009f4950 ["CALL", null, ["callee:0043b778:8"]]
+ 009f4aec ["INT_ADD", "register:40f0:8", ["const:9f4aec:8", "const:4:8"]]
+ 009f4aec ["CALL", null, ["callee:0043b778:8"]]
- 009f4950 bytes 7a1be997
+ 009f4aec bytes 231be997
- 009f494c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 009f494c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f494c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f494c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f4ae8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 009f4ae8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4ae8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4ae8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f494c bytes 00303c91
+ 009f4ae8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aeae07a4b9d25a367cb85b6b8a3e2a49"></a>

### [`009f4954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4954.md) → [`009f4af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4af0.md) FUN_009f4af0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009f1564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f1/009f1564.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`009f1700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1700.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "009f4afc",
      "incomplete_value": false,
      "site": "009f4b00",
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
      "definition_site": "009f4960",
      "incomplete_value": false,
      "site": "009f4964",
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
      "009f4afc",
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
      "009f4afc",
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

- 旧版 [`009f4964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4954.md#insn-009f4964) · [`009f4960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4954.md#insn-009f4960)
- 新版 [`009f4b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4af0.md#insn-009f4b00) · [`009f4afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4af0.md#insn-009f4afc)

~~~diff
- 009f4964 ["INT_ADD", "register:40f0:8", ["const:9f4964:8", "const:4:8"]]
- 009f4964 ["CALL", null, ["callee:0043b778:8"]]
+ 009f4b00 ["INT_ADD", "register:40f0:8", ["const:9f4b00:8", "const:4:8"]]
+ 009f4b00 ["CALL", null, ["callee:0043b778:8"]]
- 009f4964 bytes 751be997
+ 009f4b00 bytes 1e1be997
- 009f4960 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 009f4960 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f4960 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f4960 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f4afc ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 009f4afc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4afc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4afc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f4960 bytes 00303c91
+ 009f4afc bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f0f806c9e92c84f1a0cc70796b7692f"></a>

### [`009f4968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4968.md) → [`009f4b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b04.md) FUN_009f4b04

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009f4b08",
      "incomplete_value": false,
      "site": "009f4b0c",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f496c",
      "incomplete_value": false,
      "site": "009f4970",
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
      "009f4b0c",
      "DATA",
      [
        "storage",
        "00c8a030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f4b0c",
      "DATA",
      [
        "storage",
        "00c8a430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f496c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4968.md#insn-009f496c)
- 新版 [`009f4b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b04.md#insn-009f4b08)

~~~diff
- 009f496c ["COPY", "tmp:0:8", ["const:30:8"]]
- 009f496c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f496c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f496c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f4b08 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 009f4b08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4b08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4b08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f496c bytes 08c10091
+ 009f4b08 bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c4e7a40304df5cf69b1a6b3f1161fb4"></a>

### [`009f4978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4978.md) → [`009f4b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b14.md) FUN_009f4b14

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009f4b24",
      "incomplete_value": false,
      "site": "009f4b2c",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f4988",
      "incomplete_value": false,
      "site": "009f4990",
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
            "const:30:8"
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
      "009f4b2c",
      "DATA",
      [
        "storage",
        "00c8a030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f4b2c",
      "DATA",
      [
        "storage",
        "00c8a430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f4988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4978.md#insn-009f4988) · [`009f4994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4978.md#insn-009f4994)
- 新版 [`009f4b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b14.md#insn-009f4b24) · [`009f4b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b14.md#insn-009f4b30)

~~~diff
- 009f4988 ["COPY", "tmp:0:8", ["const:30:8"]]
- 009f4988 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f4988 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f4988 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f4b24 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 009f4b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f4988 bytes 08c10091
+ 009f4b24 bytes 08c11091
- 009f4994 ["INT_ADD", "register:40f0:8", ["const:9f4994:8", "const:4:8"]]
- 009f4994 ["CALL", null, ["callee:00c57ea0:8"]]
+ 009f4b30 ["INT_ADD", "register:40f0:8", ["const:9f4b30:8", "const:4:8"]]
+ 009f4b30 ["CALL", null, ["callee:00c57ea0:8"]]
- 009f4994 bytes 438c0994
+ 009f4b30 bytes dc8c0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1c9ae7d325aecdf6cfa0d9980272f15"></a>

### [`009f49b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f49b4.md) → [`009f4b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md) FUN_009f4b50

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009f49a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f49a8.md) · 呼出先 8件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`009f26f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f26f8.md) [`009f2748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2748.md) [`009f2798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f2798.md) [`009f27dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f2/009f27dc.md)
- 新版 呼出元 1件 [`009f4b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b44.md) · 呼出先 8件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`009f2894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2894.md) [`009f28e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f28e4.md) [`009f2934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2934.md) [`009f2978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2978.md)

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
      "definition_site": "009f4b6c",
      "incomplete_value": false,
      "site": "009f4b6c",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f49d0",
      "incomplete_value": false,
      "site": "009f49d0",
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
            "const:a58:8"
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
      "009f4b6c",
      "DATA",
      [
        "storage",
        "00c89a58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f4b6c",
      "DATA",
      [
        "storage",
        "00c89e58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f49c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f49b4.md#insn-009f49c8) · [`009f49d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f49b4.md#insn-009f49d4) · [`009f49e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f49b4.md#insn-009f49e0)
- 新版 [`009f4b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md#insn-009f4b64) · [`009f4b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md#insn-009f4b70) · [`009f4b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md#insn-009f4b7c)

~~~diff
- 009f49c8 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 009f49c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f49c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f49c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f4b64 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 009f4b64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4b64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4b64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f49c8 bytes 08612991
+ 009f4b64 bytes 08613991
- 009f49d4 ["INT_ADD", "register:40f0:8", ["const:9f49d4:8", "const:4:8"]]
- 009f49d4 ["CALL", null, ["callee:009f3894:8"]]
+ 009f4b70 ["INT_ADD", "register:40f0:8", ["const:9f4b70:8", "const:4:8"]]
+ 009f4b70 ["CALL", null, ["callee:009f3894:8"]]
- 009f49d4 bytes 49fbff97
+ 009f4b70 bytes 49fbff97
- 009f49e0 ["INT_ADD", "register:40f0:8", ["const:9f49e0:8", "const:4:8"]]
- 009f49e0 ["CALL", null, ["callee:009f2894:8"]]
+ 009f4b7c ["INT_ADD", "register:40f0:8", ["const:9f4b7c:8", "const:4:8"]]
+ 009f4b7c ["CALL", null, ["callee:009f2894:8"]]
- 009f49e0 bytes 46f7ff97
+ 009f4b7c bytes 46f7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1694ab008d43c4498ec980ad9da05e0d"></a>

### [`009f4a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4a70.md) → [`009f4c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4c0c.md) _INIT_205

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "009f4c48",
      "incomplete_value": true,
      "site": "009f4c64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009f4aac",
      "incomplete_value": true,
      "site": "009f4ac8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009f4cc8",
      "incomplete_value": true,
      "site": "009f4ce4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f4b2c",
      "incomplete_value": true,
      "site": "009f4b48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:592:8"
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
      "definition_site": "009f4ce8",
      "incomplete_value": true,
      "site": "009f4d04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009f4b4c",
      "incomplete_value": true,
      "site": "009f4b68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f4c48",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "009f4c6c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "009f4c8c",
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
      "009f4c48",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "009f4c6c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "009f4c8c",
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

- 旧版 [`009f4b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4a70.md#insn-009f4b08) · [`009f4ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4a70.md#insn-009f4ca4) · [`009f4a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4a70.md#insn-009f4a9c)
- 新版 [`009f4ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4c0c.md#insn-009f4ca4) · [`009f4e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4c0c.md#insn-009f4e40) · [`009f4c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4c0c.md#insn-009f4c38)

~~~diff
- 009f4b08 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 009f4b08 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009f4b08 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009f4b08 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009f4ca4 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 009f4ca4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009f4ca4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009f4ca4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009f4b08 bytes 4a553a91
+ 009f4ca4 bytes 4a893d91
- 009f4ca4 ["INT_ADD", "register:40f0:8", ["const:9f4ca4:8", "const:4:8"]]
- 009f4ca4 ["CALL", null, ["callee:00c57e30:8"]]
+ 009f4e40 ["INT_ADD", "register:40f0:8", ["const:9f4e40:8", "const:4:8"]]
+ 009f4e40 ["CALL", null, ["callee:00c57e30:8"]]
- 009f4ca4 bytes 638b0994
+ 009f4e40 bytes fc8b0994
- 009f4a9c ["COPY", "tmp:0:8", ["const:938:8"]]
- 009f4a9c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009f4a9c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009f4a9c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009f4c38 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 009f4c38 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009f4c38 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009f4c38 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009f4a9c bytes 73e22491
+ 009f4c38 bytes 73e23491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-444cd73fdfd1aeb78ae9b9bf55bcdc2a"></a>

### [`009f4e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4e08.md) → [`009f4fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4fa4.md) FUN_009f4fa4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009fb2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fb/009fb2b0.md) · 呼出先 14件 [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) [`00664860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664860.md) [`00666768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666768.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`009df728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df728.md)
- 新版 呼出元 1件 [`009fb44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md) · 呼出先 14件 [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md) [`006667a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00666/006667a8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`009df8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8c4.md)

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
      "site": "009f5288",
      "value": [
        "leaf",
        "ram:6648a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f50ec",
      "value": [
        "leaf",
        "ram:664860:8"
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
      "009f4ffc",
      "DATA",
      [
        "storage",
        "00c8a0b0",
        null,
        "undefined *"
      ]
    ],
    [
      "009f5004",
      "READ",
      [
        "storage",
        "002c41c8",
        null,
        "undefined8"
      ]
    ],
    [
      "009f5288",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664860"
      ]
    ]
  ],
  "added": [
    [
      "009f4ffc",
      "DATA",
      [
        "storage",
        "00c8a4b0",
        null,
        "undefined *"
      ]
    ],
    [
      "009f5004",
      "READ",
      [
        "storage",
        "002c4208",
        null,
        "undefined8"
      ]
    ],
    [
      "009f5288",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f50ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4e08.md#insn-009f50ec) · [`009f4e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4e08.md#insn-009f4e4c) · [`009f4e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4e08.md#insn-009f4e58)
- 新版 [`009f5288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4fa4.md#insn-009f5288) · [`009f4fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4fa4.md#insn-009f4fe8) · [`009f4ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4fa4.md#insn-009f4ff4)

~~~diff
- 009f50ec ["INT_ADD", "register:40f0:8", ["const:9f50ec:8", "const:4:8"]]
- 009f50ec ["CALL", null, ["ram:664860:8"]]
+ 009f5288 ["INT_ADD", "register:40f0:8", ["const:9f5288:8", "const:4:8"]]
+ 009f5288 ["CALL", null, ["ram:6648a0:8"]]
- 009f50ec bytes ddbdf197
+ 009f5288 bytes 86bdf197
- 009f4e4c ["INT_ADD", "register:40f0:8", ["const:9f4e4c:8", "const:4:8"]]
- 009f4e4c ["CALL", null, ["callee:00c57e90:8"]]
+ 009f4fe8 ["INT_ADD", "register:40f0:8", ["const:9f4fe8:8", "const:4:8"]]
+ 009f4fe8 ["CALL", null, ["callee:00c57e90:8"]]
- 009f4e4c bytes 118b0994
+ 009f4fe8 bytes aa8b0994
- 009f4e58 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 009f4e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f4e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f4e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f4ff4 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 009f4ff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4ff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4ff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f4e58 bytes 08c10291
+ 009f4ff4 bytes 08c11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc9377b59a0bbe057632033f9151a154"></a>

### [`009f520c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f520c.md) → [`009f53a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f53a8.md) FUN_009f53a8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "009f53c8",
      "incomplete_value": false,
      "site": "009f53cc",
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
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f522c",
      "incomplete_value": false,
      "site": "009f5230",
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
            "const:b0:8"
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
      "definition_site": "009f5408",
      "incomplete_value": false,
      "site": "009f5410",
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
    "old": {
      "definition_site": "009f526c",
      "incomplete_value": false,
      "site": "009f5274",
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
      "009f53cc",
      "DATA",
      [
        "storage",
        "00c8a0b0",
        null,
        "undefined *"
      ]
    ],
    [
      "009f5410",
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
      "009f53cc",
      "DATA",
      [
        "storage",
        "00c8a4b0",
        null,
        "undefined *"
      ]
    ],
    [
      "009f5410",
      "DATA",
      [
        "storage",
        "00c8a480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f522c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f520c.md#insn-009f522c) · [`009f5240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f520c.md#insn-009f5240) · [`009f5254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f520c.md#insn-009f5254)
- 新版 [`009f53c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f53a8.md#insn-009f53c8) · [`009f53dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f53a8.md#insn-009f53dc) · [`009f53f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f53a8.md#insn-009f53f0)

~~~diff
- 009f522c ["COPY", "tmp:0:8", ["const:b0:8"]]
- 009f522c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f522c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f522c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f53c8 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 009f53c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f53c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f53c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f522c bytes 08c10291
+ 009f53c8 bytes 08c11291
- 009f5240 ["INT_ADD", "register:40f0:8", ["const:9f5240:8", "const:4:8"]]
- 009f5240 ["CALL", null, ["callee:00c53d00:8"]]
+ 009f53dc ["INT_ADD", "register:40f0:8", ["const:9f53dc:8", "const:4:8"]]
+ 009f53dc ["CALL", null, ["callee:00c53d00:8"]]
- 009f5240 bytes a8790994
+ 009f53dc bytes 497a0994
- 009f5254 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f5254 ["INT_ADD", "register:40f0:8", ["const:9f5254:8", "const:4:8"]]
- 009f5254 ["CALLIND", null, ["register:0:8"]]
+ 009f53f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f53f0 ["INT_ADD", "register:40f0:8", ["const:9f53f0:8", "const:4:8"]]
+ 009f53f0 ["CALLIND", null, ["register:0:8"]]
- 009f5254 bytes 00013fd6
+ 009f53f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49a29f84b5eafcfb2211fdf8feb19c71"></a>

### [`009f53b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f53b8.md) → [`009f5554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5554.md) FUN_009f5554

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 19件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046a210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a210.md) [`0046aed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aed8.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md) [`0046af18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af18.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.88% / 新版 97.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f58e4",
      "incomplete_value": true,
      "site": "009f58fc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "009f5748",
      "incomplete_value": true,
      "site": "009f5760",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f58e0",
      "incomplete_value": true,
      "site": "009f5900",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:302000:8"
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
    "old": {
      "definition_site": "009f5744",
      "incomplete_value": true,
      "site": "009f5764",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:302000:8"
              ],
              [
                "leaf",
                "const:c30:8"
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
      "definition_site": "009f58e0",
      "incomplete_value": true,
      "site": "009f5900",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "009f5744",
      "incomplete_value": true,
      "site": "009f5764",
      "value": [
        "LOAD",
        "16",
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
      "009f5594",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "009f55a0",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f55a8",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f5594",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f55a0",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f55a8",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f5418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f53b8.md#insn-009f5418) · [`009f5598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f53b8.md#insn-009f5598) · [`009f55c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f53b8.md#insn-009f55c4)
- 新版 [`009f55b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5554.md#insn-009f55b4) · [`009f5734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5554.md#insn-009f5734) · [`009f5760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5554.md#insn-009f5760)

~~~diff
- 009f5418 ["INT_ADD", "register:40f0:8", ["const:9f5418:8", "const:4:8"]]
- 009f5418 ["CALL", null, ["callee:00c58610:8"]]
+ 009f55b4 ["INT_ADD", "register:40f0:8", ["const:9f55b4:8", "const:4:8"]]
+ 009f55b4 ["CALL", null, ["callee:00c58610:8"]]
- 009f5418 bytes 7e8b0994
+ 009f55b4 bytes 178c0994
- 009f5598 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f5598 ["INT_ADD", "register:40f0:8", ["const:9f5598:8", "const:4:8"]]
- 009f5598 ["CALLIND", null, ["register:0:8"]]
+ 009f5734 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f5734 ["INT_ADD", "register:40f0:8", ["const:9f5734:8", "const:4:8"]]
+ 009f5734 ["CALLIND", null, ["register:0:8"]]
- 009f5598 bytes 00013fd6
+ 009f5734 bytes 00013fd6
- 009f55c4 ["INT_ADD", "register:40f0:8", ["const:9f55c4:8", "const:4:8"]]
- 009f55c4 ["CALL", null, ["callee:009df8ec:8"]]
+ 009f5760 ["INT_ADD", "register:40f0:8", ["const:9f5760:8", "const:4:8"]]
+ 009f5760 ["CALL", null, ["callee:009df8ec:8"]]
- 009f55c4 bytes 63a8ff97
+ 009f5760 bytes 63a8ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-802e3104c7bb3da35fb8eb8c6118f16f"></a>

### [`009f5918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f5918.md) → [`009f5ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5ab4.md) FUN_009f5ab4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009fb2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fb/009fb2b0.md) · 呼出先 20件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00665d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665d24.md)
- 新版 呼出元 1件 [`009fb44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md) · 呼出先 20件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00665d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665d64.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f5b0c",
      "incomplete_value": false,
      "site": "009f5b18",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f5970",
      "incomplete_value": false,
      "site": "009f597c",
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
            "const:e8:8"
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
      "definition_site": "009f5b50",
      "incomplete_value": true,
      "site": "009f5b58",
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
                "const:208:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f59b4",
      "incomplete_value": true,
      "site": "009f59bc",
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
                "const:1c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f5f94",
      "value": [
        "leaf",
        "ram:6c6394:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f5df8",
      "value": [
        "leaf",
        "ram:6c6354:8"
      ]
    },
    "ordinal": 49,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f5b18",
      "DATA",
      [
        "storage",
        "00c8a0e8",
        null,
        "undefined *"
      ]
    ],
    [
      "009f5b50",
      "READ",
      [
        "storage",
        "002c41c8",
        null,
        "undefined8"
      ]
    ],
    [
      "009f5f94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c6354"
      ]
    ]
  ],
  "added": [
    [
      "009f5b18",
      "DATA",
      [
        "storage",
        "00c8a4e8",
        null,
        "undefined *"
      ]
    ],
    [
      "009f5b50",
      "READ",
      [
        "storage",
        "002c4208",
        null,
        "undefined8"
      ]
    ],
    [
      "009f5f94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c6394"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f5b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f5918.md#insn-009f5b18) · [`009f5df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f5918.md#insn-009f5df8) · [`009f5964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f5918.md#insn-009f5964)
- 新版 [`009f5cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5ab4.md#insn-009f5cb4) · [`009f5f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5ab4.md#insn-009f5f94) · [`009f5b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5ab4.md#insn-009f5b00)

~~~diff
- 009f5b18 ["INT_ADD", "register:40f0:8", ["const:9f5b18:8", "const:4:8"]]
- 009f5b18 ["CALL", null, ["callee:00c57e80:8"]]
+ 009f5cb4 ["INT_ADD", "register:40f0:8", ["const:9f5cb4:8", "const:4:8"]]
+ 009f5cb4 ["CALL", null, ["callee:00c57e80:8"]]
- 009f5b18 bytes da870994
+ 009f5cb4 bytes 73880994
- 009f5df8 ["INT_ADD", "register:40f0:8", ["const:9f5df8:8", "const:4:8"]]
- 009f5df8 ["CALL", null, ["ram:6c6354:8"]]
+ 009f5f94 ["INT_ADD", "register:40f0:8", ["const:9f5f94:8", "const:4:8"]]
+ 009f5f94 ["CALL", null, ["ram:6c6394:8"]]
- 009f5df8 bytes 5741f397
+ 009f5f94 bytes 0041f397
- 009f5964 ["INT_ADD", "register:40f0:8", ["const:9f5964:8", "const:4:8"]]
- 009f5964 ["CALL", null, ["callee:00c57e90:8"]]
+ 009f5b00 ["INT_ADD", "register:40f0:8", ["const:9f5b00:8", "const:4:8"]]
+ 009f5b00 ["CALL", null, ["callee:00c57e90:8"]]
- 009f5964 bytes 4b880994
+ 009f5b00 bytes e4880994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ec29d1547e96a7193899d4a71ec02c5"></a>

### [`009f6748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f6748.md) → [`009f68e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f68e4.md) FUN_009f68e4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "009f6904",
      "incomplete_value": false,
      "site": "009f6908",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f6768",
      "incomplete_value": false,
      "site": "009f676c",
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
            "const:e8:8"
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
      "definition_site": "009f6944",
      "incomplete_value": false,
      "site": "009f694c",
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
    "old": {
      "definition_site": "009f67a8",
      "incomplete_value": false,
      "site": "009f67b0",
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
      "009f6908",
      "DATA",
      [
        "storage",
        "00c8a0e8",
        null,
        "undefined *"
      ]
    ],
    [
      "009f694c",
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
      "009f6908",
      "DATA",
      [
        "storage",
        "00c8a4e8",
        null,
        "undefined *"
      ]
    ],
    [
      "009f694c",
      "DATA",
      [
        "storage",
        "00c8a480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f6768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f6748.md#insn-009f6768) · [`009f677c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f6748.md#insn-009f677c) · [`009f6790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f6748.md#insn-009f6790)
- 新版 [`009f6904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f68e4.md#insn-009f6904) · [`009f6918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f68e4.md#insn-009f6918) · [`009f692c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f68e4.md#insn-009f692c)

~~~diff
- 009f6768 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 009f6768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f6768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f6768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f6904 ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 009f6904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f6904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f6904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f6768 bytes 08a10391
+ 009f6904 bytes 08a11391
- 009f677c ["INT_ADD", "register:40f0:8", ["const:9f677c:8", "const:4:8"]]
- 009f677c ["CALL", null, ["callee:00c53d00:8"]]
+ 009f6918 ["INT_ADD", "register:40f0:8", ["const:9f6918:8", "const:4:8"]]
+ 009f6918 ["CALL", null, ["callee:00c53d00:8"]]
- 009f677c bytes 59740994
+ 009f6918 bytes fa740994
- 009f6790 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f6790 ["INT_ADD", "register:40f0:8", ["const:9f6790:8", "const:4:8"]]
- 009f6790 ["CALLIND", null, ["register:0:8"]]
+ 009f692c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f692c ["INT_ADD", "register:40f0:8", ["const:9f692c:8", "const:4:8"]]
+ 009f692c ["CALLIND", null, ["register:0:8"]]
- 009f6790 bytes 00013fd6
+ 009f692c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98f161369f618480da5888eb79fd1094"></a>

### [`009f67f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f67f4.md) → [`009f6990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6990.md) FUN_009f6990

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0046da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da1c.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0046da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da5c.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.76% / 新版 98.76%

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
      "site": "009f6b5c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f69c0",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 18,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f6bd0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f6a34",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "009f6afc",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "uleb128"
      ]
    ],
    [
      "009f6b0c",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "uleb128"
      ]
    ],
    [
      "009f6b54",
      "DATA",
      [
        "storage",
        "003c7968",
        null,
        "uleb128"
      ]
    ]
  ],
  "added": [
    [
      "009f6afc",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[59]"
      ]
    ],
    [
      "009f6b0c",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[59]"
      ]
    ],
    [
      "009f6b54",
      "DATA",
      [
        "storage",
        "003c7968",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f69c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f67f4.md#insn-009f69c0) · [`009f6a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f67f4.md#insn-009f6a34) · [`009f6838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f67f4.md#insn-009f6838)
- 新版 [`009f6b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6990.md#insn-009f6b5c) · [`009f6bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6990.md#insn-009f6bd0) · [`009f69d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6990.md#insn-009f69d4)

~~~diff
- 009f69c0 ["INT_ADD", "register:40f0:8", ["const:9f69c0:8", "const:4:8"]]
- 009f69c0 ["CALL", null, ["ram:47acb4:8"]]
+ 009f6b5c ["INT_ADD", "register:40f0:8", ["const:9f6b5c:8", "const:4:8"]]
+ 009f6b5c ["CALL", null, ["ram:47acf4:8"]]
- 009f69c0 bytes bd10ea97
+ 009f6b5c bytes 6610ea97
- 009f6a34 ["INT_ADD", "register:40f0:8", ["const:9f6a34:8", "const:4:8"]]
- 009f6a34 ["CALL", null, ["ram:47acb4:8"]]
+ 009f6bd0 ["INT_ADD", "register:40f0:8", ["const:9f6bd0:8", "const:4:8"]]
+ 009f6bd0 ["CALL", null, ["ram:47acf4:8"]]
- 009f6a34 bytes a010ea97
+ 009f6bd0 bytes 4910ea97
- 009f6838 ["INT_ADD", "register:40f0:8", ["const:9f6838:8", "const:4:8"]]
- 009f6838 ["CALL", null, ["callee:0046da5c:8"]]
+ 009f69d4 ["INT_ADD", "register:40f0:8", ["const:9f69d4:8", "const:4:8"]]
+ 009f69d4 ["CALL", null, ["callee:0046da5c:8"]]
- 009f6838 bytes 79dce997
+ 009f69d4 bytes 22dce997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe81582c4f324836d40c9894292fcf5e"></a>

### [`009f6a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f6a78.md) → [`009f6c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6c14.md) FUN_009f6c14

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 21件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469028.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md)
- 新版 呼出元 0件  · 呼出先 21件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469068.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f72e8",
      "incomplete_value": true,
      "site": "009f7300",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "009f714c",
      "incomplete_value": true,
      "site": "009f7164",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f72e4",
      "incomplete_value": true,
      "site": "009f7304",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:302000:8"
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
    "old": {
      "definition_site": "009f7148",
      "incomplete_value": true,
      "site": "009f7168",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:302000:8"
              ],
              [
                "leaf",
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f72e4",
      "incomplete_value": true,
      "site": "009f7304",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "009f7148",
      "incomplete_value": true,
      "site": "009f7168",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 39,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f6c54",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "009f6c60",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f6c68",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f6c54",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f6c60",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f6c68",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f6ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f6a78.md#insn-009f6ad8) · [`009f6ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f6a78.md#insn-009f6ab8) · [`009f6ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f6a78.md#insn-009f6ac4)
- 新版 [`009f6c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6c14.md#insn-009f6c74) · [`009f6c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6c14.md#insn-009f6c54) · [`009f6c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6c14.md#insn-009f6c60)

~~~diff
- 009f6ad8 ["INT_ADD", "register:40f0:8", ["const:9f6ad8:8", "const:4:8"]]
- 009f6ad8 ["CALL", null, ["callee:00c58610:8"]]
+ 009f6c74 ["INT_ADD", "register:40f0:8", ["const:9f6c74:8", "const:4:8"]]
+ 009f6c74 ["CALL", null, ["callee:00c58610:8"]]
- 009f6ad8 bytes ce850994
+ 009f6c74 bytes 67860994
- 009f6ab8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
- 009f6ab8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 009f6c54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
+ 009f6c54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 009f6ab8 bytes 08bd42f9
+ 009f6c54 bytes 08bd44f9
- 009f6ac4 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 009f6ac4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009f6ac4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009f6ac4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009f6c60 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 009f6c60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009f6c60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009f6c60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009f6ac4 bytes 21602991
+ 009f6c60 bytes 21603991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34910f6c54c419429e00d690188c067a"></a>

### [`009f72dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f72dc.md) → [`009f7478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7478.md) FUN_009f7478

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`009f7c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f7c44.md) [`009f9d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f9/009f9d44.md) [`009faa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fa/009faa30.md) · 呼出先 14件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00665d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665d24.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`009f7de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7de0.md) [`009f9ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9ee0.md) [`009fabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md) · 呼出先 14件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00665d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665d64.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.56% / 新版 86.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_destination` 14件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "009f7754",
      "incomplete_value": false,
      "site": "009f7754",
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
      "definition_site": "009f75b8",
      "incomplete_value": false,
      "site": "009f75b8",
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
    "ordinal": 28,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "009f7758",
      "incomplete_value": false,
      "site": "009f7758",
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
      "definition_site": "009f75bc",
      "incomplete_value": false,
      "site": "009f75bc",
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
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f7754",
      "incomplete_value": false,
      "site": "009f7758",
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
      "definition_site": "009f75b8",
      "incomplete_value": false,
      "site": "009f75bc",
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
      "009f74ac",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "009f74b8",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f74c0",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f74ac",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f74b8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f74c0",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f72dc.md#insn-009f732c) · [`009f73f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f72dc.md#insn-009f73f8) · [`009f74e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f72dc.md#insn-009f74e4)
- 新版 [`009f74c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7478.md#insn-009f74c8) · [`009f7594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7478.md#insn-009f7594) · [`009f7680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7478.md#insn-009f7680)

~~~diff
- 009f732c ["INT_ADD", "register:40f0:8", ["const:9f732c:8", "const:4:8"]]
- 009f732c ["CALL", null, ["callee:00c58610:8"]]
+ 009f74c8 ["INT_ADD", "register:40f0:8", ["const:9f74c8:8", "const:4:8"]]
+ 009f74c8 ["CALL", null, ["callee:00c58610:8"]]
- 009f732c bytes b9830994
+ 009f74c8 bytes 52840994
- 009f73f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f73f8 ["INT_ADD", "register:40f0:8", ["const:9f73f8:8", "const:4:8"]]
- 009f73f8 ["CALLIND", null, ["register:0:8"]]
+ 009f7594 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f7594 ["INT_ADD", "register:40f0:8", ["const:9f7594:8", "const:4:8"]]
+ 009f7594 ["CALLIND", null, ["register:0:8"]]
- 009f73f8 bytes 00013fd6
+ 009f7594 bytes 00013fd6
- 009f74e4 ["INT_ADD", "register:40f0:8", ["const:9f74e4:8", "const:4:8"]]
- 009f74e4 ["CALL", null, ["callee:0047e60c:8"]]
+ 009f7680 ["INT_ADD", "register:40f0:8", ["const:9f7680:8", "const:4:8"]]
+ 009f7680 ["CALL", null, ["callee:0047e60c:8"]]
- 009f74e4 bytes 3a1cea97
+ 009f7680 bytes e31bea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59ac75ce36f988bf5b2334d674a0db91"></a>

### [`009f79d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f79d8.md) → [`009f7b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7b74.md) FUN_009f7b74

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a03ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03ccc.md) · 呼出先 14件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00468c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c28.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md)
- 新版 呼出元 1件 [`00a03e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e68.md) · 呼出先 14件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c68.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.13% / 新版 96.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "009f7b9c",
      "incomplete_value": true,
      "site": "009f7b9c",
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
      "definition_site": "009f7a00",
      "incomplete_value": true,
      "site": "009f7a00",
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
      "definition_site": "009f7ba4",
      "incomplete_value": false,
      "site": "009f7bb4",
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
    "old": {
      "definition_site": "009f7a08",
      "incomplete_value": false,
      "site": "009f7a18",
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
            "const:a58:8"
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
      "definition_site": "009f7bac",
      "incomplete_value": false,
      "site": "009f7bb4",
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
    "old": {
      "definition_site": "009f7a10",
      "incomplete_value": false,
      "site": "009f7a18",
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
            "const:590:8"
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
      "009f7b98",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "009f7ba4",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f7bac",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f7b98",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f7ba4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f7bac",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f7a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f79d8.md#insn-009f7a18) · [`009f7b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f79d8.md#insn-009f7b10) · [`009f7b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f79d8.md#insn-009f7b9c)
- 新版 [`009f7bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7b74.md#insn-009f7bb4) · [`009f7cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7b74.md#insn-009f7cac) · [`009f7d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7b74.md#insn-009f7d38)

~~~diff
- 009f7a18 ["INT_ADD", "register:40f0:8", ["const:9f7a18:8", "const:4:8"]]
- 009f7a18 ["CALL", null, ["callee:00c58610:8"]]
+ 009f7bb4 ["INT_ADD", "register:40f0:8", ["const:9f7bb4:8", "const:4:8"]]
+ 009f7bb4 ["CALL", null, ["callee:00c58610:8"]]
- 009f7a18 bytes fe810994
+ 009f7bb4 bytes 97820994
- 009f7b10 ["INT_ADD", "register:40f0:8", ["const:9f7b10:8", "const:4:8"]]
- 009f7b10 ["CALL", null, ["ram:46c984:8"]]
+ 009f7cac ["INT_ADD", "register:40f0:8", ["const:9f7cac:8", "const:4:8"]]
+ 009f7cac ["CALL", null, ["ram:46c9c4:8"]]
- 009f7b10 bytes 9dd3e997
+ 009f7cac bytes 46d3e997
- 009f7b9c ["INT_ADD", "register:40f0:8", ["const:9f7b9c:8", "const:4:8"]]
- 009f7b9c ["CALL", null, ["callee:008514f8:8"]]
+ 009f7d38 ["INT_ADD", "register:40f0:8", ["const:9f7d38:8", "const:4:8"]]
+ 009f7d38 ["CALL", null, ["callee:008514f8:8"]]
- 009f7b9c bytes 4766f997
+ 009f7d38 bytes f065f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97589d9f357f7b2d2ed3c56aa4794344"></a>

### [`009f7c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f7c44.md) → [`009f7de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7de0.md) FUN_009f7de0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a05108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05108.md) · 呼出先 33件 [`0046dab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dab4.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00664860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664860.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md)
- 新版 呼出元 1件 [`00a052a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a052a4.md) · 呼出先 33件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.37% / 新版 96.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f7f34",
      "incomplete_value": false,
      "site": "009f7f34",
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
    "old": {
      "definition_site": "009f7d98",
      "incomplete_value": false,
      "site": "009f7d98",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f7fd4",
      "incomplete_value": false,
      "site": "009f7fd4",
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
    "old": {
      "definition_site": "009f7e38",
      "incomplete_value": false,
      "site": "009f7e38",
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
            "const:1a0:8"
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
      "definition_site": "009f801c",
      "incomplete_value": false,
      "site": "009f8024",
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
    "old": {
      "definition_site": "009f7e80",
      "incomplete_value": false,
      "site": "009f7e88",
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
            "const:220:8"
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
      "009f7e14",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "009f7e20",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f7e28",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f7e14",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f7e20",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f7e28",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f7c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f7c44.md#insn-009f7c98) · [`009f7d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f7c44.md#insn-009f7d2c) · [`009f7ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f7c44.md#insn-009f7ec8)
- 新版 [`009f7e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7de0.md#insn-009f7e34) · [`009f7ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7de0.md#insn-009f7ec8) · [`009f8064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7de0.md#insn-009f8064)

~~~diff
- 009f7c98 ["INT_ADD", "register:40f0:8", ["const:9f7c98:8", "const:4:8"]]
- 009f7c98 ["CALL", null, ["callee:00c58610:8"]]
+ 009f7e34 ["INT_ADD", "register:40f0:8", ["const:9f7e34:8", "const:4:8"]]
+ 009f7e34 ["CALL", null, ["callee:00c58610:8"]]
- 009f7c98 bytes 5e810994
+ 009f7e34 bytes f7810994
- 009f7d2c ["INT_ADD", "register:40f0:8", ["const:9f7d2c:8", "const:4:8"]]
- 009f7d2c ["CALL", null, ["ram:664860:8"]]
+ 009f7ec8 ["INT_ADD", "register:40f0:8", ["const:9f7ec8:8", "const:4:8"]]
+ 009f7ec8 ["CALL", null, ["ram:6648a0:8"]]
- 009f7d2c bytes cdb2f197
+ 009f7ec8 bytes 76b2f197
- 009f7ec8 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f7ec8 ["INT_ADD", "register:40f0:8", ["const:9f7ec8:8", "const:4:8"]]
- 009f7ec8 ["CALLIND", null, ["register:0:8"]]
+ 009f8064 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f8064 ["INT_ADD", "register:40f0:8", ["const:9f8064:8", "const:4:8"]]
+ 009f8064 ["CALLIND", null, ["register:0:8"]]
- 009f7ec8 bytes 00013fd6
+ 009f8064 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b8f10d8fb2a88a1af77be1bdd4ad257"></a>

### [`009f8b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f8/009f8b10.md) → [`009f8cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f8/009f8cac.md) FUN_009f8cac

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a0213c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a0213c.md) · 呼出先 20件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md)
- 新版 呼出元 1件 [`00a022d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022d8.md) · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "009f8cf8",
      "incomplete_value": true,
      "site": "009f8cf8",
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
      "definition_site": "009f8b5c",
      "incomplete_value": true,
      "site": "009f8b5c",
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
      "definition_site": "009f8d00",
      "incomplete_value": false,
      "site": "009f8d14",
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
    "old": {
      "definition_site": "009f8b64",
      "incomplete_value": false,
      "site": "009f8b78",
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
            "const:a58:8"
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
      "definition_site": "009f8d08",
      "incomplete_value": false,
      "site": "009f8d14",
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
    "old": {
      "definition_site": "009f8b6c",
      "incomplete_value": false,
      "site": "009f8b78",
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
            "const:590:8"
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
      "009f8cf4",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "009f8d00",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f8d08",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f8cf4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f8d00",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f8d08",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f8b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f8/009f8b10.md#insn-009f8b78) · [`009f8c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f8/009f8b10.md#insn-009f8c74) · [`009f8c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f8/009f8b10.md#insn-009f8c80)
- 新版 [`009f8d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f8/009f8cac.md#insn-009f8d14) · [`009f8e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f8/009f8cac.md#insn-009f8e10) · [`009f8e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f8/009f8cac.md#insn-009f8e1c)

~~~diff
- 009f8b78 ["INT_ADD", "register:40f0:8", ["const:9f8b78:8", "const:4:8"]]
- 009f8b78 ["CALL", null, ["callee:00c58610:8"]]
+ 009f8d14 ["INT_ADD", "register:40f0:8", ["const:9f8d14:8", "const:4:8"]]
+ 009f8d14 ["CALL", null, ["callee:00c58610:8"]]
- 009f8b78 bytes a67d0994
+ 009f8d14 bytes 3f7e0994
- 009f8c74 ["INT_ADD", "register:40f0:8", ["const:9f8c74:8", "const:4:8"]]
- 009f8c74 ["CALL", null, ["ram:6cba34:8"]]
+ 009f8e10 ["INT_ADD", "register:40f0:8", ["const:9f8e10:8", "const:4:8"]]
+ 009f8e10 ["CALL", null, ["ram:6cba74:8"]]
- 009f8c74 bytes 704bf397
+ 009f8e10 bytes 194bf397
- 009f8c80 ["INT_ADD", "register:40f0:8", ["const:9f8c80:8", "const:4:8"]]
- 009f8c80 ["CALL", null, ["ram:6ccb38:8"]]
+ 009f8e1c ["INT_ADD", "register:40f0:8", ["const:9f8e1c:8", "const:4:8"]]
+ 009f8e1c ["CALL", null, ["ram:6ccb78:8"]]
- 009f8c80 bytes ae4ff397
+ 009f8e1c bytes 574ff397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc1fc33a0661c07c6f0773876c3d2d55"></a>

### [`009f912c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f9/009f912c.md) → [`009f92c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f92c8.md) FUN_009f92c8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009faa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fa/009faa30.md) · 呼出先 20件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0060dd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060d/0060dd80.md) [`00664860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664860.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`009df498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df498.md)
- 新版 呼出元 1件 [`009fabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md) · 呼出先 20件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0060ddc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060d/0060ddc0.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`009df634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df634.md)

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
      "site": "009f956c",
      "value": [
        "leaf",
        "ram:6648a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f93d0",
      "value": [
        "leaf",
        "ram:664860:8"
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
      "009f93b8",
      "READ",
      [
        "storage",
        "00c9b120",
        null,
        "pointer"
      ]
    ],
    [
      "009f93c0",
      "PARAM",
      [
        "storage",
        "00310461",
        "_ZSt7nothrow",
        "undefined1"
      ]
    ],
    [
      "009f9474",
      "PARAM",
      [
        "storage",
        "002bc77e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009f93b8",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ],
    [
      "009f93c0",
      "PARAM",
      [
        "storage",
        "003104a1",
        "_ZSt7nothrow",
        "undefined1"
      ]
    ],
    [
      "009f9474",
      "PARAM",
      [
        "storage",
        "002bc7be",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f93d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f9/009f912c.md#insn-009f93d0) · [`009f9164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f9/009f912c.md#insn-009f9164) · [`009f9174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f9/009f912c.md#insn-009f9174)
- 新版 [`009f956c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f92c8.md#insn-009f956c) · [`009f9300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f92c8.md#insn-009f9300) · [`009f9310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f92c8.md#insn-009f9310)

~~~diff
- 009f93d0 ["INT_ADD", "register:40f0:8", ["const:9f93d0:8", "const:4:8"]]
- 009f93d0 ["CALL", null, ["ram:664860:8"]]
+ 009f956c ["INT_ADD", "register:40f0:8", ["const:9f956c:8", "const:4:8"]]
+ 009f956c ["CALL", null, ["ram:6648a0:8"]]
- 009f93d0 bytes 24adf197
+ 009f956c bytes cdacf197
- 009f9164 ["INT_ADD", "register:40f0:8", ["const:9f9164:8", "const:4:8"]]
- 009f9164 ["CALL", null, ["callee:008514f8:8"]]
+ 009f9300 ["INT_ADD", "register:40f0:8", ["const:9f9300:8", "const:4:8"]]
+ 009f9300 ["CALL", null, ["callee:008514f8:8"]]
- 009f9164 bytes d560f997
+ 009f9300 bytes 7e60f997
- 009f9174 ["INT_ADD", "register:40f0:8", ["const:9f9174:8", "const:4:8"]]
- 009f9174 ["CALL", null, ["callee:009e2f94:8"]]
+ 009f9310 ["INT_ADD", "register:40f0:8", ["const:9f9310:8", "const:4:8"]]
+ 009f9310 ["CALL", null, ["callee:009e2f94:8"]]
- 009f9174 bytes 21a7ff97
+ 009f9310 bytes 21a7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25cfb54ec0c0bbe008ed50400bfac059"></a>

### [`009f9d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f9/009f9d44.md) → [`009f9ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9ee0.md) FUN_009f9ee0

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a02a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02a4c.md) · 呼出先 39件 [`0046dab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dab4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md)
- 新版 呼出元 1件 [`00a02be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md) · 呼出先 39件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md)

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
    "old": {
      "definition_site": "009f9e18",
      "incomplete_value": true,
      "site": "009f9e28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4cd:8"
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
    "old": {
      "definition_site": "009f9e2c",
      "incomplete_value": true,
      "site": "009f9e2c",
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
    "old": {
      "definition_site": "009f9e20",
      "incomplete_value": true,
      "site": "009f9e30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:410:8"
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
      "009f9f20",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "009f9f2c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f9f34",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f9f20",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f9f2c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f9f34",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f9da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f9/009f9d44.md#insn-009f9da4) · [`009f9e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f9/009f9d44.md#insn-009f9e40) · [`009f9f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f9/009f9d44.md#insn-009f9f9c)
- 新版 [`009f9f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9ee0.md#insn-009f9f40) · [`009f9fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9ee0.md#insn-009f9fdc) · [`009fa138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9ee0.md#insn-009fa138)

~~~diff
- 009f9da4 ["INT_ADD", "register:40f0:8", ["const:9f9da4:8", "const:4:8"]]
- 009f9da4 ["CALL", null, ["callee:00c58610:8"]]
+ 009f9f40 ["INT_ADD", "register:40f0:8", ["const:9f9f40:8", "const:4:8"]]
+ 009f9f40 ["CALL", null, ["callee:00c58610:8"]]
- 009f9da4 bytes 1b790994
+ 009f9f40 bytes b4790994
- 009f9e40 ["INT_ADD", "register:40f0:8", ["const:9f9e40:8", "const:4:8"]]
- 009f9e40 ["CALL", null, ["callee:0048ce54:8"]]
+ 009f9fdc ["INT_ADD", "register:40f0:8", ["const:9f9fdc:8", "const:4:8"]]
+ 009f9fdc ["CALL", null, ["callee:0048ce54:8"]]
- 009f9e40 bytes f54bea97
+ 009f9fdc bytes 9e4bea97
- 009f9f9c ["COPY", "register:0:8", ["register:4040:8"]]
- 009f9f9c ["INT_ADD", "register:40f0:8", ["const:9f9f9c:8", "const:4:8"]]
- 009f9f9c ["CALLIND", null, ["register:0:8"]]
+ 009fa138 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009fa138 ["INT_ADD", "register:40f0:8", ["const:9fa138:8", "const:4:8"]]
+ 009fa138 ["CALLIND", null, ["register:0:8"]]
- 009f9f9c bytes 00013fd6
+ 009fa138 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f677a4d3044c86df87fd7f09d336a42d"></a>

### [`009faa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fa/009faa30.md) → [`009fabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md) FUN_009fabcc

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`007f3668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3668.md) [`009fdab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fdab4.md) [`00a01158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01158.md) [`00a05720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05720.md) · 呼出先 40件 [`0046dab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dab4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 4件 [`007f36a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f36a8.md) [`009fdc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc50.md) [`00a012f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012f4.md) [`00a058bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a058bc.md) · 呼出先 40件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

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
    "old": {
      "definition_site": "009fac18",
      "incomplete_value": false,
      "site": "009fac18",
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
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "009fadf0",
      "incomplete_value": false,
      "site": "009fadf0",
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
            "const:820:8"
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
    "old": {
      "definition_site": "009fae44",
      "incomplete_value": false,
      "site": "009fae44",
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
            "const:8a0:8"
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
      "009fac04",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "009fac10",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009fac18",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009fac04",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009fac10",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009fac18",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009faa7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fa/009faa30.md#insn-009faa7c) · [`009faa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fa/009faa30.md#insn-009faa88) · [`009faba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fa/009faa30.md#insn-009faba0)
- 新版 [`009fac18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md#insn-009fac18) · [`009fac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md#insn-009fac24) · [`009fad3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md#insn-009fad3c)

~~~diff
- 009faa7c ["COPY", "tmp:0:8", ["const:590:8"]]
- 009faa7c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 009faa7c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 009faa7c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 009fac18 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 009fac18 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 009fac18 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 009fac18 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 009faa7c bytes 42401691
+ 009fac18 bytes 42402691
- 009faa88 ["INT_ADD", "register:40f0:8", ["const:9faa88:8", "const:4:8"]]
- 009faa88 ["CALL", null, ["callee:00c58610:8"]]
+ 009fac24 ["INT_ADD", "register:40f0:8", ["const:9fac24:8", "const:4:8"]]
+ 009fac24 ["CALL", null, ["callee:00c58610:8"]]
- 009faa88 bytes e2750994
+ 009fac24 bytes 7b760994
- 009faba0 ["INT_ADD", "register:40f0:8", ["const:9faba0:8", "const:4:8"]]
- 009faba0 ["CALL", null, ["callee:0047e60c:8"]]
+ 009fad3c ["INT_ADD", "register:40f0:8", ["const:9fad3c:8", "const:4:8"]]
+ 009fad3c ["CALL", null, ["callee:0047e60c:8"]]
- 009faba0 bytes 8b0eea97
+ 009fad3c bytes 340eea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b234c4ce9c86965943d0520db6afdf5d"></a>

### [`009fb2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fb/009fb2b0.md) → [`009fb44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md) FUN_009fb44c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 54件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046dab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dab4.md) [`00470954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 54件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.49% / 新版 95.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `call_target` 2件, `store_value` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "009fb36c",
      "incomplete_value": true,
      "site": "009fb37c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:410:8"
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
    "old": {
      "definition_site": "009fb370",
      "incomplete_value": true,
      "site": "009fb380",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:600:8"
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
    "old": {
      "definition_site": "009fb384",
      "incomplete_value": true,
      "site": "009fb384",
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
      "009fb508",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ],
    [
      "009fb50c",
      "READ",
      [
        "storage",
        "002b5600",
        null,
        "string"
      ]
    ],
    [
      "009fb510",
      "READ",
      [
        "storage",
        "002b560f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009fb508",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ],
    [
      "009fb50c",
      "READ",
      [
        "storage",
        "002b5640",
        null,
        "string"
      ]
    ],
    [
      "009fb510",
      "READ",
      [
        "storage",
        "002b564f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fb510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fb/009fb2b0.md#insn-009fb510) · [`009fb538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fb/009fb2b0.md#insn-009fb538) · [`009fb5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fb/009fb2b0.md#insn-009fb5f4)
- 新版 [`009fb6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md#insn-009fb6ac) · [`009fb6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md#insn-009fb6d4) · [`009fb790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md#insn-009fb790)

~~~diff
- 009fb510 ["INT_ADD", "register:40f0:8", ["const:9fb510:8", "const:4:8"]]
- 009fb510 ["CALL", null, ["callee:00c57f60:8"]]
+ 009fb6ac ["INT_ADD", "register:40f0:8", ["const:9fb6ac:8", "const:4:8"]]
+ 009fb6ac ["CALL", null, ["callee:00c57f60:8"]]
- 009fb510 bytes 94710994
+ 009fb6ac bytes 2d720994
- 009fb538 ["INT_ADD", "register:40f0:8", ["const:9fb538:8", "const:4:8"]]
- 009fb538 ["CALL", null, ["callee:00c57f70:8"]]
+ 009fb6d4 ["INT_ADD", "register:40f0:8", ["const:9fb6d4:8", "const:4:8"]]
+ 009fb6d4 ["CALL", null, ["callee:00c57f70:8"]]
- 009fb538 bytes 8e710994
+ 009fb6d4 bytes 27720994
- 009fb5f4 ["INT_ADD", "register:40f0:8", ["const:9fb5f4:8", "const:4:8"]]
- 009fb5f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 009fb790 ["INT_ADD", "register:40f0:8", ["const:9fb790:8", "const:4:8"]]
+ 009fb790 ["CALL", null, ["callee:00c57eb0:8"]]
- 009fb5f4 bytes 2f710994
+ 009fb790 bytes c8710994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e647a836bb2dbcaf8c1e46bb543871d9"></a>

### [`009fcbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fc/009fcbec.md) → [`009fcd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcd88.md) FUN_009fcd88

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
      "definition_site": "009fcc10",
      "incomplete_value": false,
      "site": "009fcc18",
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
      "009fcdb4",
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
      "009fcdb4",
      "DATA",
      [
        "storage",
        "00c8a480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fcc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fc/009fcbec.md#insn-009fcc10) · [`009fcc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fc/009fcbec.md#insn-009fcc48)
- 新版 [`009fcdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcd88.md#insn-009fcdac) · [`009fcde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcd88.md#insn-009fcde4)

~~~diff
- 009fcc10 ["COPY", "tmp:0:8", ["const:80:8"]]
- 009fcc10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fcc10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fcc10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fcdac ["COPY", "tmp:0:8", ["const:480:8"]]
+ 009fcdac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fcdac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fcdac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fcc10 bytes 08010291
+ 009fcdac bytes 08011291
- 009fcc48 ["COPY", "register:0:8", ["register:4040:8"]]
- 009fcc48 ["INT_ADD", "register:40f0:8", ["const:9fcc48:8", "const:4:8"]]
- 009fcc48 ["CALLIND", null, ["register:0:8"]]
+ 009fcde4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009fcde4 ["INT_ADD", "register:40f0:8", ["const:9fcde4:8", "const:4:8"]]
+ 009fcde4 ["CALLIND", null, ["register:0:8"]]
- 009fcc48 bytes 00013fd6
+ 009fcde4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2acc4cdc19779185eeabe3b62164fa9a"></a>

### [`009fcfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fc/009fcfec.md) → [`009fd188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd188.md) FUN_009fd188

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "009fd000",
      "incomplete_value": false,
      "site": "009fd004",
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
            "const:120:8"
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
      "009fd1a0",
      "DATA",
      [
        "storage",
        "00c8a120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fd1a0",
      "DATA",
      [
        "storage",
        "00c8a520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fcff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fc/009fcfec.md#insn-009fcff8) · [`009fd000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fc/009fcfec.md#insn-009fd000)
- 新版 [`009fd194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd188.md#insn-009fd194) · [`009fd19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd188.md#insn-009fd19c)

~~~diff
- 009fcff8 ["INT_ADD", "register:40f0:8", ["const:9fcff8:8", "const:4:8"]]
- 009fcff8 ["CALL", null, ["callee:00c57e90:8"]]
+ 009fd194 ["INT_ADD", "register:40f0:8", ["const:9fd194:8", "const:4:8"]]
+ 009fd194 ["CALL", null, ["callee:00c57e90:8"]]
- 009fcff8 bytes a66a0994
+ 009fd194 bytes 3f6b0994
- 009fd000 ["COPY", "tmp:0:8", ["const:120:8"]]
- 009fd000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fd000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fd000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fd19c ["COPY", "tmp:0:8", ["const:520:8"]]
+ 009fd19c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd19c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd19c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fd000 bytes 08810491
+ 009fd19c bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d1b6550086dc27fccfdcfdc98fe65c7"></a>

### [`009fd010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd010.md) → [`009fd1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd1ac.md) FUN_009fd1ac

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "009fd014",
      "incomplete_value": false,
      "site": "009fd018",
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
      "009fd1b4",
      "DATA",
      [
        "storage",
        "00c8a120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fd1b4",
      "DATA",
      [
        "storage",
        "00c8a520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd010.md#insn-009fd014)
- 新版 [`009fd1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd1ac.md#insn-009fd1b0)

~~~diff
- 009fd014 ["COPY", "tmp:0:8", ["const:120:8"]]
- 009fd014 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fd014 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fd014 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fd1b0 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 009fd1b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd1b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd1b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fd014 bytes 08810491
+ 009fd1b0 bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fad6fabbfde20f77b56ee8ae8e1076a6"></a>

### [`009fd09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd09c.md) → [`009fd238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd238.md) FUN_009fd238

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "009fd0bc",
      "incomplete_value": false,
      "site": "009fd0c0",
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
      "009fd25c",
      "DATA",
      [
        "storage",
        "00c8a1a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fd25c",
      "DATA",
      [
        "storage",
        "00c8a5a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd09c.md#insn-009fd0b0) · [`009fd0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd09c.md#insn-009fd0bc)
- 新版 [`009fd24c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd238.md#insn-009fd24c) · [`009fd258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd238.md#insn-009fd258)

~~~diff
- 009fd0b0 ["INT_ADD", "register:40f0:8", ["const:9fd0b0:8", "const:4:8"]]
- 009fd0b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 009fd24c ["INT_ADD", "register:40f0:8", ["const:9fd24c:8", "const:4:8"]]
+ 009fd24c ["CALL", null, ["callee:00c57e90:8"]]
- 009fd0b0 bytes 786a0994
+ 009fd24c bytes 116b0994
- 009fd0bc ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 009fd0bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fd0bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fd0bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fd258 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 009fd258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fd0bc bytes 08810691
+ 009fd258 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ebe5c554620116b38d5ba38f0726bca"></a>

### [`009fd0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd0d4.md) → [`009fd270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd270.md) FUN_009fd270

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "009fd0d8",
      "incomplete_value": false,
      "site": "009fd0dc",
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
      "009fd278",
      "DATA",
      [
        "storage",
        "00c8a1a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fd278",
      "DATA",
      [
        "storage",
        "00c8a5a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd0d4.md#insn-009fd0d8)
- 新版 [`009fd274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd270.md#insn-009fd274)

~~~diff
- 009fd0d8 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 009fd0d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fd0d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fd0d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fd274 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 009fd274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fd0d8 bytes 08810691
+ 009fd274 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71e09ea82a969717da14e8833510c33c"></a>

### [`009fd0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd0f4.md) → [`009fd290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd290.md) FUN_009fd290

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00664860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664860.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00859b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b0c.md) [`008b6a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6a18.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00859b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b4c.md) [`008b6a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6a5c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.38% / 新版 98.38%

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
      "site": "009fd3f0",
      "value": [
        "leaf",
        "ram:6648a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fd254",
      "value": [
        "leaf",
        "ram:664860:8"
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
      "site": "009fd4a0",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fd304",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 21,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fd4d0",
      "value": [
        "leaf",
        "ram:adf218:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fd334",
      "value": [
        "leaf",
        "ram:adf01c:8"
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
      "009fd3f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664860"
      ]
    ],
    [
      "009fd4a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "009fd4d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00adf01c"
      ]
    ]
  ],
  "added": [
    [
      "009fd3f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648a0"
      ]
    ],
    [
      "009fd4a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "009fd4d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00adf218"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd0f4.md#insn-009fd254) · [`009fd304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd0f4.md#insn-009fd304) · [`009fd334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd0f4.md#insn-009fd334)
- 新版 [`009fd3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd290.md#insn-009fd3f0) · [`009fd4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd290.md#insn-009fd4a0) · [`009fd4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd290.md#insn-009fd4d0)

~~~diff
- 009fd254 ["INT_ADD", "register:40f0:8", ["const:9fd254:8", "const:4:8"]]
- 009fd254 ["CALL", null, ["ram:664860:8"]]
+ 009fd3f0 ["INT_ADD", "register:40f0:8", ["const:9fd3f0:8", "const:4:8"]]
+ 009fd3f0 ["CALL", null, ["ram:6648a0:8"]]
- 009fd254 bytes 839df197
+ 009fd3f0 bytes 2c9df197
- 009fd304 ["INT_ADD", "register:40f0:8", ["const:9fd304:8", "const:4:8"]]
- 009fd304 ["CALL", null, ["ram:46c984:8"]]
+ 009fd4a0 ["INT_ADD", "register:40f0:8", ["const:9fd4a0:8", "const:4:8"]]
+ 009fd4a0 ["CALL", null, ["ram:46c9c4:8"]]
- 009fd304 bytes a0bde997
+ 009fd4a0 bytes 49bde997
- 009fd334 ["INT_ADD", "register:40f0:8", ["const:9fd334:8", "const:4:8"]]
- 009fd334 ["CALL", null, ["ram:adf01c:8"]]
+ 009fd4d0 ["INT_ADD", "register:40f0:8", ["const:9fd4d0:8", "const:4:8"]]
+ 009fd4d0 ["CALL", null, ["ram:adf218:8"]]
- 009fd334 bytes 3a870394
+ 009fd4d0 bytes 52870394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-094f769fa4ca1f56f06a392d4756f044"></a>

### [`009fd438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd438.md) → [`009fd5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd5d4.md) FUN_009fd5d4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "009fd458",
      "incomplete_value": false,
      "site": "009fd45c",
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
            "const:220:8"
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
      "009fd5f8",
      "DATA",
      [
        "storage",
        "00c8a220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fd5f8",
      "DATA",
      [
        "storage",
        "00c8a620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd438.md#insn-009fd44c) · [`009fd458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd438.md#insn-009fd458)
- 新版 [`009fd5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd5d4.md#insn-009fd5e8) · [`009fd5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd5d4.md#insn-009fd5f4)

~~~diff
- 009fd44c ["INT_ADD", "register:40f0:8", ["const:9fd44c:8", "const:4:8"]]
- 009fd44c ["CALL", null, ["callee:00c57e90:8"]]
+ 009fd5e8 ["INT_ADD", "register:40f0:8", ["const:9fd5e8:8", "const:4:8"]]
+ 009fd5e8 ["CALL", null, ["callee:00c57e90:8"]]
- 009fd44c bytes 91690994
+ 009fd5e8 bytes 2a6a0994
- 009fd458 ["COPY", "tmp:0:8", ["const:220:8"]]
- 009fd458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fd458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fd458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fd5f4 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 009fd5f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd5f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd5f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fd458 bytes 08810891
+ 009fd5f4 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-213c0bf6bb7385edcf9be3d5af90655d"></a>

### [`009fd470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd470.md) → [`009fd60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd60c.md) FUN_009fd60c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "009fd474",
      "incomplete_value": false,
      "site": "009fd478",
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
            "const:220:8"
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
      "009fd614",
      "DATA",
      [
        "storage",
        "00c8a220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fd614",
      "DATA",
      [
        "storage",
        "00c8a620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd470.md#insn-009fd474)
- 新版 [`009fd610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd60c.md#insn-009fd610)

~~~diff
- 009fd474 ["COPY", "tmp:0:8", ["const:220:8"]]
- 009fd474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fd474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fd474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fd610 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 009fd610 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd610 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fd610 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fd474 bytes 08810891
+ 009fd610 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e168f22daff4f03f9c0078000eeacdbe"></a>

### [`009fd490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd490.md) → [`009fd62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd62c.md) FUN_009fd62c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md) [`0046aed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aed8.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) [`0046af18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af18.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.74% / 新版 97.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "009fd4f8",
      "incomplete_value": true,
      "site": "009fd4f8",
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
    "old": {
      "definition_site": "009fd508",
      "incomplete_value": true,
      "site": "009fd510",
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
            "const:590:8"
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
      "site": "009fd978",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fd7dc",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 24,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009fd690",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "009fd69c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009fd6a4",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009fd690",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009fd69c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009fd6a4",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd490.md#insn-009fd510) · [`009fd7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd490.md#insn-009fd7dc) · [`009fd804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd490.md#insn-009fd804)
- 新版 [`009fd6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd62c.md#insn-009fd6ac) · [`009fd978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd62c.md#insn-009fd978) · [`009fd9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd62c.md#insn-009fd9a0)

~~~diff
- 009fd510 ["INT_ADD", "register:40f0:8", ["const:9fd510:8", "const:4:8"]]
- 009fd510 ["CALL", null, ["callee:00c58610:8"]]
+ 009fd6ac ["INT_ADD", "register:40f0:8", ["const:9fd6ac:8", "const:4:8"]]
+ 009fd6ac ["CALL", null, ["callee:00c58610:8"]]
- 009fd510 bytes 406b0994
+ 009fd6ac bytes d96b0994
- 009fd7dc ["INT_ADD", "register:40f0:8", ["const:9fd7dc:8", "const:4:8"]]
- 009fd7dc ["CALL", null, ["ram:46c984:8"]]
+ 009fd978 ["INT_ADD", "register:40f0:8", ["const:9fd978:8", "const:4:8"]]
+ 009fd978 ["CALL", null, ["ram:46c9c4:8"]]
- 009fd7dc bytes 6abce997
+ 009fd978 bytes 13bce997
- 009fd804 ["INT_ADD", "register:40f0:8", ["const:9fd804:8", "const:4:8"]]
- 009fd804 ["CALL", null, ["ram:9f77f4:8"]]
+ 009fd9a0 ["INT_ADD", "register:40f0:8", ["const:9fd9a0:8", "const:4:8"]]
+ 009fd9a0 ["CALL", null, ["ram:9f7990:8"]]
- 009fd804 bytes fce7ff97
+ 009fd9a0 bytes fce7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c6074e476d1c15a5d8831ffb77cf912"></a>

### [`009fd994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd994.md) → [`009fdb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb30.md) FUN_009fdb30

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "009fd9b8",
      "incomplete_value": false,
      "site": "009fd9b8",
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
      "009fdb54",
      "DATA",
      [
        "storage",
        "00c8a2a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fdb54",
      "DATA",
      [
        "storage",
        "00c8a6a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd994.md#insn-009fd9a8) · [`009fd9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd994.md#insn-009fd9b4)
- 新版 [`009fdb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb30.md#insn-009fdb44) · [`009fdb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb30.md#insn-009fdb50)

~~~diff
- 009fd9a8 ["INT_ADD", "register:40f0:8", ["const:9fd9a8:8", "const:4:8"]]
- 009fd9a8 ["CALL", null, ["callee:00c57e90:8"]]
+ 009fdb44 ["INT_ADD", "register:40f0:8", ["const:9fdb44:8", "const:4:8"]]
+ 009fdb44 ["CALL", null, ["callee:00c57e90:8"]]
- 009fd9a8 bytes 3a680994
+ 009fdb44 bytes d3680994
- 009fd9b4 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 009fd9b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fd9b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fd9b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fdb50 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 009fdb50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fdb50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fdb50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fd9b4 bytes 08810a91
+ 009fdb50 bytes 08811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83a48f132fe83a18a2bfcaa360fdf41f"></a>

### [`009fd9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd9c8.md) → [`009fdb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb64.md) FUN_009fdb64

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "old": {
      "definition_site": "009fd9d4",
      "incomplete_value": true,
      "site": "009fd9d4",
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
      "009fdb70",
      "DATA",
      [
        "storage",
        "00c8a2a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fdb70",
      "DATA",
      [
        "storage",
        "00c8a6a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fd9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd9c8.md#insn-009fd9d0)
- 新版 [`009fdb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb64.md#insn-009fdb6c)

~~~diff
- 009fd9d0 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 009fd9d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009fd9d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009fd9d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009fdb6c ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 009fdb6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009fdb6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009fdb6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009fd9d0 bytes 29810a91
+ 009fdb6c bytes 29811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75ac5589fac53405ca8c9fa1b3a55bd3"></a>

### [`009fd9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd9e4.md) → [`009fdb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb80.md) FUN_009fdb80

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "009fdba0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fda04",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "009fdbac",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fda10",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "009fdba0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "009fdbac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "009fdba0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "009fdbac",
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

- 旧版 [`009fda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd9e4.md#insn-009fda04) · [`009fda10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd9e4.md#insn-009fda10)
- 新版 [`009fdba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb80.md#insn-009fdba0) · [`009fdbac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdb80.md#insn-009fdbac)

~~~diff
- 009fda04 ["INT_ADD", "register:40f0:8", ["const:9fda04:8", "const:4:8"]]
- 009fda04 ["CALL", null, ["ram:47acb4:8"]]
+ 009fdba0 ["INT_ADD", "register:40f0:8", ["const:9fdba0:8", "const:4:8"]]
+ 009fdba0 ["CALL", null, ["ram:47acf4:8"]]
- 009fda04 bytes acf4e997
+ 009fdba0 bytes 55f4e997
- 009fda10 ["INT_ADD", "register:40f0:8", ["const:9fda10:8", "const:4:8"]]
- 009fda10 ["CALL", null, ["ram:47acb4:8"]]
+ 009fdbac ["INT_ADD", "register:40f0:8", ["const:9fdbac:8", "const:4:8"]]
+ 009fdbac ["CALL", null, ["ram:47acf4:8"]]
- 009fda10 bytes a9f4e997
+ 009fdbac bytes 52f4e997
~~~


<a id="compare-22cd384009bba69dc3efc0a14b1e4adb"></a>

### [`009fda64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fda64.md) → [`009fdc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc00.md) FUN_009fdc00

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "009fda88",
      "incomplete_value": false,
      "site": "009fda88",
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
      "009fdc24",
      "DATA",
      [
        "storage",
        "00c8a320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fdc24",
      "DATA",
      [
        "storage",
        "00c8a720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fda78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fda64.md#insn-009fda78) · [`009fda84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fda64.md#insn-009fda84)
- 新版 [`009fdc14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc00.md#insn-009fdc14) · [`009fdc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc00.md#insn-009fdc20)

~~~diff
- 009fda78 ["INT_ADD", "register:40f0:8", ["const:9fda78:8", "const:4:8"]]
- 009fda78 ["CALL", null, ["callee:00c57e90:8"]]
+ 009fdc14 ["INT_ADD", "register:40f0:8", ["const:9fdc14:8", "const:4:8"]]
+ 009fdc14 ["CALL", null, ["callee:00c57e90:8"]]
- 009fda78 bytes 06680994
+ 009fdc14 bytes 9f680994
- 009fda84 ["COPY", "tmp:0:8", ["const:320:8"]]
- 009fda84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fda84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fda84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fdc20 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 009fdc20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fdc20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fdc20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fda84 bytes 08810c91
+ 009fdc20 bytes 08811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3deae30ad8b31d23cad7c946703d1cc5"></a>

### [`009fda98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fda98.md) → [`009fdc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc34.md) FUN_009fdc34

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "009fdaa4",
      "incomplete_value": false,
      "site": "009fdaa4",
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
      "009fdc40",
      "DATA",
      [
        "storage",
        "00c8a320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fdc40",
      "DATA",
      [
        "storage",
        "00c8a720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fdaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fda98.md#insn-009fdaa0)
- 新版 [`009fdc3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc34.md#insn-009fdc3c)

~~~diff
- 009fdaa0 ["COPY", "tmp:0:8", ["const:320:8"]]
- 009fdaa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009fdaa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009fdaa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009fdc3c ["COPY", "tmp:0:8", ["const:720:8"]]
+ 009fdc3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009fdc3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009fdc3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009fdaa0 bytes 29810c91
+ 009fdc3c bytes 29811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3dd1014e6859a0356ace9cc793e35d1"></a>

### [`009fdab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fdab4.md) → [`009fdc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc50.md) FUN_009fdc50

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`009faa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fa/009faa30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`009fabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md)

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
      "site": "009fdc70",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fdad4",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "009fdc7c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fdae0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "009fdc70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "009fdc7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "009fdc70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "009fdc7c",
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

- 旧版 [`009fdad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fdab4.md#insn-009fdad4) · [`009fdae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fdab4.md#insn-009fdae0)
- 新版 [`009fdc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc50.md#insn-009fdc70) · [`009fdc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdc50.md#insn-009fdc7c)

~~~diff
- 009fdad4 ["INT_ADD", "register:40f0:8", ["const:9fdad4:8", "const:4:8"]]
- 009fdad4 ["CALL", null, ["ram:47acb4:8"]]
+ 009fdc70 ["INT_ADD", "register:40f0:8", ["const:9fdc70:8", "const:4:8"]]
+ 009fdc70 ["CALL", null, ["ram:47acf4:8"]]
- 009fdad4 bytes 78f4e997
+ 009fdc70 bytes 21f4e997
- 009fdae0 ["INT_ADD", "register:40f0:8", ["const:9fdae0:8", "const:4:8"]]
- 009fdae0 ["CALL", null, ["ram:47acb4:8"]]
+ 009fdc7c ["INT_ADD", "register:40f0:8", ["const:9fdc7c:8", "const:4:8"]]
+ 009fdc7c ["CALL", null, ["ram:47acf4:8"]]
- 009fdae0 bytes 75f4e997
+ 009fdc7c bytes 1ef4e997
~~~


<a id="compare-71acf8e3968aaf10257baa688bb03540"></a>

### [`009ff01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff01c.md) → [`009ff1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff1b8.md) FUN_009ff1b8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "009ff028",
      "incomplete_value": false,
      "site": "009ff034",
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
      "009ff1d0",
      "DATA",
      [
        "storage",
        "00c8a3a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ff1d0",
      "DATA",
      [
        "storage",
        "00c8a7a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ff028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff01c.md#insn-009ff028)
- 新版 [`009ff1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff1b8.md#insn-009ff1c4)

~~~diff
- 009ff028 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 009ff028 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009ff028 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009ff028 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009ff1c4 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 009ff1c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009ff1c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009ff1c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009ff028 bytes 4a810e91
+ 009ff1c4 bytes 4a811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3905aac5f9d485a06b004ded41ec0d9f"></a>

### [`009ff060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff060.md) → [`009ff1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff1fc.md) FUN_009ff1fc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "009ff078",
      "incomplete_value": false,
      "site": "009ff084",
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
      "009ff220",
      "DATA",
      [
        "storage",
        "00c8a3a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ff220",
      "DATA",
      [
        "storage",
        "00c8a7a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ff078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff060.md#insn-009ff078) · [`009ff0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff060.md#insn-009ff0a8)
- 新版 [`009ff214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff1fc.md#insn-009ff214) · [`009ff244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff1fc.md#insn-009ff244)

~~~diff
- 009ff078 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 009ff078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ff078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ff078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ff214 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 009ff214 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ff214 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ff214 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ff078 bytes 08810e91
+ 009ff214 bytes 08811e91
- 009ff0a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ff0a8 ["INT_ADD", "register:40f0:8", ["const:9ff0a8:8", "const:4:8"]]
- 009ff0a8 ["CALLIND", null, ["register:0:8"]]
+ 009ff244 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ff244 ["INT_ADD", "register:40f0:8", ["const:9ff244:8", "const:4:8"]]
+ 009ff244 ["CALLIND", null, ["register:0:8"]]
- 009ff0a8 bytes 00013fd6
+ 009ff244 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a75037b4f7c53c1936efd693a49b1602"></a>

### [`009ff0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff0bc.md) → [`009ff258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff258.md) FUN_009ff258

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "009ff0d8",
      "incomplete_value": false,
      "site": "009ff0e8",
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
      "009ff284",
      "DATA",
      [
        "storage",
        "00c8a3a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ff284",
      "DATA",
      [
        "storage",
        "00c8a7a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ff0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff0bc.md#insn-009ff0d0) · [`009ff0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff0bc.md#insn-009ff0d8) · [`009ff110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff0bc.md#insn-009ff110)
- 新版 [`009ff26c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff258.md#insn-009ff26c) · [`009ff274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff258.md#insn-009ff274) · [`009ff2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff258.md#insn-009ff2ac)

~~~diff
- 009ff0d0 ["INT_ADD", "register:40f0:8", ["const:9ff0d0:8", "const:4:8"]]
- 009ff0d0 ["CALL", null, ["callee:00c57e90:8"]]
+ 009ff26c ["INT_ADD", "register:40f0:8", ["const:9ff26c:8", "const:4:8"]]
+ 009ff26c ["CALL", null, ["callee:00c57e90:8"]]
- 009ff0d0 bytes 70620994
+ 009ff26c bytes 09630994
- 009ff0d8 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 009ff0d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ff0d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ff0d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ff274 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 009ff274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ff274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ff274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ff0d8 bytes 08810e91
+ 009ff274 bytes 08811e91
- 009ff110 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ff110 ["INT_ADD", "register:40f0:8", ["const:9ff110:8", "const:4:8"]]
- 009ff110 ["CALLIND", null, ["register:0:8"]]
+ 009ff2ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ff2ac ["INT_ADD", "register:40f0:8", ["const:9ff2ac:8", "const:4:8"]]
+ 009ff2ac ["CALLIND", null, ["register:0:8"]]
- 009ff110 bytes 00013fd6
+ 009ff2ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0333dbe5eefd09756ef323b409ff428e"></a>

### [`009ff15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff15c.md) → [`009ff2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff2f8.md) FUN_009ff2f8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "009ff16c",
      "incomplete_value": false,
      "site": "009ff174",
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
      "009ff310",
      "DATA",
      [
        "storage",
        "00c8a3a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ff310",
      "DATA",
      [
        "storage",
        "00c8a7a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ff16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff15c.md#insn-009ff16c) · [`009ff1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff15c.md#insn-009ff1a8) · [`009ff1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff15c.md#insn-009ff1d0)
- 新版 [`009ff308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff2f8.md#insn-009ff308) · [`009ff344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff2f8.md#insn-009ff344) · [`009ff36c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff2f8.md#insn-009ff36c)

~~~diff
- 009ff16c ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 009ff16c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ff16c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ff16c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ff308 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 009ff308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ff308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ff308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ff16c bytes 08810e91
+ 009ff308 bytes 08811e91
- 009ff1a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ff1a8 ["INT_ADD", "register:40f0:8", ["const:9ff1a8:8", "const:4:8"]]
- 009ff1a8 ["CALLIND", null, ["register:0:8"]]
+ 009ff344 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ff344 ["INT_ADD", "register:40f0:8", ["const:9ff344:8", "const:4:8"]]
+ 009ff344 ["CALLIND", null, ["register:0:8"]]
- 009ff1a8 bytes 00013fd6
+ 009ff344 bytes 00013fd6
- 009ff1d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ff1d0 ["INT_ADD", "register:40f0:8", ["const:9ff1d0:8", "const:4:8"]]
- 009ff1d0 ["CALLIND", null, ["register:0:8"]]
+ 009ff36c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ff36c ["INT_ADD", "register:40f0:8", ["const:9ff36c:8", "const:4:8"]]
+ 009ff36c ["CALLIND", null, ["register:0:8"]]
- 009ff1d0 bytes 00013fd6
+ 009ff36c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66dede59e6f537874b907c45f293811f"></a>

### [`009ff270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff270.md) → [`009ff40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff40c.md) FUN_009ff40c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 27件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0046dab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dab4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

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
    "old": {
      "definition_site": "009ff3ec",
      "incomplete_value": true,
      "site": "009ff3fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ed8:8"
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
    "old": {
      "definition_site": "009ff400",
      "incomplete_value": true,
      "site": "009ff400",
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
    "old": {
      "definition_site": "009ff3f4",
      "incomplete_value": true,
      "site": "009ff404",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:410:8"
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
      "009ff45c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "009ff484",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "009ff588",
      "READ",
      [
        "storage",
        "002bced8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ff45c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "009ff484",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "009ff588",
      "READ",
      [
        "storage",
        "002bcf18",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ff2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff270.md#insn-009ff2c0) · [`009ff2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff270.md#insn-009ff2e8) · [`009ff43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ff270.md#insn-009ff43c)
- 新版 [`009ff45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff40c.md#insn-009ff45c) · [`009ff484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff40c.md#insn-009ff484) · [`009ff5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff40c.md#insn-009ff5d8)

~~~diff
- 009ff2c0 ["INT_ADD", "register:40f0:8", ["const:9ff2c0:8", "const:4:8"]]
- 009ff2c0 ["CALL", null, ["ram:47acb4:8"]]
+ 009ff45c ["INT_ADD", "register:40f0:8", ["const:9ff45c:8", "const:4:8"]]
+ 009ff45c ["CALL", null, ["ram:47acf4:8"]]
- 009ff2c0 bytes 7deee997
+ 009ff45c bytes 26eee997
- 009ff2e8 ["INT_ADD", "register:40f0:8", ["const:9ff2e8:8", "const:4:8"]]
- 009ff2e8 ["CALL", null, ["ram:47acb4:8"]]
+ 009ff484 ["INT_ADD", "register:40f0:8", ["const:9ff484:8", "const:4:8"]]
+ 009ff484 ["CALL", null, ["ram:47acf4:8"]]
- 009ff2e8 bytes 73eee997
+ 009ff484 bytes 1ceee997
- 009ff43c ["INT_ADD", "register:40f0:8", ["const:9ff43c:8", "const:4:8"]]
- 009ff43c ["CALL", null, ["ram:664860:8"]]
+ 009ff5d8 ["INT_ADD", "register:40f0:8", ["const:9ff5d8:8", "const:4:8"]]
+ 009ff5d8 ["CALL", null, ["ram:6648a0:8"]]
- 009ff43c bytes 0995f197
+ 009ff5d8 bytes b294f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcaffffd3cef769bf582dcad054af6b5"></a>

### [`009ffc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffc18.md) → [`009ffdb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffdb4.md) FUN_009ffdb4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "009ffc24",
      "incomplete_value": false,
      "site": "009ffc30",
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
      "009ffdcc",
      "DATA",
      [
        "storage",
        "00c8a410",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ffdcc",
      "DATA",
      [
        "storage",
        "00c8a810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ffc24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffc18.md#insn-009ffc24)
- 新版 [`009ffdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffdb4.md#insn-009ffdc0)

~~~diff
- 009ffc24 ["COPY", "tmp:0:8", ["const:410:8"]]
- 009ffc24 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009ffc24 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009ffc24 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009ffdc0 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 009ffdc0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009ffdc0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009ffdc0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009ffc24 bytes 4a411091
+ 009ffdc0 bytes 4a412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a46b7bbb0d2f63b88ed0045b80b128f9"></a>

### [`009ffcb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffcb8.md) → [`009ffe54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffe54.md) FUN_009ffe54

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "009ffce4",
      "incomplete_value": false,
      "site": "009ffce4",
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
            "const:410:8"
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
      "009ffe80",
      "DATA",
      [
        "storage",
        "00c8a410",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ffe80",
      "DATA",
      [
        "storage",
        "00c8a810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ffccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffcb8.md#insn-009ffccc) · [`009ffcdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffcb8.md#insn-009ffcdc) · [`009ffd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffcb8.md#insn-009ffd00)
- 新版 [`009ffe68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffe54.md#insn-009ffe68) · [`009ffe78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffe54.md#insn-009ffe78) · [`009ffe9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffe54.md#insn-009ffe9c)

~~~diff
- 009ffccc ["INT_ADD", "register:40f0:8", ["const:9ffccc:8", "const:4:8"]]
- 009ffccc ["CALL", null, ["callee:00c57e90:8"]]
+ 009ffe68 ["INT_ADD", "register:40f0:8", ["const:9ffe68:8", "const:4:8"]]
+ 009ffe68 ["CALL", null, ["callee:00c57e90:8"]]
- 009ffccc bytes 715f0994
+ 009ffe68 bytes 0a600994
- 009ffcdc ["COPY", "tmp:0:8", ["const:410:8"]]
- 009ffcdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ffcdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ffcdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ffe78 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 009ffe78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ffe78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ffe78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ffcdc bytes 08411091
+ 009ffe78 bytes 08412091
- 009ffd00 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ffd00 ["INT_ADD", "register:40f0:8", ["const:9ffd00:8", "const:4:8"]]
- 009ffd00 ["CALLIND", null, ["register:0:8"]]
+ 009ffe9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ffe9c ["INT_ADD", "register:40f0:8", ["const:9ffe9c:8", "const:4:8"]]
+ 009ffe9c ["CALLIND", null, ["register:0:8"]]
- 009ffd00 bytes 00013fd6
+ 009ffe9c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2e02a7bde6ecd20699ab9309c2ae1db"></a>

### [`009ffd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffd50.md) → [`009ffeec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffeec.md) FUN_009ffeec

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "009ffd70",
      "incomplete_value": false,
      "site": "009ffd70",
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
            "const:410:8"
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
      "009fff0c",
      "DATA",
      [
        "storage",
        "00c8a410",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009fff0c",
      "DATA",
      [
        "storage",
        "00c8a810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ffd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffd50.md#insn-009ffd6c) · [`009ffd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffd50.md#insn-009ffd8c) · [`009ffdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffd50.md#insn-009ffdb0)
- 新版 [`009fff08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffeec.md#insn-009fff08) · [`009fff28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffeec.md#insn-009fff28) · [`009fff4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffeec.md#insn-009fff4c)

~~~diff
- 009ffd6c ["COPY", "tmp:0:8", ["const:410:8"]]
- 009ffd6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ffd6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ffd6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009fff08 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 009fff08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009fff08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009fff08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ffd6c bytes 08411091
+ 009fff08 bytes 08412091
- 009ffd8c ["COPY", "register:0:8", ["register:4040:8"]]
- 009ffd8c ["INT_ADD", "register:40f0:8", ["const:9ffd8c:8", "const:4:8"]]
- 009ffd8c ["CALLIND", null, ["register:0:8"]]
+ 009fff28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009fff28 ["INT_ADD", "register:40f0:8", ["const:9fff28:8", "const:4:8"]]
+ 009fff28 ["CALLIND", null, ["register:0:8"]]
- 009ffd8c bytes 00013fd6
+ 009fff28 bytes 00013fd6
- 009ffdb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ffdb0 ["INT_ADD", "register:40f0:8", ["const:9ffdb0:8", "const:4:8"]]
- 009ffdb0 ["CALLIND", null, ["register:0:8"]]
+ 009fff4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009fff4c ["INT_ADD", "register:40f0:8", ["const:9fff4c:8", "const:4:8"]]
+ 009fff4c ["CALLIND", null, ["register:0:8"]]
- 009ffdb0 bytes 00013fd6
+ 009fff4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-686b663d44917c917d06f8db8e1c8742"></a>

### [`009ffe58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffe58.md) → [`009ffff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffff4.md) FUN_009ffff4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "00a00034",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009ffe98",
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
      "00a00034",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a00034",
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

- 旧版 [`009ffe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffe58.md#insn-009ffe98) · [`009ffea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffe58.md#insn-009ffea4) · [`009fff00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffe58.md#insn-009fff00)
- 新版 [`00a00034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffff4.md#insn-00a00034) · [`00a00040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffff4.md#insn-00a00040) · [`00a0009c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffff4.md#insn-00a0009c)

~~~diff
- 009ffe98 ["INT_ADD", "register:40f0:8", ["const:9ffe98:8", "const:4:8"]]
- 009ffe98 ["CALL", null, ["ram:47acb4:8"]]
+ 00a00034 ["INT_ADD", "register:40f0:8", ["const:a00034:8", "const:4:8"]]
+ 00a00034 ["CALL", null, ["ram:47acf4:8"]]
- 009ffe98 bytes 87ebe997
+ 00a00034 bytes 30ebe997
- 009ffea4 ["INT_ADD", "register:40f0:8", ["const:9ffea4:8", "const:4:8"]]
- 009ffea4 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00a00040 ["INT_ADD", "register:40f0:8", ["const:a00040:8", "const:4:8"]]
+ 00a00040 ["CALL", null, ["callee:0047cdd4:8"]]
- 009ffea4 bytes bcf3e997
+ 00a00040 bytes 65f3e997
- 009fff00 ["COPY", "register:0:8", ["register:4040:8"]]
- 009fff00 ["INT_ADD", "register:40f0:8", ["const:9fff00:8", "const:4:8"]]
- 009fff00 ["CALLIND", null, ["register:0:8"]]
+ 00a0009c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a0009c ["INT_ADD", "register:40f0:8", ["const:a0009c:8", "const:4:8"]]
+ 00a0009c ["CALLIND", null, ["register:0:8"]]
- 009fff00 bytes 00013fd6
+ 00a0009c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-806bcf4a40911b51998547a568e5ffff"></a>

### [`009fffa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009fffa0.md) → [`00a0013c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0013c.md) FUN_00a0013c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "009fffc8",
      "incomplete_value": false,
      "site": "009fffc8",
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
      "00a00164",
      "DATA",
      [
        "storage",
        "00c8a490",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a00164",
      "DATA",
      [
        "storage",
        "00c8a890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fffb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009fffa0.md#insn-009fffb4) · [`009fffc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009fffa0.md#insn-009fffc4)
- 新版 [`00a00150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0013c.md#insn-00a00150) · [`00a00160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0013c.md#insn-00a00160)

~~~diff
- 009fffb4 ["INT_ADD", "register:40f0:8", ["const:9fffb4:8", "const:4:8"]]
- 009fffb4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a00150 ["INT_ADD", "register:40f0:8", ["const:a00150:8", "const:4:8"]]
+ 00a00150 ["CALL", null, ["callee:00c57e90:8"]]
- 009fffb4 bytes b75e0994
+ 00a00150 bytes 505f0994
- 009fffc4 ["COPY", "tmp:0:8", ["const:490:8"]]
- 009fffc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fffc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fffc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a00160 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 00a00160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fffc4 bytes 08411291
+ 00a00160 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-418737b97a10c2ac5a8333f520545c74"></a>

### [`009fffdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009fffdc.md) → [`00a00178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00178.md) FUN_00a00178

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "009fffe0",
      "incomplete_value": false,
      "site": "009fffe4",
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
      "00a00180",
      "DATA",
      [
        "storage",
        "00c8a490",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a00180",
      "DATA",
      [
        "storage",
        "00c8a890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009fffe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009fffdc.md#insn-009fffe0)
- 新版 [`00a0017c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00178.md#insn-00a0017c)

~~~diff
- 009fffe0 ["COPY", "tmp:0:8", ["const:490:8"]]
- 009fffe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009fffe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009fffe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a0017c ["COPY", "tmp:0:8", ["const:890:8"]]
+ 00a0017c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a0017c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a0017c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009fffe0 bytes 08411291
+ 00a0017c bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c226b907634b14ca346571d3759fe1db"></a>

### [`00a001a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a001a0.md) → [`00a0033c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0033c.md) FUN_00a0033c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a001a4",
      "incomplete_value": false,
      "site": "00a001a8",
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
      "00a00344",
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
      "00a00344",
      "DATA",
      [
        "storage",
        "00c8a920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a001a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a001a0.md#insn-00a001a4)
- 新版 [`00a00340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0033c.md#insn-00a00340)

~~~diff
- 00a001a4 ["COPY", "tmp:0:8", ["const:520:8"]]
- 00a001a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a001a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a001a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a00340 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00a00340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a001a4 bytes 08811491
+ 00a00340 bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70d975b3d7884518a4f9727e0c03f67a"></a>

### [`00a001c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a001c0.md) → [`00a0035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0035c.md) FUN_00a0035c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00664860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664860.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00859b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b0c.md) [`008b6a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6a18.md)
- 新版 呼出元 0件  · 呼出先 17件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00859b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b4c.md) [`008b6a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6a5c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.62% / 新版 98.62%

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
      "site": "00a004f8",
      "value": [
        "leaf",
        "ram:6648a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0035c",
      "value": [
        "leaf",
        "ram:664860:8"
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
      "site": "00a005bc",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a00420",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 24,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a005ec",
      "value": [
        "leaf",
        "ram:adf218:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a00450",
      "value": [
        "leaf",
        "ram:adf01c:8"
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
      "00a004f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664860"
      ]
    ],
    [
      "00a005bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00a005ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00adf01c"
      ]
    ]
  ],
  "added": [
    [
      "00a004f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648a0"
      ]
    ],
    [
      "00a005bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00a005ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00adf218"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0035c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a001c0.md#insn-00a0035c) · [`00a00420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a001c0.md#insn-00a00420) · [`00a00450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a001c0.md#insn-00a00450)
- 新版 [`00a004f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0035c.md#insn-00a004f8) · [`00a005bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0035c.md#insn-00a005bc) · [`00a005ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0035c.md#insn-00a005ec)

~~~diff
- 00a0035c ["INT_ADD", "register:40f0:8", ["const:a0035c:8", "const:4:8"]]
- 00a0035c ["CALL", null, ["ram:664860:8"]]
+ 00a004f8 ["INT_ADD", "register:40f0:8", ["const:a004f8:8", "const:4:8"]]
+ 00a004f8 ["CALL", null, ["ram:6648a0:8"]]
- 00a0035c bytes 4191f197
+ 00a004f8 bytes ea90f197
- 00a00420 ["INT_ADD", "register:40f0:8", ["const:a00420:8", "const:4:8"]]
- 00a00420 ["CALL", null, ["ram:46c984:8"]]
+ 00a005bc ["INT_ADD", "register:40f0:8", ["const:a005bc:8", "const:4:8"]]
+ 00a005bc ["CALL", null, ["ram:46c9c4:8"]]
- 00a00420 bytes 59b1e997
+ 00a005bc bytes 02b1e997
- 00a00450 ["INT_ADD", "register:40f0:8", ["const:a00450:8", "const:4:8"]]
- 00a00450 ["CALL", null, ["ram:adf01c:8"]]
+ 00a005ec ["INT_ADD", "register:40f0:8", ["const:a005ec:8", "const:4:8"]]
+ 00a005ec ["CALL", null, ["ram:adf218:8"]]
- 00a00450 bytes f37a0394
+ 00a005ec bytes 0b7b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1be49da0a9d6308ea7de96ab8b53212"></a>

### [`00a00588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a00588.md) → [`00a00724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00724.md) FUN_00a00724

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a005a8",
      "incomplete_value": false,
      "site": "00a005ac",
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
      "00a00748",
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
      "00a00748",
      "DATA",
      [
        "storage",
        "00c8a9a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0059c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a00588.md#insn-00a0059c) · [`00a005a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a00588.md#insn-00a005a8)
- 新版 [`00a00738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00724.md#insn-00a00738) · [`00a00744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00724.md#insn-00a00744)

~~~diff
- 00a0059c ["INT_ADD", "register:40f0:8", ["const:a0059c:8", "const:4:8"]]
- 00a0059c ["CALL", null, ["callee:00c57e90:8"]]
+ 00a00738 ["INT_ADD", "register:40f0:8", ["const:a00738:8", "const:4:8"]]
+ 00a00738 ["CALL", null, ["callee:00c57e90:8"]]
- 00a0059c bytes 3d5d0994
+ 00a00738 bytes d65d0994
- 00a005a8 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 00a005a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a005a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a005a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a00744 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00a00744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a005a8 bytes 08811691
+ 00a00744 bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69f5aa4ca09860e0f7fdc45b8c514663"></a>

### [`00a005c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a005c0.md) → [`00a0075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0075c.md) FUN_00a0075c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a005c4",
      "incomplete_value": false,
      "site": "00a005c8",
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
      "00a00764",
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
      "00a00764",
      "DATA",
      [
        "storage",
        "00c8a9a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a005c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a005c0.md#insn-00a005c4)
- 新版 [`00a00760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0075c.md#insn-00a00760)

~~~diff
- 00a005c4 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 00a005c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a005c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a005c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a00760 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00a00760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a005c4 bytes 08811691
+ 00a00760 bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c682fe5340a3e1663645504d1e71f60"></a>

### [`00a005e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a005e0.md) → [`00a0077c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0077c.md) FUN_00a0077c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046aed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aed8.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046af18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af18.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.88% / 新版 97.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `call_target` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00a00644",
      "incomplete_value": true,
      "site": "00a00644",
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
    "old": {
      "definition_site": "00a00684",
      "incomplete_value": true,
      "site": "00a00684",
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
    "old": {
      "definition_site": "00a0064c",
      "incomplete_value": false,
      "site": "00a0065c",
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
            "const:a58:8"
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
      "00a007dc",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00a007e8",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a007f0",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a007dc",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00a007e8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a007f0",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0065c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a005e0.md#insn-00a0065c) · [`00a0069c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a005e0.md#insn-00a0069c) · [`00a007e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a005e0.md#insn-00a007e0)
- 新版 [`00a007f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0077c.md#insn-00a007f8) · [`00a00838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0077c.md#insn-00a00838) · [`00a0097c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0077c.md#insn-00a0097c)

~~~diff
- 00a0065c ["INT_ADD", "register:40f0:8", ["const:a0065c:8", "const:4:8"]]
- 00a0065c ["CALL", null, ["callee:00c58610:8"]]
+ 00a007f8 ["INT_ADD", "register:40f0:8", ["const:a007f8:8", "const:4:8"]]
+ 00a007f8 ["CALL", null, ["callee:00c58610:8"]]
- 00a0065c bytes ed5e0994
+ 00a007f8 bytes 865f0994
- 00a0069c ["INT_ADD", "register:40f0:8", ["const:a0069c:8", "const:4:8"]]
- 00a0069c ["CALL", null, ["callee:00c58610:8"]]
+ 00a00838 ["INT_ADD", "register:40f0:8", ["const:a00838:8", "const:4:8"]]
+ 00a00838 ["CALL", null, ["callee:00c58610:8"]]
- 00a0069c bytes dd5e0994
+ 00a00838 bytes 765f0994
- 00a007e0 ["INT_ADD", "register:40f0:8", ["const:a007e0:8", "const:4:8"]]
- 00a007e0 ["CALL", null, ["callee:00467b60:8"]]
+ 00a0097c ["INT_ADD", "register:40f0:8", ["const:a0097c:8", "const:4:8"]]
+ 00a0097c ["CALL", null, ["callee:00467b60:8"]]
- 00a007e0 bytes d09ce997
+ 00a0097c bytes 799ce997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a39e2b9ea351cdbf571defbaf4d876f0"></a>

### [`00a00cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a00cb0.md) → [`00a00e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e4c.md) FUN_00a00e4c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a00cd4",
      "incomplete_value": false,
      "site": "00a00cd4",
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
      "00a00e70",
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
      "00a00e70",
      "DATA",
      [
        "storage",
        "00c8aa20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a00cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a00cb0.md#insn-00a00cc4) · [`00a00cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a00cb0.md#insn-00a00cd0)
- 新版 [`00a00e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e4c.md#insn-00a00e60) · [`00a00e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e4c.md#insn-00a00e6c)

~~~diff
- 00a00cc4 ["INT_ADD", "register:40f0:8", ["const:a00cc4:8", "const:4:8"]]
- 00a00cc4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a00e60 ["INT_ADD", "register:40f0:8", ["const:a00e60:8", "const:4:8"]]
+ 00a00e60 ["CALL", null, ["callee:00c57e90:8"]]
- 00a00cc4 bytes 735b0994
+ 00a00e60 bytes 0c5c0994
- 00a00cd0 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00a00cd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a00cd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a00cd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a00e6c ["COPY", "tmp:0:8", ["const:a20:8"]]
+ 00a00e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a00e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a00cd0 bytes 08811891
+ 00a00e6c bytes 08812891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71c7952447782c361972432b9db62a66"></a>

### [`00a00ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a00ce4.md) → [`00a00e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e80.md) FUN_00a00e80

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a00cf0",
      "incomplete_value": false,
      "site": "00a00cf0",
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
      "00a00e8c",
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
      "00a00e8c",
      "DATA",
      [
        "storage",
        "00c8aa20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a00cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a00ce4.md#insn-00a00cec)
- 新版 [`00a00e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e80.md#insn-00a00e88)

~~~diff
- 00a00cec ["COPY", "tmp:0:8", ["const:620:8"]]
- 00a00cec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a00cec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a00cec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a00e88 ["COPY", "tmp:0:8", ["const:a20:8"]]
+ 00a00e88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a00e88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a00e88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a00cec bytes 29811891
+ 00a00e88 bytes 29812891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57f2739b7b1afaab59c94ddd1be252be"></a>

### [`00a00d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a00d00.md) → [`00a00e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e9c.md) FUN_00a00e9c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 21件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00664860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664860.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)
- 新版 呼出元 0件  · 呼出先 21件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)

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
      "site": "00a00eec",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a00d50",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "00a00f08",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a00d6c",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "00a01044",
      "value": [
        "leaf",
        "ram:6648a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a00ea8",
      "value": [
        "leaf",
        "ram:664860:8"
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
      "00a00eec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a00f08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a01044",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664860"
      ]
    ]
  ],
  "added": [
    [
      "00a00eec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a00f08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a01044",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a00d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a00d00.md#insn-00a00d50) · [`00a00d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a00d00.md#insn-00a00d6c) · [`00a00ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a00d00.md#insn-00a00ea8)
- 新版 [`00a00eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e9c.md#insn-00a00eec) · [`00a00f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e9c.md#insn-00a00f08) · [`00a01044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00e9c.md#insn-00a01044)

~~~diff
- 00a00d50 ["INT_ADD", "register:40f0:8", ["const:a00d50:8", "const:4:8"]]
- 00a00d50 ["CALL", null, ["ram:47acb4:8"]]
+ 00a00eec ["INT_ADD", "register:40f0:8", ["const:a00eec:8", "const:4:8"]]
+ 00a00eec ["CALL", null, ["ram:47acf4:8"]]
- 00a00d50 bytes d9e7e997
+ 00a00eec bytes 82e7e997
- 00a00d6c ["INT_ADD", "register:40f0:8", ["const:a00d6c:8", "const:4:8"]]
- 00a00d6c ["CALL", null, ["ram:47acb4:8"]]
+ 00a00f08 ["INT_ADD", "register:40f0:8", ["const:a00f08:8", "const:4:8"]]
+ 00a00f08 ["CALL", null, ["ram:47acf4:8"]]
- 00a00d6c bytes d2e7e997
+ 00a00f08 bytes 7be7e997
- 00a00ea8 ["INT_ADD", "register:40f0:8", ["const:a00ea8:8", "const:4:8"]]
- 00a00ea8 ["CALL", null, ["ram:664860:8"]]
+ 00a01044 ["INT_ADD", "register:40f0:8", ["const:a01044:8", "const:4:8"]]
+ 00a01044 ["CALL", null, ["ram:6648a0:8"]]
- 00a00ea8 bytes 6e8ef197
+ 00a01044 bytes 178ef197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7b5ad77c594fb8719e662a51d5054ef"></a>

### [`00a01014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01014.md) → [`00a011b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a011b0.md) FUN_00a011b0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a01038",
      "incomplete_value": false,
      "site": "00a01038",
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
      "00a011d4",
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
      "00a011d4",
      "DATA",
      [
        "storage",
        "00c8aaa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a01028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01014.md#insn-00a01028) · [`00a01034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01014.md#insn-00a01034)
- 新版 [`00a011c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a011b0.md#insn-00a011c4) · [`00a011d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a011b0.md#insn-00a011d0)

~~~diff
- 00a01028 ["INT_ADD", "register:40f0:8", ["const:a01028:8", "const:4:8"]]
- 00a01028 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a011c4 ["INT_ADD", "register:40f0:8", ["const:a011c4:8", "const:4:8"]]
+ 00a011c4 ["CALL", null, ["callee:00c57e90:8"]]
- 00a01028 bytes 9a5a0994
+ 00a011c4 bytes 335b0994
- 00a01034 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00a01034 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a01034 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a01034 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a011d0 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 00a011d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a011d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a011d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a01034 bytes 08811a91
+ 00a011d0 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f506318709d01205a0b140cad4c41804"></a>

### [`00a01048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01048.md) → [`00a011e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a011e4.md) FUN_00a011e4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a01054",
      "incomplete_value": false,
      "site": "00a01054",
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
      "00a011f0",
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
      "00a011f0",
      "DATA",
      [
        "storage",
        "00c8aaa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a01050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01048.md#insn-00a01050)
- 新版 [`00a011ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a011e4.md#insn-00a011ec)

~~~diff
- 00a01050 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00a01050 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a01050 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a01050 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a011ec ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 00a011ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a011ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a011ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a01050 bytes 29811a91
+ 00a011ec bytes 29812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3592cdcf5c5eeeded0dd38d53c38dd9"></a>

### [`00a01064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01064.md) → [`00a01200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01200.md) FUN_00a01200

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f04.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f48.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "00a01238",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0109c",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "00a01250",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a010b4",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00a01238",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a01250",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a01238",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a01250",
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

- 旧版 [`00a0109c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01064.md#insn-00a0109c) · [`00a010b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01064.md#insn-00a010b4) · [`00a01080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01064.md#insn-00a01080)
- 新版 [`00a01238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01200.md#insn-00a01238) · [`00a01250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01200.md#insn-00a01250) · [`00a0121c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01200.md#insn-00a0121c)

~~~diff
- 00a0109c ["INT_ADD", "register:40f0:8", ["const:a0109c:8", "const:4:8"]]
- 00a0109c ["CALL", null, ["ram:47acb4:8"]]
+ 00a01238 ["INT_ADD", "register:40f0:8", ["const:a01238:8", "const:4:8"]]
+ 00a01238 ["CALL", null, ["ram:47acf4:8"]]
- 00a0109c bytes 06e7e997
+ 00a01238 bytes afe6e997
- 00a010b4 ["INT_ADD", "register:40f0:8", ["const:a010b4:8", "const:4:8"]]
- 00a010b4 ["CALL", null, ["ram:47acb4:8"]]
+ 00a01250 ["INT_ADD", "register:40f0:8", ["const:a01250:8", "const:4:8"]]
+ 00a01250 ["CALL", null, ["ram:47acf4:8"]]
- 00a010b4 bytes 00e7e997
+ 00a01250 bytes a9e6e997
- 00a01080 ["INT_ADD", "register:40f0:8", ["const:a01080:8", "const:4:8"]]
- 00a01080 ["CALL", null, ["callee:008b6f48:8"]]
+ 00a0121c ["INT_ADD", "register:40f0:8", ["const:a0121c:8", "const:4:8"]]
+ 00a0121c ["CALL", null, ["callee:008b6f48:8"]]
- 00a01080 bytes a1d7fa97
+ 00a0121c bytes 4bd7fa97
~~~


<a id="compare-dee3ea963e50e01a488f44a1497a452d"></a>

### [`00a01108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01108.md) → [`00a012a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012a4.md) FUN_00a012a4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a0112c",
      "incomplete_value": false,
      "site": "00a0112c",
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
      "00a012c8",
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
      "00a012c8",
      "DATA",
      [
        "storage",
        "00c8ab20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0111c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01108.md#insn-00a0111c) · [`00a01128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01108.md#insn-00a01128)
- 新版 [`00a012b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012a4.md#insn-00a012b8) · [`00a012c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012a4.md#insn-00a012c4)

~~~diff
- 00a0111c ["INT_ADD", "register:40f0:8", ["const:a0111c:8", "const:4:8"]]
- 00a0111c ["CALL", null, ["callee:00c57e90:8"]]
+ 00a012b8 ["INT_ADD", "register:40f0:8", ["const:a012b8:8", "const:4:8"]]
+ 00a012b8 ["CALL", null, ["callee:00c57e90:8"]]
- 00a0111c bytes 5d5a0994
+ 00a012b8 bytes f65a0994
- 00a01128 ["COPY", "tmp:0:8", ["const:720:8"]]
- 00a01128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a01128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a01128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a012c4 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 00a012c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a012c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a012c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a01128 bytes 08811c91
+ 00a012c4 bytes 08812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0c5c16ef8406736097157e4956acebb"></a>

### [`00a0113c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a0113c.md) → [`00a012d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012d8.md) FUN_00a012d8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a01148",
      "incomplete_value": false,
      "site": "00a01148",
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
      "00a012e4",
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
      "00a012e4",
      "DATA",
      [
        "storage",
        "00c8ab20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a01144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a0113c.md#insn-00a01144)
- 新版 [`00a012e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012d8.md#insn-00a012e0)

~~~diff
- 00a01144 ["COPY", "tmp:0:8", ["const:720:8"]]
- 00a01144 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a01144 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a01144 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a012e0 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 00a012e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a012e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a012e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a01144 bytes 29811c91
+ 00a012e0 bytes 29812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3c8ccdaa956dadcd536a4fcf71a7a63"></a>

### [`00a01158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01158.md) → [`00a012f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012f4.md) FUN_00a012f4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`009faa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fa/009faa30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`009fabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md)

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
      "site": "00a01314",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a01178",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "00a01320",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a01184",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00a01314",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a01320",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a01314",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a01320",
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

- 旧版 [`00a01178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01158.md#insn-00a01178) · [`00a01184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01158.md#insn-00a01184)
- 新版 [`00a01314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012f4.md#insn-00a01314) · [`00a01320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a012f4.md#insn-00a01320)

~~~diff
- 00a01178 ["INT_ADD", "register:40f0:8", ["const:a01178:8", "const:4:8"]]
- 00a01178 ["CALL", null, ["ram:47acb4:8"]]
+ 00a01314 ["INT_ADD", "register:40f0:8", ["const:a01314:8", "const:4:8"]]
+ 00a01314 ["CALL", null, ["ram:47acf4:8"]]
- 00a01178 bytes cfe6e997
+ 00a01314 bytes 78e6e997
- 00a01184 ["INT_ADD", "register:40f0:8", ["const:a01184:8", "const:4:8"]]
- 00a01184 ["CALL", null, ["ram:47acb4:8"]]
+ 00a01320 ["INT_ADD", "register:40f0:8", ["const:a01320:8", "const:4:8"]]
+ 00a01320 ["CALL", null, ["ram:47acf4:8"]]
- 00a01184 bytes cce6e997
+ 00a01320 bytes 75e6e997
~~~


<a id="compare-7be1b93d4972207c3cbaa71ed0eeb175"></a>

### [`00a011d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a011d8.md) → [`00a01374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01374.md) FUN_00a01374

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "00a011ec",
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
            "const:7a0:8"
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
      "00a0138c",
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
      "00a0138c",
      "DATA",
      [
        "storage",
        "00c8aba0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a011e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a011d8.md#insn-00a011e4) · [`00a011ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a011d8.md#insn-00a011ec)
- 新版 [`00a01380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01374.md#insn-00a01380) · [`00a01388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01374.md#insn-00a01388)

~~~diff
- 00a011e4 ["INT_ADD", "register:40f0:8", ["const:a011e4:8", "const:4:8"]]
- 00a011e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a01380 ["INT_ADD", "register:40f0:8", ["const:a01380:8", "const:4:8"]]
+ 00a01380 ["CALL", null, ["callee:00c57e90:8"]]
- 00a011e4 bytes 2b5a0994
+ 00a01380 bytes c45a0994
- 00a011ec ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 00a011ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a011ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a011ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a01388 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 00a01388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a01388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a01388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a011ec bytes 08811e91
+ 00a01388 bytes 08812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efabbbe0003d806c5f975fa31faf3c93"></a>

### [`00a011fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a011fc.md) → [`00a01398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01398.md) FUN_00a01398

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a01200",
      "incomplete_value": false,
      "site": "00a01204",
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
      "00a013a0",
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
      "00a013a0",
      "DATA",
      [
        "storage",
        "00c8aba0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a01200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a011fc.md#insn-00a01200)
- 新版 [`00a0139c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01398.md#insn-00a0139c)

~~~diff
- 00a01200 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 00a01200 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a01200 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a01200 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a0139c ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 00a0139c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a0139c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a0139c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a01200 bytes 08811e91
+ 00a0139c bytes 08812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79c5d03ced5623ee015d6ef68d754f32"></a>

### [`00a01214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01214.md) → [`00a013b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a013b0.md) FUN_00a013b0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b7904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7904.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b7948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7948.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "00a013d8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0123c",
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
      "00a013d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a013d8",
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

- 旧版 [`00a0123c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01214.md#insn-00a0123c) · [`00a01248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01214.md#insn-00a01248) · [`00a01264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01214.md#insn-00a01264)
- 新版 [`00a013d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a013b0.md#insn-00a013d8) · [`00a013e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a013b0.md#insn-00a013e4) · [`00a01400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a013b0.md#insn-00a01400)

~~~diff
- 00a0123c ["INT_ADD", "register:40f0:8", ["const:a0123c:8", "const:4:8"]]
- 00a0123c ["CALL", null, ["ram:47acb4:8"]]
+ 00a013d8 ["INT_ADD", "register:40f0:8", ["const:a013d8:8", "const:4:8"]]
+ 00a013d8 ["CALL", null, ["ram:47acf4:8"]]
- 00a0123c bytes 9ee6e997
+ 00a013d8 bytes 47e6e997
- 00a01248 ["INT_ADD", "register:40f0:8", ["const:a01248:8", "const:4:8"]]
- 00a01248 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00a013e4 ["INT_ADD", "register:40f0:8", ["const:a013e4:8", "const:4:8"]]
+ 00a013e4 ["CALL", null, ["callee:0047cdd4:8"]]
- 00a01248 bytes d3eee997
+ 00a013e4 bytes 7ceee997
- 00a01264 ["INT_ADD", "register:40f0:8", ["const:a01264:8", "const:4:8"]]
- 00a01264 ["CALL", null, ["callee:008514f8:8"]]
+ 00a01400 ["INT_ADD", "register:40f0:8", ["const:a01400:8", "const:4:8"]]
+ 00a01400 ["CALL", null, ["callee:008514f8:8"]]
- 00a01264 bytes 9540f997
+ 00a01400 bytes 3e40f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ffb0af91fcec52099350169c948f56c"></a>

### [`00a012ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a012ec.md) → [`00a01488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01488.md) FUN_00a01488

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "00a01310",
      "incomplete_value": true,
      "site": "00a01314",
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
            "const:820:8"
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
      "00a014b0",
      "DATA",
      [
        "storage",
        "00c8a820",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a014b0",
      "DATA",
      [
        "storage",
        "00c8ac20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a01300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a012ec.md#insn-00a01300) · [`00a01310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a012ec.md#insn-00a01310)
- 新版 [`00a0149c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01488.md#insn-00a0149c) · [`00a014ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a01488.md#insn-00a014ac)

~~~diff
- 00a01300 ["INT_ADD", "register:40f0:8", ["const:a01300:8", "const:4:8"]]
- 00a01300 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a0149c ["INT_ADD", "register:40f0:8", ["const:a0149c:8", "const:4:8"]]
+ 00a0149c ["CALL", null, ["callee:00c57e90:8"]]
- 00a01300 bytes e4590994
+ 00a0149c bytes 7d5a0994
- 00a01310 ["COPY", "tmp:0:8", ["const:820:8"]]
- 00a01310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a01310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a01310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a014ac ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 00a014ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a014ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a014ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a01310 bytes 08812091
+ 00a014ac bytes 08813091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76796685049a73bcfa22e9400b3f4c2d"></a>

### [`00a0132c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a0132c.md) → [`00a014c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a014c8.md) FUN_00a014c8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a01330",
      "incomplete_value": false,
      "site": "00a01334",
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
            "const:820:8"
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
      "00a014d0",
      "DATA",
      [
        "storage",
        "00c8a820",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a014d0",
      "DATA",
      [
        "storage",
        "00c8ac20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a01330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a0132c.md#insn-00a01330)
- 新版 [`00a014cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a01/00a014c8.md#insn-00a014cc)

~~~diff
- 00a01330 ["COPY", "tmp:0:8", ["const:820:8"]]
- 00a01330 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a01330 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a01330 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a014cc ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 00a014cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a014cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a014cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a01330 bytes 08812091
+ 00a014cc bytes 08813091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ead1b8a8dd056a2a86f86437f23b621"></a>

### [`00a020e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a020e4.md) → [`00a02280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02280.md) FUN_00a02280

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a02104",
      "incomplete_value": false,
      "site": "00a02108",
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
            "const:8a0:8"
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
      "00a022a4",
      "DATA",
      [
        "storage",
        "00c8a8a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a022a4",
      "DATA",
      [
        "storage",
        "00c8aca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a020f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a020e4.md#insn-00a020f8) · [`00a02104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a020e4.md#insn-00a02104)
- 新版 [`00a02294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02280.md#insn-00a02294) · [`00a022a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02280.md#insn-00a022a0)

~~~diff
- 00a020f8 ["INT_ADD", "register:40f0:8", ["const:a020f8:8", "const:4:8"]]
- 00a020f8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a02294 ["INT_ADD", "register:40f0:8", ["const:a02294:8", "const:4:8"]]
+ 00a02294 ["CALL", null, ["callee:00c57e90:8"]]
- 00a020f8 bytes 66560994
+ 00a02294 bytes ff560994
- 00a02104 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00a02104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a02104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a02104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a022a0 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00a022a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a022a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a022a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a02104 bytes 08812291
+ 00a022a0 bytes 08813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f600a1a6ec1bd9fe0a55f05b81b46a87"></a>

### [`00a0211c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a0211c.md) → [`00a022b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022b8.md) FUN_00a022b8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a02120",
      "incomplete_value": false,
      "site": "00a02124",
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
            "const:8a0:8"
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
      "00a022c0",
      "DATA",
      [
        "storage",
        "00c8a8a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a022c0",
      "DATA",
      [
        "storage",
        "00c8aca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a02120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a0211c.md#insn-00a02120)
- 新版 [`00a022bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022b8.md#insn-00a022bc)

~~~diff
- 00a02120 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00a02120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a02120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a02120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a022bc ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00a022bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a022bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a022bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a02120 bytes 08812291
+ 00a022bc bytes 08813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a6af5005de21fa309a81c84662d5e38"></a>

### [`00a0213c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a0213c.md) → [`00a022d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022d8.md) FUN_00a022d8

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 19件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d74.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

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
    "old": {
      "definition_site": "00a024e4",
      "incomplete_value": false,
      "site": "00a024e8",
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
            "const:d34:8"
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
      "00a02634",
      "DATA",
      [
        "storage",
        "00436bd4",
        null,
        "qword"
      ]
    ],
    [
      "00a02680",
      "PARAM",
      [
        "storage",
        "002b3d34",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a02634",
      "DATA",
      [
        "storage",
        "00436bd4",
        null,
        "byte[59]"
      ]
    ],
    [
      "00a02680",
      "PARAM",
      [
        "storage",
        "002b3d74",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a024e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a0213c.md#insn-00a024e8) · [`00a0216c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a0213c.md#insn-00a0216c) · [`00a0217c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a0213c.md#insn-00a0217c)
- 新版 [`00a02684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022d8.md#insn-00a02684) · [`00a02308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022d8.md#insn-00a02308) · [`00a02318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022d8.md#insn-00a02318)

~~~diff
- 00a024e8 ["INT_ADD", "register:40f0:8", ["const:a024e8:8", "const:4:8"]]
- 00a024e8 ["CALL", null, ["callee:00442930:8"]]
+ 00a02684 ["INT_ADD", "register:40f0:8", ["const:a02684:8", "const:4:8"]]
+ 00a02684 ["CALL", null, ["callee:00442930:8"]]
- 00a024e8 bytes 0201e997
+ 00a02684 bytes ab00e997
- 00a0216c ["INT_ADD", "register:40f0:8", ["const:a0216c:8", "const:4:8"]]
- 00a0216c ["CALL", null, ["callee:008b9290:8"]]
+ 00a02308 ["INT_ADD", "register:40f0:8", ["const:a02308:8", "const:4:8"]]
+ 00a02308 ["CALL", null, ["callee:008b9290:8"]]
- 00a0216c bytes 38dcfa97
+ 00a02308 bytes e2dbfa97
- 00a0217c ["INT_ADD", "register:40f0:8", ["const:a0217c:8", "const:4:8"]]
- 00a0217c ["CALL", null, ["callee:008b9290:8"]]
+ 00a02318 ["INT_ADD", "register:40f0:8", ["const:a02318:8", "const:4:8"]]
+ 00a02318 ["CALL", null, ["callee:008b9290:8"]]
- 00a0217c bytes 34dcfa97
+ 00a02318 bytes dedbfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbd5f9321af66946ec5577536d1c9ca8"></a>

### [`00a02518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02518.md) → [`00a026b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a026b4.md) FUN_00a026b4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a0253c",
      "incomplete_value": false,
      "site": "00a0253c",
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
      "00a026d8",
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
      "00a026d8",
      "DATA",
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

- 旧版 [`00a0252c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02518.md#insn-00a0252c) · [`00a02538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02518.md#insn-00a02538)
- 新版 [`00a026c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a026b4.md#insn-00a026c8) · [`00a026d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a026b4.md#insn-00a026d4)

~~~diff
- 00a0252c ["INT_ADD", "register:40f0:8", ["const:a0252c:8", "const:4:8"]]
- 00a0252c ["CALL", null, ["callee:00c57e90:8"]]
+ 00a026c8 ["INT_ADD", "register:40f0:8", ["const:a026c8:8", "const:4:8"]]
+ 00a026c8 ["CALL", null, ["callee:00c57e90:8"]]
- 00a0252c bytes 59550994
+ 00a026c8 bytes f2550994
- 00a02538 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00a02538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a02538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a02538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a026d4 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00a026d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a026d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a026d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a02538 bytes 08812491
+ 00a026d4 bytes 08813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd037ae232ec3a296c081cfae20e46d5"></a>

### [`00a0254c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a0254c.md) → [`00a026e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a026e8.md) FUN_00a026e8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00a02558",
      "incomplete_value": false,
      "site": "00a02558",
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
      "00a026f4",
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
      "00a026f4",
      "DATA",
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

- 旧版 [`00a02554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a0254c.md#insn-00a02554)
- 新版 [`00a026f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a026e8.md#insn-00a026f0)

~~~diff
- 00a02554 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00a02554 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a02554 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a02554 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a026f0 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00a026f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a026f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a026f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a02554 bytes 29812491
+ 00a026f0 bytes 29813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

