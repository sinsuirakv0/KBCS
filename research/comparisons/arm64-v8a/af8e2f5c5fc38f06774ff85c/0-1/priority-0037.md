# v15.7.2 → v15.7.3 · 最優先の変更候補 (37)

[一覧の目次](README.md)

<a id="compare-51c2ac2b14e4cda1d52b158faa0c075a"></a>

### [`007ca3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca3b0.md) → [`007ca3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca3b0.md) FUN_007ca3b0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 23件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`0045a030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045a/0045a030.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00574ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff4.md)
- 新版 呼出元 0件  · 呼出先 23件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`0045a030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a030.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.33% / 新版 91.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ca4e8",
      "incomplete_value": true,
      "site": "007ca4e8",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:9df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca4e8",
      "incomplete_value": true,
      "site": "007ca4e8",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:952:8"
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
      "definition_site": "007ca4ec",
      "incomplete_value": true,
      "site": "007ca4ec",
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
      "definition_site": "007ca4ec",
      "incomplete_value": true,
      "site": "007ca4ec",
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
      "definition_site": "007ca550",
      "incomplete_value": true,
      "site": "007ca564",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:394:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca550",
      "incomplete_value": true,
      "site": "007ca564",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:428:8"
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
      "007ca4d8",
      "READ",
      [
        "storage",
        "0029f952",
        null,
        "string"
      ]
    ],
    [
      "007ca4dc",
      "READ",
      [
        "storage",
        "0029f958",
        null,
        "string"
      ]
    ],
    [
      "007ca550",
      "READ",
      [
        "storage",
        "002a8428",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007ca4d8",
      "READ",
      [
        "storage",
        "0029f9df",
        null,
        "string"
      ]
    ],
    [
      "007ca4dc",
      "READ",
      [
        "storage",
        "0029f9e5",
        null,
        "string"
      ]
    ],
    [
      "007ca550",
      "READ",
      [
        "storage",
        "002a8394",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca4d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca3b0.md#insn-007ca4d0) · [`007ca548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca3b0.md#insn-007ca548) · [`007ca57c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca3b0.md#insn-007ca57c)
- 新版 `007ca4d0`（命令位置の公開資料なし） · `007ca548`（命令位置の公開資料なし） · `007ca57c`（命令位置の公開資料なし）

~~~diff
- 007ca4d0 ["COPY", "tmp:0:8", ["const:952:8"]]
- 007ca4d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ca4d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ca4d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ca4d0 ["COPY", "tmp:0:8", ["const:9df:8"]]
+ 007ca4d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ca4d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ca4d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ca4d0 bytes 29492591
+ 007ca4d0 bytes 297d2791
- 007ca548 ["COPY", "tmp:0:8", ["const:428:8"]]
- 007ca548 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ca548 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ca548 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ca548 ["COPY", "tmp:0:8", ["const:394:8"]]
+ 007ca548 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ca548 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ca548 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ca548 bytes 29a11091
+ 007ca548 bytes 29510e91
- 007ca57c ["COPY", "tmp:0:8", ["const:a58:8"]]
- 007ca57c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ca57c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ca57c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ca57c ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 007ca57c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca57c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca57c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ca57c bytes 08612991
+ 007ca57c bytes 08212c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5f94c16f94b3ef79a0f578270ea8785"></a>

