# v15.7.2 → v15.7.3 · 最優先の変更候補 (50)

[一覧の目次](README.md)

<a id="compare-1ba58fc2c6708e81758974c82d9ed0db"></a>

### [`0097fe14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097fe14.md) → [`0097fe14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097fe14.md) FUN_0097fe14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097fe48",
      "incomplete_value": true,
      "site": "0097fe4c",
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
      "definition_site": "0097fe48",
      "incomplete_value": true,
      "site": "0097fe4c",
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
      "0097fe4c",
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
      "0097fe4c",
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

- 旧版 [`0097fe40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097fe14.md#insn-0097fe40)
- 新版 `0097fe40`（命令位置の公開資料なし）

~~~diff
- 0097fe40 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0097fe40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097fe40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097fe40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097fe40 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0097fe40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097fe40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097fe40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097fe40 bytes 08412591
+ 0097fe40 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c850f6d717dce557e6e01b816ad826e3"></a>

### [`0097fe88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097fe88.md) → [`0097fe88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097fe88.md) FUN_0097fe88

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0097febc",
      "incomplete_value": false,
      "site": "0097fec0",
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
      "definition_site": "0097febc",
      "incomplete_value": false,
      "site": "0097fec0",
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
      "0097fec0",
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
      "0097fec0",
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

- 旧版 [`0097feb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097fe88.md#insn-0097feb4)
- 新版 `0097feb4`（命令位置の公開資料なし）

~~~diff
- 0097feb4 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0097feb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097feb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097feb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097feb4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0097feb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097feb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097feb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097feb4 bytes 08412591
+ 0097feb4 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-307dd5f490dde5a9df71da4299a39415"></a>

### [`0098044c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/0098044c.md) → [`0098044c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/0098044c.md) FUN_0098044c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00980468",
      "incomplete_value": false,
      "site": "00980478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980468",
      "incomplete_value": false,
      "site": "00980478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:a38:8"
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
      "00980478",
      "DATA",
      [
        "storage",
        "00c0aa38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980478",
      "DATA",
      [
        "storage",
        "00c0aae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/0098044c.md#insn-00980468)
- 新版 `00980468`（命令位置の公開資料なし）

~~~diff
- 00980468 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 00980468 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980468 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980468 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980468 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 00980468 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980468 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980468 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980468 bytes 08e12891
+ 00980468 bytes 08a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da203562987b1da3cda3304cb9b1f5c1"></a>

### [`00980844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980844.md) → [`00980844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980844.md) FUN_00980844

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0098085c",
      "incomplete_value": false,
      "site": "00980868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098085c",
      "incomplete_value": false,
      "site": "00980868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00980868",
      "DATA",
      [
        "storage",
        "00c0aab8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980868",
      "DATA",
      [
        "storage",
        "00c0ab68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098085c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980844.md#insn-0098085c)
- 新版 `0098085c`（命令位置の公開資料なし）

~~~diff
- 0098085c ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 0098085c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098085c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098085c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098085c ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 0098085c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098085c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098085c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098085c bytes 08e12a91
+ 0098085c bytes 08a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2da3f999de929dce41921459fe8389a8"></a>

### [`009808a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/009808a0.md) → [`009808a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/009808a0.md) FUN_009808a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "009808bc",
      "incomplete_value": false,
      "site": "009808cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009808bc",
      "incomplete_value": false,
      "site": "009808cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
      "009808cc",
      "DATA",
      [
        "storage",
        "00c0aab8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009808cc",
      "DATA",
      [
        "storage",
        "00c0ab68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009808bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/009808a0.md#insn-009808bc)
- 新版 `009808bc`（命令位置の公開資料なし）

~~~diff
- 009808bc ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 009808bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009808bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009808bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009808bc ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 009808bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009808bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009808bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009808bc bytes 08e12a91
+ 009808bc bytes 08a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-522fbbd83d91e0a3e7e626b0f03e4741"></a>

### [`00980938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980938.md) → [`00980938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980938.md) FUN_00980938

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00980948",
      "incomplete_value": false,
      "site": "00980950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980948",
      "incomplete_value": false,
      "site": "00980950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00980950",
      "DATA",
      [
        "storage",
        "00c0aab8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980950",
      "DATA",
      [
        "storage",
        "00c0ab68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980938.md#insn-00980948)
- 新版 `00980948`（命令位置の公開資料なし）

~~~diff
- 00980948 ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 00980948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980948 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 00980948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980948 bytes 08e12a91
+ 00980948 bytes 08a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-145f8fb30736ba091a50951d8524eed4"></a>

### [`00980b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980b10.md) → [`00980b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980b10.md) FUN_00980b10

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
      "definition_site": "00980b24",
      "incomplete_value": false,
      "site": "00980b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980b24",
      "incomplete_value": false,
      "site": "00980b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:b38:8"
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
      "00980b28",
      "DATA",
      [
        "storage",
        "00c0ab38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980b28",
      "DATA",
      [
        "storage",
        "00c0abe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980b24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980b10.md#insn-00980b24)
- 新版 `00980b24`（命令位置の公開資料なし）

~~~diff
- 00980b24 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 00980b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980b24 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00980b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980b24 bytes 08e12c91
+ 00980b24 bytes 08a12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85f35d1799b0f08202dee3432ff26bf4"></a>

### [`00980b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980b34.md) → [`00980b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980b34.md) FUN_00980b34

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
      "definition_site": "00980b38",
      "incomplete_value": false,
      "site": "00980b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980b38",
      "incomplete_value": false,
      "site": "00980b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:b38:8"
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
      "00980b3c",
      "DATA",
      [
        "storage",
        "00c0ab38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980b3c",
      "DATA",
      [
        "storage",
        "00c0abe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980b38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980b34.md#insn-00980b38)
- 新版 `00980b38`（命令位置の公開資料なし）

~~~diff
- 00980b38 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 00980b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980b38 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00980b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980b38 bytes 08e12c91
+ 00980b38 bytes 08a12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03a2d63d64822619540b7561799a2cad"></a>

### [`00980b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980b7c.md) → [`00980b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980b7c.md) FUN_00980b7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00980ba0",
      "incomplete_value": true,
      "site": "00980ba0",
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
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980ba0",
      "incomplete_value": true,
      "site": "00980ba0",
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
            "const:bb8:8"
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
      "00980ba0",
      "DATA",
      [
        "storage",
        "00c0abb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980ba0",
      "DATA",
      [
        "storage",
        "00c0ac68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980b7c.md#insn-00980b9c)
- 新版 `00980b9c`（命令位置の公開資料なし）

~~~diff
- 00980b9c ["COPY", "tmp:0:8", ["const:bb8:8"]]
- 00980b9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980b9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980b9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980b9c ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 00980b9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980b9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980b9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980b9c bytes 08e12e91
+ 00980b9c bytes 08a13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b8065fa549ae3a15f7160d98e981582"></a>

### [`00980bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980bb0.md) → [`00980bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980bb0.md) FUN_00980bb0

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
      "definition_site": "00980bbc",
      "incomplete_value": false,
      "site": "00980bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980bbc",
      "incomplete_value": false,
      "site": "00980bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
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
      "00980bbc",
      "DATA",
      [
        "storage",
        "00c0abb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980bbc",
      "DATA",
      [
        "storage",
        "00c0ac68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980bb0.md#insn-00980bb8)
- 新版 `00980bb8`（命令位置の公開資料なし）

~~~diff
- 00980bb8 ["COPY", "tmp:0:8", ["const:bb8:8"]]
- 00980bb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00980bb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00980bb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00980bb8 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 00980bb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00980bb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00980bb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00980bb8 bytes 29e12e91
+ 00980bb8 bytes 29a13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db0363c7374ee5fb03c63b4348446022"></a>

### [`00980d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980d44.md) → [`00980d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980d44.md) FUN_00980d44

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
      "definition_site": "00980d58",
      "incomplete_value": false,
      "site": "00980d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980d58",
      "incomplete_value": false,
      "site": "00980d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "00980d5c",
      "DATA",
      [
        "storage",
        "00c0ac38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980d5c",
      "DATA",
      [
        "storage",
        "00c0ace8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980d58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980d44.md#insn-00980d58)
- 新版 `00980d58`（命令位置の公開資料なし）

~~~diff
- 00980d58 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 00980d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980d58 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 00980d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980d58 bytes 08e13091
+ 00980d58 bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b06a2ca83e5b579c07db794b35b59890"></a>

### [`00980d68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980d68.md) → [`00980d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980d68.md) FUN_00980d68

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
      "definition_site": "00980d6c",
      "incomplete_value": false,
      "site": "00980d70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980d6c",
      "incomplete_value": false,
      "site": "00980d70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
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
      "00980d70",
      "DATA",
      [
        "storage",
        "00c0ac38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980d70",
      "DATA",
      [
        "storage",
        "00c0ace8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980d6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980d68.md#insn-00980d6c)
- 新版 `00980d6c`（命令位置の公開資料なし）

~~~diff
- 00980d6c ["COPY", "tmp:0:8", ["const:c38:8"]]
- 00980d6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980d6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980d6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980d6c ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 00980d6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980d6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980d6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980d6c bytes 08e13091
+ 00980d6c bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b106c4471600fb641a513078aab7aa5"></a>

### [`00980dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980dac.md) → [`00980dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980dac.md) FUN_00980dac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00980db8",
      "incomplete_value": false,
      "site": "00980dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980db8",
      "incomplete_value": false,
      "site": "00980dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
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
      "00980dc4",
      "DATA",
      [
        "storage",
        "00c0acb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980dc4",
      "DATA",
      [
        "storage",
        "00c0ad68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980db8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980dac.md#insn-00980db8)
- 新版 `00980db8`（命令位置の公開資料なし）

~~~diff
- 00980db8 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 00980db8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00980db8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00980db8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00980db8 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00980db8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00980db8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00980db8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00980db8 bytes 4ae13291
+ 00980db8 bytes 4aa13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df06f7c19df5412ab55c05c4152b554b"></a>

### [`00980df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980df0.md) → [`00980df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980df0.md) FUN_00980df0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00980e08",
      "incomplete_value": false,
      "site": "00980e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980e08",
      "incomplete_value": false,
      "site": "00980e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
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
      "00980e14",
      "DATA",
      [
        "storage",
        "00c0acb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980e14",
      "DATA",
      [
        "storage",
        "00c0ad68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980df0.md#insn-00980e08)
- 新版 `00980e08`（命令位置の公開資料なし）

~~~diff
- 00980e08 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 00980e08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980e08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980e08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980e08 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00980e08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980e08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980e08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980e08 bytes 08e13291
+ 00980e08 bytes 08a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa678186863f24a38490d08d1c92f75a"></a>

### [`00980e4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980e4c.md) → [`00980e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980e4c.md) FUN_00980e4c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00980e78",
      "incomplete_value": false,
      "site": "00980e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980e78",
      "incomplete_value": false,
      "site": "00980e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
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
      "00980e78",
      "DATA",
      [
        "storage",
        "00c0acb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980e78",
      "DATA",
      [
        "storage",
        "00c0ad68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980e4c.md#insn-00980e70)
- 新版 `00980e70`（命令位置の公開資料なし）

~~~diff
- 00980e70 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 00980e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980e70 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00980e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980e70 bytes 08e13291
+ 00980e70 bytes 08a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f1b1a82d0e905674e013d6e032f2b4b"></a>

### [`00980edc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980edc.md) → [`00980edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980edc.md) FUN_00980edc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00980efc",
      "incomplete_value": true,
      "site": "00980efc",
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
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980efc",
      "incomplete_value": true,
      "site": "00980efc",
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
            "const:cb8:8"
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
      "00980efc",
      "DATA",
      [
        "storage",
        "00c0acb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980efc",
      "DATA",
      [
        "storage",
        "00c0ad68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980ef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980edc.md#insn-00980ef8)
- 新版 `00980ef8`（命令位置の公開資料なし）

~~~diff
- 00980ef8 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 00980ef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980ef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980ef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980ef8 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00980ef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980ef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980ef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980ef8 bytes 08e13291
+ 00980ef8 bytes 08a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6054f31adec79484a64101ee55624596"></a>

### [`00981158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981158.md) → [`00981158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981158.md) FUN_00981158

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00981164",
      "incomplete_value": false,
      "site": "00981170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981164",
      "incomplete_value": false,
      "site": "00981170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "00981170",
      "DATA",
      [
        "storage",
        "00c0ad38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981170",
      "DATA",
      [
        "storage",
        "00c0ade8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981158.md#insn-00981164)
- 新版 `00981164`（命令位置の公開資料なし）

~~~diff
- 00981164 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00981164 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00981164 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00981164 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00981164 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 00981164 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00981164 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00981164 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00981164 bytes 4ae13491
+ 00981164 bytes 4aa13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af16712ff135f0f2682c872cfd9acb96"></a>

### [`0098119c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/0098119c.md) → [`0098119c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/0098119c.md) FUN_0098119c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009811b4",
      "incomplete_value": false,
      "site": "009811c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009811b4",
      "incomplete_value": false,
      "site": "009811c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "009811c0",
      "DATA",
      [
        "storage",
        "00c0ad38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009811c0",
      "DATA",
      [
        "storage",
        "00c0ade8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009811b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/0098119c.md#insn-009811b4)
- 新版 `009811b4`（命令位置の公開資料なし）

~~~diff
- 009811b4 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 009811b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009811b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009811b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009811b4 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 009811b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009811b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009811b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009811b4 bytes 08e13491
+ 009811b4 bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51491e2c89574f5b43b955e9c6d154fb"></a>

### [`009811f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/009811f8.md) → [`009811f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/009811f8.md) FUN_009811f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00981224",
      "incomplete_value": false,
      "site": "00981224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981224",
      "incomplete_value": false,
      "site": "00981224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "00981224",
      "DATA",
      [
        "storage",
        "00c0ad38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981224",
      "DATA",
      [
        "storage",
        "00c0ade8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098121c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/009811f8.md#insn-0098121c)
- 新版 `0098121c`（命令位置の公開資料なし）

~~~diff
- 0098121c ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0098121c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098121c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098121c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098121c ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 0098121c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098121c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098121c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098121c bytes 08e13491
+ 0098121c bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84af3733d83a07456b00effb00d8a105"></a>

### [`00981280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981280.md) → [`00981280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981280.md) FUN_00981280

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0098129c",
      "incomplete_value": false,
      "site": "0098129c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098129c",
      "incomplete_value": false,
      "site": "0098129c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "0098129c",
      "DATA",
      [
        "storage",
        "00c0ad38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098129c",
      "DATA",
      [
        "storage",
        "00c0ade8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981280.md#insn-00981298)
- 新版 `00981298`（命令位置の公開資料なし）

~~~diff
- 00981298 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00981298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00981298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00981298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00981298 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 00981298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00981298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00981298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00981298 bytes 29e13491
+ 00981298 bytes 29a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74d634f2e86a8659d0eec5a0f70cb2d4"></a>

### [`00981420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981420.md) → [`00981420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981420.md) FUN_00981420

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0097f740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097f740.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ccc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0097f740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f740.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "00981458",
      "incomplete_value": false,
      "site": "00981460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981458",
      "incomplete_value": false,
      "site": "00981460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "00981460",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ],
    [
      "00981518",
      "READ",
      [
        "storage",
        "00bf30a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981460",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00981518",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981420.md#insn-00981458) · [`0098145c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981420.md#insn-0098145c)
- 新版 `00981458`（命令位置の公開資料なし） · `0098145c`（命令位置の公開資料なし）

~~~diff
- 00981458 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00981458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00981458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00981458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00981458 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00981458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00981458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00981458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00981458 bytes 08610291
+ 00981458 bytes 08210591
- 0098145c ["COPY", "register:4098:8", ["register:4000:8"]]
- 0098145c bytes f30300aa
+ 0098145c ["COPY", "register:4098:8", ["register:4000:8"]]
+ 0098145c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ac0dfc53a6090ca78b0a973dddf124c"></a>

### [`00981598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981598.md) → [`00981598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981598.md) FUN_00981598

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009815a4",
      "incomplete_value": false,
      "site": "009815b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009815a4",
      "incomplete_value": false,
      "site": "009815b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "009815b0",
      "DATA",
      [
        "storage",
        "00c0adb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009815b0",
      "DATA",
      [
        "storage",
        "00c0ae68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009815a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981598.md#insn-009815a4)
- 新版 `009815a4`（命令位置の公開資料なし）

~~~diff
- 009815a4 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 009815a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009815a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009815a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009815a4 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 009815a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009815a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009815a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009815a4 bytes 4ae13691
+ 009815a4 bytes 4aa13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d27cffd85fa397b96e5680fbb43f294"></a>

### [`009815dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/009815dc.md) → [`009815dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/009815dc.md) FUN_009815dc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009815f4",
      "incomplete_value": false,
      "site": "00981600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009815f4",
      "incomplete_value": false,
      "site": "00981600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "00981600",
      "DATA",
      [
        "storage",
        "00c0adb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981600",
      "DATA",
      [
        "storage",
        "00c0ae68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009815f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/009815dc.md#insn-009815f4)
- 新版 `009815f4`（命令位置の公開資料なし）

~~~diff
- 009815f4 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 009815f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009815f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009815f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009815f4 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 009815f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009815f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009815f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009815f4 bytes 08e13691
+ 009815f4 bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e58b17351c9aa6e4d9bc146cfea16a28"></a>

### [`009816c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/009816c0.md) → [`009816c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/009816c0.md) FUN_009816c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009816dc",
      "incomplete_value": false,
      "site": "009816dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009816dc",
      "incomplete_value": false,
      "site": "009816dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "009816dc",
      "DATA",
      [
        "storage",
        "00c0adb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009816dc",
      "DATA",
      [
        "storage",
        "00c0ae68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009816d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/009816c0.md#insn-009816d8)
- 新版 `009816d8`（命令位置の公開資料なし）

~~~diff
- 009816d8 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 009816d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009816d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009816d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009816d8 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 009816d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009816d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009816d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009816d8 bytes 29e13691
+ 009816d8 bytes 29a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af362a3bdb5d224973d10f86680d0c1a"></a>

### [`00981858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981858.md) → [`00981858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981858.md) FUN_00981858

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00981864",
      "incomplete_value": false,
      "site": "00981870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981864",
      "incomplete_value": false,
      "site": "00981870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "00981870",
      "DATA",
      [
        "storage",
        "00c0ae38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981870",
      "DATA",
      [
        "storage",
        "00c0aee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981858.md#insn-00981864)
- 新版 `00981864`（命令位置の公開資料なし）

~~~diff
- 00981864 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 00981864 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00981864 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00981864 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00981864 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 00981864 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00981864 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00981864 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00981864 bytes 4ae13891
+ 00981864 bytes 4aa13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a646a77a55254f867c3d58d54ec3fdbd"></a>

### [`0098189c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/0098189c.md) → [`0098189c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/0098189c.md) FUN_0098189c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009818b4",
      "incomplete_value": false,
      "site": "009818c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009818b4",
      "incomplete_value": false,
      "site": "009818c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "009818c0",
      "DATA",
      [
        "storage",
        "00c0ae38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009818c0",
      "DATA",
      [
        "storage",
        "00c0aee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009818b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/0098189c.md#insn-009818b4)
- 新版 `009818b4`（命令位置の公開資料なし）

~~~diff
- 009818b4 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 009818b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009818b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009818b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009818b4 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 009818b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009818b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009818b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009818b4 bytes 08e13891
+ 009818b4 bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e3edd157b5df649d7f936996cae33c5"></a>

### [`009818f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/009818f8.md) → [`009818f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/009818f8.md) FUN_009818f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00981924",
      "incomplete_value": false,
      "site": "00981924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981924",
      "incomplete_value": false,
      "site": "00981924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "00981924",
      "DATA",
      [
        "storage",
        "00c0ae38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981924",
      "DATA",
      [
        "storage",
        "00c0aee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098191c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/009818f8.md#insn-0098191c)
- 新版 `0098191c`（命令位置の公開資料なし）

~~~diff
- 0098191c ["COPY", "tmp:0:8", ["const:e38:8"]]
- 0098191c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098191c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098191c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098191c ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0098191c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098191c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098191c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098191c bytes 08e13891
+ 0098191c bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80277488877c2b3ee937eadbb0a5764b"></a>

### [`00981980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981980.md) → [`00981980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981980.md) FUN_00981980

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0098199c",
      "incomplete_value": false,
      "site": "0098199c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098199c",
      "incomplete_value": false,
      "site": "0098199c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "0098199c",
      "DATA",
      [
        "storage",
        "00c0ae38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098199c",
      "DATA",
      [
        "storage",
        "00c0aee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981980.md#insn-00981998)
- 新版 `00981998`（命令位置の公開資料なし）

~~~diff
- 00981998 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 00981998 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00981998 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00981998 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00981998 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 00981998 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00981998 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00981998 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00981998 bytes 29e13891
+ 00981998 bytes 29a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e72cefa1994e9746a6acfb620e795ec"></a>

### [`00981ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981ac4.md) → [`00981ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981ac4.md) FUN_00981ac4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0097ec84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097ec84.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ccc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0097ec84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ec84.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "00981afc",
      "incomplete_value": false,
      "site": "00981b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981afc",
      "incomplete_value": false,
      "site": "00981b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "00981b04",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ],
    [
      "00981bbc",
      "READ",
      [
        "storage",
        "00bf30a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981b04",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00981bbc",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981ac4.md#insn-00981afc) · [`00981b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981ac4.md#insn-00981b00)
- 新版 `00981afc`（命令位置の公開資料なし） · `00981b00`（命令位置の公開資料なし）

~~~diff
- 00981afc ["COPY", "tmp:0:8", ["const:98:8"]]
- 00981afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00981afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00981afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00981afc ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00981afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00981afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00981afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00981afc bytes 08610291
+ 00981afc bytes 08210591
- 00981b00 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00981b00 bytes f30300aa
+ 00981b00 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00981b00 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-301cb578a3c0e7a2693536237384237e"></a>

### [`00981c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981c3c.md) → [`00981c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981c3c.md) FUN_00981c3c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00981c48",
      "incomplete_value": true,
      "site": "00981c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981c48",
      "incomplete_value": true,
      "site": "00981c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "00981c54",
      "DATA",
      [
        "storage",
        "00c0aeb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981c54",
      "DATA",
      [
        "storage",
        "00c0af68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981c3c.md#insn-00981c48)
- 新版 `00981c48`（命令位置の公開資料なし）

~~~diff
- 00981c48 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00981c48 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00981c48 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00981c48 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00981c48 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00981c48 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00981c48 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00981c48 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00981c48 bytes 4ae13a91
+ 00981c48 bytes 4aa13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9eeed2b4f890f4e0f668a6e56e4c9e51"></a>

### [`00981cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981cdc.md) → [`00981cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981cdc.md) FUN_00981cdc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00981d08",
      "incomplete_value": false,
      "site": "00981d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981d08",
      "incomplete_value": false,
      "site": "00981d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "00981d08",
      "DATA",
      [
        "storage",
        "00c0aeb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981d08",
      "DATA",
      [
        "storage",
        "00c0af68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981cdc.md#insn-00981d00)
- 新版 `00981d00`（命令位置の公開資料なし）

~~~diff
- 00981d00 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00981d00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00981d00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00981d00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00981d00 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00981d00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00981d00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00981d00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00981d00 bytes 08e13a91
+ 00981d00 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1679ea66234832f3105b64cd5c2cc9e3"></a>

### [`00981d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981d64.md) → [`00981d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981d64.md) FUN_00981d64

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00981d80",
      "incomplete_value": false,
      "site": "00981d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981d80",
      "incomplete_value": false,
      "site": "00981d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "00981d80",
      "DATA",
      [
        "storage",
        "00c0aeb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981d80",
      "DATA",
      [
        "storage",
        "00c0af68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981d7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981d64.md#insn-00981d7c)
- 新版 `00981d7c`（命令位置の公開資料なし）

~~~diff
- 00981d7c ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00981d7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00981d7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00981d7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00981d7c ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00981d7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00981d7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00981d7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00981d7c bytes 29e13a91
+ 00981d7c bytes 29a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cae17af0c36f4c930cd9f2ce15e5fc1f"></a>

### [`00981efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981efc.md) → [`00981efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981efc.md) FUN_00981efc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00981f08",
      "incomplete_value": false,
      "site": "00981f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981f08",
      "incomplete_value": false,
      "site": "00981f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "00981f14",
      "DATA",
      [
        "storage",
        "00c0af38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981f14",
      "DATA",
      [
        "storage",
        "00c0afe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981f08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981efc.md#insn-00981f08)
- 新版 `00981f08`（命令位置の公開資料なし）

~~~diff
- 00981f08 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 00981f08 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00981f08 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00981f08 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00981f08 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 00981f08 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00981f08 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00981f08 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00981f08 bytes 4ae13c91
+ 00981f08 bytes 4aa13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6d7804dfcac0e7c0613936c3acc9742"></a>

### [`00981f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981f40.md) → [`00981f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981f40.md) FUN_00981f40

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00981f58",
      "incomplete_value": false,
      "site": "00981f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981f58",
      "incomplete_value": false,
      "site": "00981f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
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
      "00981f64",
      "DATA",
      [
        "storage",
        "00c0af38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981f64",
      "DATA",
      [
        "storage",
        "00c0afe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981f40.md#insn-00981f58)
- 新版 `00981f58`（命令位置の公開資料なし）

~~~diff
- 00981f58 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 00981f58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00981f58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00981f58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00981f58 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 00981f58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00981f58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00981f58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00981f58 bytes 08e13c91
+ 00981f58 bytes 08a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73b3657928856af6b1525beda91ba8b4"></a>

### [`00981f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981f9c.md) → [`00981f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981f9c.md) FUN_00981f9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00981fc8",
      "incomplete_value": false,
      "site": "00981fc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981fc8",
      "incomplete_value": false,
      "site": "00981fc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "00981fc8",
      "DATA",
      [
        "storage",
        "00c0af38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981fc8",
      "DATA",
      [
        "storage",
        "00c0afe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981fc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00981/00981f9c.md#insn-00981fc0)
- 新版 `00981fc0`（命令位置の公開資料なし）

~~~diff
- 00981fc0 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 00981fc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00981fc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00981fc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00981fc0 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 00981fc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00981fc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00981fc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00981fc0 bytes 08e13c91
+ 00981fc0 bytes 08a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac3970e72dcc98389366af383e64d74a"></a>

### [`00982024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982024.md) → [`00982024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982024.md) FUN_00982024

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00982040",
      "incomplete_value": true,
      "site": "00982040",
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
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00982040",
      "incomplete_value": true,
      "site": "00982040",
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
      "00982040",
      "DATA",
      [
        "storage",
        "00c0af38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00982040",
      "DATA",
      [
        "storage",
        "00c0afe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098203c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982024.md#insn-0098203c)
- 新版 `0098203c`（命令位置の公開資料なし）

~~~diff
- 0098203c ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0098203c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0098203c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0098203c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0098203c ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 0098203c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0098203c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0098203c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0098203c bytes 29e13c91
+ 0098203c bytes 29a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63664bb724fb2a1b6f6d3ddeb5de1ea7"></a>

### [`00982168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982168.md) → [`00982168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982168.md) FUN_00982168

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0097e4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097e4e8.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ccc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0097e4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097e4e8.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "009821a0",
      "incomplete_value": false,
      "site": "009821a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009821a0",
      "incomplete_value": false,
      "site": "009821a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "009821a8",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ],
    [
      "00982260",
      "READ",
      [
        "storage",
        "00bf30a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009821a8",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00982260",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009821a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982168.md#insn-009821a0) · [`009821a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982168.md#insn-009821a4)
- 新版 `009821a0`（命令位置の公開資料なし） · `009821a4`（命令位置の公開資料なし）

~~~diff
- 009821a0 ["COPY", "tmp:0:8", ["const:98:8"]]
- 009821a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009821a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009821a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009821a0 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 009821a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009821a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009821a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009821a0 bytes 08610291
+ 009821a0 bytes 08210591
- 009821a4 ["COPY", "register:4098:8", ["register:4000:8"]]
- 009821a4 bytes f30300aa
+ 009821a4 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 009821a4 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebc0011490f85709aa4c963e9a5ca21a"></a>

### [`009822e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/009822e0.md) → [`009822e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/009822e0.md) FUN_009822e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009822ec",
      "incomplete_value": false,
      "site": "009822f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009822ec",
      "incomplete_value": false,
      "site": "009822f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "009822f8",
      "DATA",
      [
        "storage",
        "00c0afb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009822f8",
      "DATA",
      [
        "storage",
        "00c0b068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009822e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/009822e0.md#insn-009822e8) · [`009822ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/009822e0.md#insn-009822ec)
- 新版 `009822e8`（命令位置の公開資料なし） · `009822ec`（命令位置の公開資料なし）

~~~diff
- 009822e8 ["COPY", "register:4050:8", ["const:c0a000:8"]]
+ 009822e8 ["COPY", "register:4050:8", ["const:c0b000:8"]]
- 009822e8 bytes 4a140090
+ 009822e8 bytes 4a1400b0
- 009822ec ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 009822ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009822ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009822ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009822ec ["COPY", "tmp:0:8", ["const:68:8"]]
+ 009822ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009822ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009822ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009822ec bytes 4ae13e91
+ 009822ec bytes 4aa10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-797f2101692b6f64388b099679b29cb1"></a>

### [`00982324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982324.md) → [`00982324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982324.md) FUN_00982324

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0098233c",
      "incomplete_value": false,
      "site": "00982348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098233c",
      "incomplete_value": false,
      "site": "00982348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "00982348",
      "DATA",
      [
        "storage",
        "00c0afb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00982348",
      "DATA",
      [
        "storage",
        "00c0b068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00982338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982324.md#insn-00982338) · [`0098233c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982324.md#insn-0098233c)
- 新版 `00982338`（命令位置の公開資料なし） · `0098233c`（命令位置の公開資料なし）

~~~diff
- 00982338 ["COPY", "register:4040:8", ["const:c0a000:8"]]
+ 00982338 ["COPY", "register:4040:8", ["const:c0b000:8"]]
- 00982338 bytes 48140090
+ 00982338 bytes 481400b0
- 0098233c ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 0098233c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098233c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098233c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098233c ["COPY", "tmp:0:8", ["const:68:8"]]
+ 0098233c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098233c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098233c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098233c bytes 08e13e91
+ 0098233c bytes 08a10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1069fc436ffdc5b148b468163139e3ba"></a>

### [`00982380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982380.md) → [`00982380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982380.md) FUN_00982380

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "009823ac",
      "incomplete_value": false,
      "site": "009823ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009823ac",
      "incomplete_value": false,
      "site": "009823ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "009823ac",
      "DATA",
      [
        "storage",
        "00c0afb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009823ac",
      "DATA",
      [
        "storage",
        "00c0b068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009823a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982380.md#insn-009823a0) · [`009823a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982380.md#insn-009823a4)
- 新版 `009823a0`（命令位置の公開資料なし） · `009823a4`（命令位置の公開資料なし）

~~~diff
- 009823a0 ["COPY", "register:4040:8", ["const:c0a000:8"]]
+ 009823a0 ["COPY", "register:4040:8", ["const:c0b000:8"]]
- 009823a0 bytes 48140090
+ 009823a0 bytes 481400b0
- 009823a4 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 009823a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009823a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009823a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009823a4 ["COPY", "tmp:0:8", ["const:68:8"]]
+ 009823a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009823a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009823a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009823a4 bytes 08e13e91
+ 009823a4 bytes 08a10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b3404492951737203bec7d6ff63e798"></a>

### [`00982408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982408.md) → [`00982408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982408.md) FUN_00982408

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00982424",
      "incomplete_value": false,
      "site": "00982424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00982424",
      "incomplete_value": false,
      "site": "00982424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "00982424",
      "DATA",
      [
        "storage",
        "00c0afb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00982424",
      "DATA",
      [
        "storage",
        "00c0b068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098241c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982408.md#insn-0098241c) · [`00982420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982408.md#insn-00982420)
- 新版 `0098241c`（命令位置の公開資料なし） · `00982420`（命令位置の公開資料なし）

~~~diff
- 0098241c ["COPY", "register:4048:8", ["const:c0a000:8"]]
+ 0098241c ["COPY", "register:4048:8", ["const:c0b000:8"]]
- 0098241c bytes 49140090
+ 0098241c bytes 491400b0
- 00982420 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 00982420 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00982420 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00982420 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00982420 ["COPY", "tmp:0:8", ["const:68:8"]]
+ 00982420 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00982420 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00982420 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00982420 bytes 29e13e91
+ 00982420 bytes 29a10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f81d5f64720aa2dcd2a2dad5bffb98c4"></a>

### [`009825a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/009825a0.md) → [`009825a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/009825a0.md) FUN_009825a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009825ac",
      "incomplete_value": false,
      "site": "009825b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009825ac",
      "incomplete_value": false,
      "site": "009825b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "009825b8",
      "DATA",
      [
        "storage",
        "00c0b038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009825b8",
      "DATA",
      [
        "storage",
        "00c0b0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009825ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/009825a0.md#insn-009825ac)
- 新版 `009825ac`（命令位置の公開資料なし）

~~~diff
- 009825ac ["COPY", "tmp:0:8", ["const:38:8"]]
- 009825ac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009825ac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009825ac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009825ac ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 009825ac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009825ac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009825ac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009825ac bytes 4ae10091
+ 009825ac bytes 4aa10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b48138f5875c274f5662a3a86e1386aa"></a>

### [`00982640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982640.md) → [`00982640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982640.md) FUN_00982640

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0098266c",
      "incomplete_value": false,
      "site": "0098266c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098266c",
      "incomplete_value": false,
      "site": "0098266c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "0098266c",
      "DATA",
      [
        "storage",
        "00c0b038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098266c",
      "DATA",
      [
        "storage",
        "00c0b0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00982664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982640.md#insn-00982664)
- 新版 `00982664`（命令位置の公開資料なし）

~~~diff
- 00982664 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00982664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00982664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00982664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00982664 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00982664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00982664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00982664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00982664 bytes 08e10091
+ 00982664 bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78b75d44839dcc92e14c0652d77bef22"></a>

### [`009826c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/009826c8.md) → [`009826c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/009826c8.md) FUN_009826c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009826e4",
      "incomplete_value": false,
      "site": "009826e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009826e4",
      "incomplete_value": false,
      "site": "009826e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "009826e4",
      "DATA",
      [
        "storage",
        "00c0b038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009826e4",
      "DATA",
      [
        "storage",
        "00c0b0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009826e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/009826c8.md#insn-009826e0)
- 新版 `009826e0`（命令位置の公開資料なし）

~~~diff
- 009826e0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 009826e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009826e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009826e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009826e0 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 009826e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009826e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009826e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009826e0 bytes 29e10091
+ 009826e0 bytes 29a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24862f7d5f3f8b90ab10cafaa084f864"></a>

### [`0098280c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/0098280c.md) → [`0098280c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/0098280c.md) _INIT_192

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.40% / 新版 90.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0098288c",
      "incomplete_value": true,
      "site": "009828a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0098288c",
      "incomplete_value": true,
      "site": "009828a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009828ac",
      "incomplete_value": true,
      "site": "009828c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009828ac",
      "incomplete_value": true,
      "site": "009828c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009828c8",
      "incomplete_value": true,
      "site": "009828e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009828c8",
      "incomplete_value": true,
      "site": "009828e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00982848",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0098286c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0098288c",
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
      "00982848",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0098286c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0098288c",
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

- 旧版 [`00982838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/0098280c.md#insn-00982838) · [`00982840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/0098280c.md#insn-00982840)
- 新版 `00982838`（命令位置の公開資料なし） · `00982840`（命令位置の公開資料なし）

~~~diff
- 00982838 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 00982838 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00982838 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00982838 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00982838 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00982838 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00982838 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00982838 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00982838 bytes 73622391
+ 00982838 bytes 73622691
- 00982840 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00982840 bytes 29c9ffb0
+ 00982840 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00982840 bytes 29c9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0826b4bb85c0f16b288913b58aa109c4"></a>

### [`00982c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982c5c.md) → [`00982c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982c5c.md) FUN_00982c5c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) · 呼出先 13件 [`009009cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009009cc.md) [`0090126c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/0090126c.md) [`00977eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00977/00977eec.md) [`00982ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982ed4.md) [`00983570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00983/00983570.md)
- 新版 呼出元 1件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 13件 [`009009cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009009cc.md) [`0090126c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/0090126c.md) [`00977eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00977/00977eec.md) [`00982ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982ed4.md) [`00983570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00983/00983570.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.44% / 新版 98.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00982dbc",
      "incomplete_value": false,
      "site": "00982dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00982dbc",
      "incomplete_value": false,
      "site": "00982dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:b8:8"
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
      "00982dbc",
      "DATA",
      [
        "storage",
        "00c0b0b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00982df4",
      "READ",
      [
        "storage",
        "00c0b0d8",
        null,
        "pointer"
      ]
    ],
    [
      "00982df4",
      "READ",
      [
        "storage",
        "00c0b0e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00982dbc",
      "DATA",
      [
        "storage",
        "00c0b168",
        null,
        "undefined *"
      ]
    ],
    [
      "00982df4",
      "READ",
      [
        "storage",
        "00c0b188",
        null,
        "pointer"
      ]
    ],
    [
      "00982df4",
      "READ",
      [
        "storage",
        "00c0b190",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00982db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982c5c.md#insn-00982db4)
- 新版 `00982db4`（命令位置の公開資料なし）

~~~diff
- 00982db4 ["COPY", "tmp:0:8", ["const:b8:8"]]
- 00982db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00982db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00982db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00982db4 ["COPY", "tmp:0:8", ["const:168:8"]]
+ 00982db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00982db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00982db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00982db4 bytes 08e10291
+ 00982db4 bytes 08a10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ecf3b02ac4dbc76f0e3418b2453634f"></a>

### [`00982ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982ed4.md) → [`00982ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982ed4.md) FUN_00982ed4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00982c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982c5c.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00459a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md)
- 新版 呼出元 1件 [`00982c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982c5c.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.29% / 新版 92.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0098341c",
      "incomplete_value": false,
      "site": "0098341c",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "definition_site": "0098341c",
      "incomplete_value": false,
      "site": "0098341c",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 37,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00983420",
      "incomplete_value": false,
      "site": "00983420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00983420",
      "incomplete_value": false,
      "site": "00983420",
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
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0098341c",
      "incomplete_value": false,
      "site": "00983420",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "definition_site": "0098341c",
      "incomplete_value": false,
      "site": "00983420",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
      "00982f10",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00982f1c",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00982f24",
      "PARAM",
      [
        "storage",
        "0109e910",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00982f10",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00982f1c",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "00982f24",
      "PARAM",
      [
        "storage",
        "0109e9d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00982f08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982ed4.md#insn-00982f08) · [`00982f0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982ed4.md#insn-00982f0c) · [`00982f18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982ed4.md#insn-00982f18)
- 新版 `00982f08`（命令位置の公開資料なし） · `00982f0c`（命令位置の公開資料なし） · `00982f18`（命令位置の公開資料なし）

~~~diff
- 00982f08 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 00982f08 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 00982f08 bytes 081500d0
+ 00982f08 bytes 081500f0
- 00982f0c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00982f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00982f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00982f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00982f0c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00982f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00982f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00982f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00982f0c bytes 08e13d91
+ 00982f0c bytes 08e10091
- 00982f18 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 00982f18 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 00982f18 bytes 001500d0
+ 00982f18 bytes 001500f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-146dc8db06fc54042b3b12c5c6186da7"></a>

### [`00983570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00983/00983570.md) → [`00983570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00983/00983570.md) FUN_00983570

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00982c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982c5c.md) · 呼出先 12件 [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`00883d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883d5c.md) [`00883e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883e08.md) [`009846f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/009846f8.md)
- 新版 呼出元 1件 [`00982c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982c5c.md) · 呼出先 12件 [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00883d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d5c.md) [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md) [`009846f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00984/009846f8.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "00983724",
      "incomplete_value": false,
      "site": "00983728",
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
      "definition_site": "00983724",
      "incomplete_value": false,
      "site": "00983728",
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
      "00983670",
      "DATA",
      [
        "storage",
        "00c0b138",
        null,
        "undefined *"
      ]
    ],
    [
      "009836cc",
      "READ",
      [
        "storage",
        "00c0b158",
        null,
        "pointer"
      ]
    ],
    [
      "009836cc",
      "READ",
      [
        "storage",
        "00c0b160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00983670",
      "DATA",
      [
        "storage",
        "00c0b1e8",
        null,
        "undefined *"
      ]
    ],
    [
      "009836cc",
      "READ",
      [
        "storage",
        "00c0b208",
        null,
        "pointer"
      ]
    ],
    [
      "009836cc",
      "READ",
      [
        "storage",
        "00c0b210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098365c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00983/00983570.md#insn-0098365c) · [`009836dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00983/00983570.md#insn-009836dc) · [`0098371c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00983/00983570.md#insn-0098371c)
- 新版 `0098365c`（命令位置の公開資料なし） · `009836dc`（命令位置の公開資料なし） · `0098371c`（命令位置の公開資料なし）

~~~diff
- 0098365c ["COPY", "tmp:0:8", ["const:138:8"]]
- 0098365c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0098365c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0098365c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0098365c ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 0098365c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0098365c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0098365c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0098365c bytes 4ae10491
+ 0098365c bytes 4aa10791
- 009836dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:470:8"]]
- 009836dc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 009836dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:520:8"]]
+ 009836dc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 009836dc bytes b53a42f9
+ 009836dc bytes b59242f9
- 0098371c ["COPY", "tmp:0:8", ["const:c80:8"]]
- 0098371c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098371c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098371c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098371c ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 0098371c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098371c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098371c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098371c bytes 08013291
+ 0098371c bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d50d3252fa8fe2bce2eac88f2865719"></a>

### [`009843fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/009843fc.md) → [`009843fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00984/009843fc.md) FUN_009843fc

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
      "definition_site": "00984420",
      "incomplete_value": false,
      "site": "00984420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00984420",
      "incomplete_value": false,
      "site": "00984420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:b8:8"
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
      "00984420",
      "DATA",
      [
        "storage",
        "00c0b0b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00984420",
      "DATA",
      [
        "storage",
        "00c0b168",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098441c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/009843fc.md#insn-0098441c)
- 新版 `0098441c`（命令位置の公開資料なし）

~~~diff
- 0098441c ["COPY", "tmp:0:8", ["const:b8:8"]]
- 0098441c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098441c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098441c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098441c ["COPY", "tmp:0:8", ["const:168:8"]]
+ 0098441c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098441c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098441c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098441c bytes 08e10291
+ 0098441c bytes 08a10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03b4ec178422639a6210a5a99dd8f02f"></a>

### [`00984430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/00984430.md) → [`00984430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00984/00984430.md) FUN_00984430

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
      "definition_site": "0098443c",
      "incomplete_value": false,
      "site": "0098443c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098443c",
      "incomplete_value": false,
      "site": "0098443c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:b8:8"
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
      "0098443c",
      "DATA",
      [
        "storage",
        "00c0b0b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098443c",
      "DATA",
      [
        "storage",
        "00c0b168",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00984438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/00984430.md#insn-00984438)
- 新版 `00984438`（命令位置の公開資料なし）

~~~diff
- 00984438 ["COPY", "tmp:0:8", ["const:b8:8"]]
- 00984438 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00984438 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00984438 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00984438 ["COPY", "tmp:0:8", ["const:168:8"]]
+ 00984438 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00984438 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00984438 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00984438 bytes 29e10291
+ 00984438 bytes 29a10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0c55b96358f7de3d26499186fa67589"></a>

### [`009846a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/009846a8.md) → [`009846a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00984/009846a8.md) FUN_009846a8

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
      "definition_site": "009846c8",
      "incomplete_value": false,
      "site": "009846cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009846c8",
      "incomplete_value": false,
      "site": "009846cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "009846cc",
      "DATA",
      [
        "storage",
        "00c0b138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009846cc",
      "DATA",
      [
        "storage",
        "00c0b1e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009846c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/009846a8.md#insn-009846c8)
- 新版 `009846c8`（命令位置の公開資料なし）

~~~diff
- 009846c8 ["COPY", "tmp:0:8", ["const:138:8"]]
- 009846c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009846c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009846c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009846c8 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 009846c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009846c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009846c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009846c8 bytes 08e10491
+ 009846c8 bytes 08a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bad63ce7af437069afdb6f820b92bb3"></a>

### [`009846e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/009846e0.md) → [`009846e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00984/009846e0.md) FUN_009846e0

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
      "definition_site": "009846e4",
      "incomplete_value": false,
      "site": "009846e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009846e4",
      "incomplete_value": false,
      "site": "009846e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "009846e8",
      "DATA",
      [
        "storage",
        "00c0b138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009846e8",
      "DATA",
      [
        "storage",
        "00c0b1e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009846e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/009846e0.md#insn-009846e4)
- 新版 `009846e4`（命令位置の公開資料なし）

~~~diff
- 009846e4 ["COPY", "tmp:0:8", ["const:138:8"]]
- 009846e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009846e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009846e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009846e4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 009846e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009846e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009846e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009846e4 bytes 08e10491
+ 009846e4 bytes 08a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aff7debf642656c19c55182c2f96c92"></a>

### [`00984ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/00984ce0.md) → [`00984ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00984/00984ce0.md) FUN_00984ce0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00987404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987404.md) · 呼出先 17件 [`0042ca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca08.md) [`00431e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431e50.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0073a038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a038.md) [`0073ab94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073ab94.md)
- 新版 呼出元 1件 [`00987404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00987/00987404.md) · 呼出先 17件 [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`00431e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431e50.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md) [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00984dc0",
      "incomplete_value": false,
      "site": "00984dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00984dc0",
      "incomplete_value": false,
      "site": "00984dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:238:8"
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
      "definition_site": "00984e14",
      "incomplete_value": true,
      "site": "00984e24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:147:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00984e14",
      "incomplete_value": true,
      "site": "00984e24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ba:8"
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
      "definition_site": "00984e28",
      "incomplete_value": true,
      "site": "00984e28",
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
      "definition_site": "00984e28",
      "incomplete_value": true,
      "site": "00984e28",
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
      "00984dc8",
      "DATA",
      [
        "storage",
        "00c0b238",
        null,
        "undefined *"
      ]
    ],
    [
      "00984e14",
      "READ",
      [
        "storage",
        "002950ba",
        null,
        "string"
      ]
    ],
    [
      "00984e18",
      "READ",
      [
        "storage",
        "002950c7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00984dc8",
      "DATA",
      [
        "storage",
        "00c0b2e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00984e14",
      "READ",
      [
        "storage",
        "00295147",
        null,
        "string"
      ]
    ],
    [
      "00984e18",
      "READ",
      [
        "storage",
        "00295154",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00984dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/00984ce0.md#insn-00984dc0) · [`00984e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/00984ce0.md#insn-00984e0c) · [`00984e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/00984ce0.md#insn-00984e3c)
- 新版 `00984dc0`（命令位置の公開資料なし） · `00984e0c`（命令位置の公開資料なし） · `00984e3c`（命令位置の公開資料なし）

~~~diff
- 00984dc0 ["COPY", "tmp:0:8", ["const:238:8"]]
- 00984dc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00984dc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00984dc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00984dc0 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00984dc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00984dc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00984dc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00984dc0 bytes 08e10891
+ 00984dc0 bytes 08a10b91
- 00984e0c ["COPY", "tmp:0:8", ["const:ba:8"]]
- 00984e0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00984e0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00984e0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00984e0c ["COPY", "tmp:0:8", ["const:147:8"]]
+ 00984e0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00984e0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00984e0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00984e0c bytes 29e90291
+ 00984e0c bytes 291d0591
- 00984e3c ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 00984e3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00984e3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00984e3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00984e3c ["COPY", "tmp:0:8", ["const:268:8"]]
+ 00984e3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00984e3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00984e3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00984e3c bytes 08e10691
+ 00984e3c bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3734ac766eb3081cb36de667181680b1"></a>

### [`00985084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00985/00985084.md) → [`00985084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00985/00985084.md) FUN_00985084

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00987ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987ebc.md) · 呼出先 24件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0044b660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b660.md) [`00459a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md)
- 新版 呼出元 1件 [`00987ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00987/00987ebc.md) · 呼出先 24件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0044b660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md) [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.01% / 新版 92.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 51件, `store_destination` 35件, `store_value` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00985108",
      "incomplete_value": true,
      "site": "00985118",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00985108",
      "incomplete_value": true,
      "site": "00985118",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00985320",
      "incomplete_value": true,
      "site": "00985330",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00985320",
      "incomplete_value": true,
      "site": "00985330",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009854a8",
      "incomplete_value": true,
      "site": "009854b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009854a8",
      "incomplete_value": true,
      "site": "009854b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "009850f4",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00985108",
      "READ",
      [
        "storage",
        "002a260c",
        null,
        "string"
      ]
    ],
    [
      "009851bc",
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
      "009850f4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00985108",
      "READ",
      [
        "storage",
        "002a2605",
        null,
        "string"
      ]
    ],
    [
      "009851bc",
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

- 旧版 [`009850ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00985/00985084.md#insn-009850ac) · [`009850c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00985/00985084.md#insn-009850c4) · [`009850c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00985/00985084.md#insn-009850c8)
- 新版 `009850ac`（命令位置の公開資料なし） · `009850c4`（命令位置の公開資料なし） · `009850c8`（命令位置の公開資料なし）

~~~diff
- 009850ac ["COPY", "register:40d0:8", ["const:4cae:8"]]
+ 009850ac ["COPY", "register:40d0:8", ["const:4caf:8"]]
- 009850ac bytes da958952
+ 009850ac bytes fa958952
- 009850c4 ["COPY", "register:40d8:8", ["const:c24000:8"]]
+ 009850c4 ["COPY", "register:40d8:8", ["const:c25000:8"]]
- 009850c4 bytes fb1400f0
+ 009850c4 bytes 1b150090
- 009850c8 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 009850c8 ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
- 009850c8 ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
- 009850c8 ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
+ 009850c8 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 009850c8 ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
+ 009850c8 ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
+ 009850c8 ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
- 009850c8 bytes 7be33d91
+ 009850c8 bytes 7be30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-989c975f9e6c5037d23193edd06052cf"></a>

### [`00987204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987204.md) → [`00987204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00987/00987204.md) FUN_00987204

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0098a8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a8fc.md) · 呼出先 7件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0069aa30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0069a/0069aa30.md) [`0069ab6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0069a/0069ab6c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00989584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/00989584.md)
- 新版 呼出元 1件 [`0098a8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098a/0098a8fc.md) · 呼出先 7件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0069aa30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069aa30.md) [`0069ab6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069ab6c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00989584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/00989584.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00987230",
      "incomplete_value": true,
      "site": "00987230",
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
      "definition_site": "00987230",
      "incomplete_value": true,
      "site": "00987230",
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
      "definition_site": "00987238",
      "incomplete_value": false,
      "site": "0098724c",
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
      "definition_site": "00987238",
      "incomplete_value": false,
      "site": "0098724c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00987240",
      "incomplete_value": false,
      "site": "0098724c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00987240",
      "incomplete_value": false,
      "site": "0098724c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "00987228",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00987238",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00987240",
      "PARAM",
      [
        "storage",
        "00c0b2a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00987228",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00987238",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00987240",
      "PARAM",
      [
        "storage",
        "00c0b358",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00987228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987204.md#insn-00987228) · [`00987238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987204.md#insn-00987238) · [`00987240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987204.md#insn-00987240)
- 新版 `00987228`（命令位置の公開資料なし） · `00987238`（命令位置の公開資料なし） · `00987240`（命令位置の公開資料なし）

~~~diff
- 00987228 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00987228 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00987228 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00987228 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00987228 bytes 08dd44f9
+ 00987228 bytes 083d45f9
- 00987238 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00987238 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00987238 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00987238 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00987238 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00987238 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00987238 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00987238 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00987238 bytes 21603691
+ 00987238 bytes 21203991
- 00987240 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00987240 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00987240 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00987240 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00987240 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00987240 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00987240 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00987240 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00987240 bytes 42a00a91
+ 00987240 bytes 42600d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-991cd4289ad204ea0b0d9c777a4915a4"></a>

### [`009875e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/009875e4.md) → [`009875e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00987/009875e4.md) FUN_009875e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00988664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/00988664.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md)
- 新版 呼出元 1件 [`00988664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00988/00988664.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.85% / 新版 96.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00987600",
      "incomplete_value": true,
      "site": "00987600",
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
      "definition_site": "00987600",
      "incomplete_value": true,
      "site": "00987600",
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
      "definition_site": "00987608",
      "incomplete_value": false,
      "site": "0098761c",
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
      "definition_site": "00987608",
      "incomplete_value": false,
      "site": "0098761c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00987610",
      "incomplete_value": false,
      "site": "0098761c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00987610",
      "incomplete_value": false,
      "site": "0098761c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "009875fc",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00987608",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00987610",
      "PARAM",
      [
        "storage",
        "00c0b2a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009875fc",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00987608",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00987610",
      "PARAM",
      [
        "storage",
        "00c0b358",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009875fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/009875e4.md#insn-009875fc) · [`00987608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/009875e4.md#insn-00987608) · [`00987610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/009875e4.md#insn-00987610)
- 新版 `009875fc`（命令位置の公開資料なし） · `00987608`（命令位置の公開資料なし） · `00987610`（命令位置の公開資料なし）

~~~diff
- 009875fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 009875fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 009875fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 009875fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 009875fc bytes 08dd44f9
+ 009875fc bytes 083d45f9
- 00987608 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00987608 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00987608 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00987608 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00987608 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00987608 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00987608 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00987608 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00987608 bytes 21603691
+ 00987608 bytes 21203991
- 00987610 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00987610 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00987610 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00987610 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00987610 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00987610 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00987610 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00987610 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00987610 bytes 42a00a91
+ 00987610 bytes 42600d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fbefa1555eb37fb33f1d67216e0df8a"></a>

### [`00987b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987b70.md) → [`00987b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00987/00987b70.md) FUN_00987b70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009880bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/009880bc.md) · 呼出先 15件 [`0042ca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca08.md) [`0043196c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/0043196c.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0073a038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a038.md) [`0073ab94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073ab94.md)
- 新版 呼出元 1件 [`009880bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00988/009880bc.md) · 呼出先 15件 [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`0043196c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/0043196c.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md) [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.79% / 新版 96.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00987ca4",
      "incomplete_value": false,
      "site": "00987cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00987ca4",
      "incomplete_value": false,
      "site": "00987cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "definition_site": "00987d48",
      "incomplete_value": false,
      "site": "00987d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00987d48",
      "incomplete_value": false,
      "site": "00987d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "00987bec",
      "DATA",
      [
        "storage",
        "00c0b3d0",
        null,
        "undefined *"
      ]
    ],
    [
      "00987c38",
      "READ",
      [
        "storage",
        "00c0b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "00987c38",
      "READ",
      [
        "storage",
        "00c0b3f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00987bec",
      "DATA",
      [
        "storage",
        "00c0b480",
        null,
        "undefined *"
      ]
    ],
    [
      "00987c38",
      "READ",
      [
        "storage",
        "00c0b4a0",
        null,
        "pointer"
      ]
    ],
    [
      "00987c38",
      "READ",
      [
        "storage",
        "00c0b4a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00987be4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987b70.md#insn-00987be4) · [`00987ca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987b70.md#insn-00987ca4) · [`00987d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987b70.md#insn-00987d44)
- 新版 `00987be4`（命令位置の公開資料なし） · `00987ca4`（命令位置の公開資料なし） · `00987d44`（命令位置の公開資料なし）

~~~diff
- 00987be4 ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 00987be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00987be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00987be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00987be4 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 00987be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00987be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00987be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00987be4 bytes 08410f91
+ 00987be4 bytes 08011291
- 00987ca4 ["COPY", "tmp:0:8", ["const:450:8"]]
- 00987ca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00987ca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00987ca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00987ca4 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 00987ca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00987ca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00987ca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00987ca4 bytes 08411191
+ 00987ca4 bytes 08011491
- 00987d44 ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 00987d44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00987d44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00987d44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00987d44 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00987d44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00987d44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00987d44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00987d44 bytes 08411391
+ 00987d44 bytes 08011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9838173aa8292673ff508cdf7ceaa271"></a>

### [`00987ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987ebc.md) → [`00987ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00987/00987ebc.md) FUN_00987ebc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`009880bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/009880bc.md) [`00988400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/00988400.md) [`0098a8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a8fc.md) · 呼出先 7件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`004752f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/004752f8.md) [`00985084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00985/00985084.md) [`009870dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/009870dc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 3件 [`009880bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00988/009880bc.md) [`00988400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00988/00988400.md) [`0098a8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098a/0098a8fc.md) · 呼出先 7件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`004752f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/004752f8.md) [`00985084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00985/00985084.md) [`009870dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00987/009870dc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 74.39% / 新版 74.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_destination` 8件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00987ef8",
      "incomplete_value": true,
      "site": "00987ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6e4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00987ef8",
      "incomplete_value": true,
      "site": "00987ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:634:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00987fd8",
      "incomplete_value": false,
      "site": "00987fd8",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "definition_site": "00987fd8",
      "incomplete_value": false,
      "site": "00987fd8",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00987fdc",
      "incomplete_value": false,
      "site": "00987fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00987fdc",
      "incomplete_value": false,
      "site": "00987fdc",
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
            "const:f40:8"
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
      "00987ee0",
      "READ",
      [
        "storage",
        "00c24634",
        null,
        "undefined4"
      ]
    ],
    [
      "00987ef8",
      "WRITE",
      [
        "storage",
        "00c24634",
        null,
        "undefined4"
      ]
    ],
    [
      "00987f40",
      "READ",
      [
        "storage",
        "00c24634",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00987ee0",
      "READ",
      [
        "storage",
        "00c246e4",
        null,
        "undefined4"
      ]
    ],
    [
      "00987ef8",
      "WRITE",
      [
        "storage",
        "00c246e4",
        null,
        "undefined4"
      ]
    ],
    [
      "00987f40",
      "READ",
      [
        "storage",
        "00c246e4",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00987ef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987ebc.md#insn-00987ef8) · [`00987ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987ebc.md#insn-00987ee0) · [`00987f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987ebc.md#insn-00987f40)
- 新版 `00987ef8`（命令位置の公開資料なし） · `00987ee0`（命令位置の公開資料なし） · `00987f40`（命令位置の公開資料なし）

~~~diff
- 00987ef8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:634:8"]]
- 00987ef8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00987ef8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e4:8"]]
+ 00987ef8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00987ef8 bytes 893606b9
+ 00987ef8 bytes 89e606b9
- 00987ee0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:634:8"]]
- 00987ee0 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00987ee0 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
+ 00987ee0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e4:8"]]
+ 00987ee0 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00987ee0 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 00987ee0 bytes 883646b9
+ 00987ee0 bytes 88e646b9
- 00987f40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:634:8"]]
- 00987f40 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00987f40 ["INT_SEXT", "register:4048:8", ["tmp:1:4"]]
+ 00987f40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e4:8"]]
+ 00987f40 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00987f40 ["INT_SEXT", "register:4048:8", ["tmp:1:4"]]
- 00987f40 bytes 893686b9
+ 00987f40 bytes 89e686b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3841ae749459d5272f38036804a7e63"></a>

### [`009880bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/009880bc.md) → [`009880bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00988/009880bc.md) FUN_009880bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00988788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/00988788.md) · 呼出先 18件 [`0041fff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fff8.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00646dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00646/00646dc4.md)
- 新版 呼出元 1件 [`00988788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00988/00988788.md) · 呼出先 18件 [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00646dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646dc4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00988228",
      "incomplete_value": false,
      "site": "00988248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00988228",
      "incomplete_value": false,
      "site": "00988248",
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
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0098822c",
      "incomplete_value": true,
      "site": "00988248",
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
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098822c",
      "incomplete_value": true,
      "site": "00988248",
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
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00988310",
      "incomplete_value": false,
      "site": "00988314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00988310",
      "incomplete_value": false,
      "site": "00988314",
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
            "const:f78:8"
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
      "00988188",
      "READ",
      [
        "storage",
        "0029d9d2",
        null,
        "string"
      ]
    ],
    [
      "0098818c",
      "READ",
      [
        "storage",
        "0029d9d9",
        null,
        "string"
      ]
    ],
    [
      "00988218",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00988188",
      "READ",
      [
        "storage",
        "0029da5f",
        null,
        "string"
      ]
    ],
    [
      "0098818c",
      "READ",
      [
        "storage",
        "0029da66",
        null,
        "string"
      ]
    ],
    [
      "00988218",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00988180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/009880bc.md#insn-00988180) · [`00988210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/009880bc.md#insn-00988210) · [`00988214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/009880bc.md#insn-00988214)
- 新版 `00988180`（命令位置の公開資料なし） · `00988210`（命令位置の公開資料なし） · `00988214`（命令位置の公開資料なし）

~~~diff
- 00988180 ["COPY", "tmp:0:8", ["const:9d2:8"]]
- 00988180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00988180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00988180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00988180 ["COPY", "tmp:0:8", ["const:a5f:8"]]
+ 00988180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00988180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00988180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00988180 bytes 29492791
+ 00988180 bytes 297d2991
- 00988210 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 00988210 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 00988210 bytes e8140090
+ 00988210 bytes e81400b0
- 00988214 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00988214 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00988214 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00988214 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00988214 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00988214 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00988214 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00988214 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00988214 bytes 08e13d91
+ 00988214 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f29c460f3a9d235d65922c2d267bc32"></a>

### [`00988400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/00988400.md) → [`00988400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00988/00988400.md) FUN_00988400

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00988b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/00988b78.md) · 呼出先 13件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00886420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/00886420.md) [`008865b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00887/008879f4.md)
- 新版 呼出元 1件 [`00988b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00988/00988b78.md) · 呼出先 13件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00886420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/00886420.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/008879f4.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.06% / 新版 96.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009884c8",
      "incomplete_value": false,
      "site": "009884d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009884c8",
      "incomplete_value": false,
      "site": "009884d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009885b4",
      "incomplete_value": false,
      "site": "009885b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009885b4",
      "incomplete_value": false,
      "site": "009885b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "009884d0",
      "DATA",
      [
        "storage",
        "00c0b6e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00988594",
      "READ",
      [
        "storage",
        "00c0b700",
        null,
        "pointer"
      ]
    ],
    [
      "00988594",
      "READ",
      [
        "storage",
        "00c0b708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009884d0",
      "DATA",
      [
        "storage",
        "00c0b790",
        null,
        "undefined *"
      ]
    ],
    [
      "00988594",
      "READ",
      [
        "storage",
        "00c0b7b0",
        null,
        "pointer"
      ]
    ],
    [
      "00988594",
      "READ",
      [
        "storage",
        "00c0b7b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009884c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/00988400.md#insn-009884c8) · [`009884cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/00988400.md#insn-009884cc)
- 新版 `009884c8`（命令位置の公開資料なし） · `009884cc`（命令位置の公開資料なし）

~~~diff
- 009884c8 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 009884c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009884c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009884c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009884c8 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 009884c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009884c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009884c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009884c8 bytes 08811b91
+ 009884c8 bytes 08411e91
- 009884cc ["COPY", "tmp:0:8", ["const:30:8"]]
- 009884cc ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 009884cc ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 009884cc ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 009884cc bytes f5c30091
+ 009884cc ["COPY", "tmp:0:8", ["const:30:8"]]
+ 009884cc ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
+ 009884cc ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
+ 009884cc ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
+ 009884cc bytes f5c30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d3771dba6ff6c22dbbe670e017c9b44"></a>

### [`00988788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/00988788.md) → [`00988788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00988/00988788.md) FUN_00988788

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 17件 [`0041be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c8f8.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0062d9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062d/0062d9b8.md) [`0062d9bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062d/0062d9bc.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 17件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0062d9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d9b8.md) [`0062d9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d9bc.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.02% / 新版 96.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00988994",
      "incomplete_value": false,
      "site": "00988994",
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
      "definition_site": "00988994",
      "incomplete_value": false,
      "site": "00988994",
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
    "ordinal": 73,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0098898c",
      "incomplete_value": true,
      "site": "00988994",
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
      "definition_site": "0098898c",
      "incomplete_value": true,
      "site": "00988994",
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
    "ordinal": 73,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00988998",
      "incomplete_value": true,
      "site": "00988998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00988998",
      "incomplete_value": true,
      "site": "00988998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "ordinal": 74,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0098898c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00988990",
      "READ",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00988994",
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
      "0098898c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00988990",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00988994",
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

- 旧版 [`00988994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/00988788.md#insn-00988994) · [`00988998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/00988788.md#insn-00988998) · [`009889b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00988/00988788.md#insn-009889b0)
- 新版 `00988994`（命令位置の公開資料なし） · `00988998`（命令位置の公開資料なし） · `009889b0`（命令位置の公開資料なし）

~~~diff
- 00988994 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 00988994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00988994 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 00988994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00988994 bytes 09d504f9
+ 00988994 bytes 093505f9
- 00988998 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:9b8:8"]]
- 00988998 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00988998 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:a78:8"]]
+ 00988998 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00988998 bytes 4adf04f9
+ 00988998 bytes 4a3f05f9
- 009889b0 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:9b8:8"]]
- 009889b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 009889b0 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:a78:8"]]
+ 009889b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 009889b0 bytes 54df04f9
+ 009889b0 bytes 543f05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ba0403c99fe981fff2b508786807e6b"></a>

### [`0098913c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/0098913c.md) → [`0098913c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/0098913c.md) FUN_0098913c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 14件 [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00445d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 14件 [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.54% / 新版 98.54%

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
      "definition_site": "00989164",
      "incomplete_value": true,
      "site": "00989164",
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
      "definition_site": "00989164",
      "incomplete_value": true,
      "site": "00989164",
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
      "definition_site": "00989174",
      "incomplete_value": true,
      "site": "00989188",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00989174",
      "incomplete_value": true,
      "site": "00989188",
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
            "const:d98:8"
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
      "definition_site": "0098917c",
      "incomplete_value": false,
      "site": "00989188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098917c",
      "incomplete_value": false,
      "site": "00989188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "00989160",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00989174",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0098917c",
      "PARAM",
      [
        "storage",
        "00c0b2a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00989160",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00989174",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0098917c",
      "PARAM",
      [
        "storage",
        "00c0b358",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00989160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/0098913c.md#insn-00989160) · [`00989174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/0098913c.md#insn-00989174) · [`0098917c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/0098913c.md#insn-0098917c)
- 新版 `00989160`（命令位置の公開資料なし） · `00989174`（命令位置の公開資料なし） · `0098917c`（命令位置の公開資料なし）

~~~diff
- 00989160 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00989160 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00989160 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00989160 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00989160 bytes 08dd44f9
+ 00989160 bytes 083d45f9
- 00989174 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00989174 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00989174 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00989174 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00989174 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00989174 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00989174 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00989174 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00989174 bytes 21603691
+ 00989174 bytes 21203991
- 0098917c ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 0098917c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0098917c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0098917c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0098917c ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0098917c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0098917c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0098917c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0098917c bytes 42a00a91
+ 0098917c bytes 42600d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cae77171712bdbd7392015cc9d9f0f3"></a>

### [`009898dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/009898dc.md) → [`009898dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/009898dc.md) FUN_009898dc

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
      "definition_site": "009898f0",
      "incomplete_value": false,
      "site": "009898f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009898f0",
      "incomplete_value": false,
      "site": "009898f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
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
      "009898f4",
      "DATA",
      [
        "storage",
        "00c0b1b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009898f4",
      "DATA",
      [
        "storage",
        "00c0b268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009898f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/009898dc.md#insn-009898f0)
- 新版 `009898f0`（命令位置の公開資料なし）

~~~diff
- 009898f0 ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 009898f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009898f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009898f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009898f0 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 009898f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009898f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009898f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009898f0 bytes 08e10691
+ 009898f0 bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5c98e08bf0207cd4b6fda09659fadb2"></a>

### [`00989900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/00989900.md) → [`00989900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/00989900.md) FUN_00989900

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
      "definition_site": "00989904",
      "incomplete_value": false,
      "site": "00989908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00989904",
      "incomplete_value": false,
      "site": "00989908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
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
      "00989908",
      "DATA",
      [
        "storage",
        "00c0b1b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00989908",
      "DATA",
      [
        "storage",
        "00c0b268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00989904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/00989900.md#insn-00989904)
- 新版 `00989904`（命令位置の公開資料なし）

~~~diff
- 00989904 ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 00989904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00989904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00989904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00989904 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 00989904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00989904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00989904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00989904 bytes 08e10691
+ 00989904 bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dafdba2657d2a778059a34064334596"></a>

### [`0098998c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/0098998c.md) → [`0098998c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/0098998c.md) FUN_0098998c

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
      "definition_site": "009899a0",
      "incomplete_value": false,
      "site": "009899a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009899a0",
      "incomplete_value": false,
      "site": "009899a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:238:8"
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
      "009899a4",
      "DATA",
      [
        "storage",
        "00c0b238",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009899a4",
      "DATA",
      [
        "storage",
        "00c0b2e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009899a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/0098998c.md#insn-009899a0)
- 新版 `009899a0`（命令位置の公開資料なし）

~~~diff
- 009899a0 ["COPY", "tmp:0:8", ["const:238:8"]]
- 009899a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009899a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009899a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009899a0 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 009899a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009899a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009899a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009899a0 bytes 08e10891
+ 009899a0 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3100fc2edaec5ec800fe0f7f3409248f"></a>

### [`009899b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/009899b0.md) → [`009899b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/009899b0.md) FUN_009899b0

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
      "definition_site": "009899b4",
      "incomplete_value": false,
      "site": "009899b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009899b4",
      "incomplete_value": false,
      "site": "009899b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:238:8"
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
      "009899b8",
      "DATA",
      [
        "storage",
        "00c0b238",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009899b8",
      "DATA",
      [
        "storage",
        "00c0b2e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009899b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/009899b0.md#insn-009899b4)
- 新版 `009899b4`（命令位置の公開資料なし）

~~~diff
- 009899b4 ["COPY", "tmp:0:8", ["const:238:8"]]
- 009899b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009899b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009899b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009899b4 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 009899b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009899b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009899b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009899b4 bytes 08e10891
+ 009899b4 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a63d510a52a8806a1bf07473ace3651"></a>

### [`009899f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/009899f8.md) → [`009899f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/009899f8.md) FUN_009899f8

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
      "definition_site": "00989a1c",
      "incomplete_value": false,
      "site": "00989a1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00989a1c",
      "incomplete_value": false,
      "site": "00989a1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
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
      "00989a1c",
      "DATA",
      [
        "storage",
        "00c0b2d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00989a1c",
      "DATA",
      [
        "storage",
        "00c0b380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00989a18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/009899f8.md#insn-00989a18)
- 新版 `00989a18`（命令位置の公開資料なし）

~~~diff
- 00989a18 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 00989a18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00989a18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00989a18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00989a18 ["COPY", "tmp:0:8", ["const:380:8"]]
+ 00989a18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00989a18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00989a18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00989a18 bytes 08410b91
+ 00989a18 bytes 08010e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f373ad510957d355bb4d7b9ec6534494"></a>

### [`00989a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/00989a2c.md) → [`00989a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/00989a2c.md) FUN_00989a2c

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
      "definition_site": "00989a38",
      "incomplete_value": false,
      "site": "00989a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00989a38",
      "incomplete_value": false,
      "site": "00989a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
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
      "00989a38",
      "DATA",
      [
        "storage",
        "00c0b2d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00989a38",
      "DATA",
      [
        "storage",
        "00c0b380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00989a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/00989a2c.md#insn-00989a34)
- 新版 `00989a34`（命令位置の公開資料なし）

~~~diff
- 00989a34 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 00989a34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00989a34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00989a34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00989a34 ["COPY", "tmp:0:8", ["const:380:8"]]
+ 00989a34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00989a34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00989a34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00989a34 bytes 29410b91
+ 00989a34 bytes 29010e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d236e2db6963b5763d63c77dafec47cc"></a>

### [`00989a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/00989a48.md) → [`00989a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/00989a48.md) FUN_00989a48

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 40件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046ff30.md) [`005b5878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b5/005b5878.md) [`0063e6d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063e6d4.md)
- 新版 呼出元 0件  · 呼出先 40件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`005b5878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b5878.md) [`0063e6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e6d4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.83% / 新版 94.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00989b34",
      "incomplete_value": true,
      "site": "00989b44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b67:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00989b34",
      "incomplete_value": true,
      "site": "00989b44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ada:8"
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
      "definition_site": "00989b48",
      "incomplete_value": true,
      "site": "00989b48",
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
      "definition_site": "00989b48",
      "incomplete_value": true,
      "site": "00989b48",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00989b78",
      "incomplete_value": false,
      "site": "00989b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00989b78",
      "incomplete_value": false,
      "site": "00989b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:340:8"
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
      "00989af4",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00989b0c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00989b14",
      "PARAM",
      [
        "storage",
        "00c0b2a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00989af4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00989b0c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00989b14",
      "PARAM",
      [
        "storage",
        "00c0b358",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00989af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/00989a48.md#insn-00989af4) · [`00989b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/00989a48.md#insn-00989b0c) · [`00989b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/00989a48.md#insn-00989b14)
- 新版 `00989af4`（命令位置の公開資料なし） · `00989b0c`（命令位置の公開資料なし） · `00989b14`（命令位置の公開資料なし）

~~~diff
- 00989af4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b8:8"]]
- 00989af4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00989af4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 00989af4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00989af4 bytes 20dd44f9
+ 00989af4 bytes 203d45f9
- 00989b0c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00989b0c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00989b0c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00989b0c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00989b0c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00989b0c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00989b0c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00989b0c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00989b0c bytes 21603691
+ 00989b0c bytes 21203991
- 00989b14 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00989b14 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00989b14 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00989b14 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00989b14 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00989b14 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00989b14 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00989b14 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00989b14 bytes 42a00a91
+ 00989b14 bytes 42600d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-046355925983bb1f0bce8d8578334b9c"></a>

### [`0098a6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a6d0.md) → [`0098a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098a/0098a6d0.md) FUN_0098a6d0

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
      "definition_site": "0098a6e4",
      "incomplete_value": false,
      "site": "0098a6e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098a6e4",
      "incomplete_value": false,
      "site": "0098a6e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:340:8"
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
      "0098a6e8",
      "DATA",
      [
        "storage",
        "00c0b340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098a6e8",
      "DATA",
      [
        "storage",
        "00c0b3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098a6e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a6d0.md#insn-0098a6e4)
- 新版 `0098a6e4`（命令位置の公開資料なし）

~~~diff
- 0098a6e4 ["COPY", "tmp:0:8", ["const:340:8"]]
- 0098a6e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098a6e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098a6e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098a6e4 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 0098a6e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098a6e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098a6e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098a6e4 bytes 08010d91
+ 0098a6e4 bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73252700d55c6e7a9b96d95cf5a3de2b"></a>

### [`0098a6f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a6f4.md) → [`0098a6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098a/0098a6f4.md) FUN_0098a6f4

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
      "definition_site": "0098a6f8",
      "incomplete_value": false,
      "site": "0098a6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098a6f8",
      "incomplete_value": false,
      "site": "0098a6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
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
      "0098a6fc",
      "DATA",
      [
        "storage",
        "00c0b340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098a6fc",
      "DATA",
      [
        "storage",
        "00c0b3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098a6f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a6f4.md#insn-0098a6f8)
- 新版 `0098a6f8`（命令位置の公開資料なし）

~~~diff
- 0098a6f8 ["COPY", "tmp:0:8", ["const:340:8"]]
- 0098a6f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098a6f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098a6f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098a6f8 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 0098a6f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098a6f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098a6f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098a6f8 bytes 08010d91
+ 0098a6f8 bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea600c45f095b62c83a5883e57b77541"></a>

### [`0098a83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a83c.md) → [`0098a83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098a/0098a83c.md) FUN_0098a83c

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
      "definition_site": "0098a850",
      "incomplete_value": false,
      "site": "0098a854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098a850",
      "incomplete_value": false,
      "site": "0098a854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "0098a854",
      "DATA",
      [
        "storage",
        "00c0b450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098a854",
      "DATA",
      [
        "storage",
        "00c0b500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098a850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a83c.md#insn-0098a850)
- 新版 `0098a850`（命令位置の公開資料なし）

~~~diff
- 0098a850 ["COPY", "tmp:0:8", ["const:450:8"]]
- 0098a850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098a850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098a850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098a850 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0098a850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098a850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098a850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098a850 bytes 08411191
+ 0098a850 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bced69b7231999e608c499febceee93a"></a>

### [`0098a860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a860.md) → [`0098a860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098a/0098a860.md) FUN_0098a860

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
      "definition_site": "0098a864",
      "incomplete_value": false,
      "site": "0098a868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098a864",
      "incomplete_value": false,
      "site": "0098a868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "0098a868",
      "DATA",
      [
        "storage",
        "00c0b450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098a868",
      "DATA",
      [
        "storage",
        "00c0b500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098a864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a860.md#insn-0098a864)
- 新版 `0098a864`（命令位置の公開資料なし）

~~~diff
- 0098a864 ["COPY", "tmp:0:8", ["const:450:8"]]
- 0098a864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098a864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098a864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098a864 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0098a864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098a864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098a864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098a864 bytes 08411191
+ 0098a864 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04451592422c26b8bbe18fa129c06704"></a>

### [`0098a8ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a8ac.md) → [`0098a8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098a/0098a8ac.md) FUN_0098a8ac

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
      "definition_site": "0098a8d0",
      "incomplete_value": false,
      "site": "0098a8d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098a8d0",
      "incomplete_value": false,
      "site": "0098a8d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "0098a8d0",
      "DATA",
      [
        "storage",
        "00c0b4d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098a8d0",
      "DATA",
      [
        "storage",
        "00c0b580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098a8cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a8ac.md#insn-0098a8cc)
- 新版 `0098a8cc`（命令位置の公開資料なし）

~~~diff
- 0098a8cc ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 0098a8cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098a8cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098a8cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098a8cc ["COPY", "tmp:0:8", ["const:580:8"]]
+ 0098a8cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098a8cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098a8cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098a8cc bytes 08411391
+ 0098a8cc bytes 08011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adf6f8d96c5330a4e5ec4739c5faede6"></a>

### [`0098a8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a8e0.md) → [`0098a8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098a/0098a8e0.md) FUN_0098a8e0

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
      "definition_site": "0098a8ec",
      "incomplete_value": false,
      "site": "0098a8ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098a8ec",
      "incomplete_value": false,
      "site": "0098a8ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "0098a8ec",
      "DATA",
      [
        "storage",
        "00c0b4d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098a8ec",
      "DATA",
      [
        "storage",
        "00c0b580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098a8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a8e0.md#insn-0098a8e8)
- 新版 `0098a8e8`（命令位置の公開資料なし）

~~~diff
- 0098a8e8 ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 0098a8e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0098a8e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0098a8e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0098a8e8 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 0098a8e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0098a8e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0098a8e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0098a8e8 bytes 29411391
+ 0098a8e8 bytes 29011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ad2366c0a3b19637342445f766465dc"></a>

### [`0098a8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a8fc.md) → [`0098a8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098a/0098a8fc.md) FUN_0098a8fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 24件 [`0043eba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043eba8.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0062d9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062d/0062d9b8.md) [`0062d9bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062d/0062d9bc.md)
- 新版 呼出元 0件  · 呼出先 24件 [`0043eba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043eba8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0062d9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d9b8.md) [`0062d9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d9bc.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.31% / 新版 93.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0098a9ec",
      "incomplete_value": true,
      "site": "0098a9f4",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098a9ec",
      "incomplete_value": true,
      "site": "0098a9f4",
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
            "const:550:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0098abb8",
      "incomplete_value": false,
      "site": "0098abbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098abb8",
      "incomplete_value": false,
      "site": "0098abbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:210:8"
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0098ac1c",
      "incomplete_value": true,
      "site": "0098ac2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:15d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098ac1c",
      "incomplete_value": true,
      "site": "0098ac2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d0:8"
              ]
            ]
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
      "0098a9f4",
      "DATA",
      [
        "storage",
        "00c0b550",
        null,
        "undefined *"
      ]
    ],
    [
      "0098abbc",
      "DATA",
      [
        "storage",
        "00bf6210",
        null,
        "undefined *"
      ]
    ],
    [
      "0098ac1c",
      "READ",
      [
        "storage",
        "002950d0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0098a9f4",
      "DATA",
      [
        "storage",
        "00c0b600",
        null,
        "undefined *"
      ]
    ],
    [
      "0098abbc",
      "DATA",
      [
        "storage",
        "00bf62c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0098ac1c",
      "READ",
      [
        "storage",
        "0029515d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098a9ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a8fc.md#insn-0098a9ec) · [`0098a9f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098a8fc.md#insn-0098a9f0)
- 新版 `0098a9ec`（命令位置の公開資料なし） · `0098a9f0`（命令位置の公開資料なし）

~~~diff
- 0098a9ec ["COPY", "tmp:0:8", ["const:550:8"]]
- 0098a9ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098a9ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098a9ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098a9ec ["COPY", "tmp:0:8", ["const:600:8"]]
+ 0098a9ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098a9ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098a9ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098a9ec bytes 08411591
+ 0098a9ec bytes 08011891
- 0098a9f0 ["COPY", "tmp:0:8", ["const:40:8"]]
- 0098a9f0 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 0098a9f0 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 0098a9f0 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 0098a9f0 bytes f3030191
+ 0098a9f0 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 0098a9f0 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
+ 0098a9f0 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
+ 0098a9f0 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
+ 0098a9f0 bytes f3030191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb83c38102548f49288a13b0f0497412"></a>

### [`0098afb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098afb0.md) → [`0098afb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098a/0098afb0.md) FUN_0098afb0

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
      "definition_site": "0098afb4",
      "incomplete_value": false,
      "site": "0098afb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098afb4",
      "incomplete_value": false,
      "site": "0098afb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "0098afb8",
      "DATA",
      [
        "storage",
        "00c0b550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098afb8",
      "DATA",
      [
        "storage",
        "00c0b600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098afb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098a/0098afb0.md#insn-0098afb4)
- 新版 `0098afb4`（命令位置の公開資料なし）

~~~diff
- 0098afb4 ["COPY", "tmp:0:8", ["const:550:8"]]
- 0098afb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098afb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098afb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098afb4 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 0098afb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098afb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098afb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098afb4 bytes 08411591
+ 0098afb4 bytes 08011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b310209731fe7d22ebe2e61238147c92"></a>

### [`0098b03c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b03c.md) → [`0098b03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098b/0098b03c.md) FUN_0098b03c

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
      "definition_site": "0098b050",
      "incomplete_value": false,
      "site": "0098b054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098b050",
      "incomplete_value": false,
      "site": "0098b054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
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
      "0098b054",
      "DATA",
      [
        "storage",
        "00c0b5d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098b054",
      "DATA",
      [
        "storage",
        "00c0b680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098b050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b03c.md#insn-0098b050)
- 新版 `0098b050`（命令位置の公開資料なし）

~~~diff
- 0098b050 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 0098b050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098b050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098b050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098b050 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 0098b050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098b050 bytes 08411791
+ 0098b050 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c3157598247635bc7567ea21d0ca4a1"></a>

### [`0098b060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b060.md) → [`0098b060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098b/0098b060.md) FUN_0098b060

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
      "definition_site": "0098b064",
      "incomplete_value": false,
      "site": "0098b068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098b064",
      "incomplete_value": false,
      "site": "0098b068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
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
      "0098b068",
      "DATA",
      [
        "storage",
        "00c0b5d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098b068",
      "DATA",
      [
        "storage",
        "00c0b680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b060.md#insn-0098b064)
- 新版 `0098b064`（命令位置の公開資料なし）

~~~diff
- 0098b064 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 0098b064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098b064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098b064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098b064 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 0098b064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098b064 bytes 08411791
+ 0098b064 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d3c651dbbcc5bad07b45118bab78b16"></a>

### [`0098b3a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b3a8.md) → [`0098b3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098b/0098b3a8.md) FUN_0098b3a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0098b0e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b0e8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0098b0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098b/0098b0e8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0098b3b4",
      "incomplete_value": false,
      "site": "0098b3b8",
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
      "definition_site": "0098b3b4",
      "incomplete_value": false,
      "site": "0098b3b8",
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
      "0098b3b4",
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
      "0098b3b4",
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

- 旧版 [`0098b3b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b3a8.md#insn-0098b3b4)
- 新版 `0098b3b4`（命令位置の公開資料なし）

~~~diff
- 0098b3b4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0098b3b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0098b3b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0098b3b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0098b3b4 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0098b3b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0098b3b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0098b3b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0098b3b4 bytes 00280c91
+ 0098b3b4 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51b5338c1fe071fb28bc708df06312bb"></a>

### [`0098b4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b4e4.md) → [`0098b4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098b/0098b4e4.md) FUN_0098b4e4

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
      "definition_site": "0098b508",
      "incomplete_value": false,
      "site": "0098b508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098b508",
      "incomplete_value": false,
      "site": "0098b508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
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
      "0098b508",
      "DATA",
      [
        "storage",
        "00c0b650",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098b508",
      "DATA",
      [
        "storage",
        "00c0b700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098b504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b4e4.md#insn-0098b504)
- 新版 `0098b504`（命令位置の公開資料なし）

~~~diff
- 0098b504 ["COPY", "tmp:0:8", ["const:650:8"]]
- 0098b504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098b504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098b504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098b504 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 0098b504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098b504 bytes 08411991
+ 0098b504 bytes 08011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1eb83cde18844f08116c55703f09041"></a>

### [`0098b518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b518.md) → [`0098b518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098b/0098b518.md) FUN_0098b518

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
      "definition_site": "0098b524",
      "incomplete_value": false,
      "site": "0098b524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098b524",
      "incomplete_value": false,
      "site": "0098b524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
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
      "0098b524",
      "DATA",
      [
        "storage",
        "00c0b650",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098b524",
      "DATA",
      [
        "storage",
        "00c0b700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098b520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b518.md#insn-0098b520)
- 新版 `0098b520`（命令位置の公開資料なし）

~~~diff
- 0098b520 ["COPY", "tmp:0:8", ["const:650:8"]]
- 0098b520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0098b520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0098b520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0098b520 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 0098b520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0098b520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0098b520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0098b520 bytes 29411991
+ 0098b520 bytes 29011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eae1822db246e8836c1f3bd9851ed154"></a>

### [`0098b534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b534.md) → [`0098b534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098b/0098b534.md) FUN_0098b534

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 80.99% / 新版 80.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0098b5ac",
      "incomplete_value": true,
      "site": "0098b5bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d0c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098b5ac",
      "incomplete_value": true,
      "site": "0098b5bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d15:8"
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
      "definition_site": "0098b5b0",
      "incomplete_value": true,
      "site": "0098b5c0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0098b5b0",
      "incomplete_value": true,
      "site": "0098b5c0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0098b6e8",
      "incomplete_value": false,
      "site": "0098b6e8",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "definition_site": "0098b6e8",
      "incomplete_value": false,
      "site": "0098b6e8",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0098b590",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "0098b5ac",
      "READ",
      [
        "storage",
        "002a9d15",
        null,
        "string"
      ]
    ],
    [
      "0098b5b0",
      "READ",
      [
        "storage",
        "002a9d1e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0098b590",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0098b5ac",
      "READ",
      [
        "storage",
        "002a9d0c",
        null,
        "string"
      ]
    ],
    [
      "0098b5b0",
      "READ",
      [
        "storage",
        "002a9d15",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098b588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b534.md#insn-0098b588) · [`0098b58c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b534.md#insn-0098b58c) · [`0098b5a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b534.md#insn-0098b5a4)
- 新版 `0098b588`（命令位置の公開資料なし） · `0098b58c`（命令位置の公開資料なし） · `0098b5a4`（命令位置の公開資料なし）

~~~diff
- 0098b588 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0098b588 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 0098b588 bytes c81400b0
+ 0098b588 bytes c81400d0
- 0098b58c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 0098b58c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098b58c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098b58c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098b58c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0098b58c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b58c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b58c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098b58c bytes 08e13d91
+ 0098b58c bytes 08e10091
- 0098b5a4 ["COPY", "tmp:0:8", ["const:d15:8"]]
- 0098b5a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098b5a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098b5a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098b5a4 ["COPY", "tmp:0:8", ["const:d0c:8"]]
+ 0098b5a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b5a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b5a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098b5a4 bytes 08553491
+ 0098b5a4 bytes 08313491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e388a958215b9c2e6b8c12ffef1fc310"></a>

### [`0098b788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b788.md) → [`0098b788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098b/0098b788.md) FUN_0098b788

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
      "definition_site": "0098b79c",
      "incomplete_value": false,
      "site": "0098b7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098b79c",
      "incomplete_value": false,
      "site": "0098b7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "0098b7a0",
      "DATA",
      [
        "storage",
        "00c0b6e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098b7a0",
      "DATA",
      [
        "storage",
        "00c0b790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098b79c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b788.md#insn-0098b79c)
- 新版 `0098b79c`（命令位置の公開資料なし）

~~~diff
- 0098b79c ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 0098b79c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098b79c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098b79c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098b79c ["COPY", "tmp:0:8", ["const:790:8"]]
+ 0098b79c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b79c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b79c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098b79c bytes 08811b91
+ 0098b79c bytes 08411e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78a95c50a9ea9f5c39bac1cefb8ecd9c"></a>

### [`0098b7ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b7ac.md) → [`0098b7ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098b/0098b7ac.md) FUN_0098b7ac

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
      "definition_site": "0098b7b0",
      "incomplete_value": false,
      "site": "0098b7b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098b7b0",
      "incomplete_value": false,
      "site": "0098b7b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
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
      "0098b7b4",
      "DATA",
      [
        "storage",
        "00c0b6e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098b7b4",
      "DATA",
      [
        "storage",
        "00c0b790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098b7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b7ac.md#insn-0098b7b0)
- 新版 `0098b7b0`（命令位置の公開資料なし）

~~~diff
- 0098b7b0 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 0098b7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098b7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098b7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098b7b0 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 0098b7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098b7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098b7b0 bytes 08811b91
+ 0098b7b0 bytes 08411e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-066485e5b472f37c7790846cbccf6e46"></a>

### [`0098b86c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b86c.md) → [`0098b86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098b/0098b86c.md) FUN_0098b86c

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
      "definition_site": "0098b878",
      "incomplete_value": false,
      "site": "0098b878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098b878",
      "incomplete_value": false,
      "site": "0098b878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "0098b878",
      "DATA",
      [
        "storage",
        "00c0b760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098b878",
      "DATA",
      [
        "storage",
        "00c0b810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098b874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098b/0098b86c.md#insn-0098b874)
- 新版 `0098b874`（命令位置の公開資料なし）

~~~diff
- 0098b874 ["COPY", "tmp:0:8", ["const:760:8"]]
- 0098b874 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0098b874 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0098b874 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0098b874 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 0098b874 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0098b874 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0098b874 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0098b874 bytes 29811d91
+ 0098b874 bytes 29412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2acfb85613e93941f34aa39de5e32fa"></a>

### [`0098c998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098c/0098c998.md) → [`0098c998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098c/0098c998.md) FUN_0098c998

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0098ca8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098c/0098ca8c.md) · 呼出先 4件 [`0064c828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0064c/0064c828.md) [`006582c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00658/006582c8.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0098ca8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098c/0098ca8c.md) · 呼出先 4件 [`0064c828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c828.md) [`006582c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006582c8.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0098c9b0",
      "incomplete_value": false,
      "site": "0098c9b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098c9b0",
      "incomplete_value": false,
      "site": "0098c9b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "0098c9b4",
      "DATA",
      [
        "storage",
        "00c0b7e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0098c9b4",
      "DATA",
      [
        "storage",
        "00c0b890",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098c9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098c/0098c998.md#insn-0098c9b0)
- 新版 `0098c9b0`（命令位置の公開資料なし）

~~~diff
- 0098c9b0 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 0098c9b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098c9b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098c9b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098c9b0 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 0098c9b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098c9b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098c9b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098c9b0 bytes 08811f91
+ 0098c9b0 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f9a726c4fd4c26918befd0d36c16e8d"></a>

### [`0098cab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098c/0098cab0.md) → [`0098cab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098c/0098cab0.md) _INIT_194

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
      "definition_site": "0098caec",
      "incomplete_value": true,
      "site": "0098cb08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0098caec",
      "incomplete_value": true,
      "site": "0098cb08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0098cb10",
      "incomplete_value": true,
      "site": "0098cb2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0098cb10",
      "incomplete_value": true,
      "site": "0098cb2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0098cb30",
      "incomplete_value": true,
      "site": "0098cb4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0098cb30",
      "incomplete_value": true,
      "site": "0098cb4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0098caec",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0098cb10",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0098cb30",
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
      "0098caec",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0098cb10",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0098cb30",
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

- 旧版 [`0098cadc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098c/0098cab0.md#insn-0098cadc) · [`0098cae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098c/0098cab0.md#insn-0098cae4)
- 新版 `0098cadc`（命令位置の公開資料なし） · `0098cae4`（命令位置の公開資料なし）

~~~diff
- 0098cadc ["COPY", "tmp:0:8", ["const:978:8"]]
- 0098cadc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0098cadc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0098cadc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0098cadc ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 0098cadc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0098cadc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0098cadc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0098cadc bytes 73e22591
+ 0098cadc bytes 73e22891
- 0098cae4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0098cae4 bytes c9c8fff0
+ 0098cae4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0098cae4 bytes c9c8fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66d3e2c95cdf4f50e7f8b1235b3f42c9"></a>

### [`0098ce40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098c/0098ce40.md) → [`0098ce40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098c/0098ce40.md) FUN_0098ce40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.74% / 新版 97.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0098ce80",
      "incomplete_value": false,
      "site": "0098ce84",
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
      "definition_site": "0098ce80",
      "incomplete_value": false,
      "site": "0098ce84",
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
      "definition_site": "0098d048",
      "incomplete_value": true,
      "site": "0098d04c",
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
      "definition_site": "0098d048",
      "incomplete_value": true,
      "site": "0098d04c",
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
    "ordinal": 36,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0098ce84",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "0098d014",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ],
    [
      "0098d018",
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
      "0098ce84",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0098d014",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "0098d018",
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

- 旧版 [`0098ce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098c/0098ce40.md#insn-0098ce80) · [`0098d014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098c/0098ce40.md#insn-0098d014) · [`0098d018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098c/0098ce40.md#insn-0098d018)
- 新版 `0098ce80`（命令位置の公開資料なし） · `0098d014`（命令位置の公開資料なし） · `0098d018`（命令位置の公開資料なし）

~~~diff
- 0098ce80 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 0098ce80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098ce80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098ce80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098ce80 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 0098ce80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098ce80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098ce80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098ce80 bytes 08e13191
+ 0098ce80 bytes 08a13491
- 0098d014 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 0098d014 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0098d014 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 0098d014 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0098d014 bytes 086146f9
+ 0098d014 bytes 08b946f9
- 0098d018 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cc8:8"]]
- 0098d018 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0098d018 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
+ 0098d018 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 0098d018 bytes b56646f9
+ 0098d018 bytes b5be46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0b7078f769136fcfc029ea63f5ee1fc"></a>

### [`0098d74c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098d/0098d74c.md) → [`0098d74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098d/0098d74c.md) FUN_0098d74c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.51% / 新版 95.51%

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
      "definition_site": "0098d78c",
      "incomplete_value": false,
      "site": "0098d79c",
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
      "definition_site": "0098d78c",
      "incomplete_value": false,
      "site": "0098d79c",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0098d7c0",
      "incomplete_value": true,
      "site": "0098d7d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d77:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098d7c0",
      "incomplete_value": true,
      "site": "0098d7d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d71:8"
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
      "definition_site": "0098d7d4",
      "incomplete_value": true,
      "site": "0098d7d4",
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
      "definition_site": "0098d7d4",
      "incomplete_value": true,
      "site": "0098d7d4",
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
      "0098d79c",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "0098d7c0",
      "READ",
      [
        "storage",
        "002aad71",
        null,
        "string"
      ]
    ],
    [
      "0098d7c4",
      "READ",
      [
        "storage",
        "002aad80",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0098d79c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0098d7c0",
      "READ",
      [
        "storage",
        "002aad77",
        null,
        "string"
      ]
    ],
    [
      "0098d7c4",
      "READ",
      [
        "storage",
        "002aad86",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098d78c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098d/0098d74c.md#insn-0098d78c) · [`0098d7b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098d/0098d74c.md#insn-0098d7b8) · [`0098d7bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098d/0098d74c.md#insn-0098d7bc)
- 新版 `0098d78c`（命令位置の公開資料なし） · `0098d7b8`（命令位置の公開資料なし）

~~~diff
- 0098d78c ["COPY", "tmp:0:8", ["const:c78:8"]]
- 0098d78c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098d78c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098d78c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098d78c ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 0098d78c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098d78c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098d78c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098d78c bytes 08e13191
+ 0098d78c bytes 08a13491
- 0098d7b8 ["COPY", "tmp:0:8", ["const:d71:8"]]
- 0098d7b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098d7b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098d7b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098d7b8 ["COPY", "tmp:0:8", ["const:d77:8"]]
+ 0098d7b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098d7b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098d7b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098d7b8 bytes 08c53591
+ 0098d7b8 bytes 08dd3591
- 0098d7bc ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0098d7bc bytes 09c9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ed6b07321064e068848eab17f565a5d"></a>

### [`0098dd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098d/0098dd80.md) → [`0098dd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098d/0098dd80.md) FUN_0098dd80

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009903e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00990/009903e4.md) · 呼出先 45件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00574810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574810.md) [`005748a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/005748a0.md)
- 新版 呼出元 1件 [`009903e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00990/009903e4.md) · 呼出先 45件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00574810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574810.md) [`005748a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005748a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.63% / 新版 99.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0098e53c",
      "incomplete_value": true,
      "site": "0098e554",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098e53c",
      "incomplete_value": true,
      "site": "0098e554",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f22:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 94,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0098f314",
      "incomplete_value": true,
      "site": "0098f320",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098f314",
      "incomplete_value": true,
      "site": "0098f320",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f22:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 212,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0098e53c",
      "READ",
      [
        "storage",
        "002abf22",
        null,
        "string"
      ]
    ],
    [
      "0098f314",
      "READ",
      [
        "storage",
        "002abf22",
        null,
        "string"
      ]
    ],
    [
      "0098f88c",
      "READ",
      [
        "storage",
        "00c1b628",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0098e53c",
      "READ",
      [
        "storage",
        "002abf28",
        null,
        "string"
      ]
    ],
    [
      "0098f314",
      "READ",
      [
        "storage",
        "002abf28",
        null,
        "string"
      ]
    ],
    [
      "0098f88c",
      "READ",
      [
        "storage",
        "00c1b6d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098e538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098d/0098dd80.md#insn-0098e538) · [`0098f310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098d/0098dd80.md#insn-0098f310) · [`0098f88c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098d/0098dd80.md#insn-0098f88c)
- 新版 `0098e538`（命令位置の公開資料なし） · `0098f310`（命令位置の公開資料なし） · `0098f88c`（命令位置の公開資料なし）

~~~diff
- 0098e538 ["COPY", "tmp:0:8", ["const:f22:8"]]
- 0098e538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098e538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098e538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098e538 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 0098e538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098e538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098e538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098e538 bytes 08893c91
+ 0098e538 bytes 08a13c91
- 0098f310 ["COPY", "tmp:0:8", ["const:f22:8"]]
- 0098f310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098f310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098f310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098f310 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 0098f310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098f310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098f310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098f310 bytes 08893c91
+ 0098f310 bytes 08a13c91
- 0098f88c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:628:8"]]
- 0098f88c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0098f88c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:6d8:8"]]
+ 0098f88c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 0098f88c bytes 181743f9
+ 0098f88c bytes 186f43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3083e0cc65d4f7aba795f971b2ec0c26"></a>

### [`009903e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00990/009903e4.md) → [`009903e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00990/009903e4.md) FUN_009903e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0094f7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094f/0094f7d0.md) · 呼出先 20件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00469fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469fac.md) [`0059d12c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059d/0059d12c.md)
- 新版 呼出元 1件 [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) · 呼出先 20件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.79% / 新版 99.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00990e58",
      "incomplete_value": true,
      "site": "00990e58",
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
      "definition_site": "00990e58",
      "incomplete_value": true,
      "site": "00990e58",
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
    "ordinal": 161,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00990e44",
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
      "00990e44",
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

- 旧版 [`00990e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00990/009903e4.md#insn-00990e38)
- 新版 `00990e38`（命令位置の公開資料なし）

~~~diff
- 00990e38 ["COPY", "tmp:0:8", ["const:135:8"]]
- 00990e38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00990e38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00990e38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00990e38 ["COPY", "tmp:0:8", ["const:a1:8"]]
+ 00990e38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00990e38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00990e38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00990e38 bytes 29d50491
+ 00990e38 bytes 29850291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79152cdedc47efe2a614b0c1d754927d"></a>

### [`00992e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00992/00992e38.md) → [`00992e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00992/00992e38.md) FUN_00992e38

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0098ce40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098c/0098ce40.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0098ce40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098c/0098ce40.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00992e44",
      "incomplete_value": false,
      "site": "00992e48",
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
      "definition_site": "00992e44",
      "incomplete_value": false,
      "site": "00992e48",
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
      "00992e44",
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
      "00992e44",
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

- 旧版 [`00992e44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00992/00992e38.md#insn-00992e44)
- 新版 `00992e44`（命令位置の公開資料なし）

~~~diff
- 00992e44 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00992e44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00992e44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00992e44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00992e44 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00992e44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00992e44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00992e44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00992e44 bytes 00280c91
+ 00992e44 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fec6dded6e72ebce344eb33f4ca9d49"></a>

### [`00992f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00992/00992f28.md) → [`00992f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00992/00992f28.md) FUN_00992f28

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0098dd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098d/0098dd80.md) [`0099a654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0099a/0099a654.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 2件 [`0098dd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098d/0098dd80.md) [`0099a654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0099a/0099a654.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "00992f34",
      "incomplete_value": false,
      "site": "00992f38",
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
      "definition_site": "00992f34",
      "incomplete_value": false,
      "site": "00992f38",
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
      "00992f34",
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
      "00992f34",
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

- 旧版 [`00992f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00992/00992f28.md#insn-00992f34)
- 新版 `00992f34`（命令位置の公開資料なし）

~~~diff
- 00992f34 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00992f34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00992f34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00992f34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00992f34 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00992f34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00992f34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00992f34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00992f34 bytes 00280c91
+ 00992f34 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb547e8ff501e3409e7d35ad70a9c55a"></a>

### [`00992f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00992/00992f3c.md) → [`00992f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00992/00992f3c.md) FUN_00992f3c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0098dd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0098d/0098dd80.md) [`00992f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00992/00992f3c.md) [`0099a654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0099a/0099a654.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`0098dd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0098d/0098dd80.md) [`00992f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00992/00992f3c.md) [`0099a654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0099a/0099a654.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.92% / 新版 98.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00993090",
      "incomplete_value": false,
      "site": "00993098",
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
    "old": {
      "definition_site": "00993090",
      "incomplete_value": false,
      "site": "00993098",
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
            "const:311:8"
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
      "definition_site": "009931e8",
      "incomplete_value": false,
      "site": "009931f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:2ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009931e8",
      "incomplete_value": false,
      "site": "009931f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:2f5:8"
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
      "definition_site": "00993290",
      "incomplete_value": false,
      "site": "0099329c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00993290",
      "incomplete_value": false,
      "site": "0099329c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7da:8"
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
      "00993090",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "009931e8",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00993290",
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00993090",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "009931e8",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00993290",
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00993090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00992/00992f3c.md#insn-00993090) · [`009931e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00992/00992f3c.md#insn-009931e8) · [`00993290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00992/00992f3c.md#insn-00993290)
- 新版 `00993090`（命令位置の公開資料なし） · `009931e8`（命令位置の公開資料なし） · `00993290`（命令位置の公開資料なし）

~~~diff
- 00993090 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00993090 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00993090 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00993090 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00993090 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00993090 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00993090 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00993090 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00993090 bytes 21440c91
+ 00993090 bytes 21280c91
- 009931e8 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 009931e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009931e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009931e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009931e8 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 009931e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009931e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009931e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009931e8 bytes 21d40b91
+ 009931e8 bytes 21b80b91
- 00993290 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00993290 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00993290 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00993290 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00993290 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00993290 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00993290 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00993290 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00993290 bytes 21681f91
+ 00993290 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a879d5b60467bffcbd3c6811b5b0bee"></a>

### [`0099373c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00993/0099373c.md) → [`0099373c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00993/0099373c.md) FUN_0099373c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00992f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00992/00992f3c.md) [`0099373c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00993/0099373c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00992f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00992/00992f3c.md) [`0099373c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00993/0099373c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0099388c",
      "incomplete_value": false,
      "site": "00993894",
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
    "old": {
      "definition_site": "0099388c",
      "incomplete_value": false,
      "site": "00993894",
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
            "const:311:8"
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
      "definition_site": "00993a8c",
      "incomplete_value": false,
      "site": "00993a98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00993a8c",
      "incomplete_value": false,
      "site": "00993a98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7da:8"
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
      "definition_site": "00993ca0",
      "incomplete_value": false,
      "site": "00993cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:672:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00993ca0",
      "incomplete_value": false,
      "site": "00993cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5e5:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0099388c",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "009939e4",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00993a8c",
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0099388c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "009939e4",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00993a8c",
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0099388c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00993/0099373c.md#insn-0099388c) · [`009939e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00993/0099373c.md#insn-009939e4) · [`00993a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00993/0099373c.md#insn-00993a8c)
- 新版 `0099388c`（命令位置の公開資料なし） · `009939e4`（命令位置の公開資料なし） · `00993a8c`（命令位置の公開資料なし）

~~~diff
- 0099388c ["COPY", "tmp:0:8", ["const:311:8"]]
- 0099388c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0099388c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0099388c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0099388c ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0099388c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0099388c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0099388c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0099388c bytes 21440c91
+ 0099388c bytes 21280c91
- 009939e4 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 009939e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009939e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009939e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009939e4 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 009939e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009939e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009939e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009939e4 bytes 21d40b91
+ 009939e4 bytes 21b80b91
- 00993a8c ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00993a8c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00993a8c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00993a8c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00993a8c ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00993a8c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00993a8c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00993a8c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00993a8c bytes 21681f91
+ 00993a8c bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7218b639258ebe85a7f1ef5751713da"></a>

### [`009965ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/009965ec.md) → [`009965ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/009965ec.md) _INIT_195

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0099668c",
      "incomplete_value": true,
      "site": "009966a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0099668c",
      "incomplete_value": true,
      "site": "009966a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009966a8",
      "incomplete_value": true,
      "site": "009966c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009966a8",
      "incomplete_value": true,
      "site": "009966c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009966e8",
      "incomplete_value": true,
      "site": "0099672c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009966e8",
      "incomplete_value": true,
      "site": "0099672c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:526:8"
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
      "00996628",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0099664c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0099666c",
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
      "00996628",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0099664c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0099666c",
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

- 旧版 [`00996618`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/009965ec.md#insn-00996618) · [`00996620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/009965ec.md#insn-00996620)
- 新版 `00996618`（命令位置の公開資料なし） · `00996620`（命令位置の公開資料なし）

~~~diff
- 00996618 ["COPY", "tmp:0:8", ["const:990:8"]]
- 00996618 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00996618 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00996618 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00996618 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00996618 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00996618 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00996618 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00996618 bytes 73422691
+ 00996618 bytes 73422991
- 00996620 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00996620 bytes 89c8ffb0
+ 00996620 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00996620 bytes 89c8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c80b93dde305f22ee57db636aea29ce"></a>

### [`00996b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/00996b10.md) → [`00996b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/00996b10.md) _INIT_196

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00996b4c",
      "incomplete_value": true,
      "site": "00996b68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00996b4c",
      "incomplete_value": true,
      "site": "00996b68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00996bcc",
      "incomplete_value": true,
      "site": "00996be8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00996bcc",
      "incomplete_value": true,
      "site": "00996be8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00996c0c",
      "incomplete_value": true,
      "site": "00996c50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00996c0c",
      "incomplete_value": true,
      "site": "00996c50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:526:8"
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
      "00996b4c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00996b70",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00996b90",
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
      "00996b4c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00996b70",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00996b90",
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

- 旧版 [`00996b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/00996b10.md#insn-00996b3c) · [`00996b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/00996b10.md#insn-00996b44)
- 新版 `00996b3c`（命令位置の公開資料なし） · `00996b44`（命令位置の公開資料なし）

~~~diff
- 00996b3c ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 00996b3c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00996b3c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00996b3c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00996b3c ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 00996b3c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00996b3c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00996b3c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00996b3c bytes 73a22691
+ 00996b3c bytes 73a22991
- 00996b44 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00996b44 bytes 89c8ffb0
+ 00996b44 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00996b44 bytes 89c8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d6a05d1ffc9d90d1bb14c5f507a095c"></a>

### [`00996eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/00996eec.md) → [`00996eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/00996eec.md) FUN_00996eec

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 28件 [`00647388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00647/00647388.md) [`00651720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00651/00651720.md) [`006584d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00658/006584d8.md) [`0068d484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068d/0068d484.md) [`00695904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00695/00695904.md) · 呼出先 51件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00424bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044a8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a8d8.md)
- 新版 呼出元 28件 [`00647388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00647/00647388.md) [`00651720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00651/00651720.md) [`006584d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006584d8.md) [`0068d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md) [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) · 呼出先 51件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.85% / 新版 90.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 49件, `store_destination` 49件, `store_value` 51件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0099708c",
      "incomplete_value": true,
      "site": "0099708c",
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
                "const:315:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0099708c",
      "incomplete_value": true,
      "site": "0099708c",
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
                "const:288:8"
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
      "definition_site": "009970a4",
      "incomplete_value": true,
      "site": "009970a4",
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
                "const:3e3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009970a4",
      "incomplete_value": true,
      "site": "009970a4",
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
                "const:3ea:8"
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
      "definition_site": "009970a8",
      "incomplete_value": true,
      "site": "009970a8",
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
      "definition_site": "009970a8",
      "incomplete_value": true,
      "site": "009970a8",
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
      "00997058",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00997078",
      "READ",
      [
        "storage",
        "002a0288",
        null,
        "string"
      ]
    ],
    [
      "0099709c",
      "READ",
      [
        "storage",
        "002a73ea",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00997058",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00997078",
      "READ",
      [
        "storage",
        "002a0315",
        null,
        "string"
      ]
    ],
    [
      "0099709c",
      "READ",
      [
        "storage",
        "002a73e3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00997050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/00996eec.md#insn-00997050) · [`00997054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/00996eec.md#insn-00997054) · [`00997074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/00996eec.md#insn-00997074)
- 新版 `00997050`（命令位置の公開資料なし） · `00997054`（命令位置の公開資料なし） · `00997074`（命令位置の公開資料なし）

~~~diff
- 00997050 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 00997050 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 00997050 bytes 681400b0
+ 00997050 bytes 681400d0
- 00997054 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00997054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00997054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00997054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00997054 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00997054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00997054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00997054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00997054 bytes 08e13d91
+ 00997054 bytes 08e10091
- 00997074 ["COPY", "tmp:0:8", ["const:288:8"]]
- 00997074 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00997074 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00997074 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00997074 ["COPY", "tmp:0:8", ["const:315:8"]]
+ 00997074 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00997074 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00997074 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00997074 bytes 08210a91
+ 00997074 bytes 08550c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8ff08d64a708ca25c717851226cd6f8"></a>

### [`0099a330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0099a/0099a330.md) → [`0099a330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0099a/0099a330.md) FUN_0099a330

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00abf464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abf/00abf464.md) · 呼出先 12件 [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`00465680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465680.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 12件 [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465680.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.27% / 新版 92.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0099a364",
      "incomplete_value": false,
      "site": "0099a36c",
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
      "definition_site": "0099a364",
      "incomplete_value": false,
      "site": "0099a36c",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0099a390",
      "incomplete_value": true,
      "site": "0099a390",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:fea:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0099a390",
      "incomplete_value": true,
      "site": "0099a390",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:ff3:8"
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
      "definition_site": "0099a454",
      "incomplete_value": true,
      "site": "0099a454",
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
                "const:296000:8"
              ],
              [
                "leaf",
                "const:276:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0099a454",
      "incomplete_value": true,
      "site": "0099a454",
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
                "const:296000:8"
              ],
              [
                "leaf",
                "const:1e9:8"
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
      "0099a36c",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "0099a384",
      "READ",
      [
        "storage",
        "002acff3",
        null,
        "string"
      ]
    ],
    [
      "0099a444",
      "READ",
      [
        "storage",
        "002961e9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0099a36c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0099a384",
      "READ",
      [
        "storage",
        "002acfea",
        null,
        "string"
      ]
    ],
    [
      "0099a444",
      "READ",
      [
        "storage",
        "00296276",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0099a364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0099a/0099a330.md#insn-0099a364) · [`0099a380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0099a/0099a330.md#insn-0099a380) · [`0099a43c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0099a/0099a330.md#insn-0099a43c)
- 新版 `0099a364`（命令位置の公開資料なし） · `0099a380`（命令位置の公開資料なし） · `0099a43c`（命令位置の公開資料なし）

~~~diff
- 0099a364 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 0099a364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0099a364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0099a364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0099a364 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 0099a364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0099a364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0099a364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0099a364 bytes 08e13191
+ 0099a364 bytes 08a13491
- 0099a380 ["COPY", "tmp:0:8", ["const:ff3:8"]]
- 0099a380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0099a380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0099a380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0099a380 ["COPY", "tmp:0:8", ["const:fea:8"]]
+ 0099a380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0099a380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0099a380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0099a380 bytes 08cd3f91
+ 0099a380 bytes 08a93f91
- 0099a43c ["COPY", "tmp:0:8", ["const:1e9:8"]]
- 0099a43c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0099a43c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0099a43c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0099a43c ["COPY", "tmp:0:8", ["const:276:8"]]
+ 0099a43c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0099a43c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0099a43c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0099a43c bytes 29a50791
+ 0099a43c bytes 29d90991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

