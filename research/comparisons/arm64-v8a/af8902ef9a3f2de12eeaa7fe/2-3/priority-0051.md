# v16.0.0 → v16.0.1 · 最優先の変更候補 (51)

[一覧の目次](README.md)

<a id="compare-3ac70e591f828459ade04200fcf336fa"></a>

### [`008e0a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0a94.md) → [`008e0c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e0/008e0c30.md) FUN_008e0c30

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008ddb18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008ddb18.md) · 呼出先 13件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) [`00758190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/00758190.md) [`0086369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00863/0086369c.md)
- 新版 呼出元 1件 [`008ddcb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddcb4.md) · 呼出先 13件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00633374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md) [`007581d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00758/007581d0.md) [`008636dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00863/008636dc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.69% / 新版 82.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 36件, `store_destination` 7件, `store_value` 27件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008e0c68",
      "incomplete_value": false,
      "site": "008e0c74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e0acc",
      "incomplete_value": false,
      "site": "008e0ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "definition_site": "008e0cb0",
      "incomplete_value": true,
      "site": "008e0cb0",
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
                "const:38e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e0b14",
      "incomplete_value": true,
      "site": "008e0b14",
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
                "const:34e:8"
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
      "definition_site": "008e0cc8",
      "incomplete_value": true,
      "site": "008e0cc8",
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
                "const:f16:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e0b2c",
      "incomplete_value": true,
      "site": "008e0b2c",
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
                "const:ed6:8"
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
      "008e0c74",
      "DATA",
      [
        "storage",
        "00c84cc0",
        null,
        "pointer"
      ]
    ],
    [
      "008e0c80",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "008e0ca0",
      "READ",
      [
        "storage",
        "002b634e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e0c74",
      "DATA",
      [
        "storage",
        "00c850c0",
        null,
        "pointer"
      ]
    ],
    [
      "008e0c80",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "008e0ca0",
      "READ",
      [
        "storage",
        "002b638e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e0ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0a94.md#insn-008e0ad4) · [`008e0c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0a94.md#insn-008e0c20) · [`008e0c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0a94.md#insn-008e0c74)
- 新版 `008e0c70`（命令位置の公開資料なし） · `008e0dbc`（命令位置の公開資料なし）

~~~diff
- 008e0ad4 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 008e0ad4 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 008e0ad4 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 008e0ad4 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 008e0c70 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 008e0c70 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 008e0c70 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 008e0c70 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 008e0ad4 bytes 18e32c91
+ 008e0c70 bytes 18e33c91
- 008e0c20 ["INT_ADD", "register:40f0:8", ["const:8e0c20:8", "const:4:8"]]
- 008e0c20 ["CALL", null, ["callee:00c53d00:8"]]
+ 008e0dbc ["INT_ADD", "register:40f0:8", ["const:8e0dbc:8", "const:4:8"]]
+ 008e0dbc ["CALL", null, ["callee:00c53d00:8"]]
- 008e0c20 bytes 30cb0d94
+ 008e0dbc bytes d1cb0d94
- 008e0c74 ["COPY", "register:4040:8", ["const:2a9000:8"]]
- 008e0c74 bytes 48ceffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b67d72be86f5c3fec076eebf67105c2a"></a>

### [`008e1778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1778.md) → [`008e1914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e1/008e1914.md) FUN_008e1914

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "008e192c",
      "incomplete_value": false,
      "site": "008e1930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e1790",
      "incomplete_value": false,
      "site": "008e1794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "definition_site": "008e1968",
      "incomplete_value": false,
      "site": "008e196c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e17cc",
      "incomplete_value": false,
      "site": "008e17d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:410:8"
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
      "008e1930",
      "DATA",
      [
        "storage",
        "00c77f30",
        null,
        "pointer"
      ]
    ],
    [
      "008e196c",
      "DATA",
      [
        "storage",
        "00c74410",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008e1930",
      "DATA",
      [
        "storage",
        "00c78330",
        null,
        "pointer"
      ]
    ],
    [
      "008e196c",
      "DATA",
      [
        "storage",
        "00c74810",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e178c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1778.md#insn-008e178c) · [`008e1790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1778.md#insn-008e1790) · [`008e17a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1778.md#insn-008e17a4)
- 新版 `008e1928`（命令位置の公開資料なし） · `008e192c`（命令位置の公開資料なし） · `008e1940`（命令位置の公開資料なし）

~~~diff
- 008e178c ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 008e1928 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 008e178c bytes a81c00d0
+ 008e1928 bytes a81c00f0
- 008e1790 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 008e1790 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e1790 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e1790 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e192c ["COPY", "tmp:0:8", ["const:330:8"]]
+ 008e192c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e192c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e192c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e1790 bytes 08c13c91
+ 008e192c bytes 08c10c91
- 008e17a4 ["INT_ADD", "register:40f0:8", ["const:8e17a4:8", "const:4:8"]]
- 008e17a4 ["CALL", null, ["callee:00c53d00:8"]]
+ 008e1940 ["INT_ADD", "register:40f0:8", ["const:8e1940:8", "const:4:8"]]
+ 008e1940 ["CALL", null, ["callee:00c53d00:8"]]
- 008e17a4 bytes 4fc80d94
+ 008e1940 bytes f0c80d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e812d689f95505dbe856d7e98b5fcce0"></a>

### [`008e1818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1818.md) → [`008e19b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e1/008e19b4.md) _INIT_173

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "008e19f0",
      "incomplete_value": true,
      "site": "008e1a0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008e1854",
      "incomplete_value": true,
      "site": "008e1870",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008e1a14",
      "incomplete_value": true,
      "site": "008e1a30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008e1878",
      "incomplete_value": true,
      "site": "008e1894",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008e1a34",
      "incomplete_value": true,
      "site": "008e1a50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008e1898",
      "incomplete_value": true,
      "site": "008e18b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "008e19f0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "008e1a14",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "008e1a34",
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
      "008e19f0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "008e1a14",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "008e1a34",
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

- 旧版 [`008e18b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1818.md#insn-008e18b0) · [`008e1978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1818.md#insn-008e1978) · [`008e1a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1818.md#insn-008e1a30)
- 新版 `008e1a4c`（命令位置の公開資料なし） · `008e1b14`（命令位置の公開資料なし） · `008e1bcc`（命令位置の公開資料なし）

~~~diff
- 008e18b0 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 008e18b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008e18b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008e18b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008e1a4c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 008e1a4c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008e1a4c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008e1a4c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008e18b0 bytes 4a553a91
+ 008e1a4c bytes 4a893d91
- 008e1978 ["INT_ADD", "register:40f0:8", ["const:8e1978:8", "const:4:8"]]
- 008e1978 ["CALL", null, ["callee:0043b7f8:8"]]
+ 008e1b14 ["INT_ADD", "register:40f0:8", ["const:8e1b14:8", "const:4:8"]]
+ 008e1b14 ["CALL", null, ["callee:0043b7f8:8"]]
- 008e1978 bytes 9067ed97
+ 008e1b14 bytes 3967ed97
- 008e1a30 ["INT_ADD", "register:40f0:8", ["const:8e1a30:8", "const:4:8"]]
- 008e1a30 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008e1bcc ["INT_ADD", "register:40f0:8", ["const:8e1bcc:8", "const:4:8"]]
+ 008e1bcc ["CALL", null, ["callee:00c57eb0:8"]]
- 008e1a30 bytes 20d80d94
+ 008e1bcc bytes b9d80d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e31f912b21963a94d0fb58575ec6025"></a>

### [`008e1ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1ba8.md) → [`008e1d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e1/008e1d44.md) FUN_008e1d44

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008e5de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5de0.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)
- 新版 呼出元 1件 [`008e5f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e5/008e5f7c.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.55% / 新版 88.55%

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
      "definition_site": "008e1d90",
      "incomplete_value": false,
      "site": "008e1d98",
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
      "definition_site": "008e1bf4",
      "incomplete_value": false,
      "site": "008e1bfc",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e1dbc",
      "incomplete_value": true,
      "site": "008e1dcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:266:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e1c20",
      "incomplete_value": true,
      "site": "008e1c30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:226:8"
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
      "definition_site": "008e1dd0",
      "incomplete_value": true,
      "site": "008e1dd0",
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
      "definition_site": "008e1c34",
      "incomplete_value": true,
      "site": "008e1c34",
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
      "008e1d98",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "008e1dbc",
      "READ",
      [
        "storage",
        "002b4226",
        null,
        "string"
      ]
    ],
    [
      "008e1dc0",
      "READ",
      [
        "storage",
        "002b4235",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e1d98",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "008e1dbc",
      "READ",
      [
        "storage",
        "002b4266",
        null,
        "string"
      ]
    ],
    [
      "008e1dc0",
      "READ",
      [
        "storage",
        "002b4275",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e1c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1ba8.md#insn-008e1c00) · [`008e1dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1ba8.md#insn-008e1dd0) · [`008e1be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1ba8.md#insn-008e1be0)
- 新版 `008e1d9c`（命令位置の公開資料なし） · `008e1f6c`（命令位置の公開資料なし） · `008e1d7c`（命令位置の公開資料なし）

~~~diff
- 008e1c00 ["INT_ADD", "register:40f0:8", ["const:8e1c00:8", "const:4:8"]]
- 008e1c00 ["CALL", null, ["callee:00868c20:8"]]
+ 008e1d9c ["INT_ADD", "register:40f0:8", ["const:8e1d9c:8", "const:4:8"]]
+ 008e1d9c ["CALL", null, ["callee:00868c20:8"]]
- 008e1c00 bytes f81bfe97
+ 008e1d9c bytes a11bfe97
- 008e1dd0 ["INT_ADD", "register:40f0:8", ["const:8e1dd0:8", "const:4:8"]]
- 008e1dd0 ["CALL", null, ["callee:00c57fa0:8"]]
+ 008e1f6c ["INT_ADD", "register:40f0:8", ["const:8e1f6c:8", "const:4:8"]]
+ 008e1f6c ["CALL", null, ["callee:00c57fa0:8"]]
- 008e1dd0 bytes 74d70d94
+ 008e1f6c bytes 0dd80d94
- 008e1be0 ["INT_ADD", "register:40f0:8", ["const:8e1be0:8", "const:4:8"]]
- 008e1be0 ["CALL", null, ["callee:00487e20:8"]]
+ 008e1d7c ["INT_ADD", "register:40f0:8", ["const:8e1d7c:8", "const:4:8"]]
+ 008e1d7c ["CALL", null, ["callee:00487e20:8"]]
- 008e1be0 bytes 8098ee97
+ 008e1d7c bytes 2998ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43f106d83cf4377ebfd3937e5d157e5b"></a>

### [`008e2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md) → [`008e28bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e2/008e28bc.md) FUN_008e28bc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008e5de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5de0.md) · 呼出先 23件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)
- 新版 呼出元 1件 [`008e5f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e5/008e5f7c.md) · 呼出先 23件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008e2900",
      "incomplete_value": false,
      "site": "008e2908",
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
      "definition_site": "008e2764",
      "incomplete_value": false,
      "site": "008e276c",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e2920",
      "incomplete_value": true,
      "site": "008e292c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7b7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e2784",
      "incomplete_value": true,
      "site": "008e2790",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:777:8"
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
      "definition_site": "008e2a4c",
      "incomplete_value": true,
      "site": "008e2a4c",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:c2d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e28b0",
      "incomplete_value": true,
      "site": "008e28b0",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:bed:8"
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
      "008e2908",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "008e2920",
      "READ",
      [
        "storage",
        "002b8777",
        null,
        "string"
      ]
    ],
    [
      "008e2a3c",
      "READ",
      [
        "storage",
        "002abbed",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e2908",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "008e2920",
      "READ",
      [
        "storage",
        "002b87b7",
        null,
        "string"
      ]
    ],
    [
      "008e2a3c",
      "READ",
      [
        "storage",
        "002abc2d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e2f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md#insn-008e2f54) · [`008e2758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md#insn-008e2758) · [`008e2764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md#insn-008e2764)
- 新版 `008e30f0`（命令位置の公開資料なし） · `008e28f4`（命令位置の公開資料なし） · `008e2900`（命令位置の公開資料なし）

~~~diff
- 008e2f54 ["INT_ADD", "register:40f0:8", ["const:8e2f54:8", "const:4:8"]]
- 008e2f54 ["CALL", null, ["callee:00c57ee0:8"]]
+ 008e30f0 ["INT_ADD", "register:40f0:8", ["const:8e30f0:8", "const:4:8"]]
+ 008e30f0 ["CALL", null, ["callee:00c57ee0:8"]]
- 008e2f54 bytes e3d20d94
+ 008e30f0 bytes 7cd30d94
- 008e2758 ["INT_ADD", "register:40f0:8", ["const:8e2758:8", "const:4:8"]]
- 008e2758 ["CALL", null, ["callee:00487e20:8"]]
+ 008e28f4 ["INT_ADD", "register:40f0:8", ["const:8e28f4:8", "const:4:8"]]
+ 008e28f4 ["CALL", null, ["callee:00487e20:8"]]
- 008e2758 bytes a295ee97
+ 008e28f4 bytes 4b95ee97
- 008e2764 ["COPY", "tmp:0:8", ["const:938:8"]]
- 008e2764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e2764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e2764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e2900 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 008e2900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e2900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e2900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e2764 bytes 08e12491
+ 008e2900 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-672a5675d9667bbaa3e910efa676e97b"></a>

### [`008e3210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3210.md) → [`008e33ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e3/008e33ac.md) FUN_008e33ac

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008e6510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e6/008e6510.md) · 呼出先 22件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6eec.md) [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md)
- 新版 呼出元 1件 [`008e66ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e6/008e66ac.md) · 呼出先 22件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f30.md) [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.69% / 新版 81.69%

CFGの説明率　旧版 72.38% / 新版 72.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_value` 4件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 15件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e3360"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e3370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e338c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e33f0",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008e33fc",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e3404",
      "PARAM",
      [
        "storage",
        "00c73410",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008e33f0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008e33fc",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e3404",
      "PARAM",
      [
        "storage",
        "00c73810",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e328c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3210.md#insn-008e328c) · [`008e333c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3210.md#insn-008e333c) · [`008e3360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3210.md#insn-008e3360)
- 新版 `008e34d8`（命令位置の公開資料なし）

~~~diff
- 008e328c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008e328c ["COPY", "tmp:1:4", ["register:4000:4"]]
- 008e328c ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 008e328c ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 008e328c bytes 1ba4801a
- 008e333c ["COPY", "register:0:8", ["register:4040:8"]]
- 008e333c ["INT_ADD", "register:40f0:8", ["const:8e333c:8", "const:4:8"]]
- 008e333c ["CALLIND", null, ["register:0:8"]]
+ 008e34d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008e34d8 ["INT_ADD", "register:40f0:8", ["const:8e34d8:8", "const:4:8"]]
+ 008e34d8 ["CALLIND", null, ["register:0:8"]]
- 008e333c bytes 00013fd6
+ 008e34d8 bytes 00013fd6
- 008e3360 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 008e3360 ["COPY", "tmp:1:8", ["const:0:8"]]
- 008e3360 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 008e3360 bytes ff1300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d59af0ca9d19eb2911f6e52a097d4d9d"></a>

### [`008e3bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3bb4.md) → [`008e3d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e3/008e3d50.md) FUN_008e3d50

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006b3440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3440.md) · 呼出先 21件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046a210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a210.md)
- 新版 呼出元 1件 [`006b3480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3480.md) · 呼出先 21件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008e3d9c",
      "incomplete_value": true,
      "site": "008e3d9c",
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
      "definition_site": "008e3c00",
      "incomplete_value": true,
      "site": "008e3c00",
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
      "definition_site": "008e3da4",
      "incomplete_value": false,
      "site": "008e3db4",
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
      "definition_site": "008e3c08",
      "incomplete_value": false,
      "site": "008e3c18",
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
      "definition_site": "008e3dac",
      "incomplete_value": false,
      "site": "008e3db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e3c10",
      "incomplete_value": false,
      "site": "008e3c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:410:8"
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
      "008e3d98",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008e3da4",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e3dac",
      "PARAM",
      [
        "storage",
        "00c73410",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008e3d98",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008e3da4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e3dac",
      "PARAM",
      [
        "storage",
        "00c73810",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e3c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3bb4.md#insn-008e3c18) · [`008e3c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3bb4.md#insn-008e3c60) · [`008e3ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3bb4.md#insn-008e3ca4)
- 新版 `008e3db4`（命令位置の公開資料なし） · `008e3dfc`（命令位置の公開資料なし） · `008e3e40`（命令位置の公開資料なし）

~~~diff
- 008e3c18 ["INT_ADD", "register:40f0:8", ["const:8e3c18:8", "const:4:8"]]
- 008e3c18 ["CALL", null, ["callee:00c58610:8"]]
+ 008e3db4 ["INT_ADD", "register:40f0:8", ["const:8e3db4:8", "const:4:8"]]
+ 008e3db4 ["CALL", null, ["callee:00c58610:8"]]
- 008e3c18 bytes 7ed10d94
+ 008e3db4 bytes 17d20d94
- 008e3c60 ["INT_ADD", "register:40f0:8", ["const:8e3c60:8", "const:4:8"]]
- 008e3c60 ["CALL", null, ["ram:46c984:8"]]
+ 008e3dfc ["INT_ADD", "register:40f0:8", ["const:8e3dfc:8", "const:4:8"]]
+ 008e3dfc ["CALL", null, ["ram:46c9c4:8"]]
- 008e3c60 bytes 4923ee97
+ 008e3dfc bytes f222ee97
- 008e3ca4 ["INT_ADD", "register:40f0:8", ["const:8e3ca4:8", "const:4:8"]]
- 008e3ca4 ["CALL", null, ["ram:46c984:8"]]
+ 008e3e40 ["INT_ADD", "register:40f0:8", ["const:8e3e40:8", "const:4:8"]]
+ 008e3e40 ["CALL", null, ["ram:46c9c4:8"]]
- 008e3ca4 bytes 3823ee97
+ 008e3e40 bytes e122ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e8a56753cd5ab5fd3a575bbf61e91b0"></a>

### [`008e465c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e465c.md) → [`008e47f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e47f8.md) FUN_008e47f8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006b2968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b2968.md) · 呼出先 11件 [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00597dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597dc8.md) [`00597e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`006b29a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b29a8.md) · 呼出先 11件 [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00597e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e08.md) [`00597e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e48.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "site": "008e488c",
      "value": [
        "leaf",
        "ram:a84c48:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e46f0",
      "value": [
        "leaf",
        "ram:a84a50:8"
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
      "site": "008e48c4",
      "value": [
        "leaf",
        "ram:a84c68:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e4728",
      "value": [
        "leaf",
        "ram:a84a70:8"
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
      "008e488c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84a50"
      ]
    ],
    [
      "008e48c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84a70"
      ]
    ]
  ],
  "added": [
    [
      "008e488c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84c48"
      ]
    ],
    [
      "008e48c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84c68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e46f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e465c.md#insn-008e46f0) · [`008e4728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e465c.md#insn-008e4728) · [`008e4684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e465c.md#insn-008e4684)
- 新版 `008e488c`（命令位置の公開資料なし） · `008e48c4`（命令位置の公開資料なし） · `008e4820`（命令位置の公開資料なし）

~~~diff
- 008e46f0 ["INT_ADD", "register:40f0:8", ["const:8e46f0:8", "const:4:8"]]
- 008e46f0 ["CALL", null, ["ram:a84a50:8"]]
+ 008e488c ["INT_ADD", "register:40f0:8", ["const:8e488c:8", "const:4:8"]]
+ 008e488c ["CALL", null, ["ram:a84c48:8"]]
- 008e46f0 bytes d8800694
+ 008e488c bytes ef800694
- 008e4728 ["INT_ADD", "register:40f0:8", ["const:8e4728:8", "const:4:8"]]
- 008e4728 ["CALL", null, ["ram:a84a70:8"]]
+ 008e48c4 ["INT_ADD", "register:40f0:8", ["const:8e48c4:8", "const:4:8"]]
+ 008e48c4 ["CALL", null, ["ram:a84c68:8"]]
- 008e4728 bytes d2800694
+ 008e48c4 bytes e9800694
- 008e4684 ["INT_ADD", "register:40f0:8", ["const:8e4684:8", "const:4:8"]]
- 008e4684 ["CALL", null, ["callee:008514f8:8"]]
+ 008e4820 ["INT_ADD", "register:40f0:8", ["const:8e4820:8", "const:4:8"]]
+ 008e4820 ["CALL", null, ["callee:008514f8:8"]]
- 008e4684 bytes 8db3fd97
+ 008e4820 bytes 36b3fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b969b09d9a8681fdcfb7ef95a085fa4f"></a>

### [`008e4804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4804.md) → [`008e49a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e49a0.md) FUN_008e49a0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008e9af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9af0.md) · 呼出先 26件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 1件 [`008e9c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9c8c.md) · 呼出先 26件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.13% / 新版 94.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e4b28",
      "incomplete_value": true,
      "site": "008e4b3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b14:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e498c",
      "incomplete_value": true,
      "site": "008e49a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ad4:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "008e4b40",
      "incomplete_value": true,
      "site": "008e4b40",
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
      "definition_site": "008e49a4",
      "incomplete_value": true,
      "site": "008e49a4",
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
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008e4f8c",
      "incomplete_value": false,
      "site": "008e4f8c",
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
      "definition_site": "008e4df0",
      "incomplete_value": false,
      "site": "008e4df0",
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
    "ordinal": 53,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e4b14",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "008e4b28",
      "READ",
      [
        "storage",
        "002aead4",
        null,
        "string"
      ]
    ],
    [
      "008e4b2c",
      "READ",
      [
        "storage",
        "002aeae1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e4b14",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "008e4b28",
      "READ",
      [
        "storage",
        "002aeb14",
        null,
        "string"
      ]
    ],
    [
      "008e4b2c",
      "READ",
      [
        "storage",
        "002aeb21",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e48fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4804.md#insn-008e48fc) · [`008e49ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4804.md#insn-008e49ac) · [`008e49ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4804.md#insn-008e49ec)
- 新版 `008e4a98`（命令位置の公開資料なし） · `008e4b48`（命令位置の公開資料なし） · `008e4b88`（命令位置の公開資料なし）

~~~diff
- 008e48fc ["INT_ADD", "register:40f0:8", ["const:8e48fc:8", "const:4:8"]]
- 008e48fc ["CALL", null, ["callee:008e27ec:8"]]
+ 008e4a98 ["INT_ADD", "register:40f0:8", ["const:8e4a98:8", "const:4:8"]]
+ 008e4a98 ["CALL", null, ["callee:008e27ec:8"]]
- 008e48fc bytes 55f7ff97
+ 008e4a98 bytes 55f7ff97
- 008e49ac ["INT_ADD", "register:40f0:8", ["const:8e49ac:8", "const:4:8"]]
- 008e49ac ["CALL", null, ["ram:71d16c:8"]]
+ 008e4b48 ["INT_ADD", "register:40f0:8", ["const:8e4b48:8", "const:4:8"]]
+ 008e4b48 ["CALL", null, ["ram:71d1ac:8"]]
- 008e49ac bytes f0e1f897
+ 008e4b48 bytes 99e1f897
- 008e49ec ["INT_ADD", "register:40f0:8", ["const:8e49ec:8", "const:4:8"]]
- 008e49ec ["CALL", null, ["callee:0047e60c:8"]]
+ 008e4b88 ["INT_ADD", "register:40f0:8", ["const:8e4b88:8", "const:4:8"]]
+ 008e4b88 ["CALL", null, ["callee:0047e60c:8"]]
- 008e49ec bytes f866ee97
+ 008e4b88 bytes a166ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1c6229df58e4332be08aead20e49049"></a>

### [`008e5048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5048.md) → [`008e51e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e5/008e51e4.md) FUN_008e51e4

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008ea120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea120.md) · 呼出先 20件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`006df504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006df504.md)
- 新版 呼出元 1件 [`008ea2bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea2bc.md) · 呼出先 20件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`006df544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006df/006df544.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.34% / 新版 85.34%

CFGの説明率　旧版 73.96% / 新版 74.40%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e5254",
      "incomplete_value": true,
      "site": "008e5264",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2f9000:8"
              ],
              [
                "leaf",
                "const:a90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e50b8",
      "incomplete_value": true,
      "site": "008e50c8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2f9000:8"
              ],
              [
                "leaf",
                "const:a50:8"
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
      "definition_site": "008e5254",
      "incomplete_value": true,
      "site": "008e5264",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008e50b8",
      "incomplete_value": true,
      "site": "008e50c8",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e52d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e5254",
      "READ",
      [
        "storage",
        "002f9a50",
        null,
        null
      ]
    ],
    [
      "008e5254",
      "READ",
      [
        "storage",
        "002f9a60",
        null,
        null
      ]
    ],
    [
      "unmatched:008e51d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e5444"
      ]
    ]
  ],
  "added": [
    [
      "008e5254",
      "READ",
      [
        "storage",
        "002f9a90",
        null,
        null
      ]
    ],
    [
      "008e5254",
      "READ",
      [
        "storage",
        "002f9aa0",
        null,
        null
      ]
    ],
    [
      "008e5370",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e5444"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5048.md#insn-008e51bc) · [`008e51d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5048.md#insn-008e51d4) · [`008e51dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5048.md#insn-008e51dc)
- 新版 `008e5358`（命令位置の公開資料なし） · `008e5378`（命令位置の公開資料なし）

~~~diff
- 008e51bc ["INT_ADD", "register:40f0:8", ["const:8e51bc:8", "const:4:8"]]
- 008e51bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 008e5358 ["INT_ADD", "register:40f0:8", ["const:8e5358:8", "const:4:8"]]
+ 008e5358 ["CALL", null, ["callee:00c57eb0:8"]]
- 008e51bc bytes 3dca0d94
+ 008e5358 bytes d6ca0d94
- 008e51d4 ["CBRANCH", null, ["local:b29:8", "register:101:1"]]
- 008e51d4 bytes a0060054
- 008e51dc ["BRANCH", null, ["local:b15:8"]]
+ 008e5378 ["BRANCH", null, ["local:b16:8"]]
- 008e51dc bytes 04000014
+ 008e5378 bytes 04000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2965b7c4afe612c81f640c35f67c07e3"></a>

### [`008e5de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5de0.md) → [`008e5f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e5/008e5f7c.md) FUN_008e5f7c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006b2968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b2968.md) · 呼出先 24件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004476b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md)
- 新版 呼出元 1件 [`006b29a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b29a8.md) · 呼出先 24件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.45% / 新版 81.45%

CFGの説明率　旧版 56.41% / 新版 57.39%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 24件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e5e88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e5e8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e5e90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e6004",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:008e5e7c",
      "READ",
      [
        "storage",
        "002a7e24",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008e5e80",
      "READ",
      [
        "storage",
        "002a7e2a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e6004",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "008e6018",
      "READ",
      [
        "storage",
        "002a7f00",
        null,
        "string"
      ]
    ],
    [
      "008e601c",
      "READ",
      [
        "storage",
        "002a7f06",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e5e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5de0.md#insn-008e5e88) · [`008e5e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5de0.md#insn-008e5e8c) · [`008e5e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5de0.md#insn-008e5e90)

~~~diff
- 008e5e88 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008e5e88 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:58:8"]]
- 008e5e88 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008e5e88 bytes e8630139
- 008e5e8c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 008e5e8c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:59:8"]]
- 008e5e8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008e5e8c bytes ea9305f8
- 008e5e90 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008e5e90 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:5f:8"]]
- 008e5e90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008e5e90 bytes e9f305f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69889dc8ccea24206cf1d4e6c192dcf7"></a>

### [`008e6510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e6/008e6510.md) → [`008e66ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e6/008e66ac.md) FUN_008e66ac

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006b2b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b2b1c.md) · 呼出先 42件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0044e948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e948.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`0046d934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d934.md)
- 新版 呼出元 1件 [`006b2b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b2b5c.md) · 呼出先 42件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0044e988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e988.md) [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`0046d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.61% / 新版 94.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 11件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e67a4",
      "incomplete_value": true,
      "site": "008e67a4",
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
                "const:263:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e6608",
      "incomplete_value": true,
      "site": "008e6608",
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
                "const:223:8"
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
      "definition_site": "008e6848",
      "incomplete_value": true,
      "site": "008e6848",
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
                "const:b14:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e66ac",
      "incomplete_value": true,
      "site": "008e66ac",
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
                "const:ad4:8"
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
      "definition_site": "008e6860",
      "incomplete_value": false,
      "site": "008e6860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e66c4",
      "incomplete_value": false,
      "site": "008e66c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "008e6724",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "008e673c",
      "DATA",
      [
        "storage",
        "0039b1bc",
        "fde_0039b1bc",
        "dword"
      ]
    ],
    [
      "008e6754",
      "DATA",
      [
        "storage",
        "0039b1bc",
        "fde_0039b1bc",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "008e6724",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "008e673c",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "uleb128"
      ]
    ],
    [
      "008e6754",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "uleb128"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e65dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e6/008e6510.md#insn-008e65dc) · [`008e6708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e6/008e6510.md#insn-008e6708) · [`008e6764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e6/008e6510.md#insn-008e6764)
- 新版 `008e6778`（命令位置の公開資料なし） · `008e68a4`（命令位置の公開資料なし） · `008e6900`（命令位置の公開資料なし）

~~~diff
- 008e65dc ["INT_ADD", "register:40f0:8", ["const:8e65dc:8", "const:4:8"]]
- 008e65dc ["CALL", null, ["ram:48ccb8:8"]]
+ 008e6778 ["INT_ADD", "register:40f0:8", ["const:8e6778:8", "const:4:8"]]
+ 008e6778 ["CALL", null, ["ram:48ccf8:8"]]
- 008e65dc bytes b799ee97
+ 008e6778 bytes 6099ee97
- 008e6708 ["INT_ADD", "register:40f0:8", ["const:8e6708:8", "const:4:8"]]
- 008e6708 ["CALL", null, ["ram:48ccb8:8"]]
+ 008e68a4 ["INT_ADD", "register:40f0:8", ["const:8e68a4:8", "const:4:8"]]
+ 008e68a4 ["CALL", null, ["ram:48ccf8:8"]]
- 008e6708 bytes 6c99ee97
+ 008e68a4 bytes 1599ee97
- 008e6764 ["INT_ADD", "register:40f0:8", ["const:8e6764:8", "const:4:8"]]
- 008e6764 ["CALL", null, ["ram:47acb4:8"]]
+ 008e6900 ["INT_ADD", "register:40f0:8", ["const:8e6900:8", "const:4:8"]]
+ 008e6900 ["CALL", null, ["ram:47acf4:8"]]
- 008e6764 bytes 5451ee97
+ 008e6900 bytes fd50ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcd9b5c18c9fdcb3ce4c9afdf59bddfb"></a>

### [`008e7234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e7/008e7234.md) → [`008e73d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e7/008e73d0.md) FUN_008e73d0

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006b3440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3440.md) · 呼出先 15件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f0c.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md)
- 新版 呼出元 1件 [`006b3480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3480.md) · 呼出先 15件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f4c.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 81.52% / 新版 81.52%

CFGの説明率　旧版 63.64% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `call_target` 2件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008e7414",
      "incomplete_value": true,
      "site": "008e7414",
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
      "definition_site": "008e7278",
      "incomplete_value": true,
      "site": "008e7278",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008e75b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008e7658"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e7410",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008e741c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e7424",
      "PARAM",
      [
        "storage",
        "00c73410",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008e7410",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008e741c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e7424",
      "PARAM",
      [
        "storage",
        "00c73810",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e7290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e7/008e7234.md#insn-008e7290) · [`008e7418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e7/008e7234.md#insn-008e7418) · [`008e742c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e7/008e7234.md#insn-008e742c)
- 新版 `008e742c`（命令位置の公開資料なし） · `008e75b4`（命令位置の公開資料なし） · `008e75c8`（命令位置の公開資料なし）

~~~diff
- 008e7290 ["INT_ADD", "register:40f0:8", ["const:8e7290:8", "const:4:8"]]
- 008e7290 ["CALL", null, ["callee:00c58610:8"]]
+ 008e742c ["INT_ADD", "register:40f0:8", ["const:8e742c:8", "const:4:8"]]
+ 008e742c ["CALL", null, ["callee:00c58610:8"]]
- 008e7290 bytes e0c30d94
+ 008e742c bytes 79c40d94
- 008e7418 ["INT_ADD", "register:40f0:8", ["const:8e7418:8", "const:4:8"]]
- 008e7418 ["CALL", null, ["callee:0046bd54:8"]]
+ 008e75b4 ["INT_ADD", "register:40f0:8", ["const:8e75b4:8", "const:4:8"]]
+ 008e75b4 ["CALL", null, ["callee:0046bd54:8"]]
- 008e7418 bytes 3f12ee97
+ 008e75b4 bytes e811ee97
- 008e742c ["INT_ADD", "register:40f0:8", ["const:8e742c:8", "const:4:8"]]
- 008e742c ["CALL", null, ["callee:008514f8:8"]]
+ 008e75c8 ["INT_ADD", "register:40f0:8", ["const:8e75c8:8", "const:4:8"]]
+ 008e75c8 ["CALL", null, ["callee:008514f8:8"]]
- 008e742c bytes 23a8fd97
+ 008e75c8 bytes cca7fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dba611d937e88e86dbeb0a3d0197e8ec"></a>

### [`008e78cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e7/008e78cc.md) → [`008e7a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e7/008e7a68.md) FUN_008e7a68

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006b3440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3440.md) · 呼出先 15件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046a8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a8a8.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md)
- 新版 呼出元 1件 [`006b3480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3480.md) · 呼出先 15件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046a8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a8e8.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.93% / 新版 66.93%

CFGの説明率　旧版 27.85% / 新版 28.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 2件, `unresolved_branch_alignment` 35件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 20件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e7960"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e7bf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e7bfc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008e7934",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e7ad8"
      ]
    ],
    [
      "unmatched:008e7964",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e7b18"
      ]
    ],
    [
      "unmatched:008e7a94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e8058"
      ]
    ]
  ],
  "added": [
    [
      "008e7ad0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e7ad8"
      ]
    ],
    [
      "008e7b00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e7b18"
      ]
    ],
    [
      "008e7c30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e8058"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e7960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e7/008e78cc.md#insn-008e7960) · [`008e7a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e7/008e78cc.md#insn-008e7a60)
- 新版 `008e7bfc`（命令位置の公開資料なし） · `008e7afc`（命令位置の公開資料なし）

~~~diff
- 008e7960 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2e0:8"]]
- 008e7960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008e7960 bytes 747201f9
- 008e7a60 ["INT_ADD", "register:40f0:8", ["const:8e7a60:8", "const:4:8"]]
- 008e7a60 ["CALL", null, ["callee:00c58000:8"]]
+ 008e7bfc ["INT_ADD", "register:40f0:8", ["const:8e7bfc:8", "const:4:8"]]
+ 008e7bfc ["CALL", null, ["callee:00c58000:8"]]
- 008e7a60 bytes 68c00d94
+ 008e7bfc bytes 01c10d94
+ 008e7afc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2e0:8"]]
+ 008e7afc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 008e7afc bytes 747201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-085df0527d61f65d04fb46d540840fa0"></a>

### [`008e80c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e80c8.md) → [`008e8264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8264.md) FUN_008e8264

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008e2f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2f58.md) [`008e4804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4804.md) [`008e84b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`008e30f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e3/008e30f4.md) [`008e49a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e49a0.md) [`008e8650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8650.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "008e8270",
      "incomplete_value": false,
      "site": "008e8274",
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
      "definition_site": "008e80d4",
      "incomplete_value": false,
      "site": "008e80d8",
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
      "008e8270",
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
      "008e8270",
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

- 旧版 [`008e80d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e80c8.md#insn-008e80d8) · [`008e80d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e80c8.md#insn-008e80d4)
- 新版 `008e8274`（命令位置の公開資料なし） · `008e8270`（命令位置の公開資料なし）

~~~diff
- 008e80d8 ["INT_ADD", "register:40f0:8", ["const:8e80d8:8", "const:4:8"]]
- 008e80d8 ["CALL", null, ["callee:0043b778:8"]]
+ 008e8274 ["INT_ADD", "register:40f0:8", ["const:8e8274:8", "const:4:8"]]
+ 008e8274 ["CALL", null, ["callee:0043b778:8"]]
- 008e80d8 bytes 984ded97
+ 008e8274 bytes 414ded97
- 008e80d4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 008e80d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e80d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e80d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e8270 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 008e8270 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8270 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8270 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e80d4 bytes 00303c91
+ 008e8270 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c176a2c0c84e88f106cf8ce5577d3ba4"></a>

### [`008e83b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e83b0.md) → [`008e854c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e854c.md) FUN_008e854c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008e81cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e81cc.md) [`008e8ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ca4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`008e8368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8368.md) [`008e8e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8e40.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "008e8558",
      "incomplete_value": false,
      "site": "008e855c",
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
      "definition_site": "008e83bc",
      "incomplete_value": false,
      "site": "008e83c0",
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
      "008e8558",
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
      "008e8558",
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

- 旧版 [`008e83c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e83b0.md#insn-008e83c0) · [`008e83bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e83b0.md#insn-008e83bc)
- 新版 `008e855c`（命令位置の公開資料なし） · `008e8558`（命令位置の公開資料なし）

~~~diff
- 008e83c0 ["INT_ADD", "register:40f0:8", ["const:8e83c0:8", "const:4:8"]]
- 008e83c0 ["CALL", null, ["callee:0043b778:8"]]
+ 008e855c ["INT_ADD", "register:40f0:8", ["const:8e855c:8", "const:4:8"]]
+ 008e855c ["CALL", null, ["callee:0043b778:8"]]
- 008e83c0 bytes de4ced97
+ 008e855c bytes 874ced97
- 008e83bc ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 008e83bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e83bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e83bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e8558 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 008e8558 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8558 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8558 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e83bc bytes 00303c91
+ 008e8558 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68674cf5947dfd754bb9ed46c1c3faa8"></a>

### [`008e84a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84a0.md) → [`008e863c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e863c.md) FUN_008e863c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008e43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e43f4.md) [`008e8b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8b1c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`008e4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e4590.md) [`008e8cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8cb8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "008e8648",
      "incomplete_value": false,
      "site": "008e864c",
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
      "definition_site": "008e84ac",
      "incomplete_value": false,
      "site": "008e84b0",
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
      "008e8648",
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
      "008e8648",
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

- 旧版 [`008e84b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84a0.md#insn-008e84b0) · [`008e84ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84a0.md#insn-008e84ac)
- 新版 `008e864c`（命令位置の公開資料なし） · `008e8648`（命令位置の公開資料なし）

~~~diff
- 008e84b0 ["INT_ADD", "register:40f0:8", ["const:8e84b0:8", "const:4:8"]]
- 008e84b0 ["CALL", null, ["callee:0043b778:8"]]
+ 008e864c ["INT_ADD", "register:40f0:8", ["const:8e864c:8", "const:4:8"]]
+ 008e864c ["CALL", null, ["callee:0043b778:8"]]
- 008e84b0 bytes a24ced97
+ 008e864c bytes 4b4ced97
- 008e84ac ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 008e84ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e84ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e84ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e8648 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 008e8648 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8648 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8648 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e84ac bytes 00303c91
+ 008e8648 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1650b1ed5fa0af678eabab99b0d97e79"></a>

### [`008e8670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8670.md) → [`008e880c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e880c.md) FUN_008e880c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008e2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md) [`008e43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e43f4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`008e28bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e2/008e28bc.md) [`008e4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e4590.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "008e8818",
      "incomplete_value": false,
      "site": "008e881c",
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
      "definition_site": "008e867c",
      "incomplete_value": false,
      "site": "008e8680",
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
      "008e8818",
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
      "008e8818",
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

- 旧版 [`008e8680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8670.md#insn-008e8680) · [`008e867c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8670.md#insn-008e867c)
- 新版 `008e881c`（命令位置の公開資料なし） · `008e8818`（命令位置の公開資料なし）

~~~diff
- 008e8680 ["INT_ADD", "register:40f0:8", ["const:8e8680:8", "const:4:8"]]
- 008e8680 ["CALL", null, ["callee:0043b778:8"]]
+ 008e881c ["INT_ADD", "register:40f0:8", ["const:8e881c:8", "const:4:8"]]
+ 008e881c ["CALL", null, ["callee:0043b778:8"]]
- 008e8680 bytes 2e4ced97
+ 008e881c bytes d74bed97
- 008e867c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 008e867c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e867c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e867c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e8818 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 008e8818 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8818 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8818 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e867c bytes 00303c91
+ 008e8818 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb3a2f4e7638f101fa3c26e81abed972"></a>

### [`008e8868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8868.md) → [`008e8a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8a04.md) FUN_008e8a04

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008e8684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8684.md) [`008e8dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8dec.md) [`008ea3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea3fc.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`008e8820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8820.md) [`008e8f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8f88.md) [`008ea598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea598.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "008e8a10",
      "incomplete_value": false,
      "site": "008e8a14",
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
      "definition_site": "008e8874",
      "incomplete_value": false,
      "site": "008e8878",
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
      "008e8a10",
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
      "008e8a10",
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

- 旧版 [`008e8878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8868.md#insn-008e8878) · [`008e8874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8868.md#insn-008e8874)
- 新版 `008e8a14`（命令位置の公開資料なし） · `008e8a10`（命令位置の公開資料なし）

~~~diff
- 008e8878 ["INT_ADD", "register:40f0:8", ["const:8e8878:8", "const:4:8"]]
- 008e8878 ["CALL", null, ["callee:0043b778:8"]]
+ 008e8a14 ["INT_ADD", "register:40f0:8", ["const:8e8a14:8", "const:4:8"]]
+ 008e8a14 ["CALL", null, ["callee:0043b778:8"]]
- 008e8878 bytes b04bed97
+ 008e8a14 bytes 594bed97
- 008e8874 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 008e8874 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e8874 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e8874 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e8a10 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 008e8a10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8a10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8a10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e8874 bytes 00303c91
+ 008e8a10 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a59babd5d1e0e3b584233d39d1a800e"></a>

### [`008e8ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ab4.md) → [`008e8c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8c50.md) FUN_008e8c50

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008e88d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e88d0.md) [`008e8f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8f9c.md) [`008ea200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea200.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`008e8a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8a6c.md) [`008e9138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9138.md) [`008ea39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea39c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "008e8c5c",
      "incomplete_value": false,
      "site": "008e8c60",
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
      "definition_site": "008e8ac0",
      "incomplete_value": false,
      "site": "008e8ac4",
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
      "008e8c5c",
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
      "008e8c5c",
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

- 旧版 [`008e8ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ab4.md#insn-008e8ac4) · [`008e8ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ab4.md#insn-008e8ac0)
- 新版 `008e8c60`（命令位置の公開資料なし） · `008e8c5c`（命令位置の公開資料なし）

~~~diff
- 008e8ac4 ["INT_ADD", "register:40f0:8", ["const:8e8ac4:8", "const:4:8"]]
- 008e8ac4 ["CALL", null, ["callee:0043b778:8"]]
+ 008e8c60 ["INT_ADD", "register:40f0:8", ["const:8e8c60:8", "const:4:8"]]
+ 008e8c60 ["CALL", null, ["callee:0043b778:8"]]
- 008e8ac4 bytes 1d4bed97
+ 008e8c60 bytes c64aed97
- 008e8ac0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 008e8ac0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e8ac0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e8ac0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e8c5c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 008e8c5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8c5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8c5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e8ac0 bytes 00303c91
+ 008e8c5c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4832058d189cf7c7a1b2dff3f2cd8679"></a>

### [`008e8f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8f9c.md) → [`008e9138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9138.md) FUN_008e9138

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008e2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`008e8ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ab4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008e28bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e2/008e28bc.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`008e8c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8c50.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.59% / 新版 86.59%

CFGの説明率　旧版 42.31% / 新版 39.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e9034"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e9038"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e903c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008e8fc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e9274"
      ]
    ],
    [
      "unmatched:008e9080",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e91f0"
      ]
    ]
  ],
  "added": [
    [
      "008e9164",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e9274"
      ]
    ],
    [
      "008e921c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e91f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e8fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8f9c.md#insn-008e8fc8) · [`008e9034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8f9c.md#insn-008e9034) · [`008e9038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8f9c.md#insn-008e9038)

~~~diff
- 008e8fc8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 008e8fc8 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 008e8fc8 bytes 8a0800b5
- 008e9034 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008e9034 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008e9034 bytes 2a0100f9
- 008e9038 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:18:8"]]
- 008e9038 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008e9038 bytes 280d00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b40bb1bb8d87babb9e5eba692ffcaf40"></a>

### [`008e90e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e90e4.md) → [`008e9280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9280.md) FUN_008e9280

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 88.89% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e90fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e90e4.md#insn-008e90fc) · [`008e9104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e90e4.md#insn-008e9104) · [`008e912c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e90e4.md#insn-008e912c)
- 新版 `008e9298`（命令位置の公開資料なし） · `008e92a0`（命令位置の公開資料なし） · `008e92c8`（命令位置の公開資料なし）

~~~diff
- 008e90fc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008e90fc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 008e9298 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008e9298 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 008e90fc bytes 21010054
+ 008e9298 bytes 21010054
- 008e9104 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008e9104 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 008e92a0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 008e92a0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 008e9104 bytes e00100b4
+ 008e92a0 bytes e00100b4
- 008e912c ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 008e912c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 008e912c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 008e912c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 008e92c8 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
+ 008e92c8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 008e92c8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 008e92c8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 008e912c bytes 4aff0736
+ 008e92c8 bytes 4aff0736
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0a3fa83ef3bb957571a90833bbde112"></a>

### [`008e9184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9184.md) → [`008e9320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9320.md) FUN_008e9320

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
      "definition_site": "008e932c",
      "incomplete_value": false,
      "site": "008e932c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9190",
      "incomplete_value": false,
      "site": "008e9190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
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
      "008e932c",
      "DATA",
      [
        "storage",
        "00c84ce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e932c",
      "DATA",
      [
        "storage",
        "00c850e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9184.md#insn-008e9188) · [`008e918c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9184.md#insn-008e918c)
- 新版 `008e9324`（命令位置の公開資料なし） · `008e9328`（命令位置の公開資料なし）

~~~diff
- 008e9188 ["COPY", "register:4048:8", ["const:c84000:8"]]
+ 008e9324 ["COPY", "register:4048:8", ["const:c85000:8"]]
- 008e9188 bytes c91c00f0
+ 008e9324 bytes e91c0090
- 008e918c ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 008e918c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008e918c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008e918c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008e9328 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 008e9328 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008e9328 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008e9328 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008e918c bytes 29813391
+ 008e9328 bytes 29810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4768c72c67ec6f2ddb8ea40a4cc47cd9"></a>

### [`008e91a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e91a0.md) → [`008e933c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e933c.md) FUN_008e933c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`008e3af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3af0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`008e3c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e3/008e3c8c.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 50.00% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008e9248"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008e93e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e93f4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e9258",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "unmatched:008e9248",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e941c"
      ]
    ],
    [
      "008e93f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008e9400",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008e93e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e941c"
      ]
    ],
    [
      "008e93f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008e9400",
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

- 旧版 [`008e9248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e91a0.md#insn-008e9248) · [`008e9258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e91a0.md#insn-008e9258) · [`008e9264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e91a0.md#insn-008e9264)
- 新版 `008e93f4`（命令位置の公開資料なし） · `008e9400`（命令位置の公開資料なし）

~~~diff
- 008e9248 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 008e9248 bytes c0010054
- 008e9258 ["INT_ADD", "register:40f0:8", ["const:8e9258:8", "const:4:8"]]
- 008e9258 ["CALL", null, ["ram:47acb4:8"]]
+ 008e93f4 ["INT_ADD", "register:40f0:8", ["const:8e93f4:8", "const:4:8"]]
+ 008e93f4 ["CALL", null, ["ram:47acf4:8"]]
- 008e9258 bytes 9746ee97
+ 008e93f4 bytes 4046ee97
- 008e9264 ["INT_ADD", "register:40f0:8", ["const:8e9264:8", "const:4:8"]]
- 008e9264 ["CALL", null, ["ram:47acb4:8"]]
+ 008e9400 ["INT_ADD", "register:40f0:8", ["const:8e9400:8", "const:4:8"]]
+ 008e9400 ["CALL", null, ["ram:47acf4:8"]]
- 008e9264 bytes 9446ee97
+ 008e9400 bytes 3d46ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24d5f57ba1e4ed251bf4b0881d6c73c9"></a>

### [`008e9304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9304.md) → [`008e94a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e94a0.md) FUN_008e94a0

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
      "definition_site": "008e94ac",
      "incomplete_value": false,
      "site": "008e94ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9310",
      "incomplete_value": false,
      "site": "008e9310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:d60:8"
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
      "008e94ac",
      "DATA",
      [
        "storage",
        "00c84d60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e94ac",
      "DATA",
      [
        "storage",
        "00c85160",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9304.md#insn-008e9308) · [`008e930c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9304.md#insn-008e930c)
- 新版 `008e94a4`（命令位置の公開資料なし） · `008e94a8`（命令位置の公開資料なし）

~~~diff
- 008e9308 ["COPY", "register:4048:8", ["const:c84000:8"]]
+ 008e94a4 ["COPY", "register:4048:8", ["const:c85000:8"]]
- 008e9308 bytes c91c00f0
+ 008e94a4 bytes e91c0090
- 008e930c ["COPY", "tmp:0:8", ["const:d60:8"]]
- 008e930c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008e930c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008e930c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008e94a8 ["COPY", "tmp:0:8", ["const:160:8"]]
+ 008e94a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008e94a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008e94a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008e930c bytes 29813591
+ 008e94a8 bytes 29810591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b88b94f8592f3583b48014a468922a92"></a>

### [`008e9320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9320.md) → [`008e94bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e94bc.md) FUN_008e94bc

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 66.67% / 新版 75.00%

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
      "site": "008e94dc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e9340",
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
      "site": "008e94e8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e934c",
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
      "008e94dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008e94e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008e950c",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "008e94dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008e94e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008e950c",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9320.md#insn-008e9340) · [`008e934c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9320.md#insn-008e934c) · [`008e9330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9320.md#insn-008e9330)
- 新版 `008e94dc`（命令位置の公開資料なし） · `008e94e8`（命令位置の公開資料なし） · `008e94cc`（命令位置の公開資料なし）

~~~diff
- 008e9340 ["INT_ADD", "register:40f0:8", ["const:8e9340:8", "const:4:8"]]
- 008e9340 ["CALL", null, ["ram:47acb4:8"]]
+ 008e94dc ["INT_ADD", "register:40f0:8", ["const:8e94dc:8", "const:4:8"]]
+ 008e94dc ["CALL", null, ["ram:47acf4:8"]]
- 008e9340 bytes 5d46ee97
+ 008e94dc bytes 0646ee97
- 008e934c ["INT_ADD", "register:40f0:8", ["const:8e934c:8", "const:4:8"]]
- 008e934c ["CALL", null, ["ram:47acb4:8"]]
+ 008e94e8 ["INT_ADD", "register:40f0:8", ["const:8e94e8:8", "const:4:8"]]
+ 008e94e8 ["CALL", null, ["ram:47acf4:8"]]
- 008e934c bytes 5a46ee97
+ 008e94e8 bytes 0346ee97
- 008e9330 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 008e94cc ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 008e9330 bytes 80010054
+ 008e94cc bytes 80010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86f25d13a66bac71e147f936c72e2063"></a>

### [`008e9424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9424.md) → [`008e95c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e95c0.md) FUN_008e95c0

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 17件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.07% / 新版 92.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e96f0",
      "incomplete_value": true,
      "site": "008e96f0",
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
                "const:7dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9554",
      "incomplete_value": true,
      "site": "008e9554",
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
                "const:79c:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008e9714",
      "incomplete_value": false,
      "site": "008e9714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9578",
      "incomplete_value": false,
      "site": "008e9578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008e9774",
      "incomplete_value": true,
      "site": "008e9774",
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
                "const:5e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e95d8",
      "incomplete_value": true,
      "site": "008e95d8",
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
                "const:51b:8"
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
      "008e95fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008e9618",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008e96d8",
      "READ",
      [
        "storage",
        "002b879c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e95fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008e9618",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008e96d8",
      "READ",
      [
        "storage",
        "002b87dc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9424.md#insn-008e9460) · [`008e947c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9424.md#insn-008e947c) · [`008e94b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9424.md#insn-008e94b8)
- 新版 `008e95fc`（命令位置の公開資料なし） · `008e9618`（命令位置の公開資料なし） · `008e9654`（命令位置の公開資料なし）

~~~diff
- 008e9460 ["INT_ADD", "register:40f0:8", ["const:8e9460:8", "const:4:8"]]
- 008e9460 ["CALL", null, ["ram:47acb4:8"]]
+ 008e95fc ["INT_ADD", "register:40f0:8", ["const:8e95fc:8", "const:4:8"]]
+ 008e95fc ["CALL", null, ["ram:47acf4:8"]]
- 008e9460 bytes 1546ee97
+ 008e95fc bytes be45ee97
- 008e947c ["INT_ADD", "register:40f0:8", ["const:8e947c:8", "const:4:8"]]
- 008e947c ["CALL", null, ["ram:47acb4:8"]]
+ 008e9618 ["INT_ADD", "register:40f0:8", ["const:8e9618:8", "const:4:8"]]
+ 008e9618 ["CALL", null, ["ram:47acf4:8"]]
- 008e947c bytes 0e46ee97
+ 008e9618 bytes b745ee97
- 008e94b8 ["INT_ADD", "register:40f0:8", ["const:8e94b8:8", "const:4:8"]]
- 008e94b8 ["CALL", null, ["callee:008514f8:8"]]
+ 008e9654 ["INT_ADD", "register:40f0:8", ["const:8e9654:8", "const:4:8"]]
+ 008e9654 ["CALL", null, ["callee:008514f8:8"]]
- 008e94b8 bytes 00a0fd97
+ 008e9654 bytes a99ffd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6df1b69370e078ee3c8c77b2e21f641a"></a>

### [`008e9910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9910.md) → [`008e9aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9aac.md) FUN_008e9aac

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
      "definition_site": "008e9acc",
      "incomplete_value": false,
      "site": "008e9ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9930",
      "incomplete_value": false,
      "site": "008e9934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
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
      "008e9ad0",
      "DATA",
      [
        "storage",
        "00c84e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9ad0",
      "DATA",
      [
        "storage",
        "00c85250",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9910.md#insn-008e9924) · [`008e992c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9910.md#insn-008e992c) · [`008e9930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9910.md#insn-008e9930)
- 新版 `008e9ac0`（命令位置の公開資料なし） · `008e9ac8`（命令位置の公開資料なし） · `008e9acc`（命令位置の公開資料なし）

~~~diff
- 008e9924 ["INT_ADD", "register:40f0:8", ["const:8e9924:8", "const:4:8"]]
- 008e9924 ["CALL", null, ["callee:00c57e90:8"]]
+ 008e9ac0 ["INT_ADD", "register:40f0:8", ["const:8e9ac0:8", "const:4:8"]]
+ 008e9ac0 ["CALL", null, ["callee:00c57e90:8"]]
- 008e9924 bytes 5bb80d94
+ 008e9ac0 bytes f4b80d94
- 008e992c ["COPY", "register:4040:8", ["const:c84000:8"]]
+ 008e9ac8 ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008e992c bytes c81c00f0
+ 008e9ac8 bytes e81c0090
- 008e9930 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 008e9930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e9acc ["COPY", "tmp:0:8", ["const:250:8"]]
+ 008e9acc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9acc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9acc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9930 bytes 08413991
+ 008e9acc bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-943bcccf44138a0147a0e3afad14b5c1"></a>

### [`008e9948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9948.md) → [`008e9ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9ae4.md) FUN_008e9ae4

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
      "definition_site": "008e9ae8",
      "incomplete_value": false,
      "site": "008e9aec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e994c",
      "incomplete_value": false,
      "site": "008e9950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
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
      "008e9aec",
      "DATA",
      [
        "storage",
        "00c84e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9aec",
      "DATA",
      [
        "storage",
        "00c85250",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9948.md#insn-008e9948) · [`008e994c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9948.md#insn-008e994c)
- 新版 `008e9ae4`（命令位置の公開資料なし） · `008e9ae8`（命令位置の公開資料なし）

~~~diff
- 008e9948 ["COPY", "register:4040:8", ["const:c84000:8"]]
+ 008e9ae4 ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008e9948 bytes c81c00f0
+ 008e9ae4 bytes e81c0090
- 008e994c ["COPY", "tmp:0:8", ["const:e50:8"]]
- 008e994c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e994c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e994c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e9ae8 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 008e9ae8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9ae8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9ae8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e994c bytes 08413991
+ 008e9ae8 bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce5c0c49362d9d29188c90c659aa701e"></a>

### [`008e9968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9968.md) → [`008e9b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9b04.md) FUN_008e9b04

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "008e9b2c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e9990",
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
      "008e9b2c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008e9b2c",
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

- 旧版 [`008e9990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9968.md#insn-008e9990) · [`008e998c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9968.md#insn-008e998c)
- 新版 `008e9b2c`（命令位置の公開資料なし） · `008e9b28`（命令位置の公開資料なし）

~~~diff
- 008e9990 ["INT_ADD", "register:40f0:8", ["const:8e9990:8", "const:4:8"]]
- 008e9990 ["CALL", null, ["ram:47acb4:8"]]
+ 008e9b2c ["INT_ADD", "register:40f0:8", ["const:8e9b2c:8", "const:4:8"]]
+ 008e9b2c ["CALL", null, ["ram:47acf4:8"]]
- 008e9990 bytes c944ee97
+ 008e9b2c bytes 7244ee97
- 008e998c ["INT_ADD", "register:40f0:8", ["const:8e998c:8", "const:4:8"]]
- 008e998c ["CALL", null, ["callee:008b9178:8"]]
+ 008e9b28 ["INT_ADD", "register:40f0:8", ["const:8e9b28:8", "const:4:8"]]
+ 008e9b28 ["CALL", null, ["callee:008b9178:8"]]
- 008e998c bytes ea3dff97
+ 008e9b28 bytes 943dff97
~~~


<a id="compare-968ddd1070211476055aeedbc15e8d96"></a>

### [`008e99d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e99d4.md) → [`008e9b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9b70.md) FUN_008e9b70

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
      "definition_site": "008e9b90",
      "incomplete_value": false,
      "site": "008e9b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e99f4",
      "incomplete_value": false,
      "site": "008e99f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
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
      "008e9b94",
      "DATA",
      [
        "storage",
        "00c84ed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9b94",
      "DATA",
      [
        "storage",
        "00c852d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e99e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e99d4.md#insn-008e99e8) · [`008e99f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e99d4.md#insn-008e99f0) · [`008e99f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e99d4.md#insn-008e99f4)
- 新版 `008e9b84`（命令位置の公開資料なし） · `008e9b8c`（命令位置の公開資料なし） · `008e9b90`（命令位置の公開資料なし）

~~~diff
- 008e99e8 ["INT_ADD", "register:40f0:8", ["const:8e99e8:8", "const:4:8"]]
- 008e99e8 ["CALL", null, ["callee:00c57e90:8"]]
+ 008e9b84 ["INT_ADD", "register:40f0:8", ["const:8e9b84:8", "const:4:8"]]
+ 008e9b84 ["CALL", null, ["callee:00c57e90:8"]]
- 008e99e8 bytes 2ab80d94
+ 008e9b84 bytes c3b80d94
- 008e99f0 ["COPY", "register:4040:8", ["const:c84000:8"]]
+ 008e9b8c ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008e99f0 bytes c81c00f0
+ 008e9b8c bytes e81c0090
- 008e99f4 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008e99f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e99f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e99f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e9b90 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 008e9b90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9b90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9b90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e99f4 bytes 08413b91
+ 008e9b90 bytes 08410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f6b96e119f9341260586ccd73c1a423"></a>

### [`008e9a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a0c.md) → [`008e9ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9ba8.md) FUN_008e9ba8

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
      "definition_site": "008e9bac",
      "incomplete_value": false,
      "site": "008e9bb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9a10",
      "incomplete_value": false,
      "site": "008e9a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
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
      "008e9bb0",
      "DATA",
      [
        "storage",
        "00c84ed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9bb0",
      "DATA",
      [
        "storage",
        "00c852d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a0c.md#insn-008e9a0c) · [`008e9a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a0c.md#insn-008e9a10)
- 新版 `008e9ba8`（命令位置の公開資料なし） · `008e9bac`（命令位置の公開資料なし）

~~~diff
- 008e9a0c ["COPY", "register:4040:8", ["const:c84000:8"]]
+ 008e9ba8 ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008e9a0c bytes c81c00f0
+ 008e9ba8 bytes e81c0090
- 008e9a10 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008e9a10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9a10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9a10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e9bac ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 008e9bac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9bac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9bac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9a10 bytes 08413b91
+ 008e9bac bytes 08410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b687e8b0764fbc9a1683ddd030a50520"></a>

### [`008e9a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a2c.md) → [`008e9bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9bc8.md) FUN_008e9bc8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "008e9bf0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e9a54",
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
      "008e9bf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008e9bf0",
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

- 旧版 [`008e9a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a2c.md#insn-008e9a54) · [`008e9a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a2c.md#insn-008e9a50)
- 新版 `008e9bf0`（命令位置の公開資料なし） · `008e9bec`（命令位置の公開資料なし）

~~~diff
- 008e9a54 ["INT_ADD", "register:40f0:8", ["const:8e9a54:8", "const:4:8"]]
- 008e9a54 ["CALL", null, ["ram:47acb4:8"]]
+ 008e9bf0 ["INT_ADD", "register:40f0:8", ["const:8e9bf0:8", "const:4:8"]]
+ 008e9bf0 ["CALL", null, ["ram:47acf4:8"]]
- 008e9a54 bytes 9844ee97
+ 008e9bf0 bytes 4144ee97
- 008e9a50 ["INT_ADD", "register:40f0:8", ["const:8e9a50:8", "const:4:8"]]
- 008e9a50 ["CALL", null, ["callee:008b9178:8"]]
+ 008e9bec ["INT_ADD", "register:40f0:8", ["const:8e9bec:8", "const:4:8"]]
+ 008e9bec ["CALL", null, ["callee:008b9178:8"]]
- 008e9a50 bytes b93dff97
+ 008e9bec bytes 633dff97
~~~


<a id="compare-4dc2cd66001212a07776557ec5ce8181"></a>

### [`008e9a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a98.md) → [`008e9c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9c34.md) FUN_008e9c34

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
      "definition_site": "008e9c54",
      "incomplete_value": false,
      "site": "008e9c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9ab8",
      "incomplete_value": false,
      "site": "008e9abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
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
      "008e9c58",
      "DATA",
      [
        "storage",
        "00c84f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9c58",
      "DATA",
      [
        "storage",
        "00c85350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a98.md#insn-008e9aac) · [`008e9ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a98.md#insn-008e9ab4) · [`008e9ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a98.md#insn-008e9ab8)
- 新版 `008e9c48`（命令位置の公開資料なし） · `008e9c50`（命令位置の公開資料なし） · `008e9c54`（命令位置の公開資料なし）

~~~diff
- 008e9aac ["INT_ADD", "register:40f0:8", ["const:8e9aac:8", "const:4:8"]]
- 008e9aac ["CALL", null, ["callee:00c57e90:8"]]
+ 008e9c48 ["INT_ADD", "register:40f0:8", ["const:8e9c48:8", "const:4:8"]]
+ 008e9c48 ["CALL", null, ["callee:00c57e90:8"]]
- 008e9aac bytes f9b70d94
+ 008e9c48 bytes 92b80d94
- 008e9ab4 ["COPY", "register:4040:8", ["const:c84000:8"]]
+ 008e9c50 ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008e9ab4 bytes c81c00f0
+ 008e9c50 bytes e81c0090
- 008e9ab8 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 008e9ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e9c54 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 008e9c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9ab8 bytes 08413d91
+ 008e9c54 bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-287e2b82f793e3d1a634cf927f472eed"></a>

### [`008e9ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9ad0.md) → [`008e9c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9c6c.md) FUN_008e9c6c

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
      "definition_site": "008e9c70",
      "incomplete_value": false,
      "site": "008e9c74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9ad4",
      "incomplete_value": false,
      "site": "008e9ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
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
      "008e9c74",
      "DATA",
      [
        "storage",
        "00c84f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9c74",
      "DATA",
      [
        "storage",
        "00c85350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9ad0.md#insn-008e9ad0) · [`008e9ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9ad0.md#insn-008e9ad4)
- 新版 `008e9c6c`（命令位置の公開資料なし） · `008e9c70`（命令位置の公開資料なし）

~~~diff
- 008e9ad0 ["COPY", "register:4040:8", ["const:c84000:8"]]
+ 008e9c6c ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008e9ad0 bytes c81c00f0
+ 008e9c6c bytes e81c0090
- 008e9ad4 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 008e9ad4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9ad4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9ad4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e9c70 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 008e9c70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9c70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9c70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9ad4 bytes 08413d91
+ 008e9c70 bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fc7cedba9804b9ec2a693a512cab3ef"></a>

### [`008e9bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bbc.md) → [`008e9d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9d58.md) FUN_008e9d58

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
      "definition_site": "008e9d7c",
      "incomplete_value": false,
      "site": "008e9d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9be0",
      "incomplete_value": false,
      "site": "008e9be0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
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
      "008e9d7c",
      "DATA",
      [
        "storage",
        "00c84fe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9d7c",
      "DATA",
      [
        "storage",
        "00c853e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bbc.md#insn-008e9bd0) · [`008e9bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bbc.md#insn-008e9bd8) · [`008e9bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bbc.md#insn-008e9bdc)
- 新版 `008e9d6c`（命令位置の公開資料なし） · `008e9d74`（命令位置の公開資料なし） · `008e9d78`（命令位置の公開資料なし）

~~~diff
- 008e9bd0 ["INT_ADD", "register:40f0:8", ["const:8e9bd0:8", "const:4:8"]]
- 008e9bd0 ["CALL", null, ["callee:00c57e90:8"]]
+ 008e9d6c ["INT_ADD", "register:40f0:8", ["const:8e9d6c:8", "const:4:8"]]
+ 008e9d6c ["CALL", null, ["callee:00c57e90:8"]]
- 008e9bd0 bytes b0b70d94
+ 008e9d6c bytes 49b80d94
- 008e9bd8 ["COPY", "register:4040:8", ["const:c84000:8"]]
+ 008e9d74 ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008e9bd8 bytes c81c00f0
+ 008e9d74 bytes e81c0090
- 008e9bdc ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 008e9bdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9bdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9bdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e9d78 ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 008e9d78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9d78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9d78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9bdc bytes 08813f91
+ 008e9d78 bytes 08810f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69ff585b6ab94e303b337cc566d311b0"></a>

### [`008e9bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bf0.md) → [`008e9d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9d8c.md) FUN_008e9d8c

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
      "definition_site": "008e9d98",
      "incomplete_value": false,
      "site": "008e9d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9bfc",
      "incomplete_value": false,
      "site": "008e9bfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
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
      "008e9d98",
      "DATA",
      [
        "storage",
        "00c84fe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9d98",
      "DATA",
      [
        "storage",
        "00c853e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bf0.md#insn-008e9bf4) · [`008e9bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bf0.md#insn-008e9bf8)
- 新版 `008e9d90`（命令位置の公開資料なし） · `008e9d94`（命令位置の公開資料なし）

~~~diff
- 008e9bf4 ["COPY", "register:4048:8", ["const:c84000:8"]]
+ 008e9d90 ["COPY", "register:4048:8", ["const:c85000:8"]]
- 008e9bf4 bytes c91c00f0
+ 008e9d90 bytes e91c0090
- 008e9bf8 ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 008e9bf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008e9bf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008e9bf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008e9d94 ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 008e9d94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008e9d94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008e9d94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008e9bf8 bytes 29813f91
+ 008e9d94 bytes 29810f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4cfccdcbb9f7e65d8186f85013504d3"></a>

### [`008e9c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9c0c.md) → [`008e9da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9da8.md) FUN_008e9da8

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9814.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9858.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.57% / 新版 84.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e9e84",
      "incomplete_value": true,
      "site": "008e9e84",
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
                "const:955:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9ce8",
      "incomplete_value": true,
      "site": "008e9ce8",
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
                "const:915:8"
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
      "definition_site": "008e9e88",
      "incomplete_value": true,
      "site": "008e9e88",
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
      "definition_site": "008e9cec",
      "incomplete_value": true,
      "site": "008e9cec",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008e9ea0",
      "incomplete_value": false,
      "site": "008e9ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9d04",
      "incomplete_value": false,
      "site": "008e9d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:d0:8"
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
      "008e9de0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008e9dfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008e9e3c",
      "DATA",
      [
        "storage",
        "00436310",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "008e9de0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008e9dfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008e9e3c",
      "DATA",
      [
        "storage",
        "00436310",
        null,
        "byte[63]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9c0c.md#insn-008e9c44) · [`008e9c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9c0c.md#insn-008e9c60) · [`008e9c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9c0c.md#insn-008e9c94)
- 新版 `008e9de0`（命令位置の公開資料なし） · `008e9dfc`（命令位置の公開資料なし） · `008e9e30`（命令位置の公開資料なし）

~~~diff
- 008e9c44 ["INT_ADD", "register:40f0:8", ["const:8e9c44:8", "const:4:8"]]
- 008e9c44 ["CALL", null, ["ram:47acb4:8"]]
+ 008e9de0 ["INT_ADD", "register:40f0:8", ["const:8e9de0:8", "const:4:8"]]
+ 008e9de0 ["CALL", null, ["ram:47acf4:8"]]
- 008e9c44 bytes 1c44ee97
+ 008e9de0 bytes c543ee97
- 008e9c60 ["INT_ADD", "register:40f0:8", ["const:8e9c60:8", "const:4:8"]]
- 008e9c60 ["CALL", null, ["ram:47acb4:8"]]
+ 008e9dfc ["INT_ADD", "register:40f0:8", ["const:8e9dfc:8", "const:4:8"]]
+ 008e9dfc ["CALL", null, ["ram:47acf4:8"]]
- 008e9c60 bytes 1544ee97
+ 008e9dfc bytes be43ee97
- 008e9c94 ["INT_ADD", "register:40f0:8", ["const:8e9c94:8", "const:4:8"]]
- 008e9c94 ["CALL", null, ["callee:008514f8:8"]]
+ 008e9e30 ["INT_ADD", "register:40f0:8", ["const:8e9e30:8", "const:4:8"]]
+ 008e9e30 ["CALL", null, ["callee:008514f8:8"]]
- 008e9c94 bytes 099efd97
+ 008e9e30 bytes b29dfd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93738b38bdce964cc83b8e02299acdbd"></a>

### [`008e9f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9f58.md) → [`008ea0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea0f4.md) FUN_008ea0f4

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
      "definition_site": "008ea118",
      "incomplete_value": false,
      "site": "008ea118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9f7c",
      "incomplete_value": false,
      "site": "008e9f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008ea118",
      "DATA",
      [
        "storage",
        "00c85050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea118",
      "DATA",
      [
        "storage",
        "00c85450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9f58.md#insn-008e9f6c) · [`008e9f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9f58.md#insn-008e9f78)
- 新版 `008ea108`（命令位置の公開資料なし） · `008ea114`（命令位置の公開資料なし）

~~~diff
- 008e9f6c ["INT_ADD", "register:40f0:8", ["const:8e9f6c:8", "const:4:8"]]
- 008e9f6c ["CALL", null, ["callee:00c57e90:8"]]
+ 008ea108 ["INT_ADD", "register:40f0:8", ["const:8ea108:8", "const:4:8"]]
+ 008ea108 ["CALL", null, ["callee:00c57e90:8"]]
- 008e9f6c bytes c9b60d94
+ 008ea108 bytes 62b70d94
- 008e9f78 ["COPY", "tmp:0:8", ["const:50:8"]]
- 008e9f78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9f78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9f78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea114 ["COPY", "tmp:0:8", ["const:450:8"]]
+ 008ea114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9f78 bytes 08410191
+ 008ea114 bytes 08411191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-615ffbeedae2eb7af8caeadc4ac189a0"></a>

### [`008e9f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9f8c.md) → [`008ea128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea128.md) FUN_008ea128

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
      "definition_site": "008ea134",
      "incomplete_value": false,
      "site": "008ea134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9f98",
      "incomplete_value": false,
      "site": "008e9f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008ea134",
      "DATA",
      [
        "storage",
        "00c85050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea134",
      "DATA",
      [
        "storage",
        "00c85450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9f8c.md#insn-008e9f94)
- 新版 `008ea130`（命令位置の公開資料なし）

~~~diff
- 008e9f94 ["COPY", "tmp:0:8", ["const:50:8"]]
- 008e9f94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008e9f94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008e9f94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ea130 ["COPY", "tmp:0:8", ["const:450:8"]]
+ 008ea130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008e9f94 bytes 29410191
+ 008ea130 bytes 29411191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d26d953871ad3444d5a880ce9f2fedb"></a>

### [`008e9fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9fa8.md) → [`008ea144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea144.md) FUN_008ea144

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "008ea16c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e9fd0",
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
      "008ea16c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008ea16c",
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

- 旧版 [`008e9fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9fa8.md#insn-008e9fd0) · [`008e9fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9fa8.md#insn-008e9fcc)
- 新版 `008ea16c`（命令位置の公開資料なし） · `008ea168`（命令位置の公開資料なし）

~~~diff
- 008e9fd0 ["INT_ADD", "register:40f0:8", ["const:8e9fd0:8", "const:4:8"]]
- 008e9fd0 ["CALL", null, ["ram:47acb4:8"]]
+ 008ea16c ["INT_ADD", "register:40f0:8", ["const:8ea16c:8", "const:4:8"]]
+ 008ea16c ["CALL", null, ["ram:47acf4:8"]]
- 008e9fd0 bytes 3943ee97
+ 008ea16c bytes e242ee97
- 008e9fcc ["INT_ADD", "register:40f0:8", ["const:8e9fcc:8", "const:4:8"]]
- 008e9fcc ["CALL", null, ["callee:008b9178:8"]]
+ 008ea168 ["INT_ADD", "register:40f0:8", ["const:8ea168:8", "const:4:8"]]
+ 008ea168 ["CALL", null, ["callee:008b9178:8"]]
- 008e9fcc bytes 5a3cff97
+ 008ea168 bytes 043cff97
~~~


<a id="compare-a23eeeab1b223adbb24ace755d186451"></a>

### [`008ea014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea014.md) → [`008ea1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea1b0.md) FUN_008ea1b0

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
      "definition_site": "008ea1d4",
      "incomplete_value": false,
      "site": "008ea1d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea038",
      "incomplete_value": false,
      "site": "008ea038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008ea1d4",
      "DATA",
      [
        "storage",
        "00c850d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea1d4",
      "DATA",
      [
        "storage",
        "00c854d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea014.md#insn-008ea028) · [`008ea034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea014.md#insn-008ea034)
- 新版 `008ea1c4`（命令位置の公開資料なし） · `008ea1d0`（命令位置の公開資料なし）

~~~diff
- 008ea028 ["INT_ADD", "register:40f0:8", ["const:8ea028:8", "const:4:8"]]
- 008ea028 ["CALL", null, ["callee:00c57e90:8"]]
+ 008ea1c4 ["INT_ADD", "register:40f0:8", ["const:8ea1c4:8", "const:4:8"]]
+ 008ea1c4 ["CALL", null, ["callee:00c57e90:8"]]
- 008ea028 bytes 9ab60d94
+ 008ea1c4 bytes 33b70d94
- 008ea034 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 008ea034 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ea034 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ea034 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea1d0 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 008ea1d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea1d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea1d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ea034 bytes 08410391
+ 008ea1d0 bytes 08411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09a56b26f108b385efd9a425b0ad508c"></a>

### [`008ea048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea048.md) → [`008ea1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea1e4.md) FUN_008ea1e4

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
      "definition_site": "008ea1f0",
      "incomplete_value": false,
      "site": "008ea1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea054",
      "incomplete_value": false,
      "site": "008ea054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008ea1f0",
      "DATA",
      [
        "storage",
        "00c850d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea1f0",
      "DATA",
      [
        "storage",
        "00c854d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea048.md#insn-008ea050)
- 新版 `008ea1ec`（命令位置の公開資料なし）

~~~diff
- 008ea050 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 008ea050 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ea050 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ea050 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ea1ec ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 008ea1ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea1ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea1ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ea050 bytes 29410391
+ 008ea1ec bytes 29411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6efb0b4e7b7580be42ddd1d11798ef0f"></a>

### [`008ea064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea064.md) → [`008ea200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea200.md) FUN_008ea200

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "008ea228",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ea08c",
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
      "008ea228",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008ea228",
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

- 旧版 [`008ea08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea064.md#insn-008ea08c) · [`008ea088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea064.md#insn-008ea088)
- 新版 `008ea228`（命令位置の公開資料なし） · `008ea224`（命令位置の公開資料なし）

~~~diff
- 008ea08c ["INT_ADD", "register:40f0:8", ["const:8ea08c:8", "const:4:8"]]
- 008ea08c ["CALL", null, ["ram:47acb4:8"]]
+ 008ea228 ["INT_ADD", "register:40f0:8", ["const:8ea228:8", "const:4:8"]]
+ 008ea228 ["CALL", null, ["ram:47acf4:8"]]
- 008ea08c bytes 0a43ee97
+ 008ea228 bytes b342ee97
- 008ea088 ["INT_ADD", "register:40f0:8", ["const:8ea088:8", "const:4:8"]]
- 008ea088 ["CALL", null, ["callee:008b9178:8"]]
+ 008ea224 ["INT_ADD", "register:40f0:8", ["const:8ea224:8", "const:4:8"]]
+ 008ea224 ["CALL", null, ["callee:008b9178:8"]]
- 008ea088 bytes 2b3cff97
+ 008ea224 bytes d53bff97
~~~


<a id="compare-0556c4f6481e335681ee3a77e8ea206e"></a>

### [`008ea0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea0d0.md) → [`008ea26c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea26c.md) FUN_008ea26c

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
      "definition_site": "008ea290",
      "incomplete_value": false,
      "site": "008ea290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea0f4",
      "incomplete_value": false,
      "site": "008ea0f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "008ea290",
      "DATA",
      [
        "storage",
        "00c85150",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea290",
      "DATA",
      [
        "storage",
        "00c85550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea0d0.md#insn-008ea0e4) · [`008ea0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea0d0.md#insn-008ea0f0)
- 新版 `008ea280`（命令位置の公開資料なし） · `008ea28c`（命令位置の公開資料なし）

~~~diff
- 008ea0e4 ["INT_ADD", "register:40f0:8", ["const:8ea0e4:8", "const:4:8"]]
- 008ea0e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 008ea280 ["INT_ADD", "register:40f0:8", ["const:8ea280:8", "const:4:8"]]
+ 008ea280 ["CALL", null, ["callee:00c57e90:8"]]
- 008ea0e4 bytes 6bb60d94
+ 008ea280 bytes 04b70d94
- 008ea0f0 ["COPY", "tmp:0:8", ["const:150:8"]]
- 008ea0f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ea0f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ea0f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea28c ["COPY", "tmp:0:8", ["const:550:8"]]
+ 008ea28c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea28c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea28c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ea0f0 bytes 08410591
+ 008ea28c bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e32e165cb95b4de55fd9d80b6d9eebcf"></a>

### [`008ea104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea104.md) → [`008ea2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea2a0.md) FUN_008ea2a0

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
      "definition_site": "008ea2ac",
      "incomplete_value": false,
      "site": "008ea2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea110",
      "incomplete_value": false,
      "site": "008ea110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008ea2ac",
      "DATA",
      [
        "storage",
        "00c85150",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea2ac",
      "DATA",
      [
        "storage",
        "00c85550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea104.md#insn-008ea10c)
- 新版 `008ea2a8`（命令位置の公開資料なし）

~~~diff
- 008ea10c ["COPY", "tmp:0:8", ["const:150:8"]]
- 008ea10c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ea10c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ea10c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ea2a8 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 008ea2a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea2a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea2a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ea10c bytes 29410591
+ 008ea2a8 bytes 29411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a89cc9d038f3ad620796bbe276357c63"></a>

### [`008ea5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea5f4.md) → [`008ea790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea790.md) FUN_008ea790

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
      "definition_site": "008ea7b4",
      "incomplete_value": false,
      "site": "008ea7b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea618",
      "incomplete_value": false,
      "site": "008ea618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "008ea7b4",
      "DATA",
      [
        "storage",
        "00c851e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea7b4",
      "DATA",
      [
        "storage",
        "00c855e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea5f4.md#insn-008ea608) · [`008ea614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea5f4.md#insn-008ea614)
- 新版 `008ea7a4`（命令位置の公開資料なし） · `008ea7b0`（命令位置の公開資料なし）

~~~diff
- 008ea608 ["INT_ADD", "register:40f0:8", ["const:8ea608:8", "const:4:8"]]
- 008ea608 ["CALL", null, ["callee:00c57e90:8"]]
+ 008ea7a4 ["INT_ADD", "register:40f0:8", ["const:8ea7a4:8", "const:4:8"]]
+ 008ea7a4 ["CALL", null, ["callee:00c57e90:8"]]
- 008ea608 bytes 22b50d94
+ 008ea7a4 bytes bbb50d94
- 008ea614 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 008ea614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ea614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ea614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea7b0 ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 008ea7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ea614 bytes 08810791
+ 008ea7b0 bytes 08811791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b044b9038490f0fb7d885a393d9ae529"></a>

### [`008ea628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea628.md) → [`008ea7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea7c4.md) FUN_008ea7c4

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
      "definition_site": "008ea7d0",
      "incomplete_value": false,
      "site": "008ea7d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea634",
      "incomplete_value": false,
      "site": "008ea634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "008ea7d0",
      "DATA",
      [
        "storage",
        "00c851e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea7d0",
      "DATA",
      [
        "storage",
        "00c855e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea628.md#insn-008ea630)
- 新版 `008ea7cc`（命令位置の公開資料なし）

~~~diff
- 008ea630 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 008ea630 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ea630 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ea630 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ea7cc ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 008ea7cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea7cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea7cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ea630 bytes 29810791
+ 008ea7cc bytes 29811791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b844750fa8f592cafe38faf176d9093"></a>

### [`008ea644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea644.md) → [`008ea7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea7e0.md) FUN_008ea7e0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "008ea804",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ea668",
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
      "008ea804",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008ea804",
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

- 旧版 [`008ea668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea644.md#insn-008ea668) · [`008ea664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea644.md#insn-008ea664)
- 新版 `008ea804`（命令位置の公開資料なし） · `008ea800`（命令位置の公開資料なし）

~~~diff
- 008ea668 ["INT_ADD", "register:40f0:8", ["const:8ea668:8", "const:4:8"]]
- 008ea668 ["CALL", null, ["ram:47acb4:8"]]
+ 008ea804 ["INT_ADD", "register:40f0:8", ["const:8ea804:8", "const:4:8"]]
+ 008ea804 ["CALL", null, ["ram:47acf4:8"]]
- 008ea668 bytes 9341ee97
+ 008ea804 bytes 3c41ee97
- 008ea664 ["INT_ADD", "register:40f0:8", ["const:8ea664:8", "const:4:8"]]
- 008ea664 ["CALL", null, ["callee:008b9178:8"]]
+ 008ea800 ["INT_ADD", "register:40f0:8", ["const:8ea800:8", "const:4:8"]]
+ 008ea800 ["CALL", null, ["callee:008b9178:8"]]
- 008ea664 bytes b43aff97
+ 008ea800 bytes 5e3aff97
~~~


<a id="compare-0c157acd23462db79c66420ac1d7be86"></a>

### [`008ea6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea6b8.md) → [`008ea854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea854.md) FUN_008ea854

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
      "definition_site": "008ea878",
      "incomplete_value": false,
      "site": "008ea878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea6dc",
      "incomplete_value": false,
      "site": "008ea6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008ea878",
      "DATA",
      [
        "storage",
        "00c85260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea878",
      "DATA",
      [
        "storage",
        "00c85660",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea6b8.md#insn-008ea6cc) · [`008ea6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea6b8.md#insn-008ea6d8)
- 新版 `008ea868`（命令位置の公開資料なし） · `008ea874`（命令位置の公開資料なし）

~~~diff
- 008ea6cc ["INT_ADD", "register:40f0:8", ["const:8ea6cc:8", "const:4:8"]]
- 008ea6cc ["CALL", null, ["callee:00c57e90:8"]]
+ 008ea868 ["INT_ADD", "register:40f0:8", ["const:8ea868:8", "const:4:8"]]
+ 008ea868 ["CALL", null, ["callee:00c57e90:8"]]
- 008ea6cc bytes f1b40d94
+ 008ea868 bytes 8ab50d94
- 008ea6d8 ["COPY", "tmp:0:8", ["const:260:8"]]
- 008ea6d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ea6d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ea6d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea874 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 008ea874 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea874 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea874 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ea6d8 bytes 08810991
+ 008ea874 bytes 08811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b95dca35fe54182ab059bb0e79d1ca6"></a>

### [`008ea6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea6ec.md) → [`008ea888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea888.md) FUN_008ea888

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
      "definition_site": "008ea894",
      "incomplete_value": false,
      "site": "008ea894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea6f8",
      "incomplete_value": false,
      "site": "008ea6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008ea894",
      "DATA",
      [
        "storage",
        "00c85260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea894",
      "DATA",
      [
        "storage",
        "00c85660",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea6ec.md#insn-008ea6f4)
- 新版 `008ea890`（命令位置の公開資料なし）

~~~diff
- 008ea6f4 ["COPY", "tmp:0:8", ["const:260:8"]]
- 008ea6f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ea6f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ea6f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ea890 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 008ea890 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea890 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea890 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ea6f4 bytes 29810991
+ 008ea890 bytes 29811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f489821991b8c0a2a79789aa687eaf57"></a>

### [`008ea708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea708.md) → [`008ea8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea8a4.md) FUN_008ea8a4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "008ea8c8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ea72c",
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
      "008ea8c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008ea8c8",
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

- 旧版 [`008ea72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea708.md#insn-008ea72c) · [`008ea728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea708.md#insn-008ea728)
- 新版 `008ea8c8`（命令位置の公開資料なし） · `008ea8c4`（命令位置の公開資料なし）

~~~diff
- 008ea72c ["INT_ADD", "register:40f0:8", ["const:8ea72c:8", "const:4:8"]]
- 008ea72c ["CALL", null, ["ram:47acb4:8"]]
+ 008ea8c8 ["INT_ADD", "register:40f0:8", ["const:8ea8c8:8", "const:4:8"]]
+ 008ea8c8 ["CALL", null, ["ram:47acf4:8"]]
- 008ea72c bytes 6241ee97
+ 008ea8c8 bytes 0b41ee97
- 008ea728 ["INT_ADD", "register:40f0:8", ["const:8ea728:8", "const:4:8"]]
- 008ea728 ["CALL", null, ["callee:008b9178:8"]]
+ 008ea8c4 ["INT_ADD", "register:40f0:8", ["const:8ea8c4:8", "const:4:8"]]
+ 008ea8c4 ["CALL", null, ["callee:008b9178:8"]]
- 008ea728 bytes 833aff97
+ 008ea8c4 bytes 2d3aff97
~~~


<a id="compare-06b1527935b486d55190e0304c7566d4"></a>

### [`008ea7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7ac.md) → [`008ea948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea948.md) FUN_008ea948

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
      "definition_site": "008ea96c",
      "incomplete_value": false,
      "site": "008ea96c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea7d0",
      "incomplete_value": false,
      "site": "008ea7d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
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
      "008ea96c",
      "DATA",
      [
        "storage",
        "00c852e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea96c",
      "DATA",
      [
        "storage",
        "00c856e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7ac.md#insn-008ea7c0) · [`008ea7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7ac.md#insn-008ea7cc)
- 新版 `008ea95c`（命令位置の公開資料なし） · `008ea968`（命令位置の公開資料なし）

~~~diff
- 008ea7c0 ["INT_ADD", "register:40f0:8", ["const:8ea7c0:8", "const:4:8"]]
- 008ea7c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 008ea95c ["INT_ADD", "register:40f0:8", ["const:8ea95c:8", "const:4:8"]]
+ 008ea95c ["CALL", null, ["callee:00c57e90:8"]]
- 008ea7c0 bytes b4b40d94
+ 008ea95c bytes 4db50d94
- 008ea7cc ["COPY", "tmp:0:8", ["const:2e0:8"]]
- 008ea7cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ea7cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ea7cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea968 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 008ea968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ea7cc bytes 08810b91
+ 008ea968 bytes 08811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd364d906f5cf78bcdb9b41525401cb7"></a>

### [`008ea7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7e0.md) → [`008ea97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea97c.md) FUN_008ea97c

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
      "definition_site": "008ea988",
      "incomplete_value": false,
      "site": "008ea988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea7ec",
      "incomplete_value": false,
      "site": "008ea7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
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
      "008ea988",
      "DATA",
      [
        "storage",
        "00c852e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea988",
      "DATA",
      [
        "storage",
        "00c856e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7e0.md#insn-008ea7e8)
- 新版 `008ea984`（命令位置の公開資料なし）

~~~diff
- 008ea7e8 ["COPY", "tmp:0:8", ["const:2e0:8"]]
- 008ea7e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ea7e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ea7e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ea984 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 008ea984 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea984 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea984 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ea7e8 bytes 29810b91
+ 008ea984 bytes 29811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f5d9818cc9f2b03fc54d6ffdc414107"></a>

### [`008ea7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7fc.md) → [`008ea998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea998.md) FUN_008ea998

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "site": "008ea9b4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ea818",
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
      "008ea9b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008ea9b4",
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

- 旧版 [`008ea818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7fc.md#insn-008ea818) · [`008ea814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7fc.md#insn-008ea814)
- 新版 `008ea9b4`（命令位置の公開資料なし） · `008ea9b0`（命令位置の公開資料なし）

~~~diff
- 008ea818 ["INT_ADD", "register:40f0:8", ["const:8ea818:8", "const:4:8"]]
- 008ea818 ["CALL", null, ["ram:47acb4:8"]]
+ 008ea9b4 ["INT_ADD", "register:40f0:8", ["const:8ea9b4:8", "const:4:8"]]
+ 008ea9b4 ["CALL", null, ["ram:47acf4:8"]]
- 008ea818 bytes 2741ee97
+ 008ea9b4 bytes d040ee97
- 008ea814 ["INT_ADD", "register:40f0:8", ["const:8ea814:8", "const:4:8"]]
- 008ea814 ["CALL", null, ["callee:008b9178:8"]]
+ 008ea9b0 ["INT_ADD", "register:40f0:8", ["const:8ea9b0:8", "const:4:8"]]
+ 008ea9b0 ["CALL", null, ["callee:008b9178:8"]]
- 008ea814 bytes 483aff97
+ 008ea9b0 bytes f239ff97
~~~


<a id="compare-5bda44b1cc6bc8a034d5a9bc480363d2"></a>

### [`008ea85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea85c.md) → [`008ea9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea9f8.md) FUN_008ea9f8

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
      "definition_site": "008eaa1c",
      "incomplete_value": false,
      "site": "008eaa1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea880",
      "incomplete_value": false,
      "site": "008ea880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:360:8"
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
      "008eaa1c",
      "DATA",
      [
        "storage",
        "00c85360",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eaa1c",
      "DATA",
      [
        "storage",
        "00c85760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea85c.md#insn-008ea870) · [`008ea87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea85c.md#insn-008ea87c)
- 新版 `008eaa0c`（命令位置の公開資料なし） · `008eaa18`（命令位置の公開資料なし）

~~~diff
- 008ea870 ["INT_ADD", "register:40f0:8", ["const:8ea870:8", "const:4:8"]]
- 008ea870 ["CALL", null, ["callee:00c57e90:8"]]
+ 008eaa0c ["INT_ADD", "register:40f0:8", ["const:8eaa0c:8", "const:4:8"]]
+ 008eaa0c ["CALL", null, ["callee:00c57e90:8"]]
- 008ea870 bytes 88b40d94
+ 008eaa0c bytes 21b50d94
- 008ea87c ["COPY", "tmp:0:8", ["const:360:8"]]
- 008ea87c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ea87c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ea87c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eaa18 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 008eaa18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eaa18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eaa18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ea87c bytes 08810d91
+ 008eaa18 bytes 08811d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec780be0eaa9ebfe16048c3f8b63983f"></a>

### [`008ea890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea890.md) → [`008eaa2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008eaa2c.md) FUN_008eaa2c

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
      "definition_site": "008eaa38",
      "incomplete_value": false,
      "site": "008eaa38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea89c",
      "incomplete_value": false,
      "site": "008ea89c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:360:8"
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
      "008eaa38",
      "DATA",
      [
        "storage",
        "00c85360",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eaa38",
      "DATA",
      [
        "storage",
        "00c85760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea890.md#insn-008ea898)
- 新版 `008eaa34`（命令位置の公開資料なし）

~~~diff
- 008ea898 ["COPY", "tmp:0:8", ["const:360:8"]]
- 008ea898 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ea898 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ea898 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008eaa34 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 008eaa34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008eaa34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008eaa34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ea898 bytes 29810d91
+ 008eaa34 bytes 29811d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8d0a784d07f9fe39fbc931fdca35373"></a>

### [`008ea8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea8ac.md) → [`008eaa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008eaa48.md) FUN_008eaa48

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 15件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 96.14% / 新版 96.14%

CFGの説明率　旧版 88.71% / 新版 85.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008eab30",
      "incomplete_value": true,
      "site": "008eab48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:638:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea994",
      "incomplete_value": true,
      "site": "008ea9ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5f8:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008eac20",
      "incomplete_value": false,
      "site": "008eac20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eaa84",
      "incomplete_value": false,
      "site": "008eaa84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008eaa8c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ea8f0",
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
      "008eaa8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008eab10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008eab30",
      "READ",
      [
        "storage",
        "002b95f8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008eaa8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008eab10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008eab30",
      "READ",
      [
        "storage",
        "002b9638",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea8ac.md#insn-008ea8f0) · [`008ea974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea8ac.md#insn-008ea974) · [`008ea9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea8ac.md#insn-008ea9c8)
- 新版 `008eaa8c`（命令位置の公開資料なし） · `008eab10`（命令位置の公開資料なし） · `008eab64`（命令位置の公開資料なし）

~~~diff
- 008ea8f0 ["INT_ADD", "register:40f0:8", ["const:8ea8f0:8", "const:4:8"]]
- 008ea8f0 ["CALL", null, ["ram:47acb4:8"]]
+ 008eaa8c ["INT_ADD", "register:40f0:8", ["const:8eaa8c:8", "const:4:8"]]
+ 008eaa8c ["CALL", null, ["ram:47acf4:8"]]
- 008ea8f0 bytes f140ee97
+ 008eaa8c bytes 9a40ee97
- 008ea974 ["INT_ADD", "register:40f0:8", ["const:8ea974:8", "const:4:8"]]
- 008ea974 ["CALL", null, ["ram:47acb4:8"]]
+ 008eab10 ["INT_ADD", "register:40f0:8", ["const:8eab10:8", "const:4:8"]]
+ 008eab10 ["CALL", null, ["ram:47acf4:8"]]
- 008ea974 bytes d040ee97
+ 008eab10 bytes 7940ee97
- 008ea9c8 ["INT_ADD", "register:40f0:8", ["const:8ea9c8:8", "const:4:8"]]
- 008ea9c8 ["CALL", null, ["ram:71ecc0:8"]]
+ 008eab64 ["INT_ADD", "register:40f0:8", ["const:8eab64:8", "const:4:8"]]
+ 008eab64 ["CALL", null, ["ram:71ed00:8"]]
- 008ea9c8 bytes bed0f897
+ 008eab64 bytes 67d0f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c562633110244f70c7dd3896576d6d3"></a>

### [`008ead30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead30.md) → [`008eaecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008eaecc.md) FUN_008eaecc

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
      "definition_site": "008eaef0",
      "incomplete_value": false,
      "site": "008eaef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ead54",
      "incomplete_value": false,
      "site": "008ead54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
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
      "008eaef0",
      "DATA",
      [
        "storage",
        "00c853d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eaef0",
      "DATA",
      [
        "storage",
        "00c857d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ead44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead30.md#insn-008ead44) · [`008ead50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead30.md#insn-008ead50)
- 新版 `008eaee0`（命令位置の公開資料なし） · `008eaeec`（命令位置の公開資料なし）

~~~diff
- 008ead44 ["INT_ADD", "register:40f0:8", ["const:8ead44:8", "const:4:8"]]
- 008ead44 ["CALL", null, ["callee:00c57e90:8"]]
+ 008eaee0 ["INT_ADD", "register:40f0:8", ["const:8eaee0:8", "const:4:8"]]
+ 008eaee0 ["CALL", null, ["callee:00c57e90:8"]]
- 008ead44 bytes 53b30d94
+ 008eaee0 bytes ecb30d94
- 008ead50 ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 008ead50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ead50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ead50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eaeec ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 008eaeec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eaeec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eaeec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ead50 bytes 08410f91
+ 008eaeec bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a702dc914cdcdf195f9909ddc38e871"></a>

### [`008ead64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead64.md) → [`008eaf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008eaf00.md) FUN_008eaf00

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
      "definition_site": "008eaf0c",
      "incomplete_value": false,
      "site": "008eaf0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ead70",
      "incomplete_value": false,
      "site": "008ead70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008eaf0c",
      "DATA",
      [
        "storage",
        "00c853d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eaf0c",
      "DATA",
      [
        "storage",
        "00c857d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ead6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead64.md#insn-008ead6c)
- 新版 `008eaf08`（命令位置の公開資料なし）

~~~diff
- 008ead6c ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 008ead6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ead6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ead6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008eaf08 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 008eaf08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008eaf08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008eaf08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ead6c bytes 29410f91
+ 008eaf08 bytes 29411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2550fa298775bcf23b1ab86c263dc84"></a>

### [`008ead80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead80.md) → [`008eaf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008eaf1c.md) FUN_008eaf1c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ead88"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008eaf24"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008ead9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ead88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008eaf4c"
      ]
    ],
    [
      "unmatched:008ead9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008eaf24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008eaf4c"
      ]
    ],
    [
      "008eaf38",
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

- 旧版 [`008ead88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead80.md#insn-008ead88) · [`008ead9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead80.md#insn-008ead9c)
- 新版 `008eaf24`（命令位置の公開資料なし）

~~~diff
- 008ead88 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008ead88 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008ead88 bytes 41010054
- 008ead9c ["INT_ADD", "register:40f0:8", ["const:8ead9c:8", "const:4:8"]]
- 008ead9c ["CALL", null, ["ram:47acb4:8"]]
- 008ead9c bytes c63fee97
+ 008eaf24 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008eaf24 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 008eaf24 bytes 41010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73f7ff3ad9aac8ff26684f84433bd227"></a>

### [`008eade0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eade0.md) → [`008eaf7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008eaf7c.md) FUN_008eaf7c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eade0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eade0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eade4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008eade0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008eade4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008eae04",
      "DATA",
      [
        "storage",
        "00c85460",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eaf7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008eaf80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008eafa0",
      "DATA",
      [
        "storage",
        "00c85860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eade0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eade0.md#insn-008eade0) · [`008eade4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eade0.md#insn-008eade4) · [`008eadf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eade0.md#insn-008eadf4)
- 新版 `008eaf90`（命令位置の公開資料なし）

~~~diff
- 008eade0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008eade0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008eade0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008eade0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008eade0 bytes fd7bbea9
- 008eade4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008eade4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008eade4 bytes f30b00f9
- 008eadf4 ["INT_ADD", "register:40f0:8", ["const:8eadf4:8", "const:4:8"]]
- 008eadf4 ["CALL", null, ["callee:00c57e90:8"]]
+ 008eaf90 ["INT_ADD", "register:40f0:8", ["const:8eaf90:8", "const:4:8"]]
+ 008eaf90 ["CALL", null, ["callee:00c57e90:8"]]
- 008eadf4 bytes 27b30d94
+ 008eaf90 bytes c0b30d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-913e69c27fd16b64bbf01f3afc668804"></a>

### [`008eae14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eae14.md) → [`008eafb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008eafb0.md) FUN_008eafb0

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
      "definition_site": "008eafbc",
      "incomplete_value": false,
      "site": "008eafbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eae20",
      "incomplete_value": false,
      "site": "008eae20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008eafbc",
      "DATA",
      [
        "storage",
        "00c85460",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eafbc",
      "DATA",
      [
        "storage",
        "00c85860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eae1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eae14.md#insn-008eae1c)
- 新版 `008eafb8`（命令位置の公開資料なし）

~~~diff
- 008eae1c ["COPY", "tmp:0:8", ["const:460:8"]]
- 008eae1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008eae1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008eae1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008eafb8 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 008eafb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008eafb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008eafb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008eae1c bytes 29811191
+ 008eafb8 bytes 29812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca283427f78e14ea58a60fdcbc9f05d3"></a>

### [`008eae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eae30.md) → [`008eafcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008eafcc.md) FUN_008eafcc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b924c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.77% / 新版 90.77%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008eae68"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008eb004"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008eb00c",
      "incomplete_value": false,
      "site": "008eb020",
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
      "definition_site": "008eae70",
      "incomplete_value": false,
      "site": "008eae84",
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
      "unmatched:008eae64",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008eae68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008eb03c"
      ]
    ],
    [
      "unmatched:008eae70",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008eb000",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008eb004",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008eb03c"
      ]
    ],
    [
      "008eb00c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eae68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eae30.md#insn-008eae68) · [`008eae84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eae30.md#insn-008eae84) · [`008eaebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eae30.md#insn-008eaebc)
- 新版 `008eb020`（命令位置の公開資料なし） · `008eb058`（命令位置の公開資料なし）

~~~diff
- 008eae68 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008eae68 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 008eae68 bytes c80100b4
- 008eae84 ["INT_ADD", "register:40f0:8", ["const:8eae84:8", "const:4:8"]]
- 008eae84 ["CALL", null, ["callee:00c58610:8"]]
+ 008eb020 ["INT_ADD", "register:40f0:8", ["const:8eb020:8", "const:4:8"]]
+ 008eb020 ["CALL", null, ["callee:00c58610:8"]]
- 008eae84 bytes e3b40d94
+ 008eb020 bytes 7cb50d94
- 008eaebc ["INT_ADD", "register:40f0:8", ["const:8eaebc:8", "const:4:8"]]
- 008eaebc ["CALL", null, ["callee:00468f88:8"]]
+ 008eb058 ["INT_ADD", "register:40f0:8", ["const:8eb058:8", "const:4:8"]]
+ 008eb058 ["CALL", null, ["callee:00468f88:8"]]
- 008eaebc bytes 23f8ed97
+ 008eb058 bytes ccf7ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46181c95ba0b5a83e7475ce2eaa4a6ec"></a>

### [`008eaf5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eaf5c.md) → [`008eb0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb0f8.md) _INIT_174

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 72.88% / 新版 72.88%

CFGの説明率　旧版 26.32% / 新版 24.39%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eaf8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eafa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eafa4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008eaf8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008eaf98",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008eafa0",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008eb128",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008eb134",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "008eb13c",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eaf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eaf5c.md#insn-008eaf8c) · [`008eafa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eaf5c.md#insn-008eafa0) · [`008eafa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eaf5c.md#insn-008eafa4)

~~~diff
- 008eaf8c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008eaf8c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008eaf8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008eaf8c bytes a9831ff8
- 008eafa0 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 008eafa0 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 008eafa0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 008eafa0 bytes ea130278
- 008eafa4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 008eafa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 008eafa4 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd89223557a7aa21d44f3b384ff084bd"></a>

### [`008eb2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb2ec.md) → [`008eb488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb488.md) FUN_008eb488

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006d8728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8728.md) · 呼出先 2件 [`008eb380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md) [`008eb7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb7ec.md)
- 新版 呼出元 1件 [`006d8768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d8768.md) · 呼出先 2件 [`008eb51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb51c.md) [`008eb988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb988.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 72.22% / 新版 81.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb348"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008eb50c",
      "incomplete_value": true,
      "site": "008eb50c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:614:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eb370",
      "incomplete_value": true,
      "site": "008eb370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:214:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008eb4e4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008eb4c4",
      "READ",
      [
        "storage",
        "00ca4210",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:008eb348",
      "WRITE",
      [
        "storage",
        "00ca4210",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:008eb34c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "008eb510"
      ]
    ]
  ],
  "added": [
    [
      "008eb4c4",
      "READ",
      [
        "storage",
        "00ca4610",
        null,
        "undefined4"
      ]
    ],
    [
      "008eb4e4",
      "WRITE",
      [
        "storage",
        "00ca4610",
        null,
        "undefined4"
      ]
    ],
    [
      "008eb4e8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "008eb510"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eb348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb2ec.md#insn-008eb348) · [`008eb370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb2ec.md#insn-008eb370)
- 新版 `008eb50c`（命令位置の公開資料なし） · `008eb4e4`（命令位置の公開資料なし）

~~~diff
- 008eb348 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:210:8"]]
- 008eb348 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008eb348 bytes 681202b9
- 008eb370 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:214:8"]]
- 008eb370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008eb50c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:614:8"]]
+ 008eb50c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008eb370 bytes 681602b9
+ 008eb50c bytes 681606b9
+ 008eb4e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:610:8"]]
+ 008eb4e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008eb4e4 bytes 681206b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c3267c33b06b742433a3be19c27719f"></a>

### [`008eb380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md) → [`008eb51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb51c.md) FUN_008eb51c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`008eb2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb2ec.md) [`008ec104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec104.md) [`008f5214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5214.md) [`008f694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f694c.md) · 呼出先 13件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) [`008f21dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f21dc.md)
- 新版 呼出元 5件 [`008eb488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb488.md) [`008ec2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ec/008ec2a0.md) [`008f53b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f53b0.md) [`008f6ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6ae8.md) [`008f7008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f7/008f7008.md) · 呼出先 13件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`006337e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/006337e4.md) [`008f2378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f2/008f2378.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 84.52% / 新版 79.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb5c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb5c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb5c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008eb5c8",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "008eb608",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "008eb744",
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
      "008eb5c8",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "008eb608",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "008eb744",
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

- 旧版 [`008eb474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md#insn-008eb474) · [`008eb598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md#insn-008eb598) · [`008eb5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md#insn-008eb5a4)
- 新版 `008eb610`（命令位置の公開資料なし） · `008eb734`（命令位置の公開資料なし） · `008eb740`（命令位置の公開資料なし）

~~~diff
- 008eb474 ["INT_ADD", "register:40f0:8", ["const:8eb474:8", "const:4:8"]]
- 008eb474 ["CALL", null, ["callee:008f9c14:8"]]
+ 008eb610 ["INT_ADD", "register:40f0:8", ["const:8eb610:8", "const:4:8"]]
+ 008eb610 ["CALL", null, ["callee:008f9c14:8"]]
- 008eb474 bytes 81390094
+ 008eb610 bytes 81390094
- 008eb598 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008eb598 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 008eb598 ["CBRANCH", null, ["local:b43:8", "tmp:1:1"]]
+ 008eb734 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 008eb734 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
+ 008eb734 ["CBRANCH", null, ["local:b44:8", "tmp:1:1"]]
- 008eb598 bytes 8d070054
+ 008eb734 bytes 8d070054
- 008eb5a4 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 008eb5a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008eb5a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008eb5a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eb740 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 008eb740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008eb5a4 bytes 08e12c91
+ 008eb740 bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7960aa8489f226064ba2642e1e7b17e"></a>

### [`008eb9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb9dc.md) → [`008ebb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008ebb78.md) FUN_008ebb78

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f65c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f65c8.md) · 呼出先 14件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)
- 新版 呼出元 1件 [`008f6764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6764.md) · 呼出先 14件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 87.13% / 新版 87.13%

CFGの説明率　旧版 68.09% / 新版 68.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eba38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eba60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eba64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008eba38",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008eba38",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "unmatched:008eba54",
      "READ",
      [
        "storage",
        "002a4962",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008ebbd4",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "008ebbd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "008ebbf0",
      "READ",
      [
        "storage",
        "002a4a2f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb9dc.md#insn-008eba38) · [`008eba60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb9dc.md#insn-008eba60) · [`008eba64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb9dc.md#insn-008eba64)

~~~diff
- 008eba38 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 008eba38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008eba38 bytes e91700f9
- 008eba60 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 008eba60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 008eba60 bytes e01300f9
- 008eba64 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 008eba64 ["COPY", "tmp:1:4", ["register:4048:4"]]
- 008eba64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 008eba64 bytes 09400079
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e15c398c9a02257e47c1b2445fd05819"></a>

### [`008ebcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008ebcd8.md) → [`008ebe74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008ebe74.md) FUN_008ebe74

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f65c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f65c8.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008005ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008005ec.md) [`00804034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00804/00804034.md) [`008f8850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8850.md)
- 新版 呼出元 1件 [`008f6764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6764.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`0080062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/0080062c.md) [`00804074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00804/00804074.md) [`008f89ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f8/008f89ec.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 80.00% / 新版 86.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ebd08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008ebea4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ebee8",
      "value": [
        "leaf",
        "ram:804074:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ebd4c",
      "value": [
        "leaf",
        "ram:804034:8"
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
      "unmatched:008ebd08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ebf88"
      ]
    ],
    [
      "008ebee8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00804034"
      ]
    ]
  ],
  "added": [
    [
      "008ebea4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ebf88"
      ]
    ],
    [
      "008ebee8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00804074"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ebd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008ebcd8.md#insn-008ebd08) · [`008ebd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008ebcd8.md#insn-008ebd4c)
- 新版 `008ebee8`（命令位置の公開資料なし） · `008ebea4`（命令位置の公開資料なし）

~~~diff
- 008ebd08 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 008ebd08 bytes 20070054
- 008ebd4c ["INT_ADD", "register:40f0:8", ["const:8ebd4c:8", "const:4:8"]]
- 008ebd4c ["CALL", null, ["ram:804034:8"]]
+ 008ebee8 ["INT_ADD", "register:40f0:8", ["const:8ebee8:8", "const:4:8"]]
+ 008ebee8 ["CALL", null, ["ram:804074:8"]]
- 008ebd4c bytes ba60fc97
+ 008ebee8 bytes 6360fc97
+ 008ebea4 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
+ 008ebea4 bytes 20070054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55dda33eb940ad103ee5df7f38be92ee"></a>

### [`008ebe14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008ebe14.md) → [`008ebfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008ebfb0.md) FUN_008ebfb0

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008ef858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef858.md) · 呼出先 8件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md) [`005cd0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd0b0.md) [`00664860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664860.md)
- 新版 呼出元 1件 [`008ef9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ef/008ef9f4.md) · 呼出先 8件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md) [`005cd0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd0f0.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md)

変更の種類 call, call_count, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ebe3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ebe5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ebe60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ebe3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ebe40",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "unmatched:008ebe50",
      "READ",
      [
        "storage",
        "002a5b7b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008ebfd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008ebfdc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "008ebfec",
      "READ",
      [
        "storage",
        "002a5c57",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ebe3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008ebe14.md#insn-008ebe3c) · [`008ebe40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008ebe14.md#insn-008ebe40) · [`008ebe5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008ebe14.md#insn-008ebe5c)

~~~diff
- 008ebe3c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008ebe3c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008ebe3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008ebe3c bytes a8831ff8
- 008ebe40 ["INT_ADD", "register:40f0:8", ["const:8ebe40:8", "const:4:8"]]
- 008ebe40 ["CALL", null, ["callee:00c57e90:8"]]
- 008ebe40 bytes 14af0d94
- 008ebe5c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 008ebe5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 008ebe5c bytes e02b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbe57b26c67daebe0b0175909c7f57db"></a>

### [`008ec104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec104.md) → [`008ec2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ec/008ec2a0.md) FUN_008ec2a0

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008ef858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef858.md) · 呼出先 18件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md)
- 新版 呼出元 1件 [`008ef9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ef/008ef9f4.md) · 呼出先 18件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_destination` 7件, `store_value` 4件

アドレスに依存する影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008ec38c",
      "incomplete_value": true,
      "site": "008ec38c",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:c3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ec1f0",
      "incomplete_value": true,
      "site": "008ec1f0",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:bfd:8"
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
      "definition_site": "008ec524",
      "incomplete_value": true,
      "site": "008ec524",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:c4a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ec388",
      "incomplete_value": true,
      "site": "008ec388",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:c0a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008ec840",
      "incomplete_value": false,
      "site": "008ec840",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ec6a4",
      "incomplete_value": false,
      "site": "008ec6a4",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008ec364",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "008ec378",
      "READ",
      [
        "storage",
        "002abbfd",
        null,
        "string"
      ]
    ],
    [
      "008ec400",
      "READ",
      [
        "storage",
        "00c9a8a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008ec364",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "008ec378",
      "READ",
      [
        "storage",
        "002abc3d",
        null,
        "string"
      ]
    ],
    [
      "008ec400",
      "READ",
      [
        "storage",
        "00c9aca0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ec284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec104.md#insn-008ec284) · [`008ec3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec104.md#insn-008ec3c4) · [`008ec508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec104.md#insn-008ec508)
- 新版 `008ec420`（命令位置の公開資料なし） · `008ec560`（命令位置の公開資料なし） · `008ec6a4`（命令位置の公開資料なし）

~~~diff
- 008ec284 ["INT_ADD", "register:40f0:8", ["const:8ec284:8", "const:4:8"]]
- 008ec284 ["CALL", null, ["callee:0047e8dc:8"]]
+ 008ec420 ["INT_ADD", "register:40f0:8", ["const:8ec420:8", "const:4:8"]]
+ 008ec420 ["CALL", null, ["callee:0047e8dc:8"]]
- 008ec284 bytes 8649ee97
+ 008ec420 bytes 2f49ee97
- 008ec3c4 ["INT_ADD", "register:40f0:8", ["const:8ec3c4:8", "const:4:8"]]
- 008ec3c4 ["CALL", null, ["callee:0047e8dc:8"]]
+ 008ec560 ["INT_ADD", "register:40f0:8", ["const:8ec560:8", "const:4:8"]]
+ 008ec560 ["CALL", null, ["callee:0047e8dc:8"]]
- 008ec3c4 bytes 3649ee97
+ 008ec560 bytes df48ee97
- 008ec508 ["INT_ADD", "register:40f0:8", ["const:8ec508:8", "const:4:8"]]
- 008ec508 ["CALL", null, ["callee:008514f8:8"]]
+ 008ec6a4 ["INT_ADD", "register:40f0:8", ["const:8ec6a4:8", "const:4:8"]]
+ 008ec6a4 ["CALL", null, ["callee:008514f8:8"]]
- 008ec508 bytes ec93fd97
+ 008ec6a4 bytes 9593fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaee4ad7a27ee58e3d177becf4a594ec"></a>

### [`008ec8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec8a0.md) → [`008eca3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ec/008eca3c.md) FUN_008eca3c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f7cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f7/008f7cdc.md) · 呼出先 7件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`008f7e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f7/008f7e78.md) · 呼出先 7件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.94% / 新版 90.94%

CFGの説明率　旧版 75.00% / 新版 67.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 10件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008eca58",
      "incomplete_value": true,
      "site": "008eca58",
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
      "definition_site": "008ec8bc",
      "incomplete_value": true,
      "site": "008ec8bc",
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
      "definition_site": "008eca60",
      "incomplete_value": false,
      "site": "008eca74",
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
      "definition_site": "008ec8c4",
      "incomplete_value": false,
      "site": "008ec8d8",
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
      "definition_site": "008eca68",
      "incomplete_value": false,
      "site": "008eca74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ec8cc",
      "incomplete_value": false,
      "site": "008ec8d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "008eca54",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008eca60",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008eca68",
      "PARAM",
      [
        "storage",
        "00c854d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008eca54",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008eca60",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008eca68",
      "PARAM",
      [
        "storage",
        "00c858d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ec8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec8a0.md#insn-008ec8d8) · [`008ec8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec8a0.md#insn-008ec8f8) · [`008ec92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec8a0.md#insn-008ec92c)
- 新版 `008eca74`（命令位置の公開資料なし） · `008eca94`（命令位置の公開資料なし） · `008ecac8`（命令位置の公開資料なし）

~~~diff
- 008ec8d8 ["INT_ADD", "register:40f0:8", ["const:8ec8d8:8", "const:4:8"]]
- 008ec8d8 ["CALL", null, ["callee:00c58610:8"]]
+ 008eca74 ["INT_ADD", "register:40f0:8", ["const:8eca74:8", "const:4:8"]]
+ 008eca74 ["CALL", null, ["callee:00c58610:8"]]
- 008ec8d8 bytes 4eae0d94
+ 008eca74 bytes e7ae0d94
- 008ec8f8 ["INT_ADD", "register:40f0:8", ["const:8ec8f8:8", "const:4:8"]]
- 008ec8f8 ["CALL", null, ["ram:46c984:8"]]
+ 008eca94 ["INT_ADD", "register:40f0:8", ["const:8eca94:8", "const:4:8"]]
+ 008eca94 ["CALL", null, ["ram:46c9c4:8"]]
- 008ec8f8 bytes 2300ee97
+ 008eca94 bytes ccffed97
- 008ec92c ["INT_ADD", "register:40f0:8", ["const:8ec92c:8", "const:4:8"]]
- 008ec92c ["CALL", null, ["ram:46c984:8"]]
+ 008ecac8 ["INT_ADD", "register:40f0:8", ["const:8ecac8:8", "const:4:8"]]
+ 008ecac8 ["CALL", null, ["ram:46c9c4:8"]]
- 008ec92c bytes 1600ee97
+ 008ecac8 bytes bfffed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-628abf0923eaa1f6b751c4e1043736ed"></a>

### [`008eccc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008eccc4.md) → [`008ece60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ec/008ece60.md) FUN_008ece60

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f694c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`008f6ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6ae8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 89.72% / 新版 89.72%

CFGの説明率　旧版 75.00% / 新版 77.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ece78"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ece9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008eceac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ece78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ed030"
      ]
    ],
    [
      "unmatched:008ece9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ed064"
      ]
    ],
    [
      "unmatched:008ecea8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c53d00"
      ]
    ]
  ],
  "added": [
    [
      "008ed014",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ed030"
      ]
    ],
    [
      "008ed038",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ed064"
      ]
    ],
    [
      "008ed044",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c53d00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ecd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008eccc4.md#insn-008ecd0c) · [`008ecdb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008eccc4.md#insn-008ecdb4) · [`008ecdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008eccc4.md#insn-008ecdbc)
- 新版 `008ecea8`（命令位置の公開資料なし） · `008ecf58`（命令位置の公開資料なし）

~~~diff
- 008ecd0c ["INT_ADD", "register:40f0:8", ["const:8ecd0c:8", "const:4:8"]]
- 008ecd0c ["CALL", null, ["callee:00c57e80:8"]]
+ 008ecea8 ["INT_ADD", "register:40f0:8", ["const:8ecea8:8", "const:4:8"]]
+ 008ecea8 ["CALL", null, ["callee:00c57e80:8"]]
- 008ecd0c bytes 5dab0d94
+ 008ecea8 bytes f6ab0d94
- 008ecdb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008ecdb4 ["INT_ADD", "register:40f0:8", ["const:8ecdb4:8", "const:4:8"]]
- 008ecdb4 ["CALLIND", null, ["register:0:8"]]
- 008ecdb4 bytes 00013fd6
- 008ecdbc ["INT_ADD", "register:40f0:8", ["const:8ecdbc:8", "const:4:8"]]
- 008ecdbc ["CALL", null, ["callee:00c57e80:8"]]
+ 008ecf58 ["INT_ADD", "register:40f0:8", ["const:8ecf58:8", "const:4:8"]]
+ 008ecf58 ["CALL", null, ["callee:00c57e80:8"]]
- 008ecdbc bytes 31ab0d94
+ 008ecf58 bytes caab0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2373330a06837f6a4de9f5159105652"></a>

### [`008ed01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ed/008ed01c.md) → [`008ed1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ed/008ed1b8.md) FUN_008ed1b8

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`008ef858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef858.md) [`008f2ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f2ea8.md) [`008f64f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f64f8.md) · 呼出先 53件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e730.md) [`0046e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e740.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md)
- 新版 呼出元 3件 [`008ef9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ef/008ef9f4.md) [`008f3044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f3/008f3044.md) [`008f6694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6694.md) · 呼出先 53件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046e770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e770.md) [`0046e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e780.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.26% / 新版 77.26%

CFGの説明率　旧版 49.39% / 新版 48.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `call_target` 6件, `store_value` 4件, `unresolved_branch_alignment` 48件, `unresolved_call_alignment` 62件, `unresolved_store_alignment` 86件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ed01c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ed01c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ed020"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ed01c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ed020",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ed024",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008ed1b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008ed1bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008ed1c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ed01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ed/008ed01c.md#insn-008ed01c) · [`008ed020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ed/008ed01c.md#insn-008ed020) · [`008ed024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ed/008ed01c.md#insn-008ed024)

~~~diff
- 008ed01c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008ed01c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008ed01c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 008ed01c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008ed01c bytes fd7bbaa9
- 008ed020 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008ed020 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008ed020 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008ed020 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ed020 bytes fc6f01a9
- 008ed024 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008ed024 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008ed024 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008ed024 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ed024 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6630e7b243a3a16a958733e51d2ee3f"></a>

### [`008ef76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef76c.md) → [`008ef908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ef/008ef908.md) FUN_008ef908

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008f64f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f64f8.md) · 呼出先 5件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`006c0eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0eec.md) [`006c1ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c1/006c1ef0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)
- 新版 呼出元 1件 [`008f6694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6694.md) · 呼出先 5件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`006c0f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0f2c.md) [`006c1f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c1/006c1f30.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008ef928",
      "incomplete_value": true,
      "site": "008ef928",
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
      "definition_site": "008ef78c",
      "incomplete_value": true,
      "site": "008ef78c",
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
      "definition_site": "008ef930",
      "incomplete_value": false,
      "site": "008ef944",
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
      "definition_site": "008ef794",
      "incomplete_value": false,
      "site": "008ef7a8",
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
      "definition_site": "008ef938",
      "incomplete_value": false,
      "site": "008ef944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ef79c",
      "incomplete_value": false,
      "site": "008ef7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "008ef924",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008ef930",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008ef938",
      "PARAM",
      [
        "storage",
        "00c854d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008ef924",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008ef930",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008ef938",
      "PARAM",
      [
        "storage",
        "00c858d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ef7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef76c.md#insn-008ef7a8) · [`008ef7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef76c.md#insn-008ef7d0) · [`008ef7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef76c.md#insn-008ef7d8)
- 新版 `008ef944`（命令位置の公開資料なし） · `008ef96c`（命令位置の公開資料なし）

~~~diff
- 008ef7a8 ["INT_ADD", "register:40f0:8", ["const:8ef7a8:8", "const:4:8"]]
- 008ef7a8 ["CALL", null, ["callee:00c58610:8"]]
+ 008ef944 ["INT_ADD", "register:40f0:8", ["const:8ef944:8", "const:4:8"]]
+ 008ef944 ["CALL", null, ["callee:00c58610:8"]]
- 008ef7a8 bytes 9aa20d94
+ 008ef944 bytes 33a30d94
- 008ef7d0 ["INT_ADD", "register:40f0:8", ["const:8ef7d0:8", "const:4:8"]]
- 008ef7d0 ["CALL", null, ["ram:46c984:8"]]
+ 008ef96c ["INT_ADD", "register:40f0:8", ["const:8ef96c:8", "const:4:8"]]
+ 008ef96c ["CALL", null, ["ram:46c9c4:8"]]
- 008ef7d0 bytes 6df4ed97
+ 008ef96c bytes 16f4ed97
- 008ef7d8 ["INT_ADD", "register:40f0:8", ["const:8ef7d8:8", "const:4:8"]]
- 008ef7d8 ["CALL", null, ["callee:008514f8:8"]]
- 008ef7d8 bytes 3887fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fa1c59d3631177adb7081ade4fa1342"></a>

### [`008ef858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef858.md) → [`008ef9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ef/008ef9f4.md) FUN_008ef9f4

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f65a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f65a4.md) · 呼出先 41件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ed4c.md) [`0046edc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046edc4.md)
- 新版 呼出元 1件 [`008f6740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6740.md) · 呼出先 41件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ed8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ed8c.md) [`0046ee04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee04.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.81% / 新版 86.81%

CFGの説明率　旧版 42.94% / 新版 43.20%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `call_target` 5件, `store_condition` 2件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 15件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008efcf4",
      "incomplete_value": true,
      "site": "008efcf8",
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008efb58",
      "incomplete_value": true,
      "site": "008efb5c",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008efbd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008efc14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ef8ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008efc28"
      ]
    ],
    [
      "unmatched:008ef9bc",
      "READ",
      [
        "storage",
        "00c9b128",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:008ef9c8",
      "DATA",
      [
        "storage",
        "00ca3bac",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008efa88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008efc28"
      ]
    ],
    [
      "008efb58",
      "READ",
      [
        "storage",
        "00c9b528",
        null,
        "pointer"
      ]
    ],
    [
      "008efb64",
      "DATA",
      [
        "storage",
        "00ca3fac",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ef8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef858.md#insn-008ef8ec) · [`008efaa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef858.md#insn-008efaa8)
- 新版 `008efb5c`（命令位置の公開資料なし）

~~~diff
- 008ef8ec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008ef8ec ["CBRANCH", null, ["local:b30:8", "tmp:0:1"]]
- 008ef8ec bytes 010d0054
- 008efaa8 ["CBRANCH", null, ["local:b46:8", "register:101:1"]]
- 008efaa8 bytes e0050054
+ 008efb5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:54:8"]]
+ 008efb5c ["LOAD", "register:5020:8", ["const:1b1:8", "tmp:0:8"]]
+ 008efb5c ["COPY", "register:5028:8", ["const:0:8"]]
+ 008efb5c ["COPY", "register:5030:8", ["const:0:8"]]
+ 008efb5c bytes 614245fc
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-479fbe7ae96ea56dfa5f3e333ef654c5"></a>

### [`008f0838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f0/008f0838.md) → [`008f09d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f0/008f09d4.md) FUN_008f09d4

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f7cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f7/008f7cdc.md) · 呼出先 41件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md)
- 新版 呼出元 1件 [`008f7e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f7/008f7e78.md) · 呼出先 41件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.38% / 新版 77.38%

CFGの説明率　旧版 21.36% / 新版 21.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 63件, `call_target` 5件, `store_condition` 4件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 62件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f0cf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f0cfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f0d00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008f0a14",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008f0a20",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f0a28",
      "PARAM",
      [
        "storage",
        "00c854d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f0a14",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008f0a20",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f0a28",
      "PARAM",
      [
        "storage",
        "00c858d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f0b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f0/008f0838.md#insn-008f0b68) · [`008f0cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f0/008f0838.md#insn-008f0cf4)
- 新版 `008f0d04`（命令位置の公開資料なし） · `008f0cf4`（命令位置の公開資料なし）

~~~diff
- 008f0b68 ["INT_ADD", "register:40f0:8", ["const:8f0b68:8", "const:4:8"]]
- 008f0b68 ["CALL", null, ["callee:008514f8:8"]]
+ 008f0d04 ["INT_ADD", "register:40f0:8", ["const:8f0d04:8", "const:4:8"]]
+ 008f0d04 ["CALL", null, ["callee:008514f8:8"]]
- 008f0b68 bytes 5482fd97
+ 008f0d04 bytes fd81fd97
- 008f0cf4 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008f0cf4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:48:8"]]
- 008f0cf4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008f0cf4 bytes e8230139
+ 008f0cf4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008f0cf4 ["COPY", "tmp:1:8", ["tmp:0:8"]]
+ 008f0cf4 ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:0:8"]]
+ 008f0cf4 ["INT_ADD", "tmp:2:8", ["register:4000:8", "tmp:1:8"]]
+ 008f0cf4 bytes 086868b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f6269fbb18bfbfba199734f625645fc"></a>

### [`008f21dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f21dc.md) → [`008f2378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f2/008f2378.md) FUN_008f2378

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008eb380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md) · 呼出先 12件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) [`006662e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/006662e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008f8928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8928.md)
- 新版 呼出元 1件 [`008eb51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb51c.md) · 呼出先 12件 [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00633374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md) [`00666320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00666/00666320.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008f8ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f8/008f8ac4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.57% / 新版 62.57%

CFGの説明率　旧版 5.26% / 新版 4.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f21f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f2314"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f2318"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008f21f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f2260",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f2418"
      ]
    ],
    [
      "unmatched:008f2290",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f2448"
      ]
    ]
  ],
  "added": [
    [
      "008f2394",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008f23fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f2418"
      ]
    ],
    [
      "008f242c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f2448"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f21f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f21dc.md#insn-008f21f8) · [`008f2260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f21dc.md#insn-008f2260) · [`008f2290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f21dc.md#insn-008f2290)

~~~diff
- 008f21f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008f21f8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008f21f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008f21f8 bytes a8831ff8
- 008f2260 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008f2260 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 008f2260 bytes e00000b5
- 008f2290 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008f2290 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 008f2290 bytes e00000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d492c4492a57dd4993bdf15660809f6"></a>

### [`008f24f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f24f8.md) → [`008f2694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f2/008f2694.md) FUN_008f2694

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f5214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5214.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00664780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664780.md) [`006647f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006647f0.md) [`00665c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665c3c.md) [`00665c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665c78.md)
- 新版 呼出元 1件 [`008f53b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f53b0.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`006647c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006647c0.md) [`00664830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664830.md) [`00665c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665c7c.md) [`00665cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665cb8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 59.69% / 新版 59.69%

CFGの説明率　旧版 15.82% / 新版 16.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_condition` 2件, `unresolved_branch_alignment` 28件, `unresolved_call_alignment` 14件, `unresolved_store_alignment` 41件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f24fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f24fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f2500"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008f24fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f2500",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f2504",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008f2698",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008f269c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008f26a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f24fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f24f8.md#insn-008f24fc) · [`008f2500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f24f8.md#insn-008f2500) · [`008f2504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f24f8.md#insn-008f2504)

~~~diff
- 008f24fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008f24fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008f24fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 008f24fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008f24fc bytes fd7b0ca9
- 008f2500 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008f2500 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008f2500 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 008f2500 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008f2500 bytes fc6f0da9
- 008f2504 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008f2504 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008f2504 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 008f2504 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008f2504 bytes fa670ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-371b70c7539ad4fad59ee9eaef0d5095"></a>

### [`008f2ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f2ea8.md) → [`008f3044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f3/008f3044.md) FUN_008f3044

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f5a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5a48.md) · 呼出先 11件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`006f1580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f1/006f1580.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0085b294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b294.md)
- 新版 呼出元 1件 [`008f5be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f5be4.md) · 呼出先 11件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006f15c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f1/006f15c0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085b2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2d4.md)

変更の種類 branch_condition_or_target, call, call_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.07% / 新版 94.07%

CFGの説明率　旧版 80.00% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f2ea8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f2ea8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f2eac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008f2ea8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f2eac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f2eb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008f3044",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008f3048",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008f304c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f2ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f2ea8.md#insn-008f2ea8) · [`008f2eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f2ea8.md#insn-008f2eac) · [`008f2eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f2ea8.md#insn-008f2eb0)

~~~diff
- 008f2ea8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008f2ea8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008f2ea8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 008f2ea8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008f2ea8 bytes fd7bbca9
- 008f2eac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008f2eac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 008f2eac bytes f70b00f9
- 008f2eb0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 008f2eb0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 008f2eb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008f2eb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008f2eb0 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86edeeae18aa9eba3347f699c796234c"></a>

### [`008f30c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f3/008f30c4.md) → [`008f3260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f3/008f3260.md) FUN_008f3260

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f6148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f6148.md) · 呼出先 16件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md)
- 新版 呼出元 1件 [`008f62e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f62e4.md) · 呼出先 16件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.97% / 新版 72.97%

CFGの説明率　旧版 31.25% / 新版 30.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f33b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f33b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f33c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008f30f0",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008f30f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f32bc"
      ]
    ],
    [
      "008f329c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f328c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008f3294",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f32bc"
      ]
    ],
    [
      "008f329c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f30f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f3/008f30c4.md#insn-008f30f8) · [`008f3150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f3/008f30c4.md#insn-008f3150) · [`008f3228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f3/008f30c4.md#insn-008f3228)
- 新版 `008f33c4`（命令位置の公開資料なし）

~~~diff
- 008f30f8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008f30f8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 008f30f8 bytes 480100b4
- 008f3150 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008f3150 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 008f3150 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 008f3150 ["CBRANCH", null, ["local:b14:8", "tmp:2:1"]]
- 008f3150 bytes ac080054
- 008f3228 ["INT_ADD", "register:40f0:8", ["const:8f3228:8", "const:4:8"]]
- 008f3228 ["CALL", null, ["callee:00489f4c:8"]]
+ 008f33c4 ["INT_ADD", "register:40f0:8", ["const:8f33c4:8", "const:4:8"]]
+ 008f33c4 ["CALL", null, ["callee:00489f4c:8"]]
- 008f3228 bytes 395bee97
+ 008f33c4 bytes e25aee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdc2fd50ea961bf63df6b62c863b25e0"></a>

### [`008f5214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5214.md) → [`008f53b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f53b0.md) FUN_008f53b0

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008f64f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f64f8.md) · 呼出先 27件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00664780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664780.md)
- 新版 呼出元 1件 [`008f6694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6694.md) · 呼出先 27件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`006647c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006647c0.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 98.12% / 新版 98.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 5件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008f59c0",
      "incomplete_value": false,
      "site": "008f59c0",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5824",
      "incomplete_value": false,
      "site": "008f5824",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "ordinal": 109,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008f59e0",
      "incomplete_value": false,
      "site": "008f59e0",
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
            "const:614:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5844",
      "incomplete_value": false,
      "site": "008f5844",
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
            "const:214:8"
          ]
        ]
      ]
    },
    "ordinal": 110,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008f53ec",
      "incomplete_value": true,
      "site": "008f53ec",
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
      "definition_site": "008f5250",
      "incomplete_value": true,
      "site": "008f5250",
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
      "008f53e8",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008f53f4",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f53fc",
      "PARAM",
      [
        "storage",
        "00c854d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f53e8",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008f53f4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f53fc",
      "PARAM",
      [
        "storage",
        "00c858d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f526c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5214.md#insn-008f526c) · [`008f53ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5214.md#insn-008f53ec) · [`008f540c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5214.md#insn-008f540c)
- 新版 `008f5408`（命令位置の公開資料なし） · `008f5588`（命令位置の公開資料なし） · `008f55a8`（命令位置の公開資料なし）

~~~diff
- 008f526c ["INT_ADD", "register:40f0:8", ["const:8f526c:8", "const:4:8"]]
- 008f526c ["CALL", null, ["callee:00c58610:8"]]
+ 008f5408 ["INT_ADD", "register:40f0:8", ["const:8f5408:8", "const:4:8"]]
+ 008f5408 ["CALL", null, ["callee:00c58610:8"]]
- 008f526c bytes e98b0d94
+ 008f5408 bytes 828c0d94
- 008f53ec ["INT_ADD", "register:40f0:8", ["const:8f53ec:8", "const:4:8"]]
- 008f53ec ["CALL", null, ["callee:00676a60:8"]]
+ 008f5588 ["INT_ADD", "register:40f0:8", ["const:8f5588:8", "const:4:8"]]
+ 008f5588 ["CALL", null, ["callee:00676a60:8"]]
- 008f53ec bytes 8d05f697
+ 008f5588 bytes 3605f697
- 008f540c ["INT_ADD", "register:40f0:8", ["const:8f540c:8", "const:4:8"]]
- 008f540c ["CALL", null, ["callee:00676a60:8"]]
+ 008f55a8 ["INT_ADD", "register:40f0:8", ["const:8f55a8:8", "const:4:8"]]
+ 008f55a8 ["CALL", null, ["callee:00676a60:8"]]
- 008f540c bytes 8505f697
+ 008f55a8 bytes 2e05f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99ef883e5a34ce825e967957ddae05db"></a>

### [`008f5a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5a48.md) → [`008f5be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f5be4.md) FUN_008f5be4

採用 · 移動量 `+0x19c` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f65a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f65a4.md) · 呼出先 17件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`006c0ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0ef8.md) [`006c1fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c1/006c1fd8.md)
- 新版 呼出元 1件 [`008f6740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6740.md) · 呼出先 17件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`006c0f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0f38.md) [`006c2018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c2/006c2018.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 95.98% / 新版 95.98%

CFGの説明率　旧版 98.43% / 新版 97.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 4件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008f6114",
      "incomplete_value": true,
      "site": "008f6128",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5f78",
      "incomplete_value": true,
      "site": "008f5f8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:260:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008f6120",
      "incomplete_value": true,
      "site": "008f6130",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:154:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5f84",
      "incomplete_value": true,
      "site": "008f5f94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:114:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008f6120",
      "incomplete_value": true,
      "site": "008f6130",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008f5f84",
      "incomplete_value": true,
      "site": "008f5f94",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 60,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008f5c54",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "008f5cb8",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "008f5d64",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008f5c54",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "008f5cb8",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "008f5d64",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5a48.md#insn-008f5be0) · [`008f6034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5a48.md#insn-008f6034) · [`008f603c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5a48.md#insn-008f603c)
- 新版 `008f5d7c`（命令位置の公開資料なし） · `008f61d0`（命令位置の公開資料なし）

~~~diff
- 008f5be0 ["INT_ADD", "register:40f0:8", ["const:8f5be0:8", "const:4:8"]]
- 008f5be0 ["CALL", null, ["callee:008f9c14:8"]]
+ 008f5d7c ["INT_ADD", "register:40f0:8", ["const:8f5d7c:8", "const:4:8"]]
+ 008f5d7c ["CALL", null, ["callee:008f9c14:8"]]
- 008f5be0 bytes a60f0094
+ 008f5d7c bytes a60f0094
- 008f6034 ["INT_ADD", "register:40f0:8", ["const:8f6034:8", "const:4:8"]]
- 008f6034 ["CALL", null, ["ram:6c0ef8:8"]]
+ 008f61d0 ["INT_ADD", "register:40f0:8", ["const:8f61d0:8", "const:4:8"]]
+ 008f61d0 ["CALL", null, ["ram:6c0f38:8"]]
- 008f6034 bytes b12bf797
+ 008f61d0 bytes 5a2bf797
- 008f603c ["INT_ADD", "register:40f0:8", ["const:8f603c:8", "const:4:8"]]
- 008f603c ["CALL", null, ["callee:008514f8:8"]]
- 008f603c bytes 1f6dfd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c32960781f5a118dd3271a1800c9182"></a>

### [`008f6148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f6148.md) → [`008f62e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f62e4.md) FUN_008f62e4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f7cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f7/008f7cdc.md) · 呼出先 14件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 1件 [`008f7e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f7/008f7e78.md) · 呼出先 14件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.69% / 新版 76.69%

CFGの説明率　旧版 30.19% / 新版 29.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f6174"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f62b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f6348"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008f6174",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "008f6318",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008f6188",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f6310",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "008f6318",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008f6324",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f6174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f6148.md#insn-008f6174) · [`008f6180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f6148.md#insn-008f6180) · [`008f619c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f6148.md#insn-008f619c)
- 新版 `008f631c`（命令位置の公開資料なし） · `008f6338`（命令位置の公開資料なし）

~~~diff
- 008f6174 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 008f6174 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008f6174 bytes e80f00f9
- 008f6180 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008f6180 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 008f631c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 008f631c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 008f6180 bytes 480100b4
+ 008f631c bytes 480100b4
- 008f619c ["INT_ADD", "register:40f0:8", ["const:8f619c:8", "const:4:8"]]
- 008f619c ["CALL", null, ["callee:00c58610:8"]]
+ 008f6338 ["INT_ADD", "register:40f0:8", ["const:8f6338:8", "const:4:8"]]
+ 008f6338 ["CALL", null, ["callee:00c58610:8"]]
- 008f619c bytes 1d880d94
+ 008f6338 bytes b6880d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78fd68147cc24648b623a173dfc94b05"></a>

### [`008f64f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f64f8.md) → [`008f6694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6694.md) FUN_008f6694

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f65c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f65c8.md) · 呼出先 7件 [`0066d09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d09c.md) [`006c417c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c417c.md) [`006d1808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1808.md) [`008ed01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ed/008ed01c.md) [`008ef76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef76c.md)
- 新版 呼出元 1件 [`008f6764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6764.md) · 呼出先 7件 [`0066d0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d0dc.md) [`006c41bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c41bc.md) [`006d1848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d1/006d1848.md) [`008ed1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ed/008ed1b8.md) [`008ef908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ef/008ef908.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 30.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008f6510"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008f66ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008f66b4",
      "incomplete_value": false,
      "site": "008f66c8",
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
      "definition_site": "008f6518",
      "incomplete_value": false,
      "site": "008f652c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008f650c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008f6510",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f66d4"
      ]
    ],
    [
      "008f66b4",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f66a8",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008f66ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f66d4"
      ]
    ],
    [
      "008f66b4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f6510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f64f8.md#insn-008f6510) · [`008f652c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f64f8.md#insn-008f652c) · [`008f6574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f64f8.md#insn-008f6574)
- 新版 `008f66c8`（命令位置の公開資料なし） · `008f6710`（命令位置の公開資料なし）

~~~diff
- 008f6510 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008f6510 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 008f6510 bytes 480100b4
- 008f652c ["INT_ADD", "register:40f0:8", ["const:8f652c:8", "const:4:8"]]
- 008f652c ["CALL", null, ["callee:00c58610:8"]]
+ 008f66c8 ["INT_ADD", "register:40f0:8", ["const:8f66c8:8", "const:4:8"]]
+ 008f66c8 ["CALL", null, ["callee:00c58610:8"]]
- 008f652c bytes 39870d94
+ 008f66c8 bytes d2870d94
- 008f6574 ["INT_ADD", "register:40f0:8", ["const:8f6574:8", "const:4:8"]]
- 008f6574 ["CALL", null, ["callee:008ed1b8:8"]]
+ 008f6710 ["INT_ADD", "register:40f0:8", ["const:8f6710:8", "const:4:8"]]
+ 008f6710 ["CALL", null, ["callee:008ed1b8:8"]]
- 008f6574 bytes aadaff97
+ 008f6710 bytes aadaff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92997b3c06095d3d9867f078239587a0"></a>

### [`008f8850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8850.md) → [`008f89ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f8/008f89ec.md) FUN_008f89ec

採用 · 移動量 `+0x19c` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008eb9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb9dc.md) [`008ebcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008ebcd8.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`008ebb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008ebb78.md) [`008ebe74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008ebe74.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "008f89f8",
      "incomplete_value": false,
      "site": "008f89fc",
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
      "definition_site": "008f885c",
      "incomplete_value": false,
      "site": "008f8860",
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
      "008f89f8",
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
      "008f89f8",
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

- 旧版 [`008f8860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8850.md#insn-008f8860) · [`008f885c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8850.md#insn-008f885c)
- 新版 `008f89fc`（命令位置の公開資料なし） · `008f89f8`（命令位置の公開資料なし）

~~~diff
- 008f8860 ["INT_ADD", "register:40f0:8", ["const:8f8860:8", "const:4:8"]]
- 008f8860 ["CALL", null, ["callee:0043b778:8"]]
+ 008f89fc ["INT_ADD", "register:40f0:8", ["const:8f89fc:8", "const:4:8"]]
+ 008f89fc ["CALL", null, ["callee:0043b778:8"]]
- 008f8860 bytes b60bed97
+ 008f89fc bytes 5f0bed97
- 008f885c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 008f885c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008f885c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008f885c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008f89f8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 008f89f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008f89f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008f89f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008f885c bytes 00303c91
+ 008f89f8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd45d02528589820220dbaeb0f1e0e44"></a>

### [`008f8868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8868.md) → [`008f8a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f8/008f8a04.md) FUN_008f8a04

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
      "definition_site": "008f8a28",
      "incomplete_value": false,
      "site": "008f8a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f888c",
      "incomplete_value": false,
      "site": "008f888c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
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
      "008f8a28",
      "DATA",
      [
        "storage",
        "00c854f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f8a28",
      "DATA",
      [
        "storage",
        "00c858f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f887c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8868.md#insn-008f887c) · [`008f8888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8868.md#insn-008f8888)
- 新版 `008f8a18`（命令位置の公開資料なし） · `008f8a24`（命令位置の公開資料なし）

~~~diff
- 008f887c ["INT_ADD", "register:40f0:8", ["const:8f887c:8", "const:4:8"]]
- 008f887c ["CALL", null, ["callee:00c57e90:8"]]
+ 008f8a18 ["INT_ADD", "register:40f0:8", ["const:8f8a18:8", "const:4:8"]]
+ 008f8a18 ["CALL", null, ["callee:00c57e90:8"]]
- 008f887c bytes 857c0d94
+ 008f8a18 bytes 1e7d0d94
- 008f8888 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 008f8888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f8888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f8888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f8a24 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 008f8a24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f8a24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f8a24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f8888 bytes 08e11391
+ 008f8a24 bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-546642077678ec186dfb11ed01925240"></a>

### [`008f889c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f889c.md) → [`008f8a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f8/008f8a38.md) FUN_008f8a38

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
      "definition_site": "008f8a44",
      "incomplete_value": false,
      "site": "008f8a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f88a8",
      "incomplete_value": false,
      "site": "008f88a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
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
      "008f8a44",
      "DATA",
      [
        "storage",
        "00c854f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f8a44",
      "DATA",
      [
        "storage",
        "00c858f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f88a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f889c.md#insn-008f88a4)
- 新版 `008f8a40`（命令位置の公開資料なし）

~~~diff
- 008f88a4 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 008f88a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f88a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f88a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f8a40 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 008f8a40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f8a40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f8a40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f88a4 bytes 29e11391
+ 008f8a40 bytes 29e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fde4d55464500f16816b292502c8036b"></a>

### [`008f88b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f88b8.md) → [`008f8a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f8/008f8a54.md) FUN_008f8a54

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "008f8a78",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008f88dc",
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
      "008f8a78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008f8a78",
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

- 旧版 [`008f88dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f88b8.md#insn-008f88dc) · [`008f88e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f88b8.md#insn-008f88e8)
- 新版 `008f8a78`（命令位置の公開資料なし） · `008f8a84`（命令位置の公開資料なし）

~~~diff
- 008f88dc ["INT_ADD", "register:40f0:8", ["const:8f88dc:8", "const:4:8"]]
- 008f88dc ["CALL", null, ["ram:47acb4:8"]]
+ 008f8a78 ["INT_ADD", "register:40f0:8", ["const:8f8a78:8", "const:4:8"]]
+ 008f8a78 ["CALL", null, ["ram:47acf4:8"]]
- 008f88dc bytes f608ee97
+ 008f8a78 bytes 9f08ee97
- 008f88e8 ["INT_ADD", "register:40f0:8", ["const:8f88e8:8", "const:4:8"]]
- 008f88e8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 008f8a84 ["INT_ADD", "register:40f0:8", ["const:8f8a84:8", "const:4:8"]]
+ 008f8a84 ["CALL", null, ["callee:0047cdd4:8"]]
- 008f88e8 bytes 2b11ee97
+ 008f8a84 bytes d410ee97
~~~


<a id="compare-1b17344cd66fcce99f74551500e54c8b"></a>

### [`008f8928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8928.md) → [`008f8ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f8/008f8ac4.md) FUN_008f8ac4

採用 · 移動量 `+0x19c` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008f21dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f21dc.md) [`008f8928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8928.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`008f2378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f2/008f2378.md) [`008f8ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f8/008f8ac4.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.72% / 新版 95.72%

CFGの説明率　旧版 80.74% / 新版 80.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f8ee8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f8eec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008f9084"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008f8998",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f8cf4"
      ]
    ],
    [
      "unmatched:008f89c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f8b40"
      ]
    ],
    [
      "unmatched:008f8a10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f8bc0"
      ]
    ]
  ],
  "added": [
    [
      "008f8b34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f8cf4"
      ]
    ],
    [
      "008f8b64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f8b40"
      ]
    ],
    [
      "008f8bac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f8bc0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f8998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8928.md#insn-008f8998) · [`008f89c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8928.md#insn-008f89c8) · [`008f8a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8928.md#insn-008f8a10)

~~~diff
- 008f8998 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008f8998 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 008f8998 bytes 0b0e0054
- 008f89c8 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008f89c8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008f89c8 bytes eafeff54
- 008f8a10 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 008f8a10 bytes a0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6533362e38df78e633cee7edb42c789d"></a>

### [`008f9140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9140.md) → [`008f92dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f92dc.md) FUN_008f92dc

採用 · 移動量 `+0x19c` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008f8928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8928.md) [`008f9140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9140.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`008f8ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f8/008f8ac4.md) [`008f92dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f92dc.md) · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

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
      "definition_site": "008f9434",
      "incomplete_value": false,
      "site": "008f943c",
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
      "definition_site": "008f9298",
      "incomplete_value": false,
      "site": "008f92a0",
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
      "definition_site": "008f94f0",
      "incomplete_value": false,
      "site": "008f94f8",
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
      "definition_site": "008f9354",
      "incomplete_value": false,
      "site": "008f935c",
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
      "definition_site": "008f9508",
      "incomplete_value": false,
      "site": "008f9514",
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
      "definition_site": "008f936c",
      "incomplete_value": false,
      "site": "008f9378",
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
      "008f9434",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "008f94f0",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "008f9508",
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
      "008f9434",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "008f94f0",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "008f9508",
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

- 旧版 [`008f92a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9140.md#insn-008f92a0) · [`008f935c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9140.md#insn-008f935c) · [`008f9378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9140.md#insn-008f9378)
- 新版 `008f943c`（命令位置の公開資料なし） · `008f94f8`（命令位置の公開資料なし） · `008f9514`（命令位置の公開資料なし）

~~~diff
- 008f92a0 ["INT_ADD", "register:40f0:8", ["const:8f92a0:8", "const:4:8"]]
- 008f92a0 ["CALL", null, ["callee:00441e94:8"]]
+ 008f943c ["INT_ADD", "register:40f0:8", ["const:8f943c:8", "const:4:8"]]
+ 008f943c ["CALL", null, ["callee:00441e94:8"]]
- 008f92a0 bytes ed22ed97
+ 008f943c bytes 9622ed97
- 008f935c ["INT_ADD", "register:40f0:8", ["const:8f935c:8", "const:4:8"]]
- 008f935c ["CALL", null, ["callee:00441e94:8"]]
+ 008f94f8 ["INT_ADD", "register:40f0:8", ["const:8f94f8:8", "const:4:8"]]
+ 008f94f8 ["CALL", null, ["callee:00441e94:8"]]
- 008f935c bytes be22ed97
+ 008f94f8 bytes 6722ed97
- 008f9378 ["INT_ADD", "register:40f0:8", ["const:8f9378:8", "const:4:8"]]
- 008f9378 ["CALL", null, ["callee:004427f4:8"]]
+ 008f9514 ["INT_ADD", "register:40f0:8", ["const:8f9514:8", "const:4:8"]]
+ 008f9514 ["CALL", null, ["callee:004427f4:8"]]
- 008f9378 bytes 0f25ed97
+ 008f9514 bytes b824ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d8c65f0e8d7aa868782cb8a569ef76d"></a>

### [`008f9c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c00.md) → [`008f9d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9d9c.md) FUN_008f9d9c

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
      "definition_site": "008f9db0",
      "incomplete_value": false,
      "site": "008f9db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f9c14",
      "incomplete_value": false,
      "site": "008f9c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "008f9db4",
      "DATA",
      [
        "storage",
        "00c85578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f9db4",
      "DATA",
      [
        "storage",
        "00c85978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f9c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c00.md#insn-008f9c0c) · [`008f9c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c00.md#insn-008f9c14)
- 新版 `008f9da8`（命令位置の公開資料なし） · `008f9db0`（命令位置の公開資料なし）

~~~diff
- 008f9c0c ["INT_ADD", "register:40f0:8", ["const:8f9c0c:8", "const:4:8"]]
- 008f9c0c ["CALL", null, ["callee:00c57e90:8"]]
+ 008f9da8 ["INT_ADD", "register:40f0:8", ["const:8f9da8:8", "const:4:8"]]
+ 008f9da8 ["CALL", null, ["callee:00c57e90:8"]]
- 008f9c0c bytes a1770d94
+ 008f9da8 bytes 3a780d94
- 008f9c14 ["COPY", "tmp:0:8", ["const:578:8"]]
- 008f9c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f9c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f9c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f9db0 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 008f9db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f9db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f9db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f9c14 bytes 08e11591
+ 008f9db0 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fad15ad2855cc08aa059c37a2071034"></a>

### [`008f9f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9f70.md) → [`008fa10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa10c.md) FUN_008fa10c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`008f9c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c6c.md) [`008fa0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa0e0.md) [`008fa3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa3a8.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008f9a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9a78.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`008f9e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9e08.md) [`008fa27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa27c.md) [`008fa544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa544.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008f9c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9c14.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 71.74% / 新版 71.74%

CFGの説明率　旧版 33.33% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008fa150",
      "incomplete_value": true,
      "site": "008fa164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "live",
            "register:40b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f9fb4",
      "incomplete_value": true,
      "site": "008f9fc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_ZEXT",
            "8",
            [
              "INT_OR"
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
      "definition_site": "008fa15c",
      "incomplete_value": true,
      "site": "008fa164",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": {
      "definition_site": "008f9fc0",
      "incomplete_value": false,
      "site": "008f9fc8",
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
            "const:6b5:8"
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
      "definition_site": "008fa1b8",
      "incomplete_value": false,
      "site": "008fa1c0",
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
    "old": {
      "definition_site": "008fa01c",
      "incomplete_value": false,
      "site": "008fa024",
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
            "const:6b5:8"
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
      "unmatched:008f9fc0",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "008fa184",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "unmatched:008fa01c",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008fa15c",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "008fa184",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "008fa1b8",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f9fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9f70.md#insn-008f9fc8) · [`008fa024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9f70.md#insn-008fa024) · [`008fa078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9f70.md#insn-008fa078)
- 新版 `008fa164`（命令位置の公開資料なし） · `008fa1c0`（命令位置の公開資料なし） · `008fa214`（命令位置の公開資料なし）

~~~diff
- 008f9fc8 ["INT_ADD", "register:40f0:8", ["const:8f9fc8:8", "const:4:8"]]
- 008f9fc8 ["CALL", null, ["callee:008f9c14:8"]]
+ 008fa164 ["INT_ADD", "register:40f0:8", ["const:8fa164:8", "const:4:8"]]
+ 008fa164 ["CALL", null, ["callee:008f9c14:8"]]
- 008f9fc8 bytes acfeff97
+ 008fa164 bytes acfeff97
- 008fa024 ["INT_ADD", "register:40f0:8", ["const:8fa024:8", "const:4:8"]]
- 008fa024 ["CALL", null, ["callee:008f9c14:8"]]
+ 008fa1c0 ["INT_ADD", "register:40f0:8", ["const:8fa1c0:8", "const:4:8"]]
+ 008fa1c0 ["CALL", null, ["callee:008f9c14:8"]]
- 008fa024 bytes 95feff97
+ 008fa1c0 bytes 95feff97
- 008fa078 ["INT_ADD", "register:40f0:8", ["const:8fa078:8", "const:4:8"]]
- 008fa078 ["CALL", null, ["callee:008f9c14:8"]]
+ 008fa214 ["INT_ADD", "register:40f0:8", ["const:8fa214:8", "const:4:8"]]
+ 008fa214 ["CALL", null, ["callee:008f9c14:8"]]
- 008fa078 bytes 80feff97
+ 008fa214 bytes 80feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-775b7bca453319f2add6db5d1dc64537"></a>

### [`008fa0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa0e0.md) → [`008fa27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa27c.md) FUN_008fa27c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f9c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c6c.md) · 呼出先 2件 [`008f9c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c6c.md) [`008f9f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9f70.md)
- 新版 呼出元 1件 [`008f9e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9e08.md) · 呼出先 2件 [`008f9e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9e08.md) [`008fa10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa10c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.52% / 新版 86.52%

CFGの説明率　旧版 47.22% / 新版 45.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008fa0e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008fa0e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008fa0e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008fa0e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008fa0e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008fa0ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008fa280",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008fa284",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008fa288",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fa0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa0e0.md#insn-008fa0e0) · [`008fa0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa0e0.md#insn-008fa0e4) · [`008fa0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa0e0.md#insn-008fa0e8)
- 新版 `008fa27c`（命令位置の公開資料なし）

~~~diff
- 008fa0e0 ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
- 008fa0e0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 008fa27c ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
+ 008fa27c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 008fa0e0 bytes e20300b4
+ 008fa27c bytes e20300b4
- 008fa0e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008fa0e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008fa0e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 008fa0e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008fa0e4 bytes fd7bbaa9
- 008fa0e8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008fa0e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 008fa0e8 bytes fb0b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5841fdc53b71124b345b0e77fcef4275"></a>

### [`008fa3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa3a8.md) → [`008fa544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa544.md) FUN_008fa544

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008f9c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c6c.md) [`008fa3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa3a8.md) · 呼出先 3件 [`008f9f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9f70.md) [`008fa3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa3a8.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 2件 [`008f9e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9e08.md) [`008fa544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa544.md) · 呼出先 3件 [`008fa10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa10c.md) [`008fa544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa544.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.32% / 新版 94.32%

CFGの説明率　旧版 60.99% / 新版 61.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 2件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008fa42c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008fa42c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008fa5c8"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008fa42c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:008fa430",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008fa6b0"
      ]
    ],
    [
      "unmatched:008fa4ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008fa734"
      ]
    ]
  ],
  "added": [
    [
      "008fa5c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "008fa5cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008fa6b0"
      ]
    ],
    [
      "008fa648",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008fa734"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fa42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa3a8.md#insn-008fa42c) · [`008fa430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa3a8.md#insn-008fa430) · [`008fa43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa3a8.md#insn-008fa43c)

~~~diff
- 008fa42c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008fa42c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008fa42c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 008fa42c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008fa42c bytes a96f3fa9
- 008fa430 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008fa430 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 008fa430 bytes 2a070054
- 008fa43c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008fa43c ["COPY", "tmp:1:8", ["register:40c0:8"]]
- 008fa43c ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 008fa43c ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 008fa43c bytes 08a7989a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-946569049d52155f6d8bcd974edbb997"></a>

### [`008fa9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa9b8.md) → [`008fab54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fab54.md) FUN_008fab54

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
      "definition_site": "008fab68",
      "incomplete_value": false,
      "site": "008fab6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fa9cc",
      "incomplete_value": false,
      "site": "008fa9d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
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
      "008fab6c",
      "DATA",
      [
        "storage",
        "00c855f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fab6c",
      "DATA",
      [
        "storage",
        "00c859f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fa9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa9b8.md#insn-008fa9c4) · [`008fa9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa9b8.md#insn-008fa9cc)
- 新版 `008fab60`（命令位置の公開資料なし） · `008fab68`（命令位置の公開資料なし）

~~~diff
- 008fa9c4 ["INT_ADD", "register:40f0:8", ["const:8fa9c4:8", "const:4:8"]]
- 008fa9c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 008fab60 ["INT_ADD", "register:40f0:8", ["const:8fab60:8", "const:4:8"]]
+ 008fab60 ["CALL", null, ["callee:00c57e90:8"]]
- 008fa9c4 bytes 33740d94
+ 008fab60 bytes cc740d94
- 008fa9cc ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 008fa9cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fa9cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fa9cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fab68 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 008fab68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fab68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fab68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fa9cc bytes 08e11791
+ 008fab68 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec4e31cb82afac6002dcea1db07b2b27"></a>

### [`008fa9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa9dc.md) → [`008fab78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fab78.md) FUN_008fab78

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
      "definition_site": "008fab7c",
      "incomplete_value": false,
      "site": "008fab80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fa9e0",
      "incomplete_value": false,
      "site": "008fa9e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
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
      "008fab80",
      "DATA",
      [
        "storage",
        "00c855f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fab80",
      "DATA",
      [
        "storage",
        "00c859f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fa9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa9dc.md#insn-008fa9e0)
- 新版 `008fab7c`（命令位置の公開資料なし）

~~~diff
- 008fa9e0 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 008fa9e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fa9e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fa9e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fab7c ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 008fab7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fab7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fab7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fa9e0 bytes 08e11791
+ 008fab7c bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80252216ecda208898819b36d432720a"></a>

### [`008fa9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa9f4.md) → [`008fab90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fab90.md) FUN_008fab90

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.25% / 新版 89.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008fac24",
      "incomplete_value": true,
      "site": "008fac38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008faa88",
      "incomplete_value": true,
      "site": "008faa9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:260:8"
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
      "definition_site": "008fac30",
      "incomplete_value": true,
      "site": "008fac40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:37e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008faa94",
      "incomplete_value": true,
      "site": "008faaa4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2b1:8"
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
      "definition_site": "008fac30",
      "incomplete_value": true,
      "site": "008fac40",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008faa94",
      "incomplete_value": true,
      "site": "008faaa4",
      "value": [
        "LOAD",
        "16",
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
      "008fabc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008fac24",
      "READ",
      [
        "storage",
        "002c3260",
        null,
        null
      ]
    ],
    [
      "008fac30",
      "READ",
      [
        "storage",
        "002aa2b1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008fabc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008fac24",
      "READ",
      [
        "storage",
        "002c32a0",
        null,
        null
      ]
    ],
    [
      "008fac30",
      "READ",
      [
        "storage",
        "002aa37e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008faa2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa9f4.md#insn-008faa2c) · [`008faa38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa9f4.md#insn-008faa38) · [`008faa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa9f4.md#insn-008faa6c)
- 新版 `008fabc8`（命令位置の公開資料なし） · `008fabd4`（命令位置の公開資料なし） · `008fac08`（命令位置の公開資料なし）

~~~diff
- 008faa2c ["INT_ADD", "register:40f0:8", ["const:8faa2c:8", "const:4:8"]]
- 008faa2c ["CALL", null, ["ram:47acb4:8"]]
+ 008fabc8 ["INT_ADD", "register:40f0:8", ["const:8fabc8:8", "const:4:8"]]
+ 008fabc8 ["CALL", null, ["ram:47acf4:8"]]
- 008faa2c bytes a200ee97
+ 008fabc8 bytes 4b00ee97
- 008faa38 ["INT_ADD", "register:40f0:8", ["const:8faa38:8", "const:4:8"]]
- 008faa38 ["CALL", null, ["callee:0047cdd4:8"]]
+ 008fabd4 ["INT_ADD", "register:40f0:8", ["const:8fabd4:8", "const:4:8"]]
+ 008fabd4 ["CALL", null, ["callee:0047cdd4:8"]]
- 008faa38 bytes d708ee97
+ 008fabd4 bytes 8008ee97
- 008faa6c ["INT_ADD", "register:40f0:8", ["const:8faa6c:8", "const:4:8"]]
- 008faa6c ["CALL", null, ["callee:008514f8:8"]]
+ 008fac08 ["INT_ADD", "register:40f0:8", ["const:8fac08:8", "const:4:8"]]
+ 008fac08 ["CALL", null, ["callee:008514f8:8"]]
- 008faa6c bytes 935afd97
+ 008fac08 bytes 3c5afd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32523e03cd129c9806de9f1a96e29f69"></a>

### [`008fac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fac48.md) → [`008fade4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fade4.md) FUN_008fade4

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
      "definition_site": "008fade8",
      "incomplete_value": false,
      "site": "008fadec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fac4c",
      "incomplete_value": false,
      "site": "008fac50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "008fadec",
      "DATA",
      [
        "storage",
        "00c85668",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fadec",
      "DATA",
      [
        "storage",
        "00c85a68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fac4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fac48.md#insn-008fac4c)
- 新版 `008fade8`（命令位置の公開資料なし）

~~~diff
- 008fac4c ["COPY", "tmp:0:8", ["const:668:8"]]
- 008fac4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fac4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fac4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fade8 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 008fade8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fade8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fade8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fac4c bytes 08a11991
+ 008fade8 bytes 08a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-364594fad21cffd0c7c47e7ed2784b23"></a>

### [`008fac60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fac60.md) → [`008fadfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fadfc.md) FUN_008fadfc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 25.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008fac68"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008fae04"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008fac84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008fac68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008fae5c"
      ]
    ],
    [
      "unmatched:008fac84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008fae04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008fae5c"
      ]
    ],
    [
      "008fae20",
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

- 旧版 [`008fac68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fac60.md#insn-008fac68) · [`008fac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fac60.md#insn-008fac84) · [`008fac90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fac60.md#insn-008fac90)
- 新版 `008fae2c`（命令位置の公開資料なし）

~~~diff
- 008fac68 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008fac68 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008fac68 bytes c1020054
- 008fac84 ["INT_ADD", "register:40f0:8", ["const:8fac84:8", "const:4:8"]]
- 008fac84 ["CALL", null, ["ram:47acb4:8"]]
- 008fac84 bytes 0c00ee97
- 008fac90 ["INT_ADD", "register:40f0:8", ["const:8fac90:8", "const:4:8"]]
- 008fac90 ["CALL", null, ["callee:0047cdd4:8"]]
+ 008fae2c ["INT_ADD", "register:40f0:8", ["const:8fae2c:8", "const:4:8"]]
+ 008fae2c ["CALL", null, ["callee:0047cdd4:8"]]
- 008fac90 bytes 4108ee97
+ 008fae2c bytes ea07ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

