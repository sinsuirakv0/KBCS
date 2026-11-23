# v15.7.2 → v15.7.3 · 最優先の変更候補 (20)

[一覧の目次](README.md)

<a id="compare-1d9f2510a67d55d91a693d7ed0403edc"></a>

### [`0057abd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057abd4.md) → [`0057abd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057abd4.md) FUN_0057abd4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057abf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057abf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057abf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0057abf8",
      "DATA",
      [
        "storage",
        "00bf0c88",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ac08",
      "DATA",
      [
        "storage",
        "00bf0bd8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057abf8",
      "DATA",
      [
        "storage",
        "00bf0d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ac08",
      "DATA",
      [
        "storage",
        "00bf0c88",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057abf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057abd4.md#insn-0057abf4) · [`0057abf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057abd4.md#insn-0057abf8)
- 新版 `0057abf4`（命令位置の公開資料なし）

~~~diff
- 0057abf4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0057abf4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0057abf4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0057abf4 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0057abf4 bytes 1ffc00a9
+ 0057abf4 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 0057abf4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 0057abf4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 0057abf4 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 0057abf4 bytes 1ffc00a9
- 0057abf8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0057abf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0057abf8 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef4adaf430bb3c3b13de25c22535e67c"></a>

### [`0057ac1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ac1c.md) → [`0057ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ac1c.md) FUN_0057ac1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057ac48",
      "incomplete_value": false,
      "site": "0057ac4c",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0057ac48",
      "incomplete_value": false,
      "site": "0057ac4c",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "0057ac4c",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ac4c",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ac40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ac1c.md#insn-0057ac40)
- 新版 `0057ac40`（命令位置の公開資料なし）

~~~diff
- 0057ac40 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0057ac40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ac40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ac40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ac40 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0057ac40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ac40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ac40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ac40 bytes 08412591
+ 0057ac40 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a29d57465e9e502b82e4af48178434c"></a>

### [`0057ac80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ac80.md) → [`0057ac80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ac80.md) FUN_0057ac80

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
      "definition_site": "0057acac",
      "incomplete_value": false,
      "site": "0057acb0",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0057acac",
      "incomplete_value": false,
      "site": "0057acb0",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "0057acb0",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057acb0",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057aca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ac80.md#insn-0057aca4)
- 新版 `0057aca4`（命令位置の公開資料なし）

~~~diff
- 0057aca4 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0057aca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057aca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057aca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057aca4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0057aca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057aca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057aca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057aca4 bytes 08412591
+ 0057aca4 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae114e7a682f60f77cbf983c9d4bea39"></a>

### [`0057ace0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ace0.md) → [`0057ace0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ace0.md) FUN_0057ace0

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
      "definition_site": "0057ace8",
      "incomplete_value": false,
      "site": "0057acec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ace8",
      "incomplete_value": false,
      "site": "0057acec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057acec",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057acec",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ace8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ace0.md#insn-0057ace8)
- 新版 `0057ace8`（命令位置の公開資料なし）

~~~diff
- 0057ace8 ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057ace8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057ace8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057ace8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057ace8 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057ace8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ace8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ace8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057ace8 bytes 29012591
+ 0057ace8 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-768f3ba8fb2f5d1d2ebc7ebb8909737c"></a>

### [`0057ad20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ad20.md) → [`0057ad20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ad20.md) FUN_0057ad20

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
      "definition_site": "0057ad24",
      "incomplete_value": false,
      "site": "0057ad28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ad24",
      "incomplete_value": false,
      "site": "0057ad28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "0057ad28",
      "DATA",
      [
        "storage",
        "00bf0c38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ad28",
      "DATA",
      [
        "storage",
        "00bf0ce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ad24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ad20.md#insn-0057ad24)
- 新版 `0057ad24`（命令位置の公開資料なし）

~~~diff
- 0057ad24 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 0057ad24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ad24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ad24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ad24 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 0057ad24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ad24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ad24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ad24 bytes 08e13091
+ 0057ad24 bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d58d18317afd335935f61c4ee39421ec"></a>

### [`0057ad60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ad60.md) → [`0057ad60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ad60.md) FUN_0057ad60

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
      "definition_site": "0057ad68",
      "incomplete_value": false,
      "site": "0057ad6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ad68",
      "incomplete_value": false,
      "site": "0057ad6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057ad6c",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057ad6c",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ad68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ad60.md#insn-0057ad68)
- 新版 `0057ad68`（命令位置の公開資料なし）

~~~diff
- 0057ad68 ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057ad68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057ad68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057ad68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057ad68 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057ad68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ad68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ad68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057ad68 bytes 29012591
+ 0057ad68 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f52f5c0fcdef77a580288abd9af8ca15"></a>

### [`0057ad84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ad84.md) → [`0057ad84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ad84.md) FUN_0057ad84

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
      "definition_site": "0057ad88",
      "incomplete_value": false,
      "site": "0057ad8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ad88",
      "incomplete_value": false,
      "site": "0057ad8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "0057ad8c",
      "DATA",
      [
        "storage",
        "00bf0c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ad8c",
      "DATA",
      [
        "storage",
        "00bf0d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ad88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ad84.md#insn-0057ad88)
- 新版 `0057ad88`（命令位置の公開資料なし）

~~~diff
- 0057ad88 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 0057ad88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ad88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ad88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ad88 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 0057ad88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ad88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ad88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ad88 bytes 08213291
+ 0057ad88 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffd09bf118cd4cf1842b180b7228ddc3"></a>

### [`0057ad94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ad94.md) → [`0057ad94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ad94.md) FUN_0057ad94

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
      "definition_site": "0057ada4",
      "incomplete_value": false,
      "site": "0057adac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ada4",
      "incomplete_value": false,
      "site": "0057adac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "0057adac",
      "DATA",
      [
        "storage",
        "00bf0c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057adac",
      "DATA",
      [
        "storage",
        "00bf0d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ada4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057ad94.md#insn-0057ada4)
- 新版 `0057ada4`（命令位置の公開資料なし）

~~~diff
- 0057ada4 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 0057ada4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ada4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ada4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ada4 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 0057ada4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ada4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ada4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ada4 bytes 08213291
+ 0057ada4 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-262abe8c018521407f812dc44e5d856f"></a>

### [`0057adcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057adcc.md) → [`0057adcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057adcc.md) _INIT_39

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
      "definition_site": "0057ae08",
      "incomplete_value": true,
      "site": "0057ae24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057ae08",
      "incomplete_value": true,
      "site": "0057ae24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057ae2c",
      "incomplete_value": true,
      "site": "0057ae48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057ae2c",
      "incomplete_value": true,
      "site": "0057ae48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057ae4c",
      "incomplete_value": true,
      "site": "0057ae68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057ae4c",
      "incomplete_value": true,
      "site": "0057ae68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057ae08",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0057ae2c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0057ae4c",
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
      "0057ae08",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057ae2c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057ae4c",
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

- 旧版 [`0057adf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057adcc.md#insn-0057adf8) · [`0057ae00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057adcc.md#insn-0057ae00)
- 新版 `0057adf8`（命令位置の公開資料なし） · `0057ae00`（命令位置の公開資料なし）

~~~diff
- 0057adf8 ["COPY", "tmp:0:8", ["const:670:8"]]
- 0057adf8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057adf8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057adf8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057adf8 ["COPY", "tmp:0:8", ["const:730:8"]]
+ 0057adf8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057adf8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057adf8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057adf8 bytes 73c21991
+ 0057adf8 bytes 73c21c91
- 0057ae00 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057ae00 bytes 69e9ffb0
+ 0057ae00 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057ae00 bytes 69e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c42cb15ef4f383a4d815fa64724a8638"></a>

### [`0057b184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b184.md) → [`0057b184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b184.md) FUN_0057b184

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0057b864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b864.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0057b864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b864.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.88% / 新版 98.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b1dc",
      "incomplete_value": true,
      "site": "0057b1dc",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b1dc",
      "incomplete_value": true,
      "site": "0057b1dc",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5e1:8"
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
      "0057b1c0",
      "READ",
      [
        "storage",
        "002a65e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057b1c0",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b184.md#insn-0057b1b0)
- 新版 `0057b1b0`（命令位置の公開資料なし）

~~~diff
- 0057b1b0 ["COPY", "tmp:0:8", ["const:5e1:8"]]
- 0057b1b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057b1b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057b1b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057b1b0 ["COPY", "tmp:0:8", ["const:5da:8"]]
+ 0057b1b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057b1b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057b1b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057b1b0 bytes 4a851791
+ 0057b1b0 bytes 4a691791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2ab9f775084869e63f68fdfac41b265"></a>

### [`0057b6a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b6a4.md) → [`0057b6a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b6a4.md) FUN_0057b6a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0057b6c0",
      "incomplete_value": false,
      "site": "0057b6c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b6c0",
      "incomplete_value": false,
      "site": "0057b6c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "0057b6d8",
      "incomplete_value": false,
      "site": "0057b6d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b6d8",
      "incomplete_value": false,
      "site": "0057b6d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "0057b6c8",
      "DATA",
      [
        "storage",
        "00bf0e00",
        null,
        "undefined *"
      ]
    ],
    [
      "0057b6d8",
      "DATA",
      [
        "storage",
        "00bf0cf8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057b6c8",
      "DATA",
      [
        "storage",
        "00bf0eb0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057b6d8",
      "DATA",
      [
        "storage",
        "00bf0da8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b6a4.md#insn-0057b6c0) · [`0057b6cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b6a4.md#insn-0057b6cc)
- 新版 `0057b6c0`（命令位置の公開資料なし） · `0057b6cc`（命令位置の公開資料なし）

~~~diff
- 0057b6c0 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 0057b6c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b6c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b6c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b6c0 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0057b6c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b6c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b6c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b6c0 bytes 08013891
+ 0057b6c0 bytes 08c13a91
- 0057b6cc ["COPY", "register:4040:8", ["const:bf0000:8"]]
- 0057b6cc bytes a83300b0
+ 0057b6cc ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0057b6cc bytes a83300b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13a37a0f122e6d53149c94f7dc195e3a"></a>

### [`0057b6ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b6ec.md) → [`0057b6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b6ec.md) FUN_0057b6ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057b708",
      "incomplete_value": true,
      "site": "0057b70c",
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
      "definition_site": "0057b708",
      "incomplete_value": true,
      "site": "0057b70c",
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
      "0057b700",
      "READ",
      [
        "storage",
        "00c1b430",
        null,
        "pointer"
      ]
    ],
    [
      "0057b70c",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057b700",
      "READ",
      [
        "storage",
        "00c1b4e0",
        null,
        "pointer"
      ]
    ],
    [
      "0057b70c",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b6ec.md#insn-0057b700)
- 新版 `0057b700`（命令位置の公開資料なし）

~~~diff
- 0057b700 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:430:8"]]
- 0057b700 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0057b700 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
+ 0057b700 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0057b700 bytes 081942f9
+ 0057b700 bytes 087142f9
~~~


<a id="compare-eb96c24568a3013844565407f3c6b3b7"></a>

### [`0057b73c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b73c.md) → [`0057b73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b73c.md) FUN_0057b73c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057b7a4",
      "incomplete_value": false,
      "site": "0057b7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b7a4",
      "incomplete_value": false,
      "site": "0057b7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "0057b7a8",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057b7a8",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b7a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b73c.md#insn-0057b7a4)
- 新版 `0057b7a4`（命令位置の公開資料なし）

~~~diff
- 0057b7a4 ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057b7a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057b7a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057b7a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057b7a4 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057b7a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b7a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b7a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057b7a4 bytes 29012591
+ 0057b7a4 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58775eff759b9cea443c6779451631e5"></a>

### [`0057b7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b7d4.md) → [`0057b7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b7d4.md) FUN_0057b7d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057b83c",
      "incomplete_value": false,
      "site": "0057b840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b83c",
      "incomplete_value": false,
      "site": "0057b840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "0057b840",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057b840",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b7d4.md#insn-0057b83c)
- 新版 `0057b83c`（命令位置の公開資料なし）

~~~diff
- 0057b83c ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057b83c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057b83c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057b83c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057b83c ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057b83c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b83c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b83c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057b83c bytes 29012591
+ 0057b83c bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8530f416b5dc577e8a8bac6c122a1cc8"></a>

### [`0057b864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b864.md) → [`0057b864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b864.md) FUN_0057b864

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0057b184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b184.md) · 呼出先 4件 [`0051d884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d884.md) [`00578fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578fc4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`0057b184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b184.md) · 呼出先 4件 [`0051d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d884.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b8d0",
      "incomplete_value": false,
      "site": "0057b8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b8d0",
      "incomplete_value": false,
      "site": "0057b8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "definition_site": "0057b8f8",
      "incomplete_value": true,
      "site": "0057b900",
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
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b8f8",
      "incomplete_value": true,
      "site": "0057b900",
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
            "const:cd8:8"
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
      "0057b8d4",
      "DATA",
      [
        "storage",
        "00bf0db0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057b900",
      "DATA",
      [
        "storage",
        "00bf0cd8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057b8d4",
      "DATA",
      [
        "storage",
        "00bf0e60",
        null,
        "undefined *"
      ]
    ],
    [
      "0057b900",
      "DATA",
      [
        "storage",
        "00bf0d88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b864.md#insn-0057b8d0) · [`0057b8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b864.md#insn-0057b8f8)
- 新版 `0057b8d0`（命令位置の公開資料なし） · `0057b8f8`（命令位置の公開資料なし）

~~~diff
- 0057b8d0 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0057b8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b8d0 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 0057b8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b8d0 bytes 08c13691
+ 0057b8d0 bytes 08813991
- 0057b8f8 ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 0057b8f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b8f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b8f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b8f8 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0057b8f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b8f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b8f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b8f8 bytes 08613391
+ 0057b8f8 bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6195af1644d5d731bfe2ae644eac3a97"></a>

### [`0057b97c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b97c.md) → [`0057b97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b97c.md) FUN_0057b97c

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
      "definition_site": "0057b980",
      "incomplete_value": false,
      "site": "0057b984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b980",
      "incomplete_value": false,
      "site": "0057b984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "0057b984",
      "DATA",
      [
        "storage",
        "00bf0db0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057b984",
      "DATA",
      [
        "storage",
        "00bf0e60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b97c.md#insn-0057b980)
- 新版 `0057b980`（命令位置の公開資料なし）

~~~diff
- 0057b980 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0057b980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b980 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 0057b980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b980 bytes 08c13691
+ 0057b980 bytes 08813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb6b03c1eeae615622da30e88d78c8bf"></a>

### [`0057b98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b98c.md) → [`0057b98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b98c.md) FUN_0057b98c

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
      "definition_site": "0057b99c",
      "incomplete_value": false,
      "site": "0057b9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b99c",
      "incomplete_value": false,
      "site": "0057b9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "0057b9a4",
      "DATA",
      [
        "storage",
        "00bf0db0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057b9a4",
      "DATA",
      [
        "storage",
        "00bf0e60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b99c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b98c.md#insn-0057b99c)
- 新版 `0057b99c`（命令位置の公開資料なし）

~~~diff
- 0057b99c ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0057b99c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b99c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b99c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b99c ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 0057b99c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b99c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b99c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b99c bytes 08c13691
+ 0057b99c bytes 08813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-195c8e24d0925c08c6b736f86d9a66ce"></a>

### [`0057b9bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b9bc.md) → [`0057b9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b9bc.md) FUN_0057b9bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057ba24",
      "incomplete_value": false,
      "site": "0057ba28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ba24",
      "incomplete_value": false,
      "site": "0057ba28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "0057ba28",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057ba28",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ba24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057b9bc.md#insn-0057ba24)
- 新版 `0057ba24`（命令位置の公開資料なし）

~~~diff
- 0057ba24 ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057ba24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057ba24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057ba24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057ba24 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057ba24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ba24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ba24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057ba24 bytes 29012591
+ 0057ba24 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c98235b8d92a1b1d9f21387c8e35303"></a>

### [`0057ba58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057ba58.md) → [`0057ba58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057ba58.md) FUN_0057ba58

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
      "definition_site": "0057ba5c",
      "incomplete_value": false,
      "site": "0057ba60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ba5c",
      "incomplete_value": false,
      "site": "0057ba60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "0057ba60",
      "DATA",
      [
        "storage",
        "00bf0e00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ba60",
      "DATA",
      [
        "storage",
        "00bf0eb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ba5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057ba58.md#insn-0057ba5c)
- 新版 `0057ba5c`（命令位置の公開資料なし）

~~~diff
- 0057ba5c ["COPY", "tmp:0:8", ["const:e00:8"]]
- 0057ba5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ba5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ba5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ba5c ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0057ba5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ba5c bytes 08013891
+ 0057ba5c bytes 08c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0e2b6891401893bbbb3d15d29b01bee"></a>

### [`0057ba68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057ba68.md) → [`0057ba68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057ba68.md) FUN_0057ba68

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
      "definition_site": "0057ba78",
      "incomplete_value": false,
      "site": "0057ba80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ba78",
      "incomplete_value": false,
      "site": "0057ba80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "0057ba80",
      "DATA",
      [
        "storage",
        "00bf0e00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ba80",
      "DATA",
      [
        "storage",
        "00bf0eb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ba78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057ba68.md#insn-0057ba78)
- 新版 `0057ba78`（命令位置の公開資料なし）

~~~diff
- 0057ba78 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 0057ba78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ba78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ba78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ba78 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0057ba78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ba78 bytes 08013891
+ 0057ba78 bytes 08c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48a99012f067f69f56f70fa302c42d71"></a>

### [`0057baa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057baa0.md) → [`0057baa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057baa0.md) _INIT_40

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057badc",
      "incomplete_value": true,
      "site": "0057baf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057badc",
      "incomplete_value": true,
      "site": "0057baf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057bb00",
      "incomplete_value": true,
      "site": "0057bb1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057bb00",
      "incomplete_value": true,
      "site": "0057bb1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057bb20",
      "incomplete_value": true,
      "site": "0057bb3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057bb20",
      "incomplete_value": true,
      "site": "0057bb3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057badc",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0057bb00",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0057bb20",
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
      "0057badc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057bb00",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057bb20",
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

- 旧版 [`0057bacc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057baa0.md#insn-0057bacc) · [`0057bad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057baa0.md#insn-0057bad4)
- 新版 `0057bacc`（命令位置の公開資料なし） · `0057bad4`（命令位置の公開資料なし）

~~~diff
- 0057bacc ["COPY", "tmp:0:8", ["const:688:8"]]
- 0057bacc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057bacc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057bacc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057bacc ["COPY", "tmp:0:8", ["const:748:8"]]
+ 0057bacc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057bacc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057bacc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057bacc bytes 73221a91
+ 0057bacc bytes 73221d91
- 0057bad4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057bad4 bytes 69e9ff90
+ 0057bad4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057bad4 bytes 69e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa51acd26ea5fb4dd74a5ef96cae0eff"></a>

### [`0057be30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057be30.md) → [`0057be30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057be30.md) FUN_0057be30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578fc4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.58% / 新版 95.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057be84",
      "incomplete_value": true,
      "site": "0057be84",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057be84",
      "incomplete_value": true,
      "site": "0057be84",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5e1:8"
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
      "definition_site": "0057c094",
      "incomplete_value": true,
      "site": "0057c094",
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
                "const:69d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c094",
      "incomplete_value": true,
      "site": "0057c094",
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
                "const:610:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057c11c",
      "incomplete_value": false,
      "site": "0057c128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c11c",
      "incomplete_value": false,
      "site": "0057c128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "0057be68",
      "READ",
      [
        "storage",
        "002a65e1",
        null,
        "string"
      ]
    ],
    [
      "0057c080",
      "READ",
      [
        "storage",
        "0029f610",
        null,
        "string"
      ]
    ],
    [
      "0057c128",
      "DATA",
      [
        "storage",
        "00bf0f28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057be68",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0057c080",
      "READ",
      [
        "storage",
        "0029f69d",
        null,
        "string"
      ]
    ],
    [
      "0057c128",
      "DATA",
      [
        "storage",
        "00bf0fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057be5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057be30.md#insn-0057be5c) · [`0057c078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057be30.md#insn-0057c078) · [`0057c11c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057b/0057be30.md#insn-0057c11c)
- 新版 `0057be5c`（命令位置の公開資料なし） · `0057c078`（命令位置の公開資料なし） · `0057c11c`（命令位置の公開資料なし）

~~~diff
- 0057be5c ["COPY", "tmp:0:8", ["const:5e1:8"]]
- 0057be5c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057be5c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057be5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057be5c ["COPY", "tmp:0:8", ["const:5da:8"]]
+ 0057be5c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057be5c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057be5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057be5c bytes 4a851791
+ 0057be5c bytes 4a691791
- 0057c078 ["COPY", "tmp:0:8", ["const:610:8"]]
- 0057c078 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057c078 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057c078 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057c078 ["COPY", "tmp:0:8", ["const:69d:8"]]
+ 0057c078 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c078 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c078 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057c078 bytes 29411891
+ 0057c078 bytes 29751a91
- 0057c11c ["COPY", "tmp:0:8", ["const:f28:8"]]
- 0057c11c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c11c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c11c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c11c ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 0057c11c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c11c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c11c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c11c bytes 08a13c91
+ 0057c11c bytes 08613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a6b0f87a19abdda0357f21e386332c0"></a>

### [`0057c274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c274.md) → [`0057c274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c274.md) FUN_0057c274

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058f9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f9b0.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`0058f9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f9b0.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md)

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
      "definition_site": "0057c290",
      "incomplete_value": false,
      "site": "0057c294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c290",
      "incomplete_value": false,
      "site": "0057c294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
      "0057c294",
      "DATA",
      [
        "storage",
        "00bf0e70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c294",
      "DATA",
      [
        "storage",
        "00bf0f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c274.md#insn-0057c290)
- 新版 `0057c290`（命令位置の公開資料なし）

~~~diff
- 0057c290 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 0057c290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c290 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 0057c290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c290 bytes 08c13991
+ 0057c290 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df03770ed412bb44901671bef1a9129b"></a>

### [`0057c2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c2c0.md) → [`0057c2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c2c0.md) FUN_0057c2c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057c2e4",
      "incomplete_value": true,
      "site": "0057c2f4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:c7f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c2e4",
      "incomplete_value": true,
      "site": "0057c2f4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:bf2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057c2f8",
      "incomplete_value": true,
      "site": "0057c2f8",
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
      "definition_site": "0057c2f8",
      "incomplete_value": true,
      "site": "0057c2f8",
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
      "0057c2e4",
      "READ",
      [
        "storage",
        "00296bf2",
        null,
        "string"
      ]
    ],
    [
      "0057c2e8",
      "READ",
      [
        "storage",
        "00296c01",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057c2e4",
      "READ",
      [
        "storage",
        "00296c7f",
        null,
        "string"
      ]
    ],
    [
      "0057c2e8",
      "READ",
      [
        "storage",
        "00296c8e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c2c0.md#insn-0057c2dc) · [`0057c2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c2c0.md#insn-0057c2e0)
- 新版 `0057c2dc`（命令位置の公開資料なし） · `0057c2e0`（命令位置の公開資料なし）

~~~diff
- 0057c2dc ["COPY", "tmp:0:8", ["const:bf2:8"]]
- 0057c2dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c2dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c2dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c2dc ["COPY", "tmp:0:8", ["const:c7f:8"]]
+ 0057c2dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c2dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c2dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c2dc bytes 08c92f91
+ 0057c2dc bytes 08fd3191
- 0057c2e0 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0057c2e0 bytes a9e9ff90
+ 0057c2e0 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0057c2e0 bytes a9e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e23c9173e6f912921c13f67dcfa840a"></a>

### [`0057c468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c468.md) → [`0057c468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c468.md) FUN_0057c468

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057c488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057c488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057c48c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0057c48c",
      "DATA",
      [
        "storage",
        "00bf0f78",
        null,
        "undefined *"
      ]
    ],
    [
      "0057c49c",
      "DATA",
      [
        "storage",
        "00bf0ec8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057c48c",
      "DATA",
      [
        "storage",
        "00bf1028",
        null,
        "undefined *"
      ]
    ],
    [
      "0057c49c",
      "DATA",
      [
        "storage",
        "00bf0f78",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c468.md#insn-0057c488) · [`0057c48c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c468.md#insn-0057c48c)
- 新版 `0057c488`（命令位置の公開資料なし）

~~~diff
- 0057c488 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0057c488 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0057c488 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0057c488 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0057c488 bytes 1ffc00a9
+ 0057c488 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 0057c488 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 0057c488 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 0057c488 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 0057c488 bytes 1ffc00a9
- 0057c48c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0057c48c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0057c48c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-680c6d20e9047b3e1d02cce5625fa19e"></a>

### [`0057c4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c4b0.md) → [`0057c4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c4b0.md) FUN_0057c4b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057c4dc",
      "incomplete_value": false,
      "site": "0057c4e0",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0057c4dc",
      "incomplete_value": false,
      "site": "0057c4e0",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "0057c4e0",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c4e0",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c4d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c4b0.md#insn-0057c4d4)
- 新版 `0057c4d4`（命令位置の公開資料なし）

~~~diff
- 0057c4d4 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0057c4d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c4d4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0057c4d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c4d4 bytes 08412591
+ 0057c4d4 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d64da2acaf6a37f95fc0f91af6ac561"></a>

### [`0057c514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c514.md) → [`0057c514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c514.md) FUN_0057c514

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
      "definition_site": "0057c540",
      "incomplete_value": false,
      "site": "0057c544",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0057c540",
      "incomplete_value": false,
      "site": "0057c544",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "0057c544",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c544",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c514.md#insn-0057c538)
- 新版 `0057c538`（命令位置の公開資料なし）

~~~diff
- 0057c538 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0057c538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c538 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0057c538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c538 bytes 08412591
+ 0057c538 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61dd803c5f8ee30ab654048668cf15ce"></a>

### [`0057c574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c574.md) → [`0057c574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c574.md) FUN_0057c574

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057c5ac",
      "incomplete_value": false,
      "site": "0057c5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c5ac",
      "incomplete_value": false,
      "site": "0057c5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057c5b0",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057c5b0",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c5ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c574.md#insn-0057c5ac)
- 新版 `0057c5ac`（命令位置の公開資料なし）

~~~diff
- 0057c5ac ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057c5ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057c5ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057c5ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057c5ac ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057c5ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c5ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c5ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057c5ac bytes 29012591
+ 0057c5ac bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f83281f4468bac042ed635cacdd158a"></a>

### [`0057c5d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c5d4.md) → [`0057c5d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c5d4.md) FUN_0057c5d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057c60c",
      "incomplete_value": false,
      "site": "0057c610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c60c",
      "incomplete_value": false,
      "site": "0057c610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057c610",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057c610",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c60c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c5d4.md#insn-0057c60c)
- 新版 `0057c60c`（命令位置の公開資料なし）

~~~diff
- 0057c60c ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057c60c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057c60c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057c60c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057c60c ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057c60c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c60c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c60c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057c60c bytes 29012591
+ 0057c60c bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a026fcc05bd504e47b8fba0cd6278a6a"></a>

### [`0057c630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c630.md) → [`0057c630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c630.md) FUN_0057c630

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
      "definition_site": "0057c634",
      "incomplete_value": false,
      "site": "0057c638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c634",
      "incomplete_value": false,
      "site": "0057c638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057c638",
      "DATA",
      [
        "storage",
        "00bf0f28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c638",
      "DATA",
      [
        "storage",
        "00bf0fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c630.md#insn-0057c634)
- 新版 `0057c634`（命令位置の公開資料なし）

~~~diff
- 0057c634 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 0057c634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c634 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 0057c634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c634 bytes 08a13c91
+ 0057c634 bytes 08613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60c9f7ec897a294754c25365a5afeecf"></a>

### [`0057c640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c640.md) → [`0057c640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c640.md) FUN_0057c640

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
      "definition_site": "0057c650",
      "incomplete_value": false,
      "site": "0057c658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c650",
      "incomplete_value": false,
      "site": "0057c658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057c658",
      "DATA",
      [
        "storage",
        "00bf0f28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c658",
      "DATA",
      [
        "storage",
        "00bf0fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c640.md#insn-0057c650)
- 新版 `0057c650`（命令位置の公開資料なし）

~~~diff
- 0057c650 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 0057c650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c650 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 0057c650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c650 bytes 08a13c91
+ 0057c650 bytes 08613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a769009c1d61e2ceee0f7fe527992a46"></a>

### [`0057c670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c670.md) → [`0057c670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c670.md) FUN_0057c670

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057c6a8",
      "incomplete_value": false,
      "site": "0057c6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c6a8",
      "incomplete_value": false,
      "site": "0057c6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057c6ac",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057c6ac",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c6a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c670.md#insn-0057c6a8)
- 新版 `0057c6a8`（命令位置の公開資料なし）

~~~diff
- 0057c6a8 ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057c6a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057c6a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057c6a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057c6a8 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057c6a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c6a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c6a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057c6a8 bytes 29012591
+ 0057c6a8 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5833af6413fc1b5a5648cbefb35ff991"></a>

### [`0057c6d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c6d4.md) → [`0057c6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c6d4.md) FUN_0057c6d4

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
      "definition_site": "0057c6d8",
      "incomplete_value": false,
      "site": "0057c6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c6d8",
      "incomplete_value": false,
      "site": "0057c6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057c6dc",
      "DATA",
      [
        "storage",
        "00bf0f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c6dc",
      "DATA",
      [
        "storage",
        "00bf1028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c6d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c6d4.md#insn-0057c6d4) · [`0057c6d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c6d4.md#insn-0057c6d8)
- 新版 `0057c6d4`（命令位置の公開資料なし） · `0057c6d8`（命令位置の公開資料なし）

~~~diff
- 0057c6d4 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0057c6d4 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 0057c6d4 bytes a8330090
+ 0057c6d4 bytes a83300b0
- 0057c6d8 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 0057c6d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c6d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c6d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c6d8 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 0057c6d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c6d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c6d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c6d8 bytes 08e13d91
+ 0057c6d8 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-864c764b2b4959f779f939499df52971"></a>

### [`0057c6e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c6e4.md) → [`0057c6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c6e4.md) FUN_0057c6e4

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
      "definition_site": "0057c6f4",
      "incomplete_value": false,
      "site": "0057c6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c6f4",
      "incomplete_value": false,
      "site": "0057c6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057c6fc",
      "DATA",
      [
        "storage",
        "00bf0f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c6fc",
      "DATA",
      [
        "storage",
        "00bf1028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c6f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c6e4.md#insn-0057c6f0) · [`0057c6f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c6e4.md#insn-0057c6f4)
- 新版 `0057c6f0`（命令位置の公開資料なし） · `0057c6f4`（命令位置の公開資料なし）

~~~diff
- 0057c6f0 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0057c6f0 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 0057c6f0 bytes a8330090
+ 0057c6f0 bytes a83300b0
- 0057c6f4 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 0057c6f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c6f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c6f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c6f4 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 0057c6f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c6f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c6f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c6f4 bytes 08e13d91
+ 0057c6f4 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df04db74e34b229db9d54ef208288fdb"></a>

### [`0057c71c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c71c.md) → [`0057c71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c71c.md) _INIT_41

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
      "definition_site": "0057c758",
      "incomplete_value": true,
      "site": "0057c774",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c758",
      "incomplete_value": true,
      "site": "0057c774",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c77c",
      "incomplete_value": true,
      "site": "0057c798",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c77c",
      "incomplete_value": true,
      "site": "0057c798",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c79c",
      "incomplete_value": true,
      "site": "0057c7b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c79c",
      "incomplete_value": true,
      "site": "0057c7b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057c758",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0057c77c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0057c79c",
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
      "0057c758",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057c77c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057c79c",
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

- 旧版 [`0057c748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c71c.md#insn-0057c748) · [`0057c750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c71c.md#insn-0057c750)
- 新版 `0057c748`（命令位置の公開資料なし） · `0057c750`（命令位置の公開資料なし）

~~~diff
- 0057c748 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 0057c748 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057c748 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057c748 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057c748 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 0057c748 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057c748 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057c748 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057c748 bytes 73821a91
+ 0057c748 bytes 73821d91
- 0057c750 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057c750 bytes 49e9fff0
+ 0057c750 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057c750 bytes 49e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef6e778dd4235dc683d19f3a004d6be1"></a>

### [`0057caac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057caac.md) → [`0057caac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057caac.md) FUN_0057caac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578fc4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057caf8",
      "incomplete_value": true,
      "site": "0057caf8",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057caf8",
      "incomplete_value": true,
      "site": "0057caf8",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5e1:8"
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
      "definition_site": "0057cba8",
      "incomplete_value": false,
      "site": "0057cbb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cba8",
      "incomplete_value": false,
      "site": "0057cbb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:a0:8"
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
      "definition_site": "0057cbcc",
      "incomplete_value": false,
      "site": "0057cbd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cbcc",
      "incomplete_value": false,
      "site": "0057cbd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "0057cadc",
      "READ",
      [
        "storage",
        "002a65e1",
        null,
        "string"
      ]
    ],
    [
      "0057cbb4",
      "DATA",
      [
        "storage",
        "00bf10a0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cbd4",
      "DATA",
      [
        "storage",
        "00bf0fc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057cadc",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0057cbb4",
      "DATA",
      [
        "storage",
        "00bf1150",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cbd4",
      "DATA",
      [
        "storage",
        "00bf1078",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057caac.md#insn-0057cad0) · [`0057cba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057caac.md#insn-0057cba8) · [`0057cbc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057caac.md#insn-0057cbc8)
- 新版 `0057cad0`（命令位置の公開資料なし） · `0057cba8`（命令位置の公開資料なし） · `0057cbc8`（命令位置の公開資料なし）

~~~diff
- 0057cad0 ["COPY", "tmp:0:8", ["const:5e1:8"]]
- 0057cad0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057cad0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057cad0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057cad0 ["COPY", "tmp:0:8", ["const:5da:8"]]
+ 0057cad0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057cad0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057cad0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057cad0 bytes 4a851791
+ 0057cad0 bytes 4a691791
- 0057cba8 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 0057cba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cba8 ["COPY", "tmp:0:8", ["const:150:8"]]
+ 0057cba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cba8 bytes 08810291
+ 0057cba8 bytes 08410591
- 0057cbc8 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0057cbc8 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 0057cbc8 bytes a8330090
+ 0057cbc8 bytes a83300b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c30122f932f03f7e1b01c6b20e5b9a8a"></a>

### [`0057cc9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057cc9c.md) → [`0057cc9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cc9c.md) FUN_0057cc9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058e0ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058e/0058e0ec.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`0058e0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058e0ec.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md)

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
      "definition_site": "0057ccb8",
      "incomplete_value": false,
      "site": "0057ccbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ccb8",
      "incomplete_value": false,
      "site": "0057ccbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "0057ccbc",
      "DATA",
      [
        "storage",
        "00bf0fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ccbc",
      "DATA",
      [
        "storage",
        "00bf1098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ccb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057cc9c.md#insn-0057ccb4) · [`0057ccb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057cc9c.md#insn-0057ccb8)
- 新版 `0057ccb4`（命令位置の公開資料なし） · `0057ccb8`（命令位置の公開資料なし）

~~~diff
- 0057ccb4 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0057ccb4 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 0057ccb4 bytes a8330090
+ 0057ccb4 bytes a83300b0
- 0057ccb8 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 0057ccb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ccb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ccb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ccb8 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 0057ccb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ccb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ccb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ccb8 bytes 08a13f91
+ 0057ccb8 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d46977ba1a9f02cc1e67708fa1aba82c"></a>

### [`0057cedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057cedc.md) → [`0057cedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cedc.md) FUN_0057cedc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057cf08",
      "incomplete_value": false,
      "site": "0057cf0c",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0057cf08",
      "incomplete_value": false,
      "site": "0057cf0c",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "0057cf0c",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057cf0c",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057cedc.md#insn-0057cf00)
- 新版 `0057cf00`（命令位置の公開資料なし）

~~~diff
- 0057cf00 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0057cf00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cf00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cf00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cf00 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0057cf00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cf00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cf00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cf00 bytes 08412591
+ 0057cf00 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7324dcf8a000f8d29c59b0ef9b6e612b"></a>

### [`0057cf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057cf40.md) → [`0057cf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cf40.md) FUN_0057cf40

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
      "definition_site": "0057cf6c",
      "incomplete_value": false,
      "site": "0057cf70",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0057cf6c",
      "incomplete_value": false,
      "site": "0057cf70",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "0057cf70",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057cf70",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cf64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057cf40.md#insn-0057cf64)
- 新版 `0057cf64`（命令位置の公開資料なし）

~~~diff
- 0057cf64 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0057cf64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cf64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cf64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cf64 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0057cf64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cf64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cf64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cf64 bytes 08412591
+ 0057cf64 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1b157326b4cc4a0b31971bc63cea10c"></a>

### [`0057cfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057cfe0.md) → [`0057cfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cfe0.md) FUN_0057cfe0

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
      "definition_site": "0057cfe4",
      "incomplete_value": false,
      "site": "0057cfe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cfe4",
      "incomplete_value": false,
      "site": "0057cfe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "0057cfe8",
      "DATA",
      [
        "storage",
        "00bf10a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057cfe8",
      "DATA",
      [
        "storage",
        "00bf1150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cfe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057cfe0.md#insn-0057cfe4)
- 新版 `0057cfe4`（命令位置の公開資料なし）

~~~diff
- 0057cfe4 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 0057cfe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cfe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cfe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cfe4 ["COPY", "tmp:0:8", ["const:150:8"]]
+ 0057cfe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cfe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cfe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cfe4 bytes 08810291
+ 0057cfe4 bytes 08410591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc1810ddcce56f350729eea2bbd2d614"></a>

### [`0057cff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057cff0.md) → [`0057cff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cff0.md) FUN_0057cff0

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
      "definition_site": "0057d000",
      "incomplete_value": false,
      "site": "0057d008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d000",
      "incomplete_value": false,
      "site": "0057d008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "0057d008",
      "DATA",
      [
        "storage",
        "00bf10a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d008",
      "DATA",
      [
        "storage",
        "00bf1150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057cff0.md#insn-0057d000)
- 新版 `0057d000`（命令位置の公開資料なし）

~~~diff
- 0057d000 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 0057d000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d000 ["COPY", "tmp:0:8", ["const:150:8"]]
+ 0057d000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d000 bytes 08810291
+ 0057d000 bytes 08410591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-def381e9692a2a191732926fa71e8057"></a>

### [`0057d020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d020.md) → [`0057d020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d020.md) FUN_0057d020

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
      "definition_site": "0057d028",
      "incomplete_value": false,
      "site": "0057d02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d028",
      "incomplete_value": false,
      "site": "0057d02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057d02c",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057d02c",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d020.md#insn-0057d028)
- 新版 `0057d028`（命令位置の公開資料なし）

~~~diff
- 0057d028 ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057d028 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057d028 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057d028 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057d028 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057d028 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d028 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d028 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057d028 bytes 29012591
+ 0057d028 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ada9d7e8c0697507fa56ea6972ff6e20"></a>

### [`0057d054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d054.md) → [`0057d054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d054.md) FUN_0057d054

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
      "definition_site": "0057d064",
      "incomplete_value": false,
      "site": "0057d06c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d064",
      "incomplete_value": false,
      "site": "0057d06c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
      "0057d06c",
      "DATA",
      [
        "storage",
        "00bf10f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d06c",
      "DATA",
      [
        "storage",
        "00bf11a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d054.md#insn-0057d064)
- 新版 `0057d064`（命令位置の公開資料なし）

~~~diff
- 0057d064 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 0057d064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d064 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 0057d064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d064 bytes 08c10391
+ 0057d064 bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e4af1910eed96d106c66a0a593d9669"></a>

### [`0057d08c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d08c.md) → [`0057d08c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d08c.md) _INIT_42

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057d0c8",
      "incomplete_value": true,
      "site": "0057d0e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d0c8",
      "incomplete_value": true,
      "site": "0057d0e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d12c",
      "incomplete_value": true,
      "site": "0057d144",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:73b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d12c",
      "incomplete_value": true,
      "site": "0057d144",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ae:8"
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
      "definition_site": "0057d148",
      "incomplete_value": true,
      "site": "0057d164",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29c000:8"
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
      "definition_site": "0057d148",
      "incomplete_value": true,
      "site": "0057d164",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29c000:8"
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
      "0057d0c8",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0057d0ec",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0057d10c",
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
      "0057d0c8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057d0ec",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057d10c",
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

- 旧版 [`0057d0b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d08c.md#insn-0057d0b8) · [`0057d0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d08c.md#insn-0057d0c0)
- 新版 `0057d0b8`（命令位置の公開資料なし） · `0057d0c0`（命令位置の公開資料なし）

~~~diff
- 0057d0b8 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 0057d0b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057d0b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057d0b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057d0b8 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 0057d0b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057d0b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057d0b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057d0b8 bytes 73e21a91
+ 0057d0b8 bytes 73e21d91
- 0057d0c0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057d0c0 bytes 49e9ffd0
+ 0057d0c0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057d0c0 bytes 49e9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39935461fc9a2b59177a3b2c9685cbe6"></a>

### [`0057d41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d41c.md) → [`0057d41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d41c.md) FUN_0057d41c

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
      "definition_site": "0057d424",
      "incomplete_value": false,
      "site": "0057d428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d424",
      "incomplete_value": false,
      "site": "0057d428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057d428",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057d428",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d41c.md#insn-0057d424)
- 新版 `0057d424`（命令位置の公開資料なし）

~~~diff
- 0057d424 ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057d424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057d424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057d424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057d424 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057d424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057d424 bytes 29012591
+ 0057d424 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1864ab1ff36e8d9dfa12830d386437d2"></a>

### [`0057d43c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d43c.md) → [`0057d43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d43c.md) FUN_0057d43c

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
      "definition_site": "0057d444",
      "incomplete_value": false,
      "site": "0057d448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d444",
      "incomplete_value": false,
      "site": "0057d448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057d448",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057d448",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d43c.md#insn-0057d444)
- 新版 `0057d444`（命令位置の公開資料なし）

~~~diff
- 0057d444 ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057d444 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057d444 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057d444 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057d444 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057d444 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d444 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d444 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057d444 bytes 29012591
+ 0057d444 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe615c309e70d2a6fa271abe0658ad0c"></a>

### [`0057d47c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d47c.md) → [`0057d47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d47c.md) FUN_0057d47c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578fc4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057d4c8",
      "incomplete_value": true,
      "site": "0057d4c8",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d4c8",
      "incomplete_value": true,
      "site": "0057d4c8",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5e1:8"
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
      "definition_site": "0057d578",
      "incomplete_value": false,
      "site": "0057d584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d578",
      "incomplete_value": false,
      "site": "0057d584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      "definition_site": "0057d59c",
      "incomplete_value": false,
      "site": "0057d5a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d59c",
      "incomplete_value": false,
      "site": "0057d5a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:140:8"
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
      "0057d4ac",
      "READ",
      [
        "storage",
        "002a65e1",
        null,
        "string"
      ]
    ],
    [
      "0057d584",
      "DATA",
      [
        "storage",
        "00bf1218",
        null,
        "undefined *"
      ]
    ],
    [
      "0057d5a4",
      "DATA",
      [
        "storage",
        "00bf1140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d4ac",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0057d584",
      "DATA",
      [
        "storage",
        "00bf12c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0057d5a4",
      "DATA",
      [
        "storage",
        "00bf11f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d4a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d47c.md#insn-0057d4a0) · [`0057d578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d47c.md#insn-0057d578) · [`0057d59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d47c.md#insn-0057d59c)
- 新版 `0057d4a0`（命令位置の公開資料なし） · `0057d578`（命令位置の公開資料なし） · `0057d59c`（命令位置の公開資料なし）

~~~diff
- 0057d4a0 ["COPY", "tmp:0:8", ["const:5e1:8"]]
- 0057d4a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057d4a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057d4a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057d4a0 ["COPY", "tmp:0:8", ["const:5da:8"]]
+ 0057d4a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057d4a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057d4a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057d4a0 bytes 4a851791
+ 0057d4a0 bytes 4a691791
- 0057d578 ["COPY", "tmp:0:8", ["const:218:8"]]
- 0057d578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d578 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 0057d578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d578 bytes 08610891
+ 0057d578 bytes 08210b91
- 0057d59c ["COPY", "tmp:0:8", ["const:140:8"]]
- 0057d59c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d59c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d59c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d59c ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 0057d59c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d59c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d59c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d59c bytes 08010591
+ 0057d59c bytes 08c10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e063610daf213e3cf2c5fe5993443e2"></a>

### [`0057d670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d670.md) → [`0057d670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d670.md) FUN_0057d670

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "0057d68c",
      "incomplete_value": true,
      "site": "0057d68c",
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
                "const:6ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d68c",
      "incomplete_value": true,
      "site": "0057d68c",
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
                "const:660:8"
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
      "0057d67c",
      "READ",
      [
        "storage",
        "002a1660",
        null,
        "string"
      ]
    ],
    [
      "0057d684",
      "READ",
      [
        "storage",
        "002a1667",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057d67c",
      "READ",
      [
        "storage",
        "002a16ed",
        null,
        "string"
      ]
    ],
    [
      "0057d684",
      "READ",
      [
        "storage",
        "002a16f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d670.md#insn-0057d678)
- 新版 `0057d678`（命令位置の公開資料なし）

~~~diff
- 0057d678 ["COPY", "tmp:0:8", ["const:660:8"]]
- 0057d678 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057d678 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057d678 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057d678 ["COPY", "tmp:0:8", ["const:6ed:8"]]
+ 0057d678 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057d678 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057d678 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057d678 bytes 4a811991
+ 0057d678 bytes 4ab51b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0826a3fefe102efaf62ced24e2fc3ac1"></a>

### [`0057d6c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d6c8.md) → [`0057d6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d6c8.md) FUN_0057d6c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0057d6e4",
      "incomplete_value": false,
      "site": "0057d6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d6e4",
      "incomplete_value": false,
      "site": "0057d6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "definition_site": "0057d6fc",
      "incomplete_value": false,
      "site": "0057d6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d6fc",
      "incomplete_value": false,
      "site": "0057d6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:178:8"
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
      "0057d6ec",
      "DATA",
      [
        "storage",
        "00bf1268",
        null,
        "undefined *"
      ]
    ],
    [
      "0057d6fc",
      "DATA",
      [
        "storage",
        "00bf1178",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057d6ec",
      "DATA",
      [
        "storage",
        "00bf1318",
        null,
        "undefined *"
      ]
    ],
    [
      "0057d6fc",
      "DATA",
      [
        "storage",
        "00bf1228",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d6e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d6c8.md#insn-0057d6e4) · [`0057d6f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d6c8.md#insn-0057d6f0)
- 新版 `0057d6e4`（命令位置の公開資料なし） · `0057d6f0`（命令位置の公開資料なし）

~~~diff
- 0057d6e4 ["COPY", "tmp:0:8", ["const:268:8"]]
- 0057d6e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d6e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d6e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d6e4 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0057d6e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d6e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d6e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d6e4 bytes 08a10991
+ 0057d6e4 bytes 08610c91
- 0057d6f0 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 0057d6f0 bytes a8330090
+ 0057d6f0 ["COPY", "register:4040:8", ["const:bf1000:8"]]
+ 0057d6f0 bytes a8330090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d8e50ca0a82882fe4b6ddc7dea56626"></a>

### [`0057d710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d710.md) → [`0057d710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d710.md) FUN_0057d710

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057d72c",
      "incomplete_value": true,
      "site": "0057d730",
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
      "definition_site": "0057d72c",
      "incomplete_value": true,
      "site": "0057d730",
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
      "0057d724",
      "READ",
      [
        "storage",
        "00c1b430",
        null,
        "pointer"
      ]
    ],
    [
      "0057d730",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d724",
      "READ",
      [
        "storage",
        "00c1b4e0",
        null,
        "pointer"
      ]
    ],
    [
      "0057d730",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d710.md#insn-0057d724)
- 新版 `0057d724`（命令位置の公開資料なし）

~~~diff
- 0057d724 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:430:8"]]
- 0057d724 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0057d724 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
+ 0057d724 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0057d724 bytes 081942f9
+ 0057d724 bytes 087142f9
~~~


<a id="compare-96de24ddcc1cbecd9a764fdb9f4510d9"></a>

### [`0057d760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d760.md) → [`0057d760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d760.md) FUN_0057d760

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
      "definition_site": "0057d764",
      "incomplete_value": false,
      "site": "0057d768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d764",
      "incomplete_value": false,
      "site": "0057d768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "0057d768",
      "DATA",
      [
        "storage",
        "00bf1218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d768",
      "DATA",
      [
        "storage",
        "00bf12c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d760.md#insn-0057d764)
- 新版 `0057d764`（命令位置の公開資料なし）

~~~diff
- 0057d764 ["COPY", "tmp:0:8", ["const:218:8"]]
- 0057d764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d764 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 0057d764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d764 bytes 08610891
+ 0057d764 bytes 08210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d765ff30246c14d9c2fe3918b01d7bf4"></a>

### [`0057d7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d7a0.md) → [`0057d7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d7a0.md) FUN_0057d7a0

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
      "definition_site": "0057d7a8",
      "incomplete_value": false,
      "site": "0057d7ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d7a8",
      "incomplete_value": false,
      "site": "0057d7ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057d7ac",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057d7ac",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d7a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d7a0.md#insn-0057d7a8)
- 新版 `0057d7a8`（命令位置の公開資料なし）

~~~diff
- 0057d7a8 ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057d7a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057d7a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057d7a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057d7a8 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057d7a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d7a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d7a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057d7a8 bytes 29012591
+ 0057d7a8 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebd146a86507de7f702a003d9c5362ee"></a>

### [`0057d7c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d7c4.md) → [`0057d7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d7c4.md) FUN_0057d7c4

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
      "definition_site": "0057d7c8",
      "incomplete_value": false,
      "site": "0057d7cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d7c8",
      "incomplete_value": false,
      "site": "0057d7cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "0057d7cc",
      "DATA",
      [
        "storage",
        "00bf1268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d7cc",
      "DATA",
      [
        "storage",
        "00bf1318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d7c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d7c4.md#insn-0057d7c8)
- 新版 `0057d7c8`（命令位置の公開資料なし）

~~~diff
- 0057d7c8 ["COPY", "tmp:0:8", ["const:268:8"]]
- 0057d7c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d7c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d7c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d7c8 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0057d7c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d7c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d7c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d7c8 bytes 08a10991
+ 0057d7c8 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7de4fa332e7a39cb2d94c21ef62596fe"></a>

### [`0057d7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d7d4.md) → [`0057d7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d7d4.md) FUN_0057d7d4

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
      "definition_site": "0057d7e4",
      "incomplete_value": false,
      "site": "0057d7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d7e4",
      "incomplete_value": false,
      "site": "0057d7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "0057d7ec",
      "DATA",
      [
        "storage",
        "00bf1268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d7ec",
      "DATA",
      [
        "storage",
        "00bf1318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d7e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d7d4.md#insn-0057d7e4)
- 新版 `0057d7e4`（命令位置の公開資料なし）

~~~diff
- 0057d7e4 ["COPY", "tmp:0:8", ["const:268:8"]]
- 0057d7e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d7e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d7e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d7e4 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0057d7e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d7e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d7e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d7e4 bytes 08a10991
+ 0057d7e4 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e7e3f79b2809f1abdec3aac16450826"></a>

### [`0057d80c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d80c.md) → [`0057d80c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d80c.md) _INIT_43

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
      "definition_site": "0057d848",
      "incomplete_value": true,
      "site": "0057d864",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d848",
      "incomplete_value": true,
      "site": "0057d864",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d86c",
      "incomplete_value": true,
      "site": "0057d888",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d86c",
      "incomplete_value": true,
      "site": "0057d888",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d88c",
      "incomplete_value": true,
      "site": "0057d8a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d88c",
      "incomplete_value": true,
      "site": "0057d8a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057d848",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0057d86c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0057d88c",
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
      "0057d848",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057d86c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057d88c",
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

- 旧版 [`0057d838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d80c.md#insn-0057d838) · [`0057d840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057d80c.md#insn-0057d840)
- 新版 `0057d838`（命令位置の公開資料なし） · `0057d840`（命令位置の公開資料なし）

~~~diff
- 0057d838 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 0057d838 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057d838 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057d838 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057d838 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 0057d838 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057d838 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057d838 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057d838 bytes 73421b91
+ 0057d838 bytes 73421e91
- 0057d840 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057d840 bytes 49e9ffd0
+ 0057d840 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057d840 bytes 49e9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26ccd9019ecf6bca50e39fa6e9d892c0"></a>

### [`0057db9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057db9c.md) → [`0057db9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057db9c.md) FUN_0057db9c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578fc4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "0057dbe8",
      "incomplete_value": true,
      "site": "0057dbe8",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dbe8",
      "incomplete_value": true,
      "site": "0057dbe8",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5e1:8"
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
      "definition_site": "0057dd08",
      "incomplete_value": true,
      "site": "0057dd08",
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
                "const:752:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dd08",
      "incomplete_value": true,
      "site": "0057dd08",
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
                "const:759:8"
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
      "definition_site": "0057dd5c",
      "incomplete_value": false,
      "site": "0057dd68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dd5c",
      "incomplete_value": false,
      "site": "0057dd68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:390:8"
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
      "0057dbcc",
      "READ",
      [
        "storage",
        "002a65e1",
        null,
        "string"
      ]
    ],
    [
      "0057dcf8",
      "READ",
      [
        "storage",
        "002a5759",
        null,
        "string"
      ]
    ],
    [
      "0057dd68",
      "DATA",
      [
        "storage",
        "00bf1390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057dbcc",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0057dcf8",
      "READ",
      [
        "storage",
        "002a5752",
        null,
        "string"
      ]
    ],
    [
      "0057dd68",
      "DATA",
      [
        "storage",
        "00bf1440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057db9c.md#insn-0057dbc0) · [`0057dcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057db9c.md#insn-0057dcf0) · [`0057dd5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057db9c.md#insn-0057dd5c)
- 新版 `0057dbc0`（命令位置の公開資料なし） · `0057dcf0`（命令位置の公開資料なし） · `0057dd5c`（命令位置の公開資料なし）

~~~diff
- 0057dbc0 ["COPY", "tmp:0:8", ["const:5e1:8"]]
- 0057dbc0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057dbc0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057dbc0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057dbc0 ["COPY", "tmp:0:8", ["const:5da:8"]]
+ 0057dbc0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057dbc0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057dbc0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057dbc0 bytes 4a851791
+ 0057dbc0 bytes 4a691791
- 0057dcf0 ["COPY", "tmp:0:8", ["const:759:8"]]
- 0057dcf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057dcf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057dcf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057dcf0 ["COPY", "tmp:0:8", ["const:752:8"]]
+ 0057dcf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057dcf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057dcf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057dcf0 bytes 29651d91
+ 0057dcf0 bytes 29491d91
- 0057dd5c ["COPY", "tmp:0:8", ["const:390:8"]]
- 0057dd5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dd5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dd5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dd5c ["COPY", "tmp:0:8", ["const:440:8"]]
+ 0057dd5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dd5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dd5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dd5c bytes 08410e91
+ 0057dd5c bytes 08011191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abc22986b402286869a18b685043d623"></a>

### [`0057de8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057de8c.md) → [`0057de8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057de8c.md) FUN_0057de8c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058ff20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058ff20.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`0058ff20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058ff20.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md)

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
      "definition_site": "0057dea8",
      "incomplete_value": false,
      "site": "0057deac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dea8",
      "incomplete_value": false,
      "site": "0057deac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
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
      "0057deac",
      "DATA",
      [
        "storage",
        "00bf12d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057deac",
      "DATA",
      [
        "storage",
        "00bf1388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057de8c.md#insn-0057dea8)
- 新版 `0057dea8`（命令位置の公開資料なし）

~~~diff
- 0057dea8 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0057dea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dea8 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0057dea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dea8 bytes 08610b91
+ 0057dea8 bytes 08210e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a583c4a98135054db33bcdcedef55da"></a>

### [`0057ded8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057ded8.md) → [`0057ded8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057ded8.md) FUN_0057ded8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057defc",
      "incomplete_value": true,
      "site": "0057df0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:813:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057defc",
      "incomplete_value": true,
      "site": "0057df0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:80d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057df00",
      "incomplete_value": true,
      "site": "0057df10",
      "value": [
        "LOAD",
        "16",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057df00",
      "incomplete_value": true,
      "site": "0057df10",
      "value": [
        "LOAD",
        "16",
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
                "const:9:8"
              ]
            ]
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
      "0057defc",
      "READ",
      [
        "storage",
        "002ab80d",
        null,
        "string"
      ]
    ],
    [
      "0057df00",
      "READ",
      [
        "storage",
        "002ab816",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057defc",
      "READ",
      [
        "storage",
        "002ab813",
        null,
        "string"
      ]
    ],
    [
      "0057df00",
      "READ",
      [
        "storage",
        "002ab81c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057def4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057ded8.md#insn-0057def4) · [`0057def8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057ded8.md#insn-0057def8)
- 新版 `0057def4`（命令位置の公開資料なし） · `0057def8`（命令位置の公開資料なし）

~~~diff
- 0057def4 ["COPY", "tmp:0:8", ["const:80d:8"]]
- 0057def4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057def4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057def4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057def4 ["COPY", "tmp:0:8", ["const:813:8"]]
+ 0057def4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057def4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057def4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057def4 bytes 08352091
+ 0057def4 bytes 084d2091
- 0057def8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0057def8 bytes a9e9ff90
+ 0057def8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0057def8 bytes a9e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c9c08c2e1e7c5b21e8f0978725cb147"></a>

### [`0057df28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057df28.md) → [`0057df28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057df28.md) FUN_0057df28

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a6d0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057df88",
      "incomplete_value": true,
      "site": "0057df88",
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
                "const:169:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057df88",
      "incomplete_value": true,
      "site": "0057df88",
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
                "const:170:8"
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
      "definition_site": "0057e05c",
      "incomplete_value": true,
      "site": "0057e05c",
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
                "const:5fe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e05c",
      "incomplete_value": true,
      "site": "0057e05c",
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
                "const:571:8"
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
      "definition_site": "0057e060",
      "incomplete_value": true,
      "site": "0057e060",
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
      "definition_site": "0057e060",
      "incomplete_value": true,
      "site": "0057e060",
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
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057df80",
      "READ",
      [
        "storage",
        "002a3170",
        null,
        "string"
      ]
    ],
    [
      "0057e010",
      "PARAM",
      [
        "storage",
        "0029e20c",
        null,
        "string"
      ]
    ],
    [
      "0057e030",
      "PARAM",
      [
        "storage",
        "002a65ec",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057df80",
      "READ",
      [
        "storage",
        "002a3169",
        null,
        "string"
      ]
    ],
    [
      "0057e010",
      "PARAM",
      [
        "storage",
        "0029e299",
        null,
        "string"
      ]
    ],
    [
      "0057e030",
      "PARAM",
      [
        "storage",
        "002a65e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057df7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057df28.md#insn-0057df7c) · [`0057e010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057df28.md#insn-0057e010) · [`0057e030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057df28.md#insn-0057e030)
- 新版 `0057df7c`（命令位置の公開資料なし） · `0057e010`（命令位置の公開資料なし） · `0057e030`（命令位置の公開資料なし）

~~~diff
- 0057df7c ["COPY", "tmp:0:8", ["const:170:8"]]
- 0057df7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057df7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057df7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057df7c ["COPY", "tmp:0:8", ["const:169:8"]]
+ 0057df7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057df7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057df7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057df7c bytes 08c10591
+ 0057df7c bytes 08a50591
- 0057e010 ["COPY", "tmp:0:8", ["const:20c:8"]]
- 0057e010 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0057e010 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0057e010 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0057e010 ["COPY", "tmp:0:8", ["const:299:8"]]
+ 0057e010 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0057e010 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0057e010 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0057e010 bytes 21300891
+ 0057e010 bytes 21640a91
- 0057e030 ["COPY", "tmp:0:8", ["const:5ec:8"]]
- 0057e030 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0057e030 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0057e030 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057e030 ["COPY", "tmp:0:8", ["const:5e5:8"]]
+ 0057e030 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057e030 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057e030 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0057e030 bytes 00b01791
+ 0057e030 bytes 00941791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b1134f9233dd5c1dd2730ca90c45d62"></a>

### [`0057e1b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e1b8.md) → [`0057e1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e1b8.md) FUN_0057e1b8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057e1d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057e1d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057e1dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0057e1dc",
      "DATA",
      [
        "storage",
        "00bf13e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e1ec",
      "DATA",
      [
        "storage",
        "00bf1330",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057e1dc",
      "DATA",
      [
        "storage",
        "00bf1490",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e1ec",
      "DATA",
      [
        "storage",
        "00bf13e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e1d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e1b8.md#insn-0057e1d8) · [`0057e1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e1b8.md#insn-0057e1dc)
- 新版 `0057e1d8`（命令位置の公開資料なし）

~~~diff
- 0057e1d8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0057e1d8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0057e1d8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0057e1d8 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0057e1d8 bytes 1ffc00a9
+ 0057e1d8 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 0057e1d8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 0057e1d8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 0057e1d8 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 0057e1d8 bytes 1ffc00a9
- 0057e1dc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0057e1dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0057e1dc bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8bb469da821f33a1483504d14c3a74e"></a>

### [`0057e200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e200.md) → [`0057e200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e200.md) FUN_0057e200

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057e22c",
      "incomplete_value": false,
      "site": "0057e230",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0057e22c",
      "incomplete_value": false,
      "site": "0057e230",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "0057e230",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e230",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e200.md#insn-0057e224)
- 新版 `0057e224`（命令位置の公開資料なし）

~~~diff
- 0057e224 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0057e224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e224 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0057e224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e224 bytes 08412591
+ 0057e224 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-186c5dc4a85383896d0160c085e61266"></a>

### [`0057e264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e264.md) → [`0057e264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e264.md) FUN_0057e264

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
      "definition_site": "0057e290",
      "incomplete_value": false,
      "site": "0057e294",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0057e290",
      "incomplete_value": false,
      "site": "0057e294",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "0057e294",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e294",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e264.md#insn-0057e288)
- 新版 `0057e288`（命令位置の公開資料なし）

~~~diff
- 0057e288 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0057e288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e288 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0057e288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e288 bytes 08412591
+ 0057e288 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1343e93f832b8f929e65ac9604c25964"></a>

### [`0057e2c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e2c4.md) → [`0057e2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e2c4.md) FUN_0057e2c4

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
      "definition_site": "0057e2cc",
      "incomplete_value": false,
      "site": "0057e2d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e2cc",
      "incomplete_value": false,
      "site": "0057e2d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057e2d0",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057e2d0",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e2cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e2c4.md#insn-0057e2cc)
- 新版 `0057e2cc`（命令位置の公開資料なし）

~~~diff
- 0057e2cc ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057e2cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057e2cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057e2cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057e2cc ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057e2cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e2cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e2cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057e2cc bytes 29012591
+ 0057e2cc bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8dce6d1d4ffc18818162cc5a707bccb"></a>

### [`0057e304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e304.md) → [`0057e304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e304.md) FUN_0057e304

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
      "definition_site": "0057e308",
      "incomplete_value": false,
      "site": "0057e30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e308",
      "incomplete_value": false,
      "site": "0057e30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "0057e30c",
      "DATA",
      [
        "storage",
        "00bf1390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e30c",
      "DATA",
      [
        "storage",
        "00bf1440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e304.md#insn-0057e308)
- 新版 `0057e308`（命令位置の公開資料なし）

~~~diff
- 0057e308 ["COPY", "tmp:0:8", ["const:390:8"]]
- 0057e308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e308 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 0057e308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e308 bytes 08410e91
+ 0057e308 bytes 08011191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c025f9bd609aa101e6c262973d939832"></a>

### [`0057e314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e314.md) → [`0057e314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e314.md) FUN_0057e314

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
      "definition_site": "0057e324",
      "incomplete_value": false,
      "site": "0057e32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e324",
      "incomplete_value": false,
      "site": "0057e32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "0057e32c",
      "DATA",
      [
        "storage",
        "00bf1390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e32c",
      "DATA",
      [
        "storage",
        "00bf1440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e314.md#insn-0057e324)
- 新版 `0057e324`（命令位置の公開資料なし）

~~~diff
- 0057e324 ["COPY", "tmp:0:8", ["const:390:8"]]
- 0057e324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e324 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 0057e324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e324 bytes 08410e91
+ 0057e324 bytes 08011191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37fac35231feddd1b8dab7914f1ae57f"></a>

### [`0057e344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e344.md) → [`0057e344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e344.md) FUN_0057e344

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
      "definition_site": "0057e34c",
      "incomplete_value": false,
      "site": "0057e350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e34c",
      "incomplete_value": false,
      "site": "0057e350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "0057e350",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057e350",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e344.md#insn-0057e34c)
- 新版 `0057e34c`（命令位置の公開資料なし）

~~~diff
- 0057e34c ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057e34c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057e34c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057e34c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057e34c ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057e34c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e34c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e34c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057e34c bytes 29012591
+ 0057e34c bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7860480df6b8287009d004bcd3665c67"></a>

### [`0057e368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e368.md) → [`0057e368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e368.md) FUN_0057e368

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
      "definition_site": "0057e36c",
      "incomplete_value": false,
      "site": "0057e370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e36c",
      "incomplete_value": false,
      "site": "0057e370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "0057e370",
      "DATA",
      [
        "storage",
        "00bf13e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e370",
      "DATA",
      [
        "storage",
        "00bf1490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e36c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e368.md#insn-0057e36c)
- 新版 `0057e36c`（命令位置の公開資料なし）

~~~diff
- 0057e36c ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 0057e36c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e36c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e36c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e36c ["COPY", "tmp:0:8", ["const:490:8"]]
+ 0057e36c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e36c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e36c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e36c bytes 08810f91
+ 0057e36c bytes 08411291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb1c6f9a44e840d85e1486b6e835bf58"></a>

### [`0057e378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e378.md) → [`0057e378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e378.md) FUN_0057e378

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
      "definition_site": "0057e388",
      "incomplete_value": false,
      "site": "0057e390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e388",
      "incomplete_value": false,
      "site": "0057e390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "0057e390",
      "DATA",
      [
        "storage",
        "00bf13e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e390",
      "DATA",
      [
        "storage",
        "00bf1490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e378.md#insn-0057e388)
- 新版 `0057e388`（命令位置の公開資料なし）

~~~diff
- 0057e388 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 0057e388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e388 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 0057e388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e388 bytes 08810f91
+ 0057e388 bytes 08411291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33be5ae882abfde03a65583ebbe12ea5"></a>

### [`0057e3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e3b0.md) → [`0057e3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e3b0.md) _INIT_44

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e3ec",
      "incomplete_value": true,
      "site": "0057e408",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057e3ec",
      "incomplete_value": true,
      "site": "0057e408",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057e410",
      "incomplete_value": true,
      "site": "0057e42c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057e410",
      "incomplete_value": true,
      "site": "0057e42c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057e430",
      "incomplete_value": true,
      "site": "0057e44c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057e430",
      "incomplete_value": true,
      "site": "0057e44c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057e3ec",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0057e410",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0057e430",
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
      "0057e3ec",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057e410",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057e430",
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

- 旧版 [`0057e3dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e3b0.md#insn-0057e3dc) · [`0057e3e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e3b0.md#insn-0057e3e4)
- 新版 `0057e3dc`（命令位置の公開資料なし） · `0057e3e4`（命令位置の公開資料なし）

~~~diff
- 0057e3dc ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 0057e3dc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057e3dc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057e3dc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057e3dc ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 0057e3dc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057e3dc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057e3dc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057e3dc bytes 73a21b91
+ 0057e3dc bytes 73a21e91
- 0057e3e4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057e3e4 bytes 49e9ffb0
+ 0057e3e4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057e3e4 bytes 49e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-263d9b70eb0bb92efe5466185f53a862"></a>

### [`0057e740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e740.md) → [`0057e740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e740.md) FUN_0057e740

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0057f400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f400.md) [`0057f660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f660.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0057f400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f400.md) [`0057f660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f660.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057e794",
      "incomplete_value": true,
      "site": "0057e794",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e794",
      "incomplete_value": true,
      "site": "0057e794",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5e1:8"
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
      "definition_site": "0057e8b0",
      "incomplete_value": true,
      "site": "0057e8bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:925:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e8b0",
      "incomplete_value": true,
      "site": "0057e8bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:92c:8"
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
      "0057e778",
      "READ",
      [
        "storage",
        "002a65e1",
        null,
        "string"
      ]
    ],
    [
      "0057e8b0",
      "READ",
      [
        "storage",
        "002a692c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057e778",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0057e8b0",
      "READ",
      [
        "storage",
        "002a6925",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e76c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e740.md#insn-0057e76c) · [`0057e8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e740.md#insn-0057e8a8)
- 新版 `0057e76c`（命令位置の公開資料なし） · `0057e8a8`（命令位置の公開資料なし）

~~~diff
- 0057e76c ["COPY", "tmp:0:8", ["const:5e1:8"]]
- 0057e76c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057e76c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057e76c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057e76c ["COPY", "tmp:0:8", ["const:5da:8"]]
+ 0057e76c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057e76c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057e76c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057e76c bytes 4a851791
+ 0057e76c bytes 4a691791
- 0057e8a8 ["COPY", "tmp:0:8", ["const:92c:8"]]
- 0057e8a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057e8a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057e8a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057e8a8 ["COPY", "tmp:0:8", ["const:925:8"]]
+ 0057e8a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e8a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e8a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057e8a8 bytes 29b12491
+ 0057e8a8 bytes 29952491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30736bf4b6da37866c67d28b309278fe"></a>

### [`0057ec78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057ec78.md) → [`0057ec78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ec78.md) FUN_0057ec78

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00772358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00772/00772358.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`00772358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/00772358.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ec98",
      "incomplete_value": true,
      "site": "0057eca4",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ec98",
      "incomplete_value": true,
      "site": "0057eca4",
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
            "const:450:8"
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
      "0057eca4",
      "DATA",
      [
        "storage",
        "00bf1450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057eca4",
      "DATA",
      [
        "storage",
        "00bf1500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ec98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057ec78.md#insn-0057ec98)
- 新版 `0057ec98`（命令位置の公開資料なし）

~~~diff
- 0057ec98 ["COPY", "tmp:0:8", ["const:450:8"]]
- 0057ec98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057ec98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057ec98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057ec98 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0057ec98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ec98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ec98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057ec98 bytes 29411191
+ 0057ec98 bytes 29011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1037d846e9ec4c0f1a1ad609ca6be45f"></a>

### [`0057eccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057eccc.md) → [`0057eccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057eccc.md) FUN_0057eccc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ecf0",
      "incomplete_value": true,
      "site": "0057ed04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5de:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ecf0",
      "incomplete_value": true,
      "site": "0057ed04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:551:8"
              ]
            ]
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
      "definition_site": "0057ecf0",
      "incomplete_value": true,
      "site": "0057ed04",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0057ecf0",
      "incomplete_value": true,
      "site": "0057ed04",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ed08",
      "incomplete_value": true,
      "site": "0057ed08",
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
                "const:1e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ed08",
      "incomplete_value": true,
      "site": "0057ed08",
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
                "const:1e:8"
              ]
            ]
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
      "0057ecf0",
      "READ",
      [
        "storage",
        "0029b551",
        null,
        "string"
      ]
    ],
    [
      "0057ecf0",
      "READ",
      [
        "storage",
        "0029b561",
        null,
        "string"
      ]
    ],
    [
      "0057ecf8",
      "READ",
      [
        "storage",
        "0029b56f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057ecf0",
      "READ",
      [
        "storage",
        "0029b5de",
        null,
        "string"
      ]
    ],
    [
      "0057ecf0",
      "READ",
      [
        "storage",
        "0029b5ee",
        null,
        "string"
      ]
    ],
    [
      "0057ecf8",
      "READ",
      [
        "storage",
        "0029b5fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ece8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057eccc.md#insn-0057ece8) · [`0057ecec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057eccc.md#insn-0057ecec)
- 新版 `0057ece8`（命令位置の公開資料なし） · `0057ecec`（命令位置の公開資料なし）

~~~diff
- 0057ece8 ["COPY", "tmp:0:8", ["const:551:8"]]
- 0057ece8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ece8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ece8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ece8 ["COPY", "tmp:0:8", ["const:5de:8"]]
+ 0057ece8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ece8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ece8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ece8 bytes 08451591
+ 0057ece8 bytes 08791791
- 0057ecec ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0057ecec bytes 89e9fff0
+ 0057ecec ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0057ecec bytes 89e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-770c7c549ec34fd0521817914e207080"></a>

### [`0057ed1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057ed1c.md) → [`0057ed1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ed1c.md) FUN_0057ed1c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a6d0.md) [`0057945c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00579/0057945c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`0057945c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/0057945c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.58% / 新版 97.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0057ed5c",
      "incomplete_value": false,
      "site": "0057ed64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:b41:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ed5c",
      "incomplete_value": false,
      "site": "0057ed64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:ab4:8"
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
      "definition_site": "0057ee04",
      "incomplete_value": false,
      "site": "0057ee0c",
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
            "const:196:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ee04",
      "incomplete_value": false,
      "site": "0057ee0c",
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
            "const:19d:8"
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
      "0057ed5c",
      "PARAM",
      [
        "storage",
        "00299ab4",
        null,
        null
      ]
    ],
    [
      "0057ede4",
      "PARAM",
      [
        "storage",
        "00299ab6",
        null,
        null
      ]
    ],
    [
      "0057ee04",
      "PARAM",
      [
        "storage",
        "002a319d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057ed5c",
      "PARAM",
      [
        "storage",
        "00299b41",
        null,
        null
      ]
    ],
    [
      "0057ede4",
      "PARAM",
      [
        "storage",
        "00299b43",
        null,
        null
      ]
    ],
    [
      "0057ee04",
      "PARAM",
      [
        "storage",
        "002a3196",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ed5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057ed1c.md#insn-0057ed5c) · [`0057ed88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057ed1c.md#insn-0057ed88) · [`0057ee04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057ed1c.md#insn-0057ee04)
- 新版 `0057ed5c`（命令位置の公開資料なし） · `0057ed88`（命令位置の公開資料なし） · `0057ee04`（命令位置の公開資料なし）

~~~diff
- 0057ed5c ["COPY", "tmp:0:8", ["const:ab4:8"]]
- 0057ed5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0057ed5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0057ed5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0057ed5c ["COPY", "tmp:0:8", ["const:b41:8"]]
+ 0057ed5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0057ed5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0057ed5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0057ed5c bytes 21d02a91
+ 0057ed5c bytes 21042d91
- 0057ed88 ["COPY", "tmp:0:8", ["const:ab6:8"]]
- 0057ed88 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 0057ed88 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 0057ed88 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 0057ed88 ["COPY", "tmp:0:8", ["const:b43:8"]]
+ 0057ed88 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 0057ed88 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 0057ed88 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 0057ed88 bytes b5da2a91
+ 0057ed88 bytes b50e2d91
- 0057ee04 ["COPY", "tmp:0:8", ["const:19d:8"]]
- 0057ee04 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0057ee04 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0057ee04 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0057ee04 ["COPY", "tmp:0:8", ["const:196:8"]]
+ 0057ee04 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0057ee04 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0057ee04 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0057ee04 bytes 21740691
+ 0057ee04 bytes 21580691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9ca081a60468e1c645259ce7aa4bd46"></a>

### [`0057ef60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057ef60.md) → [`0057ef60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ef60.md) FUN_0057ef60

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057ef80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057ef80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057ef84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0057ef84",
      "DATA",
      [
        "storage",
        "00bf1558",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ef94",
      "DATA",
      [
        "storage",
        "00bf14a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057ef84",
      "DATA",
      [
        "storage",
        "00bf1608",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ef94",
      "DATA",
      [
        "storage",
        "00bf1558",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ef80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057ef60.md#insn-0057ef80) · [`0057ef84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057ef60.md#insn-0057ef84)
- 新版 `0057ef80`（命令位置の公開資料なし）

~~~diff
- 0057ef80 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0057ef80 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0057ef80 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0057ef80 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0057ef80 bytes 1ffc00a9
+ 0057ef80 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 0057ef80 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 0057ef80 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 0057ef80 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 0057ef80 bytes 1ffc00a9
- 0057ef84 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0057ef84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0057ef84 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43eee3f819cfe2408ebd37df96faf49a"></a>

### [`0057efa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057efa8.md) → [`0057efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057efa8.md) FUN_0057efa8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0057f054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f054.md) [`007718f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00771/007718f4.md) [`0077246c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00772/0077246c.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 3件 [`0057f054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f054.md) [`007718f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00771/007718f4.md) [`0077246c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/0077246c.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057f014",
      "incomplete_value": false,
      "site": "0057f018",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0057f014",
      "incomplete_value": false,
      "site": "0057f018",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "0057f018",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057f018",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f00c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057efa8.md#insn-0057f00c)
- 新版 `0057f00c`（命令位置の公開資料なし）

~~~diff
- 0057f00c ["COPY", "tmp:0:8", ["const:950:8"]]
- 0057f00c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057f00c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057f00c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057f00c ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0057f00c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f00c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f00c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057f00c bytes 08412591
+ 0057f00c bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-109edceac1e14bf99d39edbccd6c397f"></a>

### [`0057f078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f078.md) → [`0057f078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f078.md) FUN_0057f078

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057f0e0",
      "incomplete_value": false,
      "site": "0057f0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f0e0",
      "incomplete_value": false,
      "site": "0057f0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "0057f0e4",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057f0e4",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f078.md#insn-0057f0e0)
- 新版 `0057f0e0`（命令位置の公開資料なし）

~~~diff
- 0057f0e0 ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057f0e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f0e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f0e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f0e0 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057f0e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f0e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f0e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f0e0 bytes 29012591
+ 0057f0e0 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36a140692f4519beb43691fa24594613"></a>

### [`0057f110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f110.md) → [`0057f110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f110.md) FUN_0057f110

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057f178",
      "incomplete_value": false,
      "site": "0057f17c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f178",
      "incomplete_value": false,
      "site": "0057f17c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "0057f17c",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057f17c",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f110.md#insn-0057f178)
- 新版 `0057f178`（命令位置の公開資料なし）

~~~diff
- 0057f178 ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057f178 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f178 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f178 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f178 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057f178 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f178 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f178 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f178 bytes 29012591
+ 0057f178 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-024adc76e27d62f409f4a52b518aed7e"></a>

### [`0057f38c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f38c.md) → [`0057f38c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f38c.md) FUN_0057f38c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0057f1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f1a0.md) [`0057f400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f400.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0057f1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f1a0.md) [`0057f400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f400.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0057f398",
      "incomplete_value": false,
      "site": "0057f39c",
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
      "definition_site": "0057f398",
      "incomplete_value": false,
      "site": "0057f39c",
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
      "0057f398",
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
      "0057f398",
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

- 旧版 [`0057f398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f38c.md#insn-0057f398)
- 新版 `0057f398`（命令位置の公開資料なし）

~~~diff
- 0057f398 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0057f398 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0057f398 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0057f398 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057f398 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0057f398 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057f398 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057f398 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0057f398 bytes 00280c91
+ 0057f398 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a155e587b28bd509b4408c572495865"></a>

### [`0057f660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f660.md) → [`0057f660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f660.md) FUN_0057f660

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0057e740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057e740.md) · 呼出先 3件 [`00578fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578fc4.md) [`0057f1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f1a0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`0057e740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e740.md) · 呼出先 3件 [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`0057f1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f1a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0057f698",
      "incomplete_value": false,
      "site": "0057f6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f698",
      "incomplete_value": false,
      "site": "0057f6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "0057f6a4",
      "DATA",
      [
        "storage",
        "00bf1508",
        null,
        "undefined *"
      ]
    ],
    [
      "0057f6e0",
      "DATA",
      [
        "storage",
        "00bf1430",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057f6a4",
      "DATA",
      [
        "storage",
        "00bf15b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0057f6e0",
      "DATA",
      [
        "storage",
        "00bf14e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f660.md#insn-0057f698) · [`0057f6dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f660.md#insn-0057f6dc)
- 新版 `0057f698`（命令位置の公開資料なし） · `0057f6dc`（命令位置の公開資料なし）

~~~diff
- 0057f698 ["COPY", "tmp:0:8", ["const:508:8"]]
- 0057f698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057f698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057f698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057f698 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 0057f698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057f698 bytes 08211491
+ 0057f698 bytes 08e11691
- 0057f6dc ["COPY", "tmp:0:8", ["const:430:8"]]
- 0057f6dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057f6dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057f6dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057f6dc ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 0057f6dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f6dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f6dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057f6dc bytes 08c11091
+ 0057f6dc bytes 08811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d57592f7a3da6098b5168a5f19c7f84c"></a>

### [`0057f750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f750.md) → [`0057f750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f750.md) FUN_0057f750

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
      "definition_site": "0057f760",
      "incomplete_value": false,
      "site": "0057f768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f760",
      "incomplete_value": false,
      "site": "0057f768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "0057f768",
      "DATA",
      [
        "storage",
        "00bf1508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057f768",
      "DATA",
      [
        "storage",
        "00bf15b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f750.md#insn-0057f760)
- 新版 `0057f760`（命令位置の公開資料なし）

~~~diff
- 0057f760 ["COPY", "tmp:0:8", ["const:508:8"]]
- 0057f760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057f760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057f760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057f760 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 0057f760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057f760 bytes 08211491
+ 0057f760 bytes 08e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cce285481225f36060fd4985159664e"></a>

### [`0057f780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f780.md) → [`0057f780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f780.md) FUN_0057f780

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057f7e8",
      "incomplete_value": false,
      "site": "0057f7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f7e8",
      "incomplete_value": false,
      "site": "0057f7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "0057f7ec",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057f7ec",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f7e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f780.md#insn-0057f7e8)
- 新版 `0057f7e8`（命令位置の公開資料なし）

~~~diff
- 0057f7e8 ["COPY", "tmp:0:8", ["const:940:8"]]
- 0057f7e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f7e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f7e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f7e8 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0057f7e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f7e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f7e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f7e8 bytes 29012591
+ 0057f7e8 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33272ad88f97e31fd5564039571f8c3b"></a>

### [`0057f81c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f81c.md) → [`0057f81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f81c.md) FUN_0057f81c

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
      "definition_site": "0057f820",
      "incomplete_value": false,
      "site": "0057f824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f820",
      "incomplete_value": false,
      "site": "0057f824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "0057f824",
      "DATA",
      [
        "storage",
        "00bf1558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057f824",
      "DATA",
      [
        "storage",
        "00bf1608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f81c.md#insn-0057f820)
- 新版 `0057f820`（命令位置の公開資料なし）

~~~diff
- 0057f820 ["COPY", "tmp:0:8", ["const:558:8"]]
- 0057f820 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057f820 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057f820 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057f820 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 0057f820 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f820 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f820 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057f820 bytes 08611591
+ 0057f820 bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00d53c0843ee4fd5d54dc701293f96b4"></a>

### [`0057f864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f864.md) → [`0057f864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f864.md) _INIT_45

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f8a0",
      "incomplete_value": true,
      "site": "0057f8bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057f8a0",
      "incomplete_value": true,
      "site": "0057f8bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0057fa94",
      "incomplete_value": true,
      "site": "0057fa98",
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
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fa94",
      "incomplete_value": true,
      "site": "0057fa98",
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
      "0057f8a0",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0057f8c4",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0057f8e4",
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
      "0057f8a0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057f8c4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057f8e4",
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

- 旧版 [`0057f890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f864.md#insn-0057f890) · [`0057f898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057f864.md#insn-0057f898)
- 新版 `0057f890`（命令位置の公開資料なし） · `0057f898`（命令位置の公開資料なし）

~~~diff
- 0057f890 ["COPY", "tmp:0:8", ["const:700:8"]]
- 0057f890 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057f890 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057f890 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057f890 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 0057f890 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057f890 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057f890 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057f890 bytes 73021c91
+ 0057f890 bytes 73021f91
- 0057f898 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057f898 bytes 49e9ff90
+ 0057f898 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057f898 bytes 49e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b60d90cb4c84123937fd37ff0137d99"></a>

### [`0057fbf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057fbf4.md) → [`0057fbf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057fbf4.md) FUN_0057fbf4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578fc4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.27% / 新版 94.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fd64",
      "incomplete_value": true,
      "site": "0057fd64",
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
                "const:7ba:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fd64",
      "incomplete_value": true,
      "site": "0057fd64",
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
                "const:7b4:8"
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
      "definition_site": "0057fdf8",
      "incomplete_value": false,
      "site": "0057fe04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fdf8",
      "incomplete_value": false,
      "site": "0057fe04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "definition_site": "0057fe1c",
      "incomplete_value": false,
      "site": "0057fe24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fe1c",
      "incomplete_value": false,
      "site": "0057fe24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
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
      "0057fc24",
      "READ",
      [
        "storage",
        "002a65e1",
        null,
        "string"
      ]
    ],
    [
      "0057fd50",
      "READ",
      [
        "storage",
        "002aa7b4",
        null,
        "string"
      ]
    ],
    [
      "0057fe04",
      "DATA",
      [
        "storage",
        "00bf1680",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057fc24",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0057fd50",
      "READ",
      [
        "storage",
        "002aa7ba",
        null,
        "string"
      ]
    ],
    [
      "0057fe04",
      "DATA",
      [
        "storage",
        "00bf1730",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057fc18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057fbf4.md#insn-0057fc18) · [`0057fd48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057fbf4.md#insn-0057fd48) · [`0057fdf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057fbf4.md#insn-0057fdf8)
- 新版 `0057fc18`（命令位置の公開資料なし） · `0057fd48`（命令位置の公開資料なし） · `0057fdf8`（命令位置の公開資料なし）

~~~diff
- 0057fc18 ["COPY", "tmp:0:8", ["const:5e1:8"]]
- 0057fc18 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057fc18 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057fc18 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057fc18 ["COPY", "tmp:0:8", ["const:5da:8"]]
+ 0057fc18 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057fc18 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057fc18 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057fc18 bytes 4a851791
+ 0057fc18 bytes 4a691791
- 0057fd48 ["COPY", "tmp:0:8", ["const:7b4:8"]]
- 0057fd48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057fd48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057fd48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057fd48 ["COPY", "tmp:0:8", ["const:7ba:8"]]
+ 0057fd48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057fd48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057fd48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057fd48 bytes 29d11e91
+ 0057fd48 bytes 29e91e91
- 0057fdf8 ["COPY", "tmp:0:8", ["const:680:8"]]
- 0057fdf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057fdf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057fdf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057fdf8 ["COPY", "tmp:0:8", ["const:730:8"]]
+ 0057fdf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057fdf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057fdf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057fdf8 bytes 08011a91
+ 0057fdf8 bytes 08c11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f695b59c6e2decfe1c10b1f744f3770d"></a>

### [`0057ff6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057ff6c.md) → [`0057ff6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057ff6c.md) FUN_0057ff6c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0057ff88",
      "incomplete_value": false,
      "site": "0057ff90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ff88",
      "incomplete_value": false,
      "site": "0057ff90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "definition_site": "0057ffa0",
      "incomplete_value": false,
      "site": "0057ffa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ffa0",
      "incomplete_value": false,
      "site": "0057ffa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "0057ff90",
      "DATA",
      [
        "storage",
        "00bf16d0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ffa0",
      "DATA",
      [
        "storage",
        "00bf15c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057ff90",
      "DATA",
      [
        "storage",
        "00bf1780",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ffa0",
      "DATA",
      [
        "storage",
        "00bf1678",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ff88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057ff6c.md#insn-0057ff88) · [`0057ff94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057ff6c.md#insn-0057ff94)
- 新版 `0057ff88`（命令位置の公開資料なし） · `0057ff94`（命令位置の公開資料なし）

~~~diff
- 0057ff88 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 0057ff88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ff88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ff88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ff88 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 0057ff88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ff88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ff88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ff88 bytes 08411b91
+ 0057ff88 bytes 08011e91
- 0057ff94 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 0057ff94 bytes 883300d0
+ 0057ff94 ["COPY", "register:4040:8", ["const:bf1000:8"]]
+ 0057ff94 bytes 883300d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08a54deb762be32b2808d9219fff02c6"></a>

### [`0057ffb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057ffb4.md) → [`0057ffb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057ffb4.md) FUN_0057ffb4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0057ffd0",
      "incomplete_value": true,
      "site": "0057ffd4",
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
      "definition_site": "0057ffd0",
      "incomplete_value": true,
      "site": "0057ffd4",
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
      "0057ffc8",
      "READ",
      [
        "storage",
        "00c1b430",
        null,
        "pointer"
      ]
    ],
    [
      "0057ffd4",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ffc8",
      "READ",
      [
        "storage",
        "00c1b4e0",
        null,
        "pointer"
      ]
    ],
    [
      "0057ffd4",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ffc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057ffb4.md#insn-0057ffc8)
- 新版 `0057ffc8`（命令位置の公開資料なし）

~~~diff
- 0057ffc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:430:8"]]
- 0057ffc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0057ffc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
+ 0057ffc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0057ffc8 bytes 081942f9
+ 0057ffc8 bytes 087142f9
~~~


<a id="compare-21a74801f13b0bb4c4662c7855e51d05"></a>

### [`00580044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580044.md) → [`00580044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580044.md) FUN_00580044

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
      "definition_site": "00580048",
      "incomplete_value": false,
      "site": "0058004c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580048",
      "incomplete_value": false,
      "site": "0058004c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "0058004c",
      "DATA",
      [
        "storage",
        "00bf1680",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058004c",
      "DATA",
      [
        "storage",
        "00bf1730",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580044.md#insn-00580048)
- 新版 `00580048`（命令位置の公開資料なし）

~~~diff
- 00580048 ["COPY", "tmp:0:8", ["const:680:8"]]
- 00580048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00580048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00580048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00580048 ["COPY", "tmp:0:8", ["const:730:8"]]
+ 00580048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00580048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00580048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00580048 bytes 08011a91
+ 00580048 bytes 08c11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b7337054cae2d7a4606aaa94c932af2"></a>

### [`00580054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580054.md) → [`00580054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580054.md) FUN_00580054

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
      "definition_site": "00580064",
      "incomplete_value": false,
      "site": "0058006c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580064",
      "incomplete_value": false,
      "site": "0058006c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "0058006c",
      "DATA",
      [
        "storage",
        "00bf1680",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058006c",
      "DATA",
      [
        "storage",
        "00bf1730",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580054.md#insn-00580064)
- 新版 `00580064`（命令位置の公開資料なし）

~~~diff
- 00580064 ["COPY", "tmp:0:8", ["const:680:8"]]
- 00580064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00580064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00580064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00580064 ["COPY", "tmp:0:8", ["const:730:8"]]
+ 00580064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00580064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00580064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00580064 bytes 08011a91
+ 00580064 bytes 08c11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-455ac98be0c305a93752fa334aca8208"></a>

### [`00580084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580084.md) → [`00580084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580084.md) FUN_00580084

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
      "definition_site": "0058008c",
      "incomplete_value": false,
      "site": "00580090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058008c",
      "incomplete_value": false,
      "site": "00580090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "00580090",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00580090",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058008c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580084.md#insn-0058008c)
- 新版 `0058008c`（命令位置の公開資料なし）

~~~diff
- 0058008c ["COPY", "tmp:0:8", ["const:940:8"]]
- 0058008c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058008c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058008c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058008c ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0058008c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058008c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058008c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058008c bytes 29012591
+ 0058008c bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06967f51f8fb4846c9fc85556a347614"></a>

### [`005800a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/005800a8.md) → [`005800a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/005800a8.md) FUN_005800a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005800ac",
      "incomplete_value": true,
      "site": "005800b0",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005800ac",
      "incomplete_value": true,
      "site": "005800b0",
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
            "const:6d0:8"
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
      "005800b0",
      "DATA",
      [
        "storage",
        "00bf16d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005800b0",
      "DATA",
      [
        "storage",
        "00bf1780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005800ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/005800a8.md#insn-005800ac)
- 新版 `005800ac`（命令位置の公開資料なし）

~~~diff
- 005800ac ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 005800ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005800ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005800ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005800ac ["COPY", "tmp:0:8", ["const:780:8"]]
+ 005800ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005800ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005800ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005800ac bytes 08411b91
+ 005800ac bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e885398eff7358282d978f6648b18d08"></a>

### [`005800b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/005800b8.md) → [`005800b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/005800b8.md) FUN_005800b8

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
      "definition_site": "005800c8",
      "incomplete_value": false,
      "site": "005800d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005800c8",
      "incomplete_value": false,
      "site": "005800d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "005800d0",
      "DATA",
      [
        "storage",
        "00bf16d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005800d0",
      "DATA",
      [
        "storage",
        "00bf1780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005800c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/005800b8.md#insn-005800c8)
- 新版 `005800c8`（命令位置の公開資料なし）

~~~diff
- 005800c8 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 005800c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005800c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005800c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005800c8 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 005800c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005800c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005800c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005800c8 bytes 08411b91
+ 005800c8 bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa77ca62716f4e4aa89ef026fe6ea4bd"></a>

### [`005800f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/005800f0.md) → [`005800f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/005800f0.md) _INIT_46

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580190",
      "incomplete_value": true,
      "site": "005801a8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:73b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580190",
      "incomplete_value": true,
      "site": "005801a8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:6ae:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00580320",
      "incomplete_value": false,
      "site": "00580324",
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
      "definition_site": "00580320",
      "incomplete_value": false,
      "site": "00580324",
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
      "0058012c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00580150",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00580170",
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
      "0058012c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00580150",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00580170",
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

- 旧版 [`0058011c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/005800f0.md#insn-0058011c) · [`00580124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/005800f0.md#insn-00580124)
- 新版 `0058011c`（命令位置の公開資料なし） · `00580124`（命令位置の公開資料なし）

~~~diff
- 0058011c ["COPY", "tmp:0:8", ["const:718:8"]]
- 0058011c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0058011c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0058011c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0058011c ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0058011c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0058011c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0058011c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0058011c bytes 73621c91
+ 0058011c bytes 73621f91
- 00580124 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00580124 bytes 29e9fff0
+ 00580124 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00580124 bytes 29e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91b55cefe894075ccdd7638e96afb611"></a>

### [`00580480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580480.md) → [`00580480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580480.md) _INIT_47

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005806a8",
      "incomplete_value": false,
      "site": "005806b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005806a8",
      "incomplete_value": false,
      "site": "005806b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "definition_site": "005806b0",
      "incomplete_value": false,
      "site": "005806b4",
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
      "definition_site": "005806b0",
      "incomplete_value": false,
      "site": "005806b4",
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
      "005804bc",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "005804e0",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00580500",
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
      "005804bc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005804e0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00580500",
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

- 旧版 [`005804ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580480.md#insn-005804ac) · [`005804b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580480.md#insn-005804b4)
- 新版 `005804ac`（命令位置の公開資料なし） · `005804b4`（命令位置の公開資料なし）

~~~diff
- 005804ac ["COPY", "tmp:0:8", ["const:730:8"]]
- 005804ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005804ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005804ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005804ac ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 005804ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005804ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005804ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005804ac bytes 73c21c91
+ 005804ac bytes 73c21f91
- 005804b4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005804b4 bytes 29e9fff0
+ 005804b4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005804b4 bytes 29e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54277a4f6670ae9aeaa1fedb99000f54"></a>

### [`00580810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580810.md) → [`00580810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580810.md) _INIT_48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005808b0",
      "incomplete_value": true,
      "site": "005808c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:73b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005808b0",
      "incomplete_value": true,
      "site": "005808c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ae:8"
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
      "0058084c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00580870",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00580890",
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
      "0058084c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00580870",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00580890",
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

- 旧版 [`0058083c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580810.md#insn-0058083c) · [`00580844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580810.md#insn-00580844)
- 新版 `0058083c`（命令位置の公開資料なし） · `00580844`（命令位置の公開資料なし）

~~~diff
- 0058083c ["COPY", "tmp:0:8", ["const:748:8"]]
- 0058083c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0058083c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0058083c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0058083c ["COPY", "tmp:0:8", ["const:808:8"]]
+ 0058083c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0058083c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0058083c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0058083c bytes 73221d91
+ 0058083c bytes 73222091
- 00580844 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00580844 bytes 29e9fff0
+ 00580844 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00580844 bytes 29e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b222db03d216c84ce529595e1dda6f1"></a>

### [`00580ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580ba0.md) → [`00580ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580ba0.md) FUN_00580ba0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00581b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/00581b20.md) [`00581cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/00581cd8.md) [`00581e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/00581e14.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00581b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581b20.md) [`00581cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581cd8.md) [`00581e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581e14.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581034",
      "incomplete_value": true,
      "site": "00581040",
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
                "const:a64:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581034",
      "incomplete_value": true,
      "site": "00581040",
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
                "const:9d7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 82,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005811dc",
      "incomplete_value": true,
      "site": "005811ec",
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
                "const:2b2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005811dc",
      "incomplete_value": true,
      "site": "005811ec",
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
                "const:346:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 105,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00580bd8",
      "READ",
      [
        "storage",
        "002a65e1",
        null,
        "string"
      ]
    ],
    [
      "00580d40",
      "READ",
      [
        "storage",
        "00299e21",
        null,
        "string"
      ]
    ],
    [
      "00580eac",
      "READ",
      [
        "storage",
        "002a65f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00580bd8",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "00580d40",
      "READ",
      [
        "storage",
        "00299eae",
        null,
        "string"
      ]
    ],
    [
      "00580eac",
      "READ",
      [
        "storage",
        "002a65ed",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580bcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580ba0.md#insn-00580bcc) · [`00580d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580ba0.md#insn-00580d38) · [`00580ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580ba0.md#insn-00580ea4)
- 新版 `00580bcc`（命令位置の公開資料なし） · `00580d38`（命令位置の公開資料なし） · `00580ea4`（命令位置の公開資料なし）

~~~diff
- 00580bcc ["COPY", "tmp:0:8", ["const:5e1:8"]]
- 00580bcc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00580bcc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00580bcc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00580bcc ["COPY", "tmp:0:8", ["const:5da:8"]]
+ 00580bcc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00580bcc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00580bcc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00580bcc bytes 4a851791
+ 00580bcc bytes 4a691791
- 00580d38 ["COPY", "tmp:0:8", ["const:e21:8"]]
- 00580d38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00580d38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00580d38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00580d38 ["COPY", "tmp:0:8", ["const:eae:8"]]
+ 00580d38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00580d38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00580d38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00580d38 bytes 29853891
+ 00580d38 bytes 29b93a91
- 00580ea4 ["COPY", "tmp:0:8", ["const:5f4:8"]]
- 00580ea4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00580ea4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00580ea4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00580ea4 ["COPY", "tmp:0:8", ["const:5ed:8"]]
+ 00580ea4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00580ea4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00580ea4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00580ea4 bytes 4ad11791
+ 00580ea4 bytes 4ab51791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25b5eadc84a15179edf35701c56e25dd"></a>

### [`005818b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/005818b0.md) → [`005818b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/005818b0.md) FUN_005818b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/00581d88.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581d88.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005818e4",
      "incomplete_value": true,
      "site": "005818e8",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005818e4",
      "incomplete_value": true,
      "site": "005818e8",
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
            "const:940:8"
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
      "005818e8",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005818e8",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005818e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/005818b0.md#insn-005818e4)
- 新版 `005818e4`（命令位置の公開資料なし）

~~~diff
- 005818e4 ["COPY", "tmp:0:8", ["const:940:8"]]
- 005818e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005818e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005818e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005818e4 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 005818e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005818e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005818e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005818e4 bytes 29012591
+ 005818e4 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed75bd74596dec0608784086bc2863b6"></a>

### [`0058190c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/0058190c.md) → [`0058190c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/0058190c.md) FUN_0058190c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/00581d88.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581d88.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581940",
      "incomplete_value": true,
      "site": "00581944",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581940",
      "incomplete_value": true,
      "site": "00581944",
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
            "const:940:8"
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
      "00581944",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00581944",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/0058190c.md#insn-00581940)
- 新版 `00581940`（命令位置の公開資料なし）

~~~diff
- 00581940 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00581940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00581940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00581940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00581940 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 00581940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00581940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00581940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00581940 bytes 29012591
+ 00581940 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a6eac3d11ee2ece058810ee469f9900"></a>

### [`00581aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/00581aec.md) → [`00581aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581aec.md) FUN_00581aec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00581964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/00581964.md) [`00581e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/00581e14.md) [`007726fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00772/007726fc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`00581964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581964.md) [`00581e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581e14.md) [`007726fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/007726fc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00581af8",
      "incomplete_value": false,
      "site": "00581afc",
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
      "definition_site": "00581af8",
      "incomplete_value": false,
      "site": "00581afc",
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
      "00581af8",
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
      "00581af8",
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

- 旧版 [`00581af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/00581aec.md#insn-00581af8)
- 新版 `00581af8`（命令位置の公開資料なし）

~~~diff
- 00581af8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00581af8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00581af8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00581af8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00581af8 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00581af8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00581af8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00581af8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00581af8 bytes 00280c91
+ 00581af8 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54e03daa566ac11b31df282851b5ce0d"></a>

### [`0058219c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00582/0058219c.md) → [`0058219c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/0058219c.md) FUN_0058219c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00580ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00580/00580ba0.md) · 呼出先 3件 [`00578fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578fc4.md) [`00581964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/00581964.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00580ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580ba0.md) · 呼出先 3件 [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00581964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581964.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "005821d4",
      "incomplete_value": false,
      "site": "005821e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005821d4",
      "incomplete_value": false,
      "site": "005821e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "005821e0",
      "DATA",
      [
        "storage",
        "00bf17f8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058221c",
      "DATA",
      [
        "storage",
        "00bf1720",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005821e0",
      "DATA",
      [
        "storage",
        "00bf18a8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058221c",
      "DATA",
      [
        "storage",
        "00bf17d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005821d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00582/0058219c.md#insn-005821d4) · [`00582218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00582/0058219c.md#insn-00582218)
- 新版 `005821d4`（命令位置の公開資料なし） · `00582218`（命令位置の公開資料なし）

~~~diff
- 005821d4 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 005821d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005821d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005821d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005821d4 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 005821d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005821d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005821d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005821d4 bytes 08e11f91
+ 005821d4 bytes 08a12291
- 00582218 ["COPY", "tmp:0:8", ["const:720:8"]]
- 00582218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00582218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00582218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582218 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 00582218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00582218 bytes 08811c91
+ 00582218 bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebf4ac690388958b65f2190303d26dc7"></a>

### [`005822bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00582/005822bc.md) → [`005822bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/005822bc.md) FUN_005822bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/00581d88.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581d88.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "005822f0",
      "incomplete_value": false,
      "site": "005822f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005822f0",
      "incomplete_value": false,
      "site": "005822f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "005822f4",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005822f4",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005822f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00582/005822bc.md#insn-005822f0)
- 新版 `005822f0`（命令位置の公開資料なし）

~~~diff
- 005822f0 ["COPY", "tmp:0:8", ["const:940:8"]]
- 005822f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005822f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005822f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005822f0 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 005822f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005822f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005822f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005822f0 bytes 29012591
+ 005822f0 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

