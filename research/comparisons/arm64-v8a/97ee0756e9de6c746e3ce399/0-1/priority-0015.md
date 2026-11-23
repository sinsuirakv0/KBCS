# v15.7.2 → v15.7.3 · 最優先の変更候補 (15)

[一覧の目次](README.md)

<a id="compare-236ff76b9f156c284dc1d33cfadeaeed"></a>

### [`00528ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00528/00528ef0.md) → [`00528ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528ef0.md) FUN_00528ef0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00528d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00528/00528d24.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512c94.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00528d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528d24.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00528f2c",
      "incomplete_value": true,
      "site": "00528f30",
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
      "definition_site": "00528f2c",
      "incomplete_value": true,
      "site": "00528f30",
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
      "00528f1c",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ],
    [
      "00528f30",
      "DATA",
      [
        "storage",
        "00be91c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00528f1c",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "00528f30",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00528f1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00528/00528ef0.md#insn-00528f1c)
- 新版 [`00528f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528ef0.md#insn-00528f1c)

~~~diff
- 00528f1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e50:8"]]
- 00528f1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00528f1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 00528f1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00528f1c bytes 082947f9
+ 00528f1c bytes 088147f9
~~~


<a id="compare-5b3a8620ea5a8c5a9b6cb40bfb2269e7"></a>

### [`0052934c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/0052934c.md) → [`0052934c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/0052934c.md) FUN_0052934c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00529214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/00529214.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00529214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/00529214.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00529358",
      "incomplete_value": false,
      "site": "0052935c",
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
      "definition_site": "00529358",
      "incomplete_value": false,
      "site": "0052935c",
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
      "00529358",
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
      "00529358",
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

- 旧版 [`00529358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/0052934c.md#insn-00529358)
- 新版 [`00529358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/0052934c.md#insn-00529358)

~~~diff
- 00529358 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00529358 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00529358 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00529358 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00529358 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00529358 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00529358 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00529358 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00529358 bytes 00280c91
+ 00529358 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71b7583fac79eb015e2fe5cb4e2f6047"></a>

### [`00529858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/00529858.md) → [`00529858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/00529858.md) FUN_00529858

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052968c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/0052968c.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512c94.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`0052968c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/0052968c.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00529894",
      "incomplete_value": true,
      "site": "00529898",
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
      "definition_site": "00529894",
      "incomplete_value": true,
      "site": "00529898",
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
      "00529884",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ],
    [
      "00529898",
      "DATA",
      [
        "storage",
        "00be91c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00529884",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "00529898",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00529884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/00529858.md#insn-00529884)
- 新版 [`00529884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/00529858.md#insn-00529884)

~~~diff
- 00529884 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e50:8"]]
- 00529884 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00529884 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 00529884 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00529884 bytes 082947f9
+ 00529884 bytes 088147f9
~~~


<a id="compare-fd18a6b01ebcff54204b1f99551015c9"></a>

### [`005299a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/005299a4.md) → [`005299a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/005299a4.md) FUN_005299a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f78a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f78a4.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0051a920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051a/0051a920.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`004f78a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f78a4.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0051a920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051a/0051a920.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.75% / 新版 96.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00529a7c",
      "incomplete_value": true,
      "site": "00529a7c",
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
      "definition_site": "00529a7c",
      "incomplete_value": true,
      "site": "00529a7c",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00529a7c",
      "incomplete_value": true,
      "site": "00529a7c",
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
      "definition_site": "00529a7c",
      "incomplete_value": true,
      "site": "00529a7c",
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
      "00529a64",
      "READ",
      [
        "storage",
        "00c1b260",
        null,
        "pointer"
      ]
    ],
    [
      "00529a68",
      "READ",
      [
        "storage",
        "00c1b238",
        null,
        "pointer"
      ]
    ],
    [
      "00529a7c",
      "DATA",
      [
        "storage",
        "00beb058",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00529a64",
      "READ",
      [
        "storage",
        "00c1b310",
        null,
        "pointer"
      ]
    ],
    [
      "00529a68",
      "READ",
      [
        "storage",
        "00c1b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "00529a7c",
      "DATA",
      [
        "storage",
        "00beb108",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00529a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/005299a4.md#insn-00529a64) · [`00529a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/005299a4.md#insn-00529a68)
- 新版 [`00529a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/005299a4.md#insn-00529a64) · [`00529a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/005299a4.md#insn-00529a68)

~~~diff
- 00529a64 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:260:8"]]
- 00529a64 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00529a64 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:310:8"]]
+ 00529a64 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 00529a64 bytes 393341f9
+ 00529a64 bytes 398b41f9
- 00529a68 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:238:8"]]
- 00529a68 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00529a68 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:2e8:8"]]
+ 00529a68 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00529a68 bytes 5a1f41f9
+ 00529a68 bytes 5a7741f9
~~~


<a id="compare-8d4052215f716c206278bc1d1050b28a"></a>

### [`00529cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/00529cc4.md) → [`00529cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/00529cc4.md) FUN_00529cc4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`004f8244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f8/004f8244.md) [`00504f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00504/00504f50.md) [`005054cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00505/005054cc.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`004f8244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8244.md) [`00504f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504f50.md) [`005054cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00505/005054cc.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "00529cd0",
      "incomplete_value": true,
      "site": "00529cd4",
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
      "definition_site": "00529cd0",
      "incomplete_value": true,
      "site": "00529cd4",
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
      "00529cd0",
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
      "00529cd0",
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

- 旧版 [`00529cd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/00529cc4.md#insn-00529cd0)
- 新版 [`00529cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/00529cc4.md#insn-00529cd0)

~~~diff
- 00529cd0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00529cd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00529cd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00529cd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00529cd0 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00529cd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00529cd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00529cd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00529cd0 bytes 00280c91
+ 00529cd0 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90baa6c3285a1c3a2ba9dd85aa1fee40"></a>

### [`00529d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/00529d48.md) → [`00529d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/00529d48.md) FUN_00529d48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004f8c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f8/004f8c10.md) [`004f9190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f9190.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`004f8c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8c10.md) [`004f9190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9190.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00529d54",
      "incomplete_value": false,
      "site": "00529d58",
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
      "definition_site": "00529d54",
      "incomplete_value": false,
      "site": "00529d58",
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
      "00529d54",
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
      "00529d54",
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

- 旧版 [`00529d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/00529d48.md#insn-00529d54)
- 新版 [`00529d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/00529d48.md#insn-00529d54)

~~~diff
- 00529d54 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00529d54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00529d54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00529d54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00529d54 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00529d54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00529d54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00529d54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00529d54 bytes 00280c91
+ 00529d54 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f1f28057083425668b8db83c4d77b6b"></a>

### [`0052a264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052a/0052a264.md) → [`0052a264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052a/0052a264.md) FUN_0052a264

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004fb4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb4c0.md) · 呼出先 9件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/005180b8.md) [`00519a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00519/00519a68.md) [`0051cdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051c/0051cdc8.md)
- 新版 呼出元 1件 [`004fb4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb4c0.md) · 呼出先 9件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005180b8.md) [`00519a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00519/00519a68.md) [`0051cdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051cdc8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.81% / 新版 96.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052a310",
      "incomplete_value": true,
      "site": "0052a310",
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
      "definition_site": "0052a310",
      "incomplete_value": true,
      "site": "0052a310",
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
      "0052a2fc",
      "READ",
      [
        "storage",
        "00c1b2f8",
        null,
        "pointer"
      ]
    ],
    [
      "0052a310",
      "DATA",
      [
        "storage",
        "00bebd68",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0052a2fc",
      "READ",
      [
        "storage",
        "00c1b3a8",
        null,
        "pointer"
      ]
    ],
    [
      "0052a310",
      "DATA",
      [
        "storage",
        "00bebe18",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052a2fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052a/0052a264.md#insn-0052a2fc)
- 新版 [`0052a2fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052a/0052a264.md#insn-0052a2fc)

~~~diff
- 0052a2fc ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:2f8:8"]]
- 0052a2fc ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052a2fc ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:3a8:8"]]
+ 0052a2fc ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 0052a2fc bytes 4a7d41f9
+ 0052a2fc bytes 4ad541f9
~~~


<a id="compare-0b5d5d62e6411b991b94f48ab9ed0a69"></a>

### [`0052ab40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052a/0052ab40.md) → [`0052ab40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052a/0052ab40.md) FUN_0052ab40

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00504f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00504/00504f50.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`00504f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504f50.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "0052ab4c",
      "incomplete_value": false,
      "site": "0052ab50",
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
      "definition_site": "0052ab4c",
      "incomplete_value": false,
      "site": "0052ab50",
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
      "0052ab4c",
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
      "0052ab4c",
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

- 旧版 [`0052ab4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052a/0052ab40.md#insn-0052ab4c)
- 新版 [`0052ab4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052a/0052ab40.md#insn-0052ab4c)

~~~diff
- 0052ab4c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0052ab4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0052ab4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0052ab4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0052ab4c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0052ab4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0052ab4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0052ab4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0052ab4c bytes 00280c91
+ 0052ab4c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbafb357a510ad499163e30fdef56083"></a>

### [`0052acbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052a/0052acbc.md) → [`0052acbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052a/0052acbc.md) FUN_0052acbc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052b868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052b/0052b868.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0052b868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052b/0052b868.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0052acc8",
      "incomplete_value": false,
      "site": "0052accc",
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
      "definition_site": "0052acc8",
      "incomplete_value": false,
      "site": "0052accc",
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
      "0052acc8",
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
      "0052acc8",
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

- 旧版 [`0052acc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052a/0052acbc.md#insn-0052acc8)
- 新版 [`0052acc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052a/0052acbc.md#insn-0052acc8)

~~~diff
- 0052acc8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0052acc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0052acc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0052acc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0052acc8 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0052acc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0052acc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0052acc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0052acc8 bytes 00280c91
+ 0052acc8 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1550de058a9649bae2b0852b81c9bc79"></a>

### [`0052ae7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052a/0052ae7c.md) → [`0052ae7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052a/0052ae7c.md) FUN_0052ae7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00506ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00506/00506ee0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00506ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/00506ee0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0052ae88",
      "incomplete_value": false,
      "site": "0052ae8c",
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
      "definition_site": "0052ae88",
      "incomplete_value": false,
      "site": "0052ae8c",
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
      "0052ae88",
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
      "0052ae88",
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

- 旧版 [`0052ae88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052a/0052ae7c.md#insn-0052ae88)
- 新版 [`0052ae88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052a/0052ae7c.md#insn-0052ae88)

~~~diff
- 0052ae88 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0052ae88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0052ae88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0052ae88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0052ae88 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0052ae88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0052ae88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0052ae88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0052ae88 bytes 00280c91
+ 0052ae88 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9b48bea476c419b3648ae1fec5ff7fa"></a>

### [`0052b348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052b/0052b348.md) → [`0052b348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052b/0052b348.md) FUN_0052b348

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052ae90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052a/0052ae90.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0052ae90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052a/0052ae90.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0052b354",
      "incomplete_value": false,
      "site": "0052b358",
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
      "definition_site": "0052b354",
      "incomplete_value": false,
      "site": "0052b358",
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
      "0052b354",
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
      "0052b354",
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

- 旧版 [`0052b354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052b/0052b348.md#insn-0052b354)
- 新版 [`0052b354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052b/0052b348.md#insn-0052b354)

~~~diff
- 0052b354 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0052b354 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0052b354 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0052b354 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0052b354 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0052b354 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0052b354 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0052b354 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0052b354 bytes 00280c91
+ 0052b354 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2528907fbc66f23815de4733206a1f70"></a>

### [`0052c024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052c/0052c024.md) → [`0052c024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052c/0052c024.md) FUN_0052c024

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052be2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052b/0052be2c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0052be2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052b/0052be2c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0052c030",
      "incomplete_value": false,
      "site": "0052c034",
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
      "definition_site": "0052c030",
      "incomplete_value": false,
      "site": "0052c034",
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
      "0052c030",
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
      "0052c030",
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

- 旧版 [`0052c030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052c/0052c024.md#insn-0052c030)
- 新版 [`0052c030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052c/0052c024.md#insn-0052c030)

~~~diff
- 0052c030 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0052c030 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0052c030 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0052c030 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0052c030 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0052c030 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0052c030 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0052c030 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0052c030 bytes 00280c91
+ 0052c030 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0177c3188dfd5b64933025f14e273e09"></a>

### [`0052c558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052c/0052c558.md) → [`0052c558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052c/0052c558.md) _INIT_25

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00450668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/00450668.md) [`004c45bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c4/004c45bc.md) [`004c4764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c4/004c4764.md) [`004f25dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f25dc.md) [`004f26f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f26f8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`004c45bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c45bc.md) [`004c4764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c4764.md) [`004f25dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f25dc.md) [`004f26f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f26f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052c87c",
      "incomplete_value": false,
      "site": "0052c890",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052c87c",
      "incomplete_value": false,
      "site": "0052c890",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052cb74",
      "incomplete_value": false,
      "site": "0052cb80",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052cb74",
      "incomplete_value": false,
      "site": "0052cb80",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052cb7c",
      "incomplete_value": false,
      "site": "0052cb80",
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
      "definition_site": "0052cb7c",
      "incomplete_value": false,
      "site": "0052cb80",
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
    "ordinal": 35,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0052c87c",
      "PARAM",
      [
        "storage",
        "00c252a8",
        null,
        null
      ]
    ],
    [
      "0052cb74",
      "PARAM",
      [
        "storage",
        "00c252a8",
        null,
        null
      ]
    ],
    [
      "0052cb7c",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052c87c",
      "PARAM",
      [
        "storage",
        "00c25368",
        null,
        null
      ]
    ],
    [
      "0052cb74",
      "PARAM",
      [
        "storage",
        "00c25368",
        null,
        null
      ]
    ],
    [
      "0052cb7c",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052c87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052c/0052c558.md#insn-0052c87c) · [`0052cb74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052c/0052c558.md#insn-0052cb74) · [`0052cb7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052c/0052c558.md#insn-0052cb7c)
- 新版 [`0052c87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052c/0052c558.md#insn-0052c87c) · [`0052cb74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052c/0052c558.md#insn-0052cb74) · [`0052cb7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052c/0052c558.md#insn-0052cb7c)

~~~diff
- 0052c87c ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 0052c87c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0052c87c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0052c87c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0052c87c ["COPY", "tmp:0:8", ["const:368:8"]]
+ 0052c87c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0052c87c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0052c87c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0052c87c bytes 00a00a91
+ 0052c87c bytes 00a00d91
- 0052cb74 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 0052cb74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052cb74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052cb74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052cb74 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 0052cb74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052cb74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052cb74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052cb74 bytes 21a00a91
+ 0052cb74 bytes 21a00d91
- 0052cb7c ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 0052cb7c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0052cb7c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0052cb7c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0052cb7c ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 0052cb7c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0052cb7c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0052cb7c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0052cb7c bytes 42403b91
+ 0052cb7c bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dc2f5ccb0afb473f573a9976c5df153"></a>

### [`0052db54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db54.md) → [`0052db54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db54.md) FUN_0052db54

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052db6c",
      "incomplete_value": true,
      "site": "0052db70",
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
      "definition_site": "0052db6c",
      "incomplete_value": true,
      "site": "0052db70",
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
      "0052db68",
      "READ",
      [
        "storage",
        "00c1b338",
        null,
        "pointer"
      ]
    ],
    [
      "0052db70",
      "DATA",
      [
        "storage",
        "00beda80",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "0052db68",
      "READ",
      [
        "storage",
        "00c1b3e8",
        null,
        "pointer"
      ]
    ],
    [
      "0052db70",
      "DATA",
      [
        "storage",
        "00bedb30",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052db68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db54.md#insn-0052db68)
- 新版 [`0052db68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db54.md#insn-0052db68)

~~~diff
- 0052db68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
- 0052db68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052db68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3e8:8"]]
+ 0052db68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052db68 bytes 089d41f9
+ 0052db68 bytes 08f541f9
~~~


<a id="compare-39294244599b141d294cad57b4da21a7"></a>

### [`0052db94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db94.md) → [`0052db94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db94.md) FUN_0052db94

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052db88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db88.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377f0.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md)
- 新版 呼出元 1件 [`0052db88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db88.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377f0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md)

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
      "definition_site": "0052dc38",
      "incomplete_value": true,
      "site": "0052dc3c",
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
      "definition_site": "0052dc38",
      "incomplete_value": true,
      "site": "0052dc3c",
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
      "definition_site": "0052dc14",
      "incomplete_value": true,
      "site": "0052dc1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052dc14",
      "incomplete_value": true,
      "site": "0052dc1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0052dc14",
      "READ",
      [
        "storage",
        "00c1ad68",
        null,
        "pointer"
      ]
    ],
    [
      "0052dc14",
      "PARAM",
      [
        "storage",
        "00c12e08",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0052dc34",
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
      "0052dc14",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0052dc14",
      "PARAM",
      [
        "storage",
        "00c12eb8",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0052dc34",
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

- 旧版 [`0052dc14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db94.md#insn-0052dc14) · [`0052dc34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db94.md#insn-0052dc34)
- 新版 [`0052dc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db94.md#insn-0052dc14) · [`0052dc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db94.md#insn-0052dc34)

~~~diff
- 0052dc14 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d68:8"]]
- 0052dc14 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052dc14 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
+ 0052dc14 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0052dc14 bytes 21b446f9
+ 0052dc14 bytes 210c47f9
- 0052dc34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 0052dc34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052dc34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e20:8"]]
+ 0052dc34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052dc34 bytes 08b946f9
+ 0052dc34 bytes 081147f9
~~~


<a id="compare-c6df50c89821426287c2ffb948121bb3"></a>

### [`0052e05c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052e/0052e05c.md) → [`0052e05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e05c.md) FUN_0052e05c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005321d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005321d8.md) · 呼出先 5件 [`0053b668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b668.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`005321d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005321d8.md) · 呼出先 5件 [`0053b668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b668.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.91% / 新版 95.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e0a0",
      "incomplete_value": false,
      "site": "0052e0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052e0a0",
      "incomplete_value": false,
      "site": "0052e0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "0052e0a4",
      "DATA",
      [
        "storage",
        "00bedb20",
        null,
        "undefined *"
      ]
    ],
    [
      "0052e0c0",
      "DATA",
      [
        "storage",
        "00bedb88",
        null,
        "undefined *"
      ]
    ],
    [
      "0052e0dc",
      "READ",
      [
        "storage",
        "00c1b350",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052e0a4",
      "DATA",
      [
        "storage",
        "00bedbd0",
        null,
        "undefined *"
      ]
    ],
    [
      "0052e0c0",
      "DATA",
      [
        "storage",
        "00bedc38",
        null,
        "undefined *"
      ]
    ],
    [
      "0052e0dc",
      "READ",
      [
        "storage",
        "00c1b400",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052e0a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052e/0052e05c.md#insn-0052e0a0) · [`0052e0dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052e/0052e05c.md#insn-0052e0dc)
- 新版 [`0052e0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e05c.md#insn-0052e0a0) · [`0052e0dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e05c.md#insn-0052e0dc)

~~~diff
- 0052e0a0 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 0052e0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0052e0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0052e0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0052e0a0 ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 0052e0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0052e0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0052e0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0052e0a0 bytes 08812c91
+ 0052e0a0 bytes 08412f91
- 0052e0dc ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:350:8"]]
- 0052e0dc ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052e0dc ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:400:8"]]
+ 0052e0dc ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0052e0dc bytes 39ab41f9
+ 0052e0dc bytes 390342f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-734cc8802f6a2bf6f2ebdf20790d6a54"></a>

### [`0052e39c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052e/0052e39c.md) → [`0052e39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e39c.md) FUN_0052e39c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`005f2980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a4/008a4e38.md) · 呼出先 6件 [`0052f11c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f11c.md) [`0053980c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/0053980c.md) [`00574ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 4件 [`005f2980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a4/008a4e38.md) · 呼出先 6件 [`0052f11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md) [`0053980c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053980c.md) [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.36% / 新版 90.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e3f0",
      "incomplete_value": true,
      "site": "0052e400",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a37:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052e3f0",
      "incomplete_value": true,
      "site": "0052e400",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9aa:8"
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
      "definition_site": "0052e3f0",
      "incomplete_value": true,
      "site": "0052e400",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0052e3f0",
      "incomplete_value": true,
      "site": "0052e400",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e404",
      "incomplete_value": true,
      "site": "0052e410",
      "value": [
        "LOAD",
        "16",
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
                "const:1c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052e404",
      "incomplete_value": true,
      "site": "0052e410",
      "value": [
        "LOAD",
        "16",
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
                "const:1c:8"
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
      "0052e3f0",
      "READ",
      [
        "storage",
        "002939aa",
        null,
        "string"
      ]
    ],
    [
      "0052e3f0",
      "READ",
      [
        "storage",
        "002939ba",
        null,
        "string"
      ]
    ],
    [
      "0052e404",
      "READ",
      [
        "storage",
        "002939c6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0052e3f0",
      "READ",
      [
        "storage",
        "00293a37",
        null,
        "string"
      ]
    ],
    [
      "0052e3f0",
      "READ",
      [
        "storage",
        "00293a47",
        null,
        "string"
      ]
    ],
    [
      "0052e404",
      "READ",
      [
        "storage",
        "00293a53",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052e3e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052e/0052e39c.md#insn-0052e3e8) · [`0052e3ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052e/0052e39c.md#insn-0052e3ec)
- 新版 [`0052e3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e39c.md#insn-0052e3e8) · [`0052e3ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e39c.md#insn-0052e3ec)

~~~diff
- 0052e3e8 ["COPY", "tmp:0:8", ["const:9aa:8"]]
- 0052e3e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0052e3e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0052e3e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0052e3e8 ["COPY", "tmp:0:8", ["const:a37:8"]]
+ 0052e3e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0052e3e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0052e3e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0052e3e8 bytes 08a92691
+ 0052e3e8 bytes 08dd2891
- 0052e3ec ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0052e3ec bytes 09ecfff0
+ 0052e3ec ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0052e3ec bytes 09ecfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1fd61c30e23bdd3c9ee75cbecba9963"></a>

### [`0052eee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052e/0052eee8.md) → [`0052eee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052eee8.md) FUN_0052eee8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0053b74c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b74c.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0053b74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b74c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052ef38",
      "incomplete_value": true,
      "site": "0052ef38",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052ef38",
      "incomplete_value": true,
      "site": "0052ef38",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "0052ef28",
      "incomplete_value": true,
      "site": "0052ef38",
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
      "definition_site": "0052ef28",
      "incomplete_value": true,
      "site": "0052ef38",
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
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0052ef20",
      "READ",
      [
        "storage",
        "00c1b350",
        null,
        "pointer"
      ]
    ],
    [
      "0052ef28",
      "READ",
      [
        "storage",
        "00c26550",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0052ef20",
      "READ",
      [
        "storage",
        "00c1b400",
        null,
        "pointer"
      ]
    ],
    [
      "0052ef28",
      "READ",
      [
        "storage",
        "00c26610",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052ef20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052e/0052eee8.md#insn-0052ef20)
- 新版 [`0052ef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052eee8.md#insn-0052ef20)

~~~diff
- 0052ef20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
- 0052ef20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052ef20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:400:8"]]
+ 0052ef20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052ef20 bytes 08a941f9
+ 0052ef20 bytes 080142f9
~~~


<a id="compare-8b701a34b3980c5895a56f212c30a70a"></a>

### [`0052f034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f034.md) → [`0052f034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f034.md) FUN_0052f034

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b6d4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052f044",
      "incomplete_value": true,
      "site": "0052f050",
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
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f044",
      "incomplete_value": true,
      "site": "0052f050",
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
            "const:b20:8"
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
      "definition_site": "0052f054",
      "incomplete_value": true,
      "site": "0052f058",
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
                "const:bd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f054",
      "incomplete_value": true,
      "site": "0052f058",
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
                "const:b20:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "0052f050",
      "DATA",
      [
        "storage",
        "00bedb20",
        null,
        "undefined *"
      ]
    ],
    [
      "0052f058",
      "DATA",
      [
        "storage",
        "00bedb88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0052f050",
      "DATA",
      [
        "storage",
        "00bedbd0",
        null,
        "undefined *"
      ]
    ],
    [
      "0052f058",
      "DATA",
      [
        "storage",
        "00bedc38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f034.md#insn-0052f044)
- 新版 [`0052f044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f034.md#insn-0052f044)

~~~diff
- 0052f044 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 0052f044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0052f044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0052f044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0052f044 ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 0052f044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0052f044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0052f044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0052f044 bytes 08812c91
+ 0052f044 bytes 08412f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c019e3812d0c1b3bf5dfa26a1c88fa07"></a>

### [`0052f0a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f0a4.md) → [`0052f0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f0a4.md) FUN_0052f0a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0053b6d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b6d4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0053b6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0052f0b4",
      "incomplete_value": false,
      "site": "0052f0c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f0b4",
      "incomplete_value": false,
      "site": "0052f0c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "0052f0c4",
      "incomplete_value": false,
      "site": "0052f0c8",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:bd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f0c4",
      "incomplete_value": false,
      "site": "0052f0c8",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:b20:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "0052f0c0",
      "DATA",
      [
        "storage",
        "00bedb20",
        null,
        "undefined *"
      ]
    ],
    [
      "0052f0c8",
      "DATA",
      [
        "storage",
        "00bedb88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0052f0c0",
      "DATA",
      [
        "storage",
        "00bedbd0",
        null,
        "undefined *"
      ]
    ],
    [
      "0052f0c8",
      "DATA",
      [
        "storage",
        "00bedc38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f0b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f0a4.md#insn-0052f0b4)
- 新版 [`0052f0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f0a4.md#insn-0052f0b4)

~~~diff
- 0052f0b4 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 0052f0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0052f0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0052f0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0052f0b4 ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 0052f0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0052f0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0052f0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0052f0b4 bytes 08812c91
+ 0052f0b4 bytes 08412f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2665af2532a0ad6c29fc458c0c8f451f"></a>

### [`0052f11c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f11c.md) → [`0052f11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md) FUN_0052f11c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0052e39c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052e/0052e39c.md) [`0052f11c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f11c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0052e39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e39c.md) [`0052f11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.96% / 新版 98.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052f284",
      "incomplete_value": false,
      "site": "0052f28c",
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
      "definition_site": "0052f284",
      "incomplete_value": false,
      "site": "0052f28c",
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
      "definition_site": "0052f3e4",
      "incomplete_value": false,
      "site": "0052f3ec",
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
      "definition_site": "0052f3e4",
      "incomplete_value": false,
      "site": "0052f3ec",
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
      "definition_site": "0052f6c0",
      "incomplete_value": false,
      "site": "0052f6d0",
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
      "definition_site": "0052f6c0",
      "incomplete_value": false,
      "site": "0052f6d0",
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
      "0052f284",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0052f3e4",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0052f48c",
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
      "0052f284",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0052f3e4",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0052f48c",
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

- 旧版 [`0052f284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f11c.md#insn-0052f284) · [`0052f3e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f11c.md#insn-0052f3e4) · [`0052f48c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f11c.md#insn-0052f48c)
- 新版 [`0052f284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md#insn-0052f284) · [`0052f3e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md#insn-0052f3e4) · [`0052f48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md#insn-0052f48c)

~~~diff
- 0052f284 ["COPY", "tmp:0:8", ["const:311:8"]]
- 0052f284 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052f284 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052f284 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052f284 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0052f284 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052f284 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052f284 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052f284 bytes 21440c91
+ 0052f284 bytes 21280c91
- 0052f3e4 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0052f3e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052f3e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052f3e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052f3e4 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0052f3e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052f3e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052f3e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052f3e4 bytes 21d40b91
+ 0052f3e4 bytes 21b80b91
- 0052f48c ["COPY", "tmp:0:8", ["const:7da:8"]]
- 0052f48c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052f48c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052f48c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052f48c ["COPY", "tmp:0:8", ["const:867:8"]]
+ 0052f48c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052f48c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052f48c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052f48c bytes 21681f91
+ 0052f48c bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fdf28018ff9df55654d8d4aad7fa924"></a>

### [`0052f968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f968.md) → [`0052f968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f968.md) FUN_0052f968

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0052f11c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f11c.md) [`0052f968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f968.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0052f11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md) [`0052f968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f968.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.95% / 新版 98.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052facc",
      "incomplete_value": false,
      "site": "0052fad4",
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
      "definition_site": "0052facc",
      "incomplete_value": false,
      "site": "0052fad4",
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
      "definition_site": "0052fc2c",
      "incomplete_value": false,
      "site": "0052fc34",
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
      "definition_site": "0052fc2c",
      "incomplete_value": false,
      "site": "0052fc34",
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
      "definition_site": "0052ff00",
      "incomplete_value": false,
      "site": "0052ff10",
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
      "definition_site": "0052ff00",
      "incomplete_value": false,
      "site": "0052ff10",
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
      "0052facc",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0052fc2c",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0052fcd4",
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
      "0052facc",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0052fc2c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0052fcd4",
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

- 旧版 [`0052facc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f968.md#insn-0052facc) · [`0052fc2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f968.md#insn-0052fc2c) · [`0052fcd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f968.md#insn-0052fcd4)
- 新版 [`0052facc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f968.md#insn-0052facc) · [`0052fc2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f968.md#insn-0052fc2c) · [`0052fcd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f968.md#insn-0052fcd4)

~~~diff
- 0052facc ["COPY", "tmp:0:8", ["const:311:8"]]
- 0052facc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052facc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052facc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052facc ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0052facc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052facc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052facc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052facc bytes 21440c91
+ 0052facc bytes 21280c91
- 0052fc2c ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0052fc2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052fc2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052fc2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052fc2c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0052fc2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052fc2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052fc2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052fc2c bytes 21d40b91
+ 0052fc2c bytes 21b80b91
- 0052fcd4 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 0052fcd4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052fcd4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052fcd4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052fcd4 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 0052fcd4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052fcd4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052fcd4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052fcd4 bytes 21681f91
+ 0052fcd4 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d2448e0953f572e2d00811ac42c4a2e"></a>

### [`005301a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00530/005301a0.md) → [`005301a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005301a0.md) FUN_005301a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0052f968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f968.md) [`005301a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00530/005301a0.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0052f968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f968.md) [`005301a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005301a0.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.95% / 新版 98.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00530300",
      "incomplete_value": false,
      "site": "00530308",
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
      "definition_site": "00530300",
      "incomplete_value": false,
      "site": "00530308",
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
      "definition_site": "00530460",
      "incomplete_value": false,
      "site": "00530468",
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
      "definition_site": "00530460",
      "incomplete_value": false,
      "site": "00530468",
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
      "definition_site": "00530508",
      "incomplete_value": false,
      "site": "00530514",
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
      "definition_site": "00530508",
      "incomplete_value": false,
      "site": "00530514",
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
      "00530300",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00530460",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00530508",
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
      "00530300",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00530460",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00530508",
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

- 旧版 [`00530300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00530/005301a0.md#insn-00530300) · [`00530460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00530/005301a0.md#insn-00530460) · [`00530508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00530/005301a0.md#insn-00530508)
- 新版 [`00530300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005301a0.md#insn-00530300) · [`00530460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005301a0.md#insn-00530460) · [`00530508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005301a0.md#insn-00530508)

~~~diff
- 00530300 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00530300 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00530300 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00530300 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00530300 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00530300 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00530300 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00530300 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00530300 bytes 21440c91
+ 00530300 bytes 21280c91
- 00530460 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00530460 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00530460 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00530460 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00530460 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00530460 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00530460 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00530460 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00530460 bytes 21d40b91
+ 00530460 bytes 21b80b91
- 00530508 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00530508 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00530508 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00530508 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00530508 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00530508 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00530508 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00530508 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00530508 bytes 21681f91
+ 00530508 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1ef2d3adae945b1806b5ce5a75d9afe"></a>

### [`005309d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00530/005309d4.md) → [`005309d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005309d4.md) FUN_005309d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005301a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00530/005301a0.md) [`005309d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00530/005309d4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`005301a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005301a0.md) [`005309d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005309d4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00530b30",
      "incomplete_value": false,
      "site": "00530b38",
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
      "definition_site": "00530b30",
      "incomplete_value": false,
      "site": "00530b38",
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
      "definition_site": "00530c90",
      "incomplete_value": false,
      "site": "00530c98",
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
      "definition_site": "00530c90",
      "incomplete_value": false,
      "site": "00530c98",
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
      "definition_site": "00530f5c",
      "incomplete_value": false,
      "site": "00530f6c",
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
      "definition_site": "00530f5c",
      "incomplete_value": false,
      "site": "00530f6c",
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
      "00530b30",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00530c90",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00530d38",
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
      "00530b30",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00530c90",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00530d38",
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

- 旧版 [`00530b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00530/005309d4.md#insn-00530b30) · [`00530c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00530/005309d4.md#insn-00530c90) · [`00530d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00530/005309d4.md#insn-00530d38)
- 新版 [`00530b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005309d4.md#insn-00530b30) · [`00530c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005309d4.md#insn-00530c90) · [`00530d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005309d4.md#insn-00530d38)

~~~diff
- 00530b30 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00530b30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00530b30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00530b30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00530b30 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00530b30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00530b30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00530b30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00530b30 bytes 21440c91
+ 00530b30 bytes 21280c91
- 00530c90 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00530c90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00530c90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00530c90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00530c90 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00530c90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00530c90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00530c90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00530c90 bytes 21d40b91
+ 00530c90 bytes 21b80b91
- 00530d38 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00530d38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00530d38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00530d38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00530d38 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00530d38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00530d38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00530d38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00530d38 bytes 21681f91
+ 00530d38 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf85151cfb934983fee434e08795a8c7"></a>

### [`005311f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00531/005311f4.md) → [`005311f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005311f4.md) FUN_005311f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005309d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00530/005309d4.md) [`005311f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00531/005311f4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`005309d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005309d4.md) [`005311f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005311f4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00531348",
      "incomplete_value": false,
      "site": "00531350",
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
      "definition_site": "00531348",
      "incomplete_value": false,
      "site": "00531350",
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
      "definition_site": "005314a4",
      "incomplete_value": false,
      "site": "005314ac",
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
      "definition_site": "005314a4",
      "incomplete_value": false,
      "site": "005314ac",
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
      "definition_site": "00531548",
      "incomplete_value": false,
      "site": "00531554",
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
      "definition_site": "00531548",
      "incomplete_value": false,
      "site": "00531554",
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
      "00531348",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "005314a4",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00531548",
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
      "00531348",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005314a4",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00531548",
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

- 旧版 [`00531348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00531/005311f4.md#insn-00531348) · [`005314a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00531/005311f4.md#insn-005314a4) · [`00531548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00531/005311f4.md#insn-00531548)
- 新版 [`00531348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005311f4.md#insn-00531348) · [`005314a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005311f4.md#insn-005314a4) · [`00531548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005311f4.md#insn-00531548)

~~~diff
- 00531348 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00531348 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00531348 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00531348 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00531348 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00531348 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00531348 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00531348 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00531348 bytes 21440c91
+ 00531348 bytes 21280c91
- 005314a4 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 005314a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005314a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005314a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005314a4 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 005314a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005314a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005314a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005314a4 bytes 21d40b91
+ 005314a4 bytes 21b80b91
- 00531548 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00531548 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00531548 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00531548 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00531548 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00531548 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00531548 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00531548 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00531548 bytes 21681f91
+ 00531548 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d87f74575b28dde5d6aa593043cc9de"></a>

### [`005319f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00531/005319f0.md) → [`005319f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005319f0.md) FUN_005319f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005311f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00531/005311f4.md) [`005319f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00531/005319f0.md) [`00829478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00829/00829478.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`005311f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005311f4.md) [`005319f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005319f0.md) [`00829478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

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
      "definition_site": "00531b40",
      "incomplete_value": false,
      "site": "00531b48",
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
      "definition_site": "00531b40",
      "incomplete_value": false,
      "site": "00531b48",
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
      "definition_site": "00531c9c",
      "incomplete_value": false,
      "site": "00531ca4",
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
      "definition_site": "00531c9c",
      "incomplete_value": false,
      "site": "00531ca4",
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
      "definition_site": "00531f50",
      "incomplete_value": false,
      "site": "00531f60",
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
      "definition_site": "00531f50",
      "incomplete_value": false,
      "site": "00531f60",
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
      "00531b40",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00531c9c",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00531d40",
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
      "00531b40",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00531c9c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00531d40",
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

- 旧版 [`00531b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00531/005319f0.md#insn-00531b40) · [`00531c9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00531/005319f0.md#insn-00531c9c) · [`00531d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00531/005319f0.md#insn-00531d40)
- 新版 [`00531b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005319f0.md#insn-00531b40) · [`00531c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005319f0.md#insn-00531c9c) · [`00531d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005319f0.md#insn-00531d40)

~~~diff
- 00531b40 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00531b40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00531b40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00531b40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00531b40 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00531b40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00531b40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00531b40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00531b40 bytes 21440c91
+ 00531b40 bytes 21280c91
- 00531c9c ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00531c9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00531c9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00531c9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00531c9c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00531c9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00531c9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00531c9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00531c9c bytes 21d40b91
+ 00531c9c bytes 21b80b91
- 00531d40 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00531d40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00531d40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00531d40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00531d40 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00531d40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00531d40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00531d40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00531d40 bytes 21681f91
+ 00531d40 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63065cae960f709b96f45f85c0182e14"></a>

### [`005321d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005321d8.md) → [`005321d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005321d8.md) FUN_005321d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0052efd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052e/0052efd4.md) · 呼出先 6件 [`0052e05c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052e/0052e05c.md) [`0053233c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/0053233c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0052efd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052efd4.md) · 呼出先 6件 [`0052e05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e05c.md) [`0053233c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053233c.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00532210",
      "incomplete_value": false,
      "site": "0053222c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532210",
      "incomplete_value": false,
      "site": "0053222c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:c18:8"
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
      "0053222c",
      "DATA",
      [
        "storage",
        "00bedc18",
        null,
        "pointer"
      ]
    ],
    [
      "005322c0",
      "READ",
      [
        "storage",
        "00bedc28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053222c",
      "DATA",
      [
        "storage",
        "00bedcc8",
        null,
        "pointer"
      ]
    ],
    [
      "005322c0",
      "READ",
      [
        "storage",
        "00bedcd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005321d8.md#insn-00532210)
- 新版 [`00532210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005321d8.md#insn-00532210)

~~~diff
- 00532210 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 00532210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00532210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00532210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00532210 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 00532210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00532210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00532210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00532210 bytes 08613091
+ 00532210 bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f93e80e6f8f9f93af41630bc72d1901"></a>

### [`005322fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005322fc.md) → [`005322fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005322fc.md) FUN_005322fc

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
      "definition_site": "00532300",
      "incomplete_value": false,
      "site": "00532304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532300",
      "incomplete_value": false,
      "site": "00532304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:c18:8"
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
      "00532304",
      "DATA",
      [
        "storage",
        "00bedc18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00532304",
      "DATA",
      [
        "storage",
        "00bedcc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005322fc.md#insn-00532300)
- 新版 [`00532300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005322fc.md#insn-00532300)

~~~diff
- 00532300 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 00532300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00532300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00532300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00532300 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 00532300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00532300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00532300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00532300 bytes 08613091
+ 00532300 bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23ba56edaf46568fee4950c1974206da"></a>

### [`0053230c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/0053230c.md) → [`0053230c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053230c.md) FUN_0053230c

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
      "definition_site": "0053231c",
      "incomplete_value": false,
      "site": "00532324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053231c",
      "incomplete_value": false,
      "site": "00532324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:c18:8"
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
      "00532324",
      "DATA",
      [
        "storage",
        "00bedc18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00532324",
      "DATA",
      [
        "storage",
        "00bedcc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053231c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/0053230c.md#insn-0053231c)
- 新版 [`0053231c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053230c.md#insn-0053231c)

~~~diff
- 0053231c ["COPY", "tmp:0:8", ["const:c18:8"]]
- 0053231c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053231c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053231c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053231c ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 0053231c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053231c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053231c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053231c bytes 08613091
+ 0053231c bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9ffa4bf35bfc77b04d9c24eaa3e8c42"></a>

### [`0053239c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/0053239c.md) → [`0053239c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053239c.md) FUN_0053239c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0056dee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056d/0056dee0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0056dee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056d/0056dee0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005323a8",
      "incomplete_value": false,
      "site": "005323a8",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005323a8",
      "incomplete_value": false,
      "site": "005323a8",
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
            "const:c48:8"
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
      "005323a0",
      "READ",
      [
        "storage",
        "00c25c48",
        null,
        "undefined4"
      ]
    ],
    [
      "005323a8",
      "WRITE",
      [
        "storage",
        "00c25c48",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005323a0",
      "READ",
      [
        "storage",
        "00c25d08",
        null,
        "undefined4"
      ]
    ],
    [
      "005323a8",
      "WRITE",
      [
        "storage",
        "00c25d08",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005323a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/0053239c.md#insn-005323a8) · [`005323a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/0053239c.md#insn-005323a0)
- 新版 [`005323a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053239c.md#insn-005323a8) · [`005323a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053239c.md#insn-005323a0)

~~~diff
- 005323a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c48:8"]]
- 005323a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 005323a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d08:8"]]
+ 005323a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 005323a8 bytes 09490cb9
+ 005323a8 bytes 09090db9
- 005323a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c48:8"]]
- 005323a0 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 005323a0 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
+ 005323a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d08:8"]]
+ 005323a0 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 005323a0 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 005323a0 bytes 09494cb9
+ 005323a0 bytes 09094db9
~~~


<a id="compare-1895b3cb3098360784e86e863c732f8f"></a>

### [`005325a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005325a0.md) → [`005325a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005325a0.md) FUN_005325a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005323ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005323ec.md) · 呼出先 13件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00445610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445610.md) [`00449574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449574.md) [`00532f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/00532f34.md) [`0053781c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/0053781c.md)
- 新版 呼出元 1件 [`005323ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323ec.md) · 呼出先 13件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00445610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445610.md) [`00449574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449574.md) [`00532f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/00532f34.md) [`0053781c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053781c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00532670",
      "incomplete_value": true,
      "site": "00532670",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532670",
      "incomplete_value": true,
      "site": "00532670",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00532744",
      "incomplete_value": true,
      "site": "00532744",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532744",
      "incomplete_value": true,
      "site": "00532744",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0053281c",
      "incomplete_value": true,
      "site": "0053281c",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053281c",
      "incomplete_value": true,
      "site": "0053281c",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005325f8",
      "READ",
      [
        "storage",
        "00c25ca8",
        null,
        "undefined1"
      ]
    ],
    [
      "00532600",
      "READ",
      [
        "storage",
        "00c25c90",
        null,
        "undefined8"
      ]
    ],
    [
      "00532604",
      "WRITE",
      [
        "storage",
        "00c25c98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005325f8",
      "READ",
      [
        "storage",
        "00c25d68",
        null,
        "undefined1"
      ]
    ],
    [
      "00532600",
      "READ",
      [
        "storage",
        "00c25d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00532604",
      "WRITE",
      [
        "storage",
        "00c25d58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005325a0.md#insn-00532670) · [`00532744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005325a0.md#insn-00532744) · [`0053281c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005325a0.md#insn-0053281c)
- 新版 [`00532670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005325a0.md#insn-00532670) · [`00532744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005325a0.md#insn-00532744) · [`0053281c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005325a0.md#insn-0053281c)

~~~diff
- 00532670 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c98:8"]]
- 00532670 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
+ 00532670 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d58:8"]]
+ 00532670 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00532670 bytes 3b4d06f9
+ 00532670 bytes 3bad06f9
- 00532744 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c98:8"]]
- 00532744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d0:8"]]
+ 00532744 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d58:8"]]
+ 00532744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d0:8"]]
- 00532744 bytes 3a4d06f9
+ 00532744 bytes 3aad06f9
- 0053281c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c98:8"]]
- 0053281c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
+ 0053281c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d58:8"]]
+ 0053281c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 0053281c bytes 3c4d06f9
+ 0053281c bytes 3cad06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a212501b515cde511fd2c8d365df204"></a>

### [`00536a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00536/00536a8c.md) → [`00536a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/00536a8c.md) FUN_00536a8c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00537664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/00537664.md) · 呼出先 14件 [`00445610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445610.md) [`00449588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449588.md) [`00532dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/00532dbc.md) [`00536d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00536/00536d38.md) [`00537068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/00537068.md)
- 新版 呼出元 1件 [`00537664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537664.md) · 呼出先 14件 [`00445610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445610.md) [`00449588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449588.md) [`00532dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/00532dbc.md) [`00536d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/00536d38.md) [`00537068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537068.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.58% / 新版 94.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536bb0",
      "incomplete_value": false,
      "site": "00536bb4",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536bb0",
      "incomplete_value": false,
      "site": "00536bb4",
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
            "const:c50:8"
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
      "definition_site": "00536c14",
      "incomplete_value": false,
      "site": "00536c18",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536c14",
      "incomplete_value": false,
      "site": "00536c18",
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
            "const:c50:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536c5c",
      "incomplete_value": false,
      "site": "00536c6c",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536c5c",
      "incomplete_value": false,
      "site": "00536c6c",
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
            "const:c68:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00536ac4",
      "READ",
      [
        "storage",
        "00c25c68",
        null,
        "undefined1"
      ]
    ],
    [
      "00536acc",
      "READ",
      [
        "storage",
        "00c25c50",
        null,
        "undefined8"
      ]
    ],
    [
      "00536ad0",
      "WRITE",
      [
        "storage",
        "00c25c58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00536ac4",
      "READ",
      [
        "storage",
        "00c25d28",
        null,
        "undefined1"
      ]
    ],
    [
      "00536acc",
      "READ",
      [
        "storage",
        "00c25d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00536ad0",
      "WRITE",
      [
        "storage",
        "00c25d18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536ab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00536/00536a8c.md#insn-00536ab8) · [`00536ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00536/00536a8c.md#insn-00536ac0) · [`00536ba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00536/00536a8c.md#insn-00536ba8)
- 新版 [`00536ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/00536a8c.md#insn-00536ab8) · [`00536ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/00536a8c.md#insn-00536ac0) · [`00536ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/00536a8c.md#insn-00536ba8)

~~~diff
- 00536ab8 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 00536ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00536ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00536ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00536ab8 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00536ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00536ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00536ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00536ab8 bytes 08a13191
+ 00536ab8 bytes 08a13491
- 00536ac0 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00536ac0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00536ac0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00536ac0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00536ac0 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00536ac0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00536ac0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00536ac0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00536ac0 bytes 73423191
+ 00536ac0 bytes 73423491
- 00536ba8 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00536ba8 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00536ba8 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00536ba8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00536ba8 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00536ba8 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00536ba8 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00536ba8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00536ba8 bytes 94423191
+ 00536ba8 bytes 94423491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b7b4ab560efc03f3d6ee6e79da7544e"></a>

### [`00537560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/00537560.md) → [`00537560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537560.md) FUN_00537560

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00445124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445124.md) · 呼出先 8件 [`00445610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445610.md) [`00532dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/00532dbc.md) [`00536d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00536/00536d38.md) [`00537068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/00537068.md) [`0056d0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056d/0056d0d0.md)
- 新版 呼出元 1件 [`00445124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445124.md) · 呼出先 8件 [`00445610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445610.md) [`00532dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/00532dbc.md) [`00536d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/00536d38.md) [`00537068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537068.md) [`0056d0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056d/0056d0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00537600",
      "incomplete_value": false,
      "site": "0053760c",
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
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537600",
      "incomplete_value": false,
      "site": "0053760c",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00537630",
      "incomplete_value": false,
      "site": "00537640",
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
      "definition_site": "00537630",
      "incomplete_value": false,
      "site": "00537640",
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
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00537648",
      "incomplete_value": false,
      "site": "0053764c",
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
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537648",
      "incomplete_value": false,
      "site": "0053764c",
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
            "const:c88:8"
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
      "00537578",
      "READ",
      [
        "storage",
        "00c25c88",
        null,
        "undefined1"
      ]
    ],
    [
      "00537588",
      "READ",
      [
        "storage",
        "00c25c70",
        null,
        "undefined8"
      ]
    ],
    [
      "00537598",
      "PARAM",
      [
        "storage",
        "00c25c70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00537578",
      "READ",
      [
        "storage",
        "00c25d48",
        null,
        "undefined1"
      ]
    ],
    [
      "00537588",
      "READ",
      [
        "storage",
        "00c25d30",
        null,
        "undefined8"
      ]
    ],
    [
      "00537598",
      "PARAM",
      [
        "storage",
        "00c25d30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/00537560.md#insn-00537574) · [`0053757c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/00537560.md#insn-0053757c)
- 新版 [`00537574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537560.md#insn-00537574) · [`0053757c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537560.md#insn-0053757c)

~~~diff
- 00537574 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00537574 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00537574 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00537574 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00537574 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 00537574 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00537574 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00537574 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00537574 bytes 08213291
+ 00537574 bytes 08213591
- 0053757c ["COPY", "register:4040:8", ["const:c25000:8"]]
- 0053757c bytes 683700d0
+ 0053757c ["COPY", "register:4040:8", ["const:c25000:8"]]
+ 0053757c bytes 683700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85a93afdb7f33b93c5d09e756cc02f6e"></a>

### [`005376d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/005376d0.md) → [`005376d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005376d0.md) FUN_005376d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00445e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445e30.md) [`00445f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445f48.md) [`00447b24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447b24.md) [`00447c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447c70.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00445e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445e30.md) [`00445f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445f48.md) [`00447b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447b24.md) [`00447c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447c70.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "005376d8",
      "incomplete_value": true,
      "site": "005376dc",
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
      "definition_site": "005376d8",
      "incomplete_value": true,
      "site": "005376dc",
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
      "005376d8",
      "READ",
      [
        "storage",
        "00c26450",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005376d8",
      "READ",
      [
        "storage",
        "00c26510",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005376d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/005376d0.md#insn-005376d4)
- 新版 [`005376d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005376d0.md#insn-005376d4)

~~~diff
- 005376d4 ["COPY", "tmp:0:8", ["const:450:8"]]
- 005376d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005376d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005376d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005376d4 ["COPY", "tmp:0:8", ["const:510:8"]]
+ 005376d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005376d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005376d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005376d4 bytes 08411191
+ 005376d4 bytes 08411491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00495caeb180aaa5e66c65bb9bdda801"></a>

### [`00537724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/00537724.md) → [`00537724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537724.md) FUN_00537724

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00444ee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444ee4.md) [`00445e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445e30.md) [`00445f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445f48.md) [`00447b24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447b24.md) [`00447c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447c70.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00444ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444ee4.md) [`00445e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445e30.md) [`00445f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445f48.md) [`00447b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447b24.md) [`00447c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447c70.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00537744",
      "incomplete_value": true,
      "site": "00537744",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:428:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537744",
      "incomplete_value": true,
      "site": "00537744",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:378:8"
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
      "00537730",
      "READ",
      [
        "storage",
        "00c1b350",
        null,
        "pointer"
      ]
    ],
    [
      "00537734",
      "READ",
      [
        "storage",
        "00c26550",
        null,
        "undefined8"
      ]
    ],
    [
      "0053773c",
      "READ",
      [
        "storage",
        "00c1b378",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00537730",
      "READ",
      [
        "storage",
        "00c1b400",
        null,
        "pointer"
      ]
    ],
    [
      "00537734",
      "READ",
      [
        "storage",
        "00c26610",
        null,
        "undefined8"
      ]
    ],
    [
      "0053773c",
      "READ",
      [
        "storage",
        "00c1b428",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/00537724.md#insn-00537730) · [`0053773c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/00537724.md#insn-0053773c)
- 新版 [`00537730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537724.md#insn-00537730) · [`0053773c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537724.md#insn-0053773c)

~~~diff
- 00537730 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
- 00537730 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00537730 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:400:8"]]
+ 00537730 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00537730 bytes 08a941f9
+ 00537730 bytes 080142f9
- 0053773c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:378:8"]]
- 0053773c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053773c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:428:8"]]
+ 0053773c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0053773c bytes 29bd41f9
+ 0053773c bytes 291542f9
~~~


<a id="compare-ee2ceb608ba2a1cdc052435cdf015372"></a>

### [`0053774c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/0053774c.md) → [`0053774c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053774c.md) FUN_0053774c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00444a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444a94.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445044.md) · 呼出先 0件 
- 新版 呼出元 3件 [`00444a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444a94.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0053775c",
      "incomplete_value": true,
      "site": "0053775c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053775c",
      "incomplete_value": true,
      "site": "0053775c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:380:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0053775c",
      "incomplete_value": true,
      "site": "0053775c",
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
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053775c",
      "incomplete_value": true,
      "site": "0053775c",
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
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0053776c",
      "incomplete_value": true,
      "site": "0053776c",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053776c",
      "incomplete_value": true,
      "site": "0053776c",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00537758",
      "READ",
      [
        "storage",
        "00c1b380",
        null,
        "pointer"
      ]
    ],
    [
      "0053775c",
      "WRITE",
      [
        "storage",
        "00c23e38",
        null,
        "undefined4"
      ]
    ],
    [
      "0053775c",
      "WRITE",
      [
        "storage",
        "00c23e3c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00537758",
      "READ",
      [
        "storage",
        "00c1b430",
        null,
        "pointer"
      ]
    ],
    [
      "0053775c",
      "WRITE",
      [
        "storage",
        "00c23ee8",
        null,
        "undefined4"
      ]
    ],
    [
      "0053775c",
      "WRITE",
      [
        "storage",
        "00c23eec",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/0053774c.md#insn-00537758) · [`00537768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/0053774c.md#insn-00537768)
- 新版 [`00537758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053774c.md#insn-00537758) · [`00537768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053774c.md#insn-00537768)

~~~diff
- 00537758 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:380:8"]]
- 00537758 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00537758 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:430:8"]]
+ 00537758 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00537758 bytes 08c141f9
+ 00537758 bytes 081942f9
- 00537768 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:358:8"]]
- 00537768 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00537768 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:408:8"]]
+ 00537768 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00537768 bytes 29ad41f9
+ 00537768 bytes 290542f9
~~~


<a id="compare-f55944ca07b53a68aa8a3f1bc6def3c7"></a>

### [`005377dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/005377dc.md) → [`005377dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377dc.md) FUN_005377dc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005f2980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a4/008a4e38.md) [`00acce84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acce84.md) · 呼出先 0件 
- 新版 呼出元 5件 [`005f2980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a4/008a4e38.md) [`00accf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "005377e4",
      "incomplete_value": true,
      "site": "005377e8",
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
      "definition_site": "005377e4",
      "incomplete_value": true,
      "site": "005377e8",
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
      "005377e4",
      "READ",
      [
        "storage",
        "00c264a0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005377e4",
      "READ",
      [
        "storage",
        "00c26560",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005377e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/005377dc.md#insn-005377e0)
- 新版 [`005377e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377dc.md#insn-005377e0)

~~~diff
- 005377e0 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 005377e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005377e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005377e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005377e0 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 005377e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005377e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005377e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005377e0 bytes 08811291
+ 005377e0 bytes 08811591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbe0dcef239bd1daaa8245f77a80c116"></a>

### [`005377ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/005377ec.md) → [`005377ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377ec.md) FUN_005377ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005f2980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a4/008a4e38.md) [`00acce84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acce84.md) · 呼出先 0件 
- 新版 呼出元 5件 [`005f2980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a4/008a4e38.md) [`00accf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "005377f4",
      "incomplete_value": true,
      "site": "005377f8",
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
      "definition_site": "005377f4",
      "incomplete_value": true,
      "site": "005377f8",
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
      "005377f4",
      "READ",
      [
        "storage",
        "00c2649c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005377f4",
      "READ",
      [
        "storage",
        "00c2655c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005377f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/005377ec.md#insn-005377f0)
- 新版 [`005377f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377ec.md#insn-005377f0)

~~~diff
- 005377f0 ["COPY", "tmp:0:8", ["const:49c:8"]]
- 005377f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005377f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005377f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005377f0 ["COPY", "tmp:0:8", ["const:55c:8"]]
+ 005377f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005377f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005377f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005377f0 bytes 08711291
+ 005377f0 bytes 08711591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33d41ecfc5492490e62c019fb69fdfc5"></a>

### [`005377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/005377fc.md) → [`005377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377fc.md) FUN_005377fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00537804",
      "incomplete_value": true,
      "site": "00537808",
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
      "definition_site": "00537804",
      "incomplete_value": true,
      "site": "00537808",
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
      "00537804",
      "READ",
      [
        "storage",
        "00c264a8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00537804",
      "READ",
      [
        "storage",
        "00c26568",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/005377fc.md#insn-00537800)
- 新版 [`00537800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377fc.md#insn-00537800)

~~~diff
- 00537800 ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 00537800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00537800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00537800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00537800 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00537800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00537800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00537800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00537800 bytes 08a11291
+ 00537800 bytes 08a11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f08675a16753df72f3e4a5023a3f165"></a>

### [`0053780c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/0053780c.md) → [`0053780c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053780c.md) FUN_0053780c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00537814",
      "incomplete_value": true,
      "site": "00537818",
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
      "definition_site": "00537814",
      "incomplete_value": true,
      "site": "00537818",
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
      "00537814",
      "READ",
      [
        "storage",
        "00c264a4",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00537814",
      "READ",
      [
        "storage",
        "00c26564",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/0053780c.md#insn-00537810)
- 新版 [`00537810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053780c.md#insn-00537810)

~~~diff
- 00537810 ["COPY", "tmp:0:8", ["const:4a4:8"]]
- 00537810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00537810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00537810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00537810 ["COPY", "tmp:0:8", ["const:564:8"]]
+ 00537810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00537810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00537810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00537810 bytes 08911291
+ 00537810 bytes 08911591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71a38ec37cc39624c4b766667ec6ea04"></a>

### [`00538260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00538/00538260.md) → [`00538260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538260.md) FUN_00538260

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0053781c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/0053781c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0053781c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053781c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0053826c",
      "incomplete_value": false,
      "site": "00538270",
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
      "definition_site": "0053826c",
      "incomplete_value": false,
      "site": "00538270",
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
      "0053826c",
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
      "0053826c",
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

- 旧版 [`0053826c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00538/00538260.md#insn-0053826c)
- 新版 [`0053826c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538260.md#insn-0053826c)

~~~diff
- 0053826c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0053826c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053826c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053826c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053826c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0053826c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053826c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053826c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053826c bytes 00280c91
+ 0053826c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44be12b936aa08ecb4e42d216bf494ad"></a>

### [`00538274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00538/00538274.md) → [`00538274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538274.md) FUN_00538274

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0053781c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/0053781c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0053781c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053781c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00538280",
      "incomplete_value": false,
      "site": "00538284",
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
      "definition_site": "00538280",
      "incomplete_value": false,
      "site": "00538284",
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
      "00538280",
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
      "00538280",
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

- 旧版 [`00538280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00538/00538274.md#insn-00538280)
- 新版 [`00538280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538274.md#insn-00538280)

~~~diff
- 00538280 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00538280 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00538280 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00538280 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00538280 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00538280 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00538280 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00538280 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00538280 bytes 00280c91
+ 00538280 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dca12fb3699592b67dbf7b02fcb8ade"></a>

### [`00538370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00538/00538370.md) → [`00538370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538370.md) FUN_00538370

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005323ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005323ec.md) [`00532dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/00532dbc.md) [`00532f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/00532f34.md) [`0053699c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00536/0053699c.md) [`00537068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00537/00537068.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 5件 [`005323ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323ec.md) [`00532dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/00532dbc.md) [`00532f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/00532f34.md) [`0053699c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/0053699c.md) [`00537068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537068.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0053837c",
      "incomplete_value": false,
      "site": "00538380",
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
      "definition_site": "0053837c",
      "incomplete_value": false,
      "site": "00538380",
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
      "0053837c",
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
      "0053837c",
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

- 旧版 [`0053837c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00538/00538370.md#insn-0053837c)
- 新版 [`0053837c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538370.md#insn-0053837c)

~~~diff
- 0053837c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0053837c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053837c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053837c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053837c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0053837c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053837c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053837c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053837c bytes 00280c91
+ 0053837c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7dc9cdaf529b8749b62502de725b3d8"></a>

### [`00538384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00538/00538384.md) → [`00538384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538384.md) FUN_00538384

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00539488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539488.md) · 呼出先 5件 [`005384a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00538/005384a8.md) [`005397fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/005397fc.md) [`00539804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539804.md) [`0053b668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b668.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 1件 [`00539488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539488.md) · 呼出先 5件 [`005384a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/005384a8.md) [`005397fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005397fc.md) [`00539804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539804.md) [`0053b668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b668.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.19% / 新版 92.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005383a4",
      "incomplete_value": false,
      "site": "005383a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005383a4",
      "incomplete_value": false,
      "site": "005383a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "definition_site": "005383c0",
      "incomplete_value": false,
      "site": "005383c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005383c0",
      "incomplete_value": false,
      "site": "005383c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "definition_site": "005383c0",
      "incomplete_value": false,
      "site": "005383c0",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d38:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005383c0",
      "incomplete_value": false,
      "site": "005383c0",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:c88:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "005383a4",
      "DATA",
      [
        "storage",
        "00bedd78",
        null,
        "undefined *"
      ]
    ],
    [
      "005383c0",
      "DATA",
      [
        "storage",
        "00bedc88",
        null,
        "undefined *"
      ]
    ],
    [
      "005383c0",
      "DATA",
      [
        "storage",
        "00bedcf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005383a4",
      "DATA",
      [
        "storage",
        "00bede28",
        null,
        "undefined *"
      ]
    ],
    [
      "005383c0",
      "DATA",
      [
        "storage",
        "00bedd38",
        null,
        "undefined *"
      ]
    ],
    [
      "005383c0",
      "DATA",
      [
        "storage",
        "00bedda0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00538398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00538/00538384.md#insn-00538398) · [`005383b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00538/00538384.md#insn-005383b0)
- 新版 [`00538398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538384.md#insn-00538398) · [`005383b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538384.md#insn-005383b0)

~~~diff
- 00538398 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00538398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00538398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00538398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00538398 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 00538398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00538398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00538398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00538398 bytes 08e13591
+ 00538398 bytes 08a13891
- 005383b0 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 005383b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005383b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005383b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005383b0 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 005383b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005383b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005383b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005383b0 bytes 08213291
+ 005383b0 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91387306eb43b03209e65e257b6f10dd"></a>

### [`00539488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539488.md) → [`00539488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539488.md) FUN_00539488

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`004665d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00466/004665d0.md) [`00a3b374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a3b/00a3b374.md) · 呼出先 2件 [`00538384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00538/00538384.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 2件 [`004665d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00466/004665d0.md) [`00a3b374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b374.md) · 呼出先 2件 [`00538384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538384.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005394b8",
      "incomplete_value": false,
      "site": "005394c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005394b8",
      "incomplete_value": false,
      "site": "005394c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:da0:8"
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
      "005394c4",
      "DATA",
      [
        "storage",
        "00bedda0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005394c4",
      "DATA",
      [
        "storage",
        "00bede50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005394b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539488.md#insn-005394b8)
- 新版 [`005394b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539488.md#insn-005394b8)

~~~diff
- 005394b8 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 005394b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005394b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005394b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005394b8 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 005394b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005394b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005394b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005394b8 bytes 08813691
+ 005394b8 bytes 08413991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b1b92ec2cdabeb39250a45349eefb70"></a>

### [`0053950c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/0053950c.md) → [`0053950c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053950c.md) FUN_0053950c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b6d4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00539520",
      "incomplete_value": false,
      "site": "0053952c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539520",
      "incomplete_value": false,
      "site": "0053952c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "definition_site": "00539538",
      "incomplete_value": false,
      "site": "00539538",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d38:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539538",
      "incomplete_value": false,
      "site": "00539538",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:c88:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "0053952c",
      "DATA",
      [
        "storage",
        "00bedc88",
        null,
        "undefined *"
      ]
    ],
    [
      "00539538",
      "DATA",
      [
        "storage",
        "00bedcf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053952c",
      "DATA",
      [
        "storage",
        "00bedd38",
        null,
        "undefined *"
      ]
    ],
    [
      "00539538",
      "DATA",
      [
        "storage",
        "00bedda0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/0053950c.md#insn-00539520) · [`00539528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/0053950c.md#insn-00539528)
- 新版 [`00539520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053950c.md#insn-00539520) · [`00539528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053950c.md#insn-00539528)

~~~diff
- 00539520 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00539520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539520 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00539520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539520 bytes 08213291
+ 00539520 bytes 08e13491
- 00539528 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00539528 bytes f40300aa
+ 00539528 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 00539528 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c90ce2ab9acb6e6b4220902897eec76e"></a>

### [`005395ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/005395ac.md) → [`005395ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005395ac.md) FUN_005395ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0053b6d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b6d4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0053b6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005395c0",
      "incomplete_value": false,
      "site": "005395cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005395c0",
      "incomplete_value": false,
      "site": "005395cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "definition_site": "005395d8",
      "incomplete_value": false,
      "site": "005395d8",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d38:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005395d8",
      "incomplete_value": false,
      "site": "005395d8",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:c88:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "005395cc",
      "DATA",
      [
        "storage",
        "00bedc88",
        null,
        "undefined *"
      ]
    ],
    [
      "005395d8",
      "DATA",
      [
        "storage",
        "00bedcf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005395cc",
      "DATA",
      [
        "storage",
        "00bedd38",
        null,
        "undefined *"
      ]
    ],
    [
      "005395d8",
      "DATA",
      [
        "storage",
        "00bedda0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005395c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/005395ac.md#insn-005395c0) · [`005395c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/005395ac.md#insn-005395c8)
- 新版 [`005395c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005395ac.md#insn-005395c0) · [`005395c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005395ac.md#insn-005395c8)

~~~diff
- 005395c0 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 005395c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005395c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005395c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005395c0 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 005395c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005395c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005395c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005395c0 bytes 08213291
+ 005395c0 bytes 08e13491
- 005395c8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 005395c8 bytes f30300aa
+ 005395c8 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 005395c8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-547d0d368e4b764be3259cbc709f27b0"></a>

### [`00539654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539654.md) → [`00539654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539654.md) FUN_00539654

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b6d4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00539674",
      "incomplete_value": false,
      "site": "00539674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539674",
      "incomplete_value": false,
      "site": "00539674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "definition_site": "00539674",
      "incomplete_value": false,
      "site": "00539674",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d38:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539674",
      "incomplete_value": false,
      "site": "00539674",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:c88:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "00539674",
      "DATA",
      [
        "storage",
        "00bedc88",
        null,
        "undefined *"
      ]
    ],
    [
      "00539674",
      "DATA",
      [
        "storage",
        "00bedcf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539674",
      "DATA",
      [
        "storage",
        "00bedd38",
        null,
        "undefined *"
      ]
    ],
    [
      "00539674",
      "DATA",
      [
        "storage",
        "00bedda0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539654.md#insn-00539664)
- 新版 [`00539664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539654.md#insn-00539664)

~~~diff
- 00539664 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00539664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539664 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00539664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539664 bytes 08213291
+ 00539664 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-111f034049aa6c09d9664444db03998f"></a>

### [`0053978c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/0053978c.md) → [`0053978c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053978c.md) FUN_0053978c

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
      "definition_site": "00539790",
      "incomplete_value": false,
      "site": "00539794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539790",
      "incomplete_value": false,
      "site": "00539794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:da0:8"
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
      "00539794",
      "DATA",
      [
        "storage",
        "00bedda0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539794",
      "DATA",
      [
        "storage",
        "00bede50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/0053978c.md#insn-00539790)
- 新版 [`00539790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053978c.md#insn-00539790)

~~~diff
- 00539790 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00539790 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539790 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539790 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539790 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00539790 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539790 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539790 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539790 bytes 08813691
+ 00539790 bytes 08413991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c6f9df0d0e72ce3a0883a2c8f4b9019"></a>

### [`0053980c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/0053980c.md) → [`0053980c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053980c.md) FUN_0053980c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0052e39c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052e/0052e39c.md) [`005385e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00538/005385e0.md) [`00a3b374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a3b/00a3b374.md) · 呼出先 2件 [`005399b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/005399b0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 3件 [`0052e39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e39c.md) [`005385e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/005385e0.md) [`00a3b374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b374.md) · 呼出先 2件 [`005399b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005399b0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00539838",
      "incomplete_value": false,
      "site": "00539840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539838",
      "incomplete_value": false,
      "site": "00539840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "definition_site": "0053984c",
      "incomplete_value": false,
      "site": "0053984c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053984c",
      "incomplete_value": false,
      "site": "0053984c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "00539840",
      "DATA",
      [
        "storage",
        "00bede40",
        null,
        "undefined *"
      ]
    ],
    [
      "0053984c",
      "DATA",
      [
        "storage",
        "00beddf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539840",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ],
    [
      "0053984c",
      "DATA",
      [
        "storage",
        "00bedea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/0053980c.md#insn-00539838) · [`0053983c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/0053980c.md#insn-0053983c)
- 新版 [`00539838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053980c.md#insn-00539838) · [`0053983c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053980c.md#insn-0053983c)

~~~diff
- 00539838 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00539838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539838 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 00539838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539838 bytes 08013991
+ 00539838 bytes 08c13b91
- 0053983c ["COPY", "register:40c0:8", ["register:4000:8"]]
- 0053983c bytes f80300aa
+ 0053983c ["COPY", "register:40c0:8", ["register:4000:8"]]
+ 0053983c bytes f80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d31bcd3ae47c3826dbc9a1a4e5fd725f"></a>

### [`0053994c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/0053994c.md) → [`0053994c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053994c.md) FUN_0053994c

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
      "definition_site": "00539958",
      "incomplete_value": false,
      "site": "0053995c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539958",
      "incomplete_value": false,
      "site": "0053995c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
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
      "0053995c",
      "DATA",
      [
        "storage",
        "00beddf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053995c",
      "DATA",
      [
        "storage",
        "00bedea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/0053994c.md#insn-00539958)
- 新版 [`00539958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053994c.md#insn-00539958)

~~~diff
- 00539958 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 00539958 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00539958 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00539958 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00539958 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00539958 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00539958 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00539958 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00539958 bytes 29c13791
+ 00539958 bytes 29813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfcb109ee0963d5b2cf29b3144480c88"></a>

### [`00539970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539970.md) → [`00539970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539970.md) FUN_00539970

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
      "definition_site": "00539978",
      "incomplete_value": false,
      "site": "0053997c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539978",
      "incomplete_value": false,
      "site": "0053997c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
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
      "0053997c",
      "DATA",
      [
        "storage",
        "00beddf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053997c",
      "DATA",
      [
        "storage",
        "00bedea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539970.md#insn-00539978)
- 新版 [`00539978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539970.md#insn-00539978)

~~~diff
- 00539978 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 00539978 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00539978 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00539978 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00539978 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00539978 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00539978 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00539978 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00539978 bytes 29c13791
+ 00539978 bytes 29813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-444f8e84b78dfd1aa5b89b0235f41175"></a>

### [`00539adc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539adc.md) → [`00539adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539adc.md) FUN_00539adc

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
      "definition_site": "00539ae0",
      "incomplete_value": false,
      "site": "00539ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539ae0",
      "incomplete_value": false,
      "site": "00539ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "00539ae4",
      "DATA",
      [
        "storage",
        "00bede40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539ae4",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539adc.md#insn-00539ae0)
- 新版 [`00539ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539adc.md#insn-00539ae0)

~~~diff
- 00539ae0 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00539ae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539ae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539ae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539ae0 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 00539ae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539ae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539ae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539ae0 bytes 08013991
+ 00539ae0 bytes 08c13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef9444aaf3572e1c4a61401268b85b49"></a>

### [`00539aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539aec.md) → [`00539aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539aec.md) FUN_00539aec

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
      "definition_site": "00539afc",
      "incomplete_value": false,
      "site": "00539b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539afc",
      "incomplete_value": false,
      "site": "00539b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "00539b04",
      "DATA",
      [
        "storage",
        "00bede40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539b04",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539aec.md#insn-00539afc)
- 新版 [`00539afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539aec.md#insn-00539afc)

~~~diff
- 00539afc ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00539afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539afc ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 00539afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539afc bytes 08013991
+ 00539afc bytes 08c13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b091e3541748c16d845c80da034f896e"></a>

### [`00539b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539b2c.md) → [`00539b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539b2c.md) FUN_00539b2c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005398ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/005398ec.md) · 呼出先 3件 [`005399b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/005399b0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`005398ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005398ec.md) · 呼出先 3件 [`005399b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005399b0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00539b5c",
      "incomplete_value": false,
      "site": "00539b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539b5c",
      "incomplete_value": false,
      "site": "00539b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "definition_site": "00539b7c",
      "incomplete_value": false,
      "site": "00539b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539b7c",
      "incomplete_value": false,
      "site": "00539b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "00539b68",
      "DATA",
      [
        "storage",
        "00bede40",
        null,
        "undefined *"
      ]
    ],
    [
      "00539b7c",
      "DATA",
      [
        "storage",
        "00beddf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539b68",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ],
    [
      "00539b7c",
      "DATA",
      [
        "storage",
        "00bedea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539b2c.md#insn-00539b5c) · [`00539b6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539b2c.md#insn-00539b6c)
- 新版 [`00539b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539b2c.md#insn-00539b5c) · [`00539b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539b2c.md#insn-00539b6c)

~~~diff
- 00539b5c ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00539b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539b5c ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 00539b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539b5c bytes 08013991
+ 00539b5c bytes 08c13b91
- 00539b6c ["COPY", "register:4040:8", ["const:bed000:8"]]
- 00539b6c bytes a8350090
+ 00539b6c ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 00539b6c bytes a8350090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6be476861ad234936fdb08faa7c09593"></a>

### [`00539c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539c08.md) → [`00539c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539c08.md) FUN_00539c08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053a518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a518.md) · 呼出先 11件 [`00449574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449574.md) [`00512c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512c94.md) [`0053a5f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a5f0.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`0053a518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a518.md) · 呼出先 11件 [`00449574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449574.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`0053a5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5f0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00539c38",
      "incomplete_value": false,
      "site": "00539c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539c38",
      "incomplete_value": false,
      "site": "00539c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "definition_site": "00539c8c",
      "incomplete_value": false,
      "site": "00539c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539c8c",
      "incomplete_value": false,
      "site": "00539c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "00539c44",
      "DATA",
      [
        "storage",
        "00bede90",
        null,
        "undefined *"
      ]
    ],
    [
      "00539c98",
      "DATA",
      [
        "storage",
        "00beded0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539c44",
      "DATA",
      [
        "storage",
        "00bedf40",
        null,
        "undefined *"
      ]
    ],
    [
      "00539c98",
      "DATA",
      [
        "storage",
        "00bedf80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539c08.md#insn-00539c38) · [`00539c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539c08.md#insn-00539c3c)
- 新版 [`00539c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539c08.md#insn-00539c38) · [`00539c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539c08.md#insn-00539c3c)

~~~diff
- 00539c38 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00539c38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539c38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539c38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539c38 ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 00539c38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539c38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539c38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539c38 bytes 08413a91
+ 00539c38 bytes 08013d91
- 00539c3c ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00539c3c bytes f40300aa
+ 00539c3c ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 00539c3c bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86f6f31ba85c60a9669ee046c96f18fe"></a>

### [`0053a518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a518.md) → [`0053a518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a518.md) FUN_0053a518

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00444d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444d18.md) · 呼出先 2件 [`00539c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539c08.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00444d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444d18.md) · 呼出先 2件 [`00539c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539c08.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0053a54c",
      "incomplete_value": false,
      "site": "0053a558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053a54c",
      "incomplete_value": false,
      "site": "0053a558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f60:8"
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
      "0053a558",
      "DATA",
      [
        "storage",
        "00bedf60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053a558",
      "DATA",
      [
        "storage",
        "00bee010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053a548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a518.md#insn-0053a548) · [`0053a54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a518.md#insn-0053a54c)
- 新版 [`0053a548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a518.md#insn-0053a548) · [`0053a54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a518.md#insn-0053a54c)

~~~diff
- 0053a548 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 0053a548 ["COPY", "register:4040:8", ["const:bee000:8"]]
- 0053a548 bytes 883500f0
+ 0053a548 bytes a8350090
- 0053a54c ["COPY", "tmp:0:8", ["const:f60:8"]]
- 0053a54c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053a54c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053a54c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053a54c ["COPY", "tmp:0:8", ["const:10:8"]]
+ 0053a54c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a54c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a54c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053a54c bytes 08813d91
+ 0053a54c bytes 08410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0421e2655898cebb062bfebc2cb9617"></a>

### [`0053a5a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a5a4.md) → [`0053a5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5a4.md) FUN_0053a5a4

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
      "definition_site": "0053a5a8",
      "incomplete_value": false,
      "site": "0053a5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053a5a8",
      "incomplete_value": false,
      "site": "0053a5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
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
      "0053a5ac",
      "DATA",
      [
        "storage",
        "00beded0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053a5ac",
      "DATA",
      [
        "storage",
        "00bedf80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053a5a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a5a4.md#insn-0053a5a8)
- 新版 [`0053a5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5a4.md#insn-0053a5a8)

~~~diff
- 0053a5a8 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 0053a5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053a5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053a5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053a5a8 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 0053a5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053a5a8 bytes 08413b91
+ 0053a5a8 bytes 08013e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33f404da3858b80f9bc942db7ccf7727"></a>

### [`0053a5b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a5b4.md) → [`0053a5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5b4.md) FUN_0053a5b4

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
      "definition_site": "0053a5c4",
      "incomplete_value": false,
      "site": "0053a5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053a5c4",
      "incomplete_value": false,
      "site": "0053a5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
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
      "0053a5cc",
      "DATA",
      [
        "storage",
        "00beded0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053a5cc",
      "DATA",
      [
        "storage",
        "00bedf80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053a5c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a5b4.md#insn-0053a5c4)
- 新版 [`0053a5c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5b4.md#insn-0053a5c4)

~~~diff
- 0053a5c4 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 0053a5c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053a5c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053a5c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053a5c4 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 0053a5c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a5c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a5c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053a5c4 bytes 08413b91
+ 0053a5c4 bytes 08013e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fbbb3bfd111b42a527ba45deeac0849"></a>

### [`0053a5f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a5f0.md) → [`0053a5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5f0.md) FUN_0053a5f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00539c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539c08.md) · 呼出先 1件 [`0053b028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b028.md)
- 新版 呼出元 1件 [`00539c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539c08.md) · 呼出先 1件 [`0053b028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b028.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053a60c",
      "incomplete_value": true,
      "site": "0053a610",
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
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053a60c",
      "incomplete_value": true,
      "site": "0053a610",
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
            "const:f20:8"
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
      "0053a610",
      "DATA",
      [
        "storage",
        "00bedf20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053a610",
      "DATA",
      [
        "storage",
        "00bedfd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053a60c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a5f0.md#insn-0053a60c)
- 新版 [`0053a60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5f0.md#insn-0053a60c)

~~~diff
- 0053a60c ["COPY", "tmp:0:8", ["const:f20:8"]]
- 0053a60c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053a60c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053a60c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053a60c ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 0053a60c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a60c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a60c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053a60c bytes 08813c91
+ 0053a60c bytes 08413f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4d40d11d2a6478260116e5d86429463"></a>

### [`0053b5a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b5a4.md) → [`0053b5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5a4.md) FUN_0053b5a4

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
      "definition_site": "0053b5a8",
      "incomplete_value": false,
      "site": "0053b5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053b5a8",
      "incomplete_value": false,
      "site": "0053b5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f60:8"
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
      "0053b5ac",
      "DATA",
      [
        "storage",
        "00bedf60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053b5ac",
      "DATA",
      [
        "storage",
        "00bee010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053b5a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b5a4.md#insn-0053b5a4) · [`0053b5a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b5a4.md#insn-0053b5a8)
- 新版 [`0053b5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5a4.md#insn-0053b5a4) · [`0053b5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5a4.md#insn-0053b5a8)

~~~diff
- 0053b5a4 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 0053b5a4 ["COPY", "register:4040:8", ["const:bee000:8"]]
- 0053b5a4 bytes 883500d0
+ 0053b5a4 bytes 883500f0
- 0053b5a8 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 0053b5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053b5a8 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 0053b5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053b5a8 bytes 08813d91
+ 0053b5a8 bytes 08410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-884510bd11519f52f8fbd3da5f4c7d9e"></a>

### [`0053b5b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b5b4.md) → [`0053b5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5b4.md) FUN_0053b5b4

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
      "definition_site": "0053b5c4",
      "incomplete_value": false,
      "site": "0053b5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053b5c4",
      "incomplete_value": false,
      "site": "0053b5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
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
      "0053b5cc",
      "DATA",
      [
        "storage",
        "00bedf60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053b5cc",
      "DATA",
      [
        "storage",
        "00bee010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053b5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b5b4.md#insn-0053b5c0) · [`0053b5c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b5b4.md#insn-0053b5c4)
- 新版 [`0053b5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5b4.md#insn-0053b5c0) · [`0053b5c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5b4.md#insn-0053b5c4)

~~~diff
- 0053b5c0 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 0053b5c0 ["COPY", "register:4040:8", ["const:bee000:8"]]
- 0053b5c0 bytes 883500d0
+ 0053b5c0 bytes 883500f0
- 0053b5c4 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 0053b5c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053b5c4 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 0053b5c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b5c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b5c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053b5c4 bytes 08813d91
+ 0053b5c4 bytes 08410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89b95c439c6c455392cea7b4427838c3"></a>

### [`0053b5e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b5e4.md) → [`0053b5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5e4.md) FUN_0053b5e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0053b5fc",
      "incomplete_value": false,
      "site": "0053b600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053b5fc",
      "incomplete_value": false,
      "site": "0053b600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "0053b600",
      "DATA",
      [
        "storage",
        "00bede90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053b600",
      "DATA",
      [
        "storage",
        "00bedf40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053b5fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b5e4.md#insn-0053b5fc)
- 新版 [`0053b5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5e4.md#insn-0053b5fc)

~~~diff
- 0053b5fc ["COPY", "tmp:0:8", ["const:e90:8"]]
- 0053b5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053b5fc ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 0053b5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053b5fc bytes 08413a91
+ 0053b5fc bytes 08013d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a97773a9dd6611857513baaf510aee00"></a>

### [`0053b6d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b6d4.md) → [`0053b6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md) FUN_0053b6d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0052f034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f034.md) [`0052f0a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052f/0052f0a4.md) [`0053950c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/0053950c.md) [`005395ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/005395ac.md) [`00539654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539654.md) · 呼出先 2件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 6件 [`0052f034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f034.md) [`0052f0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f0a4.md) [`0053950c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053950c.md) [`005395ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005395ac.md) [`00539654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539654.md) · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "0053b6e8",
      "incomplete_value": false,
      "site": "0053b6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053b6e8",
      "incomplete_value": false,
      "site": "0053b6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      "0053b6ec",
      "DATA",
      [
        "storage",
        "00bedfb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053b6ec",
      "DATA",
      [
        "storage",
        "00bee060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053b6e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b6d4.md#insn-0053b6e4) · [`0053b6e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b6d4.md#insn-0053b6e8)
- 新版 [`0053b6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md#insn-0053b6e4) · [`0053b6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md#insn-0053b6e8)

~~~diff
- 0053b6e4 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 0053b6e4 ["COPY", "register:4040:8", ["const:bee000:8"]]
- 0053b6e4 bytes 883500d0
+ 0053b6e4 bytes 883500f0
- 0053b6e8 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 0053b6e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053b6e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053b6e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053b6e8 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 0053b6e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b6e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b6e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053b6e8 bytes 08c13e91
+ 0053b6e8 bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfd2f51508fdc6a75e2ed2aed097fa8a"></a>

### [`0053be30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053be30.md) → [`0053be30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053be30.md) FUN_0053be30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046a54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046a54c.md) · 呼出先 7件 [`0055e5bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e5bc.md) [`00574740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574740.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0046a54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046a54c.md) · 呼出先 7件 [`0055e5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e5bc.md) [`00574740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574740.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.00% / 新版 97.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053c024",
      "incomplete_value": false,
      "site": "0053c02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c024",
      "incomplete_value": false,
      "site": "0053c02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053c050",
      "incomplete_value": false,
      "site": "0053c050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c050",
      "incomplete_value": false,
      "site": "0053c050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "0053c06c",
      "incomplete_value": false,
      "site": "0053c06c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c06c",
      "incomplete_value": false,
      "site": "0053c06c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0053c02c",
      "DATA",
      [
        "storage",
        "00bee088",
        null,
        "undefined *"
      ]
    ],
    [
      "0053c050",
      "DATA",
      [
        "storage",
        "00bee010",
        null,
        "undefined *"
      ]
    ],
    [
      "0053c06c",
      "DATA",
      [
        "storage",
        "00bee010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053c02c",
      "DATA",
      [
        "storage",
        "00bee138",
        null,
        "undefined *"
      ]
    ],
    [
      "0053c050",
      "DATA",
      [
        "storage",
        "00bee0c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0053c06c",
      "DATA",
      [
        "storage",
        "00bee0c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053be30.md#insn-0053c024) · [`0053c044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053be30.md#insn-0053c044) · [`0053c064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053be30.md#insn-0053c064)
- 新版 [`0053c024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053be30.md#insn-0053c024) · [`0053c044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053be30.md#insn-0053c044) · [`0053c064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053be30.md#insn-0053c064)

~~~diff
- 0053c024 ["COPY", "tmp:0:8", ["const:88:8"]]
- 0053c024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c024 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0053c024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c024 bytes 08210291
+ 0053c024 bytes 08e10491
- 0053c044 ["COPY", "tmp:0:8", ["const:10:8"]]
- 0053c044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c044 ["COPY", "tmp:0:8", ["const:c0:8"]]
+ 0053c044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c044 bytes 08410091
+ 0053c044 bytes 08010391
- 0053c064 ["COPY", "tmp:0:8", ["const:10:8"]]
- 0053c064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c064 ["COPY", "tmp:0:8", ["const:c0:8"]]
+ 0053c064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c064 bytes 08410091
+ 0053c064 bytes 08010391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48e40f5381cb29671ef2829b84cfc143"></a>

### [`0053c470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c470.md) → [`0053c470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c470.md) FUN_0053c470

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "0053c488",
      "incomplete_value": false,
      "site": "0053c48c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c488",
      "incomplete_value": false,
      "site": "0053c48c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "0053c48c",
      "DATA",
      [
        "storage",
        "00bee010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053c48c",
      "DATA",
      [
        "storage",
        "00bee0c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c470.md#insn-0053c488)
- 新版 [`0053c488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c470.md#insn-0053c488)

~~~diff
- 0053c488 ["COPY", "tmp:0:8", ["const:10:8"]]
- 0053c488 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c488 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c488 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c488 ["COPY", "tmp:0:8", ["const:c0:8"]]
+ 0053c488 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c488 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c488 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c488 bytes 08410091
+ 0053c488 bytes 08010391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00762422f2634f5e41b541764ed00c93"></a>

### [`0053c50c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c50c.md) → [`0053c50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c50c.md) FUN_0053c50c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0053c524",
      "incomplete_value": false,
      "site": "0053c528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c524",
      "incomplete_value": false,
      "site": "0053c528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "0053c528",
      "DATA",
      [
        "storage",
        "00bee010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053c528",
      "DATA",
      [
        "storage",
        "00bee0c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c524`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c50c.md#insn-0053c524)
- 新版 [`0053c524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c50c.md#insn-0053c524)

~~~diff
- 0053c524 ["COPY", "tmp:0:8", ["const:10:8"]]
- 0053c524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c524 ["COPY", "tmp:0:8", ["const:c0:8"]]
+ 0053c524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c524 bytes 08410091
+ 0053c524 bytes 08010391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1503aad043a52da9963a7afc78f4b6b4"></a>

### [`0053c598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c598.md) → [`0053c598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c598.md) FUN_0053c598

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
      "definition_site": "0053c59c",
      "incomplete_value": false,
      "site": "0053c5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c59c",
      "incomplete_value": false,
      "site": "0053c5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:88:8"
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
      "0053c5a0",
      "DATA",
      [
        "storage",
        "00bee088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053c5a0",
      "DATA",
      [
        "storage",
        "00bee138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c598.md#insn-0053c59c)
- 新版 [`0053c59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c598.md#insn-0053c59c)

~~~diff
- 0053c59c ["COPY", "tmp:0:8", ["const:88:8"]]
- 0053c59c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c59c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c59c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c59c ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0053c59c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c59c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c59c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c59c bytes 08210291
+ 0053c59c bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89e279c22cff8576bd7c68edcbb65d80"></a>

### [`0053c5a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c5a8.md) → [`0053c5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5a8.md) FUN_0053c5a8

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
      "definition_site": "0053c5b8",
      "incomplete_value": false,
      "site": "0053c5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c5b8",
      "incomplete_value": false,
      "site": "0053c5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:88:8"
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
      "0053c5c0",
      "DATA",
      [
        "storage",
        "00bee088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053c5c0",
      "DATA",
      [
        "storage",
        "00bee138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c5a8.md#insn-0053c5b8)
- 新版 [`0053c5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5a8.md#insn-0053c5b8)

~~~diff
- 0053c5b8 ["COPY", "tmp:0:8", ["const:88:8"]]
- 0053c5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c5b8 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0053c5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c5b8 bytes 08210291
+ 0053c5b8 bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1eb04472b2944561723b99929b9a59a"></a>

### [`0053c5ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c5ec.md) → [`0053c5ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5ec.md) FUN_0053c5ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 18件 [`0045d484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045d484.md) [`0045d518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045d518.md) [`0045d5ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045d5ac.md) [`0045d750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045d750.md) [`0045d7e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045d7e4.md) · 呼出先 2件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 18件 [`0045d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d484.md) [`0045d518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d518.md) [`0045d5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d5ac.md) [`0045d750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d750.md) [`0045d7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d7e4.md) · 呼出先 2件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 68.18% / 新版 68.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0053c634",
      "incomplete_value": true,
      "site": "0053c634",
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
            "const:d74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c634",
      "incomplete_value": true,
      "site": "0053c634",
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
            "const:cb4:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053c618",
      "incomplete_value": false,
      "site": "0053c61c",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c618",
      "incomplete_value": false,
      "site": "0053c61c",
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
            "const:cb8:8"
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
      "definition_site": "0053c630",
      "incomplete_value": false,
      "site": "0053c638",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c630",
      "incomplete_value": false,
      "site": "0053c638",
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
            "const:cb8:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0053c5fc",
      "READ",
      [
        "storage",
        "00c25cb8",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c608",
      "READ",
      [
        "storage",
        "00c25cb4",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c618",
      "PARAM",
      [
        "storage",
        "00c25cb8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0053c5fc",
      "READ",
      [
        "storage",
        "00c25d78",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c608",
      "READ",
      [
        "storage",
        "00c25d74",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c618",
      "PARAM",
      [
        "storage",
        "00c25d78",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c5ec.md#insn-0053c634) · [`0053c5f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c5ec.md#insn-0053c5f8) · [`0053c600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c5ec.md#insn-0053c600)
- 新版 [`0053c634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5ec.md#insn-0053c634) · [`0053c5f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5ec.md#insn-0053c5f8)

~~~diff
- 0053c634 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0053c634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:cb4:8"]]
- 0053c634 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0053c634 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0053c634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:d74:8"]]
+ 0053c634 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0053c634 bytes 09d13239
+ 0053c634 bytes 09d13539
- 0053c5f8 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 0053c5f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c5f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c5f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c5f8 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0053c5f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c5f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c5f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c5f8 bytes 08e13291
+ 0053c5f8 bytes 08e13591
- 0053c600 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 0053c600 bytes 483700b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9fe15b5bd0b3f441721839b2ffb259a"></a>

### [`0053c6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c6a0.md) → [`0053c6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c6a0.md) FUN_0053c6a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0053e1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e1dc.md) [`00a412d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a41/00a412d8.md) · 呼出先 5件 [`0053d4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d4e8.md) [`0053d590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d590.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 2件 [`0053e1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e1dc.md) [`00a412d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a41/00a412d8.md) · 呼出先 5件 [`0053d4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d4e8.md) [`0053d590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d590.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 79.41% / 新版 79.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053c6e4",
      "incomplete_value": true,
      "site": "0053c6e8",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c6e4",
      "incomplete_value": true,
      "site": "0053c6e8",
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
            "const:cd0:8"
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
      "definition_site": "0053c708",
      "incomplete_value": false,
      "site": "0053c714",
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
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c708",
      "incomplete_value": false,
      "site": "0053c714",
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
            "const:cc0:8"
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
      "definition_site": "0053c710",
      "incomplete_value": false,
      "site": "0053c714",
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
      "definition_site": "0053c710",
      "incomplete_value": false,
      "site": "0053c714",
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
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0053c6b8",
      "READ",
      [
        "storage",
        "00c25cd0",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c6c4",
      "READ",
      [
        "storage",
        "00c25cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "0053c6e4",
      "PARAM",
      [
        "storage",
        "00c25cd0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0053c6b8",
      "READ",
      [
        "storage",
        "00c25d90",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c6c4",
      "READ",
      [
        "storage",
        "00c25d80",
        null,
        "undefined8"
      ]
    ],
    [
      "0053c6e4",
      "PARAM",
      [
        "storage",
        "00c25d90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c6a0.md#insn-0053c6b0) · [`0053c6c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c6a0.md#insn-0053c6c4) · [`0053c6e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c6a0.md#insn-0053c6e4)
- 新版 [`0053c6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c6a0.md#insn-0053c6b0) · [`0053c6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c6a0.md#insn-0053c6c4) · [`0053c6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c6a0.md#insn-0053c6e4)

~~~diff
- 0053c6b0 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0053c6b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c6b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c6b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c6b0 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 0053c6b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c6b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c6b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c6b0 bytes 08413391
+ 0053c6b0 bytes 08413691
- 0053c6c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 0053c6c4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053c6c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 0053c6c4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c6c4 bytes 006146f9
+ 0053c6c4 bytes 00c146f9
- 0053c6e4 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0053c6e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053c6e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053c6e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053c6e4 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 0053c6e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053c6e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053c6e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053c6e4 bytes 00403391
+ 0053c6e4 bytes 00403691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4de459243c639f31ae3afb2772799e97"></a>

### [`0053c740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c740.md) → [`0053c740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c740.md) FUN_0053c740

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a17ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a17/00a17ce0.md) · 呼出先 5件 [`0053d4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d4e8.md) [`0053d590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d590.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`00a17ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a17/00a17ce0.md) · 呼出先 5件 [`0053d4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d4e8.md) [`0053d590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d590.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 69.44% / 新版 69.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053c78c",
      "incomplete_value": false,
      "site": "0053c790",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c78c",
      "incomplete_value": false,
      "site": "0053c790",
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
            "const:cd0:8"
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
      "definition_site": "0053c7b0",
      "incomplete_value": false,
      "site": "0053c7bc",
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
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c7b0",
      "incomplete_value": false,
      "site": "0053c7bc",
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
            "const:cc0:8"
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
      "definition_site": "0053c7b8",
      "incomplete_value": false,
      "site": "0053c7bc",
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
      "definition_site": "0053c7b8",
      "incomplete_value": false,
      "site": "0053c7bc",
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
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0053c758",
      "READ",
      [
        "storage",
        "00c25cd0",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c76c",
      "READ",
      [
        "storage",
        "00c25cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "0053c78c",
      "PARAM",
      [
        "storage",
        "00c25cd0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0053c758",
      "READ",
      [
        "storage",
        "00c25d90",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c76c",
      "READ",
      [
        "storage",
        "00c25d80",
        null,
        "undefined8"
      ]
    ],
    [
      "0053c78c",
      "PARAM",
      [
        "storage",
        "00c25d90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c740.md#insn-0053c750) · [`0053c76c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c740.md#insn-0053c76c) · [`0053c78c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c740.md#insn-0053c78c)
- 新版 [`0053c750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c740.md#insn-0053c750) · [`0053c76c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c740.md#insn-0053c76c) · [`0053c78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c740.md#insn-0053c78c)

~~~diff
- 0053c750 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0053c750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c750 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 0053c750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c750 bytes 08413391
+ 0053c750 bytes 08413691
- 0053c76c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 0053c76c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053c76c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 0053c76c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c76c bytes 006146f9
+ 0053c76c bytes 00c146f9
- 0053c78c ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0053c78c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053c78c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053c78c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053c78c ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 0053c78c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053c78c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053c78c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053c78c bytes 00403391
+ 0053c78c bytes 00403691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f97e72193ffeabd9a0b5672910b681c"></a>

### [`0053c7f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c7f0.md) → [`0053c7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c7f0.md) FUN_0053c7f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0053c990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c990.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0053c990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb110.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053c898",
      "incomplete_value": true,
      "site": "0053c89c",
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
      "definition_site": "0053c898",
      "incomplete_value": true,
      "site": "0053c89c",
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
      "0053c820",
      "READ",
      [
        "storage",
        "00c1ad98",
        null,
        "pointer"
      ]
    ],
    [
      "0053c828",
      "READ",
      [
        "storage",
        "00c1acc8",
        null,
        "pointer"
      ]
    ],
    [
      "0053c83c",
      "READ",
      [
        "storage",
        "00c13360",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0053c820",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "0053c828",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "0053c83c",
      "READ",
      [
        "storage",
        "00c13410",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c7f0.md#insn-0053c820) · [`0053c828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c7f0.md#insn-0053c828) · [`0053c894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c7f0.md#insn-0053c894)
- 新版 [`0053c820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c7f0.md#insn-0053c820) · [`0053c828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c7f0.md#insn-0053c828) · [`0053c894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c7f0.md#insn-0053c894)

~~~diff
- 0053c820 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:d98:8"]]
- 0053c820 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053c820 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:e48:8"]]
+ 0053c820 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c820 bytes 39cf46f9
+ 0053c820 bytes 392747f9
- 0053c828 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:cc8:8"]]
- 0053c828 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053c828 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:d78:8"]]
+ 0053c828 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c828 bytes 186746f9
+ 0053c828 bytes 18bf46f9
- 0053c894 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cd0:8"]]
- 0053c894 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053c894 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d80:8"]]
+ 0053c894 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c894 bytes b56a46f9
+ 0053c894 bytes b5c246f9
~~~


<a id="compare-bfcb4d612504f06988e3e84764d488b7"></a>

### [`0053c990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c990.md) → [`0053c990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c990.md) FUN_0053c990

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053c7f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c7f0.md) · 呼出先 6件 [`004365f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb2b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2b0.md) [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md)
- 新版 呼出元 1件 [`0053c7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c7f0.md) · 呼出先 6件 [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb360.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.28% / 新版 97.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053c9fc",
      "incomplete_value": true,
      "site": "0053ca00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c9fc",
      "incomplete_value": true,
      "site": "0053ca00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
              ]
            ]
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
      "definition_site": "0053ca58",
      "incomplete_value": true,
      "site": "0053ca5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ca58",
      "incomplete_value": true,
      "site": "0053ca5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053caa8",
      "incomplete_value": true,
      "site": "0053caac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053caa8",
      "incomplete_value": true,
      "site": "0053caac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
              ]
            ]
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
      "0053c9fc",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ],
    [
      "0053c9fc",
      "PARAM",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "0053ca58",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053c9fc",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "0053c9fc",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "0053ca58",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c9fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c990.md#insn-0053c9fc) · [`0053ca58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c990.md#insn-0053ca58) · [`0053caa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c990.md#insn-0053caa8)
- 新版 [`0053c9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c990.md#insn-0053c9fc) · [`0053ca58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c990.md#insn-0053ca58) · [`0053caa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c990.md#insn-0053caa8)

~~~diff
- 0053c9fc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d40:8"]]
- 0053c9fc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053c9fc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
+ 0053c9fc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c9fc bytes 21a046f9
+ 0053c9fc bytes 21f846f9
- 0053ca58 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d40:8"]]
- 0053ca58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053ca58 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
+ 0053ca58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0053ca58 bytes 21a046f9
+ 0053ca58 bytes 21f846f9
- 0053caa8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d40:8"]]
- 0053caa8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053caa8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
+ 0053caa8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0053caa8 bytes 21a046f9
+ 0053caa8 bytes 21f846f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ea764f059bc19106b3fd7a7a2a8bac9"></a>

### [`0053d168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d168.md) → [`0053d168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d168.md) FUN_0053d168

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0053d080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d080.md) [`005748e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/005748e4.md) · 呼出先 4件 [`00525380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/00525380.md) [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2a0.md) [`00bdb4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb4e0.md)
- 新版 呼出元 2件 [`0053d080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d080.md) [`005748e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005748e4.md) · 呼出先 4件 [`00525380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525380.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb350.md) [`00bdb590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb590.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 80.70% / 新版 80.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053d1ac",
      "incomplete_value": true,
      "site": "0053d1ac",
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
      "definition_site": "0053d1ac",
      "incomplete_value": true,
      "site": "0053d1ac",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053d1a4",
      "incomplete_value": true,
      "site": "0053d1b0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0053d1a4",
      "incomplete_value": true,
      "site": "0053d1b0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0053d1bc",
      "incomplete_value": true,
      "site": "0053d1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "definition_site": "0053d1bc",
      "incomplete_value": true,
      "site": "0053d1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
    "ordinal": 14,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0053d18c",
      "READ",
      [
        "storage",
        "00c1b3a0",
        null,
        "pointer"
      ]
    ],
    [
      "0053d190",
      "READ",
      [
        "storage",
        "00c1b398",
        null,
        "pointer"
      ]
    ],
    [
      "0053d1a4",
      "READ",
      [
        "storage",
        "00c133d0",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0053d18c",
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ],
    [
      "0053d190",
      "READ",
      [
        "storage",
        "00c1b448",
        null,
        "pointer"
      ]
    ],
    [
      "0053d1a4",
      "READ",
      [
        "storage",
        "00c13480",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d18c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d168.md#insn-0053d18c) · [`0053d190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d168.md#insn-0053d190) · [`0053d204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d168.md#insn-0053d204)
- 新版 [`0053d18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d168.md#insn-0053d18c) · [`0053d190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d168.md#insn-0053d190) · [`0053d204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d168.md#insn-0053d204)

~~~diff
- 0053d18c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:3a0:8"]]
- 0053d18c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053d18c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:450:8"]]
+ 0053d18c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d18c bytes 39d341f9
+ 0053d18c bytes 392b42f9
- 0053d190 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:398:8"]]
- 0053d190 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053d190 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:448:8"]]
+ 0053d190 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d190 bytes 18cf41f9
+ 0053d190 bytes 182742f9
- 0053d204 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
- 0053d204 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053d204 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 0053d204 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d204 bytes 086946f9
+ 0053d204 bytes 08c146f9
~~~


<a id="compare-bd29b99a21e156bcbdba413d328d6619"></a>

### [`0053d294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d294.md) → [`0053d294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d294.md) FUN_0053d294

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053d080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d080.md) · 呼出先 6件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 1件 [`0053d080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d080.md) · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.98% / 新版 97.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053d304",
      "incomplete_value": true,
      "site": "0053d308",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d304",
      "incomplete_value": true,
      "site": "0053d308",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:d40:8"
              ]
            ]
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
      "definition_site": "0053d3bc",
      "incomplete_value": true,
      "site": "0053d3c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d3bc",
      "incomplete_value": true,
      "site": "0053d3c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "0053d304",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ],
    [
      "0053d304",
      "PARAM",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "0053d3bc",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053d304",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "0053d304",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "0053d3bc",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d294.md#insn-0053d304) · [`0053d3bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d294.md#insn-0053d3bc)
- 新版 [`0053d304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d294.md#insn-0053d304) · [`0053d3bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d294.md#insn-0053d3bc)

~~~diff
- 0053d304 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d40:8"]]
- 0053d304 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053d304 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
+ 0053d304 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d304 bytes 21a046f9
+ 0053d304 bytes 21f846f9
- 0053d3bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d40:8"]]
- 0053d3bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053d3bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
+ 0053d3bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d3bc bytes 21a046f9
+ 0053d3bc bytes 21f846f9
~~~


<a id="compare-8aad00ad051a0f500ae5f23416d9e7af"></a>

### [`0053d46c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d46c.md) → [`0053d46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d46c.md) FUN_0053d46c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb070.md) [`00bdc8c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc8c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb120.md) [`00bdc970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc970.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 67.74% / 新版 67.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053d490",
      "incomplete_value": true,
      "site": "0053d498",
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
      "definition_site": "0053d490",
      "incomplete_value": true,
      "site": "0053d498",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0053d4a4",
      "incomplete_value": true,
      "site": "0053d4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "definition_site": "0053d4a4",
      "incomplete_value": true,
      "site": "0053d4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053d4a4",
      "incomplete_value": true,
      "site": "0053d4a4",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d4a4",
      "incomplete_value": true,
      "site": "0053d4a4",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
              ]
            ]
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
      "0053d488",
      "READ",
      [
        "storage",
        "00c1b398",
        null,
        "pointer"
      ]
    ],
    [
      "0053d490",
      "READ",
      [
        "storage",
        "00c133c8",
        "_ZTTNSt6__ndk119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0053d494",
      "READ",
      [
        "storage",
        "00c133e0",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "0053d488",
      "READ",
      [
        "storage",
        "00c1b448",
        null,
        "pointer"
      ]
    ],
    [
      "0053d490",
      "READ",
      [
        "storage",
        "00c13478",
        "_ZTTNSt6__ndk119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0053d494",
      "READ",
      [
        "storage",
        "00c13490",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d46c.md#insn-0053d488) · [`0053d48c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d46c.md#insn-0053d48c)
- 新版 [`0053d488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d46c.md#insn-0053d488) · [`0053d48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d46c.md#insn-0053d48c)

~~~diff
- 0053d488 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:398:8"]]
- 0053d488 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053d488 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:448:8"]]
+ 0053d488 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d488 bytes b5ce41f9
+ 0053d488 bytes b52642f9
- 0053d48c ["COPY", "register:4098:8", ["register:4000:8"]]
- 0053d48c bytes f30300aa
+ 0053d48c ["COPY", "register:4098:8", ["register:4000:8"]]
+ 0053d48c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9edc0f33e59c9f6ed2e33d17515644f1"></a>

### [`0053d4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d4e8.md) → [`0053d4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d4e8.md) FUN_0053d4e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0053c6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c6a0.md) [`0053c740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c740.md) · 呼出先 2件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb460.md)
- 新版 呼出元 2件 [`0053c6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c6a0.md) [`0053c740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c740.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053d4f8",
      "incomplete_value": false,
      "site": "0053d500",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d4f8",
      "incomplete_value": false,
      "site": "0053d500",
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
            "const:cb0:8"
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
      "0053d4f8",
      "PARAM",
      [
        "storage",
        "00c25cb0",
        null,
        null
      ]
    ],
    [
      "0053d520",
      "DATA",
      [
        "storage",
        "00bee160",
        null,
        "undefined *"
      ]
    ],
    [
      "0053d52c",
      "DATA",
      [
        "storage",
        "00bee0d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053d4f8",
      "PARAM",
      [
        "storage",
        "00c25d70",
        null,
        null
      ]
    ],
    [
      "0053d520",
      "DATA",
      [
        "storage",
        "00bee210",
        null,
        "undefined *"
      ]
    ],
    [
      "0053d52c",
      "DATA",
      [
        "storage",
        "00bee188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d4f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d4e8.md#insn-0053d4f8) · [`0053d514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d4e8.md#insn-0053d514) · [`0053d51c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d4e8.md#insn-0053d51c)
- 新版 [`0053d4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d4e8.md#insn-0053d4f8) · [`0053d514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d4e8.md#insn-0053d514) · [`0053d51c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d4e8.md#insn-0053d51c)

~~~diff
- 0053d4f8 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 0053d4f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053d4f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053d4f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053d4f8 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 0053d4f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053d4f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053d4f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053d4f8 bytes 00c03291
+ 0053d4f8 bytes 00c03591
- 0053d514 ["COPY", "tmp:0:8", ["const:160:8"]]
- 0053d514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053d514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053d514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053d514 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0053d514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053d514 bytes 08810591
+ 0053d514 bytes 08410891
- 0053d51c ["COPY", "tmp:0:8", ["const:d8:8"]]
- 0053d51c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053d51c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053d51c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053d51c ["COPY", "tmp:0:8", ["const:188:8"]]
+ 0053d51c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053d51c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053d51c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053d51c bytes 29610391
+ 0053d51c bytes 29210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eda6798b4341f93dc5dd012b037a060e"></a>

### [`0053d86c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d86c.md) → [`0053d86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d86c.md) FUN_0053d86c

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
      "definition_site": "0053d870",
      "incomplete_value": false,
      "site": "0053d874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d870",
      "incomplete_value": false,
      "site": "0053d874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "0053d874",
      "DATA",
      [
        "storage",
        "00bee160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053d874",
      "DATA",
      [
        "storage",
        "00bee210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d86c.md#insn-0053d870)
- 新版 [`0053d870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d86c.md#insn-0053d870)

~~~diff
- 0053d870 ["COPY", "tmp:0:8", ["const:160:8"]]
- 0053d870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053d870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053d870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053d870 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0053d870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053d870 bytes 08810591
+ 0053d870 bytes 08410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c323d8100bfa203bfac20e674b4ab1e"></a>

### [`0053d87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d87c.md) → [`0053d87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d87c.md) FUN_0053d87c

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
      "definition_site": "0053d88c",
      "incomplete_value": false,
      "site": "0053d894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d88c",
      "incomplete_value": false,
      "site": "0053d894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "0053d894",
      "DATA",
      [
        "storage",
        "00bee160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053d894",
      "DATA",
      [
        "storage",
        "00bee210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d88c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d87c.md#insn-0053d88c)
- 新版 [`0053d88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d87c.md#insn-0053d88c)

~~~diff
- 0053d88c ["COPY", "tmp:0:8", ["const:160:8"]]
- 0053d88c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053d88c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053d88c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053d88c ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0053d88c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d88c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d88c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053d88c bytes 08810591
+ 0053d88c bytes 08410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f254d2797d8a65f5a98cd13fd98c5af3"></a>

### [`0053d8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d8b4.md) → [`0053d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d8b4.md) _INIT_26

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b7dddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dddc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb450.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b7dea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dea4.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.93% / 新版 82.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053d8f0",
      "incomplete_value": true,
      "site": "0053d8f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0053d8f0",
      "incomplete_value": true,
      "site": "0053d8f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053d8fc",
      "incomplete_value": false,
      "site": "0053d904",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d8fc",
      "incomplete_value": false,
      "site": "0053d904",
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
            "const:cb0:8"
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
      "definition_site": "0053d924",
      "incomplete_value": true,
      "site": "0053d930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d924",
      "incomplete_value": true,
      "site": "0053d930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0053d8d4",
      "READ",
      [
        "storage",
        "002a8135",
        null,
        "string"
      ]
    ],
    [
      "0053d8fc",
      "PARAM",
      [
        "storage",
        "00c25cb0",
        null,
        null
      ]
    ],
    [
      "0053d920",
      "PARAM",
      [
        "storage",
        "00c25cb0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053d8d4",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ],
    [
      "0053d8fc",
      "PARAM",
      [
        "storage",
        "00c25d70",
        null,
        null
      ]
    ],
    [
      "0053d920",
      "PARAM",
      [
        "storage",
        "00c25d70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d8cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d8b4.md#insn-0053d8cc) · [`0053d8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d8b4.md#insn-0053d8fc) · [`0053d920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d8b4.md#insn-0053d920)
- 新版 [`0053d8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d8b4.md#insn-0053d8cc) · [`0053d8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d8b4.md#insn-0053d8fc) · [`0053d920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d8b4.md#insn-0053d920)

~~~diff
- 0053d8cc ["COPY", "tmp:0:8", ["const:135:8"]]
- 0053d8cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0053d8cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0053d8cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0053d8cc ["COPY", "tmp:0:8", ["const:a1:8"]]
+ 0053d8cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0053d8cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0053d8cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0053d8cc bytes 4ad50491
+ 0053d8cc bytes 4a850291
- 0053d8fc ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 0053d8fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053d8fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053d8fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053d8fc ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 0053d8fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053d8fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053d8fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053d8fc bytes 00c03291
+ 0053d8fc bytes 00c03591
- 0053d920 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 0053d920 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0053d920 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0053d920 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0053d920 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 0053d920 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0053d920 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0053d920 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0053d920 bytes 21c03291
+ 0053d920 bytes 21c03591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1476d2244aae1344ca2c865830dd1b2"></a>

### [`0053d984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d984.md) → [`0053d984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d984.md) FUN_0053d984

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 12件 [`004508a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/004508a4.md) [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) [`0084e0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084e/0084e0c0.md) [`008fc35c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc35c.md) [`008fcaf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fcaf4.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 12件 [`004508a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/004508a4.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`0084e0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e0c0.md) [`008fc35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc35c.md) [`008fcaf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fcaf4.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0053d9a0",
      "incomplete_value": false,
      "site": "0053d9a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d9a0",
      "incomplete_value": false,
      "site": "0053d9a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:210:8"
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
      "definition_site": "0053d9b8",
      "incomplete_value": false,
      "site": "0053d9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d9b8",
      "incomplete_value": false,
      "site": "0053d9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "0053d9a8",
      "DATA",
      [
        "storage",
        "00bee210",
        null,
        "undefined *"
      ]
    ],
    [
      "0053d9b8",
      "DATA",
      [
        "storage",
        "00bee260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053d9a8",
      "DATA",
      [
        "storage",
        "00bee2c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0053d9b8",
      "DATA",
      [
        "storage",
        "00bee310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d984.md#insn-0053d9a0) · [`0053d9ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d984.md#insn-0053d9ac)
- 新版 [`0053d9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d984.md#insn-0053d9a0) · [`0053d9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d984.md#insn-0053d9ac)

~~~diff
- 0053d9a0 ["COPY", "tmp:0:8", ["const:210:8"]]
- 0053d9a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053d9a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053d9a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053d9a0 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 0053d9a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d9a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d9a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053d9a0 bytes 08410891
+ 0053d9a0 bytes 08010b91
- 0053d9ac ["COPY", "register:4040:8", ["const:bee000:8"]]
- 0053d9ac bytes 883500b0
+ 0053d9ac ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 0053d9ac bytes 883500b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6997505a18bb9997940d417c93e5c6b2"></a>

### [`0053d9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d9cc.md) → [`0053d9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d9cc.md) FUN_0053d9cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0052db3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db3c.md) [`0053df70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053df70.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0052db3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db3c.md) [`0053df70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053df70.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0053da64",
      "incomplete_value": false,
      "site": "0053da64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053da64",
      "incomplete_value": false,
      "site": "0053da64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "0053da64",
      "DATA",
      [
        "storage",
        "00bee2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0053dae4",
      "READ",
      [
        "storage",
        "00bee2d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053da64",
      "DATA",
      [
        "storage",
        "00bee360",
        null,
        "undefined *"
      ]
    ],
    [
      "0053dae4",
      "READ",
      [
        "storage",
        "00bee388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053da5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d9cc.md#insn-0053da5c)
- 新版 [`0053da5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d9cc.md#insn-0053da5c)

~~~diff
- 0053da5c ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 0053da5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053da5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053da5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053da5c ["COPY", "tmp:0:8", ["const:360:8"]]
+ 0053da5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053da5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053da5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053da5c bytes 08c10a91
+ 0053da5c bytes 08810d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f378ffa51275da2690cd0973a9d9621e"></a>

### [`0053dc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dc90.md) → [`0053dc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dc90.md) FUN_0053dc90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0053dca8",
      "incomplete_value": false,
      "site": "0053dcac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053dca8",
      "incomplete_value": false,
      "site": "0053dcac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "0053dcac",
      "DATA",
      [
        "storage",
        "00bee1b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053dcac",
      "DATA",
      [
        "storage",
        "00bee260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053dca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dc90.md#insn-0053dca8)
- 新版 [`0053dca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dc90.md#insn-0053dca8)

~~~diff
- 0053dca8 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 0053dca8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053dca8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053dca8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053dca8 ["COPY", "tmp:0:8", ["const:260:8"]]
+ 0053dca8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053dca8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053dca8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053dca8 bytes 29c10691
+ 0053dca8 bytes 29810991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1191b4229025e113f57f6829fdeccfb3"></a>

### [`0053dce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dce0.md) → [`0053dce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dce0.md) FUN_0053dce0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0053dcf8",
      "incomplete_value": false,
      "site": "0053dcfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053dcf8",
      "incomplete_value": false,
      "site": "0053dcfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "0053dcfc",
      "DATA",
      [
        "storage",
        "00bee1b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053dcfc",
      "DATA",
      [
        "storage",
        "00bee260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053dcf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dce0.md#insn-0053dcf8)
- 新版 [`0053dcf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dce0.md#insn-0053dcf8)

~~~diff
- 0053dcf8 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 0053dcf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053dcf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053dcf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053dcf8 ["COPY", "tmp:0:8", ["const:260:8"]]
+ 0053dcf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053dcf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053dcf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053dcf8 bytes 29c10691
+ 0053dcf8 bytes 29810991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b5c330cf1c810daeeb1fe1907392201"></a>

### [`0053dd34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dd34.md) → [`0053dd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd34.md) FUN_0053dd34

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
      "definition_site": "0053dd38",
      "incomplete_value": false,
      "site": "0053dd3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053dd38",
      "incomplete_value": false,
      "site": "0053dd3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "0053dd3c",
      "DATA",
      [
        "storage",
        "00bee210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053dd3c",
      "DATA",
      [
        "storage",
        "00bee2c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053dd38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dd34.md#insn-0053dd38)
- 新版 [`0053dd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd34.md#insn-0053dd38)

~~~diff
- 0053dd38 ["COPY", "tmp:0:8", ["const:210:8"]]
- 0053dd38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053dd38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053dd38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053dd38 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 0053dd38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053dd38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053dd38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053dd38 bytes 08410891
+ 0053dd38 bytes 08010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f0947cdf0331fba023b5020d0a0965d"></a>

### [`0053dd44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dd44.md) → [`0053dd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd44.md) FUN_0053dd44

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
      "definition_site": "0053dd54",
      "incomplete_value": false,
      "site": "0053dd5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053dd54",
      "incomplete_value": false,
      "site": "0053dd5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "0053dd5c",
      "DATA",
      [
        "storage",
        "00bee210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053dd5c",
      "DATA",
      [
        "storage",
        "00bee2c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053dd54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dd44.md#insn-0053dd54)
- 新版 [`0053dd54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd44.md#insn-0053dd54)

~~~diff
- 0053dd54 ["COPY", "tmp:0:8", ["const:210:8"]]
- 0053dd54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053dd54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053dd54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053dd54 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 0053dd54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053dd54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053dd54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053dd54 bytes 08410891
+ 0053dd54 bytes 08010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-308ba041a35c77fc1a566f474820e99a"></a>

### [`0053dde0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dde0.md) → [`0053dde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dde0.md) FUN_0053dde0

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
      "definition_site": "0053ddf8",
      "incomplete_value": false,
      "site": "0053de04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ddf8",
      "incomplete_value": false,
      "site": "0053de04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "0053de04",
      "DATA",
      [
        "storage",
        "00bee2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053de04",
      "DATA",
      [
        "storage",
        "00bee360",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ddf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dde0.md#insn-0053ddf8)
- 新版 [`0053ddf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dde0.md#insn-0053ddf8)

~~~diff
- 0053ddf8 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 0053ddf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053ddf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053ddf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053ddf8 ["COPY", "tmp:0:8", ["const:360:8"]]
+ 0053ddf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053ddf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053ddf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053ddf8 bytes 08c10a91
+ 0053ddf8 bytes 08810d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eceb5cc68d4f0e4ad174adda245f6f62"></a>

### [`0053de3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053de3c.md) → [`0053de3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053de3c.md) FUN_0053de3c

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
      "definition_site": "0053de68",
      "incomplete_value": false,
      "site": "0053de68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053de68",
      "incomplete_value": false,
      "site": "0053de68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "0053de68",
      "DATA",
      [
        "storage",
        "00bee2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053de68",
      "DATA",
      [
        "storage",
        "00bee360",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053de60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053de3c.md#insn-0053de60)
- 新版 [`0053de60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053de3c.md#insn-0053de60)

~~~diff
- 0053de60 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 0053de60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053de60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053de60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053de60 ["COPY", "tmp:0:8", ["const:360:8"]]
+ 0053de60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053de60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053de60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053de60 bytes 08c10a91
+ 0053de60 bytes 08810d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d361e1a94891bef00e28121416ab74bc"></a>

### [`0053dec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dec4.md) → [`0053dec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dec4.md) FUN_0053dec4

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
      "definition_site": "0053dee0",
      "incomplete_value": true,
      "site": "0053dee0",
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
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053dee0",
      "incomplete_value": true,
      "site": "0053dee0",
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
      "0053dee0",
      "DATA",
      [
        "storage",
        "00bee2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053dee0",
      "DATA",
      [
        "storage",
        "00bee360",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053dedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dec4.md#insn-0053dedc)
- 新版 [`0053dedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dec4.md#insn-0053dedc)

~~~diff
- 0053dedc ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 0053dedc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053dedc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053dedc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053dedc ["COPY", "tmp:0:8", ["const:360:8"]]
+ 0053dedc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053dedc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053dedc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053dedc bytes 29c10a91
+ 0053dedc bytes 29810d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d667a910448b1797287f36197cca9369"></a>

### [`0053e008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e008.md) → [`0053e008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e008.md) FUN_0053e008

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053dc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dc30.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`0053dc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dc30.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

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
      "definition_site": "0053e020",
      "incomplete_value": false,
      "site": "0053e020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e020",
      "incomplete_value": false,
      "site": "0053e020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:330:8"
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
      "definition_site": "0053e02c",
      "incomplete_value": false,
      "site": "0053e02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e02c",
      "incomplete_value": false,
      "site": "0053e02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "0053e020",
      "DATA",
      [
        "storage",
        "00bee330",
        null,
        "undefined *"
      ]
    ],
    [
      "0053e02c",
      "DATA",
      [
        "storage",
        "00bee1b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053e020",
      "DATA",
      [
        "storage",
        "00bee3e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0053e02c",
      "DATA",
      [
        "storage",
        "00bee260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e008.md#insn-0053e018) · [`0053e024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e008.md#insn-0053e024)
- 新版 [`0053e018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e008.md#insn-0053e018) · [`0053e024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e008.md#insn-0053e024)

~~~diff
- 0053e018 ["COPY", "tmp:0:8", ["const:330:8"]]
- 0053e018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053e018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053e018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053e018 ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 0053e018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053e018 bytes 08c10c91
+ 0053e018 bytes 08810f91
- 0053e024 ["COPY", "register:4040:8", ["const:bee000:8"]]
- 0053e024 bytes 88350090
+ 0053e024 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 0053e024 bytes 88350090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-250f19caa573051d7be0d11df0f0aeee"></a>

### [`0053e0bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e0bc.md) → [`0053e0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0bc.md) FUN_0053e0bc

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
      "definition_site": "0053e0c0",
      "incomplete_value": false,
      "site": "0053e0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e0c0",
      "incomplete_value": false,
      "site": "0053e0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:330:8"
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
      "0053e0c4",
      "DATA",
      [
        "storage",
        "00bee330",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053e0c4",
      "DATA",
      [
        "storage",
        "00bee3e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e0bc.md#insn-0053e0c0)
- 新版 [`0053e0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0bc.md#insn-0053e0c0)

~~~diff
- 0053e0c0 ["COPY", "tmp:0:8", ["const:330:8"]]
- 0053e0c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053e0c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053e0c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053e0c0 ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 0053e0c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e0c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e0c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053e0c0 bytes 08c10c91
+ 0053e0c0 bytes 08810f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2a9faebfbc97fb50b3e82c7d3defcf4"></a>

### [`0053e0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e0cc.md) → [`0053e0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0cc.md) FUN_0053e0cc

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
      "definition_site": "0053e0dc",
      "incomplete_value": false,
      "site": "0053e0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e0dc",
      "incomplete_value": false,
      "site": "0053e0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:330:8"
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
      "0053e0e4",
      "DATA",
      [
        "storage",
        "00bee330",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053e0e4",
      "DATA",
      [
        "storage",
        "00bee3e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e0dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e0cc.md#insn-0053e0dc)
- 新版 [`0053e0dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0cc.md#insn-0053e0dc)

~~~diff
- 0053e0dc ["COPY", "tmp:0:8", ["const:330:8"]]
- 0053e0dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053e0dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053e0dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053e0dc ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 0053e0dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e0dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e0dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053e0dc bytes 08c10c91
+ 0053e0dc bytes 08810f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96810a5e63a739ae42c798479b89fe56"></a>

### [`0053e1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e1dc.md) → [`0053e1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e1dc.md) FUN_0053e1dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00431534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431534.md) [`00433930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00433/00433930.md) · 呼出先 14件 [`0053c6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c6a0.md) [`00574738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574738.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 2件 [`00431534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431534.md) [`00433930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/00433930.md) · 呼出先 14件 [`0053c6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c6a0.md) [`00574738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574738.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "0053e234",
      "incomplete_value": false,
      "site": "0053e240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:861:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e234",
      "incomplete_value": false,
      "site": "0053e240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:868:8"
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
      "definition_site": "0053e4c4",
      "incomplete_value": false,
      "site": "0053e4cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e4c4",
      "incomplete_value": false,
      "site": "0053e4cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:633:8"
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
      "definition_site": "0053e564",
      "incomplete_value": false,
      "site": "0053e568",
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
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e564",
      "incomplete_value": false,
      "site": "0053e568",
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
            "const:6d7:8"
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
      "0053e234",
      "PARAM",
      [
        "storage",
        "002a6868",
        null,
        "string"
      ]
    ],
    [
      "0053e2fc",
      "PARAM",
      [
        "storage",
        "002aa700",
        null,
        "string"
      ]
    ],
    [
      "0053e318",
      "READ",
      [
        "storage",
        "002a3170",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053e234",
      "PARAM",
      [
        "storage",
        "002a6861",
        null,
        "string"
      ]
    ],
    [
      "0053e2fc",
      "PARAM",
      [
        "storage",
        "002aa706",
        null,
        "string"
      ]
    ],
    [
      "0053e318",
      "READ",
      [
        "storage",
        "002a3169",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e1dc.md#insn-0053e234) · [`0053e2fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e1dc.md#insn-0053e2fc) · [`0053e310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e1dc.md#insn-0053e310)
- 新版 [`0053e234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e1dc.md#insn-0053e234) · [`0053e2fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e1dc.md#insn-0053e2fc) · [`0053e310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e1dc.md#insn-0053e310)

~~~diff
- 0053e234 ["COPY", "tmp:0:8", ["const:868:8"]]
- 0053e234 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0053e234 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0053e234 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0053e234 ["COPY", "tmp:0:8", ["const:861:8"]]
+ 0053e234 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0053e234 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0053e234 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0053e234 bytes 42a02191
+ 0053e234 bytes 42842191
- 0053e2fc ["COPY", "tmp:0:8", ["const:700:8"]]
- 0053e2fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053e2fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053e2fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053e2fc ["COPY", "tmp:0:8", ["const:706:8"]]
+ 0053e2fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053e2fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053e2fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053e2fc bytes 00001c91
+ 0053e2fc bytes 00181c91
- 0053e310 ["COPY", "tmp:0:8", ["const:170:8"]]
- 0053e310 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053e310 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053e310 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053e310 ["COPY", "tmp:0:8", ["const:169:8"]]
+ 0053e310 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053e310 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053e310 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053e310 bytes 29c10591
+ 0053e310 bytes 29a50591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-447e750fdf17fc290789ef1b0f379fbb"></a>

### [`0053e9d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e9d0.md) → [`0053e9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e9d0.md) FUN_0053e9d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00431534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431534.md) [`00433930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00433/00433930.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 2件 [`00431534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431534.md) [`00433930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/00433930.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0053e9ec",
      "incomplete_value": false,
      "site": "0053e9f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e9ec",
      "incomplete_value": false,
      "site": "0053e9f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:380:8"
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
      "0053e9f4",
      "DATA",
      [
        "storage",
        "00bee380",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053e9f4",
      "DATA",
      [
        "storage",
        "00bee430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e9ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e9d0.md#insn-0053e9ec)
- 新版 [`0053e9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e9d0.md#insn-0053e9ec)

~~~diff
- 0053e9ec ["COPY", "tmp:0:8", ["const:380:8"]]
- 0053e9ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053e9ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053e9ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053e9ec ["COPY", "tmp:0:8", ["const:430:8"]]
+ 0053e9ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e9ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e9ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053e9ec bytes 08010e91
+ 0053e9ec bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d5cc64cd756a6422fad7845c72d06f0"></a>

### [`0053ea14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ea14.md) → [`0053ea14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ea14.md) FUN_0053ea14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008a1458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a2/008a2cac.md) · 呼出先 5件 [`0053d588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d588.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`008a1458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a2/008a2cac.md) · 呼出先 5件 [`0053d588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d588.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

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
      "definition_site": "0053ea90",
      "incomplete_value": false,
      "site": "0053ea98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:5d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ea90",
      "incomplete_value": false,
      "site": "0053ea98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "0053ea74",
      "PARAM",
      [
        "storage",
        "00298c4e",
        null,
        null
      ]
    ],
    [
      "0053ea90",
      "PARAM",
      [
        "storage",
        "002a45d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053ea74",
      "PARAM",
      [
        "storage",
        "00298cdb",
        null,
        null
      ]
    ],
    [
      "0053ea90",
      "PARAM",
      [
        "storage",
        "002a45d1",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ea74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ea14.md#insn-0053ea74) · [`0053ea90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ea14.md#insn-0053ea90)
- 新版 [`0053ea74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ea14.md#insn-0053ea74) · [`0053ea90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ea14.md#insn-0053ea90)

~~~diff
- 0053ea74 ["COPY", "tmp:0:8", ["const:c4e:8"]]
- 0053ea74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0053ea74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0053ea74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0053ea74 ["COPY", "tmp:0:8", ["const:cdb:8"]]
+ 0053ea74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0053ea74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0053ea74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0053ea74 bytes 21383191
+ 0053ea74 bytes 216c3391
- 0053ea90 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 0053ea90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0053ea90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0053ea90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0053ea90 ["COPY", "tmp:0:8", ["const:5d1:8"]]
+ 0053ea90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0053ea90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0053ea90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0053ea90 bytes 21601791
+ 0053ea90 bytes 21441791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a4ce97915a893024af61e3c95d0e409"></a>

### [`0053ec4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ec4c.md) → [`0053ec4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ec4c.md) FUN_0053ec4c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008a1458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a2/008a2cac.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb210.md)
- 新版 呼出元 2件 [`008a1458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a2/008a2cac.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2c0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053ec98",
      "incomplete_value": true,
      "site": "0053ec98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0053ec98",
      "incomplete_value": true,
      "site": "0053ec98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053ecb4",
      "incomplete_value": true,
      "site": "0053eccc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:aff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ecb4",
      "incomplete_value": true,
      "site": "0053eccc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:b93:8"
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
      "definition_site": "0053ecb4",
      "incomplete_value": true,
      "site": "0053eccc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0053ecb4",
      "incomplete_value": true,
      "site": "0053eccc",
      "value": [
        "LOAD",
        "16",
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
      "0053ec70",
      "READ",
      [
        "storage",
        "002a3170",
        null,
        "string"
      ]
    ],
    [
      "0053ecb4",
      "READ",
      [
        "storage",
        "002adb93",
        null,
        "string"
      ]
    ],
    [
      "0053ecb4",
      "READ",
      [
        "storage",
        "002adba3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053ec70",
      "READ",
      [
        "storage",
        "002a3169",
        null,
        "string"
      ]
    ],
    [
      "0053ecb4",
      "READ",
      [
        "storage",
        "002adaff",
        null,
        "string"
      ]
    ],
    [
      "0053ecb4",
      "READ",
      [
        "storage",
        "002adb0f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ec68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ec4c.md#insn-0053ec68) · [`0053ecac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ec4c.md#insn-0053ecac) · [`0053ecb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ec4c.md#insn-0053ecb0)
- 新版 [`0053ec68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ec4c.md#insn-0053ec68) · [`0053ecac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ec4c.md#insn-0053ecac)

~~~diff
- 0053ec68 ["COPY", "tmp:0:8", ["const:170:8"]]
- 0053ec68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0053ec68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0053ec68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0053ec68 ["COPY", "tmp:0:8", ["const:169:8"]]
+ 0053ec68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0053ec68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0053ec68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0053ec68 bytes 4ac10591
+ 0053ec68 bytes 4aa50591
- 0053ecac ["COPY", "tmp:0:8", ["const:b93:8"]]
- 0053ecac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0053ecac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0053ecac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0053ecac ["COPY", "tmp:0:8", ["const:aff:8"]]
+ 0053ecac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0053ecac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0053ecac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0053ecac bytes 4a4d2e91
+ 0053ecac bytes 4afd2b91
- 0053ecb0 ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 0053ecb0 bytes 88ebfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-843e04e1b191d6999940c0987b740363"></a>

### [`0053ee14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee14.md) → [`0053ee14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee14.md) FUN_0053ee14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`008a1458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a2/008a2cac.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 2件 [`008a1458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a2/008a2cac.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0053ee30",
      "incomplete_value": false,
      "site": "0053ee38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ee30",
      "incomplete_value": false,
      "site": "0053ee38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
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
      "0053ee38",
      "DATA",
      [
        "storage",
        "00bee3d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053ee38",
      "DATA",
      [
        "storage",
        "00bee480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ee30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee14.md#insn-0053ee30)
- 新版 [`0053ee30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee14.md#insn-0053ee30)

~~~diff
- 0053ee30 ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 0053ee30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053ee30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053ee30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053ee30 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 0053ee30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053ee30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053ee30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053ee30 bytes 08410f91
+ 0053ee30 bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-197ed2e9c62f216d16823a1230327638"></a>

### [`0053ee5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee5c.md) → [`0053ee5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) FUN_0053ee5c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 21件 [`0041b470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b470.md) [`0041ba38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041ba38.md) [`004222e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/004222e0.md) [`0042ca70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca70.md) [`0042ce34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ce34.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00540878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/00540878.md) [`0056244c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/0056244c.md) [`0057476c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/0057476c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 21件 [`0041b470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) [`0041ba38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041ba38.md) [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`0042ca70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca70.md) [`0042ce34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ce34.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00540878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540878.md) [`0056244c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/0056244c.md) [`0057476c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057476c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0053ef1c",
      "incomplete_value": false,
      "site": "0053ef1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ef1c",
      "incomplete_value": false,
      "site": "0053ef1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      "definition_site": "0053eea0",
      "incomplete_value": true,
      "site": "0053eea0",
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
      "definition_site": "0053eea0",
      "incomplete_value": true,
      "site": "0053eea0",
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
      "0053ee9c",
      "READ",
      [
        "storage",
        "00c25d00",
        null,
        "undefined8"
      ]
    ],
    [
      "0053ef1c",
      "DATA",
      [
        "storage",
        "00bee420",
        null,
        "undefined *"
      ]
    ],
    [
      "0053efa8",
      "READ",
      [
        "storage",
        "00bee448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053ee9c",
      "READ",
      [
        "storage",
        "00c25dc0",
        null,
        "undefined8"
      ]
    ],
    [
      "0053ef1c",
      "DATA",
      [
        "storage",
        "00bee4d0",
        null,
        "undefined *"
      ]
    ],
    [
      "0053efa8",
      "READ",
      [
        "storage",
        "00bee4f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ee9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee5c.md#insn-0053ee9c) · [`0053ef14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee5c.md#insn-0053ef14) · [`0053ef18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee5c.md#insn-0053ef18)
- 新版 [`0053ee9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md#insn-0053ee9c) · [`0053ef14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md#insn-0053ef14)

~~~diff
- 0053ee9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d00:8"]]
- 0053ee9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053ee9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dc0:8"]]
+ 0053ee9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0053ee9c bytes 298146f9
+ 0053ee9c bytes 29e146f9
- 0053ef14 ["COPY", "tmp:0:8", ["const:420:8"]]
- 0053ef14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053ef14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053ef14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053ef14 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 0053ef14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053ef14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053ef14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053ef14 bytes 29811091
+ 0053ef14 bytes 29411391
- 0053ef18 ["COPY", "register:40b8:8", ["register:4000:8"]]
- 0053ef18 bytes f70300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21f926d72f5990501bd8bc900caf2506"></a>

### [`0053f0f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053f/0053f0f8.md) → [`0053f0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f0f8.md) FUN_0053f0f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0041b470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b470.md) [`00435c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/00435c18.md) [`00949c4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949c4c.md) · 呼出先 10件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`0053f81c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053f/0053f81c.md) [`00541908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/00541908.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 3件 [`0041b470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) [`00435c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435c18.md) [`00949c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949c4c.md) · 呼出先 10件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`0053f81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f81c.md) [`00541908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00541/00541908.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0053f510",
      "incomplete_value": false,
      "site": "0053f51c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053f510",
      "incomplete_value": false,
      "site": "0053f51c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:560:8"
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
      "0053f51c",
      "DATA",
      [
        "storage",
        "00bee560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053f51c",
      "DATA",
      [
        "storage",
        "00bee610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053f510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053f/0053f0f8.md#insn-0053f510)
- 新版 [`0053f510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f0f8.md#insn-0053f510)

~~~diff
- 0053f510 ["COPY", "tmp:0:8", ["const:560:8"]]
- 0053f510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053f510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053f510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053f510 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 0053f510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053f510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053f510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053f510 bytes 08811591
+ 0053f510 bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

