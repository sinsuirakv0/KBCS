# v15.7.2 → v15.7.3 · 最優先の変更候補 (3)

[一覧の目次](README.md)

<a id="compare-2d125d249fa4808d77d5213b1a1a5ca7"></a>

### [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) → [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) FUN_004377fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 20件 [`00430b04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430b04.md) [`0043c164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c164.md) [`0043cc04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cc04.md) [`00515468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00515/00515468.md) [`00515718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00515/00515718.md) · 呼出先 5件 [`00b7c6bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c6bc.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdb3c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 20件 [`00430b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430b04.md) [`0043c164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c164.md) [`0043cc04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cc04.md) [`00515468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515468.md) [`00515718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515718.md) · 呼出先 5件 [`00b7c784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c784.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb470.md) [`00bdb480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb480.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00437838",
      "incomplete_value": true,
      "site": "00437840",
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437838",
      "incomplete_value": true,
      "site": "00437840",
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
                "const:d68:8"
              ]
            ]
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
      "definition_site": "0043783c",
      "incomplete_value": true,
      "site": "00437840",
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043783c",
      "incomplete_value": true,
      "site": "00437840",
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
                "const:d78:8"
              ]
            ]
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
      "00437838",
      "READ",
      [
        "storage",
        "00c1ad68",
        null,
        "pointer"
      ]
    ],
    [
      "00437838",
      "PARAM",
      [
        "storage",
        "00c12e08",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0043783c",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00437838",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "00437838",
      "PARAM",
      [
        "storage",
        "00c12eb8",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0043783c",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md#insn-00437838) · [`0043783c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md#insn-0043783c)
- 新版 `00437838`（命令位置の公開資料なし） · `0043783c`（命令位置の公開資料なし）

~~~diff
- 00437838 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d68:8"]]
- 00437838 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00437838 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
+ 00437838 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00437838 bytes 21b446f9
+ 00437838 bytes 210c47f9
- 0043783c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:d78:8"]]
- 0043783c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043783c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e28:8"]]
+ 0043783c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 0043783c bytes 42bc46f9
+ 0043783c bytes 421447f9
~~~


<a id="compare-1b56a8b92b7c85423225a0bbb5055b0d"></a>

### [`0043785c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/0043785c.md) → [`0043785c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/0043785c.md) FUN_0043785c

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
      "definition_site": "00437870",
      "incomplete_value": false,
      "site": "00437874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437870",
      "incomplete_value": false,
      "site": "00437874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "00437874",
      "DATA",
      [
        "storage",
        "00be6840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00437874",
      "DATA",
      [
        "storage",
        "00be68f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/0043785c.md#insn-00437870)
- 新版 `00437870`（命令位置の公開資料なし）

~~~diff
- 00437870 ["COPY", "tmp:0:8", ["const:840:8"]]
- 00437870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00437870 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 00437870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00437870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00437870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437870 bytes 08012191
+ 00437870 bytes 08c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51b76ffe73a062930aa6a7124650e6ea"></a>

### [`00437880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437880.md) → [`00437880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437880.md) FUN_00437880

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
      "definition_site": "00437884",
      "incomplete_value": false,
      "site": "00437888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437884",
      "incomplete_value": false,
      "site": "00437888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "00437888",
      "DATA",
      [
        "storage",
        "00be6840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00437888",
      "DATA",
      [
        "storage",
        "00be68f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437880.md#insn-00437884)
- 新版 `00437884`（命令位置の公開資料なし）

~~~diff
- 00437884 ["COPY", "tmp:0:8", ["const:840:8"]]
- 00437884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00437884 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 00437884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00437884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00437884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437884 bytes 08012191
+ 00437884 bytes 08c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9430a97465562319621237870d87f6f"></a>

### [`00437898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437898.md) → [`00437898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437898.md) FUN_00437898

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00573e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00573/00573e38.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00573e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573e38.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.72% / 新版 91.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004379c4",
      "incomplete_value": true,
      "site": "004379c4",
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004379c4",
      "incomplete_value": true,
      "site": "004379c4",
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004379b8",
      "incomplete_value": true,
      "site": "004379c4",
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
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004379b8",
      "incomplete_value": true,
      "site": "004379c4",
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
                "const:ad8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00437a34",
      "incomplete_value": true,
      "site": "00437a34",
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
                "const:58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437a34",
      "incomplete_value": true,
      "site": "00437a34",
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
                "const:58:8"
              ]
            ]
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
      "004379a8",
      "READ",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "004379b8",
      "READ",
      [
        "storage",
        "00c24ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "004379d4",
      "READ",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004379a8",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "004379b8",
      "READ",
      [
        "storage",
        "00c24b98",
        null,
        "undefined8"
      ]
    ],
    [
      "004379d4",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004379a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437898.md#insn-004379a4) · [`004379b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437898.md#insn-004379b8) · [`004379d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437898.md#insn-004379d0)
- 新版 `004379a4`（命令位置の公開資料なし） · `004379b8`（命令位置の公開資料なし） · `004379d0`（命令位置の公開資料なし）

~~~diff
- 004379a4 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 004379a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004379a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004379a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004379a4 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 004379a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004379a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004379a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004379a4 bytes 08812b91
+ 004379a4 bytes 08812e91
- 004379b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ad8:8"]]
- 004379b8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 004379b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b98:8"]]
+ 004379b8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 004379b8 bytes 006d45f9
+ 004379b8 bytes 00cd45f9
- 004379d0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 004379d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004379d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004379d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004379d0 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 004379d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004379d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004379d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004379d0 bytes 08812b91
+ 004379d0 bytes 08812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8749502bd2df864ae063ecc14ad8c5d0"></a>

### [`00437bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437bb4.md) → [`00437bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437bb4.md) FUN_00437bb4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0042eef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eef4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0042eef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eef4.md)

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
      "definition_site": "00437bbc",
      "incomplete_value": false,
      "site": "00437bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437bbc",
      "incomplete_value": false,
      "site": "00437bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "00437bbc",
      "DATA",
      [
        "storage",
        "00be68c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00437bbc",
      "DATA",
      [
        "storage",
        "00be6970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437bb4.md#insn-00437bb8)
- 新版 `00437bb8`（命令位置の公開資料なし）

~~~diff
- 00437bb8 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00437bb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437bb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437bb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00437bb8 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00437bb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00437bb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00437bb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437bb8 bytes 08012391
+ 00437bb8 bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e137397d75d0c781eaed0cf0ba1865c8"></a>

### [`00437bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437bc4.md) → [`00437bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437bc4.md) FUN_00437bc4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0042eef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eef4.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0042eef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eef4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00437bdc",
      "incomplete_value": false,
      "site": "00437bdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437bdc",
      "incomplete_value": false,
      "site": "00437bdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "00437bdc",
      "DATA",
      [
        "storage",
        "00be68c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00437bdc",
      "DATA",
      [
        "storage",
        "00be6970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437bd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437bc4.md#insn-00437bd4)
- 新版 `00437bd4`（命令位置の公開資料なし）

~~~diff
- 00437bd4 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00437bd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437bd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00437bd4 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00437bd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00437bd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00437bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437bd4 bytes 08012391
+ 00437bd4 bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-660b73aa45232ea705850c636ca06d75"></a>

### [`00437bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437bf4.md) → [`00437bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437bf4.md) FUN_00437bf4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00438418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438418.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00438418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438418.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00437c18",
      "incomplete_value": false,
      "site": "00437c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437c18",
      "incomplete_value": false,
      "site": "00437c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "00437c18",
      "DATA",
      [
        "storage",
        "00be68c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00437c18",
      "DATA",
      [
        "storage",
        "00be6970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437bf4.md#insn-00437c14)
- 新版 `00437c14`（命令位置の公開資料なし）

~~~diff
- 00437c14 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00437c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00437c14 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00437c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00437c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00437c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437c14 bytes 08012391
+ 00437c14 bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8529235cc275d4bd3aa3e3c537c4bce9"></a>

### [`00437c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437c48.md) → [`00437c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437c48.md) FUN_00437c48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00438418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438418.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00438418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438418.md)

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
      "definition_site": "00437c54",
      "incomplete_value": false,
      "site": "00437c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437c54",
      "incomplete_value": false,
      "site": "00437c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "00437c54",
      "DATA",
      [
        "storage",
        "00be68c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00437c54",
      "DATA",
      [
        "storage",
        "00be6970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437c48.md#insn-00437c50)
- 新版 `00437c50`（命令位置の公開資料なし）

~~~diff
- 00437c50 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00437c50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00437c50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00437c50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00437c50 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00437c50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00437c50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00437c50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00437c50 bytes 29012391
+ 00437c50 bytes 29c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dd7afe99335e3309bff39b5c8ef5498"></a>

### [`00437c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437c94.md) → [`00437c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437c94.md) FUN_00437c94

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0042d878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d878.md) [`0042fd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042fd7c.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`004389d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/004389d4.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042d878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d878.md) [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`004389d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/004389d4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00437f7c",
      "incomplete_value": false,
      "site": "00437f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437f7c",
      "incomplete_value": false,
      "site": "00437f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00438074",
      "incomplete_value": false,
      "site": "00438088",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438074",
      "incomplete_value": false,
      "site": "00438088",
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
            "const:ad8:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00438204",
      "incomplete_value": false,
      "site": "00438208",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438204",
      "incomplete_value": false,
      "site": "00438208",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00437e14",
      "READ",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "00437f7c",
      "DATA",
      [
        "storage",
        "00be6930",
        null,
        "undefined *"
      ]
    ],
    [
      "00438074",
      "PARAM",
      [
        "storage",
        "00c24ad8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00437e14",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00437f7c",
      "DATA",
      [
        "storage",
        "00be69e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00438074",
      "PARAM",
      [
        "storage",
        "00c24b98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437c94.md#insn-00437e10) · [`00437f74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437c94.md#insn-00437f74) · [`00437f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437c94.md#insn-00437f78)
- 新版 `00437e10`（命令位置の公開資料なし） · `00437f74`（命令位置の公開資料なし）

~~~diff
- 00437e10 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00437e10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437e10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437e10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00437e10 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 00437e10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00437e10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00437e10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437e10 bytes 08812b91
+ 00437e10 bytes 08812e91
- 00437f74 ["COPY", "tmp:0:8", ["const:930:8"]]
- 00437f74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00437f74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00437f74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00437f74 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00437f74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00437f74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00437f74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00437f74 bytes 29c12491
+ 00437f74 bytes 29812791
- 00437f78 ["COPY", "register:40b0:8", ["register:4000:8"]]
- 00437f78 bytes f60300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-730d22f1dc726d84bc36c2d8850486a6"></a>

### [`00438788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438788.md) → [`00438788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438788.md) FUN_00438788

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004387a0",
      "incomplete_value": false,
      "site": "004387ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004387a0",
      "incomplete_value": false,
      "site": "004387ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "004387ac",
      "DATA",
      [
        "storage",
        "00be6930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004387ac",
      "DATA",
      [
        "storage",
        "00be69e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004387a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438788.md#insn-004387a0)
- 新版 `004387a0`（命令位置の公開資料なし）

~~~diff
- 004387a0 ["COPY", "tmp:0:8", ["const:930:8"]]
- 004387a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004387a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004387a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004387a0 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 004387a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004387a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004387a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004387a0 bytes 08c12491
+ 004387a0 bytes 08812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1895e432b54d9e511f37ea605e0b2e1d"></a>

### [`00438874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438874.md) → [`00438874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438874.md) FUN_00438874

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043888c",
      "incomplete_value": false,
      "site": "00438898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043888c",
      "incomplete_value": false,
      "site": "00438898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "00438898",
      "DATA",
      [
        "storage",
        "00be6930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00438898",
      "DATA",
      [
        "storage",
        "00be69e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043888c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438874.md#insn-0043888c)
- 新版 `0043888c`（命令位置の公開資料なし）

~~~diff
- 0043888c ["COPY", "tmp:0:8", ["const:930:8"]]
- 0043888c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043888c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043888c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043888c ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 0043888c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043888c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043888c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043888c bytes 08c12491
+ 0043888c bytes 08812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57e41199f581102128868161348f4c58"></a>

### [`0043895c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/0043895c.md) → [`0043895c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/0043895c.md) FUN_0043895c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00438c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00438c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00438980",
      "incomplete_value": false,
      "site": "00438980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438980",
      "incomplete_value": false,
      "site": "00438980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "00438980",
      "DATA",
      [
        "storage",
        "00be6930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00438980",
      "DATA",
      [
        "storage",
        "00be69e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043897c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/0043895c.md#insn-0043897c)
- 新版 `0043897c`（命令位置の公開資料なし）

~~~diff
- 0043897c ["COPY", "tmp:0:8", ["const:930:8"]]
- 0043897c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043897c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043897c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043897c ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 0043897c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043897c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043897c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043897c bytes 08c12491
+ 0043897c bytes 08812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bead62ff32f3fcc8bda64cf09888a1d"></a>

### [`004389b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/004389b0.md) → [`004389b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/004389b0.md) FUN_004389b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00438c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438c24.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00438c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438c24.md)

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
      "definition_site": "004389bc",
      "incomplete_value": false,
      "site": "004389bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004389bc",
      "incomplete_value": false,
      "site": "004389bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "004389bc",
      "DATA",
      [
        "storage",
        "00be6930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004389bc",
      "DATA",
      [
        "storage",
        "00be69e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004389b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/004389b0.md#insn-004389b8)
- 新版 `004389b8`（命令位置の公開資料なし）

~~~diff
- 004389b8 ["COPY", "tmp:0:8", ["const:930:8"]]
- 004389b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004389b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004389b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004389b8 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 004389b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004389b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004389b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004389b8 bytes 29c12491
+ 004389b8 bytes 29812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c39e77d862a7e5b713c15f3b63468f51"></a>

### [`004389fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/004389fc.md) → [`004389fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/004389fc.md) FUN_004389fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0073a038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a038.md) [`0073eb44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073eb44.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md) [`0073eb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073eb44.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.12% / 新版 96.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00438b64",
      "incomplete_value": false,
      "site": "00438b68",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438b64",
      "incomplete_value": false,
      "site": "00438b68",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00438b74",
      "incomplete_value": false,
      "site": "00438b78",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438b74",
      "incomplete_value": false,
      "site": "00438b78",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00438a44",
      "READ",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "00438b64",
      "PARAM",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "00438b74",
      "PARAM",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00438a44",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00438b64",
      "PARAM",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00438b74",
      "PARAM",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/004389fc.md#insn-00438a40) · [`00438b64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/004389fc.md#insn-00438b64) · [`00438b74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/004389fc.md#insn-00438b74)
- 新版 `00438a40`（命令位置の公開資料なし） · `00438b64`（命令位置の公開資料なし） · `00438b74`（命令位置の公開資料なし）

~~~diff
- 00438a40 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00438a40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00438a40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00438a40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00438a40 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 00438a40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00438a40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00438a40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00438a40 bytes 08812b91
+ 00438a40 bytes 08812e91
- 00438b64 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00438b64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00438b64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00438b64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00438b64 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 00438b64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00438b64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00438b64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00438b64 bytes 00802b91
+ 00438b64 bytes 00802e91
- 00438b74 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00438b74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00438b74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00438b74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00438b74 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 00438b74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00438b74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00438b74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00438b74 bytes 00802b91
+ 00438b74 bytes 00802e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6dcc1c7fd3bdf3ff9018f7b0c442fb2"></a>

### [`00438eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438eb4.md) → [`00438eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438eb4.md) FUN_00438eb4

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
      "definition_site": "00438eb8",
      "incomplete_value": false,
      "site": "00438ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438eb8",
      "incomplete_value": false,
      "site": "00438ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
      "00438ebc",
      "DATA",
      [
        "storage",
        "00be69d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00438ebc",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438eb4.md#insn-00438eb8)
- 新版 `00438eb8`（命令位置の公開資料なし）

~~~diff
- 00438eb8 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00438eb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00438eb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00438eb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00438eb8 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00438eb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00438eb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00438eb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00438eb8 bytes 08412791
+ 00438eb8 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-649278aeef0aaa965af43efdf3126f3c"></a>

### [`00438ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438ec4.md) → [`00438ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438ec4.md) FUN_00438ec4

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
      "definition_site": "00438ed4",
      "incomplete_value": false,
      "site": "00438edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438ed4",
      "incomplete_value": false,
      "site": "00438edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "00438edc",
      "DATA",
      [
        "storage",
        "00be69d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00438edc",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438ec4.md#insn-00438ed4)
- 新版 `00438ed4`（命令位置の公開資料なし）

~~~diff
- 00438ed4 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00438ed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00438ed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00438ed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00438ed4 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00438ed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00438ed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00438ed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00438ed4 bytes 08412791
+ 00438ed4 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7759bc60839c636d5a32d9531758ca3"></a>

### [`00438f04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438f04.md) → [`00438f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f04.md) FUN_00438f04

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00438f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438f54.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00438f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f54.md)

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
      "definition_site": "00438f14",
      "incomplete_value": false,
      "site": "00438f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438f14",
      "incomplete_value": false,
      "site": "00438f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
      "00438f18",
      "DATA",
      [
        "storage",
        "00be6a20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00438f18",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438f04.md#insn-00438f14)
- 新版 `00438f14`（命令位置の公開資料なし）

~~~diff
- 00438f14 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00438f14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00438f14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00438f14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00438f14 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 00438f14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00438f14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00438f14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00438f14 bytes 29812891
+ 00438f14 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71a0ed989421b5c357fb851c072cbe04"></a>

### [`00438f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438f20.md) → [`00438f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f20.md) FUN_00438f20

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`00572b04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00572/00572e44.md) [`0073cdfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073c/0073cdfc.md) [`0076e98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0076e/0076e98c.md) [`00ad0154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad0/00ad0154.md) · 呼出先 2件 [`00438f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438f54.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 5件 [`00572b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572e44.md) [`0073cdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md) [`0076e98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076e/0076e98c.md) [`00ad021c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad021c.md) · 呼出先 2件 [`00438f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f54.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00438f3c",
      "incomplete_value": false,
      "site": "00438f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438f3c",
      "incomplete_value": false,
      "site": "00438f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
      "00438f3c",
      "DATA",
      [
        "storage",
        "00be6a20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00438f3c",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438f20.md#insn-00438f34)
- 新版 `00438f34`（命令位置の公開資料なし）

~~~diff
- 00438f34 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00438f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00438f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00438f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00438f34 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 00438f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00438f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00438f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00438f34 bytes 08812891
+ 00438f34 bytes 08412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84e9f30f6b60accacdf68a37e52469e2"></a>

### [`00438fbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438fbc.md) → [`00438fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438fbc.md) FUN_00438fbc

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
      "definition_site": "00438fc8",
      "incomplete_value": false,
      "site": "00438fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438fc8",
      "incomplete_value": false,
      "site": "00438fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "00438fd4",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00438fd4",
      "DATA",
      [
        "storage",
        "00be6b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438fc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438fbc.md#insn-00438fc8)
- 新版 `00438fc8`（命令位置の公開資料なし）

~~~diff
- 00438fc8 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 00438fc8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00438fc8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00438fc8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00438fc8 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00438fc8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00438fc8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00438fc8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00438fc8 bytes 4a012a91
+ 00438fc8 bytes 4ac12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31dca73bd790cf8b011919f350ab0591"></a>

### [`00439000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439000.md) → [`00439000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439000.md) FUN_00439000

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
      "definition_site": "00439018",
      "incomplete_value": false,
      "site": "00439024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439018",
      "incomplete_value": false,
      "site": "00439024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "00439024",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439024",
      "DATA",
      [
        "storage",
        "00be6b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439000.md#insn-00439018)
- 新版 `00439018`（命令位置の公開資料なし）

~~~diff
- 00439018 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 00439018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00439018 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00439018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00439018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00439018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439018 bytes 08012a91
+ 00439018 bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c70e35d671ce116b916c6f9b25455b0e"></a>

### [`0043905c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/0043905c.md) → [`0043905c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/0043905c.md) FUN_0043905c

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
      "definition_site": "00439088",
      "incomplete_value": false,
      "site": "00439088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439088",
      "incomplete_value": false,
      "site": "00439088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "00439088",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439088",
      "DATA",
      [
        "storage",
        "00be6b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/0043905c.md#insn-00439080)
- 新版 `00439080`（命令位置の公開資料なし）

~~~diff
- 00439080 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 00439080 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439080 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439080 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00439080 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00439080 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00439080 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00439080 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439080 bytes 08012a91
+ 00439080 bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d1f8b26b0fa31ae26b2e5f778b2c4ea"></a>

### [`004390e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/004390e4.md) → [`004390e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/004390e4.md) FUN_004390e4

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
      "definition_site": "00439100",
      "incomplete_value": false,
      "site": "00439100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439100",
      "incomplete_value": false,
      "site": "00439100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "00439100",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439100",
      "DATA",
      [
        "storage",
        "00be6b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004390fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/004390e4.md#insn-004390fc)
- 新版 `004390fc`（命令位置の公開資料なし）

~~~diff
- 004390fc ["COPY", "tmp:0:8", ["const:a80:8"]]
- 004390fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004390fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004390fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004390fc ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 004390fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004390fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004390fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004390fc bytes 29012a91
+ 004390fc bytes 29c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e849a2b1a0ab89d1809f6a4e359ec65"></a>

### [`004391e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/004391e0.md) → [`004391e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/004391e0.md) FUN_004391e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.17% / 新版 98.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00439228",
      "incomplete_value": true,
      "site": "00439228",
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
      "definition_site": "00439228",
      "incomplete_value": true,
      "site": "00439228",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004393ac",
      "incomplete_value": true,
      "site": "004393c0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:292000:8"
              ],
              [
                "leaf",
                "const:6cb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004393ac",
      "incomplete_value": true,
      "site": "004393c0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:292000:8"
              ],
              [
                "leaf",
                "const:63e:8"
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
      "00439204",
      "READ",
      [
        "storage",
        "002a65e1",
        null,
        "string"
      ]
    ],
    [
      "004393ac",
      "READ",
      [
        "storage",
        "0029263e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00439204",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "004393ac",
      "READ",
      [
        "storage",
        "002926cb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004391fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/004391e0.md#insn-004391fc) · [`004393a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/004391e0.md#insn-004393a4)
- 新版 `004391fc`（命令位置の公開資料なし） · `004393a4`（命令位置の公開資料なし）

~~~diff
- 004391fc ["COPY", "tmp:0:8", ["const:5e1:8"]]
- 004391fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004391fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004391fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004391fc ["COPY", "tmp:0:8", ["const:5da:8"]]
+ 004391fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004391fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004391fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004391fc bytes 4a851791
+ 004391fc bytes 4a691791
- 004393a4 ["COPY", "tmp:0:8", ["const:63e:8"]]
- 004393a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004393a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004393a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004393a4 ["COPY", "tmp:0:8", ["const:6cb:8"]]
+ 004393a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004393a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004393a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004393a4 bytes 29f91891
+ 004393a4 bytes 292d1b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-679a2e016f657b34471f6705352231d4"></a>

### [`0043980c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/0043980c.md) → [`0043980c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/0043980c.md) FUN_0043980c

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
      "definition_site": "00439818",
      "incomplete_value": false,
      "site": "00439824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439818",
      "incomplete_value": false,
      "site": "00439824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "00439824",
      "DATA",
      [
        "storage",
        "00be6b10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439824",
      "DATA",
      [
        "storage",
        "00be6bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/0043980c.md#insn-00439818)
- 新版 `00439818`（命令位置の公開資料なし）

~~~diff
- 00439818 ["COPY", "tmp:0:8", ["const:b10:8"]]
- 00439818 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00439818 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00439818 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00439818 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00439818 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00439818 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00439818 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00439818 bytes 4a412c91
+ 00439818 bytes 4a012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fc7af9074b00ab214648bfffcc7bb54"></a>

### [`00439850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439850.md) → [`00439850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439850.md) FUN_00439850

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
      "definition_site": "00439868",
      "incomplete_value": false,
      "site": "00439874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439868",
      "incomplete_value": false,
      "site": "00439874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "00439874",
      "DATA",
      [
        "storage",
        "00be6b10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439874",
      "DATA",
      [
        "storage",
        "00be6bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439850.md#insn-00439868)
- 新版 `00439868`（命令位置の公開資料なし）

~~~diff
- 00439868 ["COPY", "tmp:0:8", ["const:b10:8"]]
- 00439868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00439868 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00439868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00439868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00439868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439868 bytes 08412c91
+ 00439868 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cee59ef767f2e4fba2aacf269124b2b"></a>

### [`004398ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/004398ac.md) → [`004398ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/004398ac.md) FUN_004398ac

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
      "definition_site": "004398d8",
      "incomplete_value": false,
      "site": "004398d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004398d8",
      "incomplete_value": false,
      "site": "004398d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "004398d8",
      "DATA",
      [
        "storage",
        "00be6b10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004398d8",
      "DATA",
      [
        "storage",
        "00be6bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004398d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/004398ac.md#insn-004398d0)
- 新版 `004398d0`（命令位置の公開資料なし）

~~~diff
- 004398d0 ["COPY", "tmp:0:8", ["const:b10:8"]]
- 004398d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004398d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004398d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004398d0 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 004398d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004398d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004398d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004398d0 bytes 08412c91
+ 004398d0 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0913ab5a266d17854d6f75fda0213be6"></a>

### [`00439934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439934.md) → [`00439934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439934.md) FUN_00439934

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
      "definition_site": "00439950",
      "incomplete_value": false,
      "site": "00439950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439950",
      "incomplete_value": false,
      "site": "00439950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "00439950",
      "DATA",
      [
        "storage",
        "00be6b10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439950",
      "DATA",
      [
        "storage",
        "00be6bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043994c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439934.md#insn-0043994c)
- 新版 `0043994c`（命令位置の公開資料なし）

~~~diff
- 0043994c ["COPY", "tmp:0:8", ["const:b10:8"]]
- 0043994c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043994c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043994c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043994c ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 0043994c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043994c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043994c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043994c bytes 29412c91
+ 0043994c bytes 29012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5afd5323c2db4ab8d57a4889a7f2de7a"></a>

### [`00439eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439eb4.md) → [`00439eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439eb4.md) FUN_00439eb4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00439bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439bc0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00439bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439bc0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00439ec0",
      "incomplete_value": false,
      "site": "00439ec4",
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
      "definition_site": "00439ec0",
      "incomplete_value": false,
      "site": "00439ec4",
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
      "00439ec0",
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
      "00439ec0",
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

- 旧版 [`00439ec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439eb4.md#insn-00439ec0)
- 新版 `00439ec0`（命令位置の公開資料なし）

~~~diff
- 00439ec0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00439ec0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00439ec0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00439ec0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00439ec0 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00439ec0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00439ec0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00439ec0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00439ec0 bytes 00280c91
+ 00439ec0 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea8f8ad20a789d1c2933e9b242aa7d33"></a>

### [`00439ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439ec8.md) → [`00439ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439ec8.md) FUN_00439ec8

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
      "definition_site": "00439ed4",
      "incomplete_value": false,
      "site": "00439ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439ed4",
      "incomplete_value": false,
      "site": "00439ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "00439ee0",
      "DATA",
      [
        "storage",
        "00be6ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439ee0",
      "DATA",
      [
        "storage",
        "00be6c50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439ec8.md#insn-00439ed4)
- 新版 `00439ed4`（命令位置の公開資料なし）

~~~diff
- 00439ed4 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00439ed4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00439ed4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00439ed4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00439ed4 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00439ed4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00439ed4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00439ed4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00439ed4 bytes 4a812e91
+ 00439ed4 bytes 4a413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9601ec25accdc3f61a93a36464f9cc1"></a>

### [`00439f0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439f0c.md) → [`00439f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439f0c.md) FUN_00439f0c

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
      "definition_site": "00439f24",
      "incomplete_value": false,
      "site": "00439f30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439f24",
      "incomplete_value": false,
      "site": "00439f30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "00439f30",
      "DATA",
      [
        "storage",
        "00be6ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439f30",
      "DATA",
      [
        "storage",
        "00be6c50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439f0c.md#insn-00439f24)
- 新版 `00439f24`（命令位置の公開資料なし）

~~~diff
- 00439f24 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00439f24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439f24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439f24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00439f24 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00439f24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00439f24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00439f24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439f24 bytes 08812e91
+ 00439f24 bytes 08413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62307a6c95f9c35e0a58b19f75cdf2f2"></a>

### [`00439f68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439f68.md) → [`00439f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439f68.md) FUN_00439f68

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
      "definition_site": "00439f94",
      "incomplete_value": false,
      "site": "00439f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439f94",
      "incomplete_value": false,
      "site": "00439f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "00439f94",
      "DATA",
      [
        "storage",
        "00be6ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439f94",
      "DATA",
      [
        "storage",
        "00be6c50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439f68.md#insn-00439f8c)
- 新版 `00439f8c`（命令位置の公開資料なし）

~~~diff
- 00439f8c ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00439f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00439f8c ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00439f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00439f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00439f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439f8c bytes 08812e91
+ 00439f8c bytes 08413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb156ce6a53c068440358cdfa3f1eb5f"></a>

### [`00439ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439ff0.md) → [`00439ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439ff0.md) FUN_00439ff0

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
      "definition_site": "0043a00c",
      "incomplete_value": false,
      "site": "0043a00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a00c",
      "incomplete_value": false,
      "site": "0043a00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "0043a00c",
      "DATA",
      [
        "storage",
        "00be6ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043a00c",
      "DATA",
      [
        "storage",
        "00be6c50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439ff0.md#insn-0043a008)
- 新版 `0043a008`（命令位置の公開資料なし）

~~~diff
- 0043a008 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 0043a008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043a008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043a008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043a008 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 0043a008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043a008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043a008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043a008 bytes 29812e91
+ 0043a008 bytes 29413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25c888885c2877cfc013354e7bf8c727"></a>

### [`0043a0ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043a0ec.md) → [`0043a0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a0ec.md) FUN_0043a0ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb190.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 2件, `store_destination` 6件, `store_value` 2件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043a140",
      "incomplete_value": true,
      "site": "0043a140",
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
      "definition_site": "0043a140",
      "incomplete_value": true,
      "site": "0043a140",
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043a270",
      "incomplete_value": true,
      "site": "0043a284",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:292000:8"
              ],
              [
                "leaf",
                "const:6cb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a270",
      "incomplete_value": true,
      "site": "0043a284",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:292000:8"
              ],
              [
                "leaf",
                "const:63e:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043a444",
      "incomplete_value": false,
      "site": "0043a444",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a444",
      "incomplete_value": false,
      "site": "0043a444",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043a10c",
      "PARAM",
      [
        "storage",
        "00c24b20",
        null,
        null
      ]
    ],
    [
      "0043a12c",
      "READ",
      [
        "storage",
        "002a65e1",
        null,
        "string"
      ]
    ],
    [
      "0043a270",
      "READ",
      [
        "storage",
        "0029263e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043a10c",
      "PARAM",
      [
        "storage",
        "00c24be0",
        null,
        null
      ]
    ],
    [
      "0043a12c",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0043a270",
      "READ",
      [
        "storage",
        "002926cb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043a0ec.md#insn-0043a444) · [`0043a63c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043a0ec.md#insn-0043a63c) · [`0043a640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043a0ec.md#insn-0043a640)
- 新版 `0043a444`（命令位置の公開資料なし） · `0043a63c`（命令位置の公開資料なし） · `0043a640`（命令位置の公開資料なし）

~~~diff
- 0043a444 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b58:8"]]
- 0043a444 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 0043a444 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
+ 0043a444 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 0043a444 bytes 14ad05f9
+ 0043a444 bytes 140d06f9
- 0043a63c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b58:8"]]
- 0043a63c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0043a63c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
+ 0043a63c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0043a63c bytes 13ad05f9
+ 0043a63c bytes 130d06f9
- 0043a640 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0043a640 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0043a640 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:b70:8"]]
- 0043a640 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0043a640 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0043a640 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0043a640 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c30:8"]]
+ 0043a640 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0043a640 bytes 3fc12d39
+ 0043a640 bytes 3fc13039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11a97350ba59871973bd8fda03b5d6f5"></a>

### [`0043a8b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043a8b8.md) → [`0043a8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a8b8.md) FUN_0043a8b8

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
      "definition_site": "0043a8c4",
      "incomplete_value": false,
      "site": "0043a8d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a8c4",
      "incomplete_value": false,
      "site": "0043a8d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "0043a8d0",
      "DATA",
      [
        "storage",
        "00be6c20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043a8d0",
      "DATA",
      [
        "storage",
        "00be6cd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043a8b8.md#insn-0043a8c4)
- 新版 `0043a8c4`（命令位置の公開資料なし）

~~~diff
- 0043a8c4 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 0043a8c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043a8c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043a8c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043a8c4 ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 0043a8c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043a8c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043a8c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043a8c4 bytes 4a813091
+ 0043a8c4 bytes 4a413391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-380e8cb14a09fef12743c6d078730424"></a>

### [`0043a8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043a8fc.md) → [`0043a8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a8fc.md) FUN_0043a8fc

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
      "definition_site": "0043a914",
      "incomplete_value": false,
      "site": "0043a920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a914",
      "incomplete_value": false,
      "site": "0043a920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "0043a920",
      "DATA",
      [
        "storage",
        "00be6c20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043a920",
      "DATA",
      [
        "storage",
        "00be6cd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043a8fc.md#insn-0043a914)
- 新版 `0043a914`（命令位置の公開資料なし）

~~~diff
- 0043a914 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 0043a914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043a914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043a914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043a914 ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 0043a914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043a914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043a914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043a914 bytes 08813091
+ 0043a914 bytes 08413391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23490349bdcf06e8e7a06430f8d5806c"></a>

### [`0043a958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043a958.md) → [`0043a958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a958.md) FUN_0043a958

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
      "definition_site": "0043a984",
      "incomplete_value": false,
      "site": "0043a984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a984",
      "incomplete_value": false,
      "site": "0043a984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "0043a984",
      "DATA",
      [
        "storage",
        "00be6c20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043a984",
      "DATA",
      [
        "storage",
        "00be6cd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a97c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043a958.md#insn-0043a97c)
- 新版 `0043a97c`（命令位置の公開資料なし）

~~~diff
- 0043a97c ["COPY", "tmp:0:8", ["const:c20:8"]]
- 0043a97c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043a97c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043a97c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043a97c ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 0043a97c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043a97c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043a97c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043a97c bytes 08813091
+ 0043a97c bytes 08413391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15752258a78c5c1ad716a3afef46453b"></a>

### [`0043a9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043a9e0.md) → [`0043a9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a9e0.md) FUN_0043a9e0

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
      "definition_site": "0043a9fc",
      "incomplete_value": false,
      "site": "0043a9fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a9fc",
      "incomplete_value": false,
      "site": "0043a9fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "0043a9fc",
      "DATA",
      [
        "storage",
        "00be6c20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043a9fc",
      "DATA",
      [
        "storage",
        "00be6cd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a9f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043a9e0.md#insn-0043a9f8)
- 新版 `0043a9f8`（命令位置の公開資料なし）

~~~diff
- 0043a9f8 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 0043a9f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043a9f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043a9f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043a9f8 ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 0043a9f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043a9f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043a9f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043a9f8 bytes 29813091
+ 0043a9f8 bytes 29413391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee79ba7abcd7d4c0a127b30cd8934a25"></a>

### [`0043aadc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043aadc.md) → [`0043aadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043aadc.md) FUN_0043aadc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`009bd60c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009bd/009bd60c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`009bd60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd60c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043abf0",
      "incomplete_value": false,
      "site": "0043abf0",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043abf0",
      "incomplete_value": false,
      "site": "0043abf0",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043abf4",
      "incomplete_value": false,
      "site": "0043abf4",
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
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043abf4",
      "incomplete_value": false,
      "site": "0043abf4",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0043ab38",
      "incomplete_value": true,
      "site": "0043ab38",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "0043ab38",
      "incomplete_value": true,
      "site": "0043ab38",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
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
      "0043ab30",
      "READ",
      [
        "storage",
        "00c24b50",
        null,
        "undefined8"
      ]
    ],
    [
      "0043ab30",
      "READ",
      [
        "storage",
        "00c24b58",
        null,
        "undefined8"
      ]
    ],
    [
      "0043ab9c",
      "READ",
      [
        "storage",
        "00c24b50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043ab30",
      "READ",
      [
        "storage",
        "00c24c10",
        null,
        "undefined8"
      ]
    ],
    [
      "0043ab30",
      "READ",
      [
        "storage",
        "00c24c18",
        null,
        "undefined8"
      ]
    ],
    [
      "0043ab9c",
      "READ",
      [
        "storage",
        "00c24c10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043abf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043aadc.md#insn-0043abf0) · [`0043abf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043aadc.md#insn-0043abf4) · [`0043ab2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043aadc.md#insn-0043ab2c)
- 新版 `0043abf0`（命令位置の公開資料なし） · `0043abf4`（命令位置の公開資料なし） · `0043ab2c`（命令位置の公開資料なし）

~~~diff
- 0043abf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b58:8"]]
- 0043abf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0043abf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
+ 0043abf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0043abf0 bytes 13ad05f9
+ 0043abf0 bytes 130d06f9
- 0043abf4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0043abf4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0043abf4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:b70:8"]]
- 0043abf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0043abf4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0043abf4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0043abf4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c30:8"]]
+ 0043abf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0043abf4 bytes 3fc12d39
+ 0043abf4 bytes 3fc13039
- 0043ab2c ["COPY", "tmp:0:8", ["const:b50:8"]]
- 0043ab2c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 0043ab2c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 0043ab2c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 0043ab2c ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0043ab2c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 0043ab2c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 0043ab2c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 0043ab2c bytes d6422d91
+ 0043ab2c bytes d6423091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db06d65050cf9b1be49e07e7b0a663a8"></a>

### [`0043af94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043af94.md) → [`0043af94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043af94.md) FUN_0043af94

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0043aca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043aca0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0043aca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043aca0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0043afa0",
      "incomplete_value": false,
      "site": "0043afa4",
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
      "definition_site": "0043afa0",
      "incomplete_value": false,
      "site": "0043afa4",
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
      "0043afa0",
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
      "0043afa0",
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

- 旧版 [`0043afa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043af94.md#insn-0043afa0)
- 新版 `0043afa0`（命令位置の公開資料なし）

~~~diff
- 0043afa0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0043afa0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0043afa0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0043afa0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0043afa0 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0043afa0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0043afa0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0043afa0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0043afa0 bytes 00280c91
+ 0043afa0 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0d6b54d35d8251ac7ea78c0e14ce913"></a>

### [`0043afac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043afac.md) → [`0043afac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043afac.md) FUN_0043afac

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
      "definition_site": "0043afd0",
      "incomplete_value": false,
      "site": "0043afd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043afd0",
      "incomplete_value": false,
      "site": "0043afd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
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
      "0043afd0",
      "DATA",
      [
        "storage",
        "00be6cb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043afd0",
      "DATA",
      [
        "storage",
        "00be6d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043afcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043afac.md#insn-0043afcc)
- 新版 `0043afcc`（命令位置の公開資料なし）

~~~diff
- 0043afcc ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 0043afcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043afcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043afcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043afcc ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 0043afcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043afcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043afcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043afcc bytes 08c13291
+ 0043afcc bytes 08813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0b943b1106b3cd9bc895c9bcc2845b9"></a>

### [`0043afe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043afe0.md) → [`0043afe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043afe0.md) FUN_0043afe0

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
      "definition_site": "0043afec",
      "incomplete_value": false,
      "site": "0043afec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043afec",
      "incomplete_value": false,
      "site": "0043afec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
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
      "0043afec",
      "DATA",
      [
        "storage",
        "00be6cb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043afec",
      "DATA",
      [
        "storage",
        "00be6d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043afe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043afe0.md#insn-0043afe8)
- 新版 `0043afe8`（命令位置の公開資料なし）

~~~diff
- 0043afe8 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 0043afe8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043afe8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043afe8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043afe8 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 0043afe8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043afe8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043afe8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043afe8 bytes 29c13291
+ 0043afe8 bytes 29813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3747fbb5d593f8b5814ffcfefb3848d2"></a>

### [`0043affc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043affc.md) → [`0043affc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043affc.md) FUN_0043affc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb190.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.91% / 新版 93.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 1件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043b050",
      "incomplete_value": true,
      "site": "0043b050",
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
      "definition_site": "0043b050",
      "incomplete_value": true,
      "site": "0043b050",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b3dc",
      "incomplete_value": false,
      "site": "0043b3dc",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b3dc",
      "incomplete_value": false,
      "site": "0043b3dc",
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
            "const:bb0:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b3e0",
      "incomplete_value": false,
      "site": "0043b3e0",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b3e0",
      "incomplete_value": false,
      "site": "0043b3e0",
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
            "const:bc8:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043b01c",
      "PARAM",
      [
        "storage",
        "00c24b74",
        null,
        null
      ]
    ],
    [
      "0043b03c",
      "READ",
      [
        "storage",
        "002a65e1",
        null,
        "string"
      ]
    ],
    [
      "0043b164",
      "READ",
      [
        "storage",
        "00c24ba8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043b01c",
      "PARAM",
      [
        "storage",
        "00c24c34",
        null,
        null
      ]
    ],
    [
      "0043b03c",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0043b164",
      "READ",
      [
        "storage",
        "00c24c68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b3dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043affc.md#insn-0043b3dc) · [`0043b3e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043affc.md#insn-0043b3e0) · [`0043b46c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043affc.md#insn-0043b46c)
- 新版 `0043b3dc`（命令位置の公開資料なし） · `0043b3e0`（命令位置の公開資料なし） · `0043b46c`（命令位置の公開資料なし）

~~~diff
- 0043b3dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb0:8"]]
- 0043b3dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0043b3dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c70:8"]]
+ 0043b3dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0043b3dc bytes 13d905f9
+ 0043b3dc bytes 133906f9
- 0043b3e0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0043b3e0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0043b3e0 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:bc8:8"]]
- 0043b3e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0043b3e0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0043b3e0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0043b3e0 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c88:8"]]
+ 0043b3e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0043b3e0 bytes 3f212f39
+ 0043b3e0 bytes 3f213239
- 0043b46c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb0:8"]]
- 0043b46c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0043b46c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c70:8"]]
+ 0043b46c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0043b46c bytes 13d905f9
+ 0043b46c bytes 133906f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efa2408bc8a062384a8ab4e38b4a82fc"></a>

### [`0043b598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b598.md) → [`0043b598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b598.md) FUN_0043b598

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
      "definition_site": "0043b5bc",
      "incomplete_value": false,
      "site": "0043b5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b5bc",
      "incomplete_value": false,
      "site": "0043b5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "0043b5bc",
      "DATA",
      [
        "storage",
        "00be6d30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043b5bc",
      "DATA",
      [
        "storage",
        "00be6de0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b598.md#insn-0043b5b8)
- 新版 `0043b5b8`（命令位置の公開資料なし）

~~~diff
- 0043b5b8 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 0043b5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043b5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043b5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b5b8 ["COPY", "tmp:0:8", ["const:de0:8"]]
+ 0043b5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043b5b8 bytes 08c13491
+ 0043b5b8 bytes 08813791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13cc5ac1cc1403290bf6b4ac5cce0579"></a>

### [`0043b5cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b5cc.md) → [`0043b5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b5cc.md) FUN_0043b5cc

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
      "definition_site": "0043b5d8",
      "incomplete_value": false,
      "site": "0043b5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b5d8",
      "incomplete_value": false,
      "site": "0043b5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "0043b5d8",
      "DATA",
      [
        "storage",
        "00be6d30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043b5d8",
      "DATA",
      [
        "storage",
        "00be6de0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b5d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b5cc.md#insn-0043b5d4)
- 新版 `0043b5d4`（命令位置の公開資料なし）

~~~diff
- 0043b5d4 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 0043b5d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043b5d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043b5d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043b5d4 ["COPY", "tmp:0:8", ["const:de0:8"]]
+ 0043b5d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043b5d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043b5d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043b5d4 bytes 29c13491
+ 0043b5d4 bytes 29813791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8465d92a66a1984375658eeac5f5b6b"></a>

### [`0043b5e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b5e8.md) → [`0043b5e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b5e8.md) FUN_0043b5e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0073e6dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073e6dc.md) [`0073ed78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073ed78.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0073e6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e6dc.md) [`0073ed78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ed78.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b6f0",
      "incomplete_value": false,
      "site": "0043b6f0",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b6f0",
      "incomplete_value": false,
      "site": "0043b6f0",
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
            "const:bb0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b6f4",
      "incomplete_value": false,
      "site": "0043b6f4",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b6f4",
      "incomplete_value": false,
      "site": "0043b6f4",
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
            "const:bc8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0043b650",
      "incomplete_value": true,
      "site": "0043b650",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "0043b650",
      "incomplete_value": true,
      "site": "0043b650",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
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
      "0043b648",
      "READ",
      [
        "storage",
        "00c24ba8",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b648",
      "READ",
      [
        "storage",
        "00c24bb0",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b69c",
      "READ",
      [
        "storage",
        "00c24ba8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043b648",
      "READ",
      [
        "storage",
        "00c24c68",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b648",
      "READ",
      [
        "storage",
        "00c24c70",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b69c",
      "READ",
      [
        "storage",
        "00c24c68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b6f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b5e8.md#insn-0043b6f0) · [`0043b6f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b5e8.md#insn-0043b6f4) · [`0043b644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b5e8.md#insn-0043b644)
- 新版 `0043b6f0`（命令位置の公開資料なし） · `0043b6f4`（命令位置の公開資料なし） · `0043b644`（命令位置の公開資料なし）

~~~diff
- 0043b6f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb0:8"]]
- 0043b6f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0043b6f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c70:8"]]
+ 0043b6f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0043b6f0 bytes 13d905f9
+ 0043b6f0 bytes 133906f9
- 0043b6f4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0043b6f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0043b6f4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:bc8:8"]]
- 0043b6f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0043b6f4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0043b6f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0043b6f4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c88:8"]]
+ 0043b6f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0043b6f4 bytes 3f212f39
+ 0043b6f4 bytes 3f213239
- 0043b644 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 0043b644 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 0043b644 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 0043b644 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 0043b644 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 0043b644 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 0043b644 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 0043b644 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 0043b644 bytes d6a22e91
+ 0043b644 bytes d6a23191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6981e56361e9d340e81eff4f5acc62e"></a>

### [`0043b790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b790.md) → [`0043b790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b790.md) FUN_0043b790

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0043c490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c490.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0043bd0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bd0c.md) [`00574ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`0043c490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c490.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0043bd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bd0c.md) [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.43% / 新版 92.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043b83c",
      "incomplete_value": true,
      "site": "0043b84c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b83c",
      "incomplete_value": true,
      "site": "0043b84c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3a7:8"
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
      "definition_site": "0043b95c",
      "incomplete_value": true,
      "site": "0043b96c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:453:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b95c",
      "incomplete_value": true,
      "site": "0043b96c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:44d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043b95c",
      "incomplete_value": true,
      "site": "0043b96c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0043b95c",
      "incomplete_value": true,
      "site": "0043b96c",
      "value": [
        "LOAD",
        "16",
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
      "0043b83c",
      "READ",
      [
        "storage",
        "002a53a7",
        null,
        "string"
      ]
    ],
    [
      "0043b95c",
      "READ",
      [
        "storage",
        "002aa44d",
        null,
        "string"
      ]
    ],
    [
      "0043b95c",
      "READ",
      [
        "storage",
        "002aa45d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043b83c",
      "READ",
      [
        "storage",
        "002a53a0",
        null,
        "string"
      ]
    ],
    [
      "0043b95c",
      "READ",
      [
        "storage",
        "002aa453",
        null,
        "string"
      ]
    ],
    [
      "0043b95c",
      "READ",
      [
        "storage",
        "002aa463",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b790.md#insn-0043b834) · [`0043b958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b790.md#insn-0043b958) · [`0043b9ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b790.md#insn-0043b9ac)
- 新版 `0043b834`（命令位置の公開資料なし） · `0043b958`（命令位置の公開資料なし） · `0043b9ac`（命令位置の公開資料なし）

~~~diff
- 0043b834 ["COPY", "tmp:0:8", ["const:3a7:8"]]
- 0043b834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043b834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043b834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043b834 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 0043b834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043b834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043b834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043b834 bytes 299d0e91
+ 0043b834 bytes 29810e91
- 0043b958 ["COPY", "tmp:0:8", ["const:44d:8"]]
- 0043b958 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043b958 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043b958 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b958 ["COPY", "tmp:0:8", ["const:453:8"]]
+ 0043b958 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b958 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b958 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043b958 bytes 08351191
+ 0043b958 bytes 084d1191
- 0043b9ac ["COPY", "tmp:0:8", ["const:26f:8"]]
- 0043b9ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043b9ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043b9ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b9ac ["COPY", "tmp:0:8", ["const:2fc:8"]]
+ 0043b9ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b9ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b9ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043b9ac bytes 08bd0991
+ 0043b9ac bytes 08f10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-060dcc0ca381f71b4174bac75b8404d4"></a>

### [`0043bd0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bd0c.md) → [`0043bd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bd0c.md) FUN_0043bd0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0043b790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b790.md) · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00574ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`0043b790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b790.md) · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.16% / 新版 85.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043bd58",
      "incomplete_value": true,
      "site": "0043bd58",
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
                "const:298000:8"
              ],
              [
                "leaf",
                "const:ccc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043bd58",
      "incomplete_value": true,
      "site": "0043bd58",
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
                "const:298000:8"
              ],
              [
                "leaf",
                "const:c3f:8"
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
      "definition_site": "0043bd5c",
      "incomplete_value": true,
      "site": "0043bd5c",
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
      "definition_site": "0043bd5c",
      "incomplete_value": true,
      "site": "0043bd5c",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043bdc4",
      "incomplete_value": true,
      "site": "0043bdc4",
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
                "const:3b2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043bdc4",
      "incomplete_value": true,
      "site": "0043bdc4",
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
                "const:3b9:8"
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
      "0043bd48",
      "READ",
      [
        "storage",
        "00298c3f",
        null,
        "string"
      ]
    ],
    [
      "0043bd4c",
      "READ",
      [
        "storage",
        "00298c45",
        null,
        "string"
      ]
    ],
    [
      "0043bdb0",
      "READ",
      [
        "storage",
        "002a53b9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043bd48",
      "READ",
      [
        "storage",
        "00298ccc",
        null,
        "string"
      ]
    ],
    [
      "0043bd4c",
      "READ",
      [
        "storage",
        "00298cd2",
        null,
        "string"
      ]
    ],
    [
      "0043bdb0",
      "READ",
      [
        "storage",
        "002a53b2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043bd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bd0c.md#insn-0043bd40) · [`0043bd44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bd0c.md#insn-0043bd44)
- 新版 `0043bd40`（命令位置の公開資料なし） · `0043bd44`（命令位置の公開資料なし）

~~~diff
- 0043bd40 ["COPY", "tmp:0:8", ["const:c3f:8"]]
- 0043bd40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043bd40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043bd40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043bd40 ["COPY", "tmp:0:8", ["const:ccc:8"]]
+ 0043bd40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043bd40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043bd40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043bd40 bytes 29fd3091
+ 0043bd40 bytes 29313391
- 0043bd44 ["COPY", "register:40b0:8", ["register:4000:8"]]
- 0043bd44 bytes f60300aa
+ 0043bd44 ["COPY", "register:40b0:8", ["register:4000:8"]]
+ 0043bd44 bytes f60300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf79e24b4e18c5e362364f2464ecd85a"></a>

### [`0043bf44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bf44.md) → [`0043bf44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bf44.md) FUN_0043bf44

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
      "definition_site": "0043bf48",
      "incomplete_value": false,
      "site": "0043bf4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043bf48",
      "incomplete_value": false,
      "site": "0043bf4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "0043bf4c",
      "DATA",
      [
        "storage",
        "00be6db0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0043bf4c",
      "DATA",
      [
        "storage",
        "00be6e60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043bf48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bf44.md#insn-0043bf48)
- 新版 `0043bf48`（命令位置の公開資料なし）

~~~diff
- 0043bf48 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0043bf48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043bf48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043bf48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043bf48 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 0043bf48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043bf48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043bf48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043bf48 bytes 08c13691
+ 0043bf48 bytes 08813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e88453818b9bc173b111f2b8edaae9d0"></a>

### [`0043bf54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bf54.md) → [`0043bf54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bf54.md) FUN_0043bf54

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
      "definition_site": "0043bf64",
      "incomplete_value": false,
      "site": "0043bf6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043bf64",
      "incomplete_value": false,
      "site": "0043bf6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "0043bf6c",
      "DATA",
      [
        "storage",
        "00be6db0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0043bf6c",
      "DATA",
      [
        "storage",
        "00be6e60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043bf64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bf54.md#insn-0043bf64)
- 新版 `0043bf64`（命令位置の公開資料なし）

~~~diff
- 0043bf64 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0043bf64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043bf64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043bf64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043bf64 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 0043bf64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043bf64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043bf64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043bf64 bytes 08c13691
+ 0043bf64 bytes 08813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e719aff32bbf687fa8e824a6067eef84"></a>

### [`0043bf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bf90.md) → [`0043bf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bf90.md) FUN_0043bf90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf10.md) [`00bdb180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb180.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043bfb4",
      "incomplete_value": true,
      "site": "0043bfb4",
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
      "definition_site": "0043bfb4",
      "incomplete_value": true,
      "site": "0043bfb4",
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
      "0043bfa8",
      "READ",
      [
        "storage",
        "00c1ad60",
        null,
        "pointer"
      ]
    ],
    [
      "0043bfb4",
      "DATA",
      [
        "storage",
        "00c12e30",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0043bfa8",
      "READ",
      [
        "storage",
        "00c1ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0043bfb4",
      "DATA",
      [
        "storage",
        "00c12ee0",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043bfa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bf90.md#insn-0043bfa8)
- 新版 `0043bfa8`（命令位置の公開資料なし）

~~~diff
- 0043bfa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d60:8"]]
- 0043bfa8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043bfa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 0043bfa8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0043bfa8 bytes 08b146f9
+ 0043bfa8 bytes 080947f9
~~~


<a id="compare-037bc025751ce29aa2c0998dbae112ca"></a>

### [`0043bfdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bfdc.md) → [`0043bfdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bfdc.md) FUN_0043bfdc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdaf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf10.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb180.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c000",
      "incomplete_value": true,
      "site": "0043c000",
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
      "definition_site": "0043c000",
      "incomplete_value": true,
      "site": "0043c000",
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
      "0043bff4",
      "READ",
      [
        "storage",
        "00c1ad60",
        null,
        "pointer"
      ]
    ],
    [
      "0043c000",
      "DATA",
      [
        "storage",
        "00c12e30",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0043bff4",
      "READ",
      [
        "storage",
        "00c1ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0043c000",
      "DATA",
      [
        "storage",
        "00c12ee0",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043bff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bfdc.md#insn-0043bff4)
- 新版 `0043bff4`（命令位置の公開資料なし）

~~~diff
- 0043bff4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d60:8"]]
- 0043bff4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043bff4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 0043bff4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0043bff4 bytes 08b146f9
+ 0043bff4 bytes 080947f9
~~~


<a id="compare-4e14ea824d676fe247e992b9dc297983"></a>

### [`0043c03c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c03c.md) → [`0043c03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c03c.md) FUN_0043c03c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043bf84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bf84.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377f0.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md)
- 新版 呼出元 1件 [`0043bf84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bf84.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377f0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c0e0",
      "incomplete_value": true,
      "site": "0043c0e4",
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
      "definition_site": "0043c0e0",
      "incomplete_value": true,
      "site": "0043c0e4",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043c0bc",
      "incomplete_value": true,
      "site": "0043c0c4",
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c0bc",
      "incomplete_value": true,
      "site": "0043c0c4",
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
                "const:d68:8"
              ]
            ]
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
      "0043c0bc",
      "READ",
      [
        "storage",
        "00c1ad68",
        null,
        "pointer"
      ]
    ],
    [
      "0043c0bc",
      "PARAM",
      [
        "storage",
        "00c12e08",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0043c0dc",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0043c0bc",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0043c0bc",
      "PARAM",
      [
        "storage",
        "00c12eb8",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0043c0dc",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c0bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c03c.md#insn-0043c0bc) · [`0043c0dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c03c.md#insn-0043c0dc)
- 新版 `0043c0bc`（命令位置の公開資料なし） · `0043c0dc`（命令位置の公開資料なし）

~~~diff
- 0043c0bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d68:8"]]
- 0043c0bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043c0bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
+ 0043c0bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0043c0bc bytes 21b446f9
+ 0043c0bc bytes 210c47f9
- 0043c0dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 0043c0dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043c0dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e20:8"]]
+ 0043c0dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0043c0dc bytes 08b946f9
+ 0043c0dc bytes 081147f9
~~~


<a id="compare-a9f711b1ac482956e8ec3955c7dab766"></a>

### [`0043c260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c260.md) → [`0043c260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c260.md) FUN_0043c260

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
      "definition_site": "0043c26c",
      "incomplete_value": false,
      "site": "0043c278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c26c",
      "incomplete_value": false,
      "site": "0043c278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "0043c278",
      "DATA",
      [
        "storage",
        "00be6e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c278",
      "DATA",
      [
        "storage",
        "00be6f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c26c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c260.md#insn-0043c26c)
- 新版 `0043c26c`（命令位置の公開資料なし）

~~~diff
- 0043c26c ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0043c26c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043c26c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043c26c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043c26c ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 0043c26c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043c26c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043c26c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043c26c bytes 4a613991
+ 0043c26c bytes 4a213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe485c99ab3dcd84f3d613f87beab46a"></a>

### [`0043c2a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c2a4.md) → [`0043c2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c2a4.md) FUN_0043c2a4

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
      "definition_site": "0043c2bc",
      "incomplete_value": false,
      "site": "0043c2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c2bc",
      "incomplete_value": false,
      "site": "0043c2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "0043c2c8",
      "DATA",
      [
        "storage",
        "00be6e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c2c8",
      "DATA",
      [
        "storage",
        "00be6f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c2bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c2a4.md#insn-0043c2bc)
- 新版 `0043c2bc`（命令位置の公開資料なし）

~~~diff
- 0043c2bc ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0043c2bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c2bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c2bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043c2bc ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 0043c2bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c2bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c2bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c2bc bytes 08613991
+ 0043c2bc bytes 08213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b2ee7541079ff9e7b0673b3e36ebb5d"></a>

### [`0043c300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c300.md) → [`0043c300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c300.md) FUN_0043c300

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0043c32c",
      "incomplete_value": false,
      "site": "0043c32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c32c",
      "incomplete_value": false,
      "site": "0043c32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "0043c32c",
      "DATA",
      [
        "storage",
        "00be6e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c32c",
      "DATA",
      [
        "storage",
        "00be6f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c300.md#insn-0043c324)
- 新版 `0043c324`（命令位置の公開資料なし）

~~~diff
- 0043c324 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0043c324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043c324 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 0043c324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c324 bytes 08613991
+ 0043c324 bytes 08213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceebfdf016e798e07ef982bc332572e6"></a>

### [`0043c390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c390.md) → [`0043c390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c390.md) FUN_0043c390

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c3b0",
      "incomplete_value": false,
      "site": "0043c3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c3b0",
      "incomplete_value": false,
      "site": "0043c3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "0043c3b0",
      "DATA",
      [
        "storage",
        "00be6e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c3b0",
      "DATA",
      [
        "storage",
        "00be6f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c3ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c390.md#insn-0043c3ac)
- 新版 `0043c3ac`（命令位置の公開資料なし）

~~~diff
- 0043c3ac ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0043c3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043c3ac ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 0043c3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c3ac bytes 08613991
+ 0043c3ac bytes 08213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89f9bebcd2628aab394687ca7131d71a"></a>

### [`0043c490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c490.md) → [`0043c490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c490.md) FUN_0043c490

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0043b790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043b790.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0043b790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b790.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c53c",
      "incomplete_value": true,
      "site": "0043c53c",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:6e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c53c",
      "incomplete_value": true,
      "site": "0043c53c",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:653:8"
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
      "0043c528",
      "READ",
      [
        "storage",
        "00292653",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043c528",
      "READ",
      [
        "storage",
        "002926e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c490.md#insn-0043c520)
- 新版 `0043c520`（命令位置の公開資料なし）

~~~diff
- 0043c520 ["COPY", "tmp:0:8", ["const:653:8"]]
- 0043c520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043c520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043c520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043c520 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 0043c520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043c520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043c520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043c520 bytes 294d1991
+ 0043c520 bytes 29811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff18e6a8346891a1cd46ee48a153a5b7"></a>

### [`0043c754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c754.md) → [`0043c754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c754.md) FUN_0043c754

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
      "definition_site": "0043c760",
      "incomplete_value": false,
      "site": "0043c76c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c760",
      "incomplete_value": false,
      "site": "0043c76c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "0043c76c",
      "DATA",
      [
        "storage",
        "00be6ed8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c76c",
      "DATA",
      [
        "storage",
        "00be6f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c754.md#insn-0043c760)
- 新版 `0043c760`（命令位置の公開資料なし）

~~~diff
- 0043c760 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 0043c760 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043c760 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043c760 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043c760 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0043c760 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043c760 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043c760 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043c760 bytes 4a613b91
+ 0043c760 bytes 4a213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9805be8ed2a408ea0b08cc8b43d1a539"></a>

### [`0043c798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c798.md) → [`0043c798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c798.md) FUN_0043c798

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
      "definition_site": "0043c7b0",
      "incomplete_value": false,
      "site": "0043c7bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c7b0",
      "incomplete_value": false,
      "site": "0043c7bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "0043c7bc",
      "DATA",
      [
        "storage",
        "00be6ed8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c7bc",
      "DATA",
      [
        "storage",
        "00be6f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c798.md#insn-0043c7b0)
- 新版 `0043c7b0`（命令位置の公開資料なし）

~~~diff
- 0043c7b0 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 0043c7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043c7b0 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0043c7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c7b0 bytes 08613b91
+ 0043c7b0 bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44931213aa1887555485b54234295313"></a>

### [`0043c7f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c7f4.md) → [`0043c7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c7f4.md) FUN_0043c7f4

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
      "definition_site": "0043c820",
      "incomplete_value": false,
      "site": "0043c820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c820",
      "incomplete_value": false,
      "site": "0043c820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "0043c820",
      "DATA",
      [
        "storage",
        "00be6ed8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c820",
      "DATA",
      [
        "storage",
        "00be6f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c7f4.md#insn-0043c818)
- 新版 `0043c818`（命令位置の公開資料なし）

~~~diff
- 0043c818 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 0043c818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043c818 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0043c818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c818 bytes 08613b91
+ 0043c818 bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-342d8d4154132f885dcd6296ec295a8b"></a>

### [`0043c87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c87c.md) → [`0043c87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c87c.md) FUN_0043c87c

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
      "definition_site": "0043c898",
      "incomplete_value": false,
      "site": "0043c898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c898",
      "incomplete_value": false,
      "site": "0043c898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "0043c898",
      "DATA",
      [
        "storage",
        "00be6ed8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c898",
      "DATA",
      [
        "storage",
        "00be6f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043c87c.md#insn-0043c894)
- 新版 `0043c894`（命令位置の公開資料なし）

~~~diff
- 0043c894 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 0043c894 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043c894 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043c894 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043c894 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0043c894 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043c894 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043c894 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043c894 bytes 29613b91
+ 0043c894 bytes 29213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27556011da524317c9c884dcc79a3e7f"></a>

### [`0043ca28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043ca28.md) → [`0043ca28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043ca28.md) FUN_0043ca28

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "0043ca3c",
      "incomplete_value": false,
      "site": "0043ca40",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ca3c",
      "incomplete_value": false,
      "site": "0043ca40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "0043ca40",
      "DATA",
      [
        "storage",
        "00be6f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043ca40",
      "DATA",
      [
        "storage",
        "00be7008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043ca38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043ca28.md#insn-0043ca38) · [`0043ca3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043ca28.md#insn-0043ca3c)
- 新版 `0043ca38`（命令位置の公開資料なし） · `0043ca3c`（命令位置の公開資料なし）

~~~diff
- 0043ca38 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0043ca38 ["COPY", "register:4040:8", ["const:be7000:8"]]
- 0043ca38 bytes 483d00d0
+ 0043ca38 bytes 483d00f0
- 0043ca3c ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0043ca3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043ca3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043ca3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043ca3c ["COPY", "tmp:0:8", ["const:8:8"]]
+ 0043ca3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ca3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ca3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043ca3c bytes 08613d91
+ 0043ca3c bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6007c7ce3272afb54a85c49861bdbf5"></a>

### [`0043ca84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043ca84.md) → [`0043ca84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043ca84.md) FUN_0043ca84

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0043ca9c",
      "incomplete_value": false,
      "site": "0043caa0",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ca9c",
      "incomplete_value": false,
      "site": "0043caa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "0043caa0",
      "DATA",
      [
        "storage",
        "00be6f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043caa0",
      "DATA",
      [
        "storage",
        "00be7008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043ca98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043ca84.md#insn-0043ca98) · [`0043ca9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043ca84.md#insn-0043ca9c)
- 新版 `0043ca98`（命令位置の公開資料なし） · `0043ca9c`（命令位置の公開資料なし）

~~~diff
- 0043ca98 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0043ca98 ["COPY", "register:4040:8", ["const:be7000:8"]]
- 0043ca98 bytes 483d00d0
+ 0043ca98 bytes 483d00f0
- 0043ca9c ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0043ca9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043ca9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043ca9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043ca9c ["COPY", "tmp:0:8", ["const:8:8"]]
+ 0043ca9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ca9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ca9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043ca9c bytes 08613d91
+ 0043ca9c bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a38a7ecb5291eb6c5ad2b21ab540a45"></a>

### [`0043cae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cae0.md) → [`0043cae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cae0.md) FUN_0043cae0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0043cb04",
      "incomplete_value": false,
      "site": "0043cb04",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cb04",
      "incomplete_value": false,
      "site": "0043cb04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "0043cb04",
      "DATA",
      [
        "storage",
        "00be6f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cb04",
      "DATA",
      [
        "storage",
        "00be7008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cafc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cae0.md#insn-0043cafc) · [`0043cb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cae0.md#insn-0043cb00)
- 新版 `0043cafc`（命令位置の公開資料なし） · `0043cb00`（命令位置の公開資料なし）

~~~diff
- 0043cafc ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0043cafc ["COPY", "register:4048:8", ["const:be7000:8"]]
- 0043cafc bytes 493d00d0
+ 0043cafc bytes 493d00f0
- 0043cb00 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0043cb00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043cb00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043cb00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043cb00 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 0043cb00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043cb00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043cb00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043cb00 bytes 29613d91
+ 0043cb00 bytes 29210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-453f000ae2ae15e2805324c8c0a30020"></a>

### [`0043cb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cb30.md) → [`0043cb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cb30.md) FUN_0043cb30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

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
      "definition_site": "0043cb3c",
      "incomplete_value": false,
      "site": "0043cb3c",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cb3c",
      "incomplete_value": false,
      "site": "0043cb3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "0043cb3c",
      "DATA",
      [
        "storage",
        "00be6f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cb3c",
      "DATA",
      [
        "storage",
        "00be7008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cb34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cb30.md#insn-0043cb34) · [`0043cb38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cb30.md#insn-0043cb38)
- 新版 `0043cb34`（命令位置の公開資料なし） · `0043cb38`（命令位置の公開資料なし）

~~~diff
- 0043cb34 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0043cb34 ["COPY", "register:4048:8", ["const:be7000:8"]]
- 0043cb34 bytes 493d00d0
+ 0043cb34 bytes 493d00f0
- 0043cb38 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0043cb38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043cb38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043cb38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043cb38 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 0043cb38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043cb38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043cb38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043cb38 bytes 29613d91
+ 0043cb38 bytes 29210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f1fa84db0d2a2df181567b23438b18a"></a>

### [`0043ccc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043ccc4.md) → [`0043ccc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043ccc4.md) FUN_0043ccc4

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
      "definition_site": "0043ccd0",
      "incomplete_value": false,
      "site": "0043ccdc",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ccd0",
      "incomplete_value": false,
      "site": "0043ccdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
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
      "0043ccdc",
      "DATA",
      [
        "storage",
        "00be6fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043ccdc",
      "DATA",
      [
        "storage",
        "00be7088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043ccc4.md#insn-0043cccc) · [`0043ccd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043ccc4.md#insn-0043ccd0)
- 新版 `0043cccc`（命令位置の公開資料なし） · `0043ccd0`（命令位置の公開資料なし）

~~~diff
- 0043cccc ["COPY", "register:4050:8", ["const:be6000:8"]]
+ 0043cccc ["COPY", "register:4050:8", ["const:be7000:8"]]
- 0043cccc bytes 4a3d00d0
+ 0043cccc bytes 4a3d00f0
- 0043ccd0 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 0043ccd0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043ccd0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043ccd0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043ccd0 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 0043ccd0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043ccd0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043ccd0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043ccd0 bytes 4a613f91
+ 0043ccd0 bytes 4a210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-419ff02ef759d3d57316e682e1de9c1f"></a>

### [`0043cd08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cd08.md) → [`0043cd08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cd08.md) FUN_0043cd08

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
      "definition_site": "0043cd20",
      "incomplete_value": false,
      "site": "0043cd2c",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cd20",
      "incomplete_value": false,
      "site": "0043cd2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
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
      "0043cd2c",
      "DATA",
      [
        "storage",
        "00be6fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cd2c",
      "DATA",
      [
        "storage",
        "00be7088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cd08.md#insn-0043cd1c) · [`0043cd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cd08.md#insn-0043cd20)
- 新版 `0043cd1c`（命令位置の公開資料なし） · `0043cd20`（命令位置の公開資料なし）

~~~diff
- 0043cd1c ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0043cd1c ["COPY", "register:4040:8", ["const:be7000:8"]]
- 0043cd1c bytes 483d00d0
+ 0043cd1c bytes 483d00f0
- 0043cd20 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 0043cd20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043cd20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043cd20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043cd20 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 0043cd20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cd20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cd20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043cd20 bytes 08613f91
+ 0043cd20 bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19074119405003672a295b2f439550f6"></a>

### [`0043cd64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cd64.md) → [`0043cd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cd64.md) FUN_0043cd64

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
      "definition_site": "0043cd90",
      "incomplete_value": false,
      "site": "0043cd90",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cd90",
      "incomplete_value": false,
      "site": "0043cd90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
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
      "0043cd90",
      "DATA",
      [
        "storage",
        "00be6fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cd90",
      "DATA",
      [
        "storage",
        "00be7088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cd84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cd64.md#insn-0043cd84) · [`0043cd88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cd64.md#insn-0043cd88)
- 新版 `0043cd84`（命令位置の公開資料なし） · `0043cd88`（命令位置の公開資料なし）

~~~diff
- 0043cd84 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0043cd84 ["COPY", "register:4040:8", ["const:be7000:8"]]
- 0043cd84 bytes 483d00d0
+ 0043cd84 bytes 483d00f0
- 0043cd88 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 0043cd88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043cd88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043cd88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043cd88 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 0043cd88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cd88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cd88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043cd88 bytes 08613f91
+ 0043cd88 bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a623b4a972e52f8e0249e1a95b7a8dab"></a>

### [`0043cdec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cdec.md) → [`0043cdec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cdec.md) FUN_0043cdec

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
      "definition_site": "0043ce08",
      "incomplete_value": false,
      "site": "0043ce08",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ce08",
      "incomplete_value": false,
      "site": "0043ce08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
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
      "0043ce08",
      "DATA",
      [
        "storage",
        "00be6fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043ce08",
      "DATA",
      [
        "storage",
        "00be7088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043ce00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cdec.md#insn-0043ce00) · [`0043ce04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cdec.md#insn-0043ce04)
- 新版 `0043ce00`（命令位置の公開資料なし） · `0043ce04`（命令位置の公開資料なし）

~~~diff
- 0043ce00 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0043ce00 ["COPY", "register:4048:8", ["const:be7000:8"]]
- 0043ce00 bytes 493d00d0
+ 0043ce00 bytes 493d00f0
- 0043ce04 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 0043ce04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043ce04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043ce04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043ce04 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 0043ce04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043ce04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043ce04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043ce04 bytes 29613f91
+ 0043ce04 bytes 29210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65a3b0cbf5f807bef24638c2c8ec4149"></a>

### [`0043cf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cf30.md) → [`0043cf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cf30.md) FUN_0043cf30

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
      "definition_site": "0043cf3c",
      "incomplete_value": false,
      "site": "0043cf48",
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
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cf3c",
      "incomplete_value": false,
      "site": "0043cf48",
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
            "const:58:8"
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
      "0043cf48",
      "DATA",
      [
        "storage",
        "00be7058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cf48",
      "DATA",
      [
        "storage",
        "00be7108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cf3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cf30.md#insn-0043cf3c)
- 新版 `0043cf3c`（命令位置の公開資料なし）

~~~diff
- 0043cf3c ["COPY", "tmp:0:8", ["const:58:8"]]
- 0043cf3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043cf3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043cf3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043cf3c ["COPY", "tmp:0:8", ["const:108:8"]]
+ 0043cf3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043cf3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043cf3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043cf3c bytes 4a610191
+ 0043cf3c bytes 4a210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-367462c45e4b49b6a61f22a79a923e03"></a>

### [`0043cf74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cf74.md) → [`0043cf74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cf74.md) FUN_0043cf74

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
      "definition_site": "0043cf8c",
      "incomplete_value": false,
      "site": "0043cf98",
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
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cf8c",
      "incomplete_value": false,
      "site": "0043cf98",
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
            "const:58:8"
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
      "0043cf98",
      "DATA",
      [
        "storage",
        "00be7058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cf98",
      "DATA",
      [
        "storage",
        "00be7108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cf8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cf74.md#insn-0043cf8c)
- 新版 `0043cf8c`（命令位置の公開資料なし）

~~~diff
- 0043cf8c ["COPY", "tmp:0:8", ["const:58:8"]]
- 0043cf8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043cf8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043cf8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043cf8c ["COPY", "tmp:0:8", ["const:108:8"]]
+ 0043cf8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cf8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cf8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043cf8c bytes 08610191
+ 0043cf8c bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b4f6ee4fb14ecc03207a4811ecaa8f2"></a>

### [`0043cfd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cfd0.md) → [`0043cfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cfd0.md) FUN_0043cfd0

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
      "definition_site": "0043cffc",
      "incomplete_value": false,
      "site": "0043cffc",
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
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cffc",
      "incomplete_value": false,
      "site": "0043cffc",
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
            "const:58:8"
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
      "0043cffc",
      "DATA",
      [
        "storage",
        "00be7058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cffc",
      "DATA",
      [
        "storage",
        "00be7108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cfd0.md#insn-0043cff4)
- 新版 `0043cff4`（命令位置の公開資料なし）

~~~diff
- 0043cff4 ["COPY", "tmp:0:8", ["const:58:8"]]
- 0043cff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043cff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043cff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043cff4 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 0043cff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043cff4 bytes 08610191
+ 0043cff4 bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb2924f08920e749e707e666d5f8896a"></a>

### [`0043d058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d058.md) → [`0043d058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d058.md) FUN_0043d058

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
      "definition_site": "0043d074",
      "incomplete_value": false,
      "site": "0043d074",
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
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d074",
      "incomplete_value": false,
      "site": "0043d074",
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
            "const:58:8"
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
      "0043d074",
      "DATA",
      [
        "storage",
        "00be7058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d074",
      "DATA",
      [
        "storage",
        "00be7108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d058.md#insn-0043d070)
- 新版 `0043d070`（命令位置の公開資料なし）

~~~diff
- 0043d070 ["COPY", "tmp:0:8", ["const:58:8"]]
- 0043d070 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043d070 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043d070 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043d070 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 0043d070 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043d070 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043d070 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043d070 bytes 29610191
+ 0043d070 bytes 29210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70eed1a91f0b5a229c90cb49a204dff6"></a>

### [`0043d1f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d1f8.md) → [`0043d1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d1f8.md) FUN_0043d1f8

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
      "definition_site": "0043d20c",
      "incomplete_value": false,
      "site": "0043d210",
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
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d20c",
      "incomplete_value": false,
      "site": "0043d210",
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
            "const:d8:8"
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
      "0043d210",
      "DATA",
      [
        "storage",
        "00be70d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d210",
      "DATA",
      [
        "storage",
        "00be7188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d20c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d1f8.md#insn-0043d20c)
- 新版 `0043d20c`（命令位置の公開資料なし）

~~~diff
- 0043d20c ["COPY", "tmp:0:8", ["const:d8:8"]]
- 0043d20c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d20c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d20c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043d20c ["COPY", "tmp:0:8", ["const:188:8"]]
+ 0043d20c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d20c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d20c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d20c bytes 08610391
+ 0043d20c bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d2f0321a7ff64cfac88144cc6612886"></a>

### [`0043d21c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d21c.md) → [`0043d21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d21c.md) FUN_0043d21c

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
      "definition_site": "0043d220",
      "incomplete_value": false,
      "site": "0043d224",
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
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d220",
      "incomplete_value": false,
      "site": "0043d224",
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
            "const:d8:8"
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
      "0043d224",
      "DATA",
      [
        "storage",
        "00be70d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d224",
      "DATA",
      [
        "storage",
        "00be7188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d21c.md#insn-0043d220)
- 新版 `0043d220`（命令位置の公開資料なし）

~~~diff
- 0043d220 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 0043d220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043d220 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 0043d220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d220 bytes 08610391
+ 0043d220 bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5fe82488e89bb451ded216e7805c1ff"></a>

### [`0043d234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d234.md) → [`0043d234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d234.md) FUN_0043d234

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00573e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00573/00573e38.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00573e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573e38.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.77% / 新版 91.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043d360",
      "incomplete_value": true,
      "site": "0043d360",
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
                "const:396:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d360",
      "incomplete_value": true,
      "site": "0043d360",
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
                "const:39d:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0043d3fc",
      "incomplete_value": true,
      "site": "0043d3fc",
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
      "definition_site": "0043d3fc",
      "incomplete_value": true,
      "site": "0043d3fc",
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
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043d3ec",
      "incomplete_value": true,
      "site": "0043d3fc",
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
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d3ec",
      "incomplete_value": true,
      "site": "0043d3fc",
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
                "const:ad8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043d350",
      "READ",
      [
        "storage",
        "002a539d",
        null,
        "string"
      ]
    ],
    [
      "0043d398",
      "READ",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043d3a4",
      "READ",
      [
        "storage",
        "00c24ad8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043d350",
      "READ",
      [
        "storage",
        "002a5396",
        null,
        "string"
      ]
    ],
    [
      "0043d398",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043d3a4",
      "READ",
      [
        "storage",
        "00c24b98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d234.md#insn-0043d348) · [`0043d394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d234.md#insn-0043d394) · [`0043d3a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d234.md#insn-0043d3a4)
- 新版 `0043d348`（命令位置の公開資料なし） · `0043d394`（命令位置の公開資料なし） · `0043d3a4`（命令位置の公開資料なし）

~~~diff
- 0043d348 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0043d348 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043d348 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043d348 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043d348 ["COPY", "tmp:0:8", ["const:396:8"]]
+ 0043d348 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043d348 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043d348 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043d348 bytes 29750e91
+ 0043d348 bytes 29590e91
- 0043d394 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0043d394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043d394 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 0043d394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d394 bytes 08812b91
+ 0043d394 bytes 08812e91
- 0043d3a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ad8:8"]]
- 0043d3a4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043d3a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b98:8"]]
+ 0043d3a4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0043d3a4 bytes 006d45f9
+ 0043d3a4 bytes 00cd45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4185da9ba145b8365c1d9a69b740318"></a>

### [`0043d694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d694.md) → [`0043d694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d694.md) FUN_0043d694

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
      "definition_site": "0043d6a0",
      "incomplete_value": false,
      "site": "0043d6ac",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d6a0",
      "incomplete_value": false,
      "site": "0043d6ac",
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
            "const:158:8"
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
      "0043d6ac",
      "DATA",
      [
        "storage",
        "00be7158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d6ac",
      "DATA",
      [
        "storage",
        "00be7208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d694.md#insn-0043d6a0)
- 新版 `0043d6a0`（命令位置の公開資料なし）

~~~diff
- 0043d6a0 ["COPY", "tmp:0:8", ["const:158:8"]]
- 0043d6a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043d6a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043d6a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043d6a0 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 0043d6a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043d6a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043d6a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043d6a0 bytes 4a610591
+ 0043d6a0 bytes 4a210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-355b950445d29b27d4c63ccda6018f4e"></a>

### [`0043d6d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d6d8.md) → [`0043d6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d6d8.md) FUN_0043d6d8

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
      "definition_site": "0043d6f0",
      "incomplete_value": false,
      "site": "0043d6fc",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d6f0",
      "incomplete_value": false,
      "site": "0043d6fc",
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
            "const:158:8"
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
      "0043d6fc",
      "DATA",
      [
        "storage",
        "00be7158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d6fc",
      "DATA",
      [
        "storage",
        "00be7208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d6f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d6d8.md#insn-0043d6f0)
- 新版 `0043d6f0`（命令位置の公開資料なし）

~~~diff
- 0043d6f0 ["COPY", "tmp:0:8", ["const:158:8"]]
- 0043d6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043d6f0 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 0043d6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d6f0 bytes 08610591
+ 0043d6f0 bytes 08210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3a1ffa72adba4817c0da7109fe67915"></a>

### [`0043d734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d734.md) → [`0043d734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d734.md) FUN_0043d734

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
      "definition_site": "0043d760",
      "incomplete_value": false,
      "site": "0043d760",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d760",
      "incomplete_value": false,
      "site": "0043d760",
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
            "const:158:8"
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
      "0043d760",
      "DATA",
      [
        "storage",
        "00be7158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d760",
      "DATA",
      [
        "storage",
        "00be7208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d734.md#insn-0043d758)
- 新版 `0043d758`（命令位置の公開資料なし）

~~~diff
- 0043d758 ["COPY", "tmp:0:8", ["const:158:8"]]
- 0043d758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043d758 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 0043d758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d758 bytes 08610591
+ 0043d758 bytes 08210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04aa2be61f51f07c821f2884ba79802c"></a>

### [`0043d7bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d7bc.md) → [`0043d7bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d7bc.md) FUN_0043d7bc

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
      "definition_site": "0043d7d8",
      "incomplete_value": false,
      "site": "0043d7d8",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d7d8",
      "incomplete_value": false,
      "site": "0043d7d8",
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
            "const:158:8"
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
      "0043d7d8",
      "DATA",
      [
        "storage",
        "00be7158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d7d8",
      "DATA",
      [
        "storage",
        "00be7208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d7bc.md#insn-0043d7d4)
- 新版 `0043d7d4`（命令位置の公開資料なし）

~~~diff
- 0043d7d4 ["COPY", "tmp:0:8", ["const:158:8"]]
- 0043d7d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043d7d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043d7d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043d7d4 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 0043d7d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043d7d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043d7d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043d7d4 bytes 29610591
+ 0043d7d4 bytes 29210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05e9345bd1f9cf976adb13322c92c1a7"></a>

### [`0043d8b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d8b8.md) → [`0043d8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d8b8.md) FUN_0043d8b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0043e5d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043e5d8.md) [`0043e7f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043e7f8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0043e5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e5d8.md) [`0043e7f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e7f8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.41% / 新版 97.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043da40",
      "incomplete_value": true,
      "site": "0043da4c",
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
                "const:1e5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043da40",
      "incomplete_value": true,
      "site": "0043da4c",
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
                "const:158:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043dbac",
      "incomplete_value": true,
      "site": "0043dbbc",
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
                "const:5ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043dbac",
      "incomplete_value": true,
      "site": "0043dbbc",
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
                "const:5f4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043dbc0",
      "incomplete_value": true,
      "site": "0043dbc0",
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
      "definition_site": "0043dbc0",
      "incomplete_value": true,
      "site": "0043dbc0",
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
      "0043da40",
      "READ",
      [
        "storage",
        "002a2158",
        null,
        "string"
      ]
    ],
    [
      "0043dbac",
      "READ",
      [
        "storage",
        "002a65f4",
        null,
        "string"
      ]
    ],
    [
      "0043dbb4",
      "READ",
      [
        "storage",
        "002a65f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043da40",
      "READ",
      [
        "storage",
        "002a21e5",
        null,
        "string"
      ]
    ],
    [
      "0043dbac",
      "READ",
      [
        "storage",
        "002a65ed",
        null,
        "string"
      ]
    ],
    [
      "0043dbb4",
      "READ",
      [
        "storage",
        "002a65f2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043da3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d8b8.md#insn-0043da3c) · [`0043dba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d8b8.md#insn-0043dba4) · [`0043dc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d8b8.md#insn-0043dc48)
- 新版 `0043da3c`（命令位置の公開資料なし） · `0043dba4`（命令位置の公開資料なし） · `0043dc48`（命令位置の公開資料なし）

~~~diff
- 0043da3c ["COPY", "tmp:0:8", ["const:158:8"]]
- 0043da3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043da3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043da3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043da3c ["COPY", "tmp:0:8", ["const:1e5:8"]]
+ 0043da3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043da3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043da3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043da3c bytes 08610591
+ 0043da3c bytes 08950791
- 0043dba4 ["COPY", "tmp:0:8", ["const:5f4:8"]]
- 0043dba4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043dba4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043dba4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043dba4 ["COPY", "tmp:0:8", ["const:5ed:8"]]
+ 0043dba4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043dba4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043dba4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043dba4 bytes 4ad11791
+ 0043dba4 bytes 4ab51791
- 0043dc48 ["COPY", "tmp:0:8", ["const:2bd:8"]]
- 0043dc48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043dc48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043dc48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043dc48 ["COPY", "tmp:0:8", ["const:34a:8"]]
+ 0043dc48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043dc48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043dc48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043dc48 bytes 08f50a91
+ 0043dc48 bytes 08290d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dd20039f0f6e4e00f30bd1dfb680e46"></a>

### [`0043e788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043e788.md) → [`0043e788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e788.md) FUN_0043e788

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0043e5d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043e5d8.md) [`0043eef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043eef0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0043e5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e5d8.md) [`0043eef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043eef0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0043e794",
      "incomplete_value": false,
      "site": "0043e798",
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
      "definition_site": "0043e794",
      "incomplete_value": false,
      "site": "0043e798",
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
      "0043e794",
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
      "0043e794",
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

- 旧版 [`0043e794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043e788.md#insn-0043e794)
- 新版 `0043e794`（命令位置の公開資料なし）

~~~diff
- 0043e794 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0043e794 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0043e794 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0043e794 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0043e794 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0043e794 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0043e794 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0043e794 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0043e794 bytes 00280c91
+ 0043e794 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6596086849a2f4c179dc0b9db50c3d1"></a>

### [`0043eb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043eb40.md) → [`0043eb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043eb40.md) FUN_0043eb40

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0043e940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043e940.md) [`0043ec60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043ec60.md) [`00989584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/00989584.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`0043e940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e940.md) [`0043ec60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043ec60.md) [`00989584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/00989584.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0043eb4c",
      "incomplete_value": false,
      "site": "0043eb50",
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
      "definition_site": "0043eb4c",
      "incomplete_value": false,
      "site": "0043eb50",
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
      "0043eb4c",
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
      "0043eb4c",
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

- 旧版 [`0043eb4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043eb40.md#insn-0043eb4c)
- 新版 `0043eb4c`（命令位置の公開資料なし）

~~~diff
- 0043eb4c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0043eb4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0043eb4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0043eb4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0043eb4c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0043eb4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0043eb4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0043eb4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0043eb4c bytes 00280c91
+ 0043eb4c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d932edb6470d245e8307319399e7d80"></a>

### [`0043f158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f158.md) → [`0043f158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f158.md) FUN_0043f158

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
      "definition_site": "0043f164",
      "incomplete_value": false,
      "site": "0043f170",
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
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f164",
      "incomplete_value": false,
      "site": "0043f170",
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
            "const:1d8:8"
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
      "0043f170",
      "DATA",
      [
        "storage",
        "00be71d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f170",
      "DATA",
      [
        "storage",
        "00be7288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f158.md#insn-0043f164)
- 新版 `0043f164`（命令位置の公開資料なし）

~~~diff
- 0043f164 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 0043f164 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043f164 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043f164 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043f164 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 0043f164 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043f164 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043f164 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043f164 bytes 4a610791
+ 0043f164 bytes 4a210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1966969913842ea64ccecbd994c560f9"></a>

### [`0043f19c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f19c.md) → [`0043f19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f19c.md) FUN_0043f19c

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
      "definition_site": "0043f1b4",
      "incomplete_value": false,
      "site": "0043f1c0",
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
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f1b4",
      "incomplete_value": false,
      "site": "0043f1c0",
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
            "const:1d8:8"
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
      "0043f1c0",
      "DATA",
      [
        "storage",
        "00be71d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f1c0",
      "DATA",
      [
        "storage",
        "00be7288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f1b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f19c.md#insn-0043f1b4)
- 新版 `0043f1b4`（命令位置の公開資料なし）

~~~diff
- 0043f1b4 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 0043f1b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f1b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f1b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f1b4 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 0043f1b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f1b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f1b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f1b4 bytes 08610791
+ 0043f1b4 bytes 08210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c47ef6b1579c3f7ce89400bc637ca6e"></a>

### [`0043f1f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f1f8.md) → [`0043f1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f1f8.md) FUN_0043f1f8

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
      "definition_site": "0043f224",
      "incomplete_value": false,
      "site": "0043f224",
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
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f224",
      "incomplete_value": false,
      "site": "0043f224",
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
            "const:1d8:8"
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
      "0043f224",
      "DATA",
      [
        "storage",
        "00be71d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f224",
      "DATA",
      [
        "storage",
        "00be7288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f21c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f1f8.md#insn-0043f21c)
- 新版 `0043f21c`（命令位置の公開資料なし）

~~~diff
- 0043f21c ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 0043f21c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f21c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f21c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f21c ["COPY", "tmp:0:8", ["const:288:8"]]
+ 0043f21c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f21c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f21c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f21c bytes 08610791
+ 0043f21c bytes 08210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5133e01914a175c70608e9bedecc9c3"></a>

### [`0043f280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f280.md) → [`0043f280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f280.md) FUN_0043f280

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
      "definition_site": "0043f29c",
      "incomplete_value": false,
      "site": "0043f29c",
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
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f29c",
      "incomplete_value": false,
      "site": "0043f29c",
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
            "const:1d8:8"
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
      "0043f29c",
      "DATA",
      [
        "storage",
        "00be71d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f29c",
      "DATA",
      [
        "storage",
        "00be7288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f280.md#insn-0043f298)
- 新版 `0043f298`（命令位置の公開資料なし）

~~~diff
- 0043f298 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 0043f298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043f298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043f298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043f298 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 0043f298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043f298 bytes 29610791
+ 0043f298 bytes 29210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06714c3d783cb6b2af08340a8efe43f7"></a>

### [`0043f4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f4e8.md) → [`0043f4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f4e8.md) FUN_0043f4e8

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
      "definition_site": "0043f4f4",
      "incomplete_value": false,
      "site": "0043f500",
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
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f4f4",
      "incomplete_value": false,
      "site": "0043f500",
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
            "const:258:8"
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
      "0043f500",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f500",
      "DATA",
      [
        "storage",
        "00be7308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f4f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f4e8.md#insn-0043f4f4)
- 新版 `0043f4f4`（命令位置の公開資料なし）

~~~diff
- 0043f4f4 ["COPY", "tmp:0:8", ["const:258:8"]]
- 0043f4f4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043f4f4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043f4f4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043f4f4 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 0043f4f4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043f4f4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043f4f4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043f4f4 bytes 4a610991
+ 0043f4f4 bytes 4a210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30dffd717e2f4a77ea4f32ebf5930bef"></a>

### [`0043f52c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f52c.md) → [`0043f52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f52c.md) FUN_0043f52c

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
      "definition_site": "0043f544",
      "incomplete_value": false,
      "site": "0043f550",
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
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f544",
      "incomplete_value": false,
      "site": "0043f550",
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
            "const:258:8"
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
      "0043f550",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f550",
      "DATA",
      [
        "storage",
        "00be7308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f52c.md#insn-0043f544)
- 新版 `0043f544`（命令位置の公開資料なし）

~~~diff
- 0043f544 ["COPY", "tmp:0:8", ["const:258:8"]]
- 0043f544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f544 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 0043f544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f544 bytes 08610991
+ 0043f544 bytes 08210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8743ffc73ff2619212586ad6960e8053"></a>

### [`0043f588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f588.md) → [`0043f588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f588.md) FUN_0043f588

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
      "definition_site": "0043f5b4",
      "incomplete_value": false,
      "site": "0043f5b4",
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
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f5b4",
      "incomplete_value": false,
      "site": "0043f5b4",
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
            "const:258:8"
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
      "0043f5b4",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f5b4",
      "DATA",
      [
        "storage",
        "00be7308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f5ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f588.md#insn-0043f5ac)
- 新版 `0043f5ac`（命令位置の公開資料なし）

~~~diff
- 0043f5ac ["COPY", "tmp:0:8", ["const:258:8"]]
- 0043f5ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f5ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f5ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f5ac ["COPY", "tmp:0:8", ["const:308:8"]]
+ 0043f5ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f5ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f5ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f5ac bytes 08610991
+ 0043f5ac bytes 08210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73a189e4abb19df29d09f61d36ffaaa0"></a>

### [`0043f610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f610.md) → [`0043f610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f610.md) FUN_0043f610

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
      "definition_site": "0043f62c",
      "incomplete_value": false,
      "site": "0043f62c",
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
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f62c",
      "incomplete_value": false,
      "site": "0043f62c",
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
            "const:258:8"
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
      "0043f62c",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f62c",
      "DATA",
      [
        "storage",
        "00be7308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f610.md#insn-0043f628)
- 新版 `0043f628`（命令位置の公開資料なし）

~~~diff
- 0043f628 ["COPY", "tmp:0:8", ["const:258:8"]]
- 0043f628 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043f628 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043f628 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043f628 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 0043f628 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f628 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f628 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043f628 bytes 29610991
+ 0043f628 bytes 29210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae163aadc790067a5e47d091609b0d8e"></a>

### [`0043f7a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f7a8.md) → [`0043f7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f7a8.md) FUN_0043f7a8

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
      "definition_site": "0043f7b4",
      "incomplete_value": false,
      "site": "0043f7c0",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f7b4",
      "incomplete_value": false,
      "site": "0043f7c0",
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
            "const:2d8:8"
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
      "0043f7c0",
      "DATA",
      [
        "storage",
        "00be72d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f7c0",
      "DATA",
      [
        "storage",
        "00be7388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f7b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f7a8.md#insn-0043f7b4)
- 新版 `0043f7b4`（命令位置の公開資料なし）

~~~diff
- 0043f7b4 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0043f7b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043f7b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043f7b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043f7b4 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0043f7b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043f7b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043f7b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043f7b4 bytes 4a610b91
+ 0043f7b4 bytes 4a210e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01f7439dd1b193a2f02d09bb69d0b92d"></a>

### [`0043f7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f7ec.md) → [`0043f7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f7ec.md) FUN_0043f7ec

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
      "definition_site": "0043f804",
      "incomplete_value": false,
      "site": "0043f810",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f804",
      "incomplete_value": false,
      "site": "0043f810",
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
            "const:2d8:8"
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
      "0043f810",
      "DATA",
      [
        "storage",
        "00be72d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f810",
      "DATA",
      [
        "storage",
        "00be7388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f7ec.md#insn-0043f804)
- 新版 `0043f804`（命令位置の公開資料なし）

~~~diff
- 0043f804 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0043f804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f804 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0043f804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f804 bytes 08610b91
+ 0043f804 bytes 08210e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42a4cdf32111e71f7560f9799037f53a"></a>

### [`0043f848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f848.md) → [`0043f848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f848.md) FUN_0043f848

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
      "definition_site": "0043f874",
      "incomplete_value": false,
      "site": "0043f874",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f874",
      "incomplete_value": false,
      "site": "0043f874",
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
      "0043f874",
      "DATA",
      [
        "storage",
        "00be72d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f874",
      "DATA",
      [
        "storage",
        "00be7388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f86c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f848.md#insn-0043f86c)
- 新版 `0043f86c`（命令位置の公開資料なし）

~~~diff
- 0043f86c ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0043f86c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f86c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f86c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f86c ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0043f86c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f86c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f86c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f86c bytes 08610b91
+ 0043f86c bytes 08210e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acfe1a270d6eeb2d5f25ba1b4b9214bb"></a>

### [`0043f8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f8d0.md) → [`0043f8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f8d0.md) FUN_0043f8d0

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
      "definition_site": "0043f8ec",
      "incomplete_value": false,
      "site": "0043f8ec",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f8ec",
      "incomplete_value": false,
      "site": "0043f8ec",
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
            "const:2d8:8"
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
      "0043f8ec",
      "DATA",
      [
        "storage",
        "00be72d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f8ec",
      "DATA",
      [
        "storage",
        "00be7388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f8d0.md#insn-0043f8e8)
- 新版 `0043f8e8`（命令位置の公開資料なし）

~~~diff
- 0043f8e8 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0043f8e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043f8e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043f8e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043f8e8 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0043f8e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f8e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f8e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043f8e8 bytes 29610b91
+ 0043f8e8 bytes 29210e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6629141fd8745ecd6aaaf8ffd573393e"></a>

### [`0043fa68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043fa68.md) → [`0043fa68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043fa68.md) FUN_0043fa68

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
      "definition_site": "0043fa74",
      "incomplete_value": false,
      "site": "0043fa80",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fa74",
      "incomplete_value": false,
      "site": "0043fa80",
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
            "const:358:8"
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
      "0043fa80",
      "DATA",
      [
        "storage",
        "00be7358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043fa80",
      "DATA",
      [
        "storage",
        "00be7408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fa74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043fa68.md#insn-0043fa74)
- 新版 `0043fa74`（命令位置の公開資料なし）

~~~diff
- 0043fa74 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0043fa74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043fa74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043fa74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043fa74 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 0043fa74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043fa74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043fa74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043fa74 bytes 4a610d91
+ 0043fa74 bytes 4a211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f55cebbaa08593411c9179eebf18df8a"></a>

### [`0043faac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043faac.md) → [`0043faac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043faac.md) FUN_0043faac

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
      "definition_site": "0043fac4",
      "incomplete_value": false,
      "site": "0043fad0",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fac4",
      "incomplete_value": false,
      "site": "0043fad0",
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
            "const:358:8"
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
      "0043fad0",
      "DATA",
      [
        "storage",
        "00be7358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043fad0",
      "DATA",
      [
        "storage",
        "00be7408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043faac.md#insn-0043fac4)
- 新版 `0043fac4`（命令位置の公開資料なし）

~~~diff
- 0043fac4 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0043fac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043fac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043fac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043fac4 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 0043fac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043fac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043fac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043fac4 bytes 08610d91
+ 0043fac4 bytes 08211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae9eb05d5d894899d9a9ddc0b17f8023"></a>

### [`0043fb08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043fb08.md) → [`0043fb08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043fb08.md) FUN_0043fb08

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
      "definition_site": "0043fb34",
      "incomplete_value": false,
      "site": "0043fb34",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fb34",
      "incomplete_value": false,
      "site": "0043fb34",
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
            "const:358:8"
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
      "0043fb34",
      "DATA",
      [
        "storage",
        "00be7358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043fb34",
      "DATA",
      [
        "storage",
        "00be7408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fb2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043fb08.md#insn-0043fb2c)
- 新版 `0043fb2c`（命令位置の公開資料なし）

~~~diff
- 0043fb2c ["COPY", "tmp:0:8", ["const:358:8"]]
- 0043fb2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043fb2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043fb2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043fb2c ["COPY", "tmp:0:8", ["const:408:8"]]
+ 0043fb2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043fb2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043fb2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043fb2c bytes 08610d91
+ 0043fb2c bytes 08211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1d871b88444f7e8f17074d1d34f30e5"></a>

### [`0043fb90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043fb90.md) → [`0043fb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043fb90.md) FUN_0043fb90

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
      "definition_site": "0043fbac",
      "incomplete_value": false,
      "site": "0043fbac",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fbac",
      "incomplete_value": false,
      "site": "0043fbac",
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
            "const:358:8"
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
      "0043fbac",
      "DATA",
      [
        "storage",
        "00be7358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043fbac",
      "DATA",
      [
        "storage",
        "00be7408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043fb90.md#insn-0043fba8)
- 新版 `0043fba8`（命令位置の公開資料なし）

~~~diff
- 0043fba8 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0043fba8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043fba8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043fba8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043fba8 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 0043fba8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043fba8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043fba8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043fba8 bytes 29610d91
+ 0043fba8 bytes 29211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db3043553fb5aa88aeba74411c52e342"></a>

### [`0043fee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043fee4.md) → [`0043fee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043fee4.md) FUN_0043fee4

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
      "definition_site": "0043fef0",
      "incomplete_value": false,
      "site": "0043fefc",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fef0",
      "incomplete_value": false,
      "site": "0043fefc",
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
            "const:3d8:8"
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
      "0043fefc",
      "DATA",
      [
        "storage",
        "00be73d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043fefc",
      "DATA",
      [
        "storage",
        "00be7488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043fee4.md#insn-0043fef0)
- 新版 `0043fef0`（命令位置の公開資料なし）

~~~diff
- 0043fef0 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 0043fef0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043fef0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043fef0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043fef0 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 0043fef0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043fef0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043fef0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043fef0 bytes 4a610f91
+ 0043fef0 bytes 4a211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