### [`007ca9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca9e0.md) → [`007ca9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca9e0.md) FUN_007ca9e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007ca9f4",
      "incomplete_value": false,
      "site": "007ca9f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca9f4",
      "incomplete_value": false,
      "site": "007ca9f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "007ca9f8",
      "DATA",
      [
        "storage",
        "00bff9d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ca9f8",
      "DATA",
      [
        "storage",
        "00bffa88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca9f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca9e0.md#insn-007ca9f4)
- 新版 `007ca9f4`（命令位置の公開資料なし）

~~~diff
- 007ca9f4 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 007ca9f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ca9f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ca9f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ca9f4 ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 007ca9f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca9f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca9f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ca9f4 bytes 08612791
+ 007ca9f4 bytes 08212a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-771906a09fdaab160b6d4b094400b485"></a>

### [`007caa04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007caa04.md) → [`007caa04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caa04.md) FUN_007caa04

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007caa08",
      "incomplete_value": false,
      "site": "007caa0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007caa08",
      "incomplete_value": false,
      "site": "007caa0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "007caa0c",
      "DATA",
      [
        "storage",
        "00bff9d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007caa0c",
      "DATA",
      [
        "storage",
        "00bffa88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007caa08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007caa04.md#insn-007caa08)
- 新版 `007caa08`（命令位置の公開資料なし）

~~~diff
- 007caa08 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 007caa08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007caa08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007caa08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007caa08 ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 007caa08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007caa08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007caa08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007caa08 bytes 08612791
+ 007caa08 bytes 08212a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff56f74aed6123afdb416626af5be42a"></a>

### [`007caab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007caab4.md) → [`007caab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caab4.md) FUN_007caab4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007caab8",
      "incomplete_value": false,
      "site": "007caabc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007caab8",
      "incomplete_value": false,
      "site": "007caabc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
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
      "007caabc",
      "DATA",
      [
        "storage",
        "00bffa58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007caabc",
      "DATA",
      [
        "storage",
        "00bffb08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007caab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007caab4.md#insn-007caab8)
- 新版 `007caab8`（命令位置の公開資料なし）

~~~diff
- 007caab8 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 007caab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007caab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007caab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007caab8 ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 007caab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007caab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007caab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007caab8 bytes 08612991
+ 007caab8 bytes 08212c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9471b1c7149b66a0925c8aea26e8735"></a>

### [`007cab40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007cab40.md) → [`007cab40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cab40.md) FUN_007cab40

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007cab60",
      "incomplete_value": false,
      "site": "007cab64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cab60",
      "incomplete_value": false,
      "site": "007cab64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "007cab64",
      "DATA",
      [
        "storage",
        "00bffaf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cab64",
      "DATA",
      [
        "storage",
        "00bffba8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cab60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007cab40.md#insn-007cab60)
- 新版 `007cab60`（命令位置の公開資料なし）

~~~diff
- 007cab60 ["COPY", "tmp:0:8", ["const:af8:8"]]
- 007cab60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cab60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cab60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cab60 ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 007cab60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cab60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cab60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cab60 bytes 08e12b91
+ 007cab60 bytes 08a12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc03afebc4af03c263dc80a24bd51be0"></a>

### [`007cac74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007cac74.md) → [`007cac74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cac74.md) FUN_007cac74

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007cac88",
      "incomplete_value": false,
      "site": "007cac8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cac88",
      "incomplete_value": false,
      "site": "007cac8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "007cac8c",
      "DATA",
      [
        "storage",
        "00bffb78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cac8c",
      "DATA",
      [
        "storage",
        "00bffc28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cac88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007cac74.md#insn-007cac88)
- 新版 `007cac88`（命令位置の公開資料なし）

~~~diff
- 007cac88 ["COPY", "tmp:0:8", ["const:b78:8"]]
- 007cac88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cac88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cac88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cac88 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 007cac88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cac88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cac88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cac88 bytes 08e12d91
+ 007cac88 bytes 08a13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e05a27b5b3a4ebaa4d781aec5b2b606"></a>

### [`007cad1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007cad1c.md) → [`007cad1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cad1c.md) FUN_007cad1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007cad40",
      "incomplete_value": false,
      "site": "007cad40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cad40",
      "incomplete_value": false,
      "site": "007cad40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "007cad40",
      "DATA",
      [
        "storage",
        "00bffbf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cad40",
      "DATA",
      [
        "storage",
        "00bffca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cad3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007cad1c.md#insn-007cad3c)
- 新版 `007cad3c`（命令位置の公開資料なし）

~~~diff
- 007cad3c ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 007cad3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cad3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cad3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cad3c ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 007cad3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cad3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cad3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cad3c bytes 08e12f91
+ 007cad3c bytes 08a13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7d5a4a24ab0c50ba19e378b80c4e714"></a>

### [`007cae68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007cae68.md) → [`007cae68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cae68.md) FUN_007cae68

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007cae88",
      "incomplete_value": false,
      "site": "007cae8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cae88",
      "incomplete_value": false,
      "site": "007cae8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "007cae8c",
      "DATA",
      [
        "storage",
        "00bffc78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cae8c",
      "DATA",
      [
        "storage",
        "00bffd28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cae88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007cae68.md#insn-007cae88)
- 新版 `007cae88`（命令位置の公開資料なし）

~~~diff
- 007cae88 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 007cae88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cae88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cae88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cae88 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 007cae88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cae88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cae88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cae88 bytes 08e13191
+ 007cae88 bytes 08a13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bdcd8ebeb707b8239b411f89f489779"></a>

### [`007caec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007caec0.md) → [`007caec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caec0.md) FUN_007caec0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 17件 [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`00446784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446784.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446784.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007caf1c",
      "incomplete_value": true,
      "site": "007caf1c",
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
      "definition_site": "007caf1c",
      "incomplete_value": true,
      "site": "007caf1c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007caf18",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007caf24",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007caf2c",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007caf18",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007caf24",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007caf2c",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007caf18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007caec0.md#insn-007caf18) · [`007caf24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007caec0.md#insn-007caf24) · [`007caf2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007caec0.md#insn-007caf2c)
- 新版 `007caf18`（命令位置の公開資料なし） · `007caf24`（命令位置の公開資料なし） · `007caf2c`（命令位置の公開資料なし）

~~~diff
- 007caf18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007caf18 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007caf18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007caf18 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007caf18 bytes 00dd44f9
+ 007caf18 bytes 003d45f9
- 007caf24 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007caf24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007caf24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007caf24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007caf24 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007caf24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007caf24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007caf24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007caf24 bytes 21603691
+ 007caf24 bytes 21203991
- 007caf2c ["COPY", "tmp:0:8", ["const:468:8"]]
- 007caf2c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007caf2c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007caf2c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007caf2c ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007caf2c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007caf2c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007caf2c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007caf2c bytes 42a01191
+ 007caf2c bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34992a125d7ee11e349115e431c0d14d"></a>

### [`007cb37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cb37c.md) → [`007cb37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb37c.md) FUN_007cb37c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "007cb388",
      "incomplete_value": false,
      "site": "007cb38c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb388",
      "incomplete_value": false,
      "site": "007cb38c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "007cb38c",
      "DATA",
      [
        "storage",
        "00bffd78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cb38c",
      "DATA",
      [
        "storage",
        "00bffe28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cb388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cb37c.md#insn-007cb388)
- 新版 `007cb388`（命令位置の公開資料なし）

~~~diff
- 007cb388 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 007cb388 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cb388 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cb388 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cb388 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 007cb388 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb388 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb388 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cb388 bytes 29e13591
+ 007cb388 bytes 29a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd1a3718caa3b8d46b9a10ceb1a4f6f5"></a>

### [`007cb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cb3a0.md) → [`007cb3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb3a0.md) FUN_007cb3a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "007cb3a8",
      "incomplete_value": false,
      "site": "007cb3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb3a8",
      "incomplete_value": false,
      "site": "007cb3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "007cb3ac",
      "DATA",
      [
        "storage",
        "00bffd78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cb3ac",
      "DATA",
      [
        "storage",
        "00bffe28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cb3a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cb3a0.md#insn-007cb3a8)
- 新版 `007cb3a8`（命令位置の公開資料なし）

~~~diff
- 007cb3a8 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 007cb3a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cb3a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cb3a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cb3a8 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 007cb3a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb3a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb3a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cb3a8 bytes 29e13591
+ 007cb3a8 bytes 29a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-810e5b179c3e01190f7653ea38aa3d3f"></a>

### [`007cb4a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cb4a4.md) → [`007cb4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb4a4.md) FUN_007cb4a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

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
      "definition_site": "007cb4dc",
      "incomplete_value": false,
      "site": "007cb4dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb4dc",
      "incomplete_value": false,
      "site": "007cb4dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "007cb4dc",
      "DATA",
      [
        "storage",
        "00bffd78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cb4dc",
      "DATA",
      [
        "storage",
        "00bffe28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cb4d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cb4a4.md#insn-007cb4d8)
- 新版 `007cb4d8`（命令位置の公開資料なし）

~~~diff
- 007cb4d8 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 007cb4d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007cb4d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007cb4d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007cb4d8 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 007cb4d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007cb4d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007cb4d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007cb4d8 bytes 4ae13591
+ 007cb4d8 bytes 4aa13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16b9770dec87f265f5333170cd26e4de"></a>

### [`007cb5a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cb5a0.md) → [`007cb5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb5a0.md) FUN_007cb5a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007cbcc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbcc0.md) [`007cbcc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbcc4.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007cbcc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbcc0.md) [`007cbcc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbcc4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.51% / 新版 97.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007cb680",
      "incomplete_value": true,
      "site": "007cb690",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:295000:8"
              ],
              [
                "leaf",
                "const:f33:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb680",
      "incomplete_value": true,
      "site": "007cb690",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:295000:8"
              ],
              [
                "leaf",
                "const:ea6:8"
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
      "definition_site": "007cb6a8",
      "incomplete_value": false,
      "site": "007cb6b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb6a8",
      "incomplete_value": false,
      "site": "007cb6b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "definition_site": "007cb6e8",
      "incomplete_value": true,
      "site": "007cb6fc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:298000:8"
              ],
              [
                "leaf",
                "const:6c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb6e8",
      "incomplete_value": true,
      "site": "007cb6fc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:297000:8"
              ],
              [
                "leaf",
                "const:fdf:8"
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
      "007cb680",
      "READ",
      [
        "storage",
        "00295ea6",
        null,
        "string"
      ]
    ],
    [
      "007cb6b0",
      "DATA",
      [
        "storage",
        "00bffde8",
        null,
        "undefined *"
      ]
    ],
    [
      "007cb6e8",
      "READ",
      [
        "storage",
        "00297fdf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007cb680",
      "READ",
      [
        "storage",
        "00295f33",
        null,
        "string"
      ]
    ],
    [
      "007cb6b0",
      "DATA",
      [
        "storage",
        "00bffe98",
        null,
        "undefined *"
      ]
    ],
    [
      "007cb6e8",
      "READ",
      [
        "storage",
        "0029806c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cb678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cb5a0.md#insn-007cb678) · [`007cb6a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cb5a0.md#insn-007cb6a8) · [`007cb6dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cb5a0.md#insn-007cb6dc)
- 新版 `007cb678`（命令位置の公開資料なし） · `007cb6a8`（命令位置の公開資料なし） · `007cb6dc`（命令位置の公開資料なし）

~~~diff
- 007cb678 ["COPY", "tmp:0:8", ["const:ea6:8"]]
- 007cb678 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cb678 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cb678 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cb678 ["COPY", "tmp:0:8", ["const:f33:8"]]
+ 007cb678 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb678 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb678 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cb678 bytes 29993a91
+ 007cb678 bytes 29cd3c91
- 007cb6a8 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 007cb6a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cb6a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cb6a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cb6a8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007cb6a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cb6a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cb6a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cb6a8 bytes 08a13791
+ 007cb6a8 bytes 08613a91
- 007cb6dc ["COPY", "register:4048:8", ["const:297000:8"]]
+ 007cb6dc ["COPY", "register:4048:8", ["const:298000:8"]]
- 007cb6dc bytes 69d6ff90
+ 007cb6dc bytes 69d6ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9540c38c706befa66bd2927b1acdfd05"></a>

### [`007cbc8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbc8c.md) → [`007cbc8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbc8c.md) FUN_007cbc8c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007cbca0",
      "incomplete_value": false,
      "site": "007cbca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbca0",
      "incomplete_value": false,
      "site": "007cbca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "007cbca4",
      "DATA",
      [
        "storage",
        "00bffde8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbca4",
      "DATA",
      [
        "storage",
        "00bffe98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbc8c.md#insn-007cbca0)
- 新版 `007cbca0`（命令位置の公開資料なし）

~~~diff
- 007cbca0 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 007cbca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cbca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cbca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cbca0 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007cbca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cbca0 bytes 08a13791
+ 007cbca0 bytes 08613a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3fc7ce00d981844733356690517a737"></a>

### [`007cbcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbcb0.md) → [`007cbcb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbcb0.md) FUN_007cbcb0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007cbcb4",
      "incomplete_value": false,
      "site": "007cbcb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbcb4",
      "incomplete_value": false,
      "site": "007cbcb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "007cbcb8",
      "DATA",
      [
        "storage",
        "00bffde8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbcb8",
      "DATA",
      [
        "storage",
        "00bffe98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbcb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbcb0.md#insn-007cbcb4)
- 新版 `007cbcb4`（命令位置の公開資料なし）

~~~diff
- 007cbcb4 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 007cbcb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cbcb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cbcb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cbcb4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007cbcb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbcb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbcb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cbcb4 bytes 08a13791
+ 007cbcb4 bytes 08613a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcd66f4fc676e9f6fa7560010f6fe36f"></a>

### [`007cbd0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbd0c.md) → [`007cbd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbd0c.md) FUN_007cbd0c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007cbd20",
      "incomplete_value": false,
      "site": "007cbd24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbd20",
      "incomplete_value": false,
      "site": "007cbd24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "007cbd24",
      "DATA",
      [
        "storage",
        "00bffe68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbd24",
      "DATA",
      [
        "storage",
        "00bfff18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbd0c.md#insn-007cbd20)
- 新版 `007cbd20`（命令位置の公開資料なし）

~~~diff
- 007cbd20 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 007cbd20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cbd20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cbd20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cbd20 ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 007cbd20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbd20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbd20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cbd20 bytes 08a13991
+ 007cbd20 bytes 08613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-506e5627457ab4c84d296e1a8c6f55c1"></a>

### [`007cbd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbd30.md) → [`007cbd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbd30.md) FUN_007cbd30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007cbd34",
      "incomplete_value": false,
      "site": "007cbd38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbd34",
      "incomplete_value": false,
      "site": "007cbd38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "007cbd38",
      "DATA",
      [
        "storage",
        "00bffe68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbd38",
      "DATA",
      [
        "storage",
        "00bfff18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbd34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbd30.md#insn-007cbd34)
- 新版 `007cbd34`（命令位置の公開資料なし）

~~~diff
- 007cbd34 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 007cbd34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cbd34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cbd34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cbd34 ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 007cbd34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbd34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbd34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cbd34 bytes 08a13991
+ 007cbd34 bytes 08613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f45315b6ea0ef55f27d8e597d55919d"></a>

### [`007cbd88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbd88.md) → [`007cbd88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbd88.md) FUN_007cbd88

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "007cbd94",
      "incomplete_value": false,
      "site": "007cbd98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbd94",
      "incomplete_value": false,
      "site": "007cbd98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "007cbd98",
      "DATA",
      [
        "storage",
        "00bffef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbd98",
      "DATA",
      [
        "storage",
        "00bfffa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbd94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbd88.md#insn-007cbd94)
- 新版 `007cbd94`（命令位置の公開資料なし）

~~~diff
- 007cbd94 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 007cbd94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cbd94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cbd94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cbd94 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 007cbd94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cbd94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cbd94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cbd94 bytes 29e13b91
+ 007cbd94 bytes 29a13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f110260ecb1afbbe30fe4f2f002b06b"></a>

### [`007cbdac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbdac.md) → [`007cbdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbdac.md) FUN_007cbdac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "007cbdb4",
      "incomplete_value": false,
      "site": "007cbdb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbdb4",
      "incomplete_value": false,
      "site": "007cbdb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "007cbdb8",
      "DATA",
      [
        "storage",
        "00bffef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbdb8",
      "DATA",
      [
        "storage",
        "00bfffa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbdb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbdac.md#insn-007cbdb4)
- 新版 `007cbdb4`（命令位置の公開資料なし）

~~~diff
- 007cbdb4 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 007cbdb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cbdb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cbdb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cbdb4 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 007cbdb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cbdb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cbdb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cbdb4 bytes 29e13b91
+ 007cbdb4 bytes 29a13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d6ba9e1ee029e523b76753cd0e9a67f"></a>

### [`007cbdec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbdec.md) → [`007cbdec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbdec.md) FUN_007cbdec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007cbe1c",
      "incomplete_value": false,
      "site": "007cbe1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbe1c",
      "incomplete_value": false,
      "site": "007cbe1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "007cbe1c",
      "DATA",
      [
        "storage",
        "00bffef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbe1c",
      "DATA",
      [
        "storage",
        "00bfffa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbe10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbdec.md#insn-007cbe10) · [`007cbe14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbdec.md#insn-007cbe14)
- 新版 `007cbe10`（命令位置の公開資料なし） · `007cbe14`（命令位置の公開資料なし）

~~~diff
- 007cbe10 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 007cbe10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cbe10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cbe10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cbe10 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 007cbe10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbe10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbe10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cbe10 bytes 08e13b91
+ 007cbe10 bytes 08a13e91
- 007cbe14 ["COPY", "register:4098:8", ["register:4000:8"]]
- 007cbe14 bytes f30300aa
+ 007cbe14 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 007cbe14 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-824ec7adf461121cd2c36aa8b56d079e"></a>

### [`007cc094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc094.md) → [`007cc094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc094.md) FUN_007cc094

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007cc0b4",
      "incomplete_value": false,
      "site": "007cc0b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc0b4",
      "incomplete_value": false,
      "site": "007cc0b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "007cc0b8",
      "DATA",
      [
        "storage",
        "00bfff78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc0b8",
      "DATA",
      [
        "storage",
        "00c00028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc094.md#insn-007cc0b0) · [`007cc0b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc094.md#insn-007cc0b4)
- 新版 `007cc0b0`（命令位置の公開資料なし） · `007cc0b4`（命令位置の公開資料なし）

~~~diff
- 007cc0b0 ["COPY", "register:4040:8", ["const:bff000:8"]]
+ 007cc0b0 ["COPY", "register:4040:8", ["const:c00000:8"]]
- 007cc0b0 bytes 882100f0
+ 007cc0b0 bytes a8210090
- 007cc0b4 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 007cc0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc0b4 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 007cc0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc0b4 bytes 08e13d91
+ 007cc0b4 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-285a49b98d9373119f45c50d08844fee"></a>

### [`007cc0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc0cc.md) → [`007cc0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc0cc.md) FUN_007cc0cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007cc0d0",
      "incomplete_value": false,
      "site": "007cc0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc0d0",
      "incomplete_value": false,
      "site": "007cc0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "007cc0d4",
      "DATA",
      [
        "storage",
        "00bfff78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc0d4",
      "DATA",
      [
        "storage",
        "00c00028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc0cc.md#insn-007cc0cc) · [`007cc0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc0cc.md#insn-007cc0d0)
- 新版 `007cc0cc`（命令位置の公開資料なし） · `007cc0d0`（命令位置の公開資料なし）

~~~diff
- 007cc0cc ["COPY", "register:4040:8", ["const:bff000:8"]]
+ 007cc0cc ["COPY", "register:4040:8", ["const:c00000:8"]]
- 007cc0cc bytes 882100f0
+ 007cc0cc bytes a8210090
- 007cc0d0 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 007cc0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc0d0 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 007cc0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc0d0 bytes 08e13d91
+ 007cc0d0 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb59ddd9a7535ec9477cee4de4e7d4a0"></a>

### [`007cc0ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc0ec.md) → [`007cc0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc0ec.md) FUN_007cc0ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007cc37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc37c.md) [`007cc380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc380.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007cc37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc37c.md) [`007cc380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc380.md)

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
      "definition_site": "007cc208",
      "incomplete_value": false,
      "site": "007cc208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc208",
      "incomplete_value": false,
      "site": "007cc208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "007cc208",
      "DATA",
      [
        "storage",
        "00bfffe8",
        null,
        "undefined *"
      ]
    ],
    [
      "007cc264",
      "READ",
      [
        "storage",
        "00c00008",
        null,
        "pointer"
      ]
    ],
    [
      "007cc264",
      "READ",
      [
        "storage",
        "00c00010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc208",
      "DATA",
      [
        "storage",
        "00c00098",
        null,
        "undefined *"
      ]
    ],
    [
      "007cc264",
      "READ",
      [
        "storage",
        "00c000b8",
        null,
        "pointer"
      ]
    ],
    [
      "007cc264",
      "READ",
      [
        "storage",
        "00c000c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc0ec.md#insn-007cc1fc) · [`007cc200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc0ec.md#insn-007cc200)
- 新版 `007cc1fc`（命令位置の公開資料なし） · `007cc200`（命令位置の公開資料なし）

~~~diff
- 007cc1fc ["COPY", "register:4048:8", ["const:bff000:8"]]
+ 007cc1fc ["COPY", "register:4048:8", ["const:c00000:8"]]
- 007cc1fc bytes 892100f0
+ 007cc1fc bytes a9210090
- 007cc200 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 007cc200 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cc200 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cc200 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cc200 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 007cc200 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc200 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc200 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cc200 bytes 29a13f91
+ 007cc200 bytes 29610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e4c20358505cb6578e443b978f3a633"></a>

### [`007cc32c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc32c.md) → [`007cc32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc32c.md) FUN_007cc32c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007cc34c",
      "incomplete_value": false,
      "site": "007cc350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc34c",
      "incomplete_value": false,
      "site": "007cc350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "007cc350",
      "DATA",
      [
        "storage",
        "00bfffe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc350",
      "DATA",
      [
        "storage",
        "00c00098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc32c.md#insn-007cc348) · [`007cc34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc32c.md#insn-007cc34c)
- 新版 `007cc348`（命令位置の公開資料なし） · `007cc34c`（命令位置の公開資料なし）

~~~diff
- 007cc348 ["COPY", "register:4040:8", ["const:bff000:8"]]
+ 007cc348 ["COPY", "register:4040:8", ["const:c00000:8"]]
- 007cc348 bytes 882100f0
+ 007cc348 bytes a8210090
- 007cc34c ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 007cc34c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc34c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc34c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc34c ["COPY", "tmp:0:8", ["const:98:8"]]
+ 007cc34c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc34c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc34c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc34c bytes 08a13f91
+ 007cc34c bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f46c3cd1bec4b9a1753237f2a5e7566c"></a>

### [`007cc364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc364.md) → [`007cc364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc364.md) FUN_007cc364

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007cc368",
      "incomplete_value": false,
      "site": "007cc36c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc368",
      "incomplete_value": false,
      "site": "007cc36c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "007cc36c",
      "DATA",
      [
        "storage",
        "00bfffe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc36c",
      "DATA",
      [
        "storage",
        "00c00098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc364.md#insn-007cc364) · [`007cc368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc364.md#insn-007cc368)
- 新版 `007cc364`（命令位置の公開資料なし） · `007cc368`（命令位置の公開資料なし）

~~~diff
- 007cc364 ["COPY", "register:4040:8", ["const:bff000:8"]]
+ 007cc364 ["COPY", "register:4040:8", ["const:c00000:8"]]
- 007cc364 bytes 882100f0
+ 007cc364 bytes a8210090
- 007cc368 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 007cc368 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc368 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc368 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc368 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 007cc368 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc368 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc368 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc368 bytes 08a13f91
+ 007cc368 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97bd2639d3273b654017f10266ad4c03"></a>

### [`007cc3f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc3f8.md) → [`007cc3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc3f8.md) FUN_007cc3f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007cc418",
      "incomplete_value": false,
      "site": "007cc41c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc418",
      "incomplete_value": false,
      "site": "007cc41c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "007cc41c",
      "DATA",
      [
        "storage",
        "00c00078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc41c",
      "DATA",
      [
        "storage",
        "00c00128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc3f8.md#insn-007cc418)
- 新版 `007cc418`（命令位置の公開資料なし）

~~~diff
- 007cc418 ["COPY", "tmp:0:8", ["const:78:8"]]
- 007cc418 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc418 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc418 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc418 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 007cc418 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc418 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc418 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc418 bytes 08e10191
+ 007cc418 bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c6ba0b37da11a58833cda8bfa4b1605"></a>

### [`007cc430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc430.md) → [`007cc430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc430.md) FUN_007cc430

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007cc434",
      "incomplete_value": false,
      "site": "007cc438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc434",
      "incomplete_value": false,
      "site": "007cc438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "007cc438",
      "DATA",
      [
        "storage",
        "00c00078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc438",
      "DATA",
      [
        "storage",
        "00c00128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc430.md#insn-007cc434)
- 新版 `007cc434`（命令位置の公開資料なし）

~~~diff
- 007cc434 ["COPY", "tmp:0:8", ["const:78:8"]]
- 007cc434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc434 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 007cc434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc434 bytes 08e10191
+ 007cc434 bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5182fc305dff1625e810c725d0255ff4"></a>

### [`007cc450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc450.md) → [`007cc450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc450.md) FUN_007cc450

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007cc658`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc658.md) [`007cc65c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc65c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007cc658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc658.md) [`007cc65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc65c.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007cc4f0",
      "incomplete_value": false,
      "site": "007cc4f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc4f0",
      "incomplete_value": false,
      "site": "007cc4f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "007cc4f0",
      "DATA",
      [
        "storage",
        "00c000e8",
        null,
        "undefined *"
      ]
    ],
    [
      "007cc548",
      "READ",
      [
        "storage",
        "00c00108",
        null,
        "pointer"
      ]
    ],
    [
      "007cc548",
      "READ",
      [
        "storage",
        "00c00110",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc4f0",
      "DATA",
      [
        "storage",
        "00c00198",
        null,
        "undefined *"
      ]
    ],
    [
      "007cc548",
      "READ",
      [
        "storage",
        "00c001b8",
        null,
        "pointer"
      ]
    ],
    [
      "007cc548",
      "READ",
      [
        "storage",
        "00c001c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc450.md#insn-007cc4e8) · [`007cc4ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc450.md#insn-007cc4ec)
- 新版 `007cc4e8`（命令位置の公開資料なし） · `007cc4ec`（命令位置の公開資料なし）

~~~diff
- 007cc4e8 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 007cc4e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc4e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc4e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc4e8 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 007cc4e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc4e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc4e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc4e8 bytes 08a10391
+ 007cc4e8 bytes 08610691
- 007cc4ec ["COPY", "tmp:0:8", ["const:20:8"]]
- 007cc4ec ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 007cc4ec ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 007cc4ec ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 007cc4ec bytes f3830091
+ 007cc4ec ["COPY", "tmp:0:8", ["const:20:8"]]
+ 007cc4ec ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
+ 007cc4ec ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
+ 007cc4ec ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
+ 007cc4ec bytes f3830091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05fb7b4bceef042f13404ce1a2c05c63"></a>

### [`007cc610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc610.md) → [`007cc610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc610.md) FUN_007cc610

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007cc634",
      "incomplete_value": false,
      "site": "007cc634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc634",
      "incomplete_value": false,
      "site": "007cc634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "007cc634",
      "DATA",
      [
        "storage",
        "00c000e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc634",
      "DATA",
      [
        "storage",
        "00c00198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc610.md#insn-007cc630)
- 新版 `007cc630`（命令位置の公開資料なし）

~~~diff
- 007cc630 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 007cc630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc630 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 007cc630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc630 bytes 08a10391
+ 007cc630 bytes 08610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0739464fd90b27b1a484c5f9728ee9ae"></a>

### [`007cc644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc644.md) → [`007cc644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc644.md) FUN_007cc644

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007cc650",
      "incomplete_value": false,
      "site": "007cc650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc650",
      "incomplete_value": false,
      "site": "007cc650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "007cc650",
      "DATA",
      [
        "storage",
        "00c000e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc650",
      "DATA",
      [
        "storage",
        "00c00198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc64c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc644.md#insn-007cc64c)
- 新版 `007cc64c`（命令位置の公開資料なし）

~~~diff
- 007cc64c ["COPY", "tmp:0:8", ["const:e8:8"]]
- 007cc64c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cc64c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cc64c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cc64c ["COPY", "tmp:0:8", ["const:198:8"]]
+ 007cc64c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc64c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc64c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cc64c bytes 29a10391
+ 007cc64c bytes 29610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-853b0ff20bc8b8924565d5e53a324f70"></a>

### [`007cc6d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc6d4.md) → [`007cc6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc6d4.md) FUN_007cc6d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007cc6f8",
      "incomplete_value": false,
      "site": "007cc6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc6f8",
      "incomplete_value": false,
      "site": "007cc6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:178:8"
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
      "007cc6f8",
      "DATA",
      [
        "storage",
        "00c00178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc6f8",
      "DATA",
      [
        "storage",
        "00c00228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc6f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc6d4.md#insn-007cc6f4)
- 新版 `007cc6f4`（命令位置の公開資料なし）

~~~diff
- 007cc6f4 ["COPY", "tmp:0:8", ["const:178:8"]]
- 007cc6f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc6f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc6f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc6f4 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 007cc6f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc6f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc6f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc6f4 bytes 08e10591
+ 007cc6f4 bytes 08a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e9a73b4a58a9c6f0daa17979942994d"></a>

### [`007cc708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc708.md) → [`007cc708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc708.md) FUN_007cc708

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007cc714",
      "incomplete_value": false,
      "site": "007cc714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc714",
      "incomplete_value": false,
      "site": "007cc714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:178:8"
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
      "007cc714",
      "DATA",
      [
        "storage",
        "00c00178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc714",
      "DATA",
      [
        "storage",
        "00c00228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc708.md#insn-007cc710)
- 新版 `007cc710`（命令位置の公開資料なし）

~~~diff
- 007cc710 ["COPY", "tmp:0:8", ["const:178:8"]]
- 007cc710 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cc710 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cc710 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cc710 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 007cc710 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc710 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc710 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cc710 bytes 29e10591
+ 007cc710 bytes 29a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40c5cc4ddf56578aa87bb2eaf6847ff2"></a>

### [`007cc7c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc7c4.md) → [`007cc7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc7c4.md) FUN_007cc7c4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "007cc7cc",
      "incomplete_value": false,
      "site": "007cc7d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc7cc",
      "incomplete_value": false,
      "site": "007cc7d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "007cc7d0",
      "DATA",
      [
        "storage",
        "00c001f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc7d0",
      "DATA",
      [
        "storage",
        "00c002a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc7cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc7c4.md#insn-007cc7cc)
- 新版 `007cc7cc`（命令位置の公開資料なし）

~~~diff
- 007cc7cc ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 007cc7cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cc7cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cc7cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cc7cc ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 007cc7cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc7cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc7cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cc7cc bytes 29e10791
+ 007cc7cc bytes 29a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4184674da92e55dd3ed17878e97a8b16"></a>

### [`007cc7e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc7e4.md) → [`007cc7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc7e4.md) FUN_007cc7e4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "007cc7ec",
      "incomplete_value": false,
      "site": "007cc7f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc7ec",
      "incomplete_value": false,
      "site": "007cc7f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "007cc7f0",
      "DATA",
      [
        "storage",
        "00c001f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc7f0",
      "DATA",
      [
        "storage",
        "00c002a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc7e4.md#insn-007cc7ec)
- 新版 `007cc7ec`（命令位置の公開資料なし）

~~~diff
- 007cc7ec ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 007cc7ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cc7ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cc7ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cc7ec ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 007cc7ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc7ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc7ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cc7ec bytes 29e10791
+ 007cc7ec bytes 29a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ca0447820fa881409b5fd14d73c2828"></a>

### [`007cc824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc824.md) → [`007cc824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc824.md) FUN_007cc824

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007cc858",
      "incomplete_value": false,
      "site": "007cc858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc858",
      "incomplete_value": false,
      "site": "007cc858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "007cc858",
      "DATA",
      [
        "storage",
        "00c001f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc858",
      "DATA",
      [
        "storage",
        "00c002a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc824.md#insn-007cc848)
- 新版 `007cc848`（命令位置の公開資料なし）

~~~diff
- 007cc848 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 007cc848 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cc848 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cc848 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cc848 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 007cc848 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc848 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc848 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cc848 bytes 29e10791
+ 007cc848 bytes 29a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c1d87598d360f5ca3580c67d168b3ab"></a>

### [`007cc8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc8a8.md) → [`007cc8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc8a8.md) FUN_007cc8a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

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
      "definition_site": "007cc8ac",
      "incomplete_value": false,
      "site": "007cc8b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc8ac",
      "incomplete_value": false,
      "site": "007cc8b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "007cc8b0",
      "DATA",
      [
        "storage",
        "00c001f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc8b0",
      "DATA",
      [
        "storage",
        "00c002a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc8ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc8a8.md#insn-007cc8ac)
- 新版 `007cc8ac`（命令位置の公開資料なし）

~~~diff
- 007cc8ac ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 007cc8ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc8ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc8ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc8ac ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 007cc8ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc8ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc8ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc8ac bytes 08e10791
+ 007cc8ac bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ea002bb4c6f1cadd7687b12a294083e"></a>

### [`007cc93c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc93c.md) → [`007cc93c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc93c.md) FUN_007cc93c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007ccbb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007ccbb4.md) [`007ccbb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007ccbb8.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007ccbb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccbb4.md) [`007ccbb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccbb8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.20% / 新版 98.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007cca08",
      "incomplete_value": false,
      "site": "007cca10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cca08",
      "incomplete_value": false,
      "site": "007cca10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "007cca10",
      "DATA",
      [
        "storage",
        "00c00268",
        null,
        "undefined *"
      ]
    ],
    [
      "007ccab4",
      "READ",
      [
        "storage",
        "00c00288",
        null,
        "pointer"
      ]
    ],
    [
      "007ccab4",
      "READ",
      [
        "storage",
        "00c00290",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cca10",
      "DATA",
      [
        "storage",
        "00c00318",
        null,
        "undefined *"
      ]
    ],
    [
      "007ccab4",
      "READ",
      [
        "storage",
        "00c00338",
        null,
        "pointer"
      ]
    ],
    [
      "007ccab4",
      "READ",
      [
        "storage",
        "00c00340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc93c.md#insn-007cca08)
- 新版 `007cca08`（命令位置の公開資料なし）

~~~diff
- 007cca08 ["COPY", "tmp:0:8", ["const:268:8"]]
- 007cca08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cca08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cca08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cca08 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 007cca08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cca08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cca08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cca08 bytes 08a10991
+ 007cca08 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5e0b558229a686bdd9842dde35bfdfa"></a>

### [`007ccb80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007ccb80.md) → [`007ccb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccb80.md) FUN_007ccb80

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007ccb94",
      "incomplete_value": false,
      "site": "007ccb98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ccb94",
      "incomplete_value": false,
      "site": "007ccb98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "007ccb98",
      "DATA",
      [
        "storage",
        "00c00268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ccb98",
      "DATA",
      [
        "storage",
        "00c00318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ccb94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007ccb80.md#insn-007ccb94)
- 新版 `007ccb94`（命令位置の公開資料なし）

~~~diff
- 007ccb94 ["COPY", "tmp:0:8", ["const:268:8"]]
- 007ccb94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ccb94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ccb94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ccb94 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 007ccb94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ccb94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ccb94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ccb94 bytes 08a10991
+ 007ccb94 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b83f2796877d8a41cfa9ff86c5d40827"></a>

### [`007ccba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007ccba4.md) → [`007ccba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccba4.md) FUN_007ccba4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ccba8",
      "incomplete_value": true,
      "site": "007ccbac",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ccba8",
      "incomplete_value": true,
      "site": "007ccbac",
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
            "const:268:8"
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
      "007ccbac",
      "DATA",
      [
        "storage",
        "00c00268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ccbac",
      "DATA",
      [
        "storage",
        "00c00318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ccba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007ccba4.md#insn-007ccba8)
- 新版 `007ccba8`（命令位置の公開資料なし）

~~~diff
- 007ccba8 ["COPY", "tmp:0:8", ["const:268:8"]]
- 007ccba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ccba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ccba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ccba8 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 007ccba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ccba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ccba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ccba8 bytes 08a10991
+ 007ccba8 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c382b12f3833e0c339bd09e23324b13c"></a>

### [`007ccd70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007ccd70.md) → [`007ccd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccd70.md) _INIT_141

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ccdac",
      "incomplete_value": true,
      "site": "007ccdc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ccdac",
      "incomplete_value": true,
      "site": "007ccdc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e4:8"
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
      "definition_site": "007ccdd0",
      "incomplete_value": true,
      "site": "007ccdec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ccdd0",
      "incomplete_value": true,
      "site": "007ccdec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f7:8"
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
      "definition_site": "007ccdf0",
      "incomplete_value": true,
      "site": "007cce0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ccdf0",
      "incomplete_value": true,
      "site": "007cce0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da:8"
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
      "007ccdac",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "007ccdd0",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "007ccdf0",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007ccdac",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007ccdd0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007ccdf0",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ccd98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007ccd70.md#insn-007ccd98) · [`007ccd9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007ccd70.md#insn-007ccd9c) · [`007ccda4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007ccd70.md#insn-007ccda4)
- 新版 `007ccd98`（命令位置の公開資料なし） · `007ccd9c`（命令位置の公開資料なし）

~~~diff
- 007ccd98 ["COPY", "register:4098:8", ["const:c27000:8"]]
+ 007ccd98 ["COPY", "register:4098:8", ["const:c28000:8"]]
- 007ccd98 bytes d32200f0
+ 007ccd98 bytes f3220090
- 007ccd9c ["COPY", "tmp:0:8", ["const:f68:8"]]
- 007ccd9c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007ccd9c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007ccd9c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007ccd9c ["COPY", "tmp:0:8", ["const:28:8"]]
+ 007ccd9c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007ccd9c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007ccd9c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007ccd9c bytes 73a23d91
+ 007ccd9c bytes 73a20091
- 007ccda4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007ccda4 bytes c9d6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f28abb04f9ff342f8d39ce82714d80e6"></a>

### [`007cd8ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cd/007cd8ac.md) → [`007cd8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd8ac.md) FUN_007cd8ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`0044dabc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044dabc.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md)
- 新版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0044dabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044dabc.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007cd8f0",
      "incomplete_value": false,
      "site": "007cd8fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cd8f0",
      "incomplete_value": false,
      "site": "007cd8fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "007ce868",
      "incomplete_value": true,
      "site": "007ce874",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ce868",
      "incomplete_value": true,
      "site": "007ce874",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "ordinal": 231,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "007ce880",
      "incomplete_value": true,
      "site": "007ce880",
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ce880",
      "incomplete_value": true,
      "site": "007ce880",
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 232,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007cd8fc",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "007cda6c",
      "READ",
      [
        "storage",
        "00292c64",
        null,
        "string"
      ]
    ],
    [
      "007cda80",
      "READ",
      [
        "storage",
        "00292c6a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007cd8fc",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007cda6c",
      "READ",
      [
        "storage",
        "00292cf1",
        null,
        "string"
      ]
    ],
    [
      "007cda80",
      "READ",
      [
        "storage",
        "00292cf7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cd/007cd8ac.md#insn-007cd8f0) · [`007cda68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cd/007cd8ac.md#insn-007cda68) · [`007ce85c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cd/007cd8ac.md#insn-007ce85c)
- 新版 `007cd8f0`（命令位置の公開資料なし） · `007cda68`（命令位置の公開資料なし） · `007ce85c`（命令位置の公開資料なし）

~~~diff
- 007cd8f0 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 007cd8f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cd8f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cd8f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cd8f0 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 007cd8f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cd8f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cd8f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cd8f0 bytes 08e13191
+ 007cd8f0 bytes 08a13491
- 007cda68 ["COPY", "tmp:0:8", ["const:c64:8"]]
- 007cda68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cda68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cda68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cda68 ["COPY", "tmp:0:8", ["const:cf1:8"]]
+ 007cda68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cda68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cda68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cda68 bytes 29913191
+ 007cda68 bytes 29c53391
- 007ce85c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 007ce85c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007ce85c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 007ce85c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007ce85c bytes 086146f9
+ 007ce85c bytes 08b946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dfb2876fc5dcbcc3756ceb5296404ef"></a>

### [`007d22d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d2/007d22d4.md) → [`007d22d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d2/007d22d4.md) FUN_007d22d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 36件 [`005d996c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d9/005d996c.md) [`005e8d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e8/005e8d4c.md) [`005e97d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e9/005e97d8.md) [`0065042c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00650/0065042c.md) [`00651720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00651/00651720.md) · 呼出先 3件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`007db210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007db210.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 36件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e8d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e8/005e8d4c.md) [`005e97d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e9/005e97d8.md) [`0065042c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00650/0065042c.md) [`00651720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00651/00651720.md) · 呼出先 3件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`007db210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db210.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.86% / 新版 98.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007d242c",
      "incomplete_value": false,
      "site": "007d2430",
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
            "const:5cf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d242c",
      "incomplete_value": false,
      "site": "007d2430",
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
            "const:5d6:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007d242c",
      "PARAM",
      [
        "storage",
        "002a35d6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007d242c",
      "PARAM",
      [
        "storage",
        "002a35cf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007d242c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d2/007d22d4.md#insn-007d242c)
- 新版 `007d242c`（命令位置の公開資料なし）

~~~diff
- 007d242c ["COPY", "tmp:0:8", ["const:5d6:8"]]
- 007d242c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007d242c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007d242c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007d242c ["COPY", "tmp:0:8", ["const:5cf:8"]]
+ 007d242c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007d242c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007d242c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007d242c bytes 00581791
+ 007d242c bytes 003c1791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d34852da8926547ff502dfc6aee68815"></a>

### [`007d48f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d4/007d48f8.md) → [`007d48f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d4/007d48f8.md) FUN_007d48f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007d493c",
      "incomplete_value": false,
      "site": "007d4948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d493c",
      "incomplete_value": false,
      "site": "007d4948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "007d4ac0",
      "incomplete_value": true,
      "site": "007d4ae0",
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
                "const:294000:8"
              ],
              [
                "leaf",
                "const:dbe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d4ac0",
      "incomplete_value": true,
      "site": "007d4ae0",
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
                "const:294000:8"
              ],
              [
                "leaf",
                "const:d31:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007d5400",
      "incomplete_value": true,
      "site": "007d5404",
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
      "definition_site": "007d5400",
      "incomplete_value": true,
      "site": "007d5404",
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
    "ordinal": 151,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007d4948",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "007d495c",
      "READ",
      [
        "storage",
        "00291e54",
        null,
        "string"
      ]
    ],
    [
      "007d4ac0",
      "READ",
      [
        "storage",
        "00294d31",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007d4948",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007d495c",
      "READ",
      [
        "storage",
        "00291ee1",
        null,
        "string"
      ]
    ],
    [
      "007d4ac0",
      "READ",
      [
        "storage",
        "00294dbe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007d493c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d4/007d48f8.md#insn-007d493c) · [`007d4950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d4/007d48f8.md#insn-007d4950)
- 新版 `007d493c`（命令位置の公開資料なし） · `007d4950`（命令位置の公開資料なし）

~~~diff
- 007d493c ["COPY", "tmp:0:8", ["const:c78:8"]]
- 007d493c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007d493c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007d493c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007d493c ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 007d493c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007d493c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007d493c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007d493c bytes 08e13191
+ 007d493c bytes 08a13491
- 007d4950 ["COPY", "register:4048:8", ["const:291000:8"]]
- 007d4950 bytes e9d5ffb0
+ 007d4950 ["COPY", "register:4048:8", ["const:291000:8"]]
+ 007d4950 bytes e9d5ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3943e81e8d5df5a70408c261c64543f4"></a>

### [`007d7f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d7/007d7f14.md) → [`007d7f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d7/007d7f14.md) FUN_007d7f14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`007d55c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d5/007d55c8.md) [`00a5e6e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5e/00a5e6e0.md) [`00a5f0e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5f/00a5f0e4.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`007d55c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d5/007d55c8.md) [`00a5e6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5e6e0.md) [`00a5f0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f0e4.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "007d7f20",
      "incomplete_value": false,
      "site": "007d7f24",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d7f20",
      "incomplete_value": false,
      "site": "007d7f24",
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
            "const:30a:8"
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
      "007d7f20",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007d7f20",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007d7f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d7/007d7f14.md#insn-007d7f20)
- 新版 `007d7f20`（命令位置の公開資料なし）

~~~diff
- 007d7f20 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007d7f20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007d7f20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007d7f20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007d7f20 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007d7f20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007d7f20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007d7f20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007d7f20 bytes 00280c91
+ 007d7f20 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80306df9f67e8db42154bcea29344b69"></a>

### [`007d7f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d7/007d7f28.md) → [`007d7f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d7/007d7f28.md) _INIT_142

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`007cd858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cd/007cd858.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`007cd858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd858.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 83.86% / 新版 83.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 9件, `store_value` 7件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007d7f68",
      "incomplete_value": true,
      "site": "007d7f84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d7f68",
      "incomplete_value": true,
      "site": "007d7f84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e4:8"
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
      "definition_site": "007d7f8c",
      "incomplete_value": true,
      "site": "007d7fa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d7f8c",
      "incomplete_value": true,
      "site": "007d7fa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f7:8"
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
      "definition_site": "007d7fac",
      "incomplete_value": true,
      "site": "007d7fc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d7fac",
      "incomplete_value": true,
      "site": "007d7fc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da:8"
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
      "007d7f68",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "007d7f8c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "007d7fac",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007d7f68",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007d7f8c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007d7fac",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007d8164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d7/007d7f28.md#insn-007d8164) · [`007d7f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d7/007d7f28.md#insn-007d7f54)
- 新版 `007d8164`（命令位置の公開資料なし） · `007d7f54`（命令位置の公開資料なし）

~~~diff
- 007d8164 ["INT_ADD", "register:40f0:8", ["const:7d8164:8", "const:4:8"]]
- 007d8164 ["CALL", null, ["callee:00bdaf90:8"]]
- 007d8164 bytes 5f0b1094
+ 007d8164 ["INT_ADD", "register:40f0:8", ["const:7d8164:8", "const:4:8"]]
+ 007d8164 ["CALL", null, ["callee:00bdaf90:8"]]
+ 007d8164 bytes 8b0b1094
- 007d7f54 ["COPY", "register:4098:8", ["const:c27000:8"]]
+ 007d7f54 ["COPY", "register:4098:8", ["const:c28000:8"]]
- 007d7f54 bytes 93220090
+ 007d7f54 bytes 932200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df3d86033840fa733d491391a80f0bb2"></a>

### [`007d8370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d8/007d8370.md) → [`007d8370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d8/007d8370.md) FUN_007d8370

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ab3338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab3/00ab3338.md) · 呼出先 17件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md) [`00464b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`00465394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465394.md)
- 新版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 17件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465394.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.91% / 新版 95.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007d83bc",
      "incomplete_value": false,
      "site": "007d83c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d83bc",
      "incomplete_value": false,
      "site": "007d83c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "007d86c8",
      "incomplete_value": true,
      "site": "007d86cc",
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
      "definition_site": "007d86c8",
      "incomplete_value": true,
      "site": "007d86cc",
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
    "ordinal": 45,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007d86c4",
      "incomplete_value": true,
      "site": "007d86d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d86c4",
      "incomplete_value": true,
      "site": "007d86d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007d83c0",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "007d86b8",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ],
    [
      "007d86bc",
      "READ",
      [
        "storage",
        "00c1acc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007d83c0",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007d86b8",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "007d86bc",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007d83bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d8/007d8370.md#insn-007d83bc) · [`007d86b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d8/007d8370.md#insn-007d86b8) · [`007d86bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d8/007d8370.md#insn-007d86bc)
- 新版 `007d83bc`（命令位置の公開資料なし） · `007d86b8`（命令位置の公開資料なし） · `007d86bc`（命令位置の公開資料なし）

~~~diff
- 007d83bc ["COPY", "tmp:0:8", ["const:c78:8"]]
- 007d83bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007d83bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007d83bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007d83bc ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 007d83bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007d83bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007d83bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007d83bc bytes 08e13191
+ 007d83bc bytes 08a13491
- 007d86b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 007d86b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007d86b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 007d86b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007d86b8 bytes 086146f9
+ 007d86b8 bytes 08b946f9
- 007d86bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cc8:8"]]
- 007d86bc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 007d86bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
+ 007d86bc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 007d86bc bytes b56646f9
+ 007d86bc bytes b5be46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-870fe565c1490b3796b9165799cfe17e"></a>

### [`007d99a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d9/007d99a4.md) → [`007d99a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d99a4.md) FUN_007d99a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007d9798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d9/007d9798.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007d9798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9798.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007d99b0",
      "incomplete_value": false,
      "site": "007d99b4",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d99b0",
      "incomplete_value": false,
      "site": "007d99b4",
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
            "const:30a:8"
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
      "007d99b0",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007d99b0",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007d99b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d9/007d99a4.md#insn-007d99b0)
- 新版 `007d99b0`（命令位置の公開資料なし）

~~~diff
- 007d99b0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007d99b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007d99b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007d99b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007d99b0 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007d99b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007d99b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007d99b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007d99b0 bytes 00280c91
+ 007d99b0 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31008725db6049ce50331b01349cb495"></a>

### [`007d9de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d9/007d9de8.md) → [`007d9de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9de8.md) FUN_007d9de8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007d99b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d9/007d99b8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007d99b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d99b8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007d9df4",
      "incomplete_value": false,
      "site": "007d9df8",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d9df4",
      "incomplete_value": false,
      "site": "007d9df8",
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
            "const:30a:8"
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
      "007d9df4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007d9df4",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007d9df4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d9/007d9de8.md#insn-007d9df4)
- 新版 `007d9df4`（命令位置の公開資料なし）

~~~diff
- 007d9df4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007d9df4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007d9df4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007d9df4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007d9df4 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007d9df4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007d9df4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007d9df4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007d9df4 bytes 00280c91
+ 007d9df4 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16d933d508b6d614465c104ab9c8dee8"></a>

### [`007d9dfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d9/007d9dfc.md) → [`007d9dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9dfc.md) FUN_007d9dfc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007d8824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d8/007d8824.md) [`00ab3338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab3/00ab3338.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`007d8824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d8/007d8824.md) [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007d9e08",
      "incomplete_value": false,
      "site": "007d9e0c",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d9e08",
      "incomplete_value": false,
      "site": "007d9e0c",
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
            "const:30a:8"
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
      "007d9e08",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007d9e08",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007d9e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d9/007d9dfc.md#insn-007d9e08)
- 新版 `007d9e08`（命令位置の公開資料なし）

~~~diff
- 007d9e08 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007d9e08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007d9e08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007d9e08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007d9e08 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007d9e08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007d9e08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007d9e08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007d9e08 bytes 00280c91
+ 007d9e08 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-091f47c0646e415b9900e126a5d3e04a"></a>

### [`007d9f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d9/007d9f3c.md) → [`007d9f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9f3c.md) FUN_007d9f3c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007d9e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d9/007d9e10.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007d9e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9e10.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007d9f48",
      "incomplete_value": false,
      "site": "007d9f4c",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d9f48",
      "incomplete_value": false,
      "site": "007d9f4c",
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
            "const:30a:8"
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
      "007d9f48",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007d9f48",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007d9f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d9/007d9f3c.md#insn-007d9f48)
- 新版 `007d9f48`（命令位置の公開資料なし）

~~~diff
- 007d9f48 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007d9f48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007d9f48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007d9f48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007d9f48 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007d9f48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007d9f48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007d9f48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007d9f48 bytes 00280c91
+ 007d9f48 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3507d917f267284cac4b4911c53a0b92"></a>

### [`007da15c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da15c.md) → [`007da15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da15c.md) FUN_007da15c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007d9f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d9/007d9f50.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007d9f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9f50.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007da168",
      "incomplete_value": true,
      "site": "007da16c",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007da168",
      "incomplete_value": true,
      "site": "007da16c",
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
            "const:30a:8"
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
      "007da168",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007da168",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007da168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da15c.md#insn-007da168)
- 新版 `007da168`（命令位置の公開資料なし）

~~~diff
- 007da168 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007da168 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007da168 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007da168 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007da168 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007da168 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007da168 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007da168 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007da168 bytes 00280c91
+ 007da168 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be0340e29f0ed3adafd4642d3276edd8"></a>

### [`007da290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da290.md) → [`007da290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da290.md) FUN_007da290

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`007da170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da170.md) [`00aa980c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa9/00aa980c.md) [`00aaa830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa830.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`007da170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da170.md) [`00aa980c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa980c.md) [`00aaa8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa8f8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007da29c",
      "incomplete_value": false,
      "site": "007da2a0",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007da29c",
      "incomplete_value": false,
      "site": "007da2a0",
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
            "const:30a:8"
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
      "007da29c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007da29c",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007da29c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da290.md#insn-007da29c)
- 新版 `007da29c`（命令位置の公開資料なし）

~~~diff
- 007da29c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007da29c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007da29c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007da29c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007da29c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007da29c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007da29c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007da29c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007da29c bytes 00280c91
+ 007da29c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae3e04ea9b3892c88ea435e1ad86535e"></a>

### [`007da2a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da2a4.md) → [`007da2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da2a4.md) _INIT_143

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007da2e0",
      "incomplete_value": true,
      "site": "007da2fc",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007da2e0",
      "incomplete_value": true,
      "site": "007da2fc",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:2e4:8"
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
      "definition_site": "007da304",
      "incomplete_value": true,
      "site": "007da320",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007da304",
      "incomplete_value": true,
      "site": "007da320",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f7:8"
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
      "definition_site": "007da324",
      "incomplete_value": true,
      "site": "007da340",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007da324",
      "incomplete_value": true,
      "site": "007da340",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da:8"
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
      "007da2e0",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "007da304",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "007da324",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007da2e0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007da304",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007da324",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007da2cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da2a4.md#insn-007da2cc) · [`007da2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da2a4.md#insn-007da2d0) · [`007da2d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da2a4.md#insn-007da2d8)
- 新版 `007da2cc`（命令位置の公開資料なし） · `007da2d0`（命令位置の公開資料なし）

~~~diff
- 007da2cc ["COPY", "register:4098:8", ["const:c27000:8"]]
+ 007da2cc ["COPY", "register:4098:8", ["const:c28000:8"]]
- 007da2cc bytes 732200b0
+ 007da2cc bytes 732200d0
- 007da2d0 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 007da2d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007da2d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007da2d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007da2d0 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 007da2d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007da2d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007da2d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007da2d0 bytes 73223f91
+ 007da2d0 bytes 73220291
- 007da2d8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007da2d8 bytes 69d6ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-339807e87bac4e05e70d5eb428b55a78"></a>

### [`007da86c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da86c.md) → [`007da86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da86c.md) FUN_007da86c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) [`009a3648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009a3/009a3648.md) · 呼出先 22件 [`0041e03c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e03c.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0045a6dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045a/0045a6dc.md) [`0045a7e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045a/0045a7e0.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`009a3648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a3/009a3648.md) · 呼出先 22件 [`0041e03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e03c.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045a6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a6dc.md) [`0045a7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a7e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.62% / 新版 96.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007da8b8",
      "incomplete_value": false,
      "site": "007da8c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007da8b8",
      "incomplete_value": false,
      "site": "007da8c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "007da8bc",
      "incomplete_value": true,
      "site": "007da8d0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007da8bc",
      "incomplete_value": true,
      "site": "007da8d0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:d3b:8"
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
      "definition_site": "007dadd4",
      "incomplete_value": true,
      "site": "007dadd8",
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
      "definition_site": "007dadd4",
      "incomplete_value": true,
      "site": "007dadd8",
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
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007da8bc",
      "READ",
      [
        "storage",
        "00294d3b",
        null,
        "string"
      ]
    ],
    [
      "007da8c4",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "007dadc4",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007da8bc",
      "READ",
      [
        "storage",
        "00294dc8",
        null,
        "string"
      ]
    ],
    [
      "007da8c4",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007dadc4",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007da8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da86c.md#insn-007da8b0) · [`007da8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da86c.md#insn-007da8b4)
- 新版 `007da8b0`（命令位置の公開資料なし） · `007da8b4`（命令位置の公開資料なし）

~~~diff
- 007da8b0 ["COPY", "tmp:0:8", ["const:d3b:8"]]
- 007da8b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007da8b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007da8b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007da8b0 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 007da8b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007da8b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007da8b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007da8b0 bytes 29ed3491
+ 007da8b0 bytes 29213791
- 007da8b4 ["COPY", "register:4040:8", ["const:be7000:8"]]
- 007da8b4 bytes 682000b0
+ 007da8b4 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 007da8b4 bytes 682000b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94cd1c8ef7a69f0b246265b4d485c294"></a>

### [`007dafe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007dafe4.md) → [`007dafe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007dafe4.md) FUN_007dafe4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 9件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md) [`00ab1128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab1/00ab1128.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 9件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`00ab11f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab11f0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007db020",
      "incomplete_value": false,
      "site": "007db02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007db020",
      "incomplete_value": false,
      "site": "007db02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "007db024",
      "incomplete_value": true,
      "site": "007db038",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007db024",
      "incomplete_value": true,
      "site": "007db038",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:d3b:8"
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
      "definition_site": "007db0c0",
      "incomplete_value": true,
      "site": "007db0c4",
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
      "definition_site": "007db0c0",
      "incomplete_value": true,
      "site": "007db0c4",
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
      "007db024",
      "READ",
      [
        "storage",
        "00294d3b",
        null,
        "string"
      ]
    ],
    [
      "007db02c",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "007db0b0",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007db024",
      "READ",
      [
        "storage",
        "00294dc8",
        null,
        "string"
      ]
    ],
    [
      "007db02c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007db0b0",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007db018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007dafe4.md#insn-007db018) · [`007db01c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007dafe4.md#insn-007db01c)
- 新版 `007db018`（命令位置の公開資料なし） · `007db01c`（命令位置の公開資料なし）

~~~diff
- 007db018 ["COPY", "tmp:0:8", ["const:d3b:8"]]
- 007db018 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007db018 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007db018 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007db018 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 007db018 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007db018 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007db018 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007db018 bytes 29ed3491
+ 007db018 bytes 29213791
- 007db01c ["COPY", "register:4040:8", ["const:be7000:8"]]
- 007db01c bytes 68200090
+ 007db01c ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 007db01c bytes 68200090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2007bec4c091c63fd1b3e1b68b019126"></a>

### [`007db34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007db34c.md) → [`007db34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db34c.md) FUN_007db34c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007db3a0",
      "incomplete_value": false,
      "site": "007db3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007db3a0",
      "incomplete_value": false,
      "site": "007db3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "007dbabc",
      "incomplete_value": true,
      "site": "007dbac8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007dbabc",
      "incomplete_value": true,
      "site": "007dbac8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "ordinal": 101,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007dbae4",
      "incomplete_value": true,
      "site": "007dbae8",
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
      "definition_site": "007dbae4",
      "incomplete_value": true,
      "site": "007dbae8",
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
    "ordinal": 103,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007db3b0",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "007db3c0",
      "PARAM",
      [
        "storage",
        "0029e7e9",
        null,
        "string"
      ]
    ],
    [
      "007dbab0",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007db3b0",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007db3c0",
      "PARAM",
      [
        "storage",
        "0029e876",
        null,
        "string"
      ]
    ],
    [
      "007dbab0",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007db3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007db34c.md#insn-007db3a0) · [`007db3b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007db34c.md#insn-007db3b4)
- 新版 `007db3a0`（命令位置の公開資料なし） · `007db3b4`（命令位置の公開資料なし）

~~~diff
- 007db3a0 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 007db3a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007db3a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007db3a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007db3a0 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 007db3a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007db3a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007db3a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007db3a0 bytes 4ae13191
+ 007db3a0 bytes 4aa13491
- 007db3b4 ["COPY", "register:4050:8", ["const:29e000:8"]]
- 007db3b4 bytes 0ad6fff0
+ 007db3b4 ["COPY", "register:4050:8", ["const:29e000:8"]]
+ 007db3b4 bytes 0ad6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a843fac625acfe1987dae45a416e2fb7"></a>

### [`007dbf7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007dbf7c.md) → [`007dbf7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbf7c.md) FUN_007dbf7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007dbc94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007dbc94.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007dbc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbc94.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007dbf88",
      "incomplete_value": false,
      "site": "007dbf8c",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007dbf88",
      "incomplete_value": false,
      "site": "007dbf8c",
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
            "const:30a:8"
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
      "007dbf88",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007dbf88",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007dbf88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007dbf7c.md#insn-007dbf88)
- 新版 `007dbf88`（命令位置の公開資料なし）

~~~diff
- 007dbf88 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007dbf88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007dbf88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007dbf88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007dbf88 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007dbf88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbf88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbf88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007dbf88 bytes 00280c91
+ 007dbf88 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38bc38d2dec76e90363c89e41cb3298b"></a>

### [`007dbf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007dbf90.md) → [`007dbf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbf90.md) FUN_007dbf90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007db210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007db210.md) [`007db258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007db258.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 2件 [`007db210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db210.md) [`007db258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db258.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "007dbf9c",
      "incomplete_value": false,
      "site": "007dbfa0",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007dbf9c",
      "incomplete_value": false,
      "site": "007dbfa0",
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
            "const:30a:8"
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
      "007dbf9c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007dbf9c",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007dbf9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007dbf90.md#insn-007dbf9c)
- 新版 `007dbf9c`（命令位置の公開資料なし）

~~~diff
- 007dbf9c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007dbf9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007dbf9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007dbf9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007dbf9c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007dbf9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbf9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbf9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007dbf9c bytes 00280c91
+ 007dbf9c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82470905d277769ba599d161d636a259"></a>

### [`007dbfa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007dbfa4.md) → [`007dbfa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbfa4.md) FUN_007dbfa4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007db258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007db258.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`007db258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db258.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "007dbfb0",
      "incomplete_value": false,
      "site": "007dbfb4",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007dbfb0",
      "incomplete_value": false,
      "site": "007dbfb4",
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
            "const:30a:8"
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
      "007dbfb0",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007dbfb0",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007dbfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007dbfa4.md#insn-007dbfb0)
- 新版 `007dbfb0`（命令位置の公開資料なし）

~~~diff
- 007dbfb0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007dbfb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007dbfb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007dbfb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007dbfb0 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007dbfb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbfb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbfb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007dbfb0 bytes 00280c91
+ 007dbfb0 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26bc27fc24bd53e16f65a43fec95565b"></a>

### [`007dbfb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007dbfb8.md) → [`007dbfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbfb8.md) FUN_007dbfb8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007db2c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007db2c4.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`007db2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db2c4.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "007dbfc4",
      "incomplete_value": false,
      "site": "007dbfc8",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007dbfc4",
      "incomplete_value": false,
      "site": "007dbfc8",
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
            "const:30a:8"
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
      "007dbfc4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007dbfc4",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007dbfc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007dbfb8.md#insn-007dbfc4)
- 新版 `007dbfc4`（命令位置の公開資料なし）

~~~diff
- 007dbfc4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007dbfc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007dbfc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007dbfc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007dbfc4 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007dbfc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbfc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbfc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007dbfc4 bytes 00280c91
+ 007dbfc4 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3e907129cef4a7370281b7125399e30"></a>

### [`007dc468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dc/007dc468.md) → [`007dc468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dc468.md) FUN_007dc468

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007dc2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dc/007dc2c0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007dc2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dc2c0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007dc474",
      "incomplete_value": false,
      "site": "007dc478",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007dc474",
      "incomplete_value": false,
      "site": "007dc478",
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
            "const:30a:8"
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
      "007dc474",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007dc474",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007dc474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dc/007dc468.md#insn-007dc474)
- 新版 `007dc474`（命令位置の公開資料なし）

~~~diff
- 007dc474 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007dc474 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007dc474 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007dc474 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007dc474 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007dc474 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007dc474 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007dc474 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007dc474 bytes 00280c91
+ 007dc474 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7c4ed7402a2331edc94533a0a603c2d"></a>

### [`007dc47c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dc/007dc47c.md) → [`007dc47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dc47c.md) _INIT_144

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007dc4b8",
      "incomplete_value": true,
      "site": "007dc4d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007dc4b8",
      "incomplete_value": true,
      "site": "007dc4d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e4:8"
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
      "definition_site": "007dc4dc",
      "incomplete_value": true,
      "site": "007dc4f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007dc4dc",
      "incomplete_value": true,
      "site": "007dc4f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f7:8"
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
      "definition_site": "007dc4fc",
      "incomplete_value": true,
      "site": "007dc518",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007dc4fc",
      "incomplete_value": true,
      "site": "007dc518",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da:8"
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
      "007dc4b8",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "007dc4dc",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "007dc4fc",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007dc4b8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007dc4dc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007dc4fc",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007dc4a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dc/007dc47c.md#insn-007dc4a4) · [`007dc4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dc/007dc47c.md#insn-007dc4a8) · [`007dc4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dc/007dc47c.md#insn-007dc4b0)
- 新版 `007dc4a4`（命令位置の公開資料なし） · `007dc4a8`（命令位置の公開資料なし）

~~~diff
- 007dc4a4 ["COPY", "register:4098:8", ["const:c27000:8"]]
+ 007dc4a4 ["COPY", "register:4098:8", ["const:c28000:8"]]
- 007dc4a4 bytes 532200f0
+ 007dc4a4 bytes 73220090
- 007dc4a8 ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 007dc4a8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007dc4a8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007dc4a8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007dc4a8 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 007dc4a8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007dc4a8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007dc4a8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007dc4a8 bytes 73823f91
+ 007dc4a8 bytes 73820291
- 007dc4b0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007dc4b0 bytes 49d6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c312afb9e4c818332670b4b56cfc5e18"></a>

### [`007dd540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dd/007dd540.md) → [`007dd540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dd/007dd540.md) _INIT_145

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.66% / 新版 92.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007dd768",
      "incomplete_value": false,
      "site": "007dd774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c28000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007dd768",
      "incomplete_value": false,
      "site": "007dd774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
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
      "definition_site": "007dd770",
      "incomplete_value": false,
      "site": "007dd774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007dd770",
      "incomplete_value": false,
      "site": "007dd774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "007dd57c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "007dd5a0",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "007dd5c0",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007dd57c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007dd5a0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007dd5c0",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007dd568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dd/007dd540.md#insn-007dd568) · [`007dd56c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dd/007dd540.md#insn-007dd56c) · [`007dd578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dd/007dd540.md#insn-007dd578)
- 新版 `007dd568`（命令位置の公開資料なし） · `007dd56c`（命令位置の公開資料なし） · `007dd578`（命令位置の公開資料なし）

~~~diff
- 007dd568 ["COPY", "register:4098:8", ["const:c27000:8"]]
+ 007dd568 ["COPY", "register:4098:8", ["const:c28000:8"]]
- 007dd568 bytes 532200d0
+ 007dd568 bytes 532200f0
- 007dd56c ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 007dd56c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007dd56c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007dd56c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007dd56c ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 007dd56c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007dd56c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007dd56c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007dd56c bytes 73e23f91
+ 007dd56c bytes 73e20291
- 007dd578 ["COPY", "tmp:0:8", ["const:2e4:8"]]
- 007dd578 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007dd578 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007dd578 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007dd578 ["COPY", "tmp:0:8", ["const:2dd:8"]]
+ 007dd578 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007dd578 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007dd578 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007dd578 bytes 29910b91
+ 007dd578 bytes 29750b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99df22f1377fcb8ab8a21dab51aac64e"></a>

### [`007dd8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dd/007dd8d0.md) → [`007dd8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dd/007dd8d0.md) FUN_007dd8d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006dd/006ddfb8.md) · 呼出先 29件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00447a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447a10.md)
- 新版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) · 呼出先 29件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00447a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ddac8",
      "incomplete_value": true,
      "site": "007ddadc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:6c4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ddac8",
      "incomplete_value": true,
      "site": "007ddadc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:637:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ddae0",
      "incomplete_value": true,
      "site": "007ddae0",
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
      "definition_site": "007ddae0",
      "incomplete_value": true,
      "site": "007ddae0",
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ddb10",
      "incomplete_value": true,
      "site": "007ddb24",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
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
      "definition_site": "007ddb10",
      "incomplete_value": true,
      "site": "007ddb24",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:6bd:8"
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
      "007ddab4",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "007ddac8",
      "READ",
      [
        "storage",
        "0029e637",
        null,
        "string"
      ]
    ],
    [
      "007ddad0",
      "READ",
      [
        "storage",
        "0029e644",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007ddab4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "007ddac8",
      "READ",
      [
        "storage",
        "0029e6c4",
        null,
        "string"
      ]
    ],
    [
      "007ddad0",
      "READ",
      [
        "storage",
        "0029e6d1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ddaa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dd/007dd8d0.md#insn-007ddaa8) · [`007ddaac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dd/007dd8d0.md#insn-007ddaac) · [`007ddabc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dd/007dd8d0.md#insn-007ddabc)
- 新版 `007ddaa8`（命令位置の公開資料なし） · `007ddaac`（命令位置の公開資料なし）

~~~diff
- 007ddaa8 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 007ddaa8 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 007ddaa8 bytes 282200f0
+ 007ddaa8 bytes 48220090
- 007ddaac ["COPY", "tmp:0:8", ["const:f78:8"]]
- 007ddaac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ddaac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ddaac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ddaac ["COPY", "tmp:0:8", ["const:38:8"]]
+ 007ddaac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ddaac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ddaac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ddaac bytes 08e13d91
+ 007ddaac bytes 08e10091
- 007ddabc ["COPY", "register:4048:8", ["const:29e000:8"]]
- 007ddabc bytes 09d6ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e899254932847df8fdaf6096a5f45bc"></a>

### [`007de628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007de/007de628.md) → [`007de628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007de/007de628.md) FUN_007de628

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00abf464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abf/00abf464.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00449588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449588.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md)
- 新版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449588.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.82% / 新版 97.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007de670",
      "incomplete_value": false,
      "site": "007de67c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007de670",
      "incomplete_value": false,
      "site": "007de67c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "007de6b4",
      "incomplete_value": true,
      "site": "007de6b4",
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
                "const:a6c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007de6b4",
      "incomplete_value": true,
      "site": "007de6b4",
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
                "const:a75:8"
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
      "definition_site": "007deee8",
      "incomplete_value": true,
      "site": "007deeec",
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
      "definition_site": "007deee8",
      "incomplete_value": true,
      "site": "007deeec",
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
    "ordinal": 168,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007de67c",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "007de698",
      "READ",
      [
        "storage",
        "002a9a75",
        null,
        "string"
      ]
    ],
    [
      "007deed8",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007de67c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007de698",
      "READ",
      [
        "storage",
        "002a9a6c",
        null,
        "string"
      ]
    ],
    [
      "007deed8",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007de670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007de/007de628.md#insn-007de670) · [`007de68c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007de/007de628.md#insn-007de68c) · [`007deed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007de/007de628.md#insn-007deed8)
- 新版 `007de670`（命令位置の公開資料なし） · `007de68c`（命令位置の公開資料なし） · `007deed8`（命令位置の公開資料なし）

~~~diff
- 007de670 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 007de670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007de670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007de670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007de670 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 007de670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007de670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007de670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007de670 bytes 08e13191
+ 007de670 bytes 08a13491
- 007de68c ["COPY", "tmp:0:8", ["const:a75:8"]]
- 007de68c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007de68c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007de68c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007de68c ["COPY", "tmp:0:8", ["const:a6c:8"]]
+ 007de68c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007de68c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007de68c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007de68c bytes 29d52991
+ 007de68c bytes 29b12991
- 007deed8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 007deed8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007deed8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 007deed8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007deed8 bytes 086146f9
+ 007deed8 bytes 08b946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-401fbd231fc699f25c33aefe2a8ca060"></a>

### [`007df8d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007df/007df8d4.md) → [`007df8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007df/007df8d4.md) _INIT_146

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007df910",
      "incomplete_value": true,
      "site": "007df92c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007df910",
      "incomplete_value": true,
      "site": "007df92c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e4:8"
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
      "definition_site": "007df934",
      "incomplete_value": true,
      "site": "007df950",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007df934",
      "incomplete_value": true,
      "site": "007df950",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f7:8"
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
      "definition_site": "007df954",
      "incomplete_value": true,
      "site": "007df970",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007df954",
      "incomplete_value": true,
      "site": "007df970",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da:8"
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
      "007df910",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "007df934",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "007df954",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007df910",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007df934",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007df954",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007df900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007df/007df8d4.md#insn-007df900) · [`007df908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007df/007df8d4.md#insn-007df908)
- 新版 `007df900`（命令位置の公開資料なし） · `007df908`（命令位置の公開資料なし）

~~~diff
- 007df900 ["COPY", "tmp:0:8", ["const:10:8"]]
- 007df900 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007df900 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007df900 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007df900 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 007df900 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007df900 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007df900 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007df900 bytes 73420091
+ 007df900 bytes 73420391
- 007df908 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007df908 bytes 49d6ff90
+ 007df908 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 007df908 bytes 49d6ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb52a241c18e0c955917eed29b489d23"></a>

### [`007dfc70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007df/007dfc70.md) → [`007dfc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007df/007dfc70.md) FUN_007dfc70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) · 呼出先 14件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`005f0320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005f0/005f0320.md) [`0069aa8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0069a/0069aa8c.md)
- 新版 呼出元 1件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 14件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`005f0320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0320.md) [`0069aa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069aa8c.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 99.53% / 新版 99.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "007e0030",
      "incomplete_value": true,
      "site": "007e0030",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e0030",
      "incomplete_value": true,
      "site": "007e0030",
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
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007e0030",
      "WRITE",
      [
        "storage",
        "00c23f40",
        null,
        "undefined4"
      ]
    ],
    [
      "007e00d4",
      "DATA",
      [
        "storage",
        "00c23f34",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007e0030",
      "WRITE",
      [
        "storage",
        "00c23ff0",
        null,
        "undefined4"
      ]
    ],
    [
      "007e00d4",
      "DATA",
      [
        "storage",
        "00c23fe4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e0030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007df/007dfc70.md#insn-007e0030) · [`007e0058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007df/007dfc70.md#insn-007e0058)
- 新版 `007e0030`（命令位置の公開資料なし） · `007e0058`（命令位置の公開資料なし）

~~~diff
- 007e0030 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
- 007e0030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 007e0030 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ff0:8"]]
+ 007e0030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 007e0030 bytes 28410fb9
+ 007e0030 bytes 28f10fb9
- 007e0058 ["COPY", "tmp:0:8", ["const:f34:8"]]
- 007e0058 ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
- 007e0058 ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
- 007e0058 ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
+ 007e0058 ["COPY", "tmp:0:8", ["const:fe4:8"]]
+ 007e0058 ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
+ 007e0058 ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
+ 007e0058 ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
- 007e0058 bytes 7bd33c91
+ 007e0058 bytes 7b933f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5985e9ca232992a81d8b57b808245e2"></a>

### [`007e0354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e0/007e0354.md) → [`007e0354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e0354.md) FUN_007e0354

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) · 呼出先 14件 [`004297e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004297e4.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0046ad74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046ad74.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 14件 [`004297e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004297e4.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ad74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046ad74.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e055c",
      "incomplete_value": true,
      "site": "007e056c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:272:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e055c",
      "incomplete_value": true,
      "site": "007e056c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:279:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007e055c",
      "READ",
      [
        "storage",
        "002a4279",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007e055c",
      "READ",
      [
        "storage",
        "002a4272",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e0558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e0/007e0354.md#insn-007e0558)
- 新版 `007e0558`（命令位置の公開資料なし）

~~~diff
- 007e0558 ["COPY", "tmp:0:8", ["const:279:8"]]
- 007e0558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007e0558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007e0558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007e0558 ["COPY", "tmp:0:8", ["const:272:8"]]
+ 007e0558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007e0558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007e0558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007e0558 bytes 08e50991
+ 007e0558 bytes 08c90991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-801c0d4c25785ae8b5913e8352dd179d"></a>

### [`007e09d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e0/007e09d8.md) → [`007e09d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e09d8.md) _INIT_147

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e0a14",
      "incomplete_value": true,
      "site": "007e0a30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e0a14",
      "incomplete_value": true,
      "site": "007e0a30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e4:8"
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
      "definition_site": "007e0a58",
      "incomplete_value": true,
      "site": "007e0a74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e0a58",
      "incomplete_value": true,
      "site": "007e0a74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da:8"
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
      "definition_site": "007e0a94",
      "incomplete_value": true,
      "site": "007e0ab0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:36e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e0a94",
      "incomplete_value": true,
      "site": "007e0ab0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:2e1:8"
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
      "007e0a14",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "007e0a38",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "007e0a58",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007e0a14",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007e0a38",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007e0a58",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e0a04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e0/007e09d8.md#insn-007e0a04) · [`007e0a0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e0/007e09d8.md#insn-007e0a0c)
- 新版 `007e0a04`（命令位置の公開資料なし） · `007e0a0c`（命令位置の公開資料なし）

~~~diff
- 007e0a04 ["COPY", "tmp:0:8", ["const:28:8"]]
- 007e0a04 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007e0a04 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007e0a04 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007e0a04 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 007e0a04 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007e0a04 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007e0a04 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007e0a04 bytes 73a20091
+ 007e0a04 bytes 73a20391
- 007e0a0c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007e0a0c bytes 29d6fff0
+ 007e0a0c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 007e0a0c bytes 29d6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5b6cb2a14753286f7b055afec87381d"></a>

### [`007e0f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e0/007e0f00.md) → [`007e0f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e0f00.md) FUN_007e0f00

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007e5fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e5/007e5fa4.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`0044dabc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044dabc.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md)
- 新版 呼出元 1件 [`007e5fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5fa4.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0044dabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044dabc.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.67% / 新版 94.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007e0f44",
      "incomplete_value": false,
      "site": "007e0f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e0f44",
      "incomplete_value": false,
      "site": "007e0f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "007e0f6c",
      "incomplete_value": true,
      "site": "007e0f84",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29a000:8"
              ],
              [
                "leaf",
                "const:1fe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e0f6c",
      "incomplete_value": true,
      "site": "007e0f84",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29a000:8"
              ],
              [
                "leaf",
                "const:171:8"
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
      "definition_site": "007e10f0",
      "incomplete_value": true,
      "site": "007e1108",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:2c7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e10f0",
      "incomplete_value": true,
      "site": "007e1108",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:23a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007e0f50",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "007e0f6c",
      "READ",
      [
        "storage",
        "0029a171",
        null,
        "string"
      ]
    ],
    [
      "007e10f0",
      "READ",
      [
        "storage",
        "0029923a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007e0f50",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007e0f6c",
      "READ",
      [
        "storage",
        "0029a1fe",
        null,
        "string"
      ]
    ],
    [
      "007e10f0",
      "READ",
      [
        "storage",
        "002992c7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e0f44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e0/007e0f00.md#insn-007e0f44) · [`007e0f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e0/007e0f00.md#insn-007e0f60) · [`007e10e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e0/007e0f00.md#insn-007e10e8)
- 新版 `007e0f44`（命令位置の公開資料なし） · `007e0f60`（命令位置の公開資料なし） · `007e10e8`（命令位置の公開資料なし）

~~~diff
- 007e0f44 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 007e0f44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007e0f44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007e0f44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007e0f44 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 007e0f44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007e0f44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007e0f44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007e0f44 bytes 08e13191
+ 007e0f44 bytes 08a13491
- 007e0f60 ["COPY", "tmp:0:8", ["const:171:8"]]
- 007e0f60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007e0f60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007e0f60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007e0f60 ["COPY", "tmp:0:8", ["const:1fe:8"]]
+ 007e0f60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007e0f60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007e0f60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007e0f60 bytes 29c50591
+ 007e0f60 bytes 29f90791
- 007e10e8 ["COPY", "tmp:0:8", ["const:23a:8"]]
- 007e10e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007e10e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007e10e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007e10e8 ["COPY", "tmp:0:8", ["const:2c7:8"]]
+ 007e10e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007e10e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007e10e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007e10e8 bytes 29e90891
+ 007e10e8 bytes 291d0b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e53a3aa02de214dd0ac3cbe25555eab3"></a>

### [`007e17f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e1/007e17f4.md) → [`007e17f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e1/007e17f4.md) FUN_007e17f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007eb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007eb/007eb290.md) [`007f78c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f7/007f78c4.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`0059d1d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059d/0059d1d4.md)
- 新版 呼出元 2件 [`007eb290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007eb290.md) [`007f78c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f78c4.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0059d1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d1d4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.51% / 新版 99.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e1ba8",
      "incomplete_value": true,
      "site": "007e1bb8",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:a1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e1ba8",
      "incomplete_value": true,
      "site": "007e1bb8",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:135:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007e1ba8",
      "READ",
      [
        "storage",
        "002a8135",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007e1ba8",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e1ba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e1/007e17f4.md#insn-007e1ba4)
- 新版 `007e1ba4`（命令位置の公開資料なし）

~~~diff
- 007e1ba4 ["COPY", "tmp:0:8", ["const:135:8"]]
- 007e1ba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007e1ba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007e1ba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007e1ba4 ["COPY", "tmp:0:8", ["const:a1:8"]]
+ 007e1ba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007e1ba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007e1ba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007e1ba4 bytes 08d50491
+ 007e1ba4 bytes 08850291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f51930081eb0e12e8e0a6d954360039"></a>

### [`007e3220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e3/007e3220.md) → [`007e3220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e3/007e3220.md) FUN_007e3220

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007e5fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e5/007e5fa4.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`007e5fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5fa4.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.01% / 新版 98.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e3550",
      "incomplete_value": true,
      "site": "007e3550",
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
                "const:2a0000:8"
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
    "old": {
      "definition_site": "007e3550",
      "incomplete_value": true,
      "site": "007e3550",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:8eb:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e366c",
      "incomplete_value": true,
      "site": "007e366c",
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
                "const:299000:8"
              ],
              [
                "leaf",
                "const:2d9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e366c",
      "incomplete_value": true,
      "site": "007e366c",
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
                "const:299000:8"
              ],
              [
                "leaf",
                "const:24c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 64,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e38c0",
      "incomplete_value": true,
      "site": "007e38c0",
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
                "const:293000:8"
              ],
              [
                "leaf",
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e38c0",
      "incomplete_value": true,
      "site": "007e38c0",
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
                "const:293000:8"
              ],
              [
                "leaf",
                "const:c93:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 84,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007e3540",
      "READ",
      [
        "storage",
        "002a08eb",
        null,
        "string"
      ]
    ],
    [
      "007e365c",
      "READ",
      [
        "storage",
        "0029924c",
        null,
        "string"
      ]
    ],
    [
      "007e36d8",
      "READ",
      [
        "storage",
        "0029d727",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007e3540",
      "READ",
      [
        "storage",
        "002a0978",
        null,
        "string"
      ]
    ],
    [
      "007e365c",
      "READ",
      [
        "storage",
        "002992d9",
        null,
        "string"
      ]
    ],
    [
      "007e36d8",
      "READ",
      [
        "storage",
        "0029d7b4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e353c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e3/007e3220.md#insn-007e353c) · [`007e364c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e3/007e3220.md#insn-007e364c) · [`007e36c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e3/007e3220.md#insn-007e36c8)
- 新版 `007e353c`（命令位置の公開資料なし） · `007e364c`（命令位置の公開資料なし） · `007e36c8`（命令位置の公開資料なし）

~~~diff
- 007e353c ["COPY", "tmp:0:8", ["const:8eb:8"]]
- 007e353c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007e353c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007e353c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007e353c ["COPY", "tmp:0:8", ["const:978:8"]]
+ 007e353c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007e353c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007e353c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007e353c bytes 4aad2391
+ 007e353c bytes 4ae12591
- 007e364c ["COPY", "tmp:0:8", ["const:24c:8"]]
- 007e364c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007e364c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007e364c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007e364c ["COPY", "tmp:0:8", ["const:2d9:8"]]
+ 007e364c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007e364c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007e364c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007e364c bytes 4a310991
+ 007e364c bytes 4a650b91
- 007e36c8 ["COPY", "tmp:0:8", ["const:727:8"]]
- 007e36c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007e36c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007e36c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007e36c8 ["COPY", "tmp:0:8", ["const:7b4:8"]]
+ 007e36c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007e36c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007e36c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007e36c8 bytes 4a9d1c91
+ 007e36c8 bytes 4ad11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82ac63f8bbadad16fe225f931f449a72"></a>

### [`007e5734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e5/007e5734.md) → [`007e5734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5734.md) FUN_007e5734

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007eafa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ea/007eafa4.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`006f1e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f1/006f1e2c.md) [`006f23b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f2/006f23b4.md) [`006f48c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f4/006f48c4.md)
- 新版 呼出元 1件 [`007eafa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ea/007eafa4.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`006f1e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1e2c.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md) [`006f48c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f4/006f48c4.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.28% / 新版 97.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007e58d0",
      "incomplete_value": false,
      "site": "007e58d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:f64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e58d0",
      "incomplete_value": false,
      "site": "007e58d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:eb4:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007e598c",
      "incomplete_value": false,
      "site": "007e5994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:ff9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e598c",
      "incomplete_value": false,
      "site": "007e5994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:f6c:8"
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
      "definition_site": "007e59b0",
      "incomplete_value": false,
      "site": "007e59bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:d7e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e59b0",
      "incomplete_value": false,
      "site": "007e59bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:d87:8"
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
      "007e58d0",
      "WRITE",
      [
        "storage",
        "00c23eb4",
        null,
        "undefined1"
      ]
    ],
    [
      "007e5994",
      "DATA",
      [
        "storage",
        "00298f6c",
        null,
        "string"
      ]
    ],
    [
      "007e59bc",
      "DATA",
      [
        "storage",
        "002acd87",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007e58d0",
      "WRITE",
      [
        "storage",
        "00c23f64",
        null,
        "undefined1"
      ]
    ],
    [
      "007e5994",
      "DATA",
      [
        "storage",
        "00298ff9",
        null,
        "string"
      ]
    ],
    [
      "007e59bc",
      "DATA",
      [
        "storage",
        "002acd7e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e58d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e5/007e5734.md#insn-007e58d0) · [`007e598c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e5/007e5734.md#insn-007e598c) · [`007e59b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e5/007e5734.md#insn-007e59b0)
- 新版 `007e58d0`（命令位置の公開資料なし） · `007e598c`（命令位置の公開資料なし） · `007e59b0`（命令位置の公開資料なし）

~~~diff
- 007e58d0 ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 007e58d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:eb4:8"]]
- 007e58d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 007e58d0 ["COPY", "tmp:0:4", ["register:40a0:4"]]
+ 007e58d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:f64:8"]]
+ 007e58d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 007e58d0 bytes 14d13a39
+ 007e58d0 bytes 14913d39
- 007e598c ["COPY", "tmp:0:8", ["const:f6c:8"]]
- 007e598c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007e598c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007e598c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007e598c ["COPY", "tmp:0:8", ["const:ff9:8"]]
+ 007e598c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007e598c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007e598c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007e598c bytes 08b13d91
+ 007e598c bytes 08e53f91
- 007e59b0 ["COPY", "tmp:0:8", ["const:d87:8"]]
- 007e59b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007e59b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007e59b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007e59b0 ["COPY", "tmp:0:8", ["const:d7e:8"]]
+ 007e59b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007e59b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007e59b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007e59b0 bytes 081d3691
+ 007e59b0 bytes 08f93591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-694b09c5d045fa03775afd0de91fe028"></a>

### [`007e5fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e5/007e5fa4.md) → [`007e5fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5fa4.md) FUN_007e5fa4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00abf464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abf/00abf464.md) · 呼出先 50件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e03c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e03c.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0042d828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d828.md) [`0044abe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044abe4.md)
- 新版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 50件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e03c.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0042d828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d828.md) [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e6354",
      "incomplete_value": true,
      "site": "007e6364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bfa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e6354",
      "incomplete_value": true,
      "site": "007e6364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c01:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e6358",
      "incomplete_value": true,
      "site": "007e6368",
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
      "definition_site": "007e6358",
      "incomplete_value": true,
      "site": "007e6368",
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
    "ordinal": 53,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e67ec",
      "incomplete_value": true,
      "site": "007e67fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a49:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e67ec",
      "incomplete_value": true,
      "site": "007e67fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 100,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007e5ff4",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "007e6194",
      "DATA",
      [
        "storage",
        "00c002f8",
        null,
        "pointer"
      ]
    ],
    [
      "007e6354",
      "READ",
      [
        "storage",
        "002a6c01",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007e5ff4",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007e6194",
      "DATA",
      [
        "storage",
        "00c003a8",
        null,
        "pointer"
      ]
    ],
    [
      "007e6354",
      "READ",
      [
        "storage",
        "002a6bfa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e5fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e5/007e5fa4.md#insn-007e5fe8) · [`007e6140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e5/007e5fa4.md#insn-007e6140) · [`007e634c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e5/007e5fa4.md#insn-007e634c)
- 新版 `007e5fe8`（命令位置の公開資料なし） · `007e6140`（命令位置の公開資料なし） · `007e634c`（命令位置の公開資料なし）

~~~diff
- 007e5fe8 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 007e5fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007e5fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007e5fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007e5fe8 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 007e5fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007e5fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007e5fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007e5fe8 bytes 08e13191
+ 007e5fe8 bytes 08a13491
- 007e6140 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 007e6140 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 007e6140 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 007e6140 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 007e6140 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 007e6140 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 007e6140 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 007e6140 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 007e6140 bytes 18e30b91
+ 007e6140 bytes 18a30e91
- 007e634c ["COPY", "tmp:0:8", ["const:c01:8"]]
- 007e634c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007e634c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007e634c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007e634c ["COPY", "tmp:0:8", ["const:bfa:8"]]
+ 007e634c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007e634c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007e634c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007e634c bytes 08053091
+ 007e634c bytes 08e92f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-907a8f330fb0def4394fdd9759e9bd1c"></a>

### [`007eb474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007eb/007eb474.md) → [`007eb474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007eb474.md) FUN_007eb474

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f4120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f4/007f4120.md) · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bce8.md) [`004264e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/004264e8.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007eb8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007eb/007eb8f8.md)
- 新版 呼出元 1件 [`007f4120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f4/007f4120.md) · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004264e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007eb8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007eb8f8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.76% / 新版 98.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007eb5a4",
      "incomplete_value": true,
      "site": "007eb5b4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:887:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007eb5a4",
      "incomplete_value": true,
      "site": "007eb5b4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:7fa:8"
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
      "007eb5a4",
      "READ",
      [
        "storage",
        "0029e7fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007eb5a4",
      "READ",
      [
        "storage",
        "0029e887",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007eb59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007eb/007eb474.md#insn-007eb59c)
- 新版 `007eb59c`（命令位置の公開資料なし）

~~~diff
- 007eb59c ["COPY", "tmp:0:8", ["const:7fa:8"]]
- 007eb59c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007eb59c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007eb59c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007eb59c ["COPY", "tmp:0:8", ["const:887:8"]]
+ 007eb59c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007eb59c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007eb59c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007eb59c bytes 29e91f91
+ 007eb59c bytes 291d2291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0141e8495a4c96fc78afd66f195f269f"></a>

### [`007ebab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007eb/007ebab8.md) → [`007ebab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007ebab8.md) FUN_007ebab8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`007ec810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ec/007ec810.md) [`007f3c28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f3/007f3c28.md) [`00800728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00800/00800728.md) · 呼出先 17件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a83e4.md)
- 新版 呼出元 3件 [`007ec810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ec/007ec810.md) [`007f3c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3c28.md) [`00800728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800728.md) · 呼出先 17件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a83e4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.43% / 新版 97.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ebd40",
      "incomplete_value": true,
      "site": "007ebd50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ebd40",
      "incomplete_value": true,
      "site": "007ebd50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d91:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ebe00",
      "incomplete_value": true,
      "site": "007ebe10",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29a000:8"
              ],
              [
                "leaf",
                "const:228:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ebe00",
      "incomplete_value": true,
      "site": "007ebe10",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29a000:8"
              ],
              [
                "leaf",
                "const:19b:8"
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
      "definition_site": "007ebec4",
      "incomplete_value": true,
      "site": "007ebed0",
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
                "const:294000:8"
              ],
              [
                "leaf",
                "const:dec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ebec4",
      "incomplete_value": true,
      "site": "007ebed0",
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
                "const:294000:8"
              ],
              [
                "leaf",
                "const:d5f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 55,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007ebb24",
      "PARAM",
      [
        "storage",
        "00294d59",
        null,
        "string"
      ]
    ],
    [
      "007ebd40",
      "READ",
      [
        "storage",
        "002acd91",
        null,
        "string"
      ]
    ],
    [
      "007ebd74",
      "PARAM",
      [
        "storage",
        "002a46e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007ebb24",
      "PARAM",
      [
        "storage",
        "00294de6",
        null,
        "string"
      ]
    ],
    [
      "007ebd40",
      "READ",
      [
        "storage",
        "002acd88",
        null,
        "string"
      ]
    ],
    [
      "007ebd74",
      "PARAM",
      [
        "storage",
        "002a46d9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ebb24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007eb/007ebab8.md#insn-007ebb24) · [`007ebd38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007eb/007ebab8.md#insn-007ebd38) · [`007ebd74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007eb/007ebab8.md#insn-007ebd74)
- 新版 `007ebb24`（命令位置の公開資料なし） · `007ebd38`（命令位置の公開資料なし） · `007ebd74`（命令位置の公開資料なし）

~~~diff
- 007ebb24 ["COPY", "tmp:0:8", ["const:d59:8"]]
- 007ebb24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007ebb24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007ebb24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007ebb24 ["COPY", "tmp:0:8", ["const:de6:8"]]
+ 007ebb24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007ebb24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007ebb24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007ebb24 bytes 21643591
+ 007ebb24 bytes 21983791
- 007ebd38 ["COPY", "tmp:0:8", ["const:d91:8"]]
- 007ebd38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ebd38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ebd38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ebd38 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 007ebd38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ebd38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ebd38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ebd38 bytes 08453691
+ 007ebd38 bytes 08213691
- 007ebd74 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 007ebd74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007ebd74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007ebd74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007ebd74 ["COPY", "tmp:0:8", ["const:6d9:8"]]
+ 007ebd74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007ebd74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007ebd74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007ebd74 bytes 21801b91
+ 007ebd74 bytes 21641b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a77a969f9fc8334bc57d0e6ef445031d"></a>

### [`007f1d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f1/007f1d24.md) → [`007f1d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f1/007f1d24.md) FUN_007f1d24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`007f4120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f4/007f4120.md) [`007f5814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f5/007f5814.md) · 呼出先 13件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`009e964c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e9/009e964c.md) [`009e9790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e9/009e9790.md)
- 新版 呼出元 2件 [`007f4120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f4/007f4120.md) [`007f5814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f5/007f5814.md) · 呼出先 13件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`009e964c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e964c.md) [`009e9790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9790.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f1ea4",
      "incomplete_value": false,
      "site": "007f1ea8",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d30:8"
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
      "definition_site": "007f1ea4",
      "incomplete_value": false,
      "site": "007f1ea8",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:c80:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f1d64",
      "incomplete_value": true,
      "site": "007f1d64",
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
      "definition_site": "007f1d64",
      "incomplete_value": true,
      "site": "007f1d64",
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
      "definition_site": "007f1d6c",
      "incomplete_value": false,
      "site": "007f1d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f1d6c",
      "incomplete_value": false,
      "site": "007f1d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "007f1d60",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f1d6c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f1d74",
      "PARAM",
      [
        "storage",
        "00c003d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f1d60",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f1d6c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f1d74",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f1d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f1/007f1d24.md#insn-007f1d60) · [`007f1d6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f1/007f1d24.md#insn-007f1d6c) · [`007f1d74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f1/007f1d24.md#insn-007f1d74)
- 新版 `007f1d60`（命令位置の公開資料なし） · `007f1d6c`（命令位置の公開資料なし） · `007f1d74`（命令位置の公開資料なし）

~~~diff
- 007f1d60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b8:8"]]
- 007f1d60 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f1d60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 007f1d60 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007f1d60 bytes 20dd44f9
+ 007f1d60 bytes 203d45f9
- 007f1d6c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007f1d6c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f1d6c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f1d6c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f1d6c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007f1d6c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f1d6c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f1d6c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f1d6c bytes 21603691
+ 007f1d6c bytes 21203991
- 007f1d74 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 007f1d74 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f1d74 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f1d74 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f1d74 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 007f1d74 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f1d74 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f1d74 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f1d74 bytes 42600f91
+ 007f1d74 bytes 42201291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d822ff9a05d727aeaba24fd9fac3c694"></a>

### [`007f24c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f2/007f24c4.md) → [`007f24c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f2/007f24c4.md) FUN_007f24c4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007ffe48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ff/007ffe48.md) · 呼出先 34件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`007ffe48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffe48.md) · 呼出先 34件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.33% / 新版 94.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 20件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f269c",
      "incomplete_value": false,
      "site": "007f269c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f269c",
      "incomplete_value": false,
      "site": "007f269c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f26ec",
      "incomplete_value": false,
      "site": "007f26ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f26ec",
      "incomplete_value": false,
      "site": "007f26ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "definition_site": "007f2a58",
      "incomplete_value": true,
      "site": "007f2a68",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:89a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f2a58",
      "incomplete_value": true,
      "site": "007f2a68",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:80d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 78,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f269c",
      "DATA",
      [
        "storage",
        "00c00400",
        null,
        "undefined *"
      ]
    ],
    [
      "007f26ec",
      "DATA",
      [
        "storage",
        "00c00480",
        null,
        "undefined *"
      ]
    ],
    [
      "007f2a58",
      "READ",
      [
        "storage",
        "0029e80d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f269c",
      "DATA",
      [
        "storage",
        "00c004b0",
        null,
        "undefined *"
      ]
    ],
    [
      "007f26ec",
      "DATA",
      [
        "storage",
        "00c00530",
        null,
        "undefined *"
      ]
    ],
    [
      "007f2a58",
      "READ",
      [
        "storage",
        "0029e89a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f2/007f24c4.md#insn-007f2688) · [`007f26dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f2/007f24c4.md#insn-007f26dc) · [`007f2a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f2/007f24c4.md#insn-007f2a50)
- 新版 `007f2688`（命令位置の公開資料なし） · `007f26dc`（命令位置の公開資料なし） · `007f2a50`（命令位置の公開資料なし）

~~~diff
- 007f2688 ["COPY", "tmp:0:8", ["const:400:8"]]
- 007f2688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2688 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 007f2688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2688 bytes 08011091
+ 007f2688 bytes 08c11291
- 007f26dc ["COPY", "tmp:0:8", ["const:480:8"]]
- 007f26dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f26dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f26dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f26dc ["COPY", "tmp:0:8", ["const:530:8"]]
+ 007f26dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f26dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f26dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f26dc bytes 08011291
+ 007f26dc bytes 08c11491
- 007f2a50 ["COPY", "tmp:0:8", ["const:80d:8"]]
- 007f2a50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2a50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2a50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2a50 ["COPY", "tmp:0:8", ["const:89a:8"]]
+ 007f2a50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2a50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2a50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2a50 bytes 08352091
+ 007f2a50 bytes 08692291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-908a06c9398159a2c05e627268cde14b"></a>

### [`007f3788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f3/007f3788.md) → [`007f3788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3788.md) FUN_007f3788

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007ffe48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ff/007ffe48.md) · 呼出先 22件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007eafa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ea/007eafa4.md) [`007f3c28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f3/007f3c28.md)
- 新版 呼出元 1件 [`007ffe48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffe48.md) · 呼出先 22件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007eafa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ea/007eafa4.md) [`007f3c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3c28.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f380c",
      "incomplete_value": true,
      "site": "007f381c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f380c",
      "incomplete_value": true,
      "site": "007f381c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8cf:8"
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
      "definition_site": "007f3820",
      "incomplete_value": true,
      "site": "007f3820",
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
      "definition_site": "007f3820",
      "incomplete_value": true,
      "site": "007f3820",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f3918",
      "incomplete_value": false,
      "site": "007f3918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f3918",
      "incomplete_value": false,
      "site": "007f3918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "007f380c",
      "READ",
      [
        "storage",
        "002a38cf",
        null,
        "string"
      ]
    ],
    [
      "007f3810",
      "READ",
      [
        "storage",
        "002a38de",
        null,
        "string"
      ]
    ],
    [
      "007f3918",
      "DATA",
      [
        "storage",
        "00c00600",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f380c",
      "READ",
      [
        "storage",
        "002a38c8",
        null,
        "string"
      ]
    ],
    [
      "007f3810",
      "READ",
      [
        "storage",
        "002a38d7",
        null,
        "string"
      ]
    ],
    [
      "007f3918",
      "DATA",
      [
        "storage",
        "00c006b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f3/007f3788.md#insn-007f3804) · [`007f3808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f3/007f3788.md#insn-007f3808)
- 新版 `007f3804`（命令位置の公開資料なし） · `007f3808`（命令位置の公開資料なし）

~~~diff
- 007f3804 ["COPY", "tmp:0:8", ["const:8cf:8"]]
- 007f3804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3804 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 007f3804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3804 bytes 083d2391
+ 007f3804 bytes 08212391
- 007f3808 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 007f3808 bytes e9d5ffb0
+ 007f3808 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 007f3808 bytes e9d5ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eca0da1dce8a41822118cfadbf7ce8ba"></a>

### [`007f3c28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f3/007f3c28.md) → [`007f3c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3c28.md) FUN_007f3c28

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007f3788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f3/007f3788.md) [`007ff948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ff/007ff948.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007ebab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007eb/007ebab8.md) [`007fae20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fae20.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`007f3788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3788.md) [`007ff948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff948.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007ebab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007ebab8.md) [`007fae20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fae20.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.02% / 新版 96.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f3c70",
      "incomplete_value": true,
      "site": "007f3c80",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:2e5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f3c70",
      "incomplete_value": true,
      "site": "007f3c80",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:258:8"
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
      "definition_site": "007f3c74",
      "incomplete_value": true,
      "site": "007f3c84",
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
      "definition_site": "007f3c74",
      "incomplete_value": true,
      "site": "007f3c84",
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
      "007f3c70",
      "READ",
      [
        "storage",
        "00299258",
        null,
        "string"
      ]
    ],
    [
      "007f3c74",
      "READ",
      [
        "storage",
        "00299268",
        null,
        "string"
      ]
    ],
    [
      "007f3df4",
      "PARAM",
      [
        "storage",
        "002ab855",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007f3c70",
      "READ",
      [
        "storage",
        "002992e5",
        null,
        "string"
      ]
    ],
    [
      "007f3c74",
      "READ",
      [
        "storage",
        "002992f5",
        null,
        "string"
      ]
    ],
    [
      "007f3df4",
      "PARAM",
      [
        "storage",
        "002ab85b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3c68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f3/007f3c28.md#insn-007f3c68) · [`007f3c6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f3/007f3c28.md#insn-007f3c6c)
- 新版 `007f3c68`（命令位置の公開資料なし） · `007f3c6c`（命令位置の公開資料なし）

~~~diff
- 007f3c68 ["COPY", "tmp:0:8", ["const:258:8"]]
- 007f3c68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3c68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3c68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3c68 ["COPY", "tmp:0:8", ["const:2e5:8"]]
+ 007f3c68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3c68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3c68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3c68 bytes 08610991
+ 007f3c68 bytes 08950b91
- 007f3c6c ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 007f3c6c bytes e9d5ffb0
+ 007f3c6c ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 007f3c6c bytes e9d5ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1669de40229beebd5ed7de9d3c338993"></a>

### [`007f4120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f4/007f4120.md) → [`007f4120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f4/007f4120.md) FUN_007f4120

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007f78c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f7/007f78c4.md) [`007f8950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8950.md) · 呼出先 31件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00459a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 2件 [`007f78c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f78c4.md) [`007f8950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8950.md) · 呼出先 31件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_destination` 20件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f44b4",
      "incomplete_value": true,
      "site": "007f44c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:605:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f44b4",
      "incomplete_value": true,
      "site": "007f44c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:60c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f47a0",
      "incomplete_value": true,
      "site": "007f47b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:605:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f47a0",
      "incomplete_value": true,
      "site": "007f47b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:60c:8"
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
      "definition_site": "007f49a8",
      "incomplete_value": true,
      "site": "007f49bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:605:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f49a8",
      "incomplete_value": true,
      "site": "007f49bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:60c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 76,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f44a0",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "007f44b4",
      "READ",
      [
        "storage",
        "002a260c",
        null,
        "string"
      ]
    ],
    [
      "007f4568",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "007f44a0",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "007f44b4",
      "READ",
      [
        "storage",
        "002a2605",
        null,
        "string"
      ]
    ],
    [
      "007f4568",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f4498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f4/007f4120.md#insn-007f4498) · [`007f449c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f4/007f4120.md#insn-007f449c) · [`007f44ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f4/007f4120.md#insn-007f44ac)
- 新版 `007f4498`（命令位置の公開資料なし） · `007f449c`（命令位置の公開資料なし） · `007f44ac`（命令位置の公開資料なし）

~~~diff
- 007f4498 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 007f4498 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 007f4498 bytes 88210090
+ 007f4498 bytes 882100b0
- 007f449c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 007f449c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f449c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f449c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f449c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 007f449c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f449c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f449c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f449c bytes 08e13d91
+ 007f449c bytes 08e10091
- 007f44ac ["COPY", "tmp:0:8", ["const:60c:8"]]
- 007f44ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f44ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f44ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f44ac ["COPY", "tmp:0:8", ["const:605:8"]]
+ 007f44ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f44ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f44ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f44ac bytes 29311891
+ 007f44ac bytes 29151891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4604c0a88fef5d16a929eef8065504f"></a>

### [`007f5814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f5/007f5814.md) → [`007f5814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f5/007f5814.md) FUN_007f5814

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f8354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8354.md) · 呼出先 26件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md)
- 新版 呼出元 1件 [`007f8354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8354.md) · 呼出先 26件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f5d28",
      "incomplete_value": true,
      "site": "007f5d28",
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
      "definition_site": "007f5d28",
      "incomplete_value": true,
      "site": "007f5d28",
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
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f5858",
      "incomplete_value": true,
      "site": "007f5858",
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
      "definition_site": "007f5858",
      "incomplete_value": true,
      "site": "007f5858",
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
      "definition_site": "007f5860",
      "incomplete_value": false,
      "site": "007f5874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5860",
      "incomplete_value": false,
      "site": "007f5874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "007f5854",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5860",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5868",
      "PARAM",
      [
        "storage",
        "00c003d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f5854",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5860",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5868",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f5/007f5814.md#insn-007f5854) · [`007f5860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f5/007f5814.md#insn-007f5860) · [`007f5868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f5/007f5814.md#insn-007f5868)
- 新版 `007f5854`（命令位置の公開資料なし） · `007f5860`（命令位置の公開資料なし） · `007f5868`（命令位置の公開資料なし）

~~~diff
- 007f5854 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007f5854 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f5854 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007f5854 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007f5854 bytes 08dd44f9
+ 007f5854 bytes 083d45f9
- 007f5860 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007f5860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f5860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f5860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f5860 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007f5860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f5860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f5860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f5860 bytes 21603691
+ 007f5860 bytes 21203991
- 007f5868 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 007f5868 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f5868 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f5868 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f5868 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 007f5868 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f5868 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f5868 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f5868 bytes 42600f91
+ 007f5868 bytes 42201291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cc8e556dddd77e148738ed12a7bd672"></a>

### [`007f61cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f61cc.md) → [`007f61cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f61cc.md) FUN_007f61cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f7288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f7/007f7288.md) · 呼出先 13件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`0080038c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00800/0080038c.md) [`00800390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00800/00800390.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`007f7288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f7288.md) · 呼出先 13件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0080038c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/0080038c.md) [`00800390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800390.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.99% / 新版 92.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6328",
      "incomplete_value": false,
      "site": "007f6328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6328",
      "incomplete_value": false,
      "site": "007f6328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "definition_site": "007f63b0",
      "incomplete_value": true,
      "site": "007f63b0",
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
      "definition_site": "007f63b0",
      "incomplete_value": true,
      "site": "007f63b0",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f620c",
      "incomplete_value": true,
      "site": "007f620c",
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
      "definition_site": "007f620c",
      "incomplete_value": true,
      "site": "007f620c",
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
      "007f6208",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f6214",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f621c",
      "PARAM",
      [
        "storage",
        "00c003d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f6208",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f6214",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f621c",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f61cc.md#insn-007f6208) · [`007f6214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f61cc.md#insn-007f6214) · [`007f621c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f61cc.md#insn-007f621c)
- 新版 `007f6208`（命令位置の公開資料なし） · `007f6214`（命令位置の公開資料なし） · `007f621c`（命令位置の公開資料なし）

~~~diff
- 007f6208 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007f6208 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f6208 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007f6208 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007f6208 bytes 08dd44f9
+ 007f6208 bytes 083d45f9
- 007f6214 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007f6214 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f6214 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f6214 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f6214 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007f6214 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f6214 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f6214 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f6214 bytes 21603691
+ 007f6214 bytes 21203991
- 007f621c ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 007f621c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f621c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f621c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f621c ["COPY", "tmp:0:8", ["const:488:8"]]
+ 007f621c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f621c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f621c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f621c bytes 42600f91
+ 007f621c bytes 42201291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9705ef6685e89b2691ed89653f7fa0e4"></a>

### [`007f64ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f64ac.md) → [`007f64ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f64ac.md) FUN_007f64ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f7288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f7/007f7288.md) · 呼出先 16件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`00800530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00800/00800530.md) [`00800534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00800/00800534.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`007f7288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f7288.md) · 呼出先 16件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00800530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800530.md) [`00800534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800534.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6664",
      "incomplete_value": false,
      "site": "007f6664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6664",
      "incomplete_value": false,
      "site": "007f6664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:880:8"
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
      "definition_site": "007f64e0",
      "incomplete_value": true,
      "site": "007f64e0",
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
      "definition_site": "007f64e0",
      "incomplete_value": true,
      "site": "007f64e0",
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
      "definition_site": "007f64e8",
      "incomplete_value": false,
      "site": "007f64fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f64e8",
      "incomplete_value": false,
      "site": "007f64fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "007f64dc",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f64e8",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f64f0",
      "PARAM",
      [
        "storage",
        "00c003d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f64dc",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f64e8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f64f0",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f64dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f64ac.md#insn-007f64dc) · [`007f64e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f64ac.md#insn-007f64e8) · [`007f64f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f64ac.md#insn-007f64f0)
- 新版 `007f64dc`（命令位置の公開資料なし） · `007f64e8`（命令位置の公開資料なし） · `007f64f0`（命令位置の公開資料なし）

~~~diff
- 007f64dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007f64dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f64dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007f64dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007f64dc bytes 08dd44f9
+ 007f64dc bytes 083d45f9
- 007f64e8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007f64e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f64e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f64e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f64e8 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007f64e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f64e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f64e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f64e8 bytes 21603691
+ 007f64e8 bytes 21203991
- 007f64f0 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 007f64f0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f64f0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f64f0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f64f0 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 007f64f0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f64f0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f64f0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f64f0 bytes 42600f91
+ 007f64f0 bytes 42201291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-739e79ebe71e94c71c26ff0557f44fb4"></a>

### [`007f6804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f6804.md) → [`007f6804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f6804.md) FUN_007f6804

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f7288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f7/007f7288.md) · 呼出先 12件 [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`00800640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00800/00800640.md) [`00800644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00800/00800644.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00883e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883e08.md)
- 新版 呼出元 1件 [`007f7288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f7288.md) · 呼出先 12件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00800640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800640.md) [`00800644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800644.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.52% / 新版 92.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6898",
      "incomplete_value": false,
      "site": "007f6898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6898",
      "incomplete_value": false,
      "site": "007f6898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:900:8"
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
      "definition_site": "007f693c",
      "incomplete_value": false,
      "site": "007f6940",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d30:8"
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
      "definition_site": "007f693c",
      "incomplete_value": false,
      "site": "007f6940",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:c80:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f6844",
      "incomplete_value": true,
      "site": "007f6848",
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
                "const:c24000:8"
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
      "definition_site": "007f6844",
      "incomplete_value": true,
      "site": "007f6848",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:9b8:8"
              ]
            ]
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
      "007f6824",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6830",
      "PARAM",
      [
        "storage",
        "00c003d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6840",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "007f6824",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6830",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6840",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f6804.md#insn-007f6824) · [`007f6830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f6804.md#insn-007f6830) · [`007f6840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f6804.md#insn-007f6840)
- 新版 `007f6824`（命令位置の公開資料なし） · `007f6830`（命令位置の公開資料なし） · `007f6840`（命令位置の公開資料なし）

~~~diff
- 007f6824 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007f6824 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f6824 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f6824 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f6824 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007f6824 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f6824 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f6824 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f6824 bytes 21603691
+ 007f6824 bytes 21203991
- 007f6830 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 007f6830 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f6830 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f6830 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f6830 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 007f6830 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f6830 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f6830 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f6830 bytes 42600f91
+ 007f6830 bytes 42201291
- 007f6840 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007f6840 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f6840 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007f6840 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007f6840 bytes 08dd44f9
+ 007f6840 bytes 083d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-445688046a163df81d23992af1dd294e"></a>

### [`007f6a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f6a14.md) → [`007f6a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f6a14.md) FUN_007f6a14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f7288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f7/007f7288.md) · 呼出先 17件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`007f3f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f3/007f3f40.md) [`00800720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00800/00800720.md) [`00800724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00800/00800724.md)
- 新版 呼出元 1件 [`007f7288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f7288.md) · 呼出先 17件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`007f3f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3f40.md) [`00800720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800720.md) [`00800724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800724.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.94% / 新版 97.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6d90",
      "incomplete_value": false,
      "site": "007f6d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6d90",
      "incomplete_value": false,
      "site": "007f6d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f6a4c",
      "incomplete_value": true,
      "site": "007f6a4c",
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
      "definition_site": "007f6a4c",
      "incomplete_value": true,
      "site": "007f6a4c",
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
      "definition_site": "007f6a54",
      "incomplete_value": false,
      "site": "007f6a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6a54",
      "incomplete_value": false,
      "site": "007f6a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "007f6a48",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f6a54",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6a5c",
      "PARAM",
      [
        "storage",
        "00c003d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f6a48",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f6a54",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6a5c",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f6a14.md#insn-007f6a48) · [`007f6a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f6a14.md#insn-007f6a54) · [`007f6a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f6/007f6a14.md#insn-007f6a5c)
- 新版 `007f6a48`（命令位置の公開資料なし） · `007f6a54`（命令位置の公開資料なし） · `007f6a5c`（命令位置の公開資料なし）

~~~diff
- 007f6a48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007f6a48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f6a48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007f6a48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007f6a48 bytes 08dd44f9
+ 007f6a48 bytes 083d45f9
- 007f6a54 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007f6a54 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f6a54 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f6a54 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f6a54 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007f6a54 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f6a54 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f6a54 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f6a54 bytes 21603691
+ 007f6a54 bytes 21203991
- 007f6a5c ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 007f6a5c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f6a5c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f6a5c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f6a5c ["COPY", "tmp:0:8", ["const:488:8"]]
+ 007f6a5c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f6a5c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f6a5c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f6a5c bytes 42600f91
+ 007f6a5c bytes 42201291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e5e6e9339d5c53f464656fab6ad44ea"></a>

### [`007f8354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8354.md) → [`007f8354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8354.md) FUN_007f8354

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007fa718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fa718.md) · 呼出先 16件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00446190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446190.md) [`00447378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447378.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`007e7970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e7/007e7970.md)
- 新版 呼出元 1件 [`007fa718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fa718.md) · 呼出先 16件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00446190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446190.md) [`00447378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447378.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`007e7970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e7/007e7970.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.40% / 新版 99.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f840c",
      "incomplete_value": true,
      "site": "007f840c",
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
      "definition_site": "007f840c",
      "incomplete_value": true,
      "site": "007f840c",
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
      "definition_site": "007f8414",
      "incomplete_value": false,
      "site": "007f8424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8414",
      "incomplete_value": false,
      "site": "007f8424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f841c",
      "incomplete_value": false,
      "site": "007f8424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f841c",
      "incomplete_value": false,
      "site": "007f8424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f8408",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f8414",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f841c",
      "PARAM",
      [
        "storage",
        "00c003d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f8408",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f8414",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f841c",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8354.md#insn-007f8408) · [`007f8414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8354.md#insn-007f8414) · [`007f841c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8354.md#insn-007f841c)
- 新版 `007f8408`（命令位置の公開資料なし） · `007f8414`（命令位置の公開資料なし） · `007f841c`（命令位置の公開資料なし）

~~~diff
- 007f8408 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007f8408 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f8408 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007f8408 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007f8408 bytes 00dd44f9
+ 007f8408 bytes 003d45f9
- 007f8414 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007f8414 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f8414 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f8414 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f8414 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007f8414 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f8414 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f8414 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f8414 bytes 21603691
+ 007f8414 bytes 21203991
- 007f841c ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 007f841c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f841c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f841c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f841c ["COPY", "tmp:0:8", ["const:488:8"]]
+ 007f841c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f841c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f841c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f841c bytes 42600f91
+ 007f841c bytes 42201291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f6f03dc45539c962020575df8eb829b"></a>

### [`007f8b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8b0c.md) → [`007f8b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8b0c.md) FUN_007f8b0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 20件 [`0044b898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b898.md) [`0044b8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b8a0.md) [`0044b8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b8b0.md) [`0044beb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044beb4.md) [`0044c1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c1dc.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 20件 [`0044b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044b8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a0.md) [`0044b8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8b0.md) [`0044beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.82% / 新版 97.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f8c5c",
      "incomplete_value": true,
      "site": "007f8c70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8c5c",
      "incomplete_value": true,
      "site": "007f8c70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:973:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "007f8c08",
      "incomplete_value": true,
      "site": "007f8c08",
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
      "definition_site": "007f8c08",
      "incomplete_value": true,
      "site": "007f8c08",
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
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f8c10",
      "incomplete_value": false,
      "site": "007f8c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8c10",
      "incomplete_value": false,
      "site": "007f8c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "007f8c04",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f8c10",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f8c18",
      "PARAM",
      [
        "storage",
        "00be8da8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f8c04",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f8c10",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f8c18",
      "PARAM",
      [
        "storage",
        "00be8e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8b0c.md#insn-007f8c04) · [`007f8c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8b0c.md#insn-007f8c10) · [`007f8c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8b0c.md#insn-007f8c18)
- 新版 `007f8c04`（命令位置の公開資料なし） · `007f8c10`（命令位置の公開資料なし） · `007f8c18`（命令位置の公開資料なし）

~~~diff
- 007f8c04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007f8c04 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f8c04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007f8c04 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007f8c04 bytes 00dd44f9
+ 007f8c04 bytes 003d45f9
- 007f8c10 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007f8c10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f8c10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f8c10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f8c10 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007f8c10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f8c10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f8c10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f8c10 bytes 21603691
+ 007f8c10 bytes 21203991
- 007f8c18 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 007f8c18 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f8c18 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f8c18 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f8c18 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 007f8c18 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f8c18 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f8c18 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f8c18 bytes 42a03691
+ 007f8c18 bytes 42603991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8381f59e32294cbf6c6c01474de27c4"></a>

### [`007f8ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8ecc.md) → [`007f8ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8ecc.md) FUN_007f8ecc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007f8b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8b0c.md) [`00adcbcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adc/00adcbcc.md) · 呼出先 17件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`0044ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044ba98.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md)
- 新版 呼出元 2件 [`007f8b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8b0c.md) [`00adcc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adcc94.md) · 呼出先 17件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.51% / 新版 86.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_destination` 7件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f8f28",
      "incomplete_value": true,
      "site": "007f8f40",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:8d7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8f28",
      "incomplete_value": true,
      "site": "007f8f40",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:84a:8"
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
      "definition_site": "007f8f48",
      "incomplete_value": true,
      "site": "007f8f58",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:7c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8f48",
      "incomplete_value": true,
      "site": "007f8f58",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:733:8"
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
      "definition_site": "007f904c",
      "incomplete_value": true,
      "site": "007f904c",
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
                "const:a7b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f904c",
      "incomplete_value": true,
      "site": "007f904c",
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
                "const:a75:8"
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
      "007f8f0c",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "007f8f28",
      "READ",
      [
        "storage",
        "0029b84a",
        null,
        "string"
      ]
    ],
    [
      "007f8f48",
      "READ",
      [
        "storage",
        "0029d733",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f8f0c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "007f8f28",
      "READ",
      [
        "storage",
        "0029b8d7",
        null,
        "string"
      ]
    ],
    [
      "007f8f48",
      "READ",
      [
        "storage",
        "0029d7c0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8ecc.md#insn-007f8f00) · [`007f8f04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8ecc.md#insn-007f8f04) · [`007f8f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f8/007f8ecc.md#insn-007f8f20)
- 新版 `007f8f00`（命令位置の公開資料なし） · `007f8f04`（命令位置の公開資料なし） · `007f8f20`（命令位置の公開資料なし）

~~~diff
- 007f8f00 ["COPY", "register:40c8:8", ["const:c24000:8"]]
+ 007f8f00 ["COPY", "register:40c8:8", ["const:c25000:8"]]
- 007f8f00 bytes 79210090
+ 007f8f00 bytes 792100b0
- 007f8f04 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 007f8f04 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 007f8f04 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 007f8f04 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 007f8f04 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 007f8f04 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 007f8f04 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 007f8f04 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 007f8f04 bytes 39e33d91
+ 007f8f04 bytes 39e30091
- 007f8f20 ["COPY", "tmp:0:8", ["const:84a:8"]]
- 007f8f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8f20 ["COPY", "tmp:0:8", ["const:8d7:8"]]
+ 007f8f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8f20 bytes 08292191
+ 007f8f20 bytes 085d2391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03205f6f0aef511843c148e5fdedf607"></a>

### [`007f95f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f95f4.md) → [`007f95f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f95f4.md) FUN_007f95f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044c80c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c80c.md) [`0044d1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d1dc.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044c80c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c80c.md) [`0044d1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d1dc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f9640",
      "incomplete_value": true,
      "site": "007f9644",
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
                "const:c24000:8"
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
      "definition_site": "007f9640",
      "incomplete_value": true,
      "site": "007f9644",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:9b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f962c",
      "incomplete_value": false,
      "site": "007f9644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f962c",
      "incomplete_value": false,
      "site": "007f9644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f9638",
      "incomplete_value": false,
      "site": "007f9644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9638",
      "incomplete_value": false,
      "site": "007f9644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:da8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f962c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f9630",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f9638",
      "PARAM",
      [
        "storage",
        "00be8da8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f962c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f9630",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f9638",
      "PARAM",
      [
        "storage",
        "00be8e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f962c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f95f4.md#insn-007f962c) · [`007f9630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f95f4.md#insn-007f9630) · [`007f9638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f95f4.md#insn-007f9638)
- 新版 `007f962c`（命令位置の公開資料なし） · `007f9630`（命令位置の公開資料なし） · `007f9638`（命令位置の公開資料なし）

~~~diff
- 007f962c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007f962c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f962c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f962c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f962c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007f962c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f962c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f962c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f962c bytes 21603691
+ 007f962c bytes 21203991
- 007f9630 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007f9630 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f9630 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007f9630 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007f9630 bytes 08dd44f9
+ 007f9630 bytes 083d45f9
- 007f9638 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 007f9638 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f9638 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f9638 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f9638 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 007f9638 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f9638 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f9638 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f9638 bytes 42a03691
+ 007f9638 bytes 42603991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16ab7a675e22d95221552815d0a0dc9f"></a>

### [`007f99cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f99cc.md) → [`007f99cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f99cc.md) FUN_007f99cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 23件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`007f7288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f7/007f7288.md) [`00805f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00805/00805f2c.md) [`008070c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00807/008070c0.md) [`008070c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00807/008070c4.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 23件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`007f7288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f7288.md) [`00805f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00805/00805f2c.md) [`008070c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008070c0.md) [`008070c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008070c4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 89.94% / 新版 89.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007f9a08",
      "incomplete_value": false,
      "site": "007f9a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9a08",
      "incomplete_value": false,
      "site": "007f9a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f9a00",
      "incomplete_value": true,
      "site": "007f9a08",
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
                "const:c24000:8"
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
      "definition_site": "007f9a00",
      "incomplete_value": true,
      "site": "007f9a08",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:9b8:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007f9a0c",
      "incomplete_value": false,
      "site": "007f9a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9a0c",
      "incomplete_value": false,
      "site": "007f9a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f9a00",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f9a04",
      "READ",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f9a08",
      "WRITE",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "007f9a00",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f9a04",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "007f9a08",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f9a08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f99cc.md#insn-007f9a08) · [`007f9a0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f99cc.md#insn-007f9a0c) · [`007f9a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f99cc.md#insn-007f9a24)
- 新版 `007f9a08`（命令位置の公開資料なし） · `007f9a0c`（命令位置の公開資料なし） · `007f9a24`（命令位置の公開資料なし）

~~~diff
- 007f9a08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 007f9a08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 007f9a08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 007f9a08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 007f9a08 bytes 09d504f9
+ 007f9a08 bytes 093505f9
- 007f9a0c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:9b8:8"]]
- 007f9a0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 007f9a0c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 007f9a0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 007f9a0c bytes cade04f9
+ 007f9a0c bytes ca3e05f9
- 007f9a24 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:9b8:8"]]
- 007f9a24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 007f9a24 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 007f9a24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 007f9a24 bytes d4de04f9
+ 007f9a24 bytes d43e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14091ae40204076d07a65f6604cec25f"></a>

### [`007f9cd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f9cd4.md) → [`007f9cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f9cd4.md) FUN_007f9cd4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004296cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004296cc.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0046ad74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046ad74.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004296cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004296cc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ad74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046ad74.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.41% / 新版 97.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f9d7c",
      "incomplete_value": true,
      "site": "007f9d7c",
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
                "const:8be:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9d7c",
      "incomplete_value": true,
      "site": "007f9d7c",
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
                "const:952:8"
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
      "definition_site": "007f9e08",
      "incomplete_value": true,
      "site": "007f9e08",
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
                "const:4a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9e08",
      "incomplete_value": true,
      "site": "007f9e08",
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
                "const:4a1:8"
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
      "definition_site": "007f9f64",
      "incomplete_value": true,
      "site": "007f9f64",
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
                "const:8be:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9f64",
      "incomplete_value": true,
      "site": "007f9f64",
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
                "const:952:8"
              ]
            ]
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
      "007f9d68",
      "READ",
      [
        "storage",
        "002a7952",
        null,
        "string"
      ]
    ],
    [
      "007f9df8",
      "READ",
      [
        "storage",
        "002aa4a1",
        null,
        "string"
      ]
    ],
    [
      "007f9f50",
      "READ",
      [
        "storage",
        "002a7952",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f9d68",
      "READ",
      [
        "storage",
        "002a78be",
        null,
        "string"
      ]
    ],
    [
      "007f9df8",
      "READ",
      [
        "storage",
        "002aa4a7",
        null,
        "string"
      ]
    ],
    [
      "007f9f50",
      "READ",
      [
        "storage",
        "002a78be",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f9d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f9cd4.md#insn-007f9d60) · [`007f9df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f9cd4.md#insn-007f9df0) · [`007f9f4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f9cd4.md#insn-007f9f4c)
- 新版 `007f9d60`（命令位置の公開資料なし） · `007f9df0`（命令位置の公開資料なし） · `007f9f4c`（命令位置の公開資料なし）

~~~diff
- 007f9d60 ["COPY", "tmp:0:8", ["const:952:8"]]
- 007f9d60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f9d60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f9d60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f9d60 ["COPY", "tmp:0:8", ["const:8be:8"]]
+ 007f9d60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9d60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9d60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f9d60 bytes 08492591
+ 007f9d60 bytes 08f92291
- 007f9df0 ["COPY", "tmp:0:8", ["const:4a1:8"]]
- 007f9df0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f9df0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f9df0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f9df0 ["COPY", "tmp:0:8", ["const:4a7:8"]]
+ 007f9df0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f9df0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f9df0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f9df0 bytes 29851291
+ 007f9df0 bytes 299d1291
- 007f9f4c ["COPY", "tmp:0:8", ["const:952:8"]]
- 007f9f4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f9f4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f9f4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f9f4c ["COPY", "tmp:0:8", ["const:8be:8"]]
+ 007f9f4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f9f4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f9f4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f9f4c bytes 29492591
+ 007f9f4c bytes 29f92291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52d3ed95e0725b0119bf6150ed56e441"></a>

### [`007fa718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fa718.md) → [`007fa718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fa718.md) FUN_007fa718

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 22件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 22件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.44% / 新版 98.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007fa734",
      "incomplete_value": true,
      "site": "007fa734",
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
      "definition_site": "007fa734",
      "incomplete_value": true,
      "site": "007fa734",
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
      "definition_site": "007fa74c",
      "incomplete_value": true,
      "site": "007fa758",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fa74c",
      "incomplete_value": true,
      "site": "007fa758",
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
            "const:3d8:8"
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
      "007fa730",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007fa744",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007fa74c",
      "PARAM",
      [
        "storage",
        "00c003d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007fa730",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007fa744",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007fa74c",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fa730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fa718.md#insn-007fa730) · [`007fa744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fa718.md#insn-007fa744) · [`007fa74c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fa718.md#insn-007fa74c)
- 新版 `007fa730`（命令位置の公開資料なし） · `007fa744`（命令位置の公開資料なし） · `007fa74c`（命令位置の公開資料なし）

~~~diff
- 007fa730 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007fa730 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007fa730 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007fa730 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007fa730 bytes 08dd44f9
+ 007fa730 bytes 083d45f9
- 007fa744 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007fa744 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007fa744 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007fa744 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007fa744 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007fa744 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007fa744 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007fa744 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007fa744 bytes 21603691
+ 007fa744 bytes 21203991
- 007fa74c ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 007fa74c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007fa74c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007fa74c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007fa74c ["COPY", "tmp:0:8", ["const:488:8"]]
+ 007fa74c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007fa74c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007fa74c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007fa74c bytes 42600f91
+ 007fa74c bytes 42201291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91240b4b0f60abb1849ee803f14cbdfd"></a>

### [`007fabf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fabf8.md) → [`007fabf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fabf8.md) FUN_007fabf8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`007e5fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e5/007e5fa4.md) [`007e7bcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e7/007e7bcc.md) [`007eb8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007eb/007eb8f8.md) [`007fa918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fa918.md) [`007fb248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fb/007fb248.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 5件 [`007e5fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5fa4.md) [`007e7bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e7/007e7bcc.md) [`007eb8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007eb8f8.md) [`007fa918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fa918.md) [`007fb248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fb/007fb248.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007fac04",
      "incomplete_value": false,
      "site": "007fac08",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fac04",
      "incomplete_value": false,
      "site": "007fac08",
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
            "const:30a:8"
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
      "007fac04",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007fac04",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fac04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fabf8.md#insn-007fac04)
- 新版 `007fac04`（命令位置の公開資料なし）

~~~diff
- 007fac04 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007fac04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007fac04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007fac04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007fac04 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007fac04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007fac04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007fac04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007fac04 bytes 00280c91
+ 007fac04 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea5e823a39f4bb193e3dc6e4943bd018"></a>

### [`007fae20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fae20.md) → [`007fae20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fae20.md) FUN_007fae20

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`007e555c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e5/007e555c.md) [`007e7d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e7/007e7d84.md) [`007f3c28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f3/007f3c28.md) [`007f4120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f4/007f4120.md) [`007fac0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fac0c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 5件 [`007e555c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e555c.md) [`007e7d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e7/007e7d84.md) [`007f3c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3c28.md) [`007f4120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f4/007f4120.md) [`007fac0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fac0c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007fae2c",
      "incomplete_value": false,
      "site": "007fae30",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fae2c",
      "incomplete_value": false,
      "site": "007fae30",
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
            "const:30a:8"
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
      "007fae2c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007fae2c",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fae2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fae20.md#insn-007fae2c)
- 新版 `007fae2c`（命令位置の公開資料なし）

~~~diff
- 007fae2c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007fae2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007fae2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007fae2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007fae2c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007fae2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007fae2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007fae2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007fae2c bytes 00280c91
+ 007fae2c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f325a1f966d31721066f6c3fc4b1de8"></a>

### [`007faea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007faea4.md) → [`007faea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007faea4.md) FUN_007faea4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "007faea8",
      "incomplete_value": false,
      "site": "007faeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007faea8",
      "incomplete_value": false,
      "site": "007faeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "007faeac",
      "DATA",
      [
        "storage",
        "00c002f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007faeac",
      "DATA",
      [
        "storage",
        "00c003a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007faea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007faea4.md#insn-007faea8)
- 新版 `007faea8`（命令位置の公開資料なし）

~~~diff
- 007faea8 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 007faea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007faea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007faea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007faea8 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 007faea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007faea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007faea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007faea8 bytes 08e10b91
+ 007faea8 bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c88c26139a0fd5a0081892573613e043"></a>

### [`007faeb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007faeb4.md) → [`007faeb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007faeb4.md) FUN_007faeb4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "007faec4",
      "incomplete_value": false,
      "site": "007faecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007faec4",
      "incomplete_value": false,
      "site": "007faecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "007faecc",
      "DATA",
      [
        "storage",
        "00c002f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007faecc",
      "DATA",
      [
        "storage",
        "00c003a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007faec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007faeb4.md#insn-007faec4)
- 新版 `007faec4`（命令位置の公開資料なし）

~~~diff
- 007faec4 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 007faec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007faec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007faec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007faec4 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 007faec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007faec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007faec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007faec4 bytes 08e10b91
+ 007faec4 bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d6de8d53b3443c5b79ee8d8ef3470d1"></a>

### [`007fafac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fafac.md) → [`007fafac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fafac.md) FUN_007fafac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "007fafb0",
      "incomplete_value": false,
      "site": "007fafb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fafb0",
      "incomplete_value": false,
      "site": "007fafb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "007fafb4",
      "DATA",
      [
        "storage",
        "00c00348",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007fafb4",
      "DATA",
      [
        "storage",
        "00c003f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fafb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fafac.md#insn-007fafb0)
- 新版 `007fafb0`（命令位置の公開資料なし）

~~~diff
- 007fafb0 ["COPY", "tmp:0:8", ["const:348:8"]]
- 007fafb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fafb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fafb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fafb0 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 007fafb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fafb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fafb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fafb0 bytes 08210d91
+ 007fafb0 bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee235280c04c452342fa4f1b498bd1b3"></a>

### [`007fb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fb/007fb170.md) → [`007fb170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fb/007fb170.md) FUN_007fb170

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "007fb174",
      "incomplete_value": false,
      "site": "007fb178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fb174",
      "incomplete_value": false,
      "site": "007fb178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
      "007fb178",
      "DATA",
      [
        "storage",
        "00c00398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fb178",
      "DATA",
      [
        "storage",
        "00c00448",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fb174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fb/007fb170.md#insn-007fb174)
- 新版 `007fb174`（命令位置の公開資料なし）

~~~diff
- 007fb174 ["COPY", "tmp:0:8", ["const:398:8"]]
- 007fb174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fb174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fb174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fb174 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 007fb174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fb174 bytes 08610e91
+ 007fb174 bytes 08211191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ead5463060787dcd11c930ed7dbd84f6"></a>

### [`007fb180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fb/007fb180.md) → [`007fb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fb/007fb180.md) FUN_007fb180

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "007fb190",
      "incomplete_value": false,
      "site": "007fb198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fb190",
      "incomplete_value": false,
      "site": "007fb198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
      "007fb198",
      "DATA",
      [
        "storage",
        "00c00398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fb198",
      "DATA",
      [
        "storage",
        "00c00448",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fb/007fb180.md#insn-007fb190)
- 新版 `007fb190`（命令位置の公開資料なし）

~~~diff
- 007fb190 ["COPY", "tmp:0:8", ["const:398:8"]]
- 007fb190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fb190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fb190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fb190 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 007fb190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fb190 bytes 08610e91
+ 007fb190 bytes 08211191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

